# Deployment và rollout capacity

## Concept và Mental Model

Rolling update chạy versions song song; schema/protocol phải tương thích trong cửa sổ rollout.

## How it works

maxSurge và maxUnavailable điều khiển extra/reduced capacity; readiness gate traffic, strategy cần spare resources.

## Production Use Case

Expand schema trước deploy readers/writers mới, contract sau old pods gone và migration verified.

## Failure Scenarios

Surge nhân DB pools vượt budget; readiness ready trước warm caches; incompatible schema.

## How I would debug this in production

Track available replicas, rollout progress, old/new error cohorts và DB connections.

## Trade-offs và When NOT to use

Blue-green dễ rollback nhưng gấp đôi resources; rolling tiết kiệm hơn nhưng version skew dài.

## Interview practice

How can a safe replica count still exceed DB budget during rollout? Surge tạo thêm pools đồng thời.

## Key Takeaways

Rolling update chạy versions song song; schema/protocol phải tương thích trong cửa sổ rollout..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kubernetes.io/docs/concepts/)
