# Protobuf và schema evolution

## Concept và Mental Model

Wire fields được nhận diện bằng field number; compatibility quan trọng hơn tên generated struct.

## How it works

Không reuse removed field numbers; reserve numbers/names. Additive fields thường dễ rollout hơn đổi type/semantics. Presence khác zero value, repeated/map có behavior riêng.

## Production Use Case

CI kiểm tra backward/forward compatibility và generate bằng pinned protoc/plugins.

## Failure Scenarios

Đổi field meaning không đổi number phá business semantics dù decode thành công; JSON gateway có rules khác binary wire.

## How I would debug this in production

Test old producer/new consumer và ngược lại; lưu fixtures versioned.

## Trade-offs và When NOT to use

Schema contract giảm ambiguity nhưng không thay validation/auth.

## Interview practice

Why reserve removed field numbers? Payload cũ không được diễn giải thành dữ liệu mới khác nghĩa.

## Key Takeaways

Wire fields được nhận diện bằng field number; compatibility quan trọng hơn tên generated struct..


## See also

- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)
- [idempotency](../12-distributed-systems/idempotency.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://protobuf.dev/programming-guides/proto3/)

## Contract example

Đoạn schema minh họa; cần protoc và Go plugin đã pin để generate, không được tuyên bố đã compile trong stdlib labs.

```proto
syntax = "proto3";
package inventory.v1;
option go_package = "example.com/shop/gen/inventory/v1;inventoryv1";
message GetItemRequest { string id = 1; }
message Item {
  string id = 1;
  int64 version = 2;
  optional string display_name = 3;
  reserved 4;
}
service Inventory {
  rpc GetItem(GetItemRequest) returns (Item);
}
```

Presence của display_name cho phép phân biệt omitted với empty theo generated API. Reserved4 ngăn reuse field number cũ. Semantic validation vẫn phải kiểm ID/authorization/version. [Protobuf language guide](https://protobuf.dev/programming-guides/proto3/).
