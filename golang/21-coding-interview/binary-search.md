# Binary search bằng half-open interval

## Concept và Mental Model

LowerBound tìm first index có value≥target trong sorted input; kết quả có thể len nếu không có.

## How it works

Maintain [left,right) candidates, mid=left+(right-left)/2; nums[mid]<target thì left=mid+1, ngược lại right=mid. O(log n), O(1).

## Production Use Case

Cursor/index lookup theo monotonic predicate; database index vẫn có I/O costs khác.

## Failure Scenarios

Off-by-one, infinite loop không shrink, overflow midpoint, input không sorted.

## How I would debug this in production

Fuzz partition property: mọi j<i nhỏ hơn target, mọi j≥i không nhỏ hơn.

## Trade-offs và When NOT to use

Linear scan tốt cho very small data; predicate phải monotonic.

## Interview practice

What invariant makes lower-bound binary search correct? Answer luôn nằm trong closed boundary range [left,right] của partition search.

## Key Takeaways

LowerBound tìm first index có value≥target trong sorted input; kết quả có thể len nếu không có..


## See also

- [README](../examples/README.md)
- [Coding interview workflow](go-coding-patterns.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)

## Runnable solution

[Algorithms implementation](../examples/algorithms.go) và [edge-case/property tests](../examples/algorithms_test.go)

Chạy từ `golang/examples`: `go test -race ./...`. Đọc contract ở function comment; không mở rộng numeric/Unicode/cycle assumptions mà không đổi validation và tests.
