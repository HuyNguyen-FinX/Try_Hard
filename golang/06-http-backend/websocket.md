# WebSocket: long-lived connection lifecycle

## Concept và Mental Model

WebSocket là duplex session sống lâu hơn HTTP request thông thường sau upgrade.

## How it works

Registry quản lý connections, bounded outbound queue mỗi client, ping/pong deadline và single-writer protocol theo library. Shutdown HTTP không tự drain hijacked sessions.

## Production Use Case

Chat disconnect slow consumer, resume bằng durable message sequence.

## Failure Scenarios

Broadcast goroutine per message/client tạo explosion; slow client giữ unbounded queue; reconnect storm.

## How I would debug this in production

Connection count, queue bytes/age, ping failures và send-block stacks; test network half-open.

## Trade-offs và When NOT to use

Không dùng websocket khi polling/SSE đáp ứng một chiều đơn giản hơn; library-specific concurrency phải đọc docs.

## Interview practice

How would you handle a client that reads too slowly? Bound queue, policy drop/disconnect và replay.

## Key Takeaways

WebSocket là duplex session sống lâu hơn HTTP request thông thường sau upgrade..


## See also

- [net/http: server, handler và request lifetime](net-http.md)
- [HTTP client reuse và response ownership](http-client.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/net/http)
