# Ports và adapters

## Concept và Mental Model

Port là contract tại boundary; adapter chuyển protocol/infrastructure sang contract đó.

## How it works

Inbound HTTP/gRPC gọi use case; outbound SQL/provider implement interface do consumer định nghĩa. Constructor nối concrete adapters.

## Production Use Case

Payment gateway adapter chuyển vendor status sang domain result có ambiguous outcome rõ.

## Failure Scenarios

Vendor error/type rò qua domain; mocks chỉ mô phỏng implementation thay contract.

## How I would debug this in production

Contract tests chạy cùng cases cho adapter fake/real khi thích hợp.

## Trade-offs và When NOT to use

Ports quá nhỏ/không có substitution làm ceremony; chọn boundary theo volatility.

## Interview practice

Where should an interface live? Gần consumer sở hữu nhu cầu behavior.

## Key Takeaways

Port là contract tại boundary; adapter chuyển protocol/infrastructure sang contract đó..


## See also

- [Interfaces: behavior, representation và typed nil](../01-go-core/interfaces.md)
- [Transactions và short critical sections](../08-database/transactions.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/modules/layout)

## Applied drill

Port PaymentAuthorizer nên diễn tả Authorize(ctx, operationID, amount) và outcome confirmed/unknown/rejected theo domain. Nếu port trả raw vendor response và HTTP status, domain vẫn coupled vendor dù interface tồn tại. Adapter chịu mapping, deadline propagation và error wrapping. Contract test phải có timeout-after-effect case vì fake luôn trả success không kiểm recovery behavior.
