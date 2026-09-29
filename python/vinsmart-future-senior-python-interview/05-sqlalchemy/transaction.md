# Transaction

> **Phạm vi phỏng vấn:** SQLAlchemy · **Ưu tiên:** P0/P1 · **Mindset:** Why → How → Trade-off → Production.

## 1. What is it?

SQLAlchemy transaction bọc DBAPI transaction qua Session/Connection; flush gửi SQL nhưng chỉ commit mới làm transaction durable.

## 2. Why does it matter?

Senior Engineer cần hiểu **Transaction** để giữ transaction boundary đúng mà vẫn nhìn thấy chi phí SQL thực tế. Điểm phỏng vấn nằm ở khả năng nêu invariant, điều kiện áp dụng và failure behavior, không nằm ở việc thuộc định nghĩa.

## 3. How does it work?

`begin()` quản commit/rollback; nested transaction thường dùng SAVEPOINT. Transaction boundary phải theo business use case, không tự commit rải trong repository.

Khi reasoning, đi theo chuỗi: **input → state transition → output → failure → recovery**. Quan sát `query count, pool wait, transaction age, fetched rows và p99 latency` và phân biệt symptom, bottleneck với root cause.

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

Ví dụ giữ I/O path non-blocking; production cần deadline, structured log và bounded pool cho **Transaction**.

## 5. Production Use Case

Create claim + outbox event nằm cùng `session.begin()`; external API call xảy ra ngoài transaction và flow dùng state machine/reconciliation.

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
| Tối ưu/thiết kế xoay quanh Transaction | Kiểm soát rõ constraint chính | Tăng complexity và coupling | Metric chứng minh đây là bottleneck/risk |
| Giữ baseline đơn giản | Ít dependency, dễ debug | Có thể chạm giới hạn sớm | Traffic vừa, invariant vẫn được giữ |
| Managed service/library | Giảm vận hành hạ tầng | Cost, lock-in, giới hạn control | SLA và economics phù hợp |
| Tự vận hành/customize | Kiểm soát sâu | Ownership và failure surface lớn | Có năng lực vận hành và nhu cầu thật |

## 8. Interview Questions

### Basic / Mid-level (10)

- **B1.** What is Transaction, and which concrete problem does it address?
- **B2.** Explain the main internal mechanism behind Transaction.
- **B3.** Which guarantees does Transaction provide, and which does it not provide?
- **B4.** Which metrics or observations reveal the behavior of Transaction?
- **B5.** What is the most common misconception about Transaction?
- **B6.** How would you test assumptions involving Transaction?
- **B7.** Which edge cases or failure modes matter most for Transaction?
- **B8.** How can Transaction affect latency, throughput, memory, or correctness?
- **B9.** Which runtime conditions or configuration choices change the behavior of Transaction?
- **B10.** When is a different or simpler approach better than relying on Transaction?

### Production Scenarios (5)

- **S1.** A release involving Transaction triples p99 while averages look normal. How do you investigate and mitigate?
- **S2.** A critical dependency around Transaction is unavailable for ten minutes. Define degraded behavior and recovery.
- **S3.** Two concurrent operations expose a correctness gap related to Transaction. Which invariant and atomic boundary fix it?
- **S4.** Traffic grows from 1,000 to 20,000 RPS. Which measured limit involving Transaction fails first?
- **S5.** A canary changes the behavior of Transaction; success rate is flat but saturation rises. Promote or roll back?

## 9. Senior-level Questions

- **L1.** How does Transaction constrain the surrounding architecture and operational model?
- **L2.** Which subtle correctness issue appears when Transaction meets concurrency or partial failure?
- **L3.** What breaks first around Transaction at 20,000 RPS or 100× data volume?
- **L4.** Where should admission control or backpressure be placed when using Transaction?
- **L5.** How would you benchmark or validate Transaction without a misleading microbenchmark?
- **L6.** Which hidden coupling or migration cost can Transaction introduce?
- **L7.** How would you change a poor decision around Transaction with no downtime?
- **L8.** What production evidence would make you choose a different approach?
- **L9.** How do correctness, latency, cost, and complexity trade off for Transaction?
- **L10.** How would you turn an incident involving Transaction into a durable prevention mechanism?

## 10. Short Answers

**B1.** SQLAlchemy transaction bọc DBAPI transaction qua Session/Connection; flush gửi SQL nhưng chỉ commit mới làm transaction durable. Trả lời tốt nối definition với constraint/invariant và một use case cụ thể.

**B2.** Mô tả state, lifecycle, boundary và failure path; không dừng ở public API của Transaction.

**B3.** Nêu lúc tạo, lúc sử dụng, lúc release/commit và điều xảy ra khi timeout hoặc cancellation.

**B4.** Đo query count, pool wait, transaction age, fetched rows và p99 latency; luôn tách average khỏi tail và success khỏi useful result.

**B5.** Lỗi phổ biến là dùng Transaction như mặc định mà không xác định ownership, limit và fallback.

**B6.** Test invariant trước, sau đó integration test failure path, concurrency và representative load.

**B7.** Xét timeout, duplicate, stale state, overload, dependency loss và recovery/reconciliation.

