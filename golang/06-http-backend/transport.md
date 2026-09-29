# Transport: pool owner

## Concept và Mental Model

Transport là RoundTripper quản lý wire protocol, dialing và reusable connections.

## How it works

Clone DefaultTransport giữ useful defaults; config trước khi share. Custom Dial/TLS settings có thể ảnh hưởng protocol negotiation nên xác nhận HTTP/2 thực tế.

## Production Use Case

Dedicated transports cho dependency cần isolation/proxy/TLS policy khác nhau.

## Failure Scenarios

Transport mới mỗi call; custom proxy header trust sai; HTTP/2 bị vô hiệu ngoài dự kiến.

## How I would debug this in production

httptrace protocol, connection reuse, TLS handshake và FD metrics.

## Trade-offs và When NOT to use

Không tạo transport riêng mỗi tenant khi tenant cardinality lớn trừ có lifecycle/limit rõ.

## Interview practice

Why is Transport reuse more central than Client allocation? Pool ở Transport.

## Key Takeaways

Transport là RoundTripper quản lý wire protocol, dialing và reusable connections..


## See also

- [net/http: server, handler và request lifetime](net-http.md)
- [HTTP client reuse và response ownership](http-client.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/net/http)

## Applied drill

Tạo hai requests tuần tự tới httptest.Server và quan sát GotConn.Reused. So shared Transport với Transport mới mỗi call; đóng body tới EOF ở cả hai để không lẫn biến. Tiếp theo giữ body chưa đọc và xem request concurrency/pool behavior. Đây là controlled experiment cho reuse, không là benchmark network production hoặc HTTP/2 capacity.
