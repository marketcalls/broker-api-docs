# Modify Order V3 API

## Overview

The Modify Order V3 API allows modifications to open or pending orders with latency tracking.

## Endpoint

**PUT** `https://api-hft.upstox.com/v3/order/modify`

## Request Headers

- `Content-Type: application/json`
- `Accept: application/json`
- `Authorization: Bearer {your_access_token}`

## Request Parameters

| Parameter | Required | Type | Details |
|-----------|----------|------|---------|
| order_id | Yes | string | The order identifier requiring modification |
| validity | Yes | string | `DAY` or `IOC` |
| price | Yes | number | Limit order price |
| order_type | Yes | string | `MARKET`, `LIMIT`, `SL`, or `SL-M` |
| quantity | No | integer | Modified order quantity |
| trigger_price | Yes | number | Required for stop-loss orders |
| disclosed_quantity | No | integer | Market depth display volume (minimum 10% of total) |
| market_protection | No | integer | Protection percentage (-1 to 25, default: -1) |

## Response Format

```json
{
  "status": "success",
  "data": {
    "order_id": "1644490272000"
  },
  "metadata": {
    "latency": 40
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1003 | Order ID is required |
| UDAPI100010 | Order not found |
| UDAPI100041 | Cannot modify cancelled/rejected/completed orders |
| UDAPI1158 | Market orders not allowed; try placing a limit order |
| UDAPI1161 | MCX orders via API are temporarily disabled |

Only modified parameters require inclusion; unchanged values default to original order specifications.
