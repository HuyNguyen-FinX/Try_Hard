# Context values có scope

## Concept và Mental Model

Values phù hợp request-scoped metadata qua API boundaries: trace identity, authenticated principal đã validate.

## How it works

Dùng private typed keys và accessor trả value,ok. Không dùng string key global dễ collision; không đưa mutable shared state hoặc huge payload.

## Production Use Case

Middleware xác thực tạo principal; domain nhận explicit ID nếu ID là business parameter cần thấy trong signature.

## Failure Scenarios

Missing value panic do type assertion một-value; token bị log từ context dump.

## How I would debug this in production

Kiểm tra middleware order và accessor tests; log metadata allowlist.

## Trade-offs và When NOT to use

Explicit parameters tốt hơn cho required dependencies; context values hữu ích metadata xuyên layers.

## Interview practice

Why should a DB handle not live in context? Dependency cần constructor contract/lifecycle rõ.

## Key Takeaways

Values phù hợp request-scoped metadata qua API boundaries: trace identity, authenticated principal đã validate..


## See also

- [Context: cây lifetime và cooperative cancellation](context-basics.md)
- [Goroutine leaks: blocked work còn giữ tài nguyên](../04-concurrency/goroutine-leak.md)
- [graceful-shutdown](../06-http-backend/graceful-shutdown.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/context)
