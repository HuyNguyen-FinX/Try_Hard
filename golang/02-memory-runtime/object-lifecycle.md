# Object lifecycle và resource ownership

## Concept và Mental Model

Object lifetime kết thúc khi không reachable; resource lifetime kết thúc khi owner Close/Stop đúng protocol.

## How it works

Channel/closure/cache có thể kéo dài object life vượt stack frame. Finalizer timing không phù hợp để release connection cần prompt cleanup.

## Production Use Case

DB rows close ở scope đọc; HTTP response body close ngay sau consume; worker cancel rồi join.

## Failure Scenarios

Unclosed rows giữ pool slot dù object cuối cùng có thể được GC; cancellation không được awaited.

## How I would debug this in production

Lập bảng acquire-owner-release cho request; profile references và theo dõi FD/pool metrics.

## Trade-offs và When NOT to use

Explicit cleanup dài hơn chút nhưng deterministic; không dựa GC để giữ SLO tài nguyên.

## Interview practice

Why is GC insufficient for connection lifecycle? Capacity cần release đúng lúc, không chờ collection.

## Key Takeaways

Object lifetime kết thúc khi không reachable; resource lifetime kết thúc khi owner Close/Stop đúng protocol..


## See also

- [Garbage collection: live heap, pacing và memory budget](garbage-collector.md)
- [Escape analysis: đọc quyết định của compiler](escape-analysis.md)
- [memory-profile](../16-performance/memory-profile.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/gc-guide)
