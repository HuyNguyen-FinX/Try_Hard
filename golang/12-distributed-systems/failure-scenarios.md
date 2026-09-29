# Distributed failure matrix

## Concept và Mental Model

Mỗi network boundary có thể delay, drop, duplicate, reorder hoặc trả success nhưng response mất.

## How it works

Vẽ commit point rồi đặt crash trước/sau mỗi step; định nghĩa safety và liveness riêng, cùng recovery owner.

## Production Use Case

DB commit→outbox relay→consumer DB→offset commit có ít nhất ba replay boundaries.

## Failure Scenarios

DNS outage, partition, clock skew, dependency overload, stale leader, poisoned event và regional loss.

## How I would debug this in production

Timeline theo operation/event IDs, durable states và attempts; tránh kết luận từ log absence.

## Trade-offs và When NOT to use

Fail closed bảo vệ invariant nhưng giảm availability; stale fallback cần product approval ở design time.

## Interview practice

How would you test unknown outcomes? Cắt response sau durable commit rồi replay cùng operation ID.

## Key Takeaways

Mỗi network boundary có thể delay, drop, duplicate, reorder hoặc trả success nhưng response mất..


## See also

- [Idempotent consumer transaction](../10-messaging/idempotent-consumer.md)
- [system-design-framework](../13-system-design/system-design-framework.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.postgresql.org/docs/current/transaction-iso.html)
