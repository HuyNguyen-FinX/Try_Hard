# Performance debugging workflow

## Concept và Mental Model

Bắt đầu từ regression trong user-visible latency/throughput, rồi phân loại CPU, wait, memory hoặc dependency.

## How it works

Check traffic/build/config; correlate RED metrics, pool waits, runtime metrics và profiles. Separate mean/P99 và per-route distributions.

## Production Use Case

20k RPS target: run stepped offered load, saturation knee và recovery after overload.

## Failure Scenarios

Closed-loop generator giảm load khi service chậm che queue growth; coordinated omission.

## How I would debug this in production

Use independent arrival scheduling khi phù hợp, report offered/accepted/completed rates và timeout accounting.

## Trade-offs và When NOT to use

Load test có realistic data/cardinality/security work; hello-world không đại diện.

## Interview practice

Why can reported P99 look good while clients time out? Dropped/timed-out samples có thể bị loại khỏi histogram.

## Key Takeaways

Bắt đầu từ regression trong user-visible latency/throughput, rồi phân loại CPU, wait, memory hoặc dependency..


## See also

- [pprof: chọn profile từ câu hỏi production](pprof.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)

## Applied drill

Load gate phải bao accepted, rejected và timed-out operations. Generator closed-loop chỉ gửi request mới sau response sẽ giảm offered load khi service chậm; histogram có thể che queueing user thật gặp. Với open-loop schedule, report missed scheduling/overload ở generator để không nhầm client bottleneck thành server ceiling. Sau overload, verify queue drain và memory plateau.
