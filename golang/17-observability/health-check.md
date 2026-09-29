# Health checks: liveness, readiness, startup

## Concept và Mental Model

Liveness hỏi process có tiến triển không; readiness hỏi có nên nhận traffic; startup bảo vệ slow initialization.

## How it works

Readiness bounded/lightweight; avoid making liveness depend on shared DB. Health endpoint không trả secrets/config.

## Production Use Case

Readiness false khi drain; startup probe cho migration/init policy có deadline.

## Failure Scenarios

DB outage làm mọi pods fail liveness rồi restart storm; probe timeout quá ngắn lúc CPU throttle.

## How I would debug this in production

Correlate probe failures/restarts và real request SLO; xem rollout timing.

## Trade-offs và When NOT to use

Readiness toàn bộ dependency fail có thể remove mọi pod; decide degraded service policy.

## Interview practice

Why should liveness not usually query the DB? Restart app không chữa shared DB outage.

## Key Takeaways

Liveness hỏi process có tiến triển không; readiness hỏi có nên nhận traffic; startup bảo vệ slow initialization..


## See also

- [pprof: chọn profile từ câu hỏi production](../16-performance/pprof.md)
- [service-outage](../20-production-scenarios/service-outage.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://opentelemetry.io/docs/concepts/observability-primer/)
