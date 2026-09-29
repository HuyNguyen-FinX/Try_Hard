# pgx native và database/sql adapter

## Concept và Mental Model

pgx cung cấp PostgreSQL-specific API và pgxpool; stdlib adapter cho code dùng database/sql.

## How it works

Pool/connection lifecycle khác API; native Conn không dùng concurrent tùy ý. Close Rows, BatchResults, release acquired conn; COPY/batch tăng throughput nhưng cần bounded batches.

## Production Use Case

Bulk migration dùng CopyFrom/staging + merge với checkpoint sau commit.

## Failure Scenarios

Quên close BatchResults giữ connection; tạo cả sql.DB và pgxpool vô tình nhân budget.

## How I would debug this in production

Dùng pgxpool.Stat acquire duration/empty acquire counts và PostgreSQL waits; cancellation test với version driver đã pin.

## Trade-offs và When NOT to use

Native features đổi portability; sql.DB phù hợp generic adapters nhưng không cần bọc cả hai layers.

## Interview practice

Why is pgx.Conn different from pgxpool.Pool for sharing? Conn là single connection, Pool quản lý concurrent acquisition.

## Key Takeaways

pgx cung cấp PostgreSQL-specific API và pgxpool; stdlib adapter cho code dùng database/sql..


## See also

- [database/sql: pool handle, rows và transaction ownership](database-sql.md)
- [Database connection pool: 500 requests và 20 connections](database-sql-pool.md)
- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/github.com/jackc/pgx/v5)
