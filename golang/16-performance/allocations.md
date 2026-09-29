# Allocation optimization

## Concept và Mental Model

Allocation rate tạo allocator/GC work; tối ưu ownership và buffer sizing trước unsafe tricks.

## How it works

Preallocate measured size, reuse bounded buffers với clear owner, avoid repeated conversions; sync.Pool contents có thể bị bỏ bất kỳ GC cycle.

## Production Use Case

JSON batching giảm per-item overhead nếu latency/memory budget cho phép.

## Failure Scenarios

Pool oversized buffer giữ RAM; concurrent reuse corrupt data; global sink làm benchmark escape giả.

## How I would debug this in production

benchmem plus alloc_space và inuse_space; inspect compiler -m=2 sau xác định hotspot.

## Trade-offs và When NOT to use

Clone tăng alloc nhưng có thể giảm live heap; không tối ưu alloc count tách bytes/lifetime.

## Interview practice

Why should pooled buffers have size caps? Một outlier request có thể khiến pool giữ working set quá lớn.

## Key Takeaways

Allocation rate tạo allocator/GC work; tối ưu ownership và buffer sizing trước unsafe tricks..


## See also

- [pprof: chọn profile từ câu hỏi production](pprof.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)
