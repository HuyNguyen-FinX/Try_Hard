# Pagination: stable order và cursor

## Concept và Mental Model

Pagination cần order deterministic, bound page size và contract khi dữ liệu đổi giữa pages.

## How it works

Keyset dùng (created_at,id) và index cùng thứ tự; cursor opaque có filter/version và integrity khi cần. Offset sâu tốn scan và dễ shift khi insert/delete.

## Production Use Case

GET /orders?after=cursor&limit=100 theo tenant, authorization vẫn kiểm tra mỗi page.

## Failure Scenarios

Timestamp ties bỏ/duplicate rows; cursor từ tenant khác; client đổi filter giữa pages.

## How I would debug this in production

Fixtures với equal timestamps và concurrent inserts, EXPLAIN deep pages và query count.

## Trade-offs và When NOT to use

Offset tiện nhảy page nhỏ; keyset hiệu quả nhưng không tự cho random page number.

## Interview practice

Why must a cursor include a tiebreaker? Order cần total ordering để không skip rows có cùng timestamp.

## Key Takeaways

Pagination cần order deterministic, bound page size và contract khi dữ liệu đổi giữa pages..


## See also

- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.rfc-editor.org/rfc/rfc9110)
