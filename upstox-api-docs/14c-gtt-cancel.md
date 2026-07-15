# Cancel GTT Order API

## Endpoint

**DELETE** `https://api.upstox.com/v3/order/gtt/cancel`

## Request Body

```json
{
  "gtt_order_id": "GTT-C25280200137522"
}
```

## Response

```json
{
  "status": "success",
  "data": {
    "gtt_order_ids": ["GTT-CU25280200018007"]
  },
  "metadata": {
    "latency": 65
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1134 | gtt_order_id is required |
| UDAPI1135 | GTT order ID must start with 'GTT-' |
| UDAPI1154 | Static IP restriction |
| UDAPI1156 | Invalid X-Algo-Name header |
