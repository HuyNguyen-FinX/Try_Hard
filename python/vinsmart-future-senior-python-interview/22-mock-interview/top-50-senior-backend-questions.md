# Top 50 Senior Backend Interview Questions

Dùng như active-recall bank. Trả lời câu chính trong 90–120 giây theo **definition → mechanism → trade-off → production evidence**; sau đó trả lời follow-up mà không nhìn note.


### 1. Why does CPython have a GIL, and what changes in a free-threaded build?

**What a senior answer should cover:** Phân biệt language với CPython; runtime state/refcount, I/O release, C extension compatibility và synchronization vẫn cần.

**Likely follow-up:** Does the GIL make compound operations thread-safe? When do threads still help?

### 2. What actually happens when a Python reference count reaches zero?

**What a senior answer should cover:** Deallocation/refcount cascading trong CPython; cycle cần GC; `del` chỉ bỏ binding; external resource dùng deterministic cleanup.

**Likely follow-up:** What retains an object after a request ends? Why can RSS stay high after objects are freed?

### 3. Why does CPython need a cyclic garbage collector in addition to reference counting?

**What a senior answer should cover:** Cycle giữ refcount > 0; tracked containers/generational collection; version-dependent policy và GC pause/retention trade-off.

**Likely follow-up:** What objects are tracked? When would disabling GC be reasonable?

### 4. What does `await` do internally?

**What a senior answer should cover:** Coroutine yields awaitable/Future; Task registers continuation; loop resumes on completion. `await` không tạo thread và có thể không yield.

**Likely follow-up:** How does cancellation enter a coroutine? What if the awaited function blocks?

### 5. How does an event loop know that a socket is ready?

**What a senior answer should cover:** Non-blocking FD + OS readiness mechanism như epoll/kqueue/IOCP; callback vào ready queue; implementation depends on platform/loop.

**Likely follow-up:** What is event-loop lag? How would you measure it?

### 6. Why is CPU-heavy work dangerous inside an async endpoint?

**What a senior answer should cover:** Giữ event-loop thread/GIL-enabled bytecode, trì hoãn socket/timer/cancellation; process/native/queue và bounded concurrency.

**Likely follow-up:** Would adding more Uvicorn workers fix it? What happens to DB connections?

### 7. When would threads outperform AsyncIO, and when would processes outperform threads?

**What a senior answer should cover:** Blocking library/I/O với thread; high fan-out async-compatible I/O với AsyncIO; pure Python CPU với process, cân nhắc IPC/memory/startup.

**Likely follow-up:** How would you benchmark using production-like workload?

### 8. How can a race condition happen even with the GIL?

**What a senior answer should cover:** Invariant nhiều bytecode/read-modify-write, C calls release GIL, I/O interleaving; lock/atomic DB operation/immutability.

**Likely follow-up:** Which built-in operations are implementation details rather than guarantees?

### 9. Walk me through a FastAPI request from the socket to the response.

**What a senior answer should cover:** Uvicorn → ASGI scope/receive/send → middleware → routing → DI → Pydantic → endpoint → serialization/cleanup.

**Likely follow-up:** Where are sync dependencies executed? When is a yielded dependency cleaned up?

### 10. What happens if a FastAPI `async def` endpoint calls `requests.get()`?

**What a senior answer should cover:** Utility sync call chạy ngay trên loop; blocking stalls all connections in that worker; use async client or bounded offload.

**Likely follow-up:** How would traces and loop-lag metrics prove this?

### 11. How do worker count, thread pool, and DB pool interact in FastAPI?

**What a senior answer should cover:** Mỗi process có loop/thread/pool; total connection multiplication; pool wait/admission; scaling API có thể overload DB.

**Likely follow-up:** Build a connection budget for 100 pods and a 500-connection database.

### 12. Why can dependency injection create hidden production cost?

**What a senior answer should cover:** Graph resolution, sync dependency offload, resource scope, duplicate network calls và over-broad transaction; explicit boundary/telemetry.

**Likely follow-up:** Which dependencies should be cached per request?

### 13. Why can adding a PostgreSQL index make writes slower?

**What a senior answer should cover:** B-tree maintenance, page split, WAL, cache footprint, vacuum/bloat; every INSERT/UPDATE/DELETE touches relevant indexes.

**Likely follow-up:** When is a partial or covering index worth the cost?

### 14. How does a PostgreSQL B-tree find a heap row?

**What a senior answer should cover:** Root/internal/leaf pages, index tuple/key/TID, heap visibility check; index-only scan + visibility map.

**Likely follow-up:** Why might a B-tree index still not be chosen?

### 15. How does MVCC avoid blocking readers and writers?

**What a senior answer should cover:** Tuple versions, xmin/xmax, snapshot visibility; writer creates new version, reader sees snapshot; conflict vẫn có ở writer/lock.

**Likely follow-up:** How do long transactions cause bloat and vacuum problems?

### 16. What is the difference between Read Committed, Repeatable Read, and Serializable in PostgreSQL?

