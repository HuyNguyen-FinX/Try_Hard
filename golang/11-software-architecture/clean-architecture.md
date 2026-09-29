# Clean Architecture theo tinh thần Go

## Concept và Mental Model

Dependency direction bảo vệ business policy khỏi transport/storage; không bắt buộc nhiều layer/class như Java.

## How it works

Domain package có concrete types và small consumer interfaces. Adapter implement implicit interface; cmd compose dependencies explicit.

## Production Use Case

Order service nhận Store interface gồm operations business cần, không mirror toàn ORM.

## Failure Scenarios

Interface mọi struct, DTO mapping lặp và generic base repository che transaction semantics.

## How I would debug this in production

Trace một use case qua imports; nếu thay HTTP làm domain đổi thì boundary chưa đúng.

## Trade-offs và When NOT to use

Abstraction cần lợi ích test/substitution; một package rõ thường tốt hơn nhiều layer rỗng.

## Interview practice

How would you keep domain independent of HTTP in Go? Methods nhận domain inputs/context và trả domain errors.

## Key Takeaways

Dependency direction bảo vệ business policy khỏi transport/storage; không bắt buộc nhiều layer/class như Java..


## See also

- [Interfaces: behavior, representation và typed nil](../01-go-core/interfaces.md)
- [Transactions và short critical sections](../08-database/transactions.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/modules/layout)
