# Variables, types và zero values

## Concept và Mental Model

Type định nghĩa phép toán hợp lệ; named types giúp chặn nhầm ID với amount dù underlying type giống nhau.

## How it works

:= khai báo trong block và có thể shadow biến bên ngoài. Conversion khác assertion: conversion đổi biểu diễn hợp lệ, assertion kiểm tra dynamic type. Constants untyped được suy type khi dùng.

## Production Use Case

Dùng type UserID string và số nguyên minor units cho amount với currency rõ ràng.

## Failure Scenarios

err bị shadow trong if rồi outer err nil; int overflow trong capacity estimate; zero time được hiểu nhầm là timestamp thật.

## How I would debug this in production

Bật go vet, xem scope và thêm boundary test overflow/zero; kiểm tra type ở JSON decode.

## Trade-offs và When NOT to use

Named type tăng an toàn nhưng cần conversion ở boundary; alias phù hợp migration API.

## Interview practice

How can short declaration shadow an error? Vẽ hai scope và return value quan sát được.

## Key Takeaways

Type định nghĩa phép toán hợp lệ; named types giúp chặn nhầm ID với amount dù underlying type giống nhau..


## See also

- [Interfaces: behavior, representation và typed nil](interfaces.md)
- [Error handling và error chains](errors.md)
- [unit-testing](../18-testing/unit-testing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)
