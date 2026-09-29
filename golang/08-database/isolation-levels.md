# Isolation levels trong PostgreSQL

## Concept và Mental Model

Isolation nói transaction quan sát concurrent changes thế nào, không thay mọi business constraint.

## How it works

Read Committed có snapshot mỗi statement; Repeatable Read giữ transaction snapshot nhưng có write skew; Serializable có thể abort và yêu cầu retry. PostgreSQL Read Uncommitted xử lý như Read Committed.

## Production Use Case

Reservation invariant nhiều rows có thể cần serializable hoặc explicit locking/constraint.

## Failure Scenarios

Hai transactions cùng đọc điều kiện đúng rồi update rows khác làm invariant sai dưới snapshot isolation.

## How I would debug this in production

Dựng hai sessions với barriers để quan sát anomalies; đọc SQLSTATE 40001 và plans/locks.

## Trade-offs và When NOT to use

Mạnh hơn tăng abort/cost; chọn từ invariant, không default nâng mọi query.

## Interview practice

Does Repeatable Read prevent all anomalies? Không, serialization anomalies như write skew vẫn có thể xảy ra.

## Key Takeaways

Isolation nói transaction quan sát concurrent changes thế nào, không thay mọi business constraint..


## See also

- [database/sql: pool handle, rows và transaction ownership](database-sql.md)
- [Database connection pool: 500 requests và 20 connections](database-sql-pool.md)
- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.postgresql.org/docs/current/transaction-iso.html)
