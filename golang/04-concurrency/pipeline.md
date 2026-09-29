# Pipeline: ownership ở từng stage

## Concept và Mental Model

Pipeline nối các stage bằng channels; mỗi output có owner close và mỗi blocking point có cancellation.

## How it works

Stage đọc đến input closed hoặc ctx done; send output cũng select ctx. Coordinator cancel rồi join toàn pipeline khi downstream dừng.

## Production Use Case

File processing decode-transform-write với stage concurrency theo CPU và target DB capacity.

## Failure Scenarios

Stage cuối bỏ đọc khiến mọi upstream kẹt send; chỉ cancel receive nhưng send không cancelable.

## How I would debug this in production

Goroutine profile group theo stage, queue age per edge và check close owner.

## Trade-offs và When NOT to use

Buffer giúp burst cục bộ nhưng tăng retained payloads; pipeline chỉ đáng khi stage overlap có lợi.

## Interview practice

What happens when the last stage returns early? Upstream cần cancel để thoát send và được join.

## Key Takeaways

Pipeline nối các stage bằng channels; mỗi output có owner close và mỗi blocking point có cancellation..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)
