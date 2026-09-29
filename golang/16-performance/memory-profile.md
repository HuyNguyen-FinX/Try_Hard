# Heap và allocs profiles

## Concept và Mental Model

inuse_space cho retained bytes; alloc_space cho allocation volume sampled từ lịch sử profile.

## How it works

Use sample_index để đổi views, diff cùng steady state; forced GC ảnh hưởng state và latency nên có chủ đích.

## Production Use Case

Cache token giữ huge backing array thấy allocation site của original payload.

## Failure Scenarios

Confuse alloc_space với leak; RSS ngoài Go do cgo/mmap không hiện đầy đủ.

## How I would debug this in production

So inuse_objects/space, goroutine stacks và cache cardinality qua thời gian.

## Trade-offs và When NOT to use

Giảm memory bằng clone có thể tăng allocs nhưng giảm retention; measure cả hai.

## Interview practice

How can cloning a tiny slice improve total memory despite allocating? Nó bỏ reference tới huge array.

## Key Takeaways

inuse_space cho retained bytes; alloc_space cho allocation volume sampled từ lịch sử profile..


## See also

- [pprof: chọn profile từ câu hỏi production](pprof.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)

## Applied drill

Chạy benchmark với `-memprofile=mem.out`, mở lần lượt `go tool pprof -sample_index=alloc_space mem.out` và `-sample_index=inuse_space`. Format benchmark tạo short-lived strings nên two views khác nhau là hợp lý. Để đo retention, cần workload giữ references có chủ đích; không suy parser leak từ benchmark này. Ghi capture uptime/RPS để cumulative profiles so được.
