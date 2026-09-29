# Runtime internals: ranh giới contract

## Concept và Mental Model

Language spec và public package docs là contract; runtime source giải thích implementation cụ thể.

## How it works

Đọc proc.go, chan.go, mgc.go và internal/runtime/maps theo tag Go đang deploy. Compiler flags và GODEBUG cũng có lifecycle/version.

## Production Use Case

Incident note ghi go version, GOOS/GOARCH, build flags, GOMAXPROCS và container quota.

## Failure Scenarios

Dùng bucket diagram cũ cho Swiss Tables; khẳng định queue size bất biến; tune flag đã đổi behavior.

## How I would debug this in production

Tái hiện trên đúng binary/toolchain; đối chiếu release notes và source tag trước diễn giải trace.

## Trade-offs và When NOT to use

Biết internals để đặt giả thuyết, không phụ thuộc ABI/private struct bằng unsafe trong business code.

## Interview practice

Which scheduler claims are language guarantees? Hầu hết queue/policy là implementation, synchronization semantics mới là contract.

## Key Takeaways

Language spec và public package docs là contract; runtime source giải thích implementation cụ thể..


## See also

- [Garbage collection: live heap, pacing và memory budget](garbage-collector.md)
- [Escape analysis: đọc quyết định của compiler](escape-analysis.md)
- [memory-profile](../16-performance/memory-profile.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/gc-guide)
