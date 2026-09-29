# Redis: data structures và bounded memory

## Concept và Mental Model

Redis là in-memory data server với persistence/replication tùy config; không mặc nhiên là durable source of truth.

## How it works

Strings/hashes/sets/sorted sets/streams phục vụ operations khác nhau. Command atomicity khác atomicity của read-modify-write nhiều commands. TTL, eviction policy và maxmemory cần chọn theo data role.

## Production Use Case

Cache derived user profile với TTL jitter, bounded value size và metrics hit/miss/evicted.

## Failure Scenarios

Big keys/slow commands chặn event processing; eviction xóa key app tưởng durable.

## How I would debug this in production

Latency, memory, evictions, key cardinality và slowlog; tránh KEYS toàn keyspace trong production.

## Trade-offs và When NOT to use

In-memory latency tốt nhưng RAM/persistence trade-off; SQL constraints vẫn cho durable invariant.

## Interview practice

Is Redis always just a cache? Không, role phụ thuộc persistence/delivery contract đã cấu hình.

## Key Takeaways

Redis là in-memory data server với persistence/replication tùy config; không mặc nhiên là durable source of truth..


## See also

- [Database connection pool: 500 requests và 20 connections](../08-database/database-sql-pool.md)
- [distributed-lock](../12-distributed-systems/distributed-lock.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://redis.io/docs/latest/develop/)
