# Integration testing boundaries thật

## Concept và Mental Model

Integration test xác nhận driver/protocol/schema behavior không thể suy từ fake.

## How it works

Use isolated DB/schema, migrations đúng version, deterministic fixtures và cleanup; external dependency setup có timeout.

## Production Use Case

Test unique-key concurrent insert, transaction rollback, query cancellation và pool slot release.

## Failure Scenarios

Shared database làm tests flaky; sleeping chờ broker; cleanup bỏ namespace.

## How I would debug this in production

Capture server logs/query states khi fail; test version matrix có chủ đích.

## Trade-offs và When NOT to use

Không gọi compile test là integration test; ghi rõ dependency nào thực sự chạy.

## Interview practice

Which behavior requires a real PostgreSQL test? Isolation/locks, SQL types/plans và driver cancel semantics.

## Key Takeaways

Integration test xác nhận driver/protocol/schema behavior không thể suy từ fake..


## See also

- [README](../examples/README.md)
- [Race condition versus data race](../04-concurrency/race-condition.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/testing)

## Applied drill

Transaction test có hai concurrent sessions reserve cùng last inventory item; expected total successful reservations1 và stock không âm. Sau cancel long query, query nhẹ từ cùng limited pool phải acquire được để chứng minh release. Những kiểm tra này cần PostgreSQL/driver thật; stdlib example compile pass không đủ bằng chứng. Record database/driver versions và migrated schema.
