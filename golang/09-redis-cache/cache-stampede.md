# Cache stampede và refresh coalescing

## Concept và Mental Model

Nhiều callers cùng miss một hot key làm N identical source queries.

## How it works

Singleflight coalesce trong process; cross-pod still multiple loads. TTL jitter tránh simultaneous expiry; early refresh/stale response cần explicit freshness bound.

## Production Use Case

Hot catalog page dùng shared refresh owner có timeout riêng, callers có wait budget.

## Failure Scenarios

Leader caller canceled kéo shared refresh nếu dùng sai ctx; unbounded refresh map; backend outage phá mọi refresh.

## How I would debug this in production

Measure source loads per cache key sample, fan-in waiter count và refresh duration.

## Trade-offs và When NOT to use

Coalescing giữ waiters nên vẫn bound concurrency; không biến tất cả requests thành chờ một refresh vô hạn.

## Interview practice

Does singleflight eliminate stampedes across pods? Không; scope thường là một process.

## Key Takeaways

Nhiều callers cùng miss một hot key làm N identical source queries..


## See also

- [Database connection pool: 500 requests và 20 connections](../08-database/database-sql-pool.md)
- [distributed-lock](../12-distributed-systems/distributed-lock.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://redis.io/docs/latest/develop/)
