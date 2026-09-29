# Service giữ business orchestration

## Concept và Mental Model

Service phối hợp dependencies và invariant một use case; không phải singleton global chứa mọi state.

## How it works

Constructor nhận explicit stores/clients/clock; method nhận context và command typed. Error mapping HTTP ở adapter.

## Production Use Case

Checkout ghi order/outbox trong một transaction rồi trả accepted state.

## Failure Scenarios

Service giữ request ctx trong field; gọi external provider giữa DB transaction.

## How I would debug this in production

Test failure từng boundary và review resource ownership trong constructor/lifecycle.

## Trade-offs và When NOT to use

Stateless service dễ share; mutable cache cần synchronization riêng.

## Interview practice

Which dependencies belong in a constructor versus context? Stable services trong constructor, request lifetime/metadata trong ctx.

## Key Takeaways

Service phối hợp dependencies và invariant một use case; không phải singleton global chứa mọi state..


## See also

- [Interfaces: behavior, representation và typed nil](../01-go-core/interfaces.md)
- [Transactions và short critical sections](../08-database/transactions.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/modules/layout)

## Applied drill

Service method Checkout nhận typed command và ctx, trả order ID/state/error; HTTP status mapping ở handler. Khi provider call timeout sau possible charge, service trả/persist unknown state thay báo failed chắc chắn. Business tests dùng fake provider có ambiguous outcome; infrastructure tests kiểm request deadlines và body cleanup. Điều này giữ domain semantics rõ hơn pass-through wrappers.
