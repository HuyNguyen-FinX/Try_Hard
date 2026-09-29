# Resource requests, limits và Go budgets

## Concept và Mental Model

CPU request phục vụ scheduling/share; CPU limit có thể throttle; memory limit có thể kill.

## How it works

Choose memory headroom từ live heap+stacks+runtime+native+buffers; GOMEMLIMIT soft và không bao toàn RSS. GOMAXPROCS effective cần kiểm tra runtime config.

## Production Use Case

Set requests dựa steady state và burst measurement; reserve memory cho spike và profile overhead.

## Failure Scenarios

GC thrash sát memory limit; CPU bursts bị throttle làm timeout/retry; low requests khiến poor placement.

## How I would debug this in production

RSS/heap, OOMKilled, throttled periods, scheduler latency và GC assists.

## Trade-offs và When NOT to use

Không đặt limit bằng live heap sample duy nhất; workload distribution và native memory matters.

## Interview practice

Why does GOMEMLIMIT not guarantee no OOM? Runtime limit soft và không quản tất cả process/container memory.

## Key Takeaways

CPU request phục vụ scheduling/share; CPU limit có thể throttle; memory limit có thể kill..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kubernetes.io/docs/concepts/)
