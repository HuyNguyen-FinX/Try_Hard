# Bulkheads và capacity isolation

## Concept và Mental Model

Bulkhead chia capacity để một dependency/tenant failure không làm cạn tài nguyên mọi request.

## How it works

Separate semaphores, worker pools, queue quotas và client/DB budgets theo failure domain; giữ reserve cho critical path.

## Production Use Case

Report export workers không chiếm toàn DB pool của checkout.

## Failure Scenarios

Tách HTTP clients nhưng vẫn chung unbounded goroutines/DB nên isolation giả.

## How I would debug this in production

Per-class queue/active/reject metrics và failure injection một dependency.

## Trade-offs và When NOT to use

Isolation giảm sharing efficiency; nhiều pools tăng aggregate connections.

## Interview practice

Which shared resource can defeat an apparent bulkhead? DB, CPU, memory hoặc global retry queue.

## Key Takeaways

Bulkhead chia capacity để một dependency/tenant failure không làm cạn tài nguyên mọi request..


## See also

- [Idempotent consumer transaction](../10-messaging/idempotent-consumer.md)
- [system-design-framework](../13-system-design/system-design-framework.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.postgresql.org/docs/current/transaction-iso.html)

## Applied drill

Giả định DB budget100 slots: checkout60, reports20, workers10, reserve10. Khi reports chậm, checkout không được dùng chung unbounded acquisition queue khiến isolation mất ý nghĩa. Static partition có thể lãng phí khi reports idle; adaptive borrowing cần reserve floor và overload tests. Budget còn phải nhân theo replicas hoặc dùng central authority tương ứng.
