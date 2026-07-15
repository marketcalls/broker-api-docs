# Full Market Quotes API

## Overview

Retrieves comprehensive market data for up to 500 instruments simultaneously with OHLC, depth, volume, and circuit limits.

## Endpoint

**GET** `https://api.upstox.com/v2/market-quote/quotes`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| instrument_key | Yes | string | Comma-separated keys (max 500) |

## Response

```json
{
  "status": "success",
  "data": {
    "NSE_EQ:NHPC": {
      "ohlc": {
        "open": 53.4,
        "high": 53.8,
        "low": 51.75,
        "close": 52.05
      },
      "depth": {
        "buy": [...],
        "sell": [...]
      },
      "timestamp": "2023-10-19T05:21:51.099+05:30",
      "last_price": 52.05,
      "volume": 24123697,
      "net_change": -1.05,
      "lower_circuit_limit": 46.85,
      "upper_circuit_limit": 57.25
    }
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1087 | Invalid symbol/instrument_key |
| UDAPI100042 | Exceeded 500 instrument limit |
