# Input validation tại boundaries

## Concept và Mental Model

Validation kiểm shape, limits và business semantics; sanitization không thay parameterization/authorization.

## How it works

Bound bytes trước decode, validate required/ranges/enums, normalize khi contract yêu cầu; distinguish absent/null/zero. SQL values parameterized; identifiers allowlisted.

## Production Use Case

Pagination limit 1..100 và tenant scope; upload path không cho traversal sau canonicalization policy.

## Failure Scenarios

Integer overflow, deeply nested JSON, decompression bombs, Unicode normalization mismatch.

## How I would debug this in production

Fuzz parser/property tests với boundary sizes và malformed inputs; measure allocation amplification.

## Trade-offs và When NOT to use

Strict unknown-field rejection có thể phá forward compatibility; quyết định theo API version policy.

## Interview practice

At which stage should request size be limited? Trước unbounded decode/allocation.

## Key Takeaways

Validation kiểm shape, limits và business semantics; sanitization không thay parameterization/authorization..


## See also

- [API security theo trust boundaries](../07-api-design/api-security.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://cheatsheetseries.owasp.org/)

## Applied drill

Endpoint nhận limit parse int rồi check1..100 trước allocate slice. JSON body bị MaxBytesReader bound trước decode, còn decompressed stream cần limit ở đúng tầng giải nén. Patch API phân biệt missing/null/zero theo contract; pointer DTO đơn thuần có thể chưa đủ cả ba trạng thái. Fuzz malformed UTF-8, nested inputs và numeric extremes theo accepted schema.
