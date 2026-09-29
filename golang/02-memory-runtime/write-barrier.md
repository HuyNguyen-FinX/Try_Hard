# Write barrier và concurrent marking

## Concept và Mental Model

Write barrier giúp GC theo dõi pointer mutations trong concurrent mark, không phải mutex cho application.

## How it works

Tri-color reasoning: nếu graph đổi lúc scan, barrier duy trì invariant cần thiết để object reachable không bị bỏ sót. Exact hybrid barrier phụ thuộc runtime version.

## Production Use Case

Pointer-rich cache churn có thể tăng GC work; value arrays ít pointers có scan cost khác.

## Failure Scenarios

Bỏ synchronization vì tưởng barrier bảo vệ dữ liệu tạo race; unsafe pointer manipulation phá assumptions.

## How I would debug this in production

CPU profile tìm GC/barrier-related work, xem pointer density và allocation rate trước khi sửa layout.

## Trade-offs và When NOT to use

Không tự tắt barrier; giảm churn và đo representation khi memory profile chỉ ra bottleneck.

## Interview practice

How can the graph change during marking? Mutator viết pointer trong lúc collector scan graph.

## Key Takeaways

Write barrier giúp GC theo dõi pointer mutations trong concurrent mark, không phải mutex cho application..


## See also

- [Garbage collection: live heap, pacing và memory budget](garbage-collector.md)
- [Escape analysis: đọc quyết định của compiler](escape-analysis.md)
- [memory-profile](../16-performance/memory-profile.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/gc-guide)
