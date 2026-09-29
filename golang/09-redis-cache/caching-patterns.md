# Caching patterns và consistency

## Concept và Mental Model

Cache-aside, write-through và write-behind khác ownership của update và failure window.

## How it works

Cache-aside app đọc cache rồi DB; write-through đồng bộ cả path theo protocol; write-behind async cần durable queue và ordering. TTL chỉ giới hạn staleness theo giả định update/refresh.

## Production Use Case

Product catalog chịu stale vài chục giây; payment authorization dùng authoritative state.

## Failure Scenarios

DB commit thành công nhưng invalidate fail; stale refill đè dữ liệu mới; negative cache giữ not-found quá lâu.

## How I would debug this in production

Track version/age, compare sampled cache với source và inspect invalidation events.

## Trade-offs và When NOT to use

Cache giảm read load nhưng thêm consistency system; không cache nếu working set/hit rate không có lợi.

## Interview practice

How can invalidation still race with a concurrent read? Old DB result có thể refill sau invalidation.

## Key Takeaways

Cache-aside, write-through và write-behind khác ownership của update và failure window..


## See also

- [Database connection pool: 500 requests và 20 connections](../08-database/database-sql-pool.md)
- [distributed-lock](../12-distributed-systems/distributed-lock.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://redis.io/docs/latest/develop/)
