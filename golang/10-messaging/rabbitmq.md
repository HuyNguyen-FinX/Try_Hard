# RabbitMQ acknowledgments và routing

## Concept và Mental Model

RabbitMQ broker route messages tới queues; ack xác nhận consumer đã xử lý theo application contract.

## How it works

Manual ack sau durable effect; prefetch bound unacked delivery. Publisher confirm nói broker nhận theo queue durability config, khác consumer ack.

## Production Use Case

Task queue với routing keys, retry delay và dead-letter policy; Go channel/connection recovery theo client contract.

## Failure Scenarios

Auto-ack trước work mất task khi crash; nack requeue ngay tạo poison-message loop.

## How I would debug this in production

Ready/unacked counts, redeliveries, consumer utilization và confirm latency.

## Trade-offs và When NOT to use

Kafka hợp replay log; RabbitMQ hợp routing/task queue; quorum/durability settings cần explicit.

## Interview practice

Does publisher confirmation mean business processing finished? Không, chỉ broker acceptance theo cấu hình.

## Key Takeaways

RabbitMQ broker route messages tới queues; ack xác nhận consumer đã xử lý theo application contract..


## See also

- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.rabbitmq.com/docs/confirms)
