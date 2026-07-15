# Exchange Status API

## Endpoint

**GET** `https://api.upstox.com/v2/market/status/{exchange}`

## Response

```json
{
  "status": "success",
  "data": {
    "exchange": "NSE",
    "status": "NORMAL_OPEN",
    "last_updated": 1705549500000
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1089 | Invalid exchange |
