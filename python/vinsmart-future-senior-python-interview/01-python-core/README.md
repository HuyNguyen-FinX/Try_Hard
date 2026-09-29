# Python Core

Module này được học theo **Why → How → Internals → Flow → Failure → Trade-off → Production**. Không đọc alphabet; đi theo dependency dưới đây và tự vẽ lại diagram trước khi xem.

## Learning order

[Python Memory Model](python-memory-model.md) → [Gc Reference Counting](gc-reference-counting.md) → [Mutable Immutable](mutable-immutable.md) → [Generators Iterators](generators-iterators.md) → [Context Manager](context-manager.md)

## Must know

- [Python Memory Model](python-memory-model.md)
- [Gc Reference Counting](gc-reference-counting.md)
- [Mutable Immutable](mutable-immutable.md)
- [Generators Iterators](generators-iterators.md)
- [Context Manager](context-manager.md)

## Nice to know / second pass

- [Shallow Vs Deep Copy](shallow-vs-deep-copy.md)
- [Decorators](decorators.md)
- [Dunder Methods](dunder-methods.md)
- [Descriptors](descriptors.md)
- [Closures](closures.md)
- [Typing](typing.md)
- [Common Interview Questions](common-interview-questions.md)

## Recommended exercises

1. Giải thích mỗi Must-know topic trong 2 phút, không nhìn note; interviewer hỏi “why?” ít nhất ba lần.
2. Vẽ request/data/failure flow từ trí nhớ và đánh dấu source of truth, queue, timeout, retry, metric.
3. Chọn một production incident liên quan **Python Core**, trình bày mitigation trước root cause và long-term prevention.
4. Load/fault test một assumption: bottleneck, duplicate, stale state hoặc dependency outage.

## All topics

- [Python Memory Model](python-memory-model.md)
- [Gc Reference Counting](gc-reference-counting.md)
- [Mutable Immutable](mutable-immutable.md)
- [Shallow Vs Deep Copy](shallow-vs-deep-copy.md)
- [Decorators](decorators.md)
- [Generators Iterators](generators-iterators.md)
- [Context Manager](context-manager.md)
- [Dunder Methods](dunder-methods.md)
- [Descriptors](descriptors.md)
- [Closures](closures.md)
- [Typing](typing.md)
- [Common Interview Questions](common-interview-questions.md)

[← Main Dashboard](../README.md)
