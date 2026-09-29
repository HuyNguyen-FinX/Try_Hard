# Design High-Throughput API — 20,000 RPS

**Design lab:** các con số dưới đây là giả định để ước lượng, chưa phải kết quả benchmark. Khi phỏng vấn, xác nhận semantics và workload trước khi chọn hạ tầng.

## Requirements

Phục vụ API read/write với PostgreSQL làm authority, Redis cache derived reads, Kafka cho side effects async và Kubernetes cho stateless Go replicas. Mục tiêu20k RPS, P99<200ms; phân biệt accepted writes với side effects hoàn tất.

## Non-functional Requirements

Giả định90% reads,10% writes; read cache hit95%, mean request50ms; availability99.95% trong region. Durable write ack sau DB commit; cache có stale bound30s cho fields được phép. Không cache quyết định authorization/balance nếu cần authoritative.

## Capacity Estimation

20k×0.05=1000 mean in-flight requests toàn fleet theo Little's Law. 18k reads/s×5% misses=900 DB read ops/s, cộng2k writes/s →2900 logical DB ops/s nếu mỗi operation một query/Tx. Query count/Tx hold time thực tế có thể lớn hơn. Mean connection hold10ms →29 concurrent DB connections lý tưởng; burst, locks và distribution cần measured headroom. Response2KiB →~39MiB/s outbound trước TLS/headers. Event1KiB×2k/s≈1.95MiB/s, ~165GiB/day raw Kafka payload ở sustained rate, trước replication/index/retention.

## API

GET /v1/items/{id} với ETag/version; POST /v1/orders với Idempotency-Key; GET /v1/orders/{id} cho async status. Request body cap64KiB giả định; page cap100. Trả429 tenant quota,503 admission overload, deadline errors theo contract; không silently accept khi không durable.

## Data Model

items(id,tenant,version,updated_at,data) với indexes theo tenant+id; orders(unique tenant+idempotency_key,request_hash,state,version); outbox(event_id unique,aggregate_id,aggregate_version,payload,published_at). Cache key chứa entity/version strategy; Kafka key theo aggregate giữ order.

## High-Level Architecture

```mermaid
flowchart LR
    C[Clients 20k RPS] --> LB[Load balancer and edge limits]
    LB --> A[Go API pods with admission]
    A --> R[Redis cache]
    A --> P[PostgreSQL authority]
    P --> O[Outbox relay]
    O --> K[Kafka partitions]
    K --> W[Bounded Go consumers]
    A --> H[Shared outbound HTTP or gRPC clients]
```

## Request Flow

Request budget giả định 200ms: admission≤10ms, cache≤10ms, DB or dependency≤120ms, serialization/write≤30ms và30ms headroom; các budgets không phải mọi phase luôn thực thi. Child context không vượt parent. Chọn hit/miss/write paths riêng để latency histogram không che miss tail. Write trả sau transaction commit, side effects trả pending status nếu async.

```mermaid
sequenceDiagram
    participant C as Client
    participant A as Go API
    participant R as Redis
    participant P as PostgreSQL
    participant K as Outbox Relay and Kafka
    C->>A: Request with deadline and key
    A->>A: Auth, quota, acquire admission
    alt Read cache hit
        A->>R: Bounded lookup
        R-->>A: Value and version
    else Write or miss
        A->>P: Context-aware query or transaction
        P-->>A: Committed result
        P-->>K: Committed outbox asynchronously
    end
    A-->>C: Response before budget expires
```

## Data Flow

```mermaid
flowchart TD
    W[Write intent] --> T[Domain row and outbox in one Tx]
    T --> V[Versioned invalidation]
    T --> E[Stable event ID]
    E --> K[Kafka keyed partition]
    K --> D[Idempotent consumer Tx]
    D --> C[Contiguous offset commit]
    V --> R[Redis refresh with stampede control]
```

## Go Service Implementation

net/http handlers vốn concurrent; thêm semaphore trước expensive work, không spawn unlimited children. CPU-bound tasks theo effective GOMAXPROCS/quota; IO calls theo downstream budgets. Shared sql.DB, Redis client, http.Transport/grpc ClientConn; deadlines cho acquire và execute. Pool10/pod không tự đủ nếu Tx giữ100ms: capacity planning phải dùng hold time thật. Kafka consumers dùng bounded batches/per-key ordering, idempotent transaction và contiguous commit. SIGTERM readiness/drain, join workers rồi close pools. pprof private và trace propagation xuyên calls/events.

## Scaling

Planning example: nếu load test chứng minh1k RPS/pod ở latency target và acceptable saturation, cần20 pods steady plus failure/burst headroom; không lấy số này làm default. Giả định min24/max32 pods, pool10/pod →240..320 app DB connections, còn reserve workers/admin trong total server budget400 giả định. Rollout surge4 pods làm tổng360 trước workers; phải giảm caps hoặc tăng verified budget nếu không đủ. Redis và HTTP/gRPC pools có aggregate budget tương tự. HPA theo CPU cùng in-flight/queue indicators; DB wait cao CPU thấp cần admission, không scale mù.

