# Celery Task Duplicate

> **Phạm vi phỏng vấn:** Production Scenario · **Ưu tiên:** P0/P1 · **Mindset:** Why → How → Trade-off → Production.

## 1. What is it?

Celery task duplicate là hệ quả bình thường của at-least-once delivery khi worker crash/lease hết hạn/ack thất lạc; task ID giống hay khác không quyết định business idempotency.

## 2. Why does it matter?

Senior Engineer cần hiểu **Celery Task Duplicate** để Senior Engineer phải giảm impact trước, tìm nguyên nhân bằng evidence và phòng tái diễn. Điểm phỏng vấn nằm ở khả năng nêu invariant, điều kiện áp dụng và failure behavior, không nằm ở việc thuộc định nghĩa.

## 3. How does it work?

Thiết kế idempotency theo business key bằng unique constraint/inbox, ack/visibility timeout hợp task runtime, retry có classification/backoff. Lock chỉ giảm concurrent duplicate; DB invariant và reconciliation mới bảo vệ effect.

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

Task tạo report commit artifact rồi crash trước ack; lần chạy lại thấy unique job-stage đã complete và trả artifact cũ, không generate/upload thêm.

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
| Tối ưu/thiết kế xoay quanh Celery Task Duplicate | Kiểm soát rõ constraint chính | Tăng complexity và coupling | Metric chứng minh đây là bottleneck/risk |
| Giữ baseline đơn giản | Ít dependency, dễ debug | Có thể chạm giới hạn sớm | Traffic vừa, invariant vẫn được giữ |
| Managed service/library | Giảm vận hành hạ tầng | Cost, lock-in, giới hạn control | SLA và economics phù hợp |
| Tự vận hành/customize | Kiểm soát sâu | Ownership và failure surface lớn | Có năng lực vận hành và nhu cầu thật |

## 8. Interview Questions

### Basic / Mid-level (10)

- **B1.** What is Celery Task Duplicate, and which concrete problem does it address?
- **B2.** Explain the main internal mechanism behind Celery Task Duplicate.
- **B3.** Which guarantees does Celery Task Duplicate provide, and which does it not provide?
- **B4.** Which metrics or observations reveal the behavior of Celery Task Duplicate?
- **B5.** What is the most common misconception about Celery Task Duplicate?
- **B6.** How would you test assumptions involving Celery Task Duplicate?
- **B7.** Which edge cases or failure modes matter most for Celery Task Duplicate?
- **B8.** How can Celery Task Duplicate affect latency, throughput, memory, or correctness?
- **B9.** Which runtime conditions or configuration choices change the behavior of Celery Task Duplicate?
- **B10.** When is a different or simpler approach better than relying on Celery Task Duplicate?

### Production Scenarios (5)

- **S1.** A worker completes a task then crashes before ack. Trace the redelivery and safe business behavior.
- **S2.** A task sends email then retries after timeout. How do provider idempotency and a delivery ledger help?
- **S3.** A Redis lock expires during a long task. Why is the lock insufficient, and which DB constraint is authoritative?
- **S4.** A poison task retries forever and blocks useful work. Design retry classification and quarantine.
- **S5.** A deploy terminates workers mid-task. Explain graceful drain, visibility timeout, and reconciliation.

## 9. Senior-level Questions

- **L1.** How does Celery Task Duplicate constrain the surrounding architecture and operational model?
- **L2.** Which subtle correctness issue appears when Celery Task Duplicate meets concurrency or partial failure?
- **L3.** What breaks first around Celery Task Duplicate at 20,000 RPS or 100× data volume?
- **L4.** Where should admission control or backpressure be placed when using Celery Task Duplicate?
- **L5.** How would you benchmark or validate Celery Task Duplicate without a misleading microbenchmark?
- **L6.** Which hidden coupling or migration cost can Celery Task Duplicate introduce?
- **L7.** How would you change a poor decision around Celery Task Duplicate with no downtime?
- **L8.** What production evidence would make you choose a different approach?
- **L9.** How do correctness, latency, cost, and complexity trade off for Celery Task Duplicate?
- **L10.** How would you turn an incident involving Celery Task Duplicate into a durable prevention mechanism?

## 10. Short Answers

**B1.** Celery task duplicate là hệ quả bình thường của at-least-once delivery khi worker crash/lease hết hạn/ack thất lạc; task ID giống hay khác không quyết định business idempotency. Trả lời tốt nối definition với constraint/invariant và một use case cụ thể.

**B2.** Mô tả state, lifecycle, boundary và failure path; không dừng ở public API của Celery Task Duplicate.

**B3.** Nêu lúc tạo, lúc sử dụng, lúc release/commit và điều xảy ra khi timeout hoặc cancellation.

**B4.** Đo customer impact, detection time, mitigation time, MTTR và recurrence; luôn tách average khỏi tail và success khỏi useful result.

**B5.** Lỗi phổ biến là dùng Celery Task Duplicate như mặc định mà không xác định ownership, limit và fallback.

**B6.** Test invariant trước, sau đó integration test failure path, concurrency và representative load.

**B7.** Xét timeout, duplicate, stale state, overload, dependency loss và recovery/reconciliation.

**B8.** Đo critical path, contention, queueing và amplification; throughput cao không bù được p99 xấu.

**B9.** Deadline, concurrency limit, retention/TTL, resource budget, telemetry và rollout policy phải explicit.

**B10.** Tránh Celery Task Duplicate khi bài toán đơn giản hơn giải được invariant với ít state và operational cost hơn.

Cấu trúc câu trả lời: **Definition → Why → How → Trade-off → Production example**. Với câu scenario: **stabilize → observe → hypothesize → verify → mitigate → prevent**.

## 11. Follow-up Questions

- **F1.** What assumption in your answer is most risky?
- **F2.** How would you prove that with metrics or an experiment?
- **F3.** What changes if the operation is not idempotent?
- **F4.** Where would you add timeout, retry, and backpressure?
- **F5.** What is your rollback and data-reconciliation plan?

## 12. Key Takeaways

- Nói được **vai trò, constraint hoặc invariant của Celery Task Duplicate**, không chỉ “dùng để làm gì”.
- Định lượng bằng customer impact, detection time, mitigation time, MTTR và recurrence và có baseline trước tối ưu.
- Thiết kế cho timeout, duplicate, overload, partial failure và recovery.
- Mọi tối ưu đều có chi phí về correctness, complexity, latency hoặc money.
- Production-ready nghĩa là có owner, alert, runbook, canary, rollback và reconciliation.
