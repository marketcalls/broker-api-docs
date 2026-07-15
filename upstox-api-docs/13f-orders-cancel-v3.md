# Cancel Order V3 API

## Endpoint

**DELETE** `https://api-hft.upstox.com/v3/order/cancel`

## Request Headers

- `Content-Type: application/json`
- `Accept: application/json`
- `Authorization: Bearer {your_access_token}`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| order_id | Yes | string | The order ID to cancel (alphanumeric and hyphens only) |

## Response

```json
{
  "status": "success",
  "data": {
    "order_id": "1644490272000"
  },
  "metadata": {
    "latency": 30
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1023 | Order ID is required |
| UDAPI1010 | Invalid order ID format |
| UDAPI100049 | Access restricted; use Uplink Business |
| UDAPI100010 | Order not found |
| UDAPI100040 | Cannot cancel already finalized orders |
| UDAPI1154 | Static IP not whitelisted |
| UDAPI1156 | Invalid X-Algo-Name header value |
