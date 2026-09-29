# Fan-in và fan-out

## Concept và Mental Model

Fan-out phân work nhiều workers; fan-in hợp outputs và đóng output khi mọi producer kết thúc.

## How it works

Một coordinator Wait rồi close, không từng worker tự close shared output. Order không tự giữ sau parallel execution; gắn sequence khi cần reorder bounded.

## Production Use Case

Fetch nhiều independent resources với per-request fan-out limit và global dependency limit.

## Failure Scenarios

100 calls mỗi request nhân 1000 requests tạo 100k operations; reorder buffer bị giữ bởi một slow item.

## How I would debug this in production

Đo fan-out width, aggregate deadline, slowest branch và output wait.

## Trade-offs và When NOT to use

Parallel giảm latency nhưng tăng downstream load và failure surface; batch API có thể tốt hơn.

## Interview practice

How do you preserve order under bounded fan-out? Sequence IDs và bounded reassembly, hoặc partition tuần tự.

## Key Takeaways

Fan-out phân work nhiều workers; fan-in hợp outputs và đóng output khi mọi producer kết thúc..


## See also

- [Channel internals và synchronization](channels.md)
- [Mutex: invariants, contention và lock ownership](mutex.md)
- [cancellation](../05-context/cancellation.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/sync)
