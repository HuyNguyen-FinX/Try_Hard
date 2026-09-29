# sync.Map versus typed map

## Concept và Mental Model

sync.Map tối ưu một số concurrent-key workloads; native map + lock thường dễ giữ type/invariant hơn.

## How it works

Dùng LoadOrStore cho atomic initialization, nhưng compute argument trước call vẫn có thể chạy nhiều lần. Range không phải consistent snapshot. Internals thay đổi theo Go release, không dựa mô hình read/dirty cũ như luật.

## Production Use Case

Registry write-once/read-many hoặc independent-key state sau benchmark.

## Failure Scenarios

Load rồi Store tạo lost update; values chứa pointer vẫn race; Range bị dùng làm transactional snapshot.

## How I would debug this in production

Đo hit rate/churn/contention; test compound operations và use-after-delete logic.

## Trade-offs và When NOT to use

Không chọn sync.Map cho invariant nhiều keys hoặc khi cần type safety đơn giản.

## Interview practice

Does LoadOrStore guarantee an expensive constructor runs once? Không nếu constructor được evaluate trước call.

## Key Takeaways

sync.Map tối ưu một số concurrent-key workloads; native map + lock thường dễ giữ type/invariant hơn..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)
