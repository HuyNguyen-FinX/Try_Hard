# Modular monolith

## Concept và Mental Model

Một deployable có domain boundaries rõ giúp tránh network/distributed transaction trước khi cần.

## How it works

internal/user và internal/payment expose API nhỏ, tránh truy cập tables/state nhau tùy tiện; contracts có tests.

## Production Use Case

Bắt đầu một binary, scale replicas; extract module khi workload/team autonomy chứng minh lợi ích.

## Failure Scenarios

Shared DB bị dùng làm backdoor qua module; package cycles; một global service phụ thuộc tất cả.

## How I would debug this in production

Import graph, ownership map và change lead time cho thấy coupling.

## Trade-offs và When NOT to use

Deployment chung ít vận hành nhưng scale/failure isolation kém services độc lập.

## Interview practice

What makes a monolith modular? Enforced contracts và ownership, không chỉ folders.

## Key Takeaways

Một deployable có domain boundaries rõ giúp tránh network/distributed transaction trước khi cần..


## See also

- [Interfaces: behavior, representation và typed nil](../01-go-core/interfaces.md)
- [Transactions và short critical sections](../08-database/transactions.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/modules/layout)

## Applied drill

Architecture test/review có thể cấm payment import user storage adapter; payment chỉ dùng user public contract cần thiết. Một schema DB chung vẫn có table ownership và migrations owner. Khi extract module, đo cross-module queries/transactions trước: chúng là migration work thật, không biến mất chỉ vì tạo thêm binary hoặc repository.
