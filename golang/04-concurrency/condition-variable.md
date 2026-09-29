# Condition variable và predicate

## Concept và Mental Model

sync.Cond chờ predicate của shared state dưới lock, không giữ lịch sử events như queue.

## How it works

Lock, kiểm tra predicate trong for, Wait atomically unlock/park rồi reacquire trước return. Signal wake một waiter; Broadcast wake tất cả để họ kiểm tra lại predicate.

## Production Use Case

Bounded resource manager có điều kiện phức tạp mà channel không biểu diễn dễ.

## Failure Scenarios

Signal trước waiter nhưng predicate không được lưu gây lost notification; dùng if thay for sai khi waiter khác lấy resource trước.

## How I would debug this in production

Vẽ predicate transitions dưới cùng lock và waiters; test multiple consumers.

## Trade-offs và When NOT to use

Không có direct context select với Cond; channel thường dễ lifecycle hơn.

## Interview practice

Why is a predicate loop necessary? Wake không đồng nghĩa resource vẫn còn khi reacquire.

## Key Takeaways

sync.Cond chờ predicate của shared state dưới lock, không giữ lịch sử events như queue..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)
