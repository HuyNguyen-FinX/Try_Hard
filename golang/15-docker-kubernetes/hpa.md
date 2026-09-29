# HPA và scaling limits

## Concept và Mental Model

HPA đổi replica count theo metrics/control loop; phản ứng có delay và không tạo downstream capacity.

## How it works

CPU utilization target phụ thuộc requests; custom queue age/lag có thể hợp workers hơn CPU. Bound min/max và stabilization để giảm flapping.

## Production Use Case

Scale API từ measured per-pod throughput, giữ aggregate DB/Redis/client budgets trong giới hạn.

## Failure Scenarios

Low CPU nhưng DB-wait saturation không trigger CPU HPA; tăng consumers quá partitions vô ích.

## How I would debug this in production

Desired/current replicas, metric freshness, pending pods và bottleneck downstream.

## Trade-offs và When NOT to use

Autoscaling giảm manual sizing nhưng không hấp thụ instant burst; cần admission/queue/headroom.

## Interview practice

Why can HPA worsen a DB incident? New pods tăng concurrent DB demand.

## Key Takeaways

HPA đổi replica count theo metrics/control loop; phản ứng có delay và không tạo downstream capacity..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kubernetes.io/docs/concepts/)
