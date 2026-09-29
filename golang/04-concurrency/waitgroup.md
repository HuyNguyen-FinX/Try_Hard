# WaitGroup: join và lifecycle

## Concept và Mental Model

WaitGroup đếm tasks chưa hoàn tất, không truyền results hoặc errors.

## How it works

Add trước launch để tránh Wait thấy zero quá sớm; worker defer Done. Không copy sau use; reuse chỉ khi lần Wait trước đã return. Go 1.25 thêm WaitGroup.Go với contract riêng về panic.

## Production Use Case

Coordinator đợi producers xong rồi close output; error propagation qua channel/context hoặc errgroup có bound.

## Failure Scenarios

Add trong child race với Wait; thiếu Done khiến shutdown treo; negative counter panic.

## How I would debug this in production

Dùng done signal và timeout trong test; xem stack Wait cùng worker còn blocked.

## Trade-offs và When NOT to use

WaitGroup cho join đơn giản; errgroup hữu ích khi cần error/cancel nhưng dependency có version.

## Interview practice

Why must Add precede go? Parent có thể Wait trước child được schedule.

## Key Takeaways

WaitGroup đếm tasks chưa hoàn tất, không truyền results hoặc errors..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)
