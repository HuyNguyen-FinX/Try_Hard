# OpenTelemetry instrumentation lifecycle

## Concept và Mental Model

OTel chuẩn hóa API/SDK/export để tránh binding app vào một backend; collector có lifecycle/buffer riêng.

## How it works

Set service.name/version, propagate trace context, configure sampler/batch limits và bounded Shutdown flush. Avoid duplicate auto+manual spans.

## Production Use Case

Exporter outage không được block critical requests vô hạn; bounded queue drops có metrics.

## Failure Scenarios

High-cardinality attributes, resource labels thay mỗi request, forgotten flush mất final spans.

## How I would debug this in production

Collector queue/retry/drop metrics, sampling decisions và context propagation tests.

## Trade-offs và When NOT to use

Instrumentation có overhead; measure representative workload trước bật tất cả spans.

## Interview practice

What happens when the telemetry backend is down? App cần bounded exporter policy và visibility dropped data.

## Key Takeaways

OTel chuẩn hóa API/SDK/export để tránh binding app vào một backend; collector có lifecycle/buffer riêng..


## See also

- [pprof: chọn profile từ câu hỏi production](../16-performance/pprof.md)
- [service-outage](../20-production-scenarios/service-outage.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://opentelemetry.io/docs/concepts/observability-primer/)

## Applied drill

Khởi tạo provider/exporter ở startup owner; propagate context qua HTTP clients bằng instrumentation phù hợp version. Shutdown flush với fresh bounded context sau workers dừng tạo spans. Test exporter unavailable: queue memory không tăng vô hạn, request latency không phụ thuộc exporter network và drop counters tăng có alert. Không emit raw SQL parameters hoặc auth tokens trong span attributes.
