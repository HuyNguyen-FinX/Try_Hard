# Resilience budget xuyên dependencies

## Concept và Mental Model

Timeout, retry, circuit breaker và bulkhead phải phối hợp theo total capacity/deadline.

## How it works

Bound concurrency trước retry; classify errors; fallbacks có correctness/freshness contract. Per-dependency budget bảo vệ critical path.

## Production Use Case

Recommendations fail có thể omit; authorization fail thường reject thay allow.

## Failure Scenarios

Fallback cũng gọi dependency đang lỗi; retry storm; circuit global làm unrelated routes outage.

## How I would debug this in production

Chaos test một dependency chậm/down và đo blast radius, not just success on happy path.

## Trade-offs và When NOT to use

Mỗi mechanism thêm state/complexity; bắt đầu từ deadline+limits+idempotency.

## Interview practice

What makes a fallback safe? Nó vẫn giữ security và business invariants đã định nghĩa.

## Key Takeaways

Timeout, retry, circuit breaker và bulkhead phải phối hợp theo total capacity/deadline..


## See also

- [Microservices: independent ownership có chi phí](../11-software-architecture/microservices.md)
- [Distributed failure matrix](../12-distributed-systems/failure-scenarios.md)
- [tracing](../17-observability/tracing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://grpc.io/docs/guides/)

## Applied drill

Viết matrix theo dependency: recommendations optional→omit; inventory authority→reject mutation nếu unknown; cache catalog→bounded stale; telemetry exporter→bounded drop. Cùng timeout không thể áp cùng fallback cho mọi dependency. Test optional outage không làm critical endpoint exhaust shared pools. Mỗi fallback cần metric để degraded mode không ẩn kéo dài.
