# Struct layout và composition

## Concept và Mental Model

Struct gom state có invariant chung; embedding promote method nhưng không tạo subclass.

## How it works

Fields có alignment/padding; unsafe.Sizeof không tính allocations được pointer/slice tham chiếu. JSON tags là metadata của encoder, không phải validation.

## Production Use Case

Tách request DTO khỏi domain object để input không ghi đè field privilege.

## Failure Scenarios

Copy struct chứa slice vẫn alias; exported field phá invariant; embedding vô tình mở rộng public API.

## How I would debug this in production

Kiểm tra field ownership, marshaled payload và benchmark layout nếu memory thực sự chi phối.

## Trade-offs và When NOT to use

Ưu tiên readability trước packing; không export toàn bộ domain chỉ để ORM tiện dùng.

## Interview practice

How can a copied struct still share mutable data? Nêu slice header và map storage.

## Key Takeaways

Struct gom state có invariant chung; embedding promote method nhưng không tạo subclass..


## See also

- [Interfaces: behavior, representation và typed nil](interfaces.md)
- [Error handling và error chains](errors.md)
- [unit-testing](../18-testing/unit-testing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)
