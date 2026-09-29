# Slices/maps coding: Two Sum

## Concept và Mental Model

Hash lookup đổi brute force O(n²) thành expected O(n) time với O(n) memory.

## How it works

TwoSum lưu index đã đi qua; lookup complement trước insert để không reuse cùng index. Duplicate values hợp lệ nếu indices khác. Integer subtraction cần domain không overflow.

## Production Use Case

Dedup/joins in-memory trong batch bounded, không giữ map toàn stream vô hạn.

## Failure Scenarios

Insert trước lookup trả cùng index; map không init; memory grows với input không bound.

## How I would debug this in production

Test [3,3], target 6; no pair; empty; negative values và boundary numeric domain.

## Trade-offs và When NOT to use

Sorted two-pointers O(1) extra space nếu input sorted; sort làm đổi original indices trừ giữ mapping.

## Interview practice

Why must lookup precede insertion? Đảm bảo pair gồm hai positions đã phân biệt.

## Key Takeaways

Hash lookup đổi brute force O(n²) thành expected O(n) time với O(n) memory..


## See also

- [README](../examples/README.md)
- [Coding interview workflow](go-coding-patterns.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)

## Runnable solution

[Algorithms implementation](../examples/algorithms.go) và [edge-case/property tests](../examples/algorithms_test.go)

Chạy từ `golang/examples`: `go test -race ./...`. Đọc contract ở function comment; không mở rộng numeric/Unicode/cycle assumptions mà không đổi validation và tests.
