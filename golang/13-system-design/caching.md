# Caching trong system design

## Concept và Mental Model

Cache cần xác định key, owner, freshness, eviction, failure fallback và invalidation race.

## How it works

Model hit/miss separately; TTL+jitter, bounded memory, negative caching và coalescing. Read-through/write-through names không thay correctness proof.

## Production Use Case

Catalog read cache reduce DB load, authorization state cần strict freshness theo security policy.

## Failure Scenarios

Hot-key expiry stampede, cross-tenant key collision, stale refill và Redis down overload source.

## How I would debug this in production

Hit ratio by route, age/version, source load và evictions; test cold-cache load.

## Trade-offs và When NOT to use

Không thêm cache khi miss path không chịu nổi recovery; source budget là điều kiện thiết kế.

## Interview practice

How can cache removal increase correctness risk? Fallback load có thể gây partial failures/retry duplicates.

## Key Takeaways

Cache cần xác định key, owner, freshness, eviction, failure fallback và invalidation race..


## See also

- [System design framework cho Senior Go](system-design-framework.md)
- [Design High-Throughput API — 20,000 RPS](design-high-throughput-api.md)
- [Design Migration Platform — 4–5 Billion Records](design-migration-platform.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)
