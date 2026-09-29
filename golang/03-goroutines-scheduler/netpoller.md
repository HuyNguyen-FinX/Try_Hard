# Netpoller và network readiness

## Concept và Mental Model

Netpoller nối OS readiness notifications với runnable goroutines, không xử lý business request thay application.

## How it works

Nonblocking read chưa có bytes thì G park; readiness hoặc deadline wake G để retry operation. Backend phụ thuộc OS, ví dụ kqueue trên macOS.

## Production Use Case

Một HTTP client chia sẻ Transport quản lý nhiều connections trong khi G chờ response.

## Failure Scenarios

DNS/cgo hoặc disk I/O bị nhầm là netpoll; socket không deadline giữ request buffers lâu.

## How I would debug this in production

Goroutine stack net/http + internal/poll, httptrace DNS/connect/first-byte và socket metrics xác định nơi chờ.

## Trade-offs và When NOT to use

Readiness không bảo đảm đủ toàn bộ message; parser cần framing và deadline.

## Interview practice

Is a socket wait equivalent to a dedicated blocked OS thread? Với runtime-managed nonblocking FD thường không.

## Key Takeaways

Netpoller nối OS readiness notifications với runnable goroutines, không xử lý business request thay application..


## See also

- [Go scheduler: G, M, P và các đường blocking](scheduler-gmp.md)
- [trace](../16-performance/trace.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://github.com/golang/go/blob/go1.26.4/src/runtime/proc.go)
