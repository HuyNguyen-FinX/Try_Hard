# Event-driven Go service lifecycle

## Concept và Mental Model

Event-driven code vẫn cần explicit owners cho client, poll loop, worker pool, checkpoint và shutdown.

## How it works

Poll bounded batches, dispatch theo partition/order policy, context-aware processing, durable effect, commit contiguous progress. Không share unsafe client handles trái contract.

## Production Use Case

Outbox relay publish stable event IDs; consumer service có service context tách HTTP request.

## Failure Scenarios

Background errors bị bỏ; Close broker trước workers commit; concurrent handler mutation không sync.

## How I would debug this in production

Trace links qua event headers, lag/age metrics và structured event ID logs sampled.

## Trade-offs và When NOT to use

Async decoupling thêm eventual consistency và replay burden; synchronous path tốt cho immediate invariant.

## Interview practice

What must be joined before closing a consumer client? Poll/dispatch/processing/commit owners theo library lifecycle.

## Key Takeaways

Event-driven code vẫn cần explicit owners cho client, poll loop, worker pool, checkpoint và shutdown..


## See also

- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kafka.apache.org/41/design/design/)
