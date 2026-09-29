# Mutex: invariants, contention và lock ownership

**P0 · Must know**

## Concept và Mental Model

Mutex bảo vệ critical section mà nhiều goroutines không được thực hiện đồng thời. Khóa bảo vệ **invariant**, không phải tên biến; mọi access liên quan phải theo cùng protocol.

```mermaid
flowchart LR
    A[Reader or writer] --> L[Lock]
    L --> C[Read and update invariant]
    C --> U[Unlock]
    U --> N[Next successful Lock]
```

## Why, How và Internals

Zero value sync.Mutex dùng được. `Unlock` tạo synchronization với `Lock` thành công sau đó. Mutex không reentrant và không gắn ownership với G theo API; unlock từ G khác có thể hợp lệ nhưng thường làm protocol khó review. Không copy mutex sau first use; struct có mutex thường được dùng qua pointer. Runtime có spin/park và contention modes tùy release: không hứa fairness hay FIFO cho application.

Giữ lock ngắn, không gọi network/DB hoặc callback không kiểm soát khi đang giữ. Nếu phải đọc state rồi I/O rồi cập nhật, chụp version, unlock, làm I/O và revalidate dưới lock; không đơn giản bỏ lock rồi giả định invariant giữ nguyên. Với nhiều locks đặt global order và document.

## Code Example

```go
package main
import ("fmt"; "sync")
type Inventory struct { mu sync.Mutex; available int }
func (i *Inventory) Reserve(n int) bool {
    i.mu.Lock()
    defer i.mu.Unlock()
    if n <= 0 || i.available < n { return false }
    i.available -= n
    return true
}
func main() { i := &Inventory{available: 1}; fmt.Println(i.Reserve(1), i.Reserve(1)) }
```

Read-check-write cùng critical section tránh oversell trong process. Nhiều instances vẫn cần DB atomic update/transaction; mutex chỉ có phạm vi một process.

## Production Use Case

Cache local bảo vệ map + LRU list như một invariant. Không trả mutable pointer rồi mutate ngoài lock. Contention cao có thể shard theo key nhưng operation nhiều shards phải lock theo thứ tự.

## Failure Scenarios

Recursive call cố Lock lại cùng mutex; lock order đảo; copy lock bảo vệ cùng underlying map; callback dưới lock gọi ngược lại service; thêm RWMutex nhưng readers giữ lock lâu làm writer latency tăng.

## Trade-offs

| Option | Lợi ích | Hạn chế |
|---|---|---|
| Mutex | Invariant nhiều fields rõ | Serialization |
| RWMutex | Readers song song | Bookkeeping, writer latency |
| Sharded locks | Giảm contention theo key | Cross-shard invariants |
| Atomic | Operation nhỏ | Không thay transaction |

## Common Misconceptions

Mutex không tự bảo vệ state nếu có path bỏ qua. `TryLock` thất bại không tạo memory synchronization edge để đọc state an toàn. Data-race-free không chứng minh business invariant giữa nhiều processes.

## When NOT to use

Không giữ mutex suốt external I/O. Không lock chỉ để bảo vệ counter đơn giản nếu atomic contract đã đủ, nhưng tránh tối ưu khi chưa đo.

## How I would debug this in production

Bật mutex/block profiling với sampling có budget. Mutex profile chỉ ra stack liên quan contention thường tại unlock/holder path; block profile cho waiter blocking site. Vẽ lock graph từ stacks, kiểm tra hold duration và callbacks. Run race/vet cho missing lock/copylocks; load-test hot key để phân biệt skew với global contention.

## Key Takeaways

Một lock protocol bao trọn invariant. Đo hold time và contention trước khi chọn primitive phức tạp hơn.

## Interview Questions

### Basic / Mid — 10

1. What does a mutex protect?
2. Is its zero value usable?
3. Is Mutex reentrant?
4. Can it be copied after use?
5. What does Unlock synchronize with?
6. What is a critical section?
7. Can another goroutine unlock it?
8. What does TryLock return?
9. What is lock contention?
10. What is lock ordering?

### Senior — 10

1. Why is read-check-write one invariant?
2. How can returning a pointer bypass lock protection?
3. Why is network I/O under a lock dangerous?
4. How would you revalidate state after releasing a lock?
5. When can sharding help?
6. Why can RWMutex be slower?
7. What does a failed TryLock not guarantee?
8. How can callbacks cause deadlock?
9. Why does a local mutex not prevent cross-instance oversell?
10. How do mutex and block profiles differ?

### Production scenarios — 5

1. How would you diagnose a frozen cache?
2. Why did adding a lock fix races but hurt P99?
3. Why does a copied service struct race?
4. Why does one tenant monopolize a lock?
5. Why does an inventory remain oversold across pods?

### Senior Follow-ups — 5

1. Which invariant needs atomicity?
2. Which accesses participate?
3. Which lock order applies?
4. What is the longest hold path?
5. Which profile confirms the contention source?

Chuỗi follow-up: trả lời lần lượt 5 câu cuối; mỗi câu cần một invariant, bằng chứng runtime hoặc trade-off cụ thể.


## See also

- [rwmutex](rwmutex.md)
- [deadlock](deadlock.md)
- [mutex-profile](../16-performance/mutex-profile.md)

## Nguồn đối chiếu

- [sync.Mutex](https://pkg.go.dev/sync#Mutex)
