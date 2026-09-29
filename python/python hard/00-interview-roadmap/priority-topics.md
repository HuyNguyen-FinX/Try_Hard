# Priority Topics

## P0 — MUST KNOW

- Python memory/reference model; GIL; AsyncIO/event loop; CPU-vs-I/O-bound.
- FastAPI request lifecycle, sync-vs-async endpoint, DI/session scope, authentication, error/timeout.
- PostgreSQL B-tree/composite/partial index, `EXPLAIN ANALYZE BUFFERS`, transaction, isolation, MVCC, locks, pool budget.
- Distributed system: idempotency, deadline/timeout, retry + jitter/budget, circuit breaker, outbox, at-least-once.
- System Design framework, capacity estimation, cache/queue/database scaling, observability và failure handling.
- Scenario: database high CPU, Redis down, duplicate task/message, high traffic, data consistency.

**Exit criteria:** trả lời 2 phút/topic; giải 5 scenario theo evidence; thiết kế AI Chatbot và Warranty System trong 35 phút.

## P1 — VERY IMPORTANT

- Redis cache patterns, stampede, eviction/persistence, Sentinel/Cluster.
- Celery broker/ack/retry/idempotency/routing và production operations.
- SQLAlchemy session/transaction/N+1/loading/async.
- REST/versioning/pagination/rate limit/OAuth2/JWT/API security.
- Docker multi-stage/non-root; Kubernetes requests/limits, probes, HPA, rollout/troubleshoot.
- SLI/SLO, metrics/log/trace, load test, incident response.
- RAG pipeline, embeddings/vector DB, streaming, LLM cost/quality/security.

**Exit criteria:** giải thích trade-off và failure behavior, không chỉ định nghĩa.

## P2 — NICE TO KNOW

- Python descriptors/advanced dunder; rare PostgreSQL index types.
- Terraform module/state internals; cloud service mapping chi tiết.
- Design pattern ít dùng; algorithm nâng cao ngoài pattern phổ biến.
- ML mathematics; multi-region active-active trước khi requirement đòi hỏi.

## Quy tắc ưu tiên

Khi thiếu thời gian: **P0 depth > P1 breadth > P2 recognition**. Một câu trả lời có invariant, metric, failure mode và production example đáng giá hơn danh sách nhiều tool.