**What a senior answer should cover:** Snapshot scope/anomalies, PostgreSQL SSI và whole-transaction retry; chọn theo invariant.

**Likely follow-up:** Show a write-skew or lost-update example and fix it.

### 17. How do you read `EXPLAIN (ANALYZE, BUFFERS)`?

**What a senior answer should cover:** Node deepest mismatch, estimate vs actual, loops, rows removed, join/scan, spill/temp, shared hit/read và DML safety.

**Likely follow-up:** Why can a locally fast plan be slow under production concurrency?

### 18. When does PostgreSQL choose Seq Scan, Index Scan, Index Only Scan, or Bitmap Heap Scan?

**What a senior answer should cover:** Selectivity, heap/page locality, visibility map, random vs sequential cost, multiple predicates.

**Likely follow-up:** How would stale statistics change the choice?

### 19. Compare Nested Loop, Hash Join, and Merge Join.

**What a senior answer should cover:** Input size/order/index/memory; row-estimate error; spill/batch; nested loop amplification.

**Likely follow-up:** Which plan symptom suggests the join type is wrong because of misestimation?

### 20. Why can a database connection pool become a bottleneck?

**What a senior answer should cover:** Bounded admission; request waits; long transaction/query holds slot. Oversized pool shifts queue to DB and adds contention.

**Likely follow-up:** Which metrics separate query latency from pool wait?

### 21. How would you index a 500-million-row warranty table?

**What a senior answer should cover:** Access patterns/selectivity/composite order/partial/covering/partition, write/WAL/storage cost; representative EXPLAIN.

**Likely follow-up:** How do data skew and retention change the design?

### 22. What causes a PostgreSQL deadlock and how do you fix it?

**What a senior answer should cover:** Cycle in wait graph, victim abort; consistent lock order, shorter transaction, index fewer rows, retry whole tx with jitter.

**Likely follow-up:** How is a deadlock different from a long lock wait?

### 23. Why is Redis fast beyond simply storing data in RAM?

**What a senior answer should cover:** Specialized encodings/data structures, mostly serialized command execution, event loop và low round trips; O(N)/big key blocks others.

**Likely follow-up:** How do I/O threads change—and not change—the model?

### 24. What happens when Redis disappears during a traffic spike?

**What a senior answer should cover:** Circuit, cache miss storm, DB overload, bounded stale fallback, rate limit/coalescing, jittered reconnect/warm-up.

**Likely follow-up:** Which endpoints fail open versus fail closed?

### 25. How do TTL, eviction, and expiration differ in Redis?

**What a senior answer should cover:** TTL semantic lifetime; passive/active expiry; eviction under maxmemory policy; none guarantee business invalidation.

**Likely follow-up:** How do synchronized expirations create an outage?

### 26. When is a Redis distributed lock unsafe?

**What a senior answer should cover:** Lease expiry/pause/partition/failover; stale owner writes. Owner token compare-delete, fencing, DB constraint; safety vs liveness.

**Likely follow-up:** Would Redlock protect a financial invariant? What remains at the storage boundary?

### 27. How do Redis Sentinel and Redis Cluster differ?

**What a senior answer should cover:** Sentinel HA non-sharded; Cluster 16,384 slots/sharding/failover; redirects, cross-slot, hot key, async replication loss window.

**Likely follow-up:** How does a client behave during reshard/failover?

### 28. Why can a Celery task run twice?

**What a senior answer should cover:** Worker commit then crash before ACK, lease/visibility timeout, producer retry/failover; delivery/effect scopes.

**Likely follow-up:** Compare early ACK and late ACK failure windows.

### 29. How do you make a Celery task idempotent?

**What a senior answer should cover:** Business key, unique constraint/inbox, conditional transition, provider idempotency/ledger, return prior result, reconcile.

**Likely follow-up:** Why is a Redis lock not sufficient?

### 30. How do prefetch and task routing affect Celery fairness?

**What a senior answer should cover:** Reserved local tasks, long-vs-short head-of-line, queue/resource/SLO isolation, throughput vs fairness.

**Likely follow-up:** Which metric is better than queue length for variable runtime tasks?

### 31. Why is exactly-once processing difficult?

**What a senior answer should cover:** Ack/commit crash window, external effect outside broker transaction; define scope; at-least-once + idempotency + reconciliation.

**Likely follow-up:** Can Kafka exactly-once semantics make an email send exactly once?

### 32. Why is retry dangerous?

**What a senior answer should cover:** Load amplification, synchronized retry, deadline exhaustion, duplicate non-idempotent effect; classify transient, backoff/full jitter/budget/circuit.

**Likely follow-up:** Which HTTP/DB errors are retryable and at what layer?

### 33. How should timeouts be budgeted across a service call chain?

**What a senior answer should cover:** End-to-end deadline minus queue/serialization, connect/read/pool timeouts, child shorter than parent, cancellation propagation.

**Likely follow-up:** What if the server commits after the caller times out?

### 34. How does a circuit breaker work internally?

