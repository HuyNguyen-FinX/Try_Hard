# TLS: trust, identity và lifecycle

## Concept và Mental Model

TLS bảo vệ transport confidentiality/integrity và server identity; mTLS thêm client certificate identity.

## How it works

Verify chain/hostname và trusted roots; certificate rotation trước expiry; reuse connections nhưng có policy cho identity changes.

## Production Use Case

Internal mTLS service identity map tới authorization policy, không chỉ trust mọi cert cùng CA.

## Failure Scenarios

InsecureSkipVerify bỏ identity check; missing CA in container; expired cert; clock skew.

## How I would debug this in production

Inspect handshake failures, chain/SAN/expiry, time sync và root bundle; never log private keys.

## Trade-offs và When NOT to use

TLS termination edge đơn giản nhưng trust boundary phía sau cần explicit; mTLS thêm rotation operations.

## Interview practice

Does mTLS remove the need for authorization? Không, identity chưa quyết định action/resource permission.

## Key Takeaways

TLS bảo vệ transport confidentiality/integrity và server identity; mTLS thêm client certificate identity..


## See also

- [API security theo trust boundaries](../07-api-design/api-security.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://cheatsheetseries.owasp.org/)
