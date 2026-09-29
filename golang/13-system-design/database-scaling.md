# Database scaling theo bottleneck

## Concept và Mental Model

Scale database gồm query/index fixes, caching, replicas, partitioning và sharding; mỗi cách giải quyết bottleneck khác.

## How it works

Read replica giảm eligible reads nhưng có lag; vertical scale/IO tuning khác write sharding. Connection pool không tạo DB execution capacity.

## Production Use Case

Read-your-writes route writer; background analytics tách workload khỏi OLTP.

## Failure Scenarios

Replication lag stale status; too many connections; hot row invariant vẫn serialized dù thêm shards.

## How I would debug this in production

Plans, locks, CPU/IO, WAL, replication lag và working set; xác định read/write/skew.

## Trade-offs và When NOT to use

Sharding thêm routing/rebalance/cross-shard complexity; chọn sau evidence.

## Interview practice

Why do replicas not automatically scale writes? Primary write authority và replication path vẫn giới hạn.

## Key Takeaways

Scale database gồm query/index fixes, caching, replicas, partitioning và sharding; mỗi cách giải quyết bottleneck khác..


## See also

- [System design framework cho Senior Go](system-design-framework.md)
- [Design High-Throughput API — 20,000 RPS](design-high-throughput-api.md)
- [Design Migration Platform — 4–5 Billion Records](design-migration-platform.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)
