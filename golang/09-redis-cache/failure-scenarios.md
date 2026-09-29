# Redis failure game day

## Concept và Mental Model

Cache failure cần policy theo data role: derived cache có fallback; security/rate/idempotency state cần safety decision riêng.

## How it works

Use tight timeout/circuit, bounded fallback to DB, stale cache nếu product cho phép; reconnect backoff+jitter.

## Production Use Case

Simulate Redis unavailable 5 phút, watch DB headroom và error budget.

## Failure Scenarios

Retry storm; all requests fallback DB; fail-open lock/idempotency gây duplicates.

## How I would debug this in production

Correlate Redis errors, cache misses, DB wait và request latency; verify recovery không refill storm.

## Trade-offs và When NOT to use

Availability versus freshness/correctness phải quyết định per endpoint.

## Interview practice

Would you fail open if Redis stores idempotency keys? Cần durable authority khác hoặc reject để không tạo side effect lặp.

## Key Takeaways

Cache failure cần policy theo data role: derived cache có fallback; security/rate/idempotency state cần safety decision riêng..


## See also

- [Database connection pool: 500 requests và 20 connections](../08-database/database-sql-pool.md)
- [distributed-lock](../12-distributed-systems/distributed-lock.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://redis.io/docs/latest/develop/)

## Applied drill

Game day đặt cache timeout ngắn hơn request budget, cắt Redis trong60s và đo source DB calls trước/sau. Fallback admission phải giữ DB dưới verified capacity; requests vượt budget trả explicit error/degraded response. Khi Redis hồi phục, ramp refresh và jitter TTL để không tạo đợt stampede thứ hai. Ghi rõ endpoints nào được stale và stale tối đa bao lâu.
