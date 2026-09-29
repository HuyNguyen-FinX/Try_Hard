# Concurrency coding interview

## Concept và Mental Model

Đúng concurrency gồm results, cancellation, bounded resource use và termination proof.

## How it works

Thiết kế owners cho input/output/close; Add trước launch, context ở mọi blocking operation, join trước return. Error policy fail-fast hay best-effort phải nói rõ.

## Production Use Case

Implement bounded worker pool có worker error và caller cancel như examples/pool.go.

## Failure Scenarios

Hidden leak khi result reader exit; close chung từ nhiều workers; spawn trước acquire vô hạn waiters.

## How I would debug this in production

Test completion counts, bound active workers, first error cancellation và no active worker khi return.

## Trade-offs và When NOT to use

Synchronous baseline nếu không cần parallel; đừng tối ưu scheduling trước correctness.

## Interview practice

How do you prove your pool cannot leak after cancellation? Mọi block có exit, fn honors ctx và owner waits all workers.

## Key Takeaways

Đúng concurrency gồm results, cancellation, bounded resource use và termination proof..


## See also

- [README](../examples/README.md)
- [Coding interview workflow](go-coding-patterns.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)

## Runnable solution

[Worker pool và tests](../examples/pool.go)

Chạy từ `golang/examples`: `go test -race ./...`. Đọc contract ở function comment; không mở rộng numeric/Unicode/cycle assumptions mà không đổi validation và tests.
