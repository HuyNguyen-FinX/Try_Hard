# Structured logging có context

## Concept và Mental Model

Log là event evidence có time, severity, operation và correlation; không thay metrics cho rates.

## How it works

Dùng log/slog với fields bounded, errors một lần ở boundary; redact secrets/PII, sampling noisy events và backpressure cho exporter.

## Production Use Case

Log operation_id, route template, outcome và dependency name để pivot trace.

## Failure Scenarios

Log mỗi retry/layer gây noise; sync logging I/O làm latency; token xuất raw.

## How I would debug this in production

Check dropped log counts, ingestion lag và repeated errors cùng logical request.

## Trade-offs và When NOT to use

Debug detail có cost/security; enable targeted sampling có thời hạn.

## Interview practice

Where should an error be logged? Boundary có đủ context và trách nhiệm xử lý cuối.

## Key Takeaways

Log là event evidence có time, severity, operation và correlation; không thay metrics cho rates..


## See also

- [pprof: chọn profile từ câu hỏi production](../16-performance/pprof.md)
- [service-outage](../20-production-scenarios/service-outage.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://opentelemetry.io/docs/concepts/observability-primer/)

## Applied drill

Một request retry3 lần có operation_id cố định và attempt index khác nhau. Log error cuối tại owning boundary; intermediate retries ở sampled debug/info theo policy để tránh noise. Slog fields dùng route template và dependency name, không dump headers/context. Khi log sink chậm, bounded async queue/drop policy phải bảo vệ request path và expose dropped count.
