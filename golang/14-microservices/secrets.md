# Service secrets và rotation

## Concept và Mental Model

Secrets cần least privilege, short exposure và rotation; config values không phải mọi thứ đều secret.

## How it works

Load qua secret manager/workload identity, tránh image/git/log; support overlap old/new credentials trong rotation có audit.

## Production Use Case

DB credentials rotate với new pool rồi drain old pool trong budget.

## Failure Scenarios

Secret env dump vào crash logs; revoke old key trước clients refresh; JWKS cache vô hạn.

## How I would debug this in production

Audit access/rotation timestamps, auth failures theo key ID không key value.

## Trade-offs và When NOT to use

Short TTL giảm exposure nhưng tăng dependency vào issuer availability; cache có bounded fallback.

## Interview practice

How do you rotate a credential without dropping all traffic? Overlap validity, refresh, observe, rồi revoke.

## Key Takeaways

Secrets cần least privilege, short exposure và rotation; config values không phải mọi thứ đều secret..


## See also

- [Microservices: independent ownership có chi phí](../11-software-architecture/microservices.md)
- [Distributed failure matrix](../12-distributed-systems/failure-scenarios.md)
- [tracing](../17-observability/tracing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://grpc.io/docs/guides/)
