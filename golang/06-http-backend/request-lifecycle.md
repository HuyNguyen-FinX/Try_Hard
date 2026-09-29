# HTTP request lifecycle

## Concept và Mental Model

Request đi qua network, middleware, handler, dependencies rồi response cleanup.

## How it works

Middleware order thường recovery/trace, auth, admission rồi business handler; order cụ thể phụ thuộc error/security contract. Context đi xuyên chain.

## Production Use Case

Measure tổng duration và dependency spans; inbound body bounded, outbound body closed.

## Failure Scenarios

Middleware đọc hết body rồi handler không còn input; status đã commit trước khi error mapper chạy.

## How I would debug this in production

Correlate route template, status và spans; kiểm tra middleware wrappers preserve interfaces cần thiết.

## Trade-offs và When NOT to use

Đừng ghi raw URL/query làm label vì cardinality và PII.

## Interview practice

Where does handler latency exclude upstream queuing? LB/admission spans cần tách để thấy queue time.

## Key Takeaways

Request đi qua network, middleware, handler, dependencies rồi response cleanup..


## See also

- [net/http: server, handler và request lifetime](net-http.md)
- [HTTP client reuse và response ownership](http-client.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/net/http)

## Applied drill

Vẽ riêng ba timelines: client disconnect trước DB acquire, disconnect khi query chạy, disconnect sau commit trước response. Cả ba có thể báo context error ở client nhưng durable outcomes khác nhau. Test handler không dùng ResponseWriter từ background G sau return. Request body được server cleanup không cho phép bỏ qua body limits hoặc decode errors trong handler.
