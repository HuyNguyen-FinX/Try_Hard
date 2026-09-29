# Value versus pointer

## Concept và Mental Model

Go luôn pass by value; pointer value được copy và hai bản copy có thể trỏ cùng object.

## How it works

Chọn pointer khi cần mutation, identity hoặc tránh copy object lớn; slice/map cũng là value có tham chiếu tới storage chung. Pointer không đảm bảo heap và value không đảm bảo stack.

## Production Use Case

DTO nhỏ immutable truyền value; service có mutex truyền pointer và không copy sau first use.

## Failure Scenarios

Copy struct chứa mutex gây hai lock bảo vệ cùng map; nil receiver dereference panic.

## How I would debug this in production

Dùng go vet copylocks, race detector và escape output tại call site thay vì đoán từ dấu &.

## Trade-offs và When NOT to use

Value giảm aliasing nhưng copy field reference vẫn shallow; pointer cần ownership rõ.

## Interview practice

Does returning a pointer force heap allocation? Inlining và escape analysis quyết định allocation thực tế.

## Key Takeaways

Go luôn pass by value; pointer value được copy và hai bản copy có thể trỏ cùng object..


## See also

- [Interfaces: behavior, representation và typed nil](interfaces.md)
- [Error handling và error chains](errors.md)
- [unit-testing](../18-testing/unit-testing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)
