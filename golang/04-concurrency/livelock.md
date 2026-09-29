# Livelock và retry synchronization

## Concept và Mental Model

Livelock vẫn hoạt động nhưng không tạo progress, thường do retry/coordination lặp cùng pattern.

## How it works

Hai actors nhường nhau đồng thời hoặc CAS/retry loop lặp; khác deadlock ở chỗ CPU/counters còn tăng.

## Production Use Case

Dùng bounded retry với jitter và deadline, atomic state transition rõ.

## Failure Scenarios

TryLock loop spin dưới contention; retry ngay sau 429 khiến overload tồn tại.

## How I would debug this in production

Đo attempts/s so completions/s, CPU hot loop và retry histogram.

## Trade-offs và When NOT to use

Backoff tăng latency nhưng giảm synchronized contention; phải có stop budget.

## Interview practice

How do you distinguish livelock from deadlock? Quan sát CPU/attempt progress và completed operations.

## Key Takeaways

Livelock vẫn hoạt động nhưng không tạo progress, thường do retry/coordination lặp cùng pattern..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)

## Applied drill

Hai workers dùng TryLock, fail thì nhường rồi retry tức thì. Trong load test, ghi attempts và completions: attempts tăng mạnh nhưng completions gần0 là bằng chứng thiếu progress. Thêm bounded backoff+jitter rồi so throughput và fairness; nếu invariant chỉ cần một lock, blocking Lock thường đơn giản hơn loop tự chế. Cancel phải ngắt cả backoff để shutdown không đợi vô hạn.
