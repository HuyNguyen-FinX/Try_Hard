# RWMutex và writer latency

## Concept và Mental Model

RWMutex cho nhiều readers hoặc một writer; mọi write vẫn cần exclusive Lock.

## How it works

Writer chờ sẽ chặn new readers để có cơ hội tiến triển. Không upgrade RLock sang Lock hoặc recursive read lock khi writer chờ.

## Production Use Case

Read-heavy registry với read work đủ lớn có thể hưởng lợi; benchmark với Mutex.

## Failure Scenarios

Read lock giữ trong I/O khiến writer chờ lâu; RLock rồi Lock cùng G deadlock.

## How I would debug this in production

Đo read/write ratio, hold duration, mutex profile và writer P99.

## Trade-offs và When NOT to use

Tiny reads có thể không bù bookkeeping; không dùng vì chỉ thấy workload có nhiều reads.

## Interview practice

Why can read-lock recursion deadlock? Pending writer ngăn read lock mới tiến triển.

## Key Takeaways

RWMutex cho nhiều readers hoặc một writer; mọi write vẫn cần exclusive Lock..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)
