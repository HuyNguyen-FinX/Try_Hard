# Unit testing business contracts

## Concept và Mental Model

Unit test giữ invariant và edge cases của function/package, không mirror từng line implementation.

## How it works

Arrange inputs/dependencies explicit, deterministic clock/randomness khi cần; assert observable result/error classification. Test cleanup bằng done signals.

## Production Use Case

Reserve inventory reject negative/oversell và preserve count on failure.

## Failure Scenarios

Tests chỉ happy path; sleep để chờ G; assert exact wrapped error string dễ brittle.

## How I would debug this in production

Run targeted test, go test ./..., -race cho concurrency; isolate shared globals.

## Trade-offs và When NOT to use

Không mock mọi function; pure domain logic dùng real values.

## Interview practice

What is a useful unit-test boundary? Observable behavior với invariant rõ.

## Key Takeaways

Unit test giữ invariant và edge cases của function/package, không mirror từng line implementation..


## See also

- [README](../examples/README.md)
- [Race condition versus data race](../04-concurrency/race-condition.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/testing)

## Applied drill

TestPoolCancellation dùng started channels để biết hai workers đã thực sự vào function rồi cancel. Done/error channel với timeout chỉ là failure bound, không là synchronization sleep. Sau RunPool return, active count phải0, chứng minh join. Test missing close trên input kèm worker error kiểm fail-fast siblings vẫn thoát; đây là invariant khó hơn chỉ count successful jobs.
