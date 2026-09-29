# REST API contracts

## Concept và Mental Model

HTTP API contract gồm resource, method semantics, representation và errors; JSON endpoint chưa đủ để nói thiết kế tốt.

## How it works

GET an toàn đọc; PUT biểu diễn replace theo contract; PATCH cập nhật phần; POST thường tạo action/resource. Status phải phân biệt validation, auth, conflict và overload.

## Production Use Case

POST /orders trả ID và trạng thái; async processing trả 202 với status URL khi work đã durable.

## Failure Scenarios

GET có side effect bị proxy retry; trả 200 cho mọi lỗi làm monitoring/client retry sai.

## How I would debug this in production

Contract tests cho methods/status, idempotency và field compatibility; trace route templates.

## Trade-offs và When NOT to use

Không ép workflow phức tạp thành CRUD giả; action endpoint rõ có thể tốt hơn.

## Interview practice

When should an API return 202 instead of 201? Work đã accepted bền vững nhưng chưa hoàn thành theo contract.

## Key Takeaways

HTTP API contract gồm resource, method semantics, representation và errors; JSON endpoint chưa đủ để nói thiết kế tốt..


## See also

- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.rfc-editor.org/rfc/rfc9110)
