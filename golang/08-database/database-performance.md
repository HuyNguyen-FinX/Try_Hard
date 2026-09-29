# Database performance bằng query evidence

## Concept và Mental Model

Latency DB gồm acquire, network, execution, lock waits và result consumption.

## How it works

Index cần match filters/order; selective composite indexes khác independent single indexes. EXPLAIN ANALYZE thực thi query, BUFFERS cho IO/cache clues; cập nhật statistics theo data churn.

## Production Use Case

Keyset pagination trên (created_at,id), bounded result columns và batch writes theo commit budget.

## Failure Scenarios

Unselective index không giúp; N+1, hot rows, stale stats, autovacuum pressure và long snapshots.

## How I would debug this in production

Query fingerprint + latency distributions, waits, plans và cardinality estimate errors; test realistic data volume.

## Trade-offs và When NOT to use

Index tăng read performance nhưng thêm write/storage cost; không index mọi column.

## Interview practice

How would you distinguish slow execution from pool wait? Spans và database/sql stats cùng server query timing.

## Key Takeaways

Latency DB gồm acquire, network, execution, lock waits và result consumption..


## See also

- [database/sql: pool handle, rows và transaction ownership](database-sql.md)
- [Database connection pool: 500 requests và 20 connections](database-sql-pool.md)
- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/database/)
