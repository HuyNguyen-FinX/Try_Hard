# Request Lifecycle

> **Phạm vi phỏng vấn:** FastAPI · **Ưu tiên:** P0/P1 · **Mindset:** Why → How → Trade-off → Production.

## 1. What is it?

Request đi qua proxy/ASGI server, middleware, routing, dependency resolution, validation, endpoint, serialization và response middleware.

## 2. Why does it matter?

Senior Engineer cần hiểu **Request Lifecycle** để xây API có contract rõ, concurrency đúng và vận hành an toàn. Điểm phỏng vấn nằm ở khả năng nêu invariant, điều kiện áp dụng và failure behavior, không nằm ở việc thuộc định nghĩa.

## 3. How does it work?

Context và resource scope phải kết thúc kể cả exception/cancellation; transaction không nên bao trùm network call và trace ID cần xuyên mọi lớp.

Khi reasoning, đi theo chuỗi: **input → state transition → output → failure → recovery**. Quan sát `RPS, p95/p99 latency, error rate, event-loop lag và pool utilization` và phân biệt symptom, bottleneck với root cause.

## 4. Example

```python
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

async def current_tenant() -> int:
    return 42

@app.get("/health/{component}")
async def health(component: str, tenant_id: int = Depends(current_tenant)) -> dict[str, object]:
    if component not in {"database", "cache", "queue"}:
        raise HTTPException(status_code=404, detail="unknown component")
    return {"component": component, "tenant_id": tenant_id, "healthy": True}
```

Ví dụ giữ I/O path non-blocking; production cần deadline, structured log và bounded pool cho **Request Lifecycle**.

## 5. Production Use Case

Dependency `yield` mở AsyncSession cho một request, commit ở service boundary, rollback khi lỗi và đóng session trước khi response connection được tái sử dụng.

Checklist triển khai: capacity budget, timeout, idempotency (nếu có side effect), telemetry, canary, rollback và reconciliation.

## 6. Common Problems

- Không định nghĩa invariant và source of truth trước khi chọn công nghệ.
- Retry không backoff/jitter làm traffic amplification khi dependency lỗi.
- Không có bound cho queue, connection, memory hoặc concurrency.
- Chỉ theo dõi average; bỏ qua p95/p99, saturation và error semantics.
- Rollout toàn bộ, thiếu feature flag/canary và đường rollback dữ liệu.

## 7. Trade-offs

| Lựa chọn | Lợi ích | Chi phí / rủi ro | Khi phù hợp |
|---|---|---|---|
| Tối ưu/thiết kế xoay quanh Request Lifecycle | Kiểm soát rõ constraint chính | Tăng complexity và coupling | Metric chứng minh đây là bottleneck/risk |
| Giữ baseline đơn giản | Ít dependency, dễ debug | Có thể chạm giới hạn sớm | Traffic vừa, invariant vẫn được giữ |
| Managed service/library | Giảm vận hành hạ tầng | Cost, lock-in, giới hạn control | SLA và economics phù hợp |
| Tự vận hành/customize | Kiểm soát sâu | Ownership và failure surface lớn | Có năng lực vận hành và nhu cầu thật |

## 8. Interview Questions

### Basic / Mid-level (10)

- **B1.** What is Request Lifecycle, and which concrete problem does it address?
- **B2.** Explain the main internal mechanism behind Request Lifecycle.
- **B3.** Which guarantees does Request Lifecycle provide, and which does it not provide?
- **B4.** Which metrics or observations reveal the behavior of Request Lifecycle?
- **B5.** What is the most common misconception about Request Lifecycle?
- **B6.** How would you test assumptions involving Request Lifecycle?
- **B7.** Which edge cases or failure modes matter most for Request Lifecycle?
- **B8.** How can Request Lifecycle affect latency, throughput, memory, or correctness?
- **B9.** Which runtime conditions or configuration choices change the behavior of Request Lifecycle?
- **B10.** When is a different or simpler approach better than relying on Request Lifecycle?

### Production Scenarios (5)

