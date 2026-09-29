# Vulnerabilities trong Go backend

## Concept và Mental Model

Memory safety giảm một lớp lỗi nhưng không ngăn injection, authorization bugs, SSRF hoặc resource exhaustion.

## How it works

Review SQL/command construction, template context escaping, unsafe/cgo, dependency vulnerabilities, file path/URL trust và concurrency lifetime.

## Production Use Case

Use govulncheck khi tool/version/network đã chuẩn bị, patch dependencies và verify reachability/behavior.

## Failure Scenarios

exec shell string từ input, arbitrary URL fetch, public debug listener, unbounded goroutines.

## How I would debug this in production

Threat-model data flow từ untrusted input tới sink; targeted negative tests và audit dependency versions.

## Trade-offs và When NOT to use

Không coi static scan pass là secure; business authorization cần manual review/tests.

## Interview practice

Which serious bugs remain despite Go memory safety? IDOR, SSRF, injection, replay và denial of service.

## Key Takeaways

Memory safety giảm một lớp lỗi nhưng không ngăn injection, authorization bugs, SSRF hoặc resource exhaustion..


## See also

- [API security theo trust boundaries](../07-api-design/api-security.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://cheatsheetseries.owasp.org/)
