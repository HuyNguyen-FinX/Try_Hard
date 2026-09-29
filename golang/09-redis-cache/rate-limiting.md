# Redis atomic rate limiting

## Concept và Mental Model

Distributed limiter cần check và update atomic để nhiều instances dùng chung quota.

## How it works

Lua script/token bucket hoặc sliding window theo requirements; bound key TTL/cardinality và clock assumptions. Multi-key operations trong cluster cần cùng slot khi API yêu cầu.

## Production Use Case

Tenant bucket với capacity 100, refill 20/s; chỉ sample debug cho từng tenant tránh metrics cardinality vô hạn.

## Failure Scenarios

INCR rồi EXPIRE tách commands có crash window; clock skew; limiter outage gây policy không rõ.

## How I would debug this in production

Test concurrent acquire, TTL existence và deny ratio; theo dõi script latency.

## Trade-offs và When NOT to use

Central accuracy đổi availability/latency; local fallback phải có conservative budget.

## Interview practice

How would you atomically create a counter with expiry? Một server-side atomic operation/script theo deployment contract.

## Key Takeaways

Distributed limiter cần check và update atomic để nhiều instances dùng chung quota..


## See also

- [Database connection pool: 500 requests và 20 connections](../08-database/database-sql-pool.md)
- [distributed-lock](../12-distributed-systems/distributed-lock.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://redis.io/docs/latest/develop/)