- **S1.** A release involving Request Lifecycle triples p99 while averages look normal. How do you investigate and mitigate?
- **S2.** A critical dependency around Request Lifecycle is unavailable for ten minutes. Define degraded behavior and recovery.
- **S3.** Two concurrent operations expose a correctness gap related to Request Lifecycle. Which invariant and atomic boundary fix it?
- **S4.** Traffic grows from 1,000 to 20,000 RPS. Which measured limit involving Request Lifecycle fails first?
- **S5.** A canary changes the behavior of Request Lifecycle; success rate is flat but saturation rises. Promote or roll back?

## 9. Senior-level Questions

- **L1.** How does Request Lifecycle constrain the surrounding architecture and operational model?
- **L2.** Which subtle correctness issue appears when Request Lifecycle meets concurrency or partial failure?
- **L3.** What breaks first around Request Lifecycle at 20,000 RPS or 100× data volume?
- **L4.** Where should admission control or backpressure be placed when using Request Lifecycle?
- **L5.** How would you benchmark or validate Request Lifecycle without a misleading microbenchmark?
- **L6.** Which hidden coupling or migration cost can Request Lifecycle introduce?
- **L7.** How would you change a poor decision around Request Lifecycle with no downtime?
- **L8.** What production evidence would make you choose a different approach?
- **L9.** How do correctness, latency, cost, and complexity trade off for Request Lifecycle?
- **L10.** How would you turn an incident involving Request Lifecycle into a durable prevention mechanism?

## 10. Short Answers

**B1.** Request đi qua proxy/ASGI server, middleware, routing, dependency resolution, validation, endpoint, serialization và response middleware. Trả lời tốt nối definition với constraint/invariant và một use case cụ thể.

**B2.** Mô tả state, lifecycle, boundary và failure path; không dừng ở public API của Request Lifecycle.

**B3.** Nêu lúc tạo, lúc sử dụng, lúc release/commit và điều xảy ra khi timeout hoặc cancellation.

**B4.** Đo RPS, p95/p99 latency, error rate, event-loop lag và pool utilization; luôn tách average khỏi tail và success khỏi useful result.

**B5.** Lỗi phổ biến là dùng Request Lifecycle như mặc định mà không xác định ownership, limit và fallback.

**B6.** Test invariant trước, sau đó integration test failure path, concurrency và representative load.

**B7.** Xét timeout, duplicate, stale state, overload, dependency loss và recovery/reconciliation.

**B8.** Đo critical path, contention, queueing và amplification; throughput cao không bù được p99 xấu.

**B9.** Deadline, concurrency limit, retention/TTL, resource budget, telemetry và rollout policy phải explicit.

**B10.** Tránh Request Lifecycle khi bài toán đơn giản hơn giải được invariant với ít state và operational cost hơn.

Cấu trúc câu trả lời: **Definition → Why → How → Trade-off → Production example**. Với câu scenario: **stabilize → observe → hypothesize → verify → mitigate → prevent**.

## 11. Follow-up Questions

- **F1.** What assumption in your answer is most risky?
- **F2.** How would you prove that with metrics or an experiment?
- **F3.** What changes if the operation is not idempotent?
- **F4.** Where would you add timeout, retry, and backpressure?
- **F5.** What is your rollback and data-reconciliation plan?

## 12. Key Takeaways

- Nói được **vai trò, constraint hoặc invariant của Request Lifecycle**, không chỉ “dùng để làm gì”.
- Định lượng bằng RPS, p95/p99 latency, error rate, event-loop lag và pool utilization và có baseline trước tối ưu.
- Thiết kế cho timeout, duplicate, overload, partial failure và recovery.
- Mọi tối ưu đều có chi phí về correctness, complexity, latency hoặc money.
- Production-ready nghĩa là có owner, alert, runbook, canary, rollback và reconciliation.


## 13. Mental Model

Mỗi request là một scope có deadline và resource ownership: tạo context, thực hiện work, trả response, rồi cleanup kể cả khi exception/cancel.

## 14. Internals Deep Dive


ASGI server tạo `scope` mô tả HTTP/WebSocket connection và gọi application với `receive`/`send` async callable. Uvicorn sở hữu socket/event loop/protocol; FastAPI/Starlette sở hữu middleware, routing và application behavior. Gunicorn có thể làm process manager cho nhiều worker, nhưng Uvicorn cũng hỗ trợ nhiều process; deployment choice phụ thuộc platform và graceful lifecycle.

