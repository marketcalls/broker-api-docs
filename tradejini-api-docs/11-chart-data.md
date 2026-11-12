# Chart Data

Historical OHLCV candle data.

## Interval Chart

`GET /api/mkt-data/chart/interval-data`

This service can be used to fetch the open, high, low, close and volume values (chart data points) of a given symbol.

Also it provides sum up volume of last tick to calculate the current minute volume.

For derivative symbol, an additional field Open Interest Change for that particular minute will be added in same response array.

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `from` | `integer (int64)` | Yes | Enter starting datetime(eg: 2023-06-01 9:15:00 ) in timestamp(eg: 1685591100) |
| `to` | `integer (int64)` | Yes | Enter ending datetime(eg: 2023-06-01 13:12:34) in timestamp(eg: 1685605354) |
| `interval` | `string` | Yes | Enter time interval in minutes. Values: `1` |
| `id` | `string` | Yes | Enter Symbol id. Example: `EQT_RELIANCE_EQ_NSE` |

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X GET "https://example.com/api/mkt-data/chart/interval-data?from=1685591100&to=1685605354&interval=1&id=EQT_RELIANCE_EQ_NSE" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

successful response

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"bars": [{"time": 1705290000, "open": 2445, "high": 2462.5, "low": 2438.75, "close": 2450.75, "volume": 1234567}, {"time": 1705293600, "open": 2451, "high": 2468, "low": 2447, "close": 2463.25, "volume": 987654}], "sumUpVolume": true}` |
| `d.bars` | `array<array<object>>` |  |
| `d.bars[][].time` | `integer (int64)` |  |
| `d.bars[][].open` | `number (double)` |  |
| `d.bars[][].high` | `number (double)` |  |
| `d.bars[][].low` | `number (double)` |  |
| `d.bars[][].close` | `number (double)` |  |
| `d.bars[][].volume` | `integer (int64)` |  |
| `d.bars[][].minuteOi` | `integer (int64)` |  |
| `d.sumUpVolume` | `integer (int64)` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "bars": [
      {
        "time": 1705290000,
        "open": 2445,
        "high": 2462.5,
        "low": 2438.75,
        "close": 2450.75,
        "volume": 1234567
      },
      {
        "time": 1705293600,
        "open": 2451,
        "high": 2468,
        "low": 2447,
        "close": 2463.25,
        "volume": 987654
      }
    ],
    "sumUpVolume": true
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
