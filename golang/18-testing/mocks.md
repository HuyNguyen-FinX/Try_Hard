# Mocks, fakes và contract tests

## Concept và Mental Model

Mock kiểm interactions khi interaction là contract; fake cung cấp behavior đơn giản, integration test kiểm adapter thật.

## How it works

Small consumer interfaces tránh mocks khổng lồ. Fake phải mô phỏng error/cancel/ordering mà test phụ thuộc.

## Production Use Case

Fake clock cho retry; httptest cho HTTP protocol; DB thật cho isolation.

## Failure Scenarios

Mock transaction luôn success che rollback bug; expected call order cứng dù contract cho parallelism.

## How I would debug this in production

Run same contract cases trên adapters khi khả thi; compare real driver cancellation.

## Trade-offs và When NOT to use

Không dùng mock để chứng minh SQL plan, locks hay connection pooling.

## Interview practice

Why can a mock-based test pass while production leaks connections? Mock không sở hữu real Rows/pool resources.

## Key Takeaways

Mock kiểm interactions khi interaction là contract; fake cung cấp behavior đơn giản, integration test kiểm adapter thật..


## See also

- [README](../examples/README.md)
- [Race condition versus data race](../04-concurrency/race-condition.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/testing)
