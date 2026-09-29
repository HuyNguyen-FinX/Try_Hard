# Linked list reversal

## Concept và Mental Model

Reversal cập nhật next pointers in-place, giữ reference phần chưa xử lý trước khi đổi link.

## How it works

Invariant prev là reversed prefix, head là suffix chưa xử lý. Mỗi bước next=head.Next, head.Next=prev rồi tiến hai pointers. O(n) time/O(1) auxiliary space.

## Production Use Case

Bài luyện pointer ownership; intrusive structures production còn cần concurrency/lifetime protocol.

## Failure Scenarios

Mất next tạo đứt list; cycle input khiến loop vô hạn; aliases nhìn thấy mutation.

## How I would debug this in production

Test nil/single/two nodes và verify tail.Next=nil, node identity giữ nguyên.

## Trade-offs và When NOT to use

Slice thường cache-friendly hơn list; không chọn linked list chỉ vì insert O(1) nếu chưa có node pointer.

## Interview practice

What must be saved before changing Next? Con trỏ tới phần suffix chưa đảo.

## Key Takeaways

Reversal cập nhật next pointers in-place, giữ reference phần chưa xử lý trước khi đổi link..


## See also

- [README](../examples/README.md)
- [Coding interview workflow](go-coding-patterns.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)

## Runnable solution

[Algorithms implementation](../examples/algorithms.go) và [edge-case/property tests](../examples/algorithms_test.go)

Chạy từ `golang/examples`: `go test -race ./...`. Đọc contract ở function comment; không mở rộng numeric/Unicode/cycle assumptions mà không đổi validation và tests.
