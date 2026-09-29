# Authentication và authorization

## Concept và Mental Model

Authentication xác định actor; authorization kiểm tra actor được làm gì với resource cụ thể.

## How it works

Validate credentials ở boundary, tạo principal đã xác thực; service kiểm tra tenant/resource/action. Không chỉ dựa user ID từ request body.

## Production Use Case

Order lookup dùng tenant predicate và policy; service-to-service identity không mặc nhiên bypass user permission.

## Failure Scenarios

JWT hợp lệ nhưng đọc order tenant khác; spoof forwarded identity headers.

## How I would debug this in production

Negative tests cross-tenant, expired credentials, missing scopes; log decision metadata không token.

## Trade-offs và When NOT to use

Gateway auth giảm lặp nhưng domain authorization vẫn ở service; cache policy cần invalidation.

## Interview practice

Why is a valid token insufficient to authorize a resource? Token identity không chứng minh ownership/action permission.

## Key Takeaways

Authentication xác định actor; authorization kiểm tra actor được làm gì với resource cụ thể..


## See also

- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
