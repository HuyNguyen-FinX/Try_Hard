# Context mistakes thường gặp

## Concept và Mental Model

Context truyền đúng nhưng không được dùng ở blocking operation vẫn không đạt cancellation.

## How it works

Tránh storing ctx lâu dài trong reusable service; pass per call. Cancel trong loop bằng function scope để release sớm. Không chọn Background để lờ timeout lỗi.

## Production Use Case

Code review mọi goroutine và outbound call cùng parent lifetime.

## Failure Scenarios

Lost cancel, nil context, WithValue làm dependency container, retry lấy timeout mới đầy đủ.

## How I would debug this in production

go vet có thể bắt lostcancel một số paths; integration test cancellation thực tế với driver/server.

## Trade-offs và When NOT to use

WithoutCancel có mục đích đặc biệt nhưng detach phải có bounded new owner; không dùng để che leak.

## Interview practice

Why can detaching context be dangerous? Nó cắt deadline/cancel trong khi tài nguyên vẫn cần lifetime rõ.

## Key Takeaways

Context truyền đúng nhưng không được dùng ở blocking operation vẫn không đạt cancellation..


## See also

- [Context: cây lifetime và cooperative cancellation](context-basics.md)
- [Goroutine leaks: blocked work còn giữ tài nguyên](../04-concurrency/goroutine-leak.md)
- [graceful-shutdown](../06-http-backend/graceful-shutdown.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/context)
