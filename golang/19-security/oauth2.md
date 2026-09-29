# OAuth2, OIDC và authorization code flow

## Concept và Mental Model

OAuth2 cấp delegated access; OIDC thêm identity layer. Flow choice phụ thuộc client type và threat model.

## How it works

Authorization Code + PKCE, exact redirect URI validation, state/nonce theo protocol và secure token storage. Client credentials cho machine identity, không thay end-user consent.

## Production Use Case

Backend validate tokens từ trusted issuer; refresh token rotation theo provider, secrets không nằm browser bundle.

## Failure Scenarios

Open redirect, stolen refresh token, confusing ID token với API access token, missing PKCE binding.

## How I would debug this in production

Review redirect registration, scopes/audience, callback correlation và token lifecycle; dùng provider-supported library.

## Trade-offs và When NOT to use

Không tự viết OAuth server chỉ để interview demo; contract/provider security updates phải theo docs.

## Interview practice

Why should an API not accept any ID token as an access token? Audience/purpose và validation contract khác nhau.

## Key Takeaways

OAuth2 cấp delegated access; OIDC thêm identity layer.


## See also

- [API security theo trust boundaries](../07-api-design/api-security.md)
- [HTTP client reuse và response ownership](../06-http-backend/http-client.md)

## Nguồn đối chiếu

- [Tài liệu chính thức](https://www.rfc-editor.org/rfc/rfc9700.html)
