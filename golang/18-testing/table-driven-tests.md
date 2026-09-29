# Table-driven tests và subtests

## Concept và Mental Model

Cases là data, mỗi case có expected behavior riêng dễ mở rộng edge coverage.

## How it works

t.Run names mô tả scenario; t.Parallel chỉ khi fixtures không shared mutable. Loop variable capture semantics phụ thuộc module language version cho code cũ.

## Production Use Case

Cases nil/empty/max/invalid và errors.Is expected cause.

## Failure Scenarios

Parallel tests dùng same temp DB row; old loop capture bug; one failure hides remaining cases.

## How I would debug this in production

Run -shuffle=on -count=20 targeted suite khi nghi order dependence.

## Trade-offs và When NOT to use

Table quá nhiều logic branches khó đọc hơn tests riêng cho workflows khác nhau.

## Interview practice

When should a test table be split? Khi mỗi row cần setup/assertions khác bản chất.

## Key Takeaways

Cases là data, mỗi case có expected behavior riêng dễ mở rộng edge coverage..


## See also

- [README](../examples/README.md)
- [Race condition versus data race](../04-concurrency/race-condition.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/testing)

## Applied drill

Đặt cases LowerBound gồm nil, target trước first, equal duplicate, giữa values và sau last. Assert first matching index và partition invariant, không chỉ result ở typical input. Nếu t.Parallel, mỗi case phải có fixture riêng hoặc immutable; schema shared cần unique namespace. Module language version1.22+ thay loop variable capture semantics, nhưng data referenced bên trong case vẫn có thể shared.
