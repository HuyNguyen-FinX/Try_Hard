# Prometheus metrics cho Go

## Concept và Mental Model

Prometheus scrape samples theo time series identity; labels quyết định memory/query cost.

## How it works

Expose private metrics endpoint, choose histogram buckets theo SLO, track runtime/process và application counters. Rate counters qua window đủ samples.

## Production Use Case

Pool InUse gauge, acquire wait histogram, requests by route/status class.

## Failure Scenarios

Label raw URL/order ID tạo hàng triệu series; buckets không bao quanh 200ms SLO.

## How I would debug this in production

Check scrape errors/duration, cardinality growth và aggregation across replicas.

## Trade-offs và When NOT to use

Metrics endpoint phải rẻ; không chạy expensive DB query mỗi scrape.

## Interview practice

How would you measure percentage under 200ms? Histogram bucket count phù hợp chia total count theo rate.

## Key Takeaways

Prometheus scrape samples theo time series identity; labels quyết định memory/query cost..


## See also

- [pprof: chọn profile từ câu hỏi production](../16-performance/pprof.md)
- [service-outage](../20-production-scenarios/service-outage.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://prometheus.io/docs/practices/histograms/)

## Applied drill

Với classic histogram bucket le="0.2", good fraction có thể lấy rate(bucket≤0.2)/rate(count) cùng route/window; validate bucket tồn tại và timeout policy. Counter series theo status class/service/route có bound, còn user_id khiến cardinality tăng theo customer count. Scrape endpoint không nên tự chạy DB health query vì nhiều Prometheus replicas có thể nhân load.
