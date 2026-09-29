# Keep-alive: HTTP reuse và TCP liveness

## Concept và Mental Model

HTTP keep-alive là reuse connection; TCP keepalive là probes phát hiện peer chết ở tầng TCP.

## How it works

HTTP/1 reuse cần protocol/body cleanup hợp lệ; server/client/LB có idle policies khác nhau. HTTP/2 multiplex streams trên long-lived connection.

## Production Use Case

Giảm connect/TLS CPU bằng reuse nhưng rotate connections khi lifecycle/DNS/routing yêu cầu.

## Failure Scenarios

Nhầm TCP KeepAlive với request timeout; stale connections sau LB idle expiration.

## How I would debug this in production

Đo reused ratio, reset/EOF errors sau idle và server Connection headers.

## Trade-offs và When NOT to use

Disable keep-alive thường tăng latency/load; chỉ dùng khi protocol/isolation thực sự yêu cầu.

## Interview practice

Does TCP keepalive bound an HTTP request duration? Không, cần context/client deadlines.

## Key Takeaways

HTTP keep-alive là reuse connection; TCP keepalive là probes phát hiện peer chết ở tầng TCP..


## See also

- [net/http: server, handler và request lifetime](net-http.md)
- [HTTP client reuse và response ownership](http-client.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/net/http)
