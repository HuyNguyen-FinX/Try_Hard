# Load balancing: connection versus request

## Concept và Mental Model

LB phân phối traffic theo level/policy; multiplexed connections làm connection balance khác request balance.

## How it works

L4 route TCP flows, L7 hiểu HTTP/RPC; health/readiness update có delay. Least-load policies cần accurate in-flight metrics.

## Production Use Case

Long-lived gRPC/WebSocket cần scale/drain strategy và reconnect/resume.

## Failure Scenarios

Sticky hot tenant, endpoint stale, connection reuse pin backend, cross-zone overload.

## How I would debug this in production

Per-backend RPS/in-flight/latency, connection age và health transitions.

## Trade-offs và When NOT to use

L7 thêm hop/CPU và config complexity; L4 đơn giản nhưng ít visibility request.

## Interview practice

Why might equal connection counts still mean unequal load? Streams/messages và request costs khác nhau.

## Key Takeaways

LB phân phối traffic theo level/policy; multiplexed connections làm connection balance khác request balance..


## See also

- [System design framework cho Senior Go](system-design-framework.md)
- [Design High-Throughput API — 20,000 RPS](design-high-throughput-api.md)
- [Design Migration Platform — 4–5 Billion Records](design-migration-platform.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)

## Applied drill

Lab giữ10 long-lived HTTP/2 connections tới2 pods rồi scale lên4. Nếu LB chỉ route lúc connect, new pods có thể ít traffic cho tới reconnect. Đo request distribution và active streams theo pod; không kết luận HPA hỏng chỉ vì CPU skew. Graceful drain cần connection/stream termination policy để redistribute mà giữ client resume/retry safety.
