# Methods và method sets

## Concept và Mental Model

Method gắn behavior vào named type; receiver value copy state, pointer receiver cho phép mutation trên object.

## How it works

T method set không gồm method chỉ khai báo trên *T. Addressable local T gọi pointer method được bằng compiler convenience; interface assignment vẫn tuân method set.

## Production Use Case

Giữ receiver style nhất quán khi type có mutable state; API có mutex dùng *T.

## Failure Scenarios

Value receiver tăng counter trên bản copy; interface compile failure bị hiểu nhầm là compiler không tự lấy địa chỉ.

## How I would debug this in production

Viết compile-time interface assertion và unit test observable mutation.

## Trade-offs và When NOT to use

Value receiver tốt cho value object nhỏ; pointer receiver mang nil và aliasing vào contract.

## Interview practice

Why can v.M work while assigning v to an interface fails? Phân biệt call syntax với method set.

## Key Takeaways

Method gắn behavior vào named type; receiver value copy state, pointer receiver cho phép mutation trên object..


## See also

- [Interfaces: behavior, representation và typed nil](interfaces.md)
- [Error handling và error chains](errors.md)
- [unit-testing](../18-testing/unit-testing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)
