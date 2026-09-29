# Preemption và safe points

## Concept và Mental Model

Preemption cho scheduler cơ hội chạy G khác khi một G dùng CPU lâu.

## How it works

Cooperative safe points và asynchronous mechanisms phụ thuộc architecture/runtime. STW, stack scan và unsafe runtime regions có ràng buộc riêng.

## Production Use Case

CPU-heavy parsing cần bound payload và concurrency, không dựa vào preemption để có deadline cứng.

## Failure Scenarios

Vòng default-select spin dùng toàn core; cancel context không được kiểm tra trong tight compute loop.

## How I would debug this in production

CPU profile tìm loop; execution trace xem runnable latency, GC pauses và quota throttling.

## Trade-offs và When NOT to use

Chia compute thành chunks để kiểm tra cancel nhưng đo overhead; runtime không phải real-time scheduler.

## Interview practice

Can preemption guarantee a 10ms response deadline? Không, OS scheduling/quota và downstream vẫn quyết định.

## Key Takeaways

Preemption cho scheduler cơ hội chạy G khác khi một G dùng CPU lâu..


## See also

- [Go scheduler: G, M, P và các đường blocking](scheduler-gmp.md)
- [trace](../16-performance/trace.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://github.com/golang/go/blob/go1.26.4/src/runtime/proc.go)
