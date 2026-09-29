# Allocation rate và allocator

## Concept và Mental Model

Allocation rate là bytes/objects tạo mỗi giây; live heap là objects còn reachable sau collection.

## How it works

Allocator phân size classes và có local caching; exact mcache/mcentral/mheap là implementation detail. Tiny objects, pointer density và zeroing ảnh hưởng chi phí.

## Production Use Case

Giảm temporary string/byte conversions trong hot serialization path sau profiling.

## Failure Scenarios

Pool giữ buffer cực lớn sau một request; benchmark không giữ result nên compiler loại work.

## How I would debug this in production

So alloc_space, alloc_objects, B/op và allocs/op; cùng RPS mới so rate.

## Trade-offs và When NOT to use

Preallocate có ích khi size biết rõ; cap buffer pooled để tránh giữ outlier.

## Interview practice

Why can low live heap coexist with high GC CPU? Allocation churn vẫn tạo collection work.

## Key Takeaways

Allocation rate là bytes/objects tạo mỗi giây; live heap là objects còn reachable sau collection..


## See also

- [Garbage collection: live heap, pacing và memory budget](garbage-collector.md)
- [Escape analysis: đọc quyết định của compiler](escape-analysis.md)
- [memory-profile](../16-performance/memory-profile.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/gc-guide)
