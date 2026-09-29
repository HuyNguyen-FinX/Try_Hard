# Scheduler interview scenarios

## Concept và Mental Model

Đọc workload qua runnable/waiting/syscall trước khi đề xuất tune runtime.

## How it works

CPU-bound: queue runnable; I/O-bound: waiting; mutex contention: wait tập trung; cgo: M tăng. Mỗi trường hợp cần bằng chứng khác nhau.

## Production Use Case

So ba lần chạy: busy compute, HTTP chậm, lock giữ lâu; thu CPU/goroutine/trace cho mỗi lần.

## Failure Scenarios

Tăng workers chữa I/O throughput nhưng làm DB queue vượt deadline; profile trên laptop không phản ánh CPU quota.

## How I would debug this in production

Đối chiếu P99, queue depth, CPU throttling, goroutine states và load generator schedule.

## Trade-offs và When NOT to use

Không chỉ nhìn utilization trung bình; tail latency cần xem burst và contention.

## Interview practice

Why are 20000 goroutines not sufficient evidence of a leak? Cần trend sau drain và stack/lifetime evidence.

## Key Takeaways

Đọc workload qua runnable/waiting/syscall trước khi đề xuất tune runtime..


## See also

- [Go scheduler: G, M, P và các đường blocking](scheduler-gmp.md)
- [trace](../16-performance/trace.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://github.com/golang/go/blob/go1.26.4/src/runtime/proc.go)
