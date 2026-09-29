# Explicit dependency injection

## Concept và Mental Model

Go constructor wiring làm dependency và lifecycle nhìn thấy tại startup.

## How it works

Main tạo config, logger, pool, clients, service, handlers; shutdown theo thứ tự ngược dependency use. Small interface chỉ ở boundary cần test/substitution.

## Production Use Case

NewService(store, clock) cho test deterministic time.

## Failure Scenarios

Global DB làm test tranh chấp; reflection container lỗi runtime; dependency optional mơ hồ typed nil.

## How I would debug this in production

Compile-time interface assertions và startup validation; tests explicit fake dependencies.

## Trade-offs và When NOT to use

Manual DI dễ đọc cho đa số services; generator có ích khi graph thật lớn.

## Interview practice

When is returning an interface reasonable? Khi public abstraction cố ý che nhiều concrete implementations.

## Key Takeaways

Go constructor wiring làm dependency và lifecycle nhìn thấy tại startup..


## See also

- [Interfaces: behavior, representation và typed nil](../01-go-core/interfaces.md)
- [Transactions và short critical sections](../08-database/transactions.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/modules/layout)

## Applied drill

Wiring order minh họa: load validated config→logger→DB pool→provider client→payment service→HTTP handler. Shutdown đảo quan hệ sử dụng: stop/drain handlers và workers trước close DB/client. Constructor không nên âm thầm start goroutine mà không trả owner có Close/Wait contract. Unit tests inject clock/fake provider, integration tests giữ adapter thật.
