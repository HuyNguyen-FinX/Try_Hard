# Race detector workflow

## Concept và Mental Model

go test -race ./... instrument executed paths để phát hiện conflicting memory access thiếu synchronization.

## How it works

Report gồm access stacks và G creation; fix ownership/happens-before, rerun workload. Không phát hiện mọi distributed logical race.

## Production Use Case

Negative lab build tag racedemo phải fail; default suite phải pass race.

## Failure Scenarios

Empty coverage tạo false confidence; timing under instrumentation làm bug path biến đổi.

## How I would debug this in production

Exercise shared paths với realistic concurrency; inspect both stacks, run vet copylocks.

## Trade-offs và When NOT to use

Race overhead cao; staging/targeted canary cần budget; không substitute code reasoning.

## Interview practice

Does race-free mean duplicate-free? Không, idempotency và DB constraints xử lý tầng business.

## Key Takeaways

go test -race ./...


## See also

- [README](../examples/README.md)
- [Race condition versus data race](../04-concurrency/race-condition.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/testing)

## Applied drill

Negative example được tách bằng build tag racedemo. Lệnh `go test -race -tags racedemo -run TestIntentionalRace` phải nonzero và chứa DATA RACE; default `go test -race ./...` phải pass. Nhờ tách tag, một expected failure không làm suite thường luôn đỏ. Fix increment bằng atomic/lock rồi compare report, nhưng nhớ logical duplicate test vẫn riêng.
