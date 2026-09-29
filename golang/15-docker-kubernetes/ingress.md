# Ingress và proxy boundary

## Concept và Mental Model

Ingress/controller xử lý HTTP routing/TLS theo platform; resource không tự hoạt động khi không có controller.

## How it works

Align request/body/idle timeout, max body size và trusted forwarded headers giữa proxy và Go server. gRPC/WebSocket cần protocol support cụ thể.

## Production Use Case

Public API terminate TLS tại trusted edge rồi internal TLS theo threat model.

## Failure Scenarios

Proxy timeout trả 504 trong khi backend vẫn chạy; wrong X-Forwarded-For trust bypass rate limit.

## How I would debug this in production

Compare edge access logs với service trace, status và request duration.

## Trade-offs và When NOT to use

Gateway API/controller options phụ thuộc deployment; không hardcode annotation như chuẩn chung.

## Interview practice

Why can the client see 504 while the service logs success? Edge deadline hết trước backend completion.

## Key Takeaways

Ingress/controller xử lý HTTP routing/TLS theo platform; resource không tự hoạt động khi không có controller..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kubernetes.io/docs/concepts/)
