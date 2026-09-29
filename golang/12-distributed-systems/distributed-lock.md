# Leases, locks và fencing tokens

## Concept và Mental Model

Distributed lock có timeout/lease; old holder có thể tiếp tục chạy sau lease hết vì pause/network partition.

## How it works

Target resource cần monotonic fencing token và reject stale owner. Random unlock token chống xóa lease người khác nhưng không xếp thứ tự writes.

## Production Use Case

Single migration coordinator dùng lease và DB checkpoint version guard.

## Failure Scenarios

Stop-the-world/host pause dài hơn lease; lease renewed nhưng response mất; split-brain writer.

## How I would debug this in production

Audit owner epochs và accepted target writes; simulate delayed old owner.

## Trade-offs và When NOT to use

Dùng unique constraints/CAS/transactions khi invariant nằm một DB; lock distributed thêm failure modes.

## Interview practice

Why is leader election without fencing insufficient? Old leader vẫn có thể ghi khi nó chưa biết mất quyền.

## Key Takeaways

Distributed lock có timeout/lease; old holder có thể tiếp tục chạy sau lease hết vì pause/network partition..


## See also

- [Idempotent consumer transaction](../10-messaging/idempotent-consumer.md)
- [system-design-framework](../13-system-design/system-design-framework.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://etcd.io/docs/v3.6/learning/api/)
