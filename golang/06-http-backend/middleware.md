# Middleware và interface preservation

## Concept và Mental Model

Middleware wrap Handler để xử lý concern xuyên endpoints với ordering rõ.

## How it works

Record status mặc định 200 và bytes; không gọi WriteHeader lần hai. Wrapper cần preserve Flusher/Hijacker hoặc hỗ trợ Unwrap/ResponseController theo yêu cầu.

## Production Use Case

Auth principal vào context, metrics label route template, recovery log stack bounded.

## Failure Scenarios

Response recorder wrapper phá WebSocket/streaming; log token; middleware retry response đã partial.

## How I would debug this in production

httptest cho order, panic trước/sau header, flush và hijack behavior.

## Trade-offs và When NOT to use

Không đặt business transaction logic tùy endpoint vào global middleware mơ hồ.

## Interview practice

How can middleware break a valid handler? Wrapper có thể mất optional interfaces hoặc consume body.

## Key Takeaways

Middleware wrap Handler để xử lý concern xuyên endpoints với ordering rõ..


## See also

- [net/http: server, handler và request lifetime](net-http.md)
- [HTTP client reuse và response ownership](http-client.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/net/http)

## Applied drill

Viết test chain trace→auth→handler và assert unauthorized request không vào business handler. Sau đó dùng streaming handler gọi Flush qua wrapper; ResponseRecorder-only test không đủ chứng minh WebSocket hijack. Recorder phải ghi status chỉ một lần và giữ bytes count khi Write trả partial/error. Middleware timing cần nói rõ có gồm response body streaming toàn bộ hay chỉ setup.
