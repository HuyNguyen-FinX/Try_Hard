# Redis Cluster: slots và hot keys

## Concept và Mental Model

Redis Cluster chia keyspace theo hash slots; một hot key vẫn thuộc một shard.

## How it works

Client xử lý MOVED/ASK theo library; hash tags đặt keys cùng slot khi cần multi-key atomicity nhưng có thể tạo skew. Replication/failover có durability windows tùy config.

## Production Use Case

Partition cache theo tenant/key, monitor per-shard memory/CPU thay aggregate.

## Failure Scenarios

Resharding errors nếu client không cluster-aware; hot tag dồn mọi tenant vào một slot.

## How I would debug this in production

Inspect slot ownership, redirections, per-node latency và key size distribution.

## Trade-offs và When NOT to use

Cluster scale keyspace, không tự scale single key; replicas có consistency/lag trade-off.

## Interview practice

Why can adding shards fail to fix a hot key? Key không tự chia ra nhiều primaries.

## Key Takeaways

Redis Cluster chia keyspace theo hash slots; một hot key vẫn thuộc một shard..


## See also

- [Database connection pool: 500 requests và 20 connections](../08-database/database-sql-pool.md)
- [distributed-lock](../12-distributed-systems/distributed-lock.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://redis.io/docs/latest/develop/)
