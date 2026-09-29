# sync.Once và initialization

## Concept và Mental Model

Once bảo đảm function chạy một lần và completion được publish cho các callers.

## How it works

Panic trong initializer vẫn đánh dấu Once đã thực hiện; retry cần state machine riêng. Recursive Do trên cùng Once deadlock.

## Production Use Case

Lazy immutable lookup table hoặc expensive parse; constructor eager thường rõ hơn cho config có thể fail.

## Failure Scenarios

Transient network failure trong Once bị cache vĩnh viễn; copied Once phá lifecycle.

## How I would debug this in production

Reproduce initializer failure/panic, xem readiness và callers đợi Do.

## Trade-offs và When NOT to use

Không dùng Once cho secret refresh hoặc reconnect cần retry.

## Interview practice

Does Once retry after a panic? Không; thiết kế retry state riêng.

## Key Takeaways

Once bảo đảm function chạy một lần và completion được publish cho các callers..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)

## Applied drill

Tạo initializer fail lần đầu rồi thành công ở lần hai. Với Once, lần hai không gọi lại initializer; test phải phản ánh đây là contract, không kết luận thư viện lỗi. Nếu cần retry, thiết kế state uninitialized/initializing/ready/failed với một owner, result/error publication và waiters có cancellation. Initialization network call cần deadline để không giữ tất cả callers chờ Do.
