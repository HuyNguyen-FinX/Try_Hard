# Repository theo use case

## Concept và Mental Model

Repository che storage mechanics khi domain cần persistence contract ổn định.

## How it works

Prefer GetOrder/ReserveStock transaction-aware operations thay generic CRUD đủ mọi table. Return structs khi implementation/API phù hợp; accept small interfaces tại consumer.

## Production Use Case

Store atomic method thực hiện conditional UPDATE và affected-row check.

## Failure Scenarios

Repository trả ORM session ra service; generic interface không biểu diễn transaction và locking.

## How I would debug this in production

Integration test invariant, SQL shape và cancellation; mock không chứng minh isolation.

## Trade-offs và When NOT to use

Reporting queries có thể dùng SQL trực tiếp trong adapter thay ép aggregate repository.

## Interview practice

Why can a generic repository hurt Go code? Nó giấu query semantics và thêm abstraction không cần thiết.

## Key Takeaways

Repository che storage mechanics khi domain cần persistence contract ổn định..


## See also

- [Interfaces: behavior, representation và typed nil](../01-go-core/interfaces.md)
- [Transactions và short critical sections](../08-database/transactions.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/modules/layout)

## Applied drill

So Reserve(ctx,itemID,n) atomic với Get→Set stock qua hai methods. Bản thứ hai buộc service biết transaction/locking và dễ oversell nếu fake tests không simulate concurrent callers. Repository tốt expose operation đủ diễn tả invariant, nhưng không nhồi orchestration external provider vào DB adapter. Query-specific read model có thể tách khỏi write repository.
