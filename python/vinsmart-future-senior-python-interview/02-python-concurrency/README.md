# Python Concurrency

Module này được học theo **Why → How → Internals → Flow → Failure → Trade-off → Production**. Không đọc alphabet; đi theo dependency dưới đây và tự vẽ lại diagram trước khi xem.

## Learning order

[Global Interpreter Lock (GIL)](gil.md) → [AsyncIO](asyncio.md) → [Event Loop](event-loop.md) → [Coroutine Task Future](coroutine-task-future.md) → [CPU Vs IO Bound](cpu-vs-io-bound.md)

## Must know

- [Global Interpreter Lock (GIL)](gil.md)
- [AsyncIO](asyncio.md)
- [Event Loop](event-loop.md)
- [Coroutine Task Future](coroutine-task-future.md)
- [CPU Vs IO Bound](cpu-vs-io-bound.md)

## Nice to know / second pass

- [Threading](threading.md)
- [Multiprocessing](multiprocessing.md)
- [Synchronization](synchronization.md)
- [Race Condition](race-condition.md)
- [Deadlock](deadlock.md)
- [Interview Scenarios](interview-scenarios.md)

## Recommended exercises

1. Giải thích mỗi Must-know topic trong 2 phút, không nhìn note; interviewer hỏi “why?” ít nhất ba lần.
2. Vẽ request/data/failure flow từ trí nhớ và đánh dấu source of truth, queue, timeout, retry, metric.
3. Chọn một production incident liên quan **Python Concurrency**, trình bày mitigation trước root cause và long-term prevention.
4. Load/fault test một assumption: bottleneck, duplicate, stale state hoặc dependency outage.

## All topics

- [Global Interpreter Lock (GIL)](gil.md)
- [Threading](threading.md)
- [Multiprocessing](multiprocessing.md)
- [AsyncIO](asyncio.md)
- [Event Loop](event-loop.md)
- [Coroutine Task Future](coroutine-task-future.md)
- [Synchronization](synchronization.md)
- [Race Condition](race-condition.md)
- [Deadlock](deadlock.md)
- [CPU Vs IO Bound](cpu-vs-io-bound.md)
- [Interview Scenarios](interview-scenarios.md)

[← Main Dashboard](../README.md)
