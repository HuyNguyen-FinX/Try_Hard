# CAP: quyết định trong network partition

## Concept và Mental Model

CAP xét linearizable consistency và availability theo định nghĩa lý thuyết khi có partition; không phải chọn hai tính năng tùy ý mọi lúc.

## How it works

Nếu replicas không giao tiếp được, trả lời mọi request có thể phá single-copy consistency; chờ/reject có thể giữ safety nhưng mất availability ở phần hệ thống.

## Production Use Case

Balance update chọn authority/quorum, catalog read có thể stale theo contract.

## Failure Scenarios

Gọi eventual consistency là always available dù quorum/region failure vẫn khiến request fail.

## How I would debug this in production

Xác định operation, partition model và response guarantees trước gắn nhãn CP/AP.

## Trade-offs và When NOT to use

CAP không tự quyết định latency trade-off khi network bình thường; nêu consistency model cụ thể.

## Interview practice

What does availability mean in CAP? Response hợp lệ cho requests tới non-failing nodes trong mô hình, không chỉ uptime dashboard.

## Key Takeaways

CAP xét linearizable consistency và availability theo định nghĩa lý thuyết khi có partition; không phải chọn hai tính năng tùy ý mọi lúc..


## See also

- [Idempotent consumer transaction](../10-messaging/idempotent-consumer.md)
- [system-design-framework](../13-system-design/system-design-framework.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://users.ece.cmu.edu/~adrian/731-sp04/readings/GL-cap.pdf)
