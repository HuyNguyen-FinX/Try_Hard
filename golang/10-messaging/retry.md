# Message retries và poison data

## Concept và Mental Model

Retry cần phân loại transient/permanent, delay, max age và replay-safe effect.

## How it works

Retry-in-place giữ order nhưng block partition; retry topic cho progress nhưng có thể reorder key. Dùng attempts/original ID và exponential jitter; DLQ sau policy.

## Production Use Case

DB transient retry trong short budget rồi park record; validation error vào quarantine với reason.

## Failure Scenarios

Immediate requeue chiếm CPU/broker; retry tạo new ID làm dedup thất bại.

## How I would debug this in production

Retry attempts, age, categories, original correlation ID và fresh-work throughput.

## Trade-offs và When NOT to use

Không retry vô hạn; quyết định ordering khi tách retry lane.

## Interview practice

How does a retry topic affect per-key ordering? Later records có thể vượt failed record.

## Key Takeaways

Retry cần phân loại transient/permanent, delay, max age và replay-safe effect..


## See also

- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kafka.apache.org/41/design/design/)

## Applied drill

Xét recordA1 lỗi, A2 cùng key tới sau. Retry-in-place giữ A2 chờ, tăng latency nhưng giữ order. Retry topic cho A2 chạy sớm nên target cần version guard hoặc park key tới khi A1 resolved. Nêu rõ policy cho poison message: bỏ qua có thể phá aggregate state, vì vậy DLQ phải đi cùng blocked-key/reconciliation decision.
