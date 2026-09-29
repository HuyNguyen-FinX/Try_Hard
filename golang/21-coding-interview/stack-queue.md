# Stack và queue bằng slices

## Concept và Mental Model

Stack LIFO dùng append/pop cuối; queue FIFO cần tránh dịch toàn slice mỗi Pop.

## How it works

Queue có head index, clear slot đã lấy để bỏ references; compact khi consumed prefix lớn, reset khi empty. Amortized O(1), occasional copy.

## Production Use Case

BFS queue hoặc local bounded scheduler; concurrency cần mutex/channel tùy ownership.

## Failure Scenarios

Pop bằng s=s[1:] giữ giant array; không clear pointer slot giữ objects; concurrent accesses race.

## How I would debug this in production

Test order qua compaction, empty pop và storage release sau drain.

## Trade-offs và When NOT to use

Ring buffer tốt cho fixed bound; dynamic slice queue linh hoạt nhưng cần memory policy.

## Interview practice

Why clear consumed pointer slots? Header capacity có thể giữ array và references phía sau vẫn reachable.

## Key Takeaways

Stack LIFO dùng append/pop cuối; queue FIFO cần tránh dịch toàn slice mỗi Pop..


## See also

- [README](../examples/README.md)
- [Coding interview workflow](go-coding-patterns.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)

## Runnable solution

[Algorithms implementation](../examples/algorithms.go) và [edge-case/property tests](../examples/algorithms_test.go)

Chạy từ `golang/examples`: `go test -race ./...`. Đọc contract ở function comment; không mở rộng numeric/Unicode/cycle assumptions mà không đổi validation và tests.
