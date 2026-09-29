# Go core interview drills

Mỗi bài làm15 phút: dự đoán behavior, giải thích ownership/type/lifetime và đưa một regression test.

1. **Why does append sometimes mutate caller-visible data?** Vẽ hai headers chung array; chạy với cap còn/thừa khác nhau. [Slices](arrays-slices.md).
2. **Can an interface be non-nil while holding a nil pointer?** Nêu type/value pair và error-constructor trap. [Interfaces](interfaces.md).
3. **Can two independent map keys be written concurrently safely?** Metadata/growth vẫn shared; bảo vệ invariant bằng lock. [Maps](maps.md).
4. **What changes when a receiver changes from T to *T?** Method set, mutation, nil và copy semantics. [Methods](methods.md).
5. **Does returning a pointer always allocate?** Inlining và escape analysis tại caller quyết định. [Escape](../02-memory-runtime/escape-analysis.md).
6. **What will deferred argument and closure prints observe?** Argument capture lúc đăng ký khác closure đọc biến lúc exit; LIFO. [Defer](defer.md).
7. **Can recover resume at the panicking instruction?** Không; recover boundary return sau unwind. [Panic](panic-recover.md).
8. **How should callers classify a wrapped domain error?** Is/As với %w, tránh compare strings. [Errors](errors.md).
9. **Why can len disagree with visible Unicode characters?** Byte/rune/grapheme có đơn vị khác nhau. [Strings](strings-runes-bytes.md).
10. **When should a generic function replace an interface?** Thuật toán trên type set khác runtime behavior substitution. [Generics](generics.md).

Chấm0–4/câu: definition, mechanism, edge case, production implication. Full answers và follow-ups ở từng deep dive; [100-question bank](../23-mock-interview/top-100-golang-questions.md) có đáp án đóng/mở.