**B8.** Đo critical path, contention, queueing và amplification; throughput cao không bù được p99 xấu.

**B9.** Deadline, concurrency limit, retention/TTL, resource budget, telemetry và rollout policy phải explicit.

**B10.** Tránh Transaction khi bài toán đơn giản hơn giải được invariant với ít state và operational cost hơn.

Cấu trúc câu trả lời: **Definition → Why → How → Trade-off → Production example**. Với câu scenario: **stabilize → observe → hypothesize → verify → mitigate → prevent**.

## 11. Follow-up Questions

- **F1.** What assumption in your answer is most risky?
- **F2.** How would you prove that with metrics or an experiment?
- **F3.** What changes if the operation is not idempotent?
- **F4.** Where would you add timeout, retry, and backpressure?
- **F5.** What is your rollback and data-reconciliation plan?

## 12. Key Takeaways

- Nói được **vai trò, constraint hoặc invariant của Transaction**, không chỉ “dùng để làm gì”.
- Định lượng bằng query count, pool wait, transaction age, fetched rows và p99 latency và có baseline trước tối ưu.
- Thiết kế cho timeout, duplicate, overload, partial failure và recovery.
- Mọi tối ưu đều có chi phí về correctness, complexity, latency hoặc money.
- Production-ready nghĩa là có owner, alert, runbook, canary, rollback và reconciliation.


## 13. Mental Model

Transaction là ranh giới all-or-nothing và isolation cho invariant, không phải wrapper càng rộng càng an toàn.

## 14. Internals Deep Dive

Luôn ánh xạ abstraction ORM về SQL, transaction và connection thật. Session là identity map/unit-of-work, không phải global cache; flush khác commit và loading strategy quyết định query/row amplification.

Implementation detail có thể đổi theo version; khi trả lời interview, nêu rõ CPython/PostgreSQL/Redis/framework version nếu kết luận dựa vào behavior nội bộ thay vì public contract.

## 15. Request / Data Flow

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Active: BEGIN / implicit start
    Active --> Active: statements + WAL
    Active --> Committed: COMMIT
    Active --> Aborted: error / ROLLBACK
    Aborted --> Idle: ROLLBACK complete
    Committed --> Idle
```

Đọc diagram từ input tới state transition và output. Tại mỗi mũi tên, hỏi: operation có block không, có retry không, state có durable không, identity nào dùng để dedupe và metric nào chứng minh bước đó khỏe.

## 16. Failure Scenario

Session leak, long transaction, implicit lazy load hoặc pool exhaustion thường bị ORM che. Log query count/pool wait/transaction age, rollback đúng scope và inspect SQL thật.

Phân tích theo chuỗi: **trigger → saturation/incorrect state → propagation → user impact → immediate mitigation → durable prevention**. Tránh gọi retry hoặc scale là giải pháp nếu chưa chỉ ra dependency budget.

## 17. How I would debug this in production

1. Bật SQL timing/query count có sampling.
2. Xem pool checked-out/wait/timeout.
3. Kiểm session scope, autoflush và transaction age.
4. Tìm lazy load/N+1 và row amplification.
5. So generated SQL + plan trước/sau.

## 18. Common Misconceptions

**Sai:** ORM loại bỏ nhu cầu hiểu SQL/transaction. **Đúng:** ORM chỉ sinh và hydrate SQL; database semantics vẫn quyết định correctness/performance.

## 19. When NOT to use

Không hydrate object graph cho bulk analytics/ETL; SQLAlchemy Core/raw parameterized SQL có thể rõ và rẻ hơn.

## 20. What interviewer may ask next

1. **What guarantee does Transaction provide, and what does it explicitly not guarantee?**
2. **Which implementation detail changes across versions or runtimes?**
3. **Where is the first queue or contention point under high load?**
4. **What happens if the dependency times out after committing state?**
5. **How would you observe, degrade, and recover this in production?**
6. **Which simpler design would you choose at 100 RPS, and when would you evolve it?**

## 21. Check Your Understanding

1. Nếu throughput tăng 20× nhưng downstream capacity không đổi, **Transaction** sẽ tạo queue/backpressure ở đâu?
2. Timeout xảy ra ngay sau một state transition; caller có thể kết luận điều gì và không thể kết luận điều gì?
3. Metric, trace span và log field tối thiểu nào giúp phân biệt application, dependency và network latency?

<details>
<summary>Answer</summary>

1. Queue xuất hiện tại bounded resource đầu tiên: worker/thread/semaphore/connection pool/broker hoặc dependency. Nếu không có bound, overload chuyển thành memory growth và timeout storm.
2. Caller chỉ biết chưa nhận response trong deadline; operation có thể chưa chạy, đang chạy hoặc đã commit. Cần operation identity/idempotency và status/reconciliation.
3. Dùng end-to-end latency + queue/service time, correlation/trace ID, dependency spans, error/retry classification và saturation của pool/queue/resource.

</details>

## 22. See also

- [Session Lifecycle](session-lifecycle.md)
- [PostgreSQL Pooling](../04-database-postgresql/connection-pooling.md)
