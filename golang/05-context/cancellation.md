# Cancellation propagation

## Concept và Mental Model

Cancel đi từ parent xuống descendants; siblings chỉ bị ảnh hưởng nếu common parent bị cancel.

## How it works

Mọi blocking receive/send dùng select; CPU loop check Err theo chunks. CancelFunc không join; dùng WaitGroup/done channel. WithCancelCause/Cause bổ sung nguyên nhân theo API, Err vẫn giữ categories.

## Production Use Case

Fail-fast fan-out cancel siblings khi một dependency bắt buộc lỗi; best-effort fan-out có thể giữ siblings.

## Failure Scenarios

Library nhận ctx nhưng dùng Background bên trong; worker dừng receive nhưng kẹt send result.

## How I would debug this in production

Trace cancel timestamp, goroutine completion và DB/HTTP cancellation; test cả case cancel trước start.

## Trade-offs và When NOT to use

Không cancel cả tree khi một optional dependency fail nếu product cho phép degrade.

## Interview practice

Does cancellation guarantee no later side effects? Không, external operation có thể đã commit.

## Key Takeaways

Cancel đi từ parent xuống descendants; siblings chỉ bị ảnh hưởng nếu common parent bị cancel..


## See also

- [Context: cây lifetime và cooperative cancellation](context-basics.md)
- [Goroutine leaks: blocked work còn giữ tài nguyên](../04-concurrency/goroutine-leak.md)
- [graceful-shutdown](../06-http-backend/graceful-shutdown.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/context)
