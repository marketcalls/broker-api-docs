# Historical Data

> Source: https://api-docs.indstocks.com/historicalData/

Fetches time-series **OHLCV** (Open, High, Low, Close, Volume) candle data for trading
instruments.

## Get Historical Candles

**Endpoint:** `GET /market/historical/{interval}`

### Path Parameters

| Parameter | Description |
|-----------|-------------|
| `interval` | Candle timeframe (see supported values below) |

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `scrip-codes` | string | ✅ | Comma-separated `SEGMENT_TOKEN` identifiers (e.g., `NSE_3045,NFO_51011`) |
| `start_time` | int64 | ✅ | Start timestamp, Unix epoch **milliseconds** (inclusive) |
| `end_time` | int64 | ✅ | End timestamp, Unix epoch **milliseconds** (exclusive) |

### Supported Intervals & Max Fetch Ranges

| Interval | `{interval}` value | Max Range per Request |
|----------|--------------------|-----------------------|
| 1 Minute | `1minute` | 7 Days |
| 2 Minutes | `2minute` | 7 Days |
| 3 Minutes | `3minute` | 7 Days |
| 4 Minutes | `4minute` | 7 Days |
| 5 Minutes | `5minute` | 7 Days |
| 10 Minutes | `10minute` | 7 Days |
| 15 Minutes | `15minute` | 7 Days |
| 30 Minutes | `30minute` | 7 Days |
| 1 Hour | `60minute` | 14 Days |
| 2 Hours | `120minute` | 14 Days |
| 3 Hours | `180minute` | 14 Days |
| 4 Hours | `240minute` | 14 Days |
| 1 Day | `1day` | 1 Year |
| 1 Week | `1week` | 1 Year |
| 1 Month | `1month` | 1 Year |

> There is **no `1second` interval**. The finest granularity is `1minute`.

### Request

```bash
curl --location 'https://api.indstocks.com/market/historical/1minute?scrip-codes=NSE_3045&start_time=1750055540000&end_time=1750141940000' \
  --header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
  "success": true,
  "data": {
    "NSE_1594": {
      "candles": [
        { "ts": 1782877500, "o": 1007, "h": 1013.9, "l": 999.3, "c": 1000.4, "v": 2847163 },
        { "ts": 1782881100, "o": 1000.4, "h": 1002, "l": 996.7, "c": 999.6, "v": 1389042 }
      ]
    }
  }
}
```

> ⚠️ **This endpoint does not use the standard response envelope.** It returns
> `"success": true` rather than `"status": "success"` — see
> [API Conventions](03-conventions.md#standard-response-envelope). Errors from this endpoint
> use the matching `{"message": "...", "success": false}` shape.

`data` is keyed by **scrip code**, so a multi-instrument request returns one `candles` array
per instrument (they are not merged into a single series).

| Field | Description |
|-------|-------------|
| `ts` | Candle timestamp, Unix epoch **seconds** (IST) |
| `o` | Opening price |
| `h` | Highest price |
| `l` | Lowest price |
| `c` | Closing price |
| `v` | Traded volume |

> ⚠️ **Unit mismatch:** the `start_time` / `end_time` *query parameters* are epoch
> **milliseconds**, but the candle `ts` in the *response* is epoch **seconds**. Multiply
> `ts` by 1000 before comparing against your request window.

> **Note:** Keep each request within the max range for the chosen interval and paginate over
> time windows for longer histories.
