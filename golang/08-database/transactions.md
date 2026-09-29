# Transactions và short critical sections

## Concept và Mental Model

Transaction bảo vệ durable invariant trên nhiều operations; connection bị giữ từ Begin tới Commit/Rollback.

## How it works

Dùng tx cho mọi query thuộc operation, validate trước khi begin khi có thể, lock rows theo thứ tự, xử lý commit error. Retry serialization failure cho whole transaction với budget.

## Production Use Case

Debit-credit cùng DB transaction; publish event qua outbox trong cùng commit.

## Failure Scenarios

External HTTP call trong Tx kéo lock; retry chỉ statement cuối trên aborted Tx sai.

## How I would debug this in production

Xem transaction age, lock wait, SQLSTATE và rollback paths; inject error giữa từng statement.

## Trade-offs và When NOT to use

Short Tx giảm contention; chia Tx có thể phá atomicity nên phải định nghĩa saga khi khác DB.

## Interview practice

Why should serialization retry replay the whole transaction? Snapshot và mọi reads trước đó không còn cơ sở hợp lệ.

## Key Takeaways

Transaction bảo vệ durable invariant trên nhiều operations; connection bị giữ từ Begin tới Commit/Rollback..


## See also

- [database/sql: pool handle, rows và transaction ownership](database-sql.md)
- [Database connection pool: 500 requests và 20 connections](database-sql-pool.md)
- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/database/)
