# Modify Order API (V2 - Deprecated)

## Endpoint

**PUT** `https://api-hft.upstox.com/v2/order/modify`

**Status:** Sandbox Enabled | Deprecated

## Request Body Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `order_id` | Yes | string | Order identifier for modification |
| `validity` | Yes | string | `DAY` or `IOC` |
| `order_type` | Yes | string | `MARKET`, `LIMIT`, `SL`, or `SL-M` |
| `price` | Yes | number | Order price |
| `trigger_price` | Yes | number | Trigger price for stop loss orders |
| `quantity` | No | integer | Order quantity |
| `disclosed_quantity` | No | integer | Market depth display volume (minimum 10% of quantity) |
| `market_protection` | No | integer | Market protection percentage (-1 to 25) |

## Response

```json
{
  "status": "success",
  "data": {
    "order_id": "1644490272000"
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1003 | Order ID required |
| UDAPI1004 | Valid order type required |
| UDAPI1007 | Validity required |
| UDAPI100010 | Order not found |
| UDAPI1158 | Market orders blocked; use limit orders |
| UDAPI100049 | API access restricted; use Uplink Business |
