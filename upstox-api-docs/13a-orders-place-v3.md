# Place Order V3 API

## Overview

The Place Order V3 API enables placing orders on exchanges with support for auto-slicing and latency tracking. Returns unique order IDs upon success.

## Endpoint

**POST** `https://api-hft.upstox.com/v3/order/place`

## Request Headers

```
Content-Type: application/json
Accept: application/json
Authorization: Bearer {your_access_token}
```

Optional: `X-Algo-Name` (for registered apps with exchange-approved algo strategies)

## Request Body Parameters

| Parameter | Required | Type | Notes |
|-----------|----------|------|-------|
| quantity | Yes | integer | Order quantity in units or lots |
| product | Yes | string | `I` (Intraday), `D` (Delivery), `MTF` |
| validity | Yes | string | `DAY`, `IOC` |
| price | Yes | float | Order price (0 for market orders) |
| instrument_token | Yes | string | Exchange instrument identifier |
| order_type | Yes | string | `MARKET`, `LIMIT`, `SL`, `SL-M` |
| transaction_type | Yes | string | `BUY`, `SELL` |
| is_amo | Yes | boolean | After Market Order flag (auto-inferred) |
| tag | No | string | Custom identifier (max 40 characters) |
| disclosed_quantity | Yes | integer | Market depth disclosure quantity |
| trigger_price | Yes | float | For stop-loss orders |
| slice | No | boolean | Enable auto-slicing (default: false) |
| market_protection | No | integer | Protection percentage (-1 to 25) |

## Auto-Slicing Feature

When enabled (`slice: true`), orders exceeding exchange freeze quantities automatically split into smaller orders. Example: A 10,100-unit order with 1,000-unit freeze becomes 11 orders (10x1,000 + 1x100).

## Response Format

```json
{
  "status": "success",
  "data": {
    "order_ids": ["1644490272000", "1644490272001"]
  },
  "metadata": {
    "latency": 30
  }
}
```

## Key Notes

- API accessible 5:30 AM - 12:00 AM IST daily
- The `is_amo` flag will be ignored; system automatically infers based on market session
- Market orders require market protection settings per exchange guidelines
- MCX orders currently disabled for API users

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1026 | Missing instrument key |
| UDAPI1052 | Zero quantity not allowed |
| UDAPI1118 | Maximum order limit exceeded with slicing |
| UDAPI1154 | Static IP not whitelisted |
| UDAPI1156 | Invalid algo name in headers |
| UDAPI1158 | Market orders blocked; use limit orders |
| UDAPI1161 | MCX orders temporarily disabled |
