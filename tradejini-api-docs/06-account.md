# Account

User profile and session management endpoints.

## Details

`GET /api/account/details`

to fetch the primary user details like name, allowed products and segments

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X GET "https://example.com/api/account/details" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"userId": "JNDEMO01", "userName": "Demo User", "mobile": "9876543210", "email": "demo@example.com", "pan": "ABCDE1234F", "dpId": "IN123456", "bankDetails": [{"bankName": "HDFC Bank", "accNo": "XXXX1234", "ifsc": "HDFC0001234"}], "dpIds": ["IN123456"], "products": ["mis", "cnc", "nrml"], "segments": ["NSE", "BSE", "NFO"]}` |
| `d.userId` | `string` |  |
| `d.userName` | `string` |  |
| `d.mobile` | `string` |  |
| `d.email` | `string` |  |
| `d.pan` | `string` |  |
| `d.dpId` | `string` |  |
| `d.bankDetails` | `array<object>` |  |
| `d.bankDetails[].bankName` | `string` |  |
| `d.bankDetails[].accNo` | `string` |  |
| `d.bankDetails[].ifsc` | `string` |  |
| `d.dpIds` | `array<string>` |  |
| `d.products` | `array<string>` |  |
| `d.segments` | `array<string>` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "userId": "JNDEMO01",
    "userName": "Demo User",
    "mobile": "9876543210",
    "email": "demo@example.com",
    "pan": "ABCDE1234F",
    "dpId": "IN123456",
    "bankDetails": [
      {
        "bankName": "HDFC Bank",
        "accNo": "XXXX1234",
        "ifsc": "HDFC0001234"
      }
    ],
    "dpIds": [
      "IN123456"
    ],
    "products": [
      "mis",
      "cnc",
      "nrml"
    ],
    "segments": [
      "NSE",
      "BSE",
      "NFO"
    ]
  }
}
```

#### 401 Unauthorized

Unauthorized — one of: (1) invalid or expired access token — tokens expire after 24 hours, re-authenticate to get a new one; (2) `Authorization` header missing or malformed — use format `Bearer <api_key>:<access_token>`.

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. Values: `Unauthorized` |

**Example**

```json
{
  "s": "error",
  "msg": "Unauthorized"
}
```

#### 429 Too Many Requests

Too Many Requests — rate limit exceeded. General API: 10 req/sec per auth token (400 req/min).

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message indicating the rate limit was exceeded. |

**Example**

```json
{
  "s": "error",
  "msg": "Too many requests"
}
```

#### 500 Internal Server Error

Internal Server Error — retry with backoff; contact support if it persists.

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. |

**Example**

```json
{
  "s": "error",
  "msg": "Internal server error"
}
```

---

## Logout

`POST /api/account/logout`

to logout the user and to clear all authorization tokens

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X POST "https://example.com/api/account/logout" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "Success"}` |
| `d.msg` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "Logged out successfully"
  }
}
```

#### 400 Bad Request

Bad Request

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message describing which field failed validation or why the request was rejected. Values: `Internal Error occurred. Kindly try again.`, `Input validation failed. Kindly check your input contains required fields for the request` |

**Example**

```json
{
  "s": "error",
  "msg": "Input validation failed. Kindly check your input contains required fields for the request"
}
```

#### 401 Unauthorized

Unauthorized — one of: (1) invalid or expired access token — tokens expire after 24 hours, re-authenticate to get a new one; (2) `Authorization` header missing or malformed — use format `Bearer <api_key>:<access_token>`.

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. Values: `Unauthorized` |

**Example**

```json
{
  "s": "error",
  "msg": "Unauthorized"
}
```

#### 429 Too Many Requests

Too Many Requests — rate limit exceeded. General API: 10 req/sec per auth token (400 req/min).

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message indicating the rate limit was exceeded. |

**Example**

```json
{
  "s": "error",
  "msg": "Too many requests"
}
```

#### 500 Internal Server Error

Internal Server Error — retry with backoff; contact support if it persists.

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. |

**Example**

```json
{
  "s": "error",
  "msg": "Internal server error"
}
```
