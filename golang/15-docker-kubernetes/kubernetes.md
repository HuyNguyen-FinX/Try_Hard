# Kubernetes mental model

## Concept và Mental Model

Kubernetes controllers reconcile desired state qua API; scheduling/restarts không hiểu application correctness.

## How it works

Pod là scheduling unit; Deployment quản replicas/rollout; Service route tới endpoints; probes/resource requests/limits ảnh hưởng availability.

## Production Use Case

Stateless Go API replicas, durable state ngoài pod; workers cần idempotency qua restarts.

## Failure Scenarios

Assume restart là recovery đủ; local in-memory accepted jobs mất khi pod rescheduled.

## How I would debug this in production

Events, pod status/restart reason, rollout history, endpoints và application SLO.

## Trade-offs và When NOT to use

Kubernetes thêm orchestration cost; không bắt buộc cho service nhỏ nếu platform khác đủ.

## Interview practice

What application property makes pod replacement safe? Stateless hoặc durable/replayable state với idempotency.

## Key Takeaways

Kubernetes controllers reconcile desired state qua API; scheduling/restarts không hiểu application correctness..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kubernetes.io/docs/concepts/)

## Applied drill

Triển khai một Go pod với startup/readiness/liveness riêng rồi inject slow DB. Nếu liveness phụ thuộc DB, toàn fleet có thể restart làm pool/TLS warm-up nặng hơn. Sửa liveness theo local progress, giữ readiness/degraded policy phù hợp user contract. Kubernetes giữ desired replica count, còn durable accepted jobs và replay correctness vẫn là trách nhiệm application.
