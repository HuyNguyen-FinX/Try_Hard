# OS thread versus goroutine

## Concept và Mental Model

OS schedule threads; Go runtime multiplex G trên M với P. Concurrency là nhiều việc đang tiến triển, parallelism là thực thi cùng lúc.

## How it works

OS thread có kernel resources; G có growable stack và runtime state. Blocking cgo có thể giữ M lâu nên thread count vẫn tăng.

## Production Use Case

I/O-heavy gateway có hàng nghìn socket nhưng số thread chạy Go gần capacity CPU.

## Failure Scenarios

Một library gọi blocking C mỗi request làm hết thread/FD dù GOMAXPROCS thấp.

## How I would debug this in production

Xem OS thread count, cgo stacks và execution trace; không suy từ NumGoroutine sang số thread.

## Trade-offs và When NOT to use

G phù hợp Go-managed work; thread affinity chỉ dùng khi API native yêu cầu.

## Interview practice

Why can a Go process have more threads than P? M có thể blocked trong syscall hoặc cgo.

## Key Takeaways

OS schedule threads; Go runtime multiplex G trên M với P.


## See also

- [Go scheduler: G, M, P và các đường blocking](scheduler-gmp.md)
- [trace](../16-performance/trace.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://github.com/golang/go/blob/go1.26.4/src/runtime/proc.go)
