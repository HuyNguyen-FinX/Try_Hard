# Microservices: independent ownership có chi phí

## Concept và Mental Model

Service boundary mang network failures, version skew và independent deployment; cần lý do ngoài code size.

## How it works

Tách theo business capability và data ownership; sync calls bounded deadlines, async events có replay/idempotency.

## Production Use Case

Payment independent reliability/compliance lifecycle, order qua API/event contract.

## Failure Scenarios

Distributed monolith với synchronous call chain dài và shared DB writes.

## How I would debug this in production

Service graph, fan-out, deployment coupling và incident blast radius.

## Trade-offs và When NOT to use

Không extract khi team chưa vận hành observability/on-call/versioning; modular monolith có thể đủ.

## Interview practice

When does a microservice boundary earn its operational cost? Khi autonomy/scale/isolation benefit đo được.

## Key Takeaways

Service boundary mang network failures, version skew và independent deployment; cần lý do ngoài code size..


## See also

- [Interfaces: behavior, representation và typed nil](../01-go-core/interfaces.md)
- [Transactions và short critical sections](../08-database/transactions.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/modules/layout)

## Applied drill

Trước extract notification, đo deploy coupling, provider-specific scaling và incident blast radius. Nếu tách, cần durable outbox từ order, event schema version, idempotent delivery và dashboard oldest notification age. Nếu chưa có owners/on-call cho hai services, separation code trong monolith có thể đạt phần lớn lợi ích với ít failure paths hơn.
