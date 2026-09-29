# Optimization theo bottleneck

## Concept và Mental Model

Tối ưu phải cải thiện mục tiêu đo được trong constraints correctness/memory/latency.

## How it works

Baseline, profile, hypothesis, one change, benchmark, production canary. Amdahl: tối ưu 10% cost có giới hạn lợi ích toàn hệ thống.

## Production Use Case

Giảm N+1/pool churn trước viết custom allocator.

## Failure Scenarios

Microbench nhanh nhưng memory retention cao; sync.Pool gây data race do trả buffer sớm.

## How I would debug this in production

Compare same load/hardware and confidence; rollback khi error/P99 xấu dù ns/op tốt.

## Trade-offs và When NOT to use

Complexity cần lợi ích đáng giữ; ưu tiên giảm work trước tune machinery.

## Interview practice

How would you reject an attractive optimization? Không cải thiện measured bottleneck hoặc phá ownership/maintainability.

## Key Takeaways

Tối ưu phải cải thiện mục tiêu đo được trong constraints correctness/memory/latency..


## See also

- [pprof: chọn profile từ câu hỏi production](pprof.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)

## Applied drill

Giả sử CPU profile40% JSON,10% compression,50% khác: tối ưu compression2× chỉ cải thiện tổng time lý tưởng khoảng5%, không2× toàn API. Nếu DB wait chiếm wall latency lớn, CPU savings có thể không đổi P99 nhưng giảm cost. Ghi mục tiêu rõ: latency, throughput/core hay memory; tránh dùng một benchmark metric thay cho tất cả.
