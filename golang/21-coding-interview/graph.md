# Graph BFS và visited timing

## Concept và Mental Model

BFS tìm shortest edge-count paths trong unweighted graph; weighted graph cần thuật toán khác.

## How it works

Mark visited khi enqueue để mỗi vertex vào queue một lần; distance[next]=distance[v]+1. O(V+E), map adjacency traversal order không deterministic nếu iterate map.

## Production Use Case

Dependency reachability và shortest hop count; real network latency không là edge-count distance.

## Failure Scenarios

Mark lúc dequeue enqueue duplicates; cycles không visited vô hạn; disconnected vertices bị assume reachable.

## How I would debug this in production

Test cycle, self-loop, disconnected node và multiple shortest paths; compare distances thay exact traversal order.

## Trade-offs và When NOT to use

Dijkstra cho nonnegative weights; DFS phù hợp reachability/topological work với cycle checks.

## Interview practice

Why mark visited before enqueue? Tránh nhiều predecessors enqueue cùng vertex.

## Key Takeaways

BFS tìm shortest edge-count paths trong unweighted graph; weighted graph cần thuật toán khác..


## See also

- [README](../examples/README.md)
- [Coding interview workflow](go-coding-patterns.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)

## Runnable solution

[Algorithms implementation](../examples/algorithms.go) và [edge-case/property tests](../examples/algorithms_test.go)

Chạy từ `golang/examples`: `go test -race ./...`. Đọc contract ở function comment; không mở rộng numeric/Unicode/cycle assumptions mà không đổi validation và tests.
