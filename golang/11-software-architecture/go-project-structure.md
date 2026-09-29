# Go project structure không có một luật duy nhất

## Concept và Mental Model

Go không có một project structure chính thức bắt buộc cho mọi project; package/import rules mới là ràng buộc tooling.

## How it works

Ví dụ cmd/api, internal/user, internal/payment, internal/platform, migrations, configs. pkg/ chỉ khi có public reusable packages thật, có thể bỏ. internal có import visibility rule của Go toolchain.

## Production Use Case

cmd chỉ wiring/lifecycle; domain nằm internal; migrations versioned; config schema validate startup.

## Failure Scenarios

pkg thành dumping ground; utils chứa unrelated behavior; folder architecture kéo import cycles.

## How I would debug this in production

go list/import graph và tìm owner của change; package name phải nói trách nhiệm.

## Trade-offs và When NOT to use

Small app bắt đầu ít packages rồi tách theo cohesion; không scaffold rỗng hàng chục layers.

## Interview practice

Is pkg required by Go? Không; internal có semantics đặc biệt còn pkg chỉ là convention.

## Key Takeaways

Go không có một project structure chính thức bắt buộc cho mọi project; package/import rules mới là ràng buộc tooling..


## See also

- [Interfaces: behavior, representation và typed nil](../01-go-core/interfaces.md)
- [Transactions và short critical sections](../08-database/transactions.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/modules/layout)

## Ví dụ triển khai

```text
cmd/api/main.go
cmd/worker/main.go
internal/user/
internal/payment/
internal/platform/
pkg/                 # optional reusable public APIs
migrations/
configs/              # schema/examples, khong luu secrets that
```

Một module có thể tạo hai binaries API/worker nhưng vẫn dùng chung domain packages. Chỉ tách module khi version/release lifecycle cần độc lập.
