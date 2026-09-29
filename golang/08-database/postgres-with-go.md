# PostgreSQL với Go

## Concept và Mental Model

Go client cần contract về types, transactions, cancellation và schema evolution.

## How it works

Use parameterized SQL, scan nullable fields vào explicit nullable types/pointers, UTC/time semantics rõ và numeric types không mất precision. Migration expand-contract phối hợp rolling versions.

## Production Use Case

Insert idempotency key + domain state + outbox trong một transaction.

## Failure Scenarios

Float64 dùng cho money; timestamp timezone sai; app version mới yêu cầu column trước migration.

## How I would debug this in production

Integration tests trên PostgreSQL thật đúng major; log SQLSTATE/query name thay raw sensitive parameters.

## Trade-offs và When NOT to use

Postgres features tốt nhưng tăng vendor coupling; dùng khi invariant/query benefits rõ.

## Interview practice

How would you deploy a schema change without breaking old pods? Expand schema trước, dual compatibility rồi contract sau.

## Key Takeaways

Go client cần contract về types, transactions, cancellation và schema evolution..


## See also

- [database/sql: pool handle, rows và transaction ownership](database-sql.md)
- [Database connection pool: 500 requests và 20 connections](database-sql-pool.md)
- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/database/)
