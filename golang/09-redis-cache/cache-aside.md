# Cache-aside: miss path cũng là production path

## Concept và Mental Model

App sở hữu load và cache fill; miss đi DB và phải có concurrency budget.

## How it works

Read key, on miss coalesce same-key loads, query source, set TTL+jitter; invalidation sau successful write vẫn cần versioning nếu stale refill không chấp nhận.

## Production Use Case

Cache product details; use short negative TTL cho missing ID để giảm repeated misses.

## Failure Scenarios

Cold start mọi pods miss cùng lúc; Redis down tất cả fallback DB.

## How I would debug this in production

Measure hit ratio theo route, load coalescing wait và DB QPS khi cache bypass.

## Trade-offs và When NOT to use

Stale-while-revalidate giảm latency nhưng cần stale bound và owner refresh.

## Interview practice

What protects the database when cache hit rate collapses? Admission limits, bounded refresh và degradation.

## Key Takeaways

App sở hữu load và cache fill; miss đi DB và phải có concurrency budget..


## See also

- [Database connection pool: 500 requests và 20 connections](../08-database/database-sql-pool.md)
- [distributed-lock](../12-distributed-systems/distributed-lock.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://redis.io/docs/latest/develop/)