```mermaid
flowchart TD
    LB[Multi-zone LB] --> Z1[Zone A Go replicas]
    LB --> Z2[Zone B Go replicas]
    H[HPA with max replica budget] --> Z1
    H --> Z2
    Z1 --> R[Redis shards and replicas]
    Z2 --> R
    Z1 --> DB[Postgres connection budget]
    Z2 --> DB
    K[Kafka partitions] --> W[Workers capped by sink capacity]
```

## Failure Modes

CPU saturation do JSON/TLS/compression, GC pressure do payload copies, lock contention local cache, DB slow query/lock, Redis stampede, Kafka lag, DNS failure, HPA/surge overbudget. 20k runnable G khác20k parked G; dùng CPU/trace/goroutine profile để tách.

## Failure Scenarios

Thử crash/network loss tại từng durable boundary ở request flow; kiểm tra invariant sau recovery, không chỉ việc service khởi động lại. Khi Redis down, hypothetical read DB demand nhảy từ900 lên18k/s: không cho toàn bộ fallback tự do. Local stale cache cho data được phép, per-route miss semaphore, shed low-priority load và protect DB. Kafka down: DB outbox vẫn nhận trong giới hạn storage/age đã định nghĩa; vượt bound thì reject writes cần event durability workflow.

```mermaid
flowchart TD
    S[Latency or cache failure] --> A[Reduce admission and pause backfill]
    A --> C{Read can be stale}
    C -->|yes| R[Serve bounded stale copy]
    C -->|no| B{DB capacity available}
    B -->|yes| Q[Bounded authoritative query]
    B -->|no| E[429 or 503 by policy]
    R --> V[Verify SLO and backlog recovery]
    Q --> V
```

## Observability

SLO tại edge gồm rejected/timed-out requests theo eligible policy. Per-route offered/accepted/completed RPS và P50/P95/P99, CPU/throttle, heap/alloc rate/GC assists, scheduler latency, DB acquire wait/hold time, Redis hit/miss/latency, Kafka oldest age và outbox backlog.

## How I would debug this in production

SLO tại edge gồm rejected/timed-out requests theo eligible policy. Per-route offered/accepted/completed RPS và P50/P95/P99, CPU/throttle, heap/alloc rate/GC assists, scheduler latency, DB acquire wait/hold time, Redis hit/miss/latency, Kafka oldest age và outbox backlog. Tách offered, accepted và completed rates; chọn dependency/queue đầu tiên lệch baseline. Thu profile đúng triệu chứng, đối chiếu trace với durable state theo operation ID. Sau mitigation kiểm tra cả SLO và backlog/reconciliation để tránh tuyên bố phục hồi quá sớm.

## Security

Tenant authz trên mọi DB/cache path; cache key chứa tenant; size/decompression limits; rate limits theo identity và global admission; private metrics/pprof; TLS/secret rotation không tạo reconnect herd.

## Trade-offs

| Option | Best for | Weakness |
|---|---|---|
| Cache reads | Giảm DB2900 ops/s theo assumptions | Staleness và miss storm |
| Async outbox | Bound request latency, durable intent | Lag/duplicate/reconciliation |
| Tight admission | Bảo vệ P99 và DB | Explicit rejects khi peak |
| More pods | Thêm app CPU | Nhân downstream pools |

## Evolution

1k RPS baseline: đo per-request work và fix N+1/reuse. 5k: load realistic cache misses, add bounds/SLO metrics. 10k: verify DB/query indexes và Kafka consumer headroom. 20k: multi-zone capacity test, one-zone-loss budget, Redis outage, rolling deploy và backlog recovery. Sharding chỉ sau profiling/query/schema fixes và primary capacity evidence.

## Interview rehearsal

1. What is the primary correctness invariant?
2. Which measured resource limits throughput first?
3. What happens if a response is lost after commit?
4. How would you handle a tenfold hot-key skew?
5. Which evidence would justify the next architectural change?

Trả lời bằng API semantics, capacity arithmetic và failure flow cụ thể của bài này. Một câu trả lời senior phải giải thích điểm commit, ownership trong Go, bounds của concurrency/pools và recovery cho unknown outcome.


## See also

- [capacity-estimation](capacity-estimation.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [Distributed idempotency và ambiguous outcomes](../12-distributed-systems/idempotency.md)
- [Transactional outbox](../12-distributed-systems/outbox-pattern.md)

## Load-test acceptance gates

- Generator phát offered load theo lịch độc lập khi cần để thấy queue growth; báo cả requests timeout/reject, không loại khỏi latency accounting tùy tiện.
- Warm cache, cold cache, 95% hit và Redis unavailable là bốn experiments riêng. Thêm skew một hot tenant/key, realistic auth/JSON payloads.
- Ramp1k→5k→10k→20k, giữ đủ lâu qua nhiều GC/HPA cycles; sau overload hạ tải và yêu cầu queue age/live heap/G count về plateau.
- Kill một pod, rollout với surge, làm DB query chậm10×, block Kafka publish; kiểm tra idempotent writes và outbox catch-up.
- Chỉ công nhận target khi P99<200ms, error/reject policy thỏa SLO, no lost durable writes và downstream không vượt budget. Không có benchmark20k RPS được chạy trong repository này; đây là thiết kế thí nghiệm.
