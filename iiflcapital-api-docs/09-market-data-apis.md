# Market Data APIs

Four REST endpoints for real-time and historical market data.

| Method | Endpoint | Processing Mode | Action |
| --- | --- | --- | --- |
| POST | `/marketdata/historicaldata` | Single | Historical candlestick data (OHLCV) for an instrument over a chosen time frame |
| POST | `/marketdata/marketquotes` | Single/Bulk | Real-time price/volume for selected instruments |
| POST | `/marketdata/marketdepth` | Single | Best buy/sell prices and quantities at each depth level |
| POST | `/marketdata/openinterest` | Single | Open interest for futures and options |

## Historical Candlestick Chart Data

`POST /marketdata/historicaldata`

**Headers:** `Authorization: Bearer <userSession>`

### Request

```json
{
  "exchange": "NSEEQ",
  "instrumentId": "1594",
  "interval": "1 minute",
  "fromDate": "19-Sep-2024",
  "toDate": "20-Sep-2024"
}
```

| Field | Description | Example Values |
| --- | --- | --- |
| `exchange`* | Exchange & segment | `NSEEQ`, `NSEFO`, `BSEEQ`, `BSEFO`, `NSECURR`, `BSECURR`, `MCXCOMM`, `NCDEXCOMM`, `NSECOMM`, `BSECOMM` |
| `instrumentId`* | Unique instrument identifier | `1594` |
| `interval`* | Candle interval | `1 minute`, `5 minutes`, `10 minutes`, `15 minutes`, `30 minutes`, `60 minutes`, `1 day`, `weekly`, `monthly` |
| `fromDate`* | Start date | `19-Sep-2024` |
| `toDate`* | End date | `20-Sep-2024` |

### Response

> The candle data is returned as a string, not native JSON — parse it accordingly.

```json
{
  "status": "Ok",
  "message": "Success",
  "result": [
    {
      "candles": [
        ["2024-11-11T09:15:00", 68.37, 68.7, 68.15, 68.18, 1494],
        ["2024-11-11T09:16:00", 295.0, 296.3, 293.75, 295.3, 11315876]
      ]
    }
  ]
}
```

Each candle is `[timestamp, open, high, low, close, volume]`.

---

## Market Quotes

`POST /marketdata/marketquotes`

**Headers:** `Authorization: Bearer <userSession>`

### Request

```json
[
  { "exchange": "NSEEQ", "instrumentId": "1594" },
  { "exchange": "NSEEQ", "instrumentId": "2885" }
]
```

### Response

```json
{
  "status": "Ok",
  "message": "Success",
  "result": [
    {
      "exchange": "NSEEQ", "instrumentId": 1594, "ltp": 1412.95, "lastTradedQuantity": 5,
      "averageTradedPrice": 1412.47, "tradedVolume": 7360198, "open": 1396, "high": 1421.75,
      "low": 1395.55, "close": 1389.65, "bestBidPrice": 2994.25, "bestBidQuantity": 4,
      "bestAskPrice": 2994.75, "bestAskQuantity": 13, "totalBidQuantity": 404715,
      "totalAskQuantity": 216809, "tickTimestamp": "19-Sep-2024 09:15:00"
    }
  ]
}
```

| Field | Description |
| --- | --- |
| `ltp` | Last traded price |
| `lastTradedQuantity` | Quantity of the last trade |
| `averageTradedPrice` | Session average traded price |
| `tradedVolume` | Total traded volume |
| `open` / `high` / `low` / `close` | Session OHLC |
| `bestBidPrice` / `bestBidQuantity` | Best buy price / quantity |
| `bestAskPrice` / `bestAskQuantity` | Best sell price / quantity |
| `totalBidQuantity` / `totalAskQuantity` | Total buy / sell quantity |
| `tickTimestamp` | Timestamp of the latest price update |

---

## Market Depth

`POST /marketdata/marketdepth`

**Headers:** `Authorization: Bearer <userSession>`

### Request

```json
{ "exchange": "NSEEQ", "instrumentId": "1594" }
```

### Response

```json
{
  "status": "Ok",
  "message": "Success",
  "result": {
    "exchange": "NSEFO",
    "instrumentId": 408065,
    "totalBidQuantity": 404715,
    "totalAskQuantity": 216809,
    "marketDepth": {
      "bids": [{ "price": 110, "quantity": 10, "orders": 30 }],
      "asks": [{ "price": 14311, "quantity": 100, "orders": 4 }]
    }
  }
}
```

`marketDepth.bids`/`.asks` each hold up to 5 `{ price, quantity, orders }` levels.

---

## Open Interest

`POST /marketdata/openinterest`

**Headers:** `Authorization: Bearer <userSession>`

### Request

```json
{ "exchange": "NSEEQ", "instrumentId": "1594" }
```

### Response

```json
{ "exchange": "NSEFO", "instrumentId": 408065, "openInterest": 7239000, "dayHighOi": 87863000, "dayLowOi": 69892000 }
```
