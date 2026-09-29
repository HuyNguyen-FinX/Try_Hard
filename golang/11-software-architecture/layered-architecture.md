# Layered architecture và vertical features

## Concept và Mental Model

Layering tổ chức responsibility; dependency direction cần rõ hơn số thư mục.

## How it works

Handler parse/auth/map errors; service giữ invariant; store queries. Packages theo domain giảm cross-feature imports.

## Production Use Case

user/ có service/store contract và adapters theo độ lớn, không bắt đầu bằng hàng chục global layers.

## Failure Scenarios

Handler gọi ORM bypass service; service chỉ pass-through khiến abstraction không thêm giá trị.

## How I would debug this in production

Review transaction boundaries và import cycles; map change impact của một feature.

## Trade-offs và When NOT to use

Small CRUD có thể gộp layers nếu contract vẫn rõ; đừng thêm layer rỗng.

## Interview practice

When is a service layer useful? Khi điều phối invariant/workflow, không chỉ rename repository method.

## Key Takeaways

Layering tổ chức responsibility; dependency direction cần rõ hơn số thư mục..


## See also

- [Interfaces: behavior, representation và typed nil](../01-go-core/interfaces.md)
- [Transactions và short critical sections](../08-database/transactions.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/modules/layout)

## Applied drill

Use case create order cần validate business rule, reserve local inventory và insert outbox cùng transaction. Nếu mỗi repository method tự Begin/Commit, service layer nhìn đẹp nhưng không còn atomicity. Truyền transaction-scoped store hoặc đặt atomic operation tại persistence boundary; tests kiểm lỗi statement thứ hai không để lại nửa state. Đừng thêm layer để che boundary bị sai.
