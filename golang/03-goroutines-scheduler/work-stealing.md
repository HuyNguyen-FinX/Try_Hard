# Work stealing và locality

## Concept và Mental Model

P thiếu work tìm runnable G từ P khác để dùng CPU còn rảnh.

## How it works

Local queues giảm global contention; stealing lấy batch để giảm synchronization cost. Exact victim selection và batch size phụ thuộc release.

## Production Use Case

Fan-out CPU batch được chia giữa P, nhưng task cực dài vẫn làm tail latency cao.

## Failure Scenarios

Một task giữ lock toàn cục khiến nhiều P rảnh; stealing không tạo parallelism qua serialized critical section.

## How I would debug this in production

Trace runnable delay, CPU utilization và mutex profile; xem task size skew.

## Trade-offs và When NOT to use

Chia task nhỏ giúp cân bằng nhưng quá nhỏ tăng schedule overhead; không tự tune runtime queues.

## Interview practice

Can work stealing fix lock contention? Không, waiter chưa runnable cho đến khi invariant được mở khóa.

## Key Takeaways

P thiếu work tìm runnable G từ P khác để dùng CPU còn rảnh..


## See also

- [Go scheduler: G, M, P và các đường blocking](scheduler-gmp.md)
- [trace](../16-performance/trace.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://github.com/golang/go/blob/go1.26.4/src/runtime/proc.go)
