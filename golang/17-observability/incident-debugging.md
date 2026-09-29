# Incident debugging với evidence

## Concept và Mental Model

Incident response ưu tiên giảm impact rồi tìm cause bằng timeline có thể kiểm chứng.

## How it works

Assess scope/SLO, recent changes, dependencies; choose reversible mitigation; snapshot profiles/logs trước restart khi không trì hoãn recovery.

## Production Use Case

Rollback regression đã correlate, shed optional traffic, pause backfill đang chiếm DB.

## Failure Scenarios

Thay nhiều configs cùng lúc mất causal signal; restart toàn fleet che evidence và tạo cold-cache storm.

## How I would debug this in production

Track hypothesis, evidence for/against, action/time/outcome; aftercare verify recovery và backlog.

## Trade-offs và When NOT to use

Mitigation không là root-cause fix; postmortem cần owner và measurable prevention.

## Interview practice

How do you choose between rollback and deeper debugging? User impact, change correlation và reversibility quyết định.

## Key Takeaways

Incident response ưu tiên giảm impact rồi tìm cause bằng timeline có thể kiểm chứng..


## See also

- [pprof: chọn profile từ câu hỏi production](../16-performance/pprof.md)
- [service-outage](../20-production-scenarios/service-outage.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://opentelemetry.io/docs/concepts/observability-primer/)

## Applied drill

Tạo incident note gồm timestamp, hypothesis, evidence, action, owner và expected outcome. Ví dụ “pool wait tăng sau backfill” cần DB hold-time/active-session evidence; pause backfill là reversible experiment. Nếu latency không giảm, bác bỏ hoặc chỉnh hypothesis thay tiếp tục tăng pool theo cảm tính. Recovery note phải ghi remaining data reconciliation/backlog, không chỉ process health.
