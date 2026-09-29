# DDD: invariants và bounded contexts

## Concept và Mental Model

DDD giúp ngôn ngữ nghiệp vụ và consistency boundary rõ; không bắt buộc aggregate cho mọi row.

## How it works

Aggregate bảo vệ invariant trong transaction boundary; domain event nêu fact đã xảy ra. Bounded context có model riêng, mapping ở integration boundary.

## Production Use Case

Payment ledger khác order fulfillment; saga điều phối giữa contexts.

## Failure Scenarios

Aggregate quá lớn gây lock contention; event phát trước commit; dùng một User model toàn công ty.

## How I would debug this in production

Hỏi invariant cần atomic ở đâu và domain experts gọi trạng thái thế nào.

## Trade-offs và When NOT to use

DDD hữu ích domain phức tạp; CRUD đơn giản không cần ceremony.

## Interview practice

How do you choose aggregate boundaries? Theo invariant và transaction contention, không theo ERD đơn thuần.

## Key Takeaways

DDD giúp ngôn ngữ nghiệp vụ và consistency boundary rõ; không bắt buộc aggregate cho mọi row..


## See also

- [Interfaces: behavior, representation và typed nil](../01-go-core/interfaces.md)
- [Transactions và short critical sections](../08-database/transactions.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/modules/layout)
