# Atomics và immutable publication

## Concept và Mental Model

Atomic operations phù hợp counters và state transition nhỏ; chúng không tự tạo transaction trên nhiều fields.

## How it works

Dùng typed atomic.Int64/Pointer; CAS cần loop khi update phụ thuộc current state. Sau publish pointer, snapshot phải immutable cả nested maps/slices.

## Production Use Case

Publish routing snapshot mới và giữ readers không lock.

## Failure Scenarios

Atomic pointer nhưng mutate object phía sau; CAS retry loop spin khi contention; copy atomic value sau use.

## How I would debug this in production

Race test nested state, đo failed CAS và CPU; kiểm tra invariant chứ không chỉ data race.

## Trade-offs và When NOT to use

Mutex đơn giản hơn nếu state nhiều field hoặc update phức tạp.

## Interview practice

Can atomic pointers make a mutable map safe? Không, chỉ pointer access là atomic.

## Key Takeaways

Atomic operations phù hợp counters và state transition nhỏ; chúng không tự tạo transaction trên nhiều fields..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)
