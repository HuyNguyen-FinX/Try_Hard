# Semaphore và admission

## Concept và Mental Model

Semaphore bound số operations in-flight; acquire phải trước tạo work tiêu tốn tài nguyên.

## How it works

Buffered channel tokens hoặc weighted semaphore; acquire dùng select ctx. Release đúng một lần sau successful acquire.

## Production Use Case

Giới hạn outbound calls độc lập từng dependency để tránh một host làm cạn mọi workers.

## Failure Scenarios

Spawn goroutine trước acquire tạo vô hạn waiting G; release token chưa acquire làm deadlock/panic tùy implementation.

## How I would debug this in production

Đo active permits, acquire wait và rejected requests; test cancel trước/sau acquire.

## Trade-offs và When NOT to use

Bound concurrency không bound rate hoặc payload bytes; thêm queue và rate limits khi cần.

## Interview practice

Where should you acquire a permit? Trước khi launch task nếu mục tiêu còn gồm bound goroutine count.

## Key Takeaways

Semaphore bound số operations in-flight; acquire phải trước tạo work tiêu tốn tài nguyên..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)
