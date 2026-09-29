# Partitions: ordering và scale unit

## Concept và Mental Model

Partition là ordering/replay/ownership unit; ordering toàn topic không được đảm bảo qua nhiều partitions.

## How it works

Partition key theo business aggregate giữ order cần thiết; hot keys hạn chế throughput. Tăng partition count có thể đổi key mapping tùy partitioner.

## Production Use Case

Order events theo order_id, migration CDC theo source primary key hoặc transaction protocol cần thiết.

## Failure Scenarios

Một tenant cực hot làm lag một partition; globally ordered design chỉ dùng một partition thành bottleneck.

## How I would debug this in production

Per-partition rates/lag/skew, sample key distribution và consumer utilization.

## Trade-offs và When NOT to use

Nhiều partitions tăng parallelism/metadata/operational overhead; chọn từ expected throughput và key semantics.

## Interview practice

Why is partition count a correctness decision? Nó liên quan order scope và repartition behavior.

## Key Takeaways

Partition là ordering/replay/ownership unit; ordering toàn topic không được đảm bảo qua nhiều partitions..


## See also

- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kafka.apache.org/41/design/design/)
