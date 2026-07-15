# LTP Quotes API (V2 - Deprecated)

## Endpoint

**GET** `https://api.upstox.com/v2/market-quote/ltp`

## Query Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| instrument_key | Yes | Comma-separated (max 500) |

## Response

```json
{
  "status": "success",
  "data": {
    "NSE_EQ:NHPC": {
      "last_price": 52.05,
      "instrument_token": "NSE_EQ|INE848E01016"
    }
  }
}
```
