# Kubernetes Service và endpoint routing

## Concept và Mental Model

Service tạo stable discovery/routing tới matching endpoints; không quản business request load trực tiếp.

## How it works

Selectors/EndpointSlices quyết định targets; readiness ảnh hưởng endpoints theo propagation. Headless service trả endpoints cho client xử lý.

## Production Use Case

Internal Go API dùng DNS service name; gRPC client hiểu connection lifecycle/load distribution.

## Failure Scenarios

Selector sai không endpoints; session affinity làm hot pods; stale long-lived connections.

## How I would debug this in production

kubectl get service/endpointslices, DNS resolution và per-pod request rates.

## Trade-offs và When NOT to use

L4 connection balancing không tương đương L7 request balancing với multiplexing.

## Interview practice

Why might one gRPC pod receive most traffic? Long-lived connection multiplex nhiều RPCs.

## Key Takeaways

Service tạo stable discovery/routing tới matching endpoints; không quản business request load trực tiếp..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kubernetes.io/docs/concepts/)

## Applied drill

Chẩn đoán Service không nhận traffic theo thứ tự: selector match pods, endpoints ready, targetPort/listener binding, network policy, rồi DNS/client caching. Go server chỉ bind127.0.0.1 sẽ không nhận traffic tới pod IP; lab server trong examples cố ý local-only, deployment thật cần explicit bind policy. Không sửa app logic trước kiểm routing path.
