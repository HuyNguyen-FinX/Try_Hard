# Duplicate Message

> **Phạm vi phỏng vấn:** Production Scenario · **Ưu tiên:** P0/P1 · **Mindset:** Why → How → Trade-off → Production.

## 1. What is it?

Duplicate message là delivery lặp do ack timeout, producer retry, broker failover hoặc consumer crash; broker delivery và business effect là hai scope khác nhau.

## 2. Why does it matter?

Senior Engineer cần hiểu **Duplicate Message** để Senior Engineer phải giảm impact trước, tìm nguyên nhân bằng evidence và phòng tái diễn. Điểm phỏng vấn nằm ở khả năng nêu invariant, điều kiện áp dụng và failure behavior, không nằm ở việc thuộc định nghĩa.

## 3. How does it work?

Gắn immutable message/event ID và business key; consumer atomically insert inbox/unique row cùng state transition. Ack sau durable effect, retry transient, duplicate trả success; external side effect dùng provider key/ledger và reconciliation.

Khi reasoning, đi theo chuỗi: **input → state transition → output → failure → recovery**. Quan sát `customer impact, detection time, mitigation time, MTTR và recurrence` và phân biệt symptom, bottleneck với root cause.

## 4. Example

```sql
CREATE TABLE processed_request (
    tenant_id bigint NOT NULL,
    idempotency_key text NOT NULL,
    request_hash text NOT NULL,
    response jsonb,
    created_at timestamptz NOT NULL DEFAULT now(),
    PRIMARY KEY (tenant_id, idempotency_key)
);
```

`INSERT ... ON CONFLICT` phải nằm cùng transaction với business write; cùng key nhưng khác `request_hash` bị từ chối.

## 5. Production Use Case

`ClaimApproved` đến hai lần nhưng unique `(consumer, event_id)` khiến settlement chỉ ghi một ledger entry; projection có thể replay từ log.

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
| Tối ưu/thiết kế xoay quanh Duplicate Message | Kiểm soát rõ constraint chính | Tăng complexity và coupling | Metric chứng minh đây là bottleneck/risk |
| Giữ baseline đơn giản | Ít dependency, dễ debug | Có thể chạm giới hạn sớm | Traffic vừa, invariant vẫn được giữ |
| Managed service/library | Giảm vận hành hạ tầng | Cost, lock-in, giới hạn control | SLA và economics phù hợp |
| Tự vận hành/customize | Kiểm soát sâu | Ownership và failure surface lớn | Có năng lực vận hành và nhu cầu thật |

## 8. Interview Questions

### Basic / Mid-level (10)

- **B1.** What is Duplicate Message, and which concrete problem does it address?
- **B2.** Explain the main internal mechanism behind Duplicate Message.
- **B3.** Which guarantees does Duplicate Message provide, and which does it not provide?
- **B4.** Which metrics or observations reveal the behavior of Duplicate Message?
- **B5.** What is the most common misconception about Duplicate Message?
- **B6.** How would you test assumptions involving Duplicate Message?
- **B7.** Which edge cases or failure modes matter most for Duplicate Message?
- **B8.** How can Duplicate Message affect latency, throughput, memory, or correctness?
- **B9.** Which runtime conditions or configuration choices change the behavior of Duplicate Message?
- **B10.** When is a different or simpler approach better than relying on Duplicate Message?

### Production Scenarios (5)

- **S1.** A release involving Duplicate Message triples p99 while averages look normal. How do you investigate and mitigate?
- **S2.** A critical dependency around Duplicate Message is unavailable for ten minutes. Define degraded behavior and recovery.
- **S3.** Two concurrent operations expose a correctness gap related to Duplicate Message. Which invariant and atomic boundary fix it?
- **S4.** Traffic grows from 1,000 to 20,000 RPS. Which measured limit involving Duplicate Message fails first?
- **S5.** A canary changes the behavior of Duplicate Message; success rate is flat but saturation rises. Promote or roll back?

## 9. Senior-level Questions

- **L1.** How does Duplicate Message constrain the surrounding architecture and operational model?
- **L2.** Which subtle correctness issue appears when Duplicate Message meets concurrency or partial failure?
- **L3.** What breaks first around Duplicate Message at 20,000 RPS or 100× data volume?
- **L4.** Where should admission control or backpressure be placed when using Duplicate Message?
- **L5.** How would you benchmark or validate Duplicate Message without a misleading microbenchmark?
- **L6.** Which hidden coupling or migration cost can Duplicate Message introduce?
- **L7.** How would you change a poor decision around Duplicate Message with no downtime?
- **L8.** What production evidence would make you choose a different approach?
- **L9.** How do correctness, latency, cost, and complexity trade off for Duplicate Message?
- **L10.** How would you turn an incident involving Duplicate Message into a durable prevention mechanism?

## 10. Short Answers

**B1.** Duplicate message là delivery lặp do ack timeout, producer retry, broker failover hoặc consumer crash; broker delivery và business effect là hai scope khác nhau. Trả lời tốt nối definition với constraint/invariant và một use case cụ thể.

**B2.** Mô tả state, lifecycle, boundary và failure path; không dừng ở public API của Duplicate Message.

**B3.** Nêu lúc tạo, lúc sử dụng, lúc release/commit và điều xảy ra khi timeout hoặc cancellation.

**B4.** Đo customer impact, detection time, mitigation time, MTTR và recurrence; luôn tách average khỏi tail và success khỏi useful result.

**B5.** Lỗi phổ biến là dùng Duplicate Message như mặc định mà không xác định ownership, limit và fallback.

**B6.** Test invariant trước, sau đó integration test failure path, concurrency và representative load.

**B7.** Xét timeout, duplicate, stale state, overload, dependency loss và recovery/reconciliation.

**B8.** Đo critical path, contention, queueing và amplification; throughput cao không bù được p99 xấu.

**B9.** Deadline, concurrency limit, retention/TTL, resource budget, telemetry và rollout policy phải explicit.

**B10.** Tránh Duplicate Message khi bài toán đơn giản hơn giải được invariant với ít state và operational cost hơn.

Cấu trúc câu trả lời: **Definition → Why → How → Trade-off → Production example**. Với câu scenario: **stabilize → observe → hypothesize → verify → mitigate → prevent**.

## 11. Follow-up Questions

- **F1.** What assumption in your answer is most risky?
- **F2.** How would you prove that with metrics or an experiment?
- **F3.** What changes if the operation is not idempotent?
- **F4.** Where would you add timeout, retry, and backpressure?
- **F5.** What is your rollback and data-reconciliation plan?

## 12. Key Takeaways

- Nói được **vai trò, constraint hoặc invariant của Duplicate Message**, không chỉ “dùng để làm gì”.
- Định lượng bằng customer impact, detection time, mitigation time, MTTR và recurrence và có baseline trước tối ưu.
- Thiết kế cho timeout, duplicate, overload, partial failure và recovery.
- Mọi tối ưu đều có chi phí về correctness, complexity, latency hoặc money.
- Production-ready nghĩa là có owner, alert, runbook, canary, rollback và reconciliation.
