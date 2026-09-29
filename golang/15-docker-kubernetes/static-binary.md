# Static binaries và cgo

## Concept và Mental Model

Go binary có thể tự chứa nhiều runtime support, nhưng static linkage phụ thuộc build/dependencies.

## How it works

CGO_ENABLED=0 cho pure-Go-compatible build thường tránh libc dynamic deps; cgo libraries có thể cần native runtime. DNS/user lookup behavior có thể khác.

## Production Use Case

Cross-compile linux/arm64 cho platform deployment, test target image thực.

## Failure Scenarios

Giả định mọi Go binary static; executable not found do missing dynamic loader dù file tồn tại.

## How I would debug this in production

Inspect binary format/linkage trên đúng OS; compare DNS/TLS behavior trong image.

## Trade-offs và When NOT to use

Disable cgo không là universal optimization; dependency/native performance có thể cần cgo.

## Interview practice

Why might a present binary report no such file? Dynamic interpreter/loader không tồn tại trong image.

## Key Takeaways

Go binary có thể tự chứa nhiều runtime support, nhưng static linkage phụ thuộc build/dependencies..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://kubernetes.io/docs/concepts/)
