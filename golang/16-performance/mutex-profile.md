# Mutex profile

## Concept và Mental Model

Mutex profile đo contention cost theo sampled lock-holder release paths, không chỉ nơi waiter gọi Lock.

## How it works

Enable runtime.SetMutexProfileFraction với budget; inspect cumulative wait contribution và critical section callers.

## Production Use Case

Cache LRU global lock giữ trong serialization tạo tail latency.

## Failure Scenarios

Hiểu aggregate waiter time như wall duration một request; profile disabled nên empty bị hiểu là không contention.

## How I would debug this in production

So mutex với block profile/trace và hold-time instrumentation có bounded cardinality.

## Trade-offs và When NOT to use

Sampling giảm overhead nhưng có noise; không bật tối đa vô thời hạn.

## Interview practice

Why can contention time exceed capture wall time? Nhiều waiters chờ đồng thời được cộng lại.

## Key Takeaways

Mutex profile đo contention cost theo sampled lock-holder release paths, không chỉ nơi waiter gọi Lock..


## See also

- [pprof: chọn profile từ câu hỏi production](pprof.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)

## Applied drill

Capture test/load có contention thực bằng `go test -mutexprofile=mutex.out`, rồi inspect `top -cum` và `list` vùng critical section. Empty profile từ test không tranh lock không chứng minh production không contention. Đặt giả thuyết “serialization dưới lock” rồi move copy/snapshot ngoài lock nếu invariant cho phép; compare writer P99 và race results.
