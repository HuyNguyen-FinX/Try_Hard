# API Slow

> **Phạm vi phỏng vấn:** Production Scenario · **Ưu tiên:** P0/P1 · **Mindset:** Why → How → Trade-off → Production.

## 1. What is it?

API slow là latency regression trên một hoặc nhiều percentile; average bình thường không loại trừ queueing, hot key hoặc một route/tenant bị ảnh hưởng.

## 2. Why does it matter?

Senior Engineer cần hiểu **API Slow** để Senior Engineer phải giảm impact trước, tìm nguyên nhân bằng evidence và phòng tái diễn. Điểm phỏng vấn nằm ở khả năng nêu invariant, điều kiện áp dụng và failure behavior, không nằm ở việc thuộc định nghĩa.

## 3. How does it work?

Tách queue time và service time; phân rã trace qua gateway, app, pool, DB/cache/downstream. So sánh p50/p95/p99 với deploy/traffic, xem saturation và error/retry. Mitigate bằng rollback/load shed/cache/fallback rồi profile đúng bottleneck.

Khi reasoning, đi theo chuỗi: **input → state transition → output → failure → recovery**. Quan sát `customer impact, detection time, mitigation time, MTTR và recurrence` và phân biệt symptom, bottleneck với root cause.

## 4. Example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Decision:
    topic: str
    invariant: str
    metric: str

decision = Decision(
    topic='API Slow',
    invariant="Không làm mất hoặc lặp business effect",
    metric="p99 latency và error rate",
)
```

Ví dụ biến quyết định về **API Slow** thành invariant và tín hiệu vận hành có thể kiểm chứng.

## 5. Production Use Case

Warranty API tăng 100ms lên 3s: trace cho thấy DB pool wait, top query đổi plan sau data skew; rollback query, rate-limit và bổ sung extended statistics/index sau representative load test.

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
| Tối ưu/thiết kế xoay quanh API Slow | Kiểm soát rõ constraint chính | Tăng complexity và coupling | Metric chứng minh đây là bottleneck/risk |
| Giữ baseline đơn giản | Ít dependency, dễ debug | Có thể chạm giới hạn sớm | Traffic vừa, invariant vẫn được giữ |
| Managed service/library | Giảm vận hành hạ tầng | Cost, lock-in, giới hạn control | SLA và economics phù hợp |
| Tự vận hành/customize | Kiểm soát sâu | Ownership và failure surface lớn | Có năng lực vận hành và nhu cầu thật |

## 8. Interview Questions

### Basic / Mid-level (10)

- **B1.** What is API Slow, and which concrete problem does it address?
- **B2.** Explain the main internal mechanism behind API Slow.
- **B3.** Which guarantees does API Slow provide, and which does it not provide?
- **B4.** Which metrics or observations reveal the behavior of API Slow?
- **B5.** What is the most common misconception about API Slow?
- **B6.** How would you test assumptions involving API Slow?
- **B7.** Which edge cases or failure modes matter most for API Slow?
- **B8.** How can API Slow affect latency, throughput, memory, or correctness?
- **B9.** Which runtime conditions or configuration choices change the behavior of API Slow?
- **B10.** When is a different or simpler approach better than relying on API Slow?

### Production Scenarios (5)

- **S1.** A release involving API Slow triples p99 while averages look normal. How do you investigate and mitigate?
- **S2.** A critical dependency around API Slow is unavailable for ten minutes. Define degraded behavior and recovery.
- **S3.** Two concurrent operations expose a correctness gap related to API Slow. Which invariant and atomic boundary fix it?
- **S4.** Traffic grows from 1,000 to 20,000 RPS. Which measured limit involving API Slow fails first?
- **S5.** A canary changes the behavior of API Slow; success rate is flat but saturation rises. Promote or roll back?

## 9. Senior-level Questions

- **L1.** How does API Slow constrain the surrounding architecture and operational model?
- **L2.** Which subtle correctness issue appears when API Slow meets concurrency or partial failure?
- **L3.** What breaks first around API Slow at 20,000 RPS or 100× data volume?
- **L4.** Where should admission control or backpressure be placed when using API Slow?
- **L5.** How would you benchmark or validate API Slow without a misleading microbenchmark?
- **L6.** Which hidden coupling or migration cost can API Slow introduce?
- **L7.** How would you change a poor decision around API Slow with no downtime?
- **L8.** What production evidence would make you choose a different approach?
- **L9.** How do correctness, latency, cost, and complexity trade off for API Slow?
- **L10.** How would you turn an incident involving API Slow into a durable prevention mechanism?

## 10. Short Answers

**B1.** API slow là latency regression trên một hoặc nhiều percentile; average bình thường không loại trừ queueing, hot key hoặc một route/tenant bị ảnh hưởng. Trả lời tốt nối definition với constraint/invariant và một use case cụ thể.

**B2.** Mô tả state, lifecycle, boundary và failure path; không dừng ở public API của API Slow.

**B3.** Nêu lúc tạo, lúc sử dụng, lúc release/commit và điều xảy ra khi timeout hoặc cancellation.

**B4.** Đo customer impact, detection time, mitigation time, MTTR và recurrence; luôn tách average khỏi tail và success khỏi useful result.

**B5.** Lỗi phổ biến là dùng API Slow như mặc định mà không xác định ownership, limit và fallback.

**B6.** Test invariant trước, sau đó integration test failure path, concurrency và representative load.

**B7.** Xét timeout, duplicate, stale state, overload, dependency loss và recovery/reconciliation.

**B8.** Đo critical path, contention, queueing và amplification; throughput cao không bù được p99 xấu.

**B9.** Deadline, concurrency limit, retention/TTL, resource budget, telemetry và rollout policy phải explicit.

**B10.** Tránh API Slow khi bài toán đơn giản hơn giải được invariant với ít state và operational cost hơn.

Cấu trúc câu trả lời: **Definition → Why → How → Trade-off → Production example**. Với câu scenario: **stabilize → observe → hypothesize → verify → mitigate → prevent**.

## 11. Follow-up Questions

- **F1.** What assumption in your answer is most risky?
- **F2.** How would you prove that with metrics or an experiment?
- **F3.** What changes if the operation is not idempotent?
- **F4.** Where would you add timeout, retry, and backpressure?
- **F5.** What is your rollback and data-reconciliation plan?

## 12. Key Takeaways

- Nói được **vai trò, constraint hoặc invariant của API Slow**, không chỉ “dùng để làm gì”.
- Định lượng bằng customer impact, detection time, mitigation time, MTTR và recurrence và có baseline trước tối ưu.
- Thiết kế cho timeout, duplicate, overload, partial failure và recovery.
- Mọi tối ưu đều có chi phí về correctness, complexity, latency hoặc money.
- Production-ready nghĩa là có owner, alert, runbook, canary, rollback và reconciliation.
