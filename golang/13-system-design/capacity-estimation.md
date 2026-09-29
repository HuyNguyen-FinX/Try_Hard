# Capacity estimation có units

## Concept và Mental Model

Ước lượng là model có assumptions để tìm bottleneck, không là performance guarantee.

## How it works

RPS×mean latency(s)=mean in-flight trong steady state; events/s×bytes/event×retention(s) cho raw storage. Cộng indexes/replicas/protocol overhead và headroom riêng, không trộn units MB/MiB.

## Production Use Case

20k RPS×50ms=1000 concurrent; cache90% reads và95% hit cho900 misses/s.

## Failure Scenarios

Lấy peak làm daily average; dùng P99 thay mean trong Little's Law; quên replicas và rollout surge.

## How I would debug this in production

So estimates với load generator offered rate, actual bytes và DB hold time; revise assumptions theo samples.

## Trade-offs và When NOT to use

Rough estimate hữu ích hơn precision giả; sensitivity analysis hit ratio/latency cần thiết.

## Interview practice

Which assumption most changes DB capacity? Cache miss ratio, queries per request và connection hold time.

## Key Takeaways

Ước lượng là model có assumptions để tìm bottleneck, không là performance guarantee..


## See also

- [System design framework cho Senior Go](system-design-framework.md)
- [Design High-Throughput API — 20,000 RPS](design-high-throughput-api.md)
- [Design Migration Platform — 4–5 Billion Records](design-migration-platform.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)
