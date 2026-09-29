# Probes không phải full diagnostics

## Concept và Mental Model

Startup, readiness, liveness trả lời ba câu hỏi khác nhau; probe phải rẻ và có bounded latency.

## How it works

Startup trì hoãn liveness/readiness evaluation theo semantics; readiness dừng traffic, liveness restart. Endpoint status phù hợp drain state.

## Production Use Case

Liveness kiểm local progress, readiness check minimum serving capability; dependencies optional không làm toàn pod unready.

## Failure Scenarios

Liveness query DB gây restart storm khi DB outage; threshold quá gắt khi GC/CPU throttle.

## How I would debug this in production

Probe failure timeline cùng restarts, dependency errors và CPU; test slow startup.

## Trade-offs và When NOT to use

Probe sâu tăng coverage nhưng thêm cascading dependency; synthetic end-to-end checks tách riêng.

## Interview practice

Which probe should fail during graceful draining? Readiness, không cần liveness restart process.

## Key Takeaways

Startup, readiness, liveness trả lời ba câu hỏi khác nhau; probe phải rẻ và có bounded latency..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kubernetes.io/docs/concepts/)
