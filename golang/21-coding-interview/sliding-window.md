# Sliding window: unique bytes

## Concept và Mental Model

Window [left,right] giữ invariant không lặp; last-seen index cho phép nhảy left thay scan lại.

## How it works

Store last index+1, update left=max(left,last[b]); count right-left+1. O(n) time,256 slots cho bytes. Unicode rune/grapheme là contract khác.

## Production Use Case

Byte protocol tokens hoặc ASCII interview problem; user-visible text cần chọn Unicode semantics.

## Failure Scenarios

Input abba làm left lùi nếu không max; rune dùng byte indexing sai.

## How I would debug this in production

Test empty, repeated, abba và non-ASCII để nêu giới hạn byte algorithm.

## Trade-offs và When NOT to use

Window chỉ hợp khi invariant cập nhật incremental; không áp mù cho non-monotonic constraints.

## Interview practice

Why must left never move backwards? Prefix đã loại không thể tái nhập mà phá unique window.

## Key Takeaways

Window [left,right] giữ invariant không lặp; last-seen index cho phép nhảy left thay scan lại..


## See also

- [README](../examples/README.md)
- [Coding interview workflow](go-coding-patterns.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)

## Runnable solution

[Algorithms implementation](../examples/algorithms.go) và [edge-case/property tests](../examples/algorithms_test.go)

Chạy từ `golang/examples`: `go test -race ./...`. Đọc contract ở function comment; không mở rộng numeric/Unicode/cycle assumptions mà không đổi validation và tests.
