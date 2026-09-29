# Two pointers trên sorted data

## Concept và Mental Model

Sorted order cho phép loại một đầu sau mỗi comparison, đạt O(n) time/O(1) extra space.

## How it works

Nếu sum<target tăng left vì mọi pair với current left và right nhỏ hơn nữa không đủ; sum>target giảm right. Distinct indices left<right.

## Production Use Case

Merge/intersection/dedup sorted batches; arithmetic cần no-overflow domain hoặc checked operations.

## Failure Scenarios

Dùng trên unsorted input; mutation/sort làm mất original index; overflow sum đảo comparison.

## How I would debug this in production

Test duplicates, no result, minimal length và extreme values theo contract.

## Trade-offs và When NOT to use

Hash map giữ original indices khi unsorted, tốn memory; sort rồi pointers thêm O(n log n).

## Interview practice

Why does sorting enable pointer elimination? Monotonic order chứng minh các candidates bị bỏ không thể là answer.

## Key Takeaways

Sorted order cho phép loại một đầu sau mỗi comparison, đạt O(n) time/O(1) extra space..


## See also

- [README](../examples/README.md)
- [Coding interview workflow](go-coding-patterns.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)

## Runnable solution

[Algorithms implementation](../examples/algorithms.go) và [edge-case/property tests](../examples/algorithms_test.go)

Chạy từ `golang/examples`: `go test -race ./...`. Đọc contract ở function comment; không mở rộng numeric/Unicode/cycle assumptions mà không đổi validation và tests.
