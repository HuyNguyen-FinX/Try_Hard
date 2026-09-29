# Consistency models và client observations

## Concept và Mental Model

Linearizability tôn trọng real-time order của operations; eventual consistency hứa convergence dưới assumptions, không hứa read mới ngay.

## How it works

Read-your-writes và monotonic reads là session guarantees; quorum formulas cần assumptions về membership, versioning và failures.

## Production Use Case

Sau tạo order, route read tới writer hoặc trả committed representation để tránh replica lag.

## Failure Scenarios

Read replica trả not-found sau successful write; stale config overwrites newer version.

## How I would debug this in production

Trace write/read versions, replica lag và client session routing.

## Trade-offs và When NOT to use

Strong read tăng coordination latency; stale reads chỉ khi product cho phép.

## Interview practice

How would you guarantee read-your-writes with replicas? Writer read, session token/version wait hoặc explicit stale contract.

## Key Takeaways

Linearizability tôn trọng real-time order của operations; eventual consistency hứa convergence dưới assumptions, không hứa read mới ngay..


## See also

- [Idempotent consumer transaction](../10-messaging/idempotent-consumer.md)
- [system-design-framework](../13-system-design/system-design-framework.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/linearizability.pdf)
