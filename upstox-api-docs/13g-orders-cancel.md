# Cancel Order API (V2 - Deprecated)

## Endpoint

**DELETE** `https://api-hft.upstox.com/v2/order/cancel`

**Status:** Sandbox Enabled | Deprecated

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| order_id | Yes | string | The order ID to cancel (alphanumeric and '-' only) |

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
| UDAPI1023 | Order ID is required |
| UDAPI1010 | Order ID contains invalid characters |
| UDAPI100049 | API access restricted; use Uplink Business |
| UDAPI100010 | Order not found |
| UDAPI100040 | Cannot cancel already finalized orders |
