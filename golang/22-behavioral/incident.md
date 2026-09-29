# Behavioral incident story

## Concept và Mental Model

Incident story thể hiện judgment dưới áp lực và khả năng học sau recovery.

## How it works

STAR: symptom/impact, role, mitigation hypotheses, coordination, recovery verification, root cause và prevention owners.

## Production Use Case

Ví dụ giả định: traffic ổn nhưng P99 tăng, DB WaitDuration tăng; pause backfill rồi tìm long Tx và sửa query path.

## Failure Scenarios

Claim root cause từ correlation; thay nhiều thứ cùng lúc; quên thông báo impact hoặc verify backlog.

## How I would debug this in production

Tập kể5 phút, giữ timeline và kết quả thực; phân biệt điều biết lúc incident với điều biết sau.

## Trade-offs và When NOT to use

Speed mitigation và evidence preservation cần cân bằng theo severity.

## Interview practice

Tell me about a production outage you handled. Nêu decision/risk và lesson hệ thống, tránh blame.

## Key Takeaways

Incident story thể hiện judgment dưới áp lực và khả năng học sau recovery..


## See also

- [star-method](star-method.md)
- [full-mock-interview](../23-mock-interview/full-mock-interview.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://rework.withgoogle.com/intl/en/guides/hiring-use-structured-interviewing)
