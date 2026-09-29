# Execution trace: timeline scheduling

## Concept và Mental Model

Trace cho lịch G, network/syscall blocking, GC và runtime events theo thời gian.

## How it works

go test -trace trace.out rồi go tool trace; inspect runnable delay, processor utilization và task regions. Runtime trace APIs có thể annotate business task với context.

## Production Use Case

Latency burst dù mean CPU thấp: tìm runnable queue sau quota throttling hoặc fan-out wake storm.

## Failure Scenarios

Trace quá dài phình storage/overhead; chỉ nhìn timeline không correlate request IDs.

## How I would debug this in production

Chọn cửa sổ ngắn bao regression; compare scheduler delay với dependency spans.

## Trade-offs và When NOT to use

Profile tốt cho aggregate hotspots, trace tốt cho causality/timing; dùng cả khi cần.

## Interview practice

What differs between runnable and running latency? G có thể sẵn sàng nhưng chưa được M/P execute.

## Key Takeaways

Trace cho lịch G, network/syscall blocking, GC và runtime events theo thời gian..


## See also

- [pprof: chọn profile từ câu hỏi production](pprof.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)
