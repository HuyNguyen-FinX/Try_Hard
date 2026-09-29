# Defer: evaluation, LIFO và cleanup

## Concept và Mental Model

Defer đăng ký call chạy khi function return hoặc unwind panic; không chạy sau os.Exit.

## How it works

Receiver và arguments được evaluate lúc đăng ký; closure có thể đọc biến tại thời điểm chạy. Defers chạy LIFO; named return đã được gán trước defer nên defer có thể đổi kết quả.

## Production Use Case

Acquire rồi ngay lập tức defer release sau khi kiểm tra err. Với loop mở nhiều files, tách iteration thành function để close từng file sớm.

## Failure Scenarios

defer trong loop giữ hàng nghìn FD tới cuối function; defer đặt trước kiểm tra err có thể gọi Close trên nil.

## How I would debug this in production

Theo dõi open FD, xem lifetime function và lỗi cleanup; benchmark trước khi bỏ defer vì compiler tối ưu nhiều trường hợp.

## Trade-offs và When NOT to use

Defer làm cleanup dễ review; explicit release hữu ích khi lifetime ngắn hơn function.

## Interview practice

What does defer fmt.Println(x) capture compared with a closure? Đối chiếu argument evaluation và biến capture.

## Key Takeaways

Defer đăng ký call chạy khi function return hoặc unwind panic; không chạy sau os.Exit..


## See also

- [Interfaces: behavior, representation và typed nil](interfaces.md)
- [Error handling và error chains](errors.md)
- [unit-testing](../18-testing/unit-testing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)

## Code traps: dự đoán trước khi chạy

Chương trình độc lập:

```go
package main
import "fmt"
func result() (n int) {
    defer func() { n++ }()
    return 4
}
func main() {
    x := 1
    defer fmt.Println("argument", x)
    defer func() { fmt.Println("closure", x) }()
    x = 2
    fmt.Println(result())
}
```

Output: `5`, rồi `closure 2`, rồi `argument 1`. Return expression gán named result trước defer; closure sửa result. Argument x cho Println evaluate lúc defer đăng ký; closure đọc x lúc exit. LIFO quyết định closure chạy trước deferred Println.

Resource loop: gọi helper cho mỗi file để `defer file.Close()` chạy cuối iteration helper. Đặt defer trong outer function chỉ Close tất cả ở outer return; với nhiều files sẽ giữ FD không cần thiết. Cleanup error phải return/join/log theo policy, không bỏ qua. Defer không chạy khi process bị kill hay os.Exit. Compiler có open-coded defer optimization ở nhiều cases; benchmark trên toolchain thật trước rewrite cleanup.

[Executable examples](../examples/core_test.go) kiểm tra argument capture và named return.
