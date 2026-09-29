# Top K với min-heap

## Concept và Mental Model

Heap size K giữ K largest seen; root là nhỏ nhất trong selected set, dễ loại khi gặp value lớn hơn.

## How it works

O(n log K) time/O(K) memory; container/heap yêu cầu Len/Less/Swap và pointer Push/Pop. Fix root sau replace, output heap pop ascending theo implementation example.

## Production Use Case

Top metrics trong bounded batch; streaming top-K cần define window/expiry khác static input.

## Failure Scenarios

Nhầm min/max orientation; K0 index panic; returning heap array tưởng sorted.

## How I would debug this in production

Test duplicates, negative values, K0/K>n và order của output; benchmark K nhỏ/lớn.

## Trade-offs và When NOT to use

Sort O(n log n) đơn giản nếu cần full ordered result; quickselect đổi worst-case/stability.

## Interview practice

Why is a min-heap useful for the largest K values? Root là candidate nhỏ nhất cần thay.

## Key Takeaways

Heap size K giữ K largest seen; root là nhỏ nhất trong selected set, dễ loại khi gặp value lớn hơn..


## See also

- [README](../examples/README.md)
- [Coding interview workflow](go-coding-patterns.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/container/heap)

## Runnable solution

[Algorithms implementation](../examples/algorithms.go) và [edge-case/property tests](../examples/algorithms_test.go)

Chạy từ `golang/examples`: `go test -race ./...`. Đọc contract ở function comment; không mở rộng numeric/Unicode/cycle assumptions mà không đổi validation và tests.
