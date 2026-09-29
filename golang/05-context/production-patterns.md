# Context trong production request tree

## Concept và Mental Model

Một root request budget chia cho admission, downstream và response; service lifecycle riêng cho workers.

## How it works

Child timeout defer cancel; errors wrap bằng %w; fail-fast phải cancel siblings rồi join; durable jobs có state/retry ngoài request.

## Production Use Case

Graceful shutdown dừng intake, đợi request bình thường trước cancel base context nếu muốn drain.

## Failure Scenarios

Dùng signal context làm base cho toàn request khiến SIGTERM cancel ngay mọi in-flight khi intended behavior là drain.

## How I would debug this in production

Test shutdown dưới load và cancel từng dependency; đo in-flight count về zero trước close DB.

## Trade-offs và When NOT to use

Drain dài bảo vệ completion nhưng cần termination grace budget; abort cần idempotent replay.

## Interview practice

How would you avoid canceling in-flight work too early during shutdown? Tách signal notification khỏi request base cancellation.

## Key Takeaways

Một root request budget chia cho admission, downstream và response; service lifecycle riêng cho workers..


## See also

- [Context: cây lifetime và cooperative cancellation](context-basics.md)
- [Goroutine leaks: blocked work còn giữ tài nguyên](../04-concurrency/goroutine-leak.md)
- [graceful-shutdown](../06-http-backend/graceful-shutdown.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/context)
