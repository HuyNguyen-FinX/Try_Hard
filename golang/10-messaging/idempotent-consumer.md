# Idempotent consumer transaction

## Concept và Mental Model

Dedup record và business effect phải atomic trong cùng durable boundary để replay không double-apply.

## How it works

INSERT processed_events(event_id) với unique key rồi mutation trong cùng transaction; duplicate no-op, commit rồi ack/offset. Retention dài hơn replay horizon.

## Production Use Case

Ledger event có unique event ID; outbox từ transaction phát downstream event.

## Failure Scenarios

Mark processed trước effect nhưng khác transaction làm mất effect; effect trước dedup khác transaction làm duplicate.

## How I would debug this in production

Crash injection quanh begin/dedup/effect/commit/ack; reconcile expected state.

## Trade-offs và When NOT to use

Dedup store tốn space; business natural idempotency như versioned upsert có thể đơn giản hơn.

## Interview practice

Why must dedup and effect share one transaction? Bất kỳ crash window tách hai việc đều có thể mất hoặc lặp effect.

## Key Takeaways

Dedup record và business effect phải atomic trong cùng durable boundary để replay không double-apply..


## See also

- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kafka.apache.org/41/design/design/)
