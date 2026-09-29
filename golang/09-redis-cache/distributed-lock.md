# Redis lock và fencing

## Concept và Mental Model

Lease bằng TTL giảm concurrent work nhưng expired owner vẫn có thể chạy; mutual exclusion ở lock server chưa đủ bảo vệ external writes.

## How it works

SET key token NX PX acquire; release atomically compare token rồi delete bằng script. Với correctness-critical writes, resource cần reject stale fencing token monotonic từ authority phù hợp.

## Production Use Case

Cache rebuild coalescing có thể chấp nhận duplicate; money invariant dùng DB constraint/transaction thay lock Redis đơn thuần.

## Failure Scenarios

Process pause quá TTL, owner mới chạy, owner cũ wake ghi đè; plain DEL xóa lock người khác.

## How I would debug this in production

Record token/lease timestamps và target versions; inject pause/network partition.

## Trade-offs và When NOT to use

Redis lease phù hợp best-effort exclusion; không tuyên bố universal safety cho distributed lock không nêu timing assumptions.

## Interview practice

Why is a random ownership token not a fencing token? Nó chứng minh owner release, không cung cấp thứ tự để target reject stale writes.

## Key Takeaways

Lease bằng TTL giảm concurrent work nhưng expired owner vẫn có thể chạy; mutual exclusion ở lock server chưa đủ bảo vệ external writes..


## See also

- [Database connection pool: 500 requests và 20 connections](../08-database/database-sql-pool.md)
- [distributed-lock](../12-distributed-systems/distributed-lock.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://redis.io/docs/latest/develop/)
