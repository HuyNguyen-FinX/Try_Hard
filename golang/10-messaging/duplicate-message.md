# Duplicate delivery không đồng nghĩa producer bug

## Concept và Mental Model

Producer retries, consumer crash/rebalance và network ambiguity đều có thể tạo duplicates.

## How it works

Theo dõi message ID, business operation ID và delivery attempt riêng. Kafka idempotent producer giảm duplicates trong phạm vi protocol, không dedup arbitrary business replay.

## Production Use Case

Notification dedup theo user/template/event; payment dedup theo stable operation key.

## Failure Scenarios

Gắn ID mới mỗi retry; dedup TTL ngắn hơn backlog; duplicate đang in-flight đồng thời.

## How I would debug this in production

Correlate IDs/offsets/commit timestamps, kiểm tra unique constraint và retention.

## Trade-offs và When NOT to use

Không hứa exactly-once end-to-end khi external effect không nằm trong transaction.

## Interview practice

How would you distinguish duplicate delivery from duplicate business intent? Identity scope và contract tạo ID phải rõ.

## Key Takeaways

Producer retries, consumer crash/rebalance và network ambiguity đều có thể tạo duplicates..


## See also

- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)
- [Worker pool và bounded concurrency](../04-concurrency/worker-pool.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kafka.apache.org/41/design/design/)

## Applied drill

Đặt pause sau DB Commit và trước offset commit rồi kill consumer. Khi restart, cùng event phải tới handler nhưng unique processed_event + effect transaction khiến effect count không tăng. Lặp lại với hai consumers đồng thời tranh cùng business key. Dedup key scope consumer_name+event_id cho phép independent projections xử lý cùng event mà không chặn nhau.
