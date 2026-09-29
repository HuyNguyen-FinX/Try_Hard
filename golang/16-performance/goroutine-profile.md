# Goroutine profiles và stack grouping

## Concept và Mental Model

Snapshot cho thấy G đang chạy/chờ ở call stack nào; trend mới giúp phân biệt leak với concurrency hợp lệ.

## How it works

Debug dump group by stack signature, state và creation site; strip volatile IDs khi aggregate.

## Production Use Case

20k G phần lớn database/sql acquire: kiểm tra pool/DB hold time trước scheduler tune.

## Failure Scenarios

Stack dump quá lớn gây log volume; gọi mọi waiting G là leak.

## How I would debug this in production

Lấy ba snapshots trước/trong/sau drain, xem nhóm nào không giảm và owner đã exit.

## Trade-offs và When NOT to use

Snapshot không cho duration chính xác; dùng trace/metrics để bổ sung timeline.

## Interview practice

What is evidence that a waiting goroutine is leaked? Lifetime owner đã kết thúc và không còn event/exit hợp lệ.

## Key Takeaways

Snapshot cho thấy G đang chạy/chờ ở call stack nào; trend mới giúp phân biệt leak với concurrency hợp lệ..


## See also

- [pprof: chọn profile từ câu hỏi production](pprof.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)
