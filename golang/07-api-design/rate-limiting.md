# API rate limiting

## Concept và Mental Model

Rate limit bound arrivals theo thời gian; concurrency limit bound in-flight work.

## How it works

Token bucket cho burst capacity và refill rate; key theo authenticated tenant/route, không tin X-Forwarded-For từ nguồn tùy ý. Distributed counter cần atomic update và TTL.

## Production Use Case

429 kèm retry guidance cho per-tenant quota; 503 cho global overload tùy contract.

## Failure Scenarios

Một hot tenant chiếm global bucket; retry cùng thời điểm; backend limiter unavailable có fail-open/closed trade-off.

## How I would debug this in production

Đo allowed/rejected theo bounded tenant tier, bucket wait và downstream saturation.

## Trade-offs và When NOT to use

Local limiter rẻ nhưng fleet quota chỉ approximate; centralized limiter thêm dependency.

## Interview practice

Why do rate and concurrency limits solve different problems? Slow requests tăng in-flight ngay cả rate giữ nguyên.

## Key Takeaways

Rate limit bound arrivals theo thời gian; concurrency limit bound in-flight work..


## See also

- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.rfc-editor.org/rfc/rfc9110)
