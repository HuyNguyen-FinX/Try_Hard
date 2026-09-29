# API versioning và compatibility

## Concept và Mental Model

Version tồn tại ở wire shape lẫn semantics; additive change vẫn có thể phá strict clients.

## How it works

Expand-contract: thêm optional field, deploy readers hiểu cả cũ/mới, migrate writers, đo adoption rồi deprecate. Enum thêm giá trị cần unknown handling.

## Production Use Case

Version header/path theo ecosystem; có sunset policy và compatibility tests.

## Failure Scenarios

Required field mới phá old clients; rename mang ý nghĩa khác nhưng giữ route; generated clients reject enum lạ.

## How I would debug this in production

Replay fixtures và inspect client versions/errors; canary schema changes.

## Trade-offs và When NOT to use

Giữ nhiều versions tăng maintenance; version chỉ khi contract break cần thiết.

## Interview practice

When can adding a field be breaking? Strict decoder, signatures hoặc client validation có thể reject.

## Key Takeaways

Version tồn tại ở wire shape lẫn semantics; additive change vẫn có thể phá strict clients..


## See also

- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.rfc-editor.org/rfc/rfc9110)
