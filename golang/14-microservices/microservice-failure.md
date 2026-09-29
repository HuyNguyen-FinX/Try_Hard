# Microservice cascading failure

## Concept và Mental Model

Một dependency chậm có thể làm callers giữ pools/G/memory rồi lan thành outage.

## How it works

Bound waits/concurrency và isolate pools; stop retries khi budget hết; reject overload trước khi chạm OOM.

## Production Use Case

DB slowdown khiến API shed optional work và stop background backfill.

## Failure Scenarios

Autoscale app tăng connections vào DB đang saturate; liveness phụ thuộc DB làm restart storm.

## How I would debug this in production

Timeline latency, in-flight, pool wait, errors và restarts; xác định dependency đầu tiên lệch baseline.

## Trade-offs và When NOT to use

Availability local không đủ; dependency capacity giới hạn toàn path.

## Interview practice

Why can scaling callers worsen an outage? Nó tăng demand lên bottleneck chưa được mở rộng.

## Key Takeaways

Một dependency chậm có thể làm callers giữ pools/G/memory rồi lan thành outage..


## See also

- [Microservices: independent ownership có chi phí](../11-software-architecture/microservices.md)
- [Distributed failure matrix](../12-distributed-systems/failure-scenarios.md)
- [tracing](../17-observability/tracing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://grpc.io/docs/guides/)

## Applied drill

Fault injection làm inventory delay2s trong khi order budget200ms. Order phải fail/degrade trong budget, không giữ goroutines tăng vô hạn và không retry tầng tầng. Observe breaker/semaphore state, DB pool và remaining capacity của payment path. Sau dependency hồi phục, bounded half-open probes và jitter tránh recovery herd; verify queued work đã reconcile.
