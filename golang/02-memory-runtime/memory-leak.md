# Memory leak trong ngôn ngữ có GC

## Concept và Mental Model

Leak thường là reference vẫn reachable nhưng không còn business value: cache, slice, closure hoặc goroutine bị quên.

## How it works

GC không biết entry cache đã hết ý nghĩa. Heap profile cho allocation site, không trực tiếp cho mọi retaining path như một object graph debugger.

## Production Use Case

Cache có max entries/bytes, TTL và eviction; worker queue có bound trên cả count và payload size.

## Failure Scenarios

Ticker worker giữ ctx cũ; giant array qua sub-slice; metrics label theo request ID giữ state vô hạn.

## How I would debug this in production

Lấy profiles cùng tải cách nhau nhiều phút, so inuse_space và inuse_objects; đối chiếu goroutine count/cardinality.

## Trade-offs và When NOT to use

TTL đơn thuần không bound burst memory; thêm size limit và admission.

## Interview practice

How would you distinguish a leak from healthy cache warming? Live set có đạt plateau sau workload ổn định và eviction không.

## Key Takeaways

Leak thường là reference vẫn reachable nhưng không còn business value: cache, slice, closure hoặc goroutine bị quên..


## See also

- [Garbage collection: live heap, pacing và memory budget](garbage-collector.md)
- [Escape analysis: đọc quyết định của compiler](escape-analysis.md)
- [memory-profile](../16-performance/memory-profile.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/gc-guide)
