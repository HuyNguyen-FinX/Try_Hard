# Retries như một capacity policy

## Concept và Mental Model

Retry dùng additional attempts để tăng success cho transient errors nhưng tăng load khi hệ thống yếu.

## How it works

Backoff+jitter, attempts cap, total deadline và retry budget theo logical requests; classify permanent/transient và side-effect safety.

## Production Use Case

Retry read timeout trong remaining budget; mutation chỉ replay khi có key/invariant.

## Failure Scenarios

Layered retries nhân traffic; clients cùng retry khi dependency recover; cancellation không interrupt sleep.

## How I would debug this in production

Attempts/success ratio, retry wait histogram và cause categories; test total wall time.

## Trade-offs và When NOT to use

Không retry để che overload; circuit/admission/load shedding có thể cần trước.

## Interview practice

How do three retrying layers amplify demand? Attempts nhân nhau, ví dụ 3×3×3.

## Key Takeaways

Retry dùng additional attempts để tăng success cho transient errors nhưng tăng load khi hệ thống yếu..


## See also

- [Idempotent consumer transaction](../10-messaging/idempotent-consumer.md)
- [system-design-framework](../13-system-design/system-design-framework.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.postgresql.org/docs/current/transaction-iso.html)
