# Chọn concurrency pattern

## Concept và Mental Model

Chọn primitive từ ownership và invariant, rồi mới quyết định channel hay lock.

## How it works

Task lifetime: create, admit, execute, publish, cancel, join. Errors đi cùng results hoặc boundary rõ; channel close không mang cause.

## Production Use Case

Counter dùng atomic; cache invariant dùng mutex; bounded work dùng pool; immutable config publish snapshot.

## Failure Scenarios

Mix nhiều primitives không có protocol; “fire and forget” quên errors và shutdown.

## How I would debug this in production

Vẽ wait-for graph và lifecycle table; test overload, cancellation, partial failure.

## Trade-offs và When NOT to use

Synchronous code là baseline tốt; concurrency chỉ khi có work overlap hoặc isolation cần thiết.

## Interview practice

How would you choose channels versus locks? Communication/ownership so với shared-state critical section.

## Key Takeaways

Chọn primitive từ ownership và invariant, rồi mới quyết định channel hay lock..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)
