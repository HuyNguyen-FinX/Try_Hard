# API security theo trust boundaries

## Concept và Mental Model

Input từ client, proxy và downstream đều cần validation theo trust boundary.

## How it works

Bound header/body/decompressed size, parameterize SQL, validate URLs/redirect destinations chống SSRF, authorize object-level, dùng TLS và credential rotation.

## Production Use Case

Upload presign scope object/size/expiry; outbound allowlist bảo vệ metadata/private endpoints khi nhận URL.

## Failure Scenarios

IDOR, SSRF qua redirect/DNS rebinding, mass assignment, request smuggling ở proxy mismatch.

## How I would debug this in production

Security tests gồm cross-tenant IDs, oversized/recursive payloads, unexpected content type và redirect chain.

## Trade-offs và When NOT to use

Không dùng denylist string đơn giản cho URLs; parse/resolve/connect policy phải nhất quán.

## Interview practice

How can a safe-looking URL become SSRF after a redirect? Destination mới phải được policy kiểm tra lại.

## Key Takeaways

Input từ client, proxy và downstream đều cần validation theo trust boundary..


## See also

- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)

## Applied drill

Review endpoint import-by-URL: validate scheme và destination policy trước request, kiểm lại mỗi redirect, kiểm IP resolved/connect target theo allowlist policy và deny private metadata networks khi cần. Total deadline, max response bytes và decompression bounds phải đi cùng policy. Unit URL parsing tests chưa mô phỏng DNS rebinding; integration boundary cần controlled resolver/dialer test.
