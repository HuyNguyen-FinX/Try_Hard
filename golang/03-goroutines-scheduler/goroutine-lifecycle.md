# Goroutine lifecycle

## Concept và Mental Model

Mỗi task đi qua runnable, running, waiting rồi dead; waiting không đồng nghĩa leak.

## How it works

Cancel là tín hiệu; join xác nhận task đã dừng. Parent cần wait ngay cả khi child được báo cancel.

## Production Use Case

Consumer service bắt đầu workers, ngừng fetch, cancel work theo policy rồi Wait trước đóng DB.

## Failure Scenarios

Đóng channel khi producer còn gửi gây panic; Wait trước khi unblock producer gây deadlock.

## How I would debug this in production

Vẽ dependency graph của shutdown và thu stack tại deadline; thử cancel giữa từng stage.

## Trade-offs và When NOT to use

Drain giữ work nhưng kéo dài shutdown; abort cần replay/idempotency.

## Interview practice

What is the difference between signaling stop and joining? Stop yêu cầu, join xác nhận hoàn tất.

## Key Takeaways

Mỗi task đi qua runnable, running, waiting rồi dead; waiting không đồng nghĩa leak..


## See also

- [Go scheduler: G, M, P và các đường blocking](scheduler-gmp.md)
- [trace](../16-performance/trace.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://github.com/golang/go/blob/go1.26.4/src/runtime/proc.go)
