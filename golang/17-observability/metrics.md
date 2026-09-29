# Metrics: counters, gauges và histograms

## Concept và Mental Model

Metric tập hợp numeric signals có cardinality bound để quan sát rates và distributions.

## How it works

Counter dùng rate/increase, gauge cho current state, histogram cho latency buckets; label route template không user/request ID.

## Production Use Case

RED: rate/errors/duration; USE: utilization/saturation/errors cho pools/CPU.

## Failure Scenarios

Average latency che tail; counter reset bị coi traffic giảm; label explosion OOM metrics backend.

## How I would debug this in production

Inspect series count, bucket coverage và scrape lag; compare offered versus completed requests.

## Trade-offs và When NOT to use

Không aggregate percentiles bằng average P99; merge histogram distributions đúng cách.

## Interview practice

Why cannot you average pod P99 values into fleet P99? Quantiles không tuyến tính.

## Key Takeaways

Metric tập hợp numeric signals có cardinality bound để quan sát rates và distributions..


## See also

- [pprof: chọn profile từ câu hỏi production](../16-performance/pprof.md)
- [service-outage](../20-production-scenarios/service-outage.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://opentelemetry.io/docs/concepts/observability-primer/)

## Applied drill

Giả sử một pod có100 requests và P99=1s, pod khác có10k requests P99=50ms: average525ms không là fleet P99. Aggregate histogram buckets/counts theo time window rồi tính quantile/fraction. Include timeout/reject events theo eligible definition; nếu chỉ observe successful requests, latency dashboard có thể xanh ngay khi phần lớn users fail.

## Runtime metrics example

Chương trình độc lập dùng public `runtime/metrics`; xem descriptions từ `metrics.All()` trên toolchain deploy để biết loại và units. Không coi mọi metric là gauge: heap alloc bytes và GC cycles là cumulative counters, goroutine count/live heap là snapshots.

```go
package main
import (
    "fmt"
    "runtime/metrics"
)
func main() {
    names := []string{
        "/sched/goroutines:goroutines",
        "/gc/heap/allocs:bytes",
        "/gc/heap/live:bytes",
        "/gc/cycles/total:gc-cycles",
    }
    samples := make([]metrics.Sample, len(names))
    for i, name := range names { samples[i].Name = name }
    metrics.Read(samples)
    for _, sample := range samples {
        if sample.Value.Kind() != metrics.KindUint64 {
            fmt.Printf("%s: unavailable or different kind\n", sample.Name)
            continue
        }
        fmt.Printf("%s=%d\n", sample.Name, sample.Value.Uint64())
    }
}
```

Lấy deltas alloc bytes/cycles giữa hai thời điểm và chia elapsed seconds, xử lý process restart/reset. `/sched/latencies:seconds` là histogram, không được đọc bằng Uint64; đọc Float64Histogram và interpret bucket counts theo contract. Scheduler latency khác HTTP latency: cần correlate với request traces/queue metrics để suy nguyên nhân. [Runtime metric descriptions](https://pkg.go.dev/runtime/metrics).
