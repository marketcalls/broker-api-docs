# LTP Quotes V3 API

## Overview

Last traded price data with enhanced fields: last traded quantity, cumulative daily volume, and previous closing price.

## Endpoint

**GET** `https://api.upstox.com/v3/market-quote/ltp`

## Query Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| instrument_key | Yes | Comma-separated instrument keys |

## Response

```json
{
  "status": "success",
  "data": {
    "NSE_FO:NIFTY2543021600PE": {
      "last_price": 303.9,
      "instrument_token": "NSE_FO|51834",
      "ltq": 75,
      "volume": 170325,
      "cp": 29.0
    }
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| last_price | number | Last traded price |
| instrument_token | string | Instrument identifier |
| ltq | number | Last traded quantity |
| volume | number | Current day cumulative volume |
| cp | number | Previous day closing price |

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1009 | Missing instrument_key |
| UDAPI1011 | Invalid instrument_key format |
| UDAPI1087 | Invalid instrument key |
| UDAPI100043 | Exceeded max instrument keys |
