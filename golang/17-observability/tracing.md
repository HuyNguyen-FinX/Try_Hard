# Tracing và critical path

## Concept và Mental Model

Trace nối spans của logical operation; elapsed request time chịu critical path và overlap.

## How it works

Propagate context qua HTTP/gRPC; async messaging dùng link/parent model theo instrumentation. Span attributes phải useful/bounded, redact payloads.

## Production Use Case

Checkout trace phân biệt pool wait, DB execution và provider latency.

## Failure Scenarios

Spans missing do context.Background; sampling bỏ failure; clocks lệch.

## How I would debug this in production

Pivot từ slow/error cohort; đối chiếu parent-child durations và queue stages chưa instrument.

## Trade-offs và When NOT to use

Trace samples không thay rate metrics; sampling policy cân cost với incident visibility.

## Interview practice

Why can sum of span durations exceed request latency? Concurrent spans overlap.

## Key Takeaways

Trace nối spans của logical operation; elapsed request time chịu critical path và overlap..


## See also

- [pprof: chọn profile từ câu hỏi production](../16-performance/pprof.md)
- [service-outage](../20-production-scenarios/service-outage.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://opentelemetry.io/docs/concepts/observability-primer/)

## Applied drill

Request fan-out3 calls chạy song song mỗi call100ms có tổng span duration300ms nhưng critical path khoảng100ms cộng overhead. Nếu API duration500ms, tìm queue/admission/uninstrumented gaps hoặc sequential stages. Tail sampling có thể giữ error traces nhưng collector vẫn cần bounded state. Không dùng trace sampling ratio để suy exact error rate; metrics trả lời rate.
