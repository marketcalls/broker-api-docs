# Authentication

> Source: https://groww.in/trade-api/docs/curl

Groww documents three ways to obtain an API access token: a token generated in the Groww account interface, an API key and secret approval flow, and an API key with a TOTP code. API calls use the resulting token as a Bearer token in the `Authorization` header.

## Access token from Groww

The documented UI flow is to log in to Groww, open the profile settings, choose **Trading APIs**, and generate an **Access Token**. Groww says this token expires daily at 6:00 AM. Tokens can be created, revoked, and managed from the Trading APIs page.

Example use:

```bash
curl -X GET 'https://api.groww.in/v1/order/detail/{groww_order_id}?segment=CASH' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

## API key and secret approval flow

Groww's flow uses an API key and secret generated from the Groww Cloud API Keys page and requires daily approval there. The access token endpoint is `POST https://api.groww.in/v1/token/api/access`.

The checksum is the SHA-256 hash of the API secret concatenated with the latest epoch timestamp in seconds. Groww says the timestamp is valid for 10 minutes and the same timestamp must be sent in the request.

```bash
curl -X POST 'https://api.groww.in/v1/token/api/access' \
  -H 'Authorization: Bearer {USER_API_KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "key_type": "approval",
    "checksum": "{SHA256_CHECKSUM}",
    "timestamp": "{EPOCH_SECONDS}"
  }'
```

| Field | Type | Description | Required |
|---|---|---|---|
| `key_type` | string | `approval` | Yes |
| `checksum` | string | SHA-256 checksum/signature | Yes |
| `timestamp` | string | Epoch seconds (10 digits) | Yes |

Example checksum generation in Python:

```python
import hashlib

def generate_checksum(secret: str, timestamp: str) -> str:
    return hashlib.sha256((secret + timestamp).encode("utf-8")).hexdigest()
```

## API key and TOTP flow

This flow uses an API key and a TOTP code produced by a third-party authenticator app. Groww says daily approval on its API Keys page is required. It uses the same token endpoint:

```bash
curl -X POST 'https://api.groww.in/v1/token/api/access' \
  -H 'Authorization: Bearer {USER_API_KEY}' \
  -H 'Content-Type: application/json' \
  -d '{
    "key_type": "totp",
    "totp": "{TOTP_CODE}"
  }'
```

| Field | Type | Description | Required |
|---|---|---|---|
| `key_type` | string | `totp` | Yes |
| `totp` | string | TOTP code from the authenticator app | Yes |

## Token response

The documented example response contains:

```json
{
  "token": "{ACCESS_TOKEN}",
  "tokenRefId": "ref-123",
  "sessionName": "my-session",
  "expiry": "2024-07-01T12:34:56",
  "isActive": true
}
```

The fields are the generated token, token reference ID, session name, expiry date-time, and active status. Use the `token` value in API request headers as `Authorization: Bearer {ACCESS_TOKEN}`.

## Notes

- The token generation endpoint has a documented limit of 150 requests per 24 hours, in addition to the authentication rate limits described in [01-introduction.md](01-introduction.md).
- Groww's documentation says to use `key_type: "approval"` for the API key and secret flow and `key_type: "totp"` for the API key and TOTP flow.
- Groww states that API request headers are mandatory. See [01-introduction.md](01-introduction.md) for the standard headers.

## Official source

- [Groww Introduction and Authentication](https://groww.in/trade-api/docs/curl)
