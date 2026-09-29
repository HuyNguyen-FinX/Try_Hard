# Benchmark đúng workload

## Concept và Mental Model

Benchmark phải đo operation cần tối ưu, có input đại diện và compiler không loại toàn work.

## How it works

go test -run ^$ -bench . -benchmem -count=10; tách setup khỏi timer khi phù hợp; sink result có thể thay escape nên chọn tương ứng caller.

## Production Use Case

So before/after cùng CPU/toolchain, nhiều payload sizes và hot/cold distributions.

## Failure Scenarios

Một run bị thermal/noisy neighbor; benchmarking allocations của fmt thay code chính.

## How I would debug this in production

Xem ns/op, B/op, allocs/op và benchstat confidence; profile benchmark chỉ để đặt giả thuyết.

## Trade-offs và When NOT to use

Microbench không thay load test end-to-end/P99; giữ correctness tests.

## Interview practice

How can a global sink distort allocation results? Nó kéo lifetime value ra ngoài caller thực.

## Key Takeaways

Benchmark phải đo operation cần tối ưu, có input đại diện và compiler không loại toàn work..


## See also

- [pprof: chọn profile từ câu hỏi production](pprof.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)
