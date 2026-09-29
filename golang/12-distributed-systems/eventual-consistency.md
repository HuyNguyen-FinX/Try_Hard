# Eventual consistency như product contract

## Concept và Mental Model

Async projections hội tụ nếu delivery/retry/merge assumptions giữ; UI phải biểu diễn pending/stale states.

## How it works

Version events theo aggregate, idempotent apply và reject stale updates; DLQ cần remediation để convergence thật.

## Production Use Case

Order status trả pending kèm polling/notification; reconciliation so source với projection.

## Failure Scenarios

Event bị bỏ vĩnh viễn; retry reorder làm state lùi; UI tuyên bố final khi projection chưa apply.

## How I would debug this in production

Freshness lag theo wall time, version gaps và reconciliation mismatch counts.

## Trade-offs và When NOT to use

Latency/availability tốt hơn nhưng client complexity và stale decisions tăng.

## Interview practice

What must be true for eventual convergence? Updates không mất vĩnh viễn và conflict resolution/application progress hoạt động.

## Key Takeaways

Async projections hội tụ nếu delivery/retry/merge assumptions giữ; UI phải biểu diễn pending/stale states..


## See also

- [Idempotent consumer transaction](../10-messaging/idempotent-consumer.md)
- [system-design-framework](../13-system-design/system-design-framework.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.postgresql.org/docs/current/transaction-iso.html)
