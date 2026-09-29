# Observability như phần design

## Concept và Mental Model

Thiết kế phải cho biết dùng metric/trace/state nào chứng minh invariant và SLO.

## How it works

SLIs tại boundary user thấy; queue age cho async completion; durable IDs cho reconciliation; cardinality bounded và protected diagnostics.

## Production Use Case

Payment unknown age quan trọng hơn chỉ HTTP5xx; migration version gaps quan trọng hơn worker CPU.

## Failure Scenarios

Dashboards chỉ infra xanh nhưng work stalled; retries counted success nhiều lần.

## How I would debug this in production

Track logical operations separately from attempts và source/target state mismatches.

## Trade-offs và When NOT to use

Telemetry có overhead/storage/privacy; sampling phải giữ incident visibility.

## Interview practice

Which metric detects silent data pipeline failure? Freshness/oldest age và reconciliation gaps, không chỉ process uptime.

## Key Takeaways

Thiết kế phải cho biết dùng metric/trace/state nào chứng minh invariant và SLO..


## See also

- [System design framework cho Senior Go](system-design-framework.md)
- [Design High-Throughput API — 20,000 RPS](design-high-throughput-api.md)
- [Design Migration Platform — 4–5 Billion Records](design-migration-platform.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)
