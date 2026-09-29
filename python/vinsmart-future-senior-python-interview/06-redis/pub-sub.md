# Pub Sub

> **Phạm vi phỏng vấn:** Redis · **Ưu tiên:** P0/P1 · **Mindset:** Why → How → Trade-off → Production.

## 1. What is it?

Redis Pub/Sub là ephemeral fan-out: subscriber offline hoặc disconnect sẽ mất message, không có consumer acknowledgement/history.

## 2. Why does it matter?

Senior Engineer cần hiểu **Pub Sub** để giảm latency mà không biến cache thành single point of failure. Điểm phỏng vấn nằm ở khả năng nêu invariant, điều kiện áp dụng và failure behavior, không nằm ở việc thuộc định nghĩa.

## 3. How does it work?

Publisher gửi channel, connected subscribers nhận realtime; cluster/failover và slow consumer cần hiểu. Dùng cho invalidation/presence hint, không cho durable business workflow.

Khi reasoning, đi theo chuỗi: **input → state transition → output → failure → recovery**. Quan sát `hit ratio, evictions, memory fragmentation, command latency và replication lag` và phân biệt symptom, bottleneck với root cause.

## 4. Example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Decision:
    topic: str
    invariant: str
    metric: str

decision = Decision(
    topic='Pub Sub',
    invariant="Không làm mất hoặc lặp business effect",
    metric="p99 latency và error rate",
)
```

Ví dụ biến quyết định về **Pub Sub** thành invariant và tín hiệu vận hành có thể kiểm chứng.

## 5. Production Use Case

Cache invalidation có thể dùng Pub/Sub cộng TTL safety; warranty payment phải dùng durable stream/queue + idempotent consumer.

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
| Tối ưu/thiết kế xoay quanh Pub Sub | Kiểm soát rõ constraint chính | Tăng complexity và coupling | Metric chứng minh đây là bottleneck/risk |
| Giữ baseline đơn giản | Ít dependency, dễ debug | Có thể chạm giới hạn sớm | Traffic vừa, invariant vẫn được giữ |
| Managed service/library | Giảm vận hành hạ tầng | Cost, lock-in, giới hạn control | SLA và economics phù hợp |
| Tự vận hành/customize | Kiểm soát sâu | Ownership và failure surface lớn | Có năng lực vận hành và nhu cầu thật |

## 8. Interview Questions

### Basic / Mid-level (10)

- **B1.** What is Pub Sub, and which concrete problem does it address?
- **B2.** Explain the main internal mechanism behind Pub Sub.
- **B3.** Which guarantees does Pub Sub provide, and which does it not provide?
- **B4.** Which metrics or observations reveal the behavior of Pub Sub?
- **B5.** What is the most common misconception about Pub Sub?
- **B6.** How would you test assumptions involving Pub Sub?
- **B7.** Which edge cases or failure modes matter most for Pub Sub?
- **B8.** How can Pub Sub affect latency, throughput, memory, or correctness?
- **B9.** Which runtime conditions or configuration choices change the behavior of Pub Sub?
- **B10.** When is a different or simpler approach better than relying on Pub Sub?

### Production Scenarios (5)

- **S1.** A release involving Pub Sub triples p99 while averages look normal. How do you investigate and mitigate?
- **S2.** A critical dependency around Pub Sub is unavailable for ten minutes. Define degraded behavior and recovery.
- **S3.** Two concurrent operations expose a correctness gap related to Pub Sub. Which invariant and atomic boundary fix it?
- **S4.** Traffic grows from 1,000 to 20,000 RPS. Which measured limit involving Pub Sub fails first?
- **S5.** A canary changes the behavior of Pub Sub; success rate is flat but saturation rises. Promote or roll back?

## 9. Senior-level Questions

- **L1.** How does Pub Sub constrain the surrounding architecture and operational model?
- **L2.** Which subtle correctness issue appears when Pub Sub meets concurrency or partial failure?
- **L3.** What breaks first around Pub Sub at 20,000 RPS or 100× data volume?
- **L4.** Where should admission control or backpressure be placed when using Pub Sub?
- **L5.** How would you benchmark or validate Pub Sub without a misleading microbenchmark?
- **L6.** Which hidden coupling or migration cost can Pub Sub introduce?
- **L7.** How would you change a poor decision around Pub Sub with no downtime?
- **L8.** What production evidence would make you choose a different approach?
- **L9.** How do correctness, latency, cost, and complexity trade off for Pub Sub?
- **L10.** How would you turn an incident involving Pub Sub into a durable prevention mechanism?

## 10. Short Answers

**B1.** Redis Pub/Sub là ephemeral fan-out: subscriber offline hoặc disconnect sẽ mất message, không có consumer acknowledgement/history. Trả lời tốt nối definition với constraint/invariant và một use case cụ thể.

**B2.** Mô tả state, lifecycle, boundary và failure path; không dừng ở public API của Pub Sub.

**B3.** Nêu lúc tạo, lúc sử dụng, lúc release/commit và điều xảy ra khi timeout hoặc cancellation.

**B4.** Đo hit ratio, evictions, memory fragmentation, command latency và replication lag; luôn tách average khỏi tail và success khỏi useful result.

**B5.** Lỗi phổ biến là dùng Pub Sub như mặc định mà không xác định ownership, limit và fallback.

**B6.** Test invariant trước, sau đó integration test failure path, concurrency và representative load.

**B7.** Xét timeout, duplicate, stale state, overload, dependency loss và recovery/reconciliation.

**B8.** Đo critical path, contention, queueing và amplification; throughput cao không bù được p99 xấu.

**B9.** Deadline, concurrency limit, retention/TTL, resource budget, telemetry và rollout policy phải explicit.

**B10.** Tránh Pub Sub khi bài toán đơn giản hơn giải được invariant với ít state và operational cost hơn.

Cấu trúc câu trả lời: **Definition → Why → How → Trade-off → Production example**. Với câu scenario: **stabilize → observe → hypothesize → verify → mitigate → prevent**.

## 11. Follow-up Questions

- **F1.** What assumption in your answer is most risky?
- **F2.** How would you prove that with metrics or an experiment?
- **F3.** What changes if the operation is not idempotent?
- **F4.** Where would you add timeout, retry, and backpressure?
- **F5.** What is your rollback and data-reconciliation plan?

## 12. Key Takeaways

- Nói được **vai trò, constraint hoặc invariant của Pub Sub**, không chỉ “dùng để làm gì”.
- Định lượng bằng hit ratio, evictions, memory fragmentation, command latency và replication lag và có baseline trước tối ưu.
- Thiết kế cho timeout, duplicate, overload, partial failure và recovery.
- Mọi tối ưu đều có chi phí về correctness, complexity, latency hoặc money.
- Production-ready nghĩa là có owner, alert, runbook, canary, rollback và reconciliation.
