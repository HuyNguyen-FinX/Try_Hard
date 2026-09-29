# Go philosophy

## Concept và Mental Model

Go ưu tiên composition, explicit control flow và API nhỏ. Zero value dùng được giúp giảm trạng thái khởi tạo không hợp lệ.

## How it works

Bắt đầu bằng concrete function; extract interface tại consumer khi có substitution thật. Gofmt thống nhất hình thức; error values làm đường lỗi hiển thị ở call site.

## Production Use Case

Service user có constructor nhận repository và clock; business code không import HTTP framework.

## Failure Scenarios

Interface cho từng struct và goroutine cho từng bước biến code tuần tự thành lifecycle khó quản lý.

## How I would debug this in production

Đọc import graph và trace một request; đếm object cần Close/Stop và ai sở hữu chúng.

## Trade-offs và When NOT to use

Sự rõ ràng thường đáng giá hơn framework tự động; tránh abstraction khi chỉ có một caller.

## Interview practice

Why is explicit dependency injection useful in Go? Trả lời bằng lifecycle của DB pool và khả năng test clock.

## Key Takeaways

Go ưu tiên composition, explicit control flow và API nhỏ.


## See also

- [Interfaces: behavior, representation và typed nil](interfaces.md)
- [Error handling và error chains](errors.md)
- [unit-testing](../18-testing/unit-testing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)
