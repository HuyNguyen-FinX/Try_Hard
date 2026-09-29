# Backpressure: 10k vào, 5k ra

## Concept và Mental Model

Khi arrival 10k/s và completion 5k/s, backlog tăng 5k/s; queue hữu hạn chỉ mua thời gian.

## How it works

Với payload 2KiB, thêm khoảng 9.8MiB/s trước overhead. Bound queue count/bytes, producer admission, consumer in-flight và retries. Scale chỉ khi sink còn headroom và partitions cho phép.

## Production Use Case

API reject 429/503 khi vượt latency budget; broker durable giữ work với retention và oldest-age SLO.

## Failure Scenarios

Unbounded Go channels qua wrapper/list; spawn one G mỗi queued task; scale consumers làm target DB chậm hơn.

## How I would debug this in production

Đo rates, lag derivative, oldest age, queue bytes, active workers và DB wait; recovery phải có service rate > arrival.

## Trade-offs và When NOT to use

Drop phù hợp telemetry best-effort, không money; load shedding cần product contract.

## Interview practice

How long does a 10000-item queue take to fill from empty? Khoảng 2s với net growth 5000/s, giả sử rates ổn định.

## Key Takeaways

Khi arrival 10k/s và completion 5k/s, backlog tăng 5k/s; queue hữu hạn chỉ mua thời gian..


## See also

- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kafka.apache.org/41/design/design/)
