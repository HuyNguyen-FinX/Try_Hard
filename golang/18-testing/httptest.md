# httptest: recorder versus server

## Concept và Mental Model

ResponseRecorder test handler behavior in-process; httptest.Server tạo real HTTP stack cho client/protocol tests.

## How it works

Recorder không mô phỏng TCP reuse/TLS/HTTP2; server + client + httptrace kiểm connection behavior. Close server/client idle conns sau test.

## Production Use Case

Examples test body limits, canceled request và HTTP/1 reuse bằng GotConn.Reused.

## Failure Scenarios

Assert pooling với recorder không có socket; forget response body close làm server.Close chờ.

## How I would debug this in production

Run -race và cancellation scenarios; server errors phải report có owner.

## Trade-offs và When NOT to use

Unit handler tests rẻ hơn real server; chọn theo câu hỏi cần xác minh.

## Interview practice

When is ResponseRecorder insufficient? Khi test connection reuse, TLS hoặc network cancellation.

## Key Takeaways

ResponseRecorder test handler behavior in-process; httptest.Server tạo real HTTP stack cho client/protocol tests..


## See also

- [README](../examples/README.md)
- [Race condition versus data race](../04-concurrency/race-condition.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://pkg.go.dev/testing)

## Applied drill

TestFetchReusesConnection dùng real server và GotConn.Reused ở request thứ hai sau đọc body đầy đủ. Nếu đổi sang Recorder, test không có TCP/Transport pool nên không còn kiểm yêu cầu này. Test oversized body phải trả error mà vẫn Close; test canceled ctx dùng errors.Is để không phụ thuộc wrapped message text. Local socket permission là requirement môi trường, không bug business logic.
