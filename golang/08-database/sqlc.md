# sqlc: SQL làm contract

## Concept và Mental Model

sqlc generate typed Go methods từ schema/query definitions, không thay runtime DB validation.

## How it works

Pin generator version, review SQL và generated diff; tx-bound queries dùng WithTx hoặc DBTX pattern theo generated API. Schema input phải khớp migrations.

## Production Use Case

Checkout queries giữ type-safe scan và SQL dễ review.

## Failure Scenarios

Generated code compile nhưng production schema khác; optional filters tạo query plan kém.

## How I would debug this in production

Regenerate trong CI và fail dirty diff; integration test query trên migrated database.

## Trade-offs và When NOT to use

Generated API tốt cho stable SQL; highly dynamic query builder có thể cần cách khác.

## Interview practice

Does generated code eliminate integration tests? Không, plans/schema/runtime semantics còn phải kiểm chứng.

## Key Takeaways

sqlc generate typed Go methods từ schema/query definitions, không thay runtime DB validation..


## See also

- [database/sql: pool handle, rows và transaction ownership](database-sql.md)
- [Database connection pool: 500 requests và 20 connections](database-sql-pool.md)
- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://docs.sqlc.dev/en/stable/)
