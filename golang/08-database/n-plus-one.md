# N+1 queries

## Concept và Mental Model

Một query lấy danh sách rồi N queries lấy dữ liệu con làm round trips tăng theo page size.

## How it works

Batch IDs, join hoặc preload có giới hạn; join nhiều one-to-many có thể nhân rows nên aggregation và pagination cần cẩn thận.

## Production Use Case

List 100 orders trả items qua hai bounded queries thay 101 queries.

## Failure Scenarios

Join fix làm response 100x lớn; pagination trên joined rows cắt thiếu entities.

## How I would debug this in production

Trace query count theo page size, tổng DB time và bytes/rows scanned.

## Trade-offs và When NOT to use

Batch giảm RTT nhưng payload/memory tăng; không load mọi relation mặc định.

## Interview practice

How would you prove an N+1 fix? Query count gần constant theo page size và correct pagination.

## Key Takeaways

Một query lấy danh sách rồi N queries lấy dữ liệu con làm round trips tăng theo page size..


## See also

- [database/sql: pool handle, rows và transaction ownership](database-sql.md)
- [Database connection pool: 500 requests và 20 connections](database-sql-pool.md)
- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/database/)
