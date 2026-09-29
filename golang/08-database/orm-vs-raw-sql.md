# ORM, raw SQL và query ownership

## Concept và Mental Model

Chọn abstraction theo query visibility, type safety và team workflow; Go không buộc một ORM.

## How it works

ORM giảm CRUD boilerplate; raw SQL kiểm soát plans; generated SQL như sqlc giữ query explicit và typed methods. Tất cả cần constraints/transactions.

## Production Use Case

Query reporting phức tạp dùng SQL reviewable; CRUD đơn giản có thể dùng ORM nếu đo N+1 và transaction boundaries.

## Failure Scenarios

Lazy loading N+1; query hidden trong loop; abstraction không expose timeout/Tx.

## How I would debug this in production

Đếm queries/request, đọc emitted SQL và EXPLAIN trên dữ liệu đại diện.

## Trade-offs và When NOT to use

Không bọc ORM bằng generic repository tới mức mất khả năng tối ưu query.

## Interview practice

What matters more than ORM versus raw SQL? Query shape, indexes, ownership và measurable behavior.

## Key Takeaways

Chọn abstraction theo query visibility, type safety và team workflow; Go không buộc một ORM..


## See also

- [database/sql: pool handle, rows và transaction ownership](database-sql.md)
- [Database connection pool: 500 requests và 20 connections](database-sql-pool.md)
- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/database/)
