# Service discovery và connection lifetime

## Concept và Mental Model

Discovery ánh xạ service identity tới endpoints; stale endpoints tồn tại trong caches và long-lived connections.

## How it works

DNS, platform service routing hoặc client resolver có update/TTL/load-balance policies. HTTP/2 gRPC connection reuse ảnh hưởng distribution.

## Production Use Case

Kubernetes Service tới pods, readiness loại endpoints theo propagation delay.

## Failure Scenarios

DNS cache stale, connection pin vào một pod, headless service client không rebalance.

## How I would debug this in production

Resolve answers/TTLs, endpoint health, per-pod traffic và client connection age.

## Trade-offs và When NOT to use

Client-side LB thêm logic; server-side proxy thêm hop và operational surface.

## Interview practice

Why can adding pods leave gRPC traffic skewed? Long-lived streams/connections không tự phân phối lại theo request.

## Key Takeaways

Discovery ánh xạ service identity tới endpoints; stale endpoints tồn tại trong caches và long-lived connections..


## See also

- [Microservices: independent ownership có chi phí](../11-software-architecture/microservices.md)
- [Distributed failure matrix](../12-distributed-systems/failure-scenarios.md)
- [tracing](../17-observability/tracing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://grpc.io/docs/guides/)

## Applied drill

Trong rollout, endpoint removal và client connection reuse xảy ra ở thời điểm khác nhau. Server cần drain in-flight, client cần reconnect/retry policy replay-safe khi connection đóng. DNS TTL giảm không tự đóng socket đã mở. Test backend replacement với active streams và observe traffic migration, errors và reconnect burst trước thay discovery architecture.
