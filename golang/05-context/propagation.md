# Propagation qua process boundary

## Concept và Mental Model

Context object không đi qua network; deadline, trace headers và auth metadata được serialize theo protocol.

## How it works

HTTP request dùng context; gRPC deadline/metadata theo client API; Kafka headers chứa trace linkage nhưng consumer có processing lifetime riêng.

## Production Use Case

Consumer nhận job đã accepted dùng bounded service context và trace link tới producer.

## Failure Scenarios

Giữ request deadline đã hết cho durable job; forward auth headers sang untrusted host.

## How I would debug this in production

Inspect trace parentage, client span timing và remaining budget; không log raw tokens.

## Trade-offs và When NOT to use

Propagate metadata có allowlist; async boundaries cần deadline policy mới.

## Interview practice

Does a Kafka message carry a live Go context? Không, chỉ serialized metadata và correlation.

## Key Takeaways

Context object không đi qua network; deadline, trace headers và auth metadata được serialize theo protocol..


## See also

- [Context: cây lifetime và cooperative cancellation](context-basics.md)
- [Goroutine leaks: blocked work còn giữ tài nguyên](../04-concurrency/goroutine-leak.md)
- [graceful-shutdown](../06-http-backend/graceful-shutdown.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/context)
