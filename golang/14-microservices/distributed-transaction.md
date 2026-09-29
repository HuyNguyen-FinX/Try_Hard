# Distributed transactions và ownership

## Concept và Mental Model

Atomic commit qua nhiều services cần protocol/coordination; local sql.Tx không bao HTTP calls.

## How it works

Ưu tiên local invariant+outbox; saga cho cross-service workflow có intermediate states và compensation. Two-phase commit có availability/operations trade-offs.

## Production Use Case

Reserve inventory rồi authorize payment, persist saga progress và idempotent commands.

## Failure Scenarios

Timeout sau provider success; compensation fail; retry duplicate side effect.

## How I would debug this in production

Track saga state/age, command IDs và reconcile source systems.

## Trade-offs và When NOT to use

Không tách một invariant mạnh qua services khi chưa có lý do và recovery design.

## Interview practice

Why is calling two services inside one Go function not atomic? Mỗi service commit độc lập và network có failure windows.

## Key Takeaways

Atomic commit qua nhiều services cần protocol/coordination; local sql.Tx không bao HTTP calls..


## See also

- [Microservices: independent ownership có chi phí](../11-software-architecture/microservices.md)
- [Distributed failure matrix](../12-distributed-systems/failure-scenarios.md)
- [tracing](../17-observability/tracing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://grpc.io/docs/guides/)

## Applied drill

Workflow order→inventory→payment phải ghi state sau mỗi local commit và dùng stable command IDs. Nếu payment timeout, compensation release stock ngay có thể sai khi charge đã xảy ra; chuyển unknown/reconcile theo product policy. Một saga state machine cần retry và compensation retry riêng, với alert cho stuck transitions chứ không chỉ request failure counters.
