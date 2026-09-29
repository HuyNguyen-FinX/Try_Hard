# Leader election và epochs

## Concept và Mental Model

Election chọn coordinator hiện tại theo authority; không tự dừng old leader ngoài mạng.

## How it works

Lease/quorum service cấp leadership epoch; writes cần fencing hoặc compare-version tại resource. Renew loop có deadline và stop work khi mất quyền.

## Production Use Case

Một scheduler tạo jobs với unique schedule+fire_time để duplicate leaders không double-create.

## Failure Scenarios

Network partition sinh two active actors; long pause làm expired owner wake.

## How I would debug this in production

Leadership transitions, lease age, epoch ở writes và rejected stale operations.

## Trade-offs và When NOT to use

Leader giảm coordination trong work path nhưng là bottleneck/failover concern; partition ownership có thể tốt hơn.

## Interview practice

How can two leaders exist operationally despite a correct election service? Old process chưa biết lease đã mất.

## Key Takeaways

Election chọn coordinator hiện tại theo authority; không tự dừng old leader ngoài mạng..


## See also

- [Idempotent consumer transaction](../10-messaging/idempotent-consumer.md)
- [system-design-framework](../13-system-design/system-design-framework.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://etcd.io/docs/v3.6/learning/api/)
