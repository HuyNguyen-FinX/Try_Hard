# Memory profiling: retained versus allocated

## Concept và Mental Model

Heap/inuse cho memory còn sống; alloc_space cho cumulative churn theo samples.

## How it works

go tool pprof -sample_index=inuse_space hoặc alloc_space đổi câu hỏi, không đổi workload. Forced GC có thể giúp so retained set nhưng gây overhead và thay state.

## Production Use Case

So baseline/canary cùng input và uptime; ghi build ID để symbolization đúng.

## Failure Scenarios

Nhìn alloc_space rồi kết luận leak; RSS tăng do mmap/cgo mà heap profile không giải thích.

## How I would debug this in production

Xem top, top -cum, list và caller graph; chia rate theo elapsed time/RPS.

## Trade-offs và When NOT to use

Profile sampling có sai số với allocations nhỏ; không suy exact object count từ sample đơn.

## Interview practice

Why can an allocs hotspot disappear from inuse? Object sống ngắn đã được thu hồi.

## Key Takeaways

Heap/inuse cho memory còn sống; alloc_space cho cumulative churn theo samples..


## See also

- [Garbage collection: live heap, pacing và memory budget](garbage-collector.md)
- [Escape analysis: đọc quyết định của compiler](escape-analysis.md)
- [memory-profile](../16-performance/memory-profile.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/gc-guide)
