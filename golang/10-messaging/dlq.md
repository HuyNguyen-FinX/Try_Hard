# Dead-letter queue như workflow vận hành

## Concept và Mental Model

DLQ giữ record không xử lý được cùng failure context để inspect/fix/replay.

## How it works

Store original ID/payload schema/version, reason, attempts, first/last failure và source position; redact secrets và bound payload. Replay phải giữ idempotency identity.

## Production Use Case

Schema mismatch quarantine rồi deploy converter và replay canary nhỏ trước batch.

## Failure Scenarios

DLQ không có owner/alert thành data loss im lặng; replay toàn bộ gây overload/duplicate.

## How I would debug this in production

Age/count by reason, sample payload safely, reconcile source to final effects.

## Trade-offs và When NOT to use

DLQ tránh block stream nhưng không tự chữa dữ liệu; có retention và runbook.

## Interview practice

What makes DLQ replay safe? Stable event IDs, schema handling, bounded rate và idempotent sink.

## Key Takeaways

DLQ giữ record không xử lý được cùng failure context để inspect/fix/replay..


## See also

- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kafka.apache.org/41/design/design/)

## Applied drill

Replay drill: lấy10 records cùng một schema error, deploy transform fix, replay giữ original event ID và source metadata. Verify business effect count đúng, original DLQ item được đánh dấu resolved sau durable completion. Scale replay rate từ nhỏ; nếu dùng ID mới sẽ không kiểm chứng idempotency của original workflow. Dashboard phải có oldest unresolved age, không chỉ count.
