# API idempotency key

## Concept và Mental Model

Idempotency bảo đảm replay cùng logical operation không tạo side effect thêm theo contract/retention window.

## How it works

Scope key theo tenant+operation; lưu request hash, state và stable response trong durable store. Unique constraint claim; key trùng payload khác trả conflict.

## Production Use Case

Payment creation lưu operation trước provider call và dùng cùng provider key; reconcile ambiguous outcome.

## Failure Scenarios

Redis TTL hết trước retry; cache response chỉ sau side effect để lại crash window; hai replicas cùng xử lý key.

## How I would debug this in production

Trace logical operation ID và attempts; inject crash giữa claim, effect, response persistence.

## Trade-offs và When NOT to use

Storage retention có cost; không cache mọi 500 vĩnh viễn nếu contract cho retry sau recovery.

## Interview practice

What happens if the server crashes after charging but before saving the response? Query provider bằng stable key và reconcile.

## Key Takeaways

Idempotency bảo đảm replay cùng logical operation không tạo side effect thêm theo contract/retention window..


## See also

- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.rfc-editor.org/rfc/rfc9110)
