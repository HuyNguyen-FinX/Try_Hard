# Ai Job Queue

> **Phạm vi phỏng vấn:** AI Integration · **Ưu tiên:** P0/P1 · **Mindset:** Why → How → Trade-off → Production.

## 1. What is it?

AI job queue tách batch/long-running inference khỏi request path và hấp thụ burst theo GPU/provider capacity.

## 2. Why does it matter?

Senior Engineer cần hiểu **Ai Job Queue** để kiểm soát latency, quality, privacy và chi phí của dependency xác suất. Điểm phỏng vấn nằm ở khả năng nêu invariant, điều kiện áp dụng và failure behavior, không nằm ở việc thuộc định nghĩa.

## 3. How does it work?

Job state machine queued/running/succeeded/failed/cancelled; payload lớn ở object store, message chỉ chứa pointer/version. Lease/heartbeat, idempotent stage, delayed retry và DLQ/reconciliation.

Khi reasoning, đi theo chuỗi: **input → state transition → output → failure → recovery**. Quan sát `time-to-first-token, groundedness, token cost, retrieval recall và fallback rate` và phân biệt symptom, bottleneck với root cause.

## 4. Example

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class RetrievedChunk:
    document_id: str
    text: str
    score: float

def select_context(chunks: list[RetrievedChunk], *, min_score: float = 0.72) -> list[RetrievedChunk]:
    allowed = (chunk for chunk in chunks if chunk.score >= min_score)
    return sorted(allowed, key=lambda chunk: chunk.score, reverse=True)[:8]
```

**Ai Job Queue** cần thêm tenant ACL, model version, token budget, citation và quality evaluation ở production.

## 5. Production Use Case

Document embedding route theo model/dimension, batch theo token limit và scale worker bằng oldest-job-age trong quota provider.

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
| Tối ưu/thiết kế xoay quanh Ai Job Queue | Kiểm soát rõ constraint chính | Tăng complexity và coupling | Metric chứng minh đây là bottleneck/risk |
| Giữ baseline đơn giản | Ít dependency, dễ debug | Có thể chạm giới hạn sớm | Traffic vừa, invariant vẫn được giữ |
| Managed service/library | Giảm vận hành hạ tầng | Cost, lock-in, giới hạn control | SLA và economics phù hợp |
| Tự vận hành/customize | Kiểm soát sâu | Ownership và failure surface lớn | Có năng lực vận hành và nhu cầu thật |

## 8. Interview Questions

### Basic / Mid-level (10)

- **B1.** What is Ai Job Queue, and which concrete problem does it address?
- **B2.** Explain the main internal mechanism behind Ai Job Queue.
- **B3.** Which guarantees does Ai Job Queue provide, and which does it not provide?
- **B4.** Which metrics or observations reveal the behavior of Ai Job Queue?
- **B5.** What is the most common misconception about Ai Job Queue?
- **B6.** How would you test assumptions involving Ai Job Queue?
- **B7.** Which edge cases or failure modes matter most for Ai Job Queue?
- **B8.** How can Ai Job Queue affect latency, throughput, memory, or correctness?
- **B9.** Which runtime conditions or configuration choices change the behavior of Ai Job Queue?
- **B10.** When is a different or simpler approach better than relying on Ai Job Queue?

### Production Scenarios (5)

- **S1.** A release involving Ai Job Queue triples p99 while averages look normal. How do you investigate and mitigate?
- **S2.** A critical dependency around Ai Job Queue is unavailable for ten minutes. Define degraded behavior and recovery.
- **S3.** Two concurrent operations expose a correctness gap related to Ai Job Queue. Which invariant and atomic boundary fix it?
- **S4.** Traffic grows from 1,000 to 20,000 RPS. Which measured limit involving Ai Job Queue fails first?
- **S5.** A canary changes the behavior of Ai Job Queue; success rate is flat but saturation rises. Promote or roll back?

## 9. Senior-level Questions

- **L1.** How does Ai Job Queue constrain the surrounding architecture and operational model?
- **L2.** Which subtle correctness issue appears when Ai Job Queue meets concurrency or partial failure?
- **L3.** What breaks first around Ai Job Queue at 20,000 RPS or 100× data volume?
- **L4.** Where should admission control or backpressure be placed when using Ai Job Queue?
- **L5.** How would you benchmark or validate Ai Job Queue without a misleading microbenchmark?
- **L6.** Which hidden coupling or migration cost can Ai Job Queue introduce?
- **L7.** How would you change a poor decision around Ai Job Queue with no downtime?
- **L8.** What production evidence would make you choose a different approach?
- **L9.** How do correctness, latency, cost, and complexity trade off for Ai Job Queue?
- **L10.** How would you turn an incident involving Ai Job Queue into a durable prevention mechanism?

## 10. Short Answers

**B1.** AI job queue tách batch/long-running inference khỏi request path và hấp thụ burst theo GPU/provider capacity. Trả lời tốt nối definition với constraint/invariant và một use case cụ thể.

**B2.** Mô tả state, lifecycle, boundary và failure path; không dừng ở public API của Ai Job Queue.

**B3.** Nêu lúc tạo, lúc sử dụng, lúc release/commit và điều xảy ra khi timeout hoặc cancellation.

**B4.** Đo time-to-first-token, groundedness, token cost, retrieval recall và fallback rate; luôn tách average khỏi tail và success khỏi useful result.

**B5.** Lỗi phổ biến là dùng Ai Job Queue như mặc định mà không xác định ownership, limit và fallback.

**B6.** Test invariant trước, sau đó integration test failure path, concurrency và representative load.

**B7.** Xét timeout, duplicate, stale state, overload, dependency loss và recovery/reconciliation.

**B8.** Đo critical path, contention, queueing và amplification; throughput cao không bù được p99 xấu.

**B9.** Deadline, concurrency limit, retention/TTL, resource budget, telemetry và rollout policy phải explicit.

**B10.** Tránh Ai Job Queue khi bài toán đơn giản hơn giải được invariant với ít state và operational cost hơn.

Cấu trúc câu trả lời: **Definition → Why → How → Trade-off → Production example**. Với câu scenario: **stabilize → observe → hypothesize → verify → mitigate → prevent**.

## 11. Follow-up Questions

- **F1.** What assumption in your answer is most risky?
- **F2.** How would you prove that with metrics or an experiment?
- **F3.** What changes if the operation is not idempotent?
- **F4.** Where would you add timeout, retry, and backpressure?
- **F5.** What is your rollback and data-reconciliation plan?

## 12. Key Takeaways

- Nói được **vai trò, constraint hoặc invariant của Ai Job Queue**, không chỉ “dùng để làm gì”.
- Định lượng bằng time-to-first-token, groundedness, token cost, retrieval recall và fallback rate và có baseline trước tối ưu.
- Thiết kế cho timeout, duplicate, overload, partial failure và recovery.
- Mọi tối ưu đều có chi phí về correctness, complexity, latency hoặc money.
- Production-ready nghĩa là có owner, alert, runbook, canary, rollback và reconciliation.
