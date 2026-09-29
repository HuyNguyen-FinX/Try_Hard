# PostgreSQL

Module này được học theo **Why → How → Internals → Flow → Failure → Trade-off → Production**. Không đọc alphabet; đi theo dependency dưới đây và tự vẽ lại diagram trước khi xem.

## Learning order

[Index](index.md) → [Explain Analyze](explain-analyze.md) → [Transaction](transaction.md) → [Isolation Level](isolation-level.md) → [PostgreSQL MVCC](mvcc.md) → [Connection Pooling](connection-pooling.md)

## Must know

- [Index](index.md)
- [Explain Analyze](explain-analyze.md)
- [Transaction](transaction.md)
- [Isolation Level](isolation-level.md)
- [PostgreSQL MVCC](mvcc.md)
- [Connection Pooling](connection-pooling.md)

## Nice to know / second pass

- [Database Fundamentals](database-fundamentals.md)
- [PostgreSQL Index Types: B-tree, Hash, GIN, GiST, BRIN](btree-hash-gin-gist-brin.md)
- [Query Optimization](query-optimization.md)
- [Locks](locks.md)
- [Deadlock](deadlock.md)
- [Partitioning](partitioning.md)
- [Replication](replication.md)
- [Large Table Design](large-table-design.md)

## Recommended exercises

1. Giải thích mỗi Must-know topic trong 2 phút, không nhìn note; interviewer hỏi “why?” ít nhất ba lần.
2. Vẽ request/data/failure flow từ trí nhớ và đánh dấu source of truth, queue, timeout, retry, metric.
3. Chọn một production incident liên quan **PostgreSQL**, trình bày mitigation trước root cause và long-term prevention.
4. Load/fault test một assumption: bottleneck, duplicate, stale state hoặc dependency outage.

## All topics

- [Database Fundamentals](database-fundamentals.md)
- [Index](index.md)
- [PostgreSQL Index Types: B-tree, Hash, GIN, GiST, BRIN](btree-hash-gin-gist-brin.md)
- [Explain Analyze](explain-analyze.md)
- [Query Optimization](query-optimization.md)
- [Transaction](transaction.md)
- [Isolation Level](isolation-level.md)
- [PostgreSQL MVCC](mvcc.md)
- [Locks](locks.md)
- [Deadlock](deadlock.md)
- [Partitioning](partitioning.md)
- [Replication](replication.md)
- [Connection Pooling](connection-pooling.md)
- [Large Table Design](large-table-design.md)
- [SQL Interview](sql-interview.md)

[← Main Dashboard](../README.md)
