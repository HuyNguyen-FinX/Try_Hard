# Fuzzing input space và invariants

## Concept và Mental Model

Fuzzer tìm inputs phá properties, không tự biết business correctness nếu oracle yếu.

## How it works

Seed representative edges; assert round-trip, no panic, size bounds hoặc semantic invariant. Keep function deterministic và avoid unbounded external I/O.

## Production Use Case

FuzzDecimalRoundTrip trong examples checks int64 parse/format including limits.

## Failure Scenarios

Oracle chỉ gọi code không assert; huge allocations; flaky time/network.

## How I would debug this in production

Save minimized failing corpus, turn critical failures into regression seeds.

## Trade-offs và When NOT to use

Fuzz complement unit/integration, không chứng minh absence of bugs.

## Interview practice

What makes a strong fuzz property? Invariant độc lập implementation và meaningful across input space.

## Key Takeaways

Fuzzer tìm inputs phá properties, không tự biết business correctness nếu oracle yếu..


## See also

- [README](../examples/README.md)
- [Race condition versus data race](../04-concurrency/race-condition.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/testing)

## Applied drill

FuzzLowerBound trong examples không chỉ so với một binary-search implementation khác: nó kiểm partition invariant trên mọi element trước/sau returned index. Điều này bắt off-by-one và duplicate-boundary errors. FuzzDecimalRoundTrip bao int64 extremes; minimized failing input được lưu thành seed. Với parser untrusted, thêm allocation/input bound để fuzz không thành uncontrolled memory workload.
