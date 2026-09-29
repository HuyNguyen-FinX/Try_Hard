# Coding interview workflow

## Concept và Mental Model

Clarify input domain, mutation, nil/empty, overflow và ordering trước code.

## How it works

State invariant và complexity, viết simplest correct algorithm, dry-run edge cases, rồi optimize nếu constraint đòi. Go map/slice ownership và cleanup là một phần answer.

## Production Use Case

Parser/worker interview cần context và bounded resources, không chỉ algorithm happy path.

## Failure Scenarios

Code compile nhưng ignores error; int overflow; solution sửa input dù contract cấm.

## How I would debug this in production

Run examples tests, race cho concurrency và fuzz invariant; đọc failing minimal input.

## Trade-offs và When NOT to use

Không dùng clever unsafe hoặc generic abstraction để che logic bài nhỏ.

## Interview practice

How would you explain correctness before coding? Nêu invariant và cách mỗi iteration giữ nó.

## Key Takeaways

Clarify input domain, mutation, nil/empty, overflow và ordering trước code..


## See also

- [README](../examples/README.md)
- [Coding interview workflow](go-coding-patterns.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)

## Runnable solution

[Algorithms implementation](../examples/algorithms.go) và [edge-case/property tests](../examples/algorithms_test.go)

Chạy từ `golang/examples`: `go test -race ./...`. Đọc contract ở function comment; không mở rộng numeric/Unicode/cycle assumptions mà không đổi validation và tests.
