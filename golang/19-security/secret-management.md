# Secrets: distribution, storage và rotation

## Concept và Mental Model

Secret exposure có thể qua code, image layer, logs, crash dumps và telemetry.

## How it works

Prefer workload identity/secret manager, least privilege, encryption at rest và access audit; rotation với overlap/reload và rollback policy.

## Production Use Case

Separate credentials per environment/service; migration role khác application DML role.

## Failure Scenarios

Commit secret vào git, dump env, share admin DB role, expired credential reconnect storm.

## How I would debug this in production

Audit access/version/key IDs, repo secret scanning và rotation drills; redact content.

## Trade-offs và When NOT to use

Environment variables dễ dùng nhưng dễ lọt qua diagnostics; chọn cơ chế theo runtime/threat model.

## Interview practice

How would you rotate DB credentials with pooled connections? Create refreshed pool, route new work, drain old connections rồi revoke.

## Key Takeaways

Secret exposure có thể qua code, image layer, logs, crash dumps và telemetry..


## See also

- [API security theo trust boundaries](../07-api-design/api-security.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://cheatsheetseries.owasp.org/)