FastAPI match route, resolve dependency graph (sync dependency có thể vào thread pool), validate input qua Pydantic rồi gọi endpoint. Response serialization và middleware unwind xảy ra trước/đồng thời cleanup tùy dependency scope/version; không dựa vào thứ tự mơ hồ cho transaction correctness. Mỗi worker có event loop/pool riêng, nên tổng DB connection = replicas × workers × pool configuration.


Implementation detail có thể đổi theo version; khi trả lời interview, nêu rõ CPython/PostgreSQL/Redis/framework version nếu kết luận dựa vào behavior nội bộ thay vì public contract.

## 15. Request / Data Flow

```mermaid
flowchart LR
    Client --> LB["Load balancer"]
    LB --> Uvicorn
    Uvicorn --> ASGI
    ASGI --> Middleware
    Middleware --> Router
    Router --> DI["Dependency graph"]
    DI --> Validation["Pydantic validation"]
    Validation --> Endpoint
    Endpoint --> Service
    Service --> Repository
    Repository --> DB[(PostgreSQL)]
```

Đọc diagram từ input tới state transition và output. Tại mỗi mũi tên, hỏi: operation có block không, có retry không, state có durable không, identity nào dùng để dedupe và metric nào chứng minh bước đó khỏe.

## 16. Failure Scenario

Một blocking dependency hoặc pool cạn có thể giữ toàn worker/loop, rồi client retry khuếch đại traffic. Load-shed/rate-limit, rollback, isolate route và bảo vệ downstream trước khi tăng replica.

Phân tích theo chuỗi: **trigger → saturation/incorrect state → propagation → user impact → immediate mitigation → durable prevention**. Tránh gọi retry hoặc scale là giải pháp nếu chưa chỉ ra dependency budget.

## 17. How I would debug this in production

1. So p50/p95/p99 theo route/worker/deploy.
2. Xem event-loop lag, thread tokens và worker saturation.
3. Trace middleware → dependency → endpoint → DB/cache.
4. Đo DB pool wait và downstream deadline/retry.
5. Rollback/canary fix rồi verify SLO.

## 18. Common Misconceptions

**Sai:** đổi mọi endpoint thành `async def` làm API nhanh. **Đúng:** toàn dependency path phải non-blocking và concurrency phải được bound.

## 19. When NOT to use

Không dùng async chỉ vì framework hỗ trợ; sync stack với bounded thread pool có thể đơn giản hơn khi dependency chỉ blocking.

## 20. What interviewer may ask next

1. **What guarantee does Request Lifecycle provide, and what does it explicitly not guarantee?**
2. **Which implementation detail changes across versions or runtimes?**
3. **Where is the first queue or contention point under high load?**
4. **What happens if the dependency times out after committing state?**
5. **How would you observe, degrade, and recover this in production?**
6. **Which simpler design would you choose at 100 RPS, and when would you evolve it?**

## 21. Check Your Understanding

1. Nếu throughput tăng 20× nhưng downstream capacity không đổi, **Request Lifecycle** sẽ tạo queue/backpressure ở đâu?
2. Timeout xảy ra ngay sau một state transition; caller có thể kết luận điều gì và không thể kết luận điều gì?
3. Metric, trace span và log field tối thiểu nào giúp phân biệt application, dependency và network latency?

<details>
<summary>Answer</summary>

1. Queue xuất hiện tại bounded resource đầu tiên: worker/thread/semaphore/connection pool/broker hoặc dependency. Nếu không có bound, overload chuyển thành memory growth và timeout storm.
2. Caller chỉ biết chưa nhận response trong deadline; operation có thể chưa chạy, đang chạy hoặc đã commit. Cần operation identity/idempotency và status/reconciliation.
3. Dùng end-to-end latency + queue/service time, correlation/trace ID, dependency spans, error/retry classification và saturation của pool/queue/resource.

</details>

## 22. See also

- [Sync vs Async](sync-vs-async-endpoint.md)
- [Connection Pooling](../04-database-postgresql/connection-pooling.md)
- [API Security](../16-security/api-security.md)