**What a senior answer should cover:** Closed/Open/Half-Open, rolling failure/slow-call threshold, cooldown/probes; scope/bulkhead/fallback.

**Likely follow-up:** How can a badly scoped breaker increase blast radius?

### 35. How does the transactional outbox solve the dual-write problem?

**What a senior answer should cover:** Business row + outbox same DB tx; relay poll/CDC; publish duplicate possible; consumer dedupe/monitor outbox age.

**Likely follow-up:** What if the relay publishes and crashes before marking the row?

### 36. Compare choreography and orchestration for a Saga.

**What a senior answer should cover:** Visibility/coupling/coordinator; compensation failure/idempotency, no isolation, irreversible step/human review.

**Likely follow-up:** When is a local transaction better than a Saga?

### 37. How would you prevent duplicate payment or warranty claim requests?

**What a senior answer should cover:** Tenant-scoped idempotency key + canonical payload hash + atomic business write/response; external provider key and ledger.

**Likely follow-up:** What TTL is safe, and what if the duplicate arrives after TTL?

### 38. What is eventual consistency, and how do you make it acceptable to users?

**What a senior answer should cover:** Staleness window, version/cursor/read-your-write/session semantics, status projection, reconciliation and transparent UI.

**Likely follow-up:** How do you measure convergence time?

### 39. What does CAP theorem actually say during a network partition?

**What a senior answer should cover:** For replicated operation under partition choose availability response vs consistency/linearizability; not a database ranking and not normal-state latency.

**Likely follow-up:** Can different operations choose differently?

### 40. How would you identify whether latency comes from application, database, or network?

**What a senior answer should cover:** End-to-end trace + queue/service time, loop/pool wait, DB wait/plan, DNS/connect/TLS, RED/USE baseline.

**Likely follow-up:** What evidence would make you stop scaling application pods?

### 41. How do you design graceful degradation?

**What a senior answer should cover:** Prioritize critical journey, stale/read-only/queued/fail-fast semantics, circuit/bulkhead/load shed, explicit user status and recovery reconciliation.

**Likely follow-up:** Which data may be stale, and for how long?

### 42. How do SLI, SLO, SLA, and error budgets change engineering decisions?

**What a senior answer should cover:** User-visible good/valid events, internal target vs contract, burn-rate, release/risk trade-off.

**Likely follow-up:** Why is average availability or latency insufficient?

### 43. What should a production trace contain across an async queue?

**What a senior answer should cover:** Trace context/links, operation/message ID, producer/consumer spans, queue delay vs processing, version/tenant safe tags.

**Likely follow-up:** How do you avoid high-cardinality telemetry?

### 44. Why can Kubernetes HPA make an outage worse?

**What a senior answer should cover:** Scale API based CPU while DB/provider saturated; startup lag, request denominator, reconnect storm. Custom queue age and downstream cap.

**Likely follow-up:** How do stabilization and readiness affect scaling?

### 45. Explain Kubernetes CPU requests, CPU limits, and memory limits under load.

**What a senior answer should cover:** Scheduler uses requests; CPU limit throttles; memory limit may OOM; HPA utilization denominator; workload-dependent limit policy.

**Likely follow-up:** Why can p99 be bad when node CPU looks free?

### 46. How do you deploy a database-dependent change without downtime?

**What a senior answer should cover:** Expand/contract schema, backward-compatible app, online index/backfill throttle/checkpoint, dual-read compare, canary and rollback.

**Likely follow-up:** What makes a migration irreversible?

### 47. How would you secure a multi-tenant backend beyond validating JWTs?

**What a senior answer should cover:** Resource-level authorization, tenant context isolation, DB/query guard, IAM/secret, rate quota, audit, PII encryption/redaction.

**Likely follow-up:** How would you test cross-tenant access systematically?

### 48. How does a RAG request flow from user query to cited answer?

**What a senior answer should cover:** Auth/ACL, embed/hybrid retrieve, rerank, token pack, prompt/model, citation/abstention; version and metrics.

**Likely follow-up:** How do you distinguish retrieval failure from generation failure?

### 49. What is the source of truth in an AI system with PostgreSQL, S3, a vector DB, and Redis?

**What a senior answer should cover:** S3 binary, PG metadata/ACL/workflow, vector derived index, Redis cache; rebuild/version/delete propagation.

**Likely follow-up:** What happens during an embedding model migration?

### 50. How do you scale an API from 1,000 to 20,000 RPS without overloading PostgreSQL?

**What a senior answer should cover:** Measure sustainable worker, async/nonblocking, LB/pods, global pool budget, cache, replicas for stale read, queue, HPA cap, rate limit/load shed.

**Likely follow-up:** Which component would you add first at 100 RPS, and which would you explicitly avoid?


## Self-scoring

- **0:** chỉ biết keyword hoặc sai mechanism.
- **1:** definition đúng nhưng thiếu internals/failure.
- **2:** có mechanism, trade-off và ví dụ production.
- **3:** định lượng, nói rõ assumption/version, degraded mode, observability và alternative đơn giản hơn.
