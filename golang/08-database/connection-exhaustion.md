# Connection exhaustion runbook

## Concept và Mental Model

Exhaustion là demand hoặc hold time vượt pool/server budget, không chỉ config nhỏ.

## How it works

Rows, Tx, dedicated Conn và downstream lock waits đều có thể giữ slot; fleet pool count phải có reserve cho admin/migrations.

## Production Use Case

Giới hạn API admission và worker concurrency riêng; pool acquire timeout ngăn chờ vô hạn.

## Failure Scenarios

Long idle-in-transaction; retry storm; HPA tăng pods; leak cleanup.

## How I would debug this in production

Stats InUse/Wait deltas, pg_stat_activity, blockers và transaction age; lấy goroutine stacks cùng lúc.

## Trade-offs và When NOT to use

Mitigate giảm intake/retries trước tăng DB connections khi chưa biết headroom.

## Interview practice

Why can app pool be exhausted while DB CPU is low? Connections có thể giữ idle Tx, wait locks hoặc rows chưa close.

## Key Takeaways

Exhaustion là demand hoặc hold time vượt pool/server budget, không chỉ config nhỏ..


## See also

- [database/sql: pool handle, rows và transaction ownership](database-sql.md)
- [Database connection pool: 500 requests và 20 connections](database-sql-pool.md)
- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/database/)
