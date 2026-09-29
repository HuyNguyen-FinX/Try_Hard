# HTTP performance có evidence

## Concept và Mental Model

Throughput bền vững phải giữ P99/error budget khi dependencies chịu tải thật.

## How it works

Measure allocations, TLS/reuse, JSON, compression, DB wait; bound concurrency và payload trước micro-optimizations.

## Production Use Case

Load ramp từ 1k tới 20k RPS với representative hot keys và payloads.

## Failure Scenarios

Load generator closed-loop che overload; pool tăng khiến DB saturate; compression CPU chi phối.

## How I would debug this in production

CPU/heap profiles và traces cùng load timestamps; phân biệt app CPU và upstream queuing.

## Trade-offs và When NOT to use

Custom unsafe encoder chỉ sau benchmark và compatibility tests; thường reuse/batching/index hiệu quả hơn.

## Interview practice

How would you scale from 1k to 20k RPS? Xác định bottleneck bằng measured per-request cost và downstream budgets.

## Key Takeaways

Throughput bền vững phải giữ P99/error budget khi dependencies chịu tải thật..


## See also

- [net/http: server, handler và request lifetime](net-http.md)
- [HTTP client reuse và response ownership](http-client.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/net/http)
