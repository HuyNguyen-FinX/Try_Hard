# Block profile

## Concept và Mental Model

Block profile ghi thời gian chờ synchronization events như channel và locks khi được enable.

## How it works

SetBlockProfileRate điều khiển sampling; đọc blocking site/callers. Không coi nó là toàn bộ network/OS I/O wait profile.

## Production Use Case

Pipeline kẹt output send khi downstream slower.

## Failure Scenarios

Capture trước khi enable không có history; long permanent wait có thể cần goroutine snapshot để thấy rõ.

## How I would debug this in production

So channel queue metrics, waiter stacks và execution trace.

## Trade-offs và When NOT to use

Overhead phụ thuộc rate; capture ngắn theo hypothesis.

## Interview practice

How do block and CPU profiles complement each other? Một bên chờ progress, một bên tiêu execution cycles.

## Key Takeaways

Block profile ghi thời gian chờ synchronization events như channel và locks khi được enable..


## See also

- [pprof: chọn profile từ câu hỏi production](pprof.md)
- [design-high-throughput-api](../13-system-design/design-high-throughput-api.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/diagnostics)

## Applied drill

Từ lab package, capture `go test -run TestPoolCancellation -blockprofile=block.out`, rồi `go tool pprof -top block.out`. Chờ ctx.Done trong test là expected wait, không leak; giải thích owner nào đóng signal. Trong production, chọn rate và duration trước capture; compare với goroutine snapshot để thấy waiters chưa hoàn tất trong cửa sổ sample.
