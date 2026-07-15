# Place Multi Order API

## Overview

The Place Multi Order API enables simultaneous placement of multiple orders on the exchange. Each order must include a unique `correlation_id` for individual tracking.

## Endpoint

**POST** `https://api.upstox.com/v2/order/multi/place`

## Constraints

- Maximum of **10 orders** per request
- Each successful order receives a unique `order_id`
- Subject to different rate limits than standard API endpoints
- System executes all BUY orders first, followed by SELL orders

## Request Headers

- `Content-Type: application/json`
- `Accept: application/json`
- `Authorization: Bearer {your_access_token}`

## Request Body (JSON Array)

| Parameter | Required | Type | Details |
|-----------|----------|------|---------|
| correlation_id | Yes | string | Unique identifier (max 20 characters) |
| quantity | Yes | integer | Number of units |
| product | Yes | string | Product type (e.g., "D") |
| validity | Yes | string | Order validity (e.g., "DAY") |
| price | Yes | integer | Price (0 for market orders) |
| instrument_token | Yes | string | Exchange instrument identifier |
| order_type | Yes | string | "MARKET", "LIMIT", etc. |
| transaction_type | Yes | string | "BUY" or "SELL" |
| slice | No | boolean | Enable auto-slicing (default: false) |
| tag | No | string | Custom label (max 40 characters) |
| market_protection | No | integer | Market protection percentage (-1 to 25) |

## Response Formats

**Success (200):** All orders placed

```json
{
  "status": "success",
  "data": [{"correlation_id": "1", "order_id": "1644490272000"}],
  "summary": {"total": 1, "payload_error": 0, "success": 1, "error": 0}
}
```

**Partial Success (207):** Some orders succeeded, others failed

**Error (400):** All orders failed

## Auto-Slicing

When `slice: true`, orders exceeding exchange freeze quantities are automatically split. Split orders receive correlation IDs with suffixes (e.g., "orderline25_1", "orderline25_2").

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1114 | Empty request payload |
| UDAPI1115 | Missing correlation_id |
| UDAPI1117 | Duplicate correlation_id values |
| UDAPI1118 | Maximum order limit exceeded (10 orders) |
| UDAPI1119 | Tag exceeds 40 characters |
