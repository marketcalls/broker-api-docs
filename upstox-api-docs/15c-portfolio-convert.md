# Convert Positions API

## Overview

Transform intraday positions into delivery trades, or convert margin trades to cash and carry, and vice versa. Position is converted only if required margin is available.

## Endpoint

**PUT** `https://api.upstox.com/v2/portfolio/convert-position`

## Key Constraints

- Delivery holdings can only convert to intraday if purchased same day before auto square-off
- Only simple orders qualify for intraday-to-delivery conversion
- CO orders cannot be converted

## Request Parameters

| Parameter | Required | Type | Details |
|-----------|----------|------|---------|
| instrument_token | Yes | string | Instrument key |
| new_product | Yes | string | Target: `I` or `D` |
| old_product | Yes | string | Current: `I` or `D` |
| transaction_type | Yes | string | `BUY` or `SELL` |
| quantity | Yes | int32 | Quantity to convert |

## Response

```json
{
  "status": "success",
  "data": {
    "status": "complete"
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1033 | Position data retrieval failed |
| UDAPI1034 | No positions found |
| UDAPI1035 | No positions match instrument/product |
