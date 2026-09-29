# Distributed idempotency và ambiguous outcomes

## Concept và Mental Model

Retry cùng operation identity cần tạo effect tương đương một lần theo contract, kể cả response bị mất.

## How it works

Durable key+request hash+state, unique constraint, transactional effect; external provider cần stable key và reconciliation. Dedup retention phải phủ replay horizon.

## Production Use Case

Create payment operation pending, call provider với operation ID, persist outcome; recovery query provider khi timeout.

## Failure Scenarios

Crash sau effect trước response, expiry sớm, key reuse payload khác, concurrent attempts.

## How I would debug this in production

Inject crash tại các boundaries; compare ledger/provider/state bằng operation ID.

## Trade-offs và When NOT to use

Exactly-once claim chỉ có ý nghĩa trong boundary cụ thể; external effects thường cần idempotency và reconcile.

## Interview practice

How can a timeout leave outcome unknown? Server có thể commit rồi response bị mất.

## Key Takeaways

Retry cùng operation identity cần tạo effect tương đương một lần theo contract, kể cả response bị mất..


## See also

- [Idempotent consumer transaction](../10-messaging/idempotent-consumer.md)
- [system-design-framework](../13-system-design/system-design-framework.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.postgresql.org/docs/current/transaction-iso.html)
