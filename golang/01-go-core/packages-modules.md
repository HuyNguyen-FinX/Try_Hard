# Packages và modules

## Concept và Mental Model

Package là đơn vị encapsulation/import; module là tập package được version bằng go.mod.

## How it works

go.mod ghi module path và Go version; go.sum chứa checksum, không phải lockfile chọn version. Minimal Version Selection chọn version cao nhất được yêu cầu trong graph. Major v2+ thường có suffix /v2.

## Production Use Case

Pin toolchain trong CI; dùng go mod tidy, go mod verify và xem go list -m all khi dependency thay đổi.

## Failure Scenarios

replace trỏ local path làm CI fail; import cycle báo boundary sai; init mở network khiến test bất ổn.

## How I would debug this in production

So sánh go env, go.mod, go.sum và module graph giữa local/CI; kiểm tra GOPRIVATE cho private modules.

## Trade-offs và When NOT to use

Một module đơn giản dễ release; nhiều module cần khi lifecycle version thực sự độc lập.

## Interview practice

How would you debug a dependency version mismatch? Giải thích MVS và replace chỉ tác động module chính.

## Key Takeaways

Package là đơn vị encapsulation/import; module là tập package được version bằng go.mod..


## See also

- [Interfaces: behavior, representation và typed nil](interfaces.md)
- [Error handling và error chains](errors.md)
- [unit-testing](../18-testing/unit-testing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)
