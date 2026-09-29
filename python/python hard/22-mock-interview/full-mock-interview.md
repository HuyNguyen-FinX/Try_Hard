# Full Mock Interview — 110 Minutes

**Luật:** dùng timer; hỏi clarification; think aloud; không mở Answer khi đang làm. Chấm mỗi phần 1–4: correctness, depth, trade-off, production judgment, communication.

## 0–10 min — Introduction

### Question

Give me a two-minute overview of your background and the backend system where you had the strongest technical impact. What changed because of your decision?

<details><summary>Answer rubric</summary>

Role/scope ngắn; baseline định lượng; decision của cá nhân; trade-off; outcome và relevance với role. Tránh kể chronology dài.
</details>

## 10–30 min — Python

### Question 1

Explain the CPython memory model, reference counting, cyclic GC, and one real memory-retention incident.

<details><summary>Answer</summary>

Name giữ reference; refcount về 0 thường reclaim ngay; cyclic GC tìm container cycle; `del` không đảm bảo free nếu còn reference. Resource dùng context manager. Điều tra bằng RSS/heap/tracemalloc/object growth; phân biệt leak với allocator fragmentation/cache.
</details>

### Question 2

Does the GIL mean Python cannot handle concurrent requests? Choose between threads, AsyncIO, and processes for three different workloads.

<details><summary>Answer</summary>

GIL giới hạn Python bytecode parallel trong một CPython interpreter, không cấm I/O concurrency. AsyncIO cho nhiều non-blocking I/O; thread cho blocking I/O/library sync có bound; process/native cho CPU Python, tính serialization/startup cost.
</details>

### Question 3

What happens when CPU-heavy code runs inside a FastAPI `async def` endpoint? How do you prove and fix it?

<details><summary>Answer</summary>

Nó chặn event loop, tăng loop lag và tail latency cho request khác. Dùng trace/profile/load test; offload process/queue/native, bound concurrency; scale worker chỉ sau khi hiểu bottleneck.
</details>

## 30–50 min — Backend / Database

### Question 4

A PostgreSQL table has 500 million warranty records. Design indexes for “latest claims by vehicle” and explain write cost and verification.

<details><summary>Answer</summary>

Access path gợi ý `(vehicle_id, created_at DESC) INCLUDE (status...)`; partial index cho active claim nếu predicate ổn định. Xem selectivity/size/write amplification. Verify `EXPLAIN (ANALYZE, BUFFERS)` với distribution thật, estimate vs actual, loops và I/O.
</details>

### Question 5

Two requests create the same claim. Show an idempotency design that remains correct across timeouts and retries.

<details><summary>Answer</summary>

Scope key theo tenant; hash canonical payload; atomically claim bằng unique constraint cùng business transaction; duplicate running/completed có semantics; cùng key khác payload reject; TTL dựa business window. External side effect cần provider key/inbox và reconciliation.
</details>

### Question 6

Your API scales from 20 to 200 pods. Why might the database fail even if every pod is healthy?

<details><summary>Answer</summary>

Connection explosion = pod × worker × pool, cùng query/lock/IO amplification. Đặt global connection/admission budget, pool nhỏ/PgBouncer, backpressure, cache/read replica phù hợp và cap HPA theo downstream capacity.
</details>

## 50–80 min — System Design

### Question 7

Design a multi-tenant AI Chatbot Platform for one million daily active users. It must use private documents, stream answers, cite sources, enforce document ACLs, and tolerate an LLM provider outage.

Cover requirements, estimation, API, data model, ingestion/RAG flow, cache/queue, scaling, security, failure behavior, observability, cost and trade-offs.

<details><summary>Answer</summary>

Strong path: clarify SLO/quality/privacy → estimate peak/tokens/storage → conversation/message/document/chunk model → async versioned ingestion → ACL-aware hybrid retrieval + rerank → orchestrator with token/deadline budget → SSE/cancel. PostgreSQL metadata, object store, vector index, queue for ingestion/eval. Provider bulkhead/circuit/fallback, rate limit, semantic cache carefully scoped. Measure TTFT, p99, retrieval recall, groundedness, cost/success; defend prompt injection/data exfiltration; reconciliation and model/version rollout.
</details>

## 80–95 min — Production Scenario

### Question 8

In ten minutes API latency rises from 100 ms to 3 s. App CPU is normal; PostgreSQL CPU is 95%. Walk through your response.

<details><summary>Answer</summary>

Confirm impact/SLO and freeze risky rollout; compare deploy/traffic. Check DB connections, active queries/waits/locks, top query time/calls, buffer/IO, replica lag and pool wait. Capture representative plan safely (`EXPLAIN ANALYZE` read query or transaction rollback); compare estimate/actual/index/bloat/stats. Immediate: shed/rate-limit, kill pathological query carefully, rollback, reduce fan-out/cache safe read. Long-term: query/index/schema fix, stats/vacuum, capacity test, alert and regression guard.
</details>

### Question 9

Redis becomes unavailable and Celery redelivers thousands of tasks. Prevent a cache-miss storm and duplicate business effects.

<details><summary>Answer</summary>

Circuit-break Redis, bounded fallback/stale cache, rate-limit/coalesce miss, protect DB and warm gradually. Pause/drain producer/consumer as appropriate. Task effect idempotent qua unique business key/inbox; retry jitter/budget; reconcile external effects. Redis lock alone không tạo exactly-once.
</details>

## 95–105 min — Behavioral

### Question 10

Tell me about a high-severity incident where your initial hypothesis was wrong. How did you lead, communicate, and improve the system?

<details><summary>Answer rubric</summary>

STAR: impact/timeline rõ; mitigation trước ego; hypothesis dựa evidence và cách đổi hướng; role/communication; result định lượng; blameless learning, action owner và prevention verified.
</details>

## 105–110 min — Candidate Questions

- What production outcome defines success in the first six months?
- Which architectural constraint currently limits the team most?
- How are design decisions, on-call ownership, and incident learning shared?

## Scorecard

| Dimension | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Correctness | Major gaps | Mostly basic | Correct + edge cases | Precise + teaches |
| Senior depth | Definitions | Some internals | Invariant/failure/trade-off | Cross-system judgment |
| Production | Happy path | Names tools | Metrics/mitigation/recovery | Prevents recurrence |
| Communication | Unstructured | Needs prompts | Clear assumptions | Concise, adaptive, leads |

**Hire-ready signal:** không cần hoàn hảo mọi chi tiết; cần reasoning có cấu trúc, sửa assumption khi có evidence và chủ động ownership production.
