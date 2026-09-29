# Multi-stage builds

## Concept và Mental Model

Build stage chứa compiler; runtime stage chỉ chứa binary và assets cần thiết.

## How it works

Copy go.mod/go.sum trước để cache dependencies; build target GOOS/GOARCH rõ; pin base image digest trong deployment workflow thực.

## Production Use Case

Pure Go service compile trong builder rồi copy binary + CA certs vào minimal runtime.

## Failure Scenarios

Cache layer giữ secrets do COPY; architecture mismatch; builder libs thiếu runtime khi cgo.

## How I would debug this in production

docker history/image inspect, file/ldd tương ứng platform, run non-root smoke test.

## Trade-offs và When NOT to use

Không đưa token vào ARG/layer; dùng build secret mechanism khi private modules cần credentials.

## Interview practice

What must accompany a Go binary in a minimal image? Depends on cgo, CA roots, timezone/assets và config.

## Key Takeaways

Build stage chứa compiler; runtime stage chỉ chứa binary và assets cần thiết..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://docs.docker.com/build/building/multi-stage/)
