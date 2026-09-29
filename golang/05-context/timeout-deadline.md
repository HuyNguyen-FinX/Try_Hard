# Timeout và deadline budget

## Concept và Mental Model

Timeout là duration; deadline là thời điểm tuyệt đối. Remaining budget phải giảm dọc call chain.

## How it works

Child deadline là minimum của parent và requested deadline. Budget gồm queue wait, retry delay, work và cleanup; không reset đầy đủ timeout ở mỗi hop.

## Production Use Case

Request 200ms có thể dành 20ms admission, 120ms downstream, 40ms serialize/network và 20ms headroom tùy measurements.

## Failure Scenarios

Ba retries mỗi lần 200ms phá deadline 200ms; deadline ngắn hơn normal P99 gây retry storm.

## How I would debug this in production

Trace budget còn lại và per-attempt latency; phân biệt connect với response/body timeout.

## Trade-offs và When NOT to use

Timeout nhỏ giảm resource retention nhưng có false timeout; derive từ SLO và latency histogram.

## Interview practice

Why does a timeout not reveal whether the server committed? Response có thể bị mất sau commit.

## Key Takeaways

Timeout là duration; deadline là thời điểm tuyệt đối.


## See also

- [Context: cây lifetime và cooperative cancellation](context-basics.md)
- [Goroutine leaks: blocked work còn giữ tài nguyên](../04-concurrency/goroutine-leak.md)
- [graceful-shutdown](../06-http-backend/graceful-shutdown.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/context)
