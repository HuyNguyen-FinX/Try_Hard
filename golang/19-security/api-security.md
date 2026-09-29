# Security review theo endpoint

## Concept và Mental Model

Bảo vệ identity, resource authorization, input bounds và side effects tại mọi endpoint.

## How it works

Allowlist methods/content types, bounded decode, tenant-scoped queries, rate/admission limits và consistent error redaction.

## Production Use Case

Export endpoint cần authorize dataset/tenant và signed download URL ngắn hạn.

## Failure Scenarios

IDOR, mass assignment, replay mutation, public pprof, unbounded decompression.

## How I would debug this in production

Negative tests cho cross-tenant IDs và oversized payload; review access logs bằng safe metadata.

## Trade-offs và When NOT to use

Không coi private network là đủ authorization; service identity và user permissions khác nhau.

## Interview practice

How would you test object-level authorization? Hai principals/tenants và mọi read/write route trên foreign object.

## Key Takeaways

Bảo vệ identity, resource authorization, input bounds và side effects tại mọi endpoint..


## See also

- [API security theo trust boundaries](../07-api-design/api-security.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://cheatsheetseries.owasp.org/)

## Applied drill

Dùng hai tenantsA/B và tạo resource ởA. B thử GET, PATCH, DELETE, list filter và exported download URL; tất cả access trái policy phải fail ngay cả JWT signature hợp lệ. Cache keys và query predicates đều cần tenant scope, vì DB authorization đúng nhưng cache key thiếu tenant vẫn lộ dữ liệu. Log decision reason không log token/resource contents.
