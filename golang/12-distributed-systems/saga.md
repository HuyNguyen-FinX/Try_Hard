# Saga và compensating actions

## Concept và Mental Model

Saga điều phối local transactions; compensation là business action bù, không rollback thời gian.

## How it works

State machine persisted, commands/events idempotent, retries bounded; orchestrator giữ progress hoặc choreography có event contracts rõ.

## Production Use Case

Order reserve stock → authorize payment → confirm; failure release reservation/void authorization theo policy.

## Failure Scenarios

Compensation fail; events out of order; double refund khi replay; irreversible external action.

## How I would debug this in production

Trace saga ID, state transitions, timeout age và reconciliation backlog.

## Trade-offs và When NOT to use

Saga tăng availability nhưng exposed intermediate states; dùng một DB transaction nếu đủ boundary.

## Interview practice

Can compensation always restore the original world? Không, email đã gửi hoặc shipment đã đi cần policy khác.

## Key Takeaways

Saga điều phối local transactions; compensation là business action bù, không rollback thời gian..


## See also

- [Idempotent consumer transaction](../10-messaging/idempotent-consumer.md)
- [system-design-framework](../13-system-design/system-design-framework.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.postgresql.org/docs/current/transaction-iso.html)
