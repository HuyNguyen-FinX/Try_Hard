# Blocking syscalls

## Concept và Mental Model

Syscall chạy kernel code trên M; Go runtime có protocol để Go work khác vẫn có P.

## How it works

P có thể release/retake; syscall return thử lấy lại P hoặc enqueue G. Short syscall không luôn dẫn đến M mới.

## Production Use Case

File reads và C libraries cần capacity riêng nếu block OS threads.

## Failure Scenarios

Disk stall kéo dài làm tăng blocked M và queued work.

## How I would debug this in production

Correlate thread stacks, disk latency, cgo call counts và trace syscall regions.

## Trade-offs và When NOT to use

Goroutine wrapper không biến syscall thành cancelable; giới hạn concurrency ở boundary.

## Interview practice

Does a blocking syscall always block P? Không; giải thích release/retake và return path.

## Key Takeaways

Syscall chạy kernel code trên M; Go runtime có protocol để Go work khác vẫn có P..


## See also

- [Go scheduler: G, M, P và các đường blocking](scheduler-gmp.md)
- [trace](../16-performance/trace.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://github.com/golang/go/blob/go1.26.4/src/runtime/proc.go)
