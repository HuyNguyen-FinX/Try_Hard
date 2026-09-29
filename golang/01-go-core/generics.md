# Generics và constraints

## Concept và Mental Model

Generics tái dùng thuật toán với type safety; interface behavior và type parameter giải quyết nhu cầu khác nhau.

## How it works

Constraint type set giới hạn operations; ~T chấp nhận underlying type T. comparable cần cho map keys. Compiler strategy phụ thuộc release, không giả định mọi instantiation đều được monomorphize độc lập.

## Production Use Case

Dùng generic set hoặc slice transform khi giảm lặp và giữ API rõ; business service thường chỉ cần concrete types.

## Failure Scenarios

Constraint quá rộng gây compile errors; API generic nhiều parameters khó infer; dùng any rồi assertions mất lợi ích.

## How I would debug this in production

Đọc compiler error tại constraint, benchmark binary size/allocation nếu nằm hot path.

## Trade-offs và When NOT to use

Không thay mọi interface bằng generic; runtime polymorphism cần interface value.

## Interview practice

When is a generic function better than an interface parameter? So sánh thuật toán trên type set với dependency có behavior.

## Key Takeaways

Generics tái dùng thuật toán với type safety; interface behavior và type parameter giải quyết nhu cầu khác nhau..


## See also

- [Interfaces: behavior, representation và typed nil](interfaces.md)
- [Error handling và error chains](errors.md)
- [unit-testing](../18-testing/unit-testing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)
