# Docker cho Go services

## Concept và Mental Model

Image đóng gói binary và runtime dependencies; container chia kernel với host, không phải VM riêng.

## How it works

Build reproducible bằng pinned toolchain/dependency checksums, non-root runtime user, exec-form ENTRYPOINT để signals tới process.

## Production Use Case

Một image API/worker dùng cùng source commit; inject config/secrets lúc deploy.

## Failure Scenarios

Missing CA certificates làm HTTPS fail; shell PID1 nuốt signals; timezone/native libs thiếu.

## How I would debug this in production

Inspect image metadata, UID, binary linkage và logs khi SIGTERM; smoke test outbound TLS.

## Trade-offs và When NOT to use

Minimal image giảm surface nhưng debug khó; giữ debug tooling qua workflow riêng.

## Interview practice

Why can a tiny image fail HTTPS calls? Trust store có thể không được copy vào runtime image.

## Key Takeaways

Image đóng gói binary và runtime dependencies; container chia kernel với host, không phải VM riêng..


## See also

- [Graceful shutdown và dependency order](../06-http-backend/graceful-shutdown.md)
- [GOMAXPROCS và container CPU](../03-goroutines-scheduler/gomaxprocs.md)
- [Garbage collection: live heap, pacing và memory budget](../02-memory-runtime/garbage-collector.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://docs.docker.com/guides/golang/)
