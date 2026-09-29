# GOMAXPROCS và container CPU

## Concept và Mental Model

GOMAXPROCS điều khiển số P, không giới hạn G hoặc tổng OS threads.

## How it works

Default Linux từ Go 1.25 có container awareness và cập nhật tùy config/module version; explicit environment/runtime settings có thể override. Đọc runtime value đang chạy.

## Production Use Case

CPU quota 2 cores cần benchmark concurrency hợp quota; limits, requests và affinity là khái niệm khác nhau.

## Failure Scenarios

P quá nhiều làm burst dùng hết quota sớm rồi throttle, P99 cao dù CPU average trông vừa đủ.

## How I would debug this in production

So runtime.GOMAXPROCS(0), cgroup quota, throttled periods và scheduler latency; canary một thay đổi.

## Trade-offs và When NOT to use

Nhiều P có lợi khi CPU thực sự có sẵn, nhưng tăng lock/cache contention; không đặt bằng request concurrency.

## Interview practice

Why can raising GOMAXPROCS reduce throughput? Quota và synchronization có thể trở thành bottleneck.

## Key Takeaways

GOMAXPROCS điều khiển số P, không giới hạn G hoặc tổng OS threads..


## See also

- [Go scheduler: G, M, P và các đường blocking](scheduler-gmp.md)
- [trace](../16-performance/trace.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://github.com/golang/go/blob/go1.26.4/src/runtime/proc.go)
