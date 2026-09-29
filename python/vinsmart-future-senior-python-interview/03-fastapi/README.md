# FastAPI

Module này được học theo **Why → How → Internals → Flow → Failure → Trade-off → Production**. Không đọc alphabet; đi theo dependency dưới đây và tự vẽ lại diagram trước khi xem.

## Learning order

[Architecture](architecture.md) → [Request Lifecycle](request-lifecycle.md) → [Sync Vs Async Endpoint](sync-vs-async-endpoint.md) → [Dependency Injection](dependency-injection.md) → [Performance](performance.md)

## Must know

- [Architecture](architecture.md)
- [Request Lifecycle](request-lifecycle.md)
- [Sync Vs Async Endpoint](sync-vs-async-endpoint.md)
- [Dependency Injection](dependency-injection.md)
- [Performance](performance.md)

## Nice to know / second pass

- [Middleware](middleware.md)
- [Validation Pydantic](validation-pydantic.md)
- [Authentication](authentication.md)
- [Background Task](background-task.md)
- [Websocket](websocket.md)
- [Error Handling](error-handling.md)
- [Production Best Practices](production-best-practices.md)

## Recommended exercises

1. Giải thích mỗi Must-know topic trong 2 phút, không nhìn note; interviewer hỏi “why?” ít nhất ba lần.
2. Vẽ request/data/failure flow từ trí nhớ và đánh dấu source of truth, queue, timeout, retry, metric.
3. Chọn một production incident liên quan **FastAPI**, trình bày mitigation trước root cause và long-term prevention.
4. Load/fault test một assumption: bottleneck, duplicate, stale state hoặc dependency outage.

## All topics

- [Architecture](architecture.md)
- [Request Lifecycle](request-lifecycle.md)
- [Sync Vs Async Endpoint](sync-vs-async-endpoint.md)
- [Dependency Injection](dependency-injection.md)
- [Middleware](middleware.md)
- [Validation Pydantic](validation-pydantic.md)
- [Authentication](authentication.md)
- [Background Task](background-task.md)
- [Websocket](websocket.md)
- [Error Handling](error-handling.md)
- [Performance](performance.md)
- [Production Best Practices](production-best-practices.md)

[← Main Dashboard](../README.md)
