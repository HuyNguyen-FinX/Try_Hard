# gRPC service boundaries

## Concept và Mental Model

Reuse ClientConn và generated clients; deadline/metadata/status là phần API contract.

## How it works

Unary/stream interceptors auth/trace, bounded message size và stream concurrency; validate metadata chỉ từ trusted identity.

## Production Use Case

Internal inventory RPC có per-call deadline và resource-specific authorization.

## Failure Scenarios

Stream không CloseSend/receive completion, context bị bỏ, retry partial stream thiếu resume protocol.

## How I would debug this in production

RPC method/status metrics, active streams, flow-control waits và load distribution.

## Trade-offs và When NOT to use

Không assume HTTP/2 làm mọi load balancer aware; kiểm tra proxy settings.

## Interview practice

How should you retry a partially consumed stream? Cần application checkpoint/resume, không replay mù.

## Key Takeaways

Reuse ClientConn và generated clients; deadline/metadata/status là phần API contract..


## See also

- [Microservices: independent ownership có chi phí](../11-software-architecture/microservices.md)
- [Distributed failure matrix](../12-distributed-systems/failure-scenarios.md)
- [tracing](../17-observability/tracing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://grpc.io/docs/guides/)

## Applied drill

Test unary deadline với server chờ ctx.Done và verify goroutine hoàn tất. Với streaming, cố ý consumer chậm để observe Send block/flow control, rồi cancel và join sender. ClientConn reuse không đồng nghĩa một logical call không cần timeout. Metadata inbound không tự trusted: validate caller identity và allowlist forward fields trước call sang service tiếp theo.
