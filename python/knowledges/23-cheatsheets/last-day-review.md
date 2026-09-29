# Last-day Review (60–120 phút)

## 0–20 phút: Python / FastAPI
- GIL không cấm concurrency; CPU Python → process, I/O → async/thread.
- Blocking trong async endpoint chặn loop; bound concurrency, deadline/cancel.
- Request/session lifecycle; transaction boundary; pool budget.

## 20–40 phút: PostgreSQL / Redis / Celery
- Index theo predicate/order/selectivity; đọc actual rows/loops/buffers.
- MVCC + long transaction + vacuum/bloat; isolation theo invariant.
- Cache stampede/fallback; task duplicate → idempotency, not “exactly once”.

## 40–65 phút: Distributed / System Design
- Deadline → timeout từng hop; retry transient + backoff/jitter/budget.
- Outbox cho dual write; consumer idempotent; reconciliation.
- Clarify → estimate → API/data → architecture → failure/security/observability → trade-off.

## 65–80 phút: Kubernetes / Reliability / AI
- Request/limit, probes, HPA vs downstream cap, rolling rollback.
- SLI/SLO/error budget; metrics + logs + traces; mitigation trước RCA.
- RAG: ingest/chunk/embed → retrieve/filter/rerank → prompt/cite; đo recall và groundedness.

## 80–100 phút: Story / Mental reset
- 6 STAR story có con số, decision, conflict, learning.
- Chuẩn bị câu hỏi cho interviewer. Không nhồi topic mới; ngủ và giữ nhịp nói chậm.
