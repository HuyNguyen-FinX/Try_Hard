# SQLAlchemy

Module này được học theo **Why → How → Internals → Flow → Failure → Trade-off → Production**. Không đọc alphabet; đi theo dependency dưới đây và tự vẽ lại diagram trước khi xem.

## Learning order

[Session Lifecycle](session-lifecycle.md) → [Transaction](transaction.md) → [N Plus One](n-plus-one.md) → [Relationship Loading](relationship-loading.md) → [Async Sqlalchemy](async-sqlalchemy.md)

## Must know

- [Session Lifecycle](session-lifecycle.md)
- [Transaction](transaction.md)
- [N Plus One](n-plus-one.md)
- [Relationship Loading](relationship-loading.md)
- [Async Sqlalchemy](async-sqlalchemy.md)

## Nice to know / second pass

- [ORM Vs Raw SQL](orm-vs-raw-sql.md)
- [Performance](performance.md)

## Recommended exercises

1. Giải thích mỗi Must-know topic trong 2 phút, không nhìn note; interviewer hỏi “why?” ít nhất ba lần.
2. Vẽ request/data/failure flow từ trí nhớ và đánh dấu source of truth, queue, timeout, retry, metric.
3. Chọn một production incident liên quan **SQLAlchemy**, trình bày mitigation trước root cause và long-term prevention.
4. Load/fault test một assumption: bottleneck, duplicate, stale state hoặc dependency outage.

## All topics

- [ORM Vs Raw SQL](orm-vs-raw-sql.md)
- [Session Lifecycle](session-lifecycle.md)
- [Transaction](transaction.md)
- [N Plus One](n-plus-one.md)
- [Relationship Loading](relationship-loading.md)
- [Async Sqlalchemy](async-sqlalchemy.md)
- [Performance](performance.md)

[← Main Dashboard](../README.md)
