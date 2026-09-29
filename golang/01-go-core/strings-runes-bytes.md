# Strings, runes và bytes

## Concept và Mental Model

String là chuỗi byte immutable; UTF-8 phổ biến nhưng string có thể chứa byte không hợp lệ. Rune là Unicode code point, không phải grapheme.

## How it works

len(string) đếm byte; range decode rune và trả byte index; []rune đổi sang code points. Combining marks và emoji có thể cần nhiều rune cho một ký tự người dùng nhìn thấy.

## Production Use Case

Giới hạn upload bằng byte; giới hạn hiển thị dùng quy tắc Unicode phù hợp. Dùng strings.Builder cho xây chuỗi theo batch khi benchmark ủng hộ.

## Failure Scenarios

Cắt s[:n] giữa UTF-8 sequence; thuật toán sliding window dùng byte nhưng đề yêu cầu Unicode; log secret khi debug encoding.

## How I would debug this in production

Reproduce với tiếng Việt, combining marks và invalid UTF-8; xem allocation do conversions lặp lại.

## Trade-offs và When NOT to use

[]byte hợp protocol, rune hợp code points; grapheme segmentation cần thư viện phù hợp và version Unicode rõ.

## Interview practice

Why can len disagree with visible character count? Phân biệt byte, rune và grapheme.

## Key Takeaways

String là chuỗi byte immutable; UTF-8 phổ biến nhưng string có thể chứa byte không hợp lệ.


## See also

- [Interfaces: behavior, representation và typed nil](interfaces.md)
- [Error handling và error chains](errors.md)
- [unit-testing](../18-testing/unit-testing.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://go.dev/ref/spec)
