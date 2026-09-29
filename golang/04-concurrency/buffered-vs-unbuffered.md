# Buffered versus unbuffered

## Concept và Mental Model

Unbuffered rendezvous đồng bộ sender/receiver; buffered tách thời điểm gửi và nhận tối đa capacity.

## How it works

Queue capacity C có thể hấp thụ burst nhưng nếu arrival > completion dài hạn thì sẽ đầy. Send success không phải ack processing.

## Production Use Case

Chọn C từ tolerated queue wait và payload memory; dùng buffer 1 cho one-shot result nếu caller có thể timeout.

## Failure Scenarios

Tăng C giấu overload; producer không cancel làm shutdown treo khi queue đầy.

## How I would debug this in production

Đo queue age và rate, không chỉ len; test capacity 0,1 và full.

## Trade-offs và When NOT to use

Unbuffered dễ reasoning handshake; buffered cải thiện burst nhưng thêm memory/latency.

## Interview practice

When does a buffer improve throughput versus merely increase latency? Cần xem bottleneck và service rate.

## Key Takeaways

Unbuffered rendezvous đồng bộ sender/receiver; buffered tách thời điểm gửi và nhận tối đa capacity..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)
