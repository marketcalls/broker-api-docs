# OHLC Quotes V3 API

## Overview

Retrieves OHLC data with current and previous candles, volume, and timestamps.

## Endpoint

**GET** `https://api.upstox.com/v3/market-quote/ohlc`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| instrument_key | Yes | string | Comma-separated keys |
| interval | Yes | string | `1d` (daily), `I1` (1-minute), `I30` (30-minute) |

## Response

```json
{
  "status": "success",
  "data": {
    "INSTRUMENT_KEY": {
      "last_price": 303.9,
      "instrument_token": "NSE_FO|51834",
      "prev_ohlc": {
        "open": 303.9,
        "high": 304.3,
        "low": 303.85,
        "close": 304.3,
        "volume": 300,
        "ts": 1744019880000
      },
      "live_ohlc": {
        "open": 304.45,
        "high": 304.45,
        "low": 302.75,
        "close": 303.9,
        "volume": 2250,
        "ts": 1744019940000
      }
    }
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1009 | Symbol parameter missing |
| UDAPI1027 | Interval parameter required |
| UDAPI1028 | Invalid interval value |
| UDAPI1087 | Invalid instrument key |
| UDAPI100043 | Maximum instrument key limit exceeded |
