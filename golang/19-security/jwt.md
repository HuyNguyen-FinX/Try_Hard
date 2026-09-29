# JWT validation và key rotation

## Concept và Mental Model

JWT signed token bảo vệ integrity, không tự encrypt payload và không tự cấp quyền cho mọi resource.

## How it works

Allowlist algorithm, validate signature, issuer, audience, expiry/not-before với bounded skew; trusted JWKS source và key rotation cache policy.

## Production Use Case

Access token ngắn hạn, principal có scopes nhưng domain còn kiểm tenant/ownership.

## Failure Scenarios

Accept alg từ attacker không policy; decode không verify; trust arbitrary jku URL; stale JWKS cache.

## How I would debug this in production

Test wrong issuer/audience/algorithm/key, expired tokens và rotation overlap; không log token.

## Trade-offs và When NOT to use

Self-contained token giảm introspection latency nhưng revocation khó; opaque tokens có online authority trade-off.

## Interview practice

Why is decoding JWT insufficient? Base64 decode không xác minh authenticity hoặc claims.

## Key Takeaways

JWT signed token bảo vệ integrity, không tự encrypt payload và không tự cấp quyền cho mọi resource..


## See also

- [API security theo trust boundaries](../07-api-design/api-security.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.rfc-editor.org/rfc/rfc8725.html)
