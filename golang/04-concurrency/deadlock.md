# Deadlock và wait-for graph

## Concept và Mental Model

Deadlock khi tasks chờ lẫn nhau hoặc chờ event không bao giờ có; production có thể chỉ deadlock một subsystem.

## How it works

Vẽ G giữ resource nào, đang chờ gì; cycle lock order và channel handshake là hai nguồn phổ biến. Runtime global deadlock detection không bắt mọi partial deadlock trong server còn network work.

## Production Use Case

Shutdown stop producer trước close queue, drain workers rồi close dependencies.

## Failure Scenarios

Wait trước close/unblock; unbuffered send trước launching receiver; recursive mutex.

## How I would debug this in production

Lấy nhiều goroutine dumps để xác nhận stacks đứng yên; tìm cycle và owner đã exit.

## Trade-offs và When NOT to use

Timeout giảm blast radius nhưng không sửa lock protocol; giữ order đơn giản.

## Interview practice

Why might the runtime not report a service deadlock? Vẫn còn runnable/network activity ngoài subsystem bị kẹt.

## Key Takeaways

Deadlock khi tasks chờ lẫn nhau hoặc chờ event không bao giờ có; production có thể chỉ deadlock một subsystem..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)
