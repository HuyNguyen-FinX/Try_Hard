# Tree traversal và depth

## Concept và Mental Model

Inorder binary tree là left,node,right; với BST hợp lệ kết quả sorted theo invariant.

## How it works

Iterative stack tránh recursion depth lớn; each node push/pop một lần O(n), auxiliary O(height). Clear popped pointers nếu stack giữ backing array lâu.

## Production Use Case

Nested config/AST traversal cần bound depth và detect cycle nếu structure không bảo đảm tree.

## Failure Scenarios

Assume mọi binary tree là BST; skewed tree recursion làm stack growth lớn.

## How I would debug this in production

Test empty, balanced, skewed và duplicate-key policy; verify traversal order độc lập.

## Trade-offs và When NOT to use

Recursive code dễ đọc cho bounded depth; iterative dễ kiểm memory/cancellation.

## Interview practice

Why is traversal space O(height) rather than O(n) in the balanced case? Stack chỉ giữ ancestor path.

## Key Takeaways

Inorder binary tree là left,node,right; với BST hợp lệ kết quả sorted theo invariant..


## See also

- [README](../examples/README.md)
- [Coding interview workflow](go-coding-patterns.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)

## Runnable solution

[Algorithms implementation](../examples/algorithms.go) và [edge-case/property tests](../examples/algorithms_test.go)

Chạy từ `golang/examples`: `go test -race ./...`. Đọc contract ở function comment; không mở rộng numeric/Unicode/cycle assumptions mà không đổi validation và tests.
