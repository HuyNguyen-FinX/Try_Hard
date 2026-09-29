# SLI, SLO, SLA và error budget

## Concept và Mental Model

SLI đo outcome; SLO là target nội bộ theo window; SLA là cam kết hợp đồng với consequences.

## How it works

Define eligible events, good events và window. Availability với timeout/5xx accounting; latency SLO phải nêu percentile hoặc fraction dưới threshold.

## Production Use Case

99.9% monthly availability cho endpoint critical có error budget khoảng 0.1% eligible events.

## Failure Scenarios

Loại timeout khỏi denominator; average latency dưới target nhưng P99 tệ; alert mọi CPU spike thay user impact.

## How I would debug this in production

Burn-rate alerts nhiều windows và dependency diagnostics; validate measurement tại edge.

## Trade-offs và When NOT to use

Không hứa 100% khi cost/architecture không cho; SLO dẫn trade-offs release/reliability.

## Interview practice

What does a fast error do to latency-only SLO? Có thể trông tốt dù user failure, cần availability SLI riêng.

## Key Takeaways

SLI đo outcome; SLO là target nội bộ theo window; SLA là cam kết hợp đồng với consequences..


## See also

- [pprof: chọn profile từ câu hỏi production](../16-performance/pprof.md)
- [service-outage](../20-production-scenarios/service-outage.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://opentelemetry.io/docs/concepts/observability-primer/)
