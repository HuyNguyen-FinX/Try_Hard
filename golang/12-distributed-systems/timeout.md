# Timeout và failure detection

## Concept và Mental Model

Timeout là suspicion về progress, không chứng minh remote process chết hoặc operation chưa commit.

## How it works

Budget gồm network/queue/work/cleanup; propagate remaining deadline. Clocks/transport representation khác nhau nên dùng library deadline propagation.

## Production Use Case

Caller dừng chờ payment provider, chuyển operation sang unknown/pending reconciliation.

## Failure Scenarios

Timeout ngắn tạo duplicate retries; quá dài giữ connections/goroutines; đồng loạt expiry tạo burst.

## How I would debug this in production

Trace time spent mỗi hop, canceled operations còn chạy và remote outcome records.

## Trade-offs và When NOT to use

Timeout nhỏ đổi resource protection lấy false positives; chọn theo SLO và observed tails.

## Interview practice

Why can timeout not safely trigger a second payment without a key? First attempt có thể đã charge.

## Key Takeaways

Timeout là suspicion về progress, không chứng minh remote process chết hoặc operation chưa commit..


## See also

- [Idempotent consumer transaction](../10-messaging/idempotent-consumer.md)
- [system-design-framework](../13-system-design/system-design-framework.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.postgresql.org/docs/current/transaction-iso.html)
