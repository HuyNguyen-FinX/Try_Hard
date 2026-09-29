# Container resources và process model

## Concept và Mental Model

Namespaces isolate views; cgroups budget CPU/memory/process resources; host kernel vẫn shared.

## How it works

CPU quota có thể throttle; memory limit có thể OOM kill; PID limits ảnh hưởng threads. Requests khác limits trong Kubernetes.

## Production Use Case

Tune Go concurrency/soft memory limit với headroom cho native memory và runtime.

## Failure Scenarios

Host CPU nhiều nhưng pod quota thấp; RSS chạm limit dù heap nhỏ; too many OS threads.

## How I would debug this in production

cgroup metrics, throttled periods, OOM events, process RSS và Go runtime metrics.

## Trade-offs và When NOT to use

Isolation không thay application limits; container memory phải gồm tất cả retained buffers.

## Interview practice

Why can host CPU look idle while a pod is throttled? Pod quota riêng có thể đã dùng hết trong period.

## Key Takeaways

Namespaces isolate views; cgroups budget CPU/memory/process resources; host kernel vẫn shared..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kubernetes.io/docs/concepts/)
