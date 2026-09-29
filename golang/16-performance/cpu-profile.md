# CPU profile: execution cost

## Concept và Mental Model

CPU samples cho execution đang tiêu CPU, không toàn request wall time.

## How it works

top tìm flat cost; top -cum và list tìm callers/lines; look for JSON, regex, compression, busy loops, GC assist.

## Production Use Case

Capture 30s khi CPU95%, RPS normal và latency cao, giữ deployment build ID.

## Failure Scenarios

Chỉ nhìn runtime.mallocgc mà bỏ caller tạo allocations; CPU throttle khiến wall time tăng nhưng profile không toàn bức tranh.

## How I would debug this in production

Correlate profile với CPU quota/throttled time và offered load.

## Trade-offs và When NOT to use

Không tối ưu cold functions vì graph trông lớn; quantify percent contribution.

## Interview practice

Why does a hot allocator frame point back to application design? Callers tạo churn mới là nơi giảm work.

## Key Takeaways

CPU samples cho execution đang tiêu CPU, không toàn request wall time..


## See also

- [pprof: chọn profile từ câu hỏi production](pprof.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)
