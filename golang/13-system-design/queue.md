# Queues và recovery capacity

## Concept và Mental Model

Queue tách arrival và service rate nhưng không chữa overload dài hạn; oldest age phản ánh user delay.

## How it works

Bound retention/storage/in-flight; arrival λ, service μ: nếu μ≤λ backlog không drain. Recovery time≈backlog/(μ−λ) khi rates ổn định.

## Production Use Case

Backlog1M, process8k/s, new5k/s →~333s drain ideal.

## Failure Scenarios

Scale consumers tăng DB contention làm μ giảm; queue full không có producer policy.

## How I would debug this in production

Queue age, growth derivative, retries, partition skew và sink saturation.

## Trade-offs và When NOT to use

Durable queue giữ work qua crash nhưng cần replay/idempotency; memory channel phù hợp scope process.

## Interview practice

What rate matters when estimating catch-up time? Net processing capacity sau ongoing arrivals.

## Key Takeaways

Queue tách arrival và service rate nhưng không chữa overload dài hạn; oldest age phản ánh user delay..


## See also

- [System design framework cho Senior Go](system-design-framework.md)
- [Design High-Throughput API — 20,000 RPS](design-high-throughput-api.md)
- [Design Migration Platform — 4–5 Billion Records](design-migration-platform.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)
