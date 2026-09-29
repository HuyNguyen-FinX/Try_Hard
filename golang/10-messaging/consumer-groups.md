# Consumer groups và rebalancing

## Concept và Mental Model

Một consumer group chia ownership partitions; groups khác nhau có progress độc lập.

## How it works

Active consumers hữu ích bị giới hạn bởi partitions theo protocol thông thường. Rebalance revoke ownership: stop dispatch, handle/drain in-flight và commit chỉ phần completed còn hợp lệ.

## Production Use Case

Scale workers trong pod có per-partition sequencing hoặc bounded parallel processing với contiguous commit tracking.

## Failure Scenarios

Commit từ stale owner; long task vượt poll/liveness constraints; rebalance storm do scale liên tục.

## How I would debug this in production

Assignment churn, rebalance duration, partition lag và task duration distribution.

## Trade-offs và When NOT to use

Nhiều consumers hơn partitions không thêm parallelism; tăng partitions có ordering/key mapping implications.

## Interview practice

How do you prevent committing unfinished work during rebalance? Ownership-aware drain/cancel và contiguous offsets.

## Key Takeaways

Một consumer group chia ownership partitions; groups khác nhau có progress độc lập..


## See also

- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kafka.apache.org/41/design/design/)
