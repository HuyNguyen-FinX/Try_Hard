# Prepared statements và session scope

## Concept và Mental Model

Prepared statements tái sử dụng parse/plan; parameters tách data khỏi SQL syntax.

## How it works

database/sql Stmt có thể prepare trên nhiều underlying connections; driver/server cache và transaction pooling proxy có compatibility riêng. Close explicit Stmt khi owner kết thúc.

## Production Use Case

Hot fixed query nhiều calls; dynamic filters vẫn cần bounded query shapes.

## Failure Scenarios

Hàng nghìn query shapes phình cache; plan generic kém cho skew; proxy mode làm session assumptions sai.

## How I would debug this in production

So query plan, prepare rate, cache cardinality và proxy configuration; benchmark realistic parameter distribution.

## Trade-offs và When NOT to use

Không prepare mọi one-off query; parameterization vẫn cần dù không explicit Prepare.

## Interview practice

Can a prepared statement guarantee a good plan for every tenant? Không, data skew ảnh hưởng plan choice.

## Key Takeaways

Prepared statements tái sử dụng parse/plan; parameters tách data khỏi SQL syntax..


## See also

- [database/sql: pool handle, rows và transaction ownership](database-sql.md)
- [Database connection pool: 500 requests và 20 connections](database-sql-pool.md)
- [outbox-pattern](../12-distributed-systems/outbox-pattern.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/doc/database/)
