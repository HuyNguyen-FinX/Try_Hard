# HTTP server configuration

## Concept và Mental Model

Explicit Server configuration làm resource budget review được.

## How it works

Set ReadHeaderTimeout, body limits, IdleTimeout và endpoint-specific deadline; ReadTimeout bao đọc request, WriteTimeout có semantics theo connection/protocol cần test.

## Production Use Case

API nhỏ có total request budget; streaming dùng policy riêng và ResponseController khi thích hợp.

## Failure Scenarios

Global WriteTimeout quá ngắn cắt stream; large body không limit gây memory pressure.

## How I would debug this in production

Test slowloris, delayed body, disconnect và partial response; xem LB timeout cùng server config.

## Trade-offs và When NOT to use

Không có một bộ timeout tối ưu cho mọi endpoint.

## Interview practice

How would you configure a public JSON API differently from a streaming endpoint? Phân biệt bounded body với long-lived stream.

## Key Takeaways

Explicit Server configuration làm resource budget review được..


## See also

- [net/http: server, handler và request lifetime](net-http.md)
- [HTTP client reuse và response ownership](http-client.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/net/http)

## Applied drill

Lab gồm ba clients: gửi header từng byte, gửi body lớn hơn giới hạn, và ngắt kết nối khi handler đang gọi downstream. Verify timeout/413/cancellation riêng; không kỳ vọng WriteTimeout tự return hàm CPU loop. Chạy cùng proxy timeout thật để thấy client-observed status có thể khác status handler đã cố ghi. Theo dõi FD và G sau khi clients dừng.
