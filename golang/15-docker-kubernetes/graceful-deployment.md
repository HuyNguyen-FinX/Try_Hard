# Graceful deployment và SIGTERM budget

## Concept và Mental Model

Rollout an toàn cần endpoint removal, drain và durable recovery cùng hoạt động.

## How it works

Termination budget bao preStop, LB propagation, Server.Shutdown, worker join, flush/Close; nếu hết budget process có thể bị kill.

## Production Use Case

Readiness false, stop new work, drain bounded, commit completed offsets, close DB cuối cùng.

## Failure Scenarios

Sleep preStop ăn hết grace period; WebSockets không đóng; side effect xong nhưng ack chưa gửi bị replay.

## How I would debug this in production

Load-test rolling deploy với in-flight calls và queue; record phase timestamps và duplicate/lost work.

## Trade-offs và When NOT to use

Long drain giảm interruption nhưng làm rollout chậm; idempotent replay là backstop.

## Interview practice

How do you validate zero data loss through a rollout? Reconcile accepted durable jobs với completed/replayable states, không chỉ HTTP success rate.

## Key Takeaways

Rollout an toàn cần endpoint removal, drain và durable recovery cùng hoạt động..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kubernetes.io/docs/concepts/)
