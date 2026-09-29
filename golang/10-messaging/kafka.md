# Kafka với Go: commit boundary

## Concept và Mental Model

Kafka giữ append-only logs theo partition; producer publish records, consumer group chia partitions và theo dõi offsets.

## How it works

Key quyết định partition/order scope. Consumer xử lý DB commit rồi commit offset có crash window tạo redelivery. Commit trước DB có nguy cơ mất effect. Go client cần versioned API, bounded polling/processing và shutdown.

## Production Use Case

DB effect và processed_event unique record cùng transaction; sau commit mới advance contiguous offset.

## Failure Scenarios

Crash sau DB commit trước offset commit: message được đọc lại, idempotent transaction phải no-op an toàn.

## How I would debug this in production

Lag theo partition, oldest event age, processing rate/errors/rebalances; correlate DB latency.

## Trade-offs và When NOT to use

At-least-once dễ implement nhưng cần dedup; Kafka transaction không tự bao external DB.

## Interview practice

What happens after DB success but before offset commit? Redelivery; unique event ID và effect cùng DB transaction ngăn lặp.

## Key Takeaways

Kafka giữ append-only logs theo partition; producer publish records, consumer group chia partitions và theo dõi offsets..


## See also

- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kafka.apache.org/41/design/design/)
