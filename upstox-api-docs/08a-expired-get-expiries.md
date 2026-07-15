# Get Expiries API

## Endpoint

**GET** `https://api.upstox.com/v2/expired-instruments/expiries`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| instrument_key | Yes | String | Key of underlying symbol |

## Response

```json
{
  "status": "success",
  "data": [
    "2024-10-03",
    "2024-10-10",
    "2024-10-17"
  ]
}
```

Returns up to six months of historical expiries including weekly and monthly options.

**Note:** MCX instruments are currently unsupported. Requires Upstox Plus subscription.

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI100011 | Invalid instrument key |
| UDAPI1149 | Requires Upstox Plus plan |
