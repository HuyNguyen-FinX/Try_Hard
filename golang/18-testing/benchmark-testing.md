# Benchmark tests có statistical comparison

## Concept và Mental Model

Benchmark kết quả phải repeatable và dùng đúng input distribution.

## How it works

b.ReportAllocs, setup ngoài measured loop theo API, consume result để compiler không loại. Run multiple samples rồi benchstat.

## Production Use Case

BenchmarkFormat trong examples là harness nhỏ; thêm payload distribution trước suy production benefit.

## Failure Scenarios

Parallel benchmark vượt downstream thật giả lập; global sink tạo shared race nếu RunParallel.

## How I would debug this in production

Compare ns/op, bytes/allocs và profile on same build; report hardware/toolchain.

## Trade-offs và When NOT to use

Không fail CI theo threshold quá nhạy nếu runners noisy; controlled perf lane tốt hơn.

## Interview practice

How would you tell noise from a regression? Repeated samples, baseline controls và effect size.

## Key Takeaways

Benchmark kết quả phải repeatable và dùng đúng input distribution..


## See also

- [README](../examples/README.md)
- [Race condition versus data race](../04-concurrency/race-condition.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/testing)

## Applied drill

Thử BenchmarkFormat với nhiều count, lưu before/after và benchstat khi tool sẵn có. Nếu đổi benchmark sang RunParallel, global string sink sẽ trở thành data race; dùng goroutine-local consumption hoặc design sink đúng contract. Benchmark config phải ghi GOMAXPROCS, toolchain và input sizes. Performance comparison chỉ hợp khi work và result semantics giữ nguyên.
