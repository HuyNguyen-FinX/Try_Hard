# Configuration lifecycle

## Concept và Mental Model

Config là versioned operational input cần validation và ownership.

## How it works

Parse typed schema, reject invalid budgets, immutable snapshot publish khi hot reload; distinguish startup-only settings như pool identity.

## Production Use Case

Timeout, max replicas và total DB connection budget được validate cùng nhau.

## Failure Scenarios

Partial reload state không nhất quán; zero timeout vô tình unlimited; drift giữa pods.

## How I would debug this in production

Log config version/hash và safe values, diff rollout; không log secrets.

## Trade-offs và When NOT to use

Hot reload giảm restart nhưng tăng concurrency/recovery complexity; restart rollout có thể đơn giản hơn.

## Interview practice

How do you reload config without a data race? Validate snapshot mới rồi atomic publish, không mutate shared map.

## Key Takeaways

Config là versioned operational input cần validation và ownership..


## See also

- [Microservices: independent ownership có chi phí](../11-software-architecture/microservices.md)
- [Distributed failure matrix](../12-distributed-systems/failure-scenarios.md)
- [tracing](../17-observability/tracing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://grpc.io/docs/guides/)

## Applied drill

Reload config gồm rate cap và pool cap cần validate quan hệ tổng trước publish. Build một immutable Config mới, không update từng field shared object vì request có thể thấy half old/half new. Nếu pool endpoint đổi, tạo dependency mới và health-check rồi swap owner có drain; atomic config pointer không tự quản connection pool lifecycle.
