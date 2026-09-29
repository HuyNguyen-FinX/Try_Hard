# HTTP timeout layers

## Concept và Mental Model

Deadline tổng khác timeout từng network phase.

## How it works

Client.Timeout gồm body read; Dial timeout cho kết nối, TLSHandshakeTimeout cho TLS, ResponseHeaderTimeout cho headers, IdleConnTimeout cho idle sockets. Server timeout không kill arbitrary Go work.

## Production Use Case

Budget 200ms chia admission/connect/dependency/serialize với headroom; từng hop lấy remaining parent deadline.

## Failure Scenarios

Timeout retry không idempotent tạo duplicate; header nhận nhanh nhưng body chậm vượt budget.

## How I would debug this in production

httptrace và request spans tách pool wait/connect/TTFB/body; errors.Is context deadline với wrapped errors.

## Trade-offs và When NOT to use

Streaming không hợp total timeout ngắn; cần idle/progress policy riêng.

## Interview practice

Why can headers arrive successfully but body reading timeout? Body vẫn nằm trong total client deadline.

## Key Takeaways

Deadline tổng khác timeout từng network phase..


## See also

- [net/http: server, handler và request lifetime](net-http.md)
- [HTTP client reuse và response ownership](http-client.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/net/http)

## Applied drill

Experiment server trả headers sau20ms rồi body sau2s; client timeout500ms phải fail trong body read dù header timeout100ms không hết. Test khác giữ connection cap1 và occupy slot: request thứ hai có thể hết budget trước dial. Dùng httptrace để phân biệt acquisition wait với remote first-byte latency, rồi size concurrency theo evidence thay tăng mọi timeout.
