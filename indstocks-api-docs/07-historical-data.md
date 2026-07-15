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
| 1 Second | `1second` | 1 Day |
| 1 Minute | `1minute` | 7 Days |
| 1 Hour | `60minute` | 14 Days |
| 1 Day | `1day` | 1 Year |
| 1 Week | `1week` | 1 Year |
| 1 Month | `1month` | 1 Year |

### Request

```bash
curl 'https://api.indstocks.com/market/historical/1minute?scrip-codes=NSE_3045&start_time=1750055540000&end_time=1750141940000' \
  --header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
  "status": "success",
  "data": {
    "candles": [
      [1678886400000, 2500.00, 2501.50, 2499.50, 2501.00, 500],
      [1678886460000, 2501.00, 2502.00, 2500.50, 2501.80, 650]
    ]
  }
}
```

Each candle is an array in the order:

```
[ timestamp, open, high, low, close, volume ]
```

| Index | Field | Description |
|-------|-------|-------------|
| 0 | `timestamp` | Candle start time, Unix epoch milliseconds (IST) |
| 1 | `open` | Opening price |
| 2 | `high` | Highest price |
| 3 | `low` | Lowest price |
| 4 | `close` | Closing price |
| 5 | `volume` | Traded volume |

> **Note:** All timestamps are in **IST** and expressed in Unix epoch **milliseconds**. Keep
> each request within the max range for the chosen interval and paginate over time windows for
> longer histories.
