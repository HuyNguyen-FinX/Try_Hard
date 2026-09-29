# Observability across services

## Concept và Mental Model

Correlation cần request/trace/event IDs và semantic metrics xuyên boundaries.

## How it works

HTTP/gRPC propagate trace context; Kafka dùng headers và links. Consistent service/version/operation attributes, không raw user IDs làm metric labels.

## Production Use Case

Một checkout trace nối inventory call, DB Tx và outbox event processing latency.

## Failure Scenarios

Sampling bỏ rare failures; clock skew gây timeline khó đọc; logs thiếu operation ID.

## How I would debug this in production

Start từ SLO symptom, pivot metric→trace→log; compare deployment cohorts.

## Trade-offs và When NOT to use

100% tracing có overhead/storage; sampling và error-focused capture cần privacy policy.

## Interview practice

How do you trace asynchronous work after request completion? Dùng producer context metadata và consumer span/link theo instrumentation model.

## Key Takeaways

Correlation cần request/trace/event IDs và semantic metrics xuyên boundaries..


## See also

- [Microservices: independent ownership có chi phí](../11-software-architecture/microservices.md)
- [Distributed failure matrix](../12-distributed-systems/failure-scenarios.md)
- [tracing](../17-observability/tracing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://grpc.io/docs/guides/)

## Applied drill

Một async notification có producer request kết thúc trước consumer bắt đầu. Giữ event ID và trace metadata trong envelope, consumer tạo processing span/link theo instrumentation convention. Không giữ nguyên expired request deadline làm job fail ngay. Đo event_age tại consumer và total delivery latency vì HTTP producer span ngắn không chứng minh user nhận notification nhanh.
