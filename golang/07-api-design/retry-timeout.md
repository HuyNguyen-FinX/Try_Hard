# API retry và deadline

## Concept và Mental Model

Retry tiêu thêm capacity để phục hồi transient failures; timeout là ambiguity, không chứng minh operation thất bại.

## How it works

Retry replay-safe operations, exponential backoff + jitter, max attempts và total budget. Chỉ một layer sở hữu policy hoặc bounded shared retry budget.

## Production Use Case

GET temporary 503 retry trong remaining ctx; POST mutation cần idempotency key.

## Failure Scenarios

Ba layers × ba attempts tạo tới 27 calls; body không replayable; retries chiếm pool.

## How I would debug this in production

Đo attempts/logical request, retry cause và remaining deadline trước mỗi attempt.

## Trade-offs và When NOT to use

Không retry validation/auth hoặc permanent errors; bounded retries vẫn cần circuit/admission khi outage.

## Interview practice

How do you avoid retry amplification? Một owner và per-operation total budget rõ.

## Key Takeaways

Retry tiêu thêm capacity để phục hồi transient failures; timeout là ambiguity, không chứng minh operation thất bại..


## See also

- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.rfc-editor.org/rfc/rfc9110)
