# Sharding và partition ownership

## Concept và Mental Model

Sharding chia dữ liệu/throughput theo key qua authorities; chọn key quyết định locality và hot spots.

## How it works

Hash phân đều average; range hỗ trợ scans nhưng có skew; directory routing linh hoạt nhưng thêm metadata authority. Rebalance cần copy+CDC+cutover epoch.

## Production Use Case

Tenant-sharded data giữ tenant transactions local, có special handling cho hot tenant.

## Failure Scenarios

Cross-shard joins/transactions; key migration double writes; one large tenant saturates shard.

## How I would debug this in production

Per-shard load/storage/lag, routing version và invariant reconciliation sau move.

## Trade-offs và When NOT to use

Không shard chỉ vì table lớn; index/query/access pattern có thể đủ.

## Interview practice

How would you move a shard without losing writes? Snapshot+change capture, verify, routing epoch và fenced ownership.

## Key Takeaways

Sharding chia dữ liệu/throughput theo key qua authorities; chọn key quyết định locality và hot spots..


## See also

- [System design framework cho Senior Go](system-design-framework.md)
- [Design High-Throughput API — 20,000 RPS](design-high-throughput-api.md)
- [Design Migration Platform — 4–5 Billion Records](design-migration-platform.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)
