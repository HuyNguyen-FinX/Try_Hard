# REST versus gRPC

## Concept và Mental Model

So sánh từ client ecosystem, latency, streaming và operational tooling, không từ benchmark hello-world.

## How it works

HTTP JSON dễ inspect/cache/browser; gRPC typed codegen và streaming, cần proxy/load-balancing hiểu HTTP/2 streams.

## Production Use Case

Public REST gateway tới internal gRPC có contract mapping lỗi/deadline rõ.

## Failure Scenarios

Một HTTP/2 connection lâu dài dồn backend khi LB chỉ cân connection; proxy timeout cắt stream.

## How I would debug this in production

Load test realistic payloads, protocol negotiation, request distribution và generated client compatibility.

## Trade-offs và When NOT to use

Không thêm hai protocols nếu team chưa cần; gateway thêm latency và version mapping.

## Interview practice

Can a faster serialization format fix a slow database? Không; phải đo toàn request path.

## Key Takeaways

So sánh từ client ecosystem, latency, streaming và operational tooling, không từ benchmark hello-world..


## See also

- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.rfc-editor.org/rfc/rfc9110)

## Applied drill

So cùng schema/payload, same TLS/network path và business work; report CPU, bytes, allocations, P99 cùng concurrency. Thêm long stream và backend rollout để đánh giá LB distribution/drain, không chỉ unary hello-world. REST có thể dùng HTTP/2, và gRPC không mặc nhiên làm DB nhanh hơn; tách serialization savings khỏi total request critical path.
