# Ordering và contiguous commit

## Concept và Mental Model

Broker order không bảo đảm side-effect completion order khi consumer chạy parallel.

## How it works

Offsets 10,11,12: nếu 12 xong trước 10, không commit tiến qua 10 chưa xong. Commit offset biểu thị next record theo client/protocol contract; track contiguous completed prefix.

## Production Use Case

Per-key sequencing trong worker shard, version guard ở target để reject stale writes.

## Failure Scenarios

Out-of-order DB upsert đè record mới bằng cũ; commit high watermark mất work khi crash.

## How I would debug this in production

Log partition/offset/entity version, kiểm tra checkpoint algorithm và replay tests.

## Trade-offs và When NOT to use

Strict order giảm parallelism; chỉ giữ order đúng scope business.

## Interview practice

Can a parallel consumer preserve Kafka order automatically? Không, cần sequencing hoặc versioned state transitions.

## Key Takeaways

Broker order không bảo đảm side-effect completion order khi consumer chạy parallel..


## See also

- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kafka.apache.org/41/design/design/)

## Applied drill

Cho offsets100,101,102 chạy parallel, ép101 chậm. Dù102 xong, next committed offset chỉ được tiến tới101 khi100 complete; sau101 complete mới có thể tới103 nếu102 đã xong. Nếu client API dùng record offset thay next-offset, tuân API mapping rõ. Test restart ở mỗi bước để chứng minh không skip101. Per-key state version guard bổ sung chống reordered effects.
