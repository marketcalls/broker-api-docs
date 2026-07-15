# Exit All Positions API

## Overview

Enables traders to close all open positions simultaneously. Uses MARKET orders with Market Price Protection (MPP) by default.

## Endpoint

**POST** `https://api.upstox.com/v2/order/positions/exit`

## Request Headers

- `Content-Type: application/json`
- `Accept: application/json`
- `Authorization: Bearer {your_access_token}`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| `segment` | No | string | NSE_EQ, BSE_EQ, NSE_FO, BSE_FO, MCX_FO, NCD_FO, BCD_FO, NSE_COM |
| `tag` | No | string | Order tag for filtering (valid for intraday positions only) |

## Response

```json
{
  "status": "success",
  "data": {
    "order_ids": ["1644490272000", "1644490272001", "1644490272003"]
  },
  "errors": null,
  "summary": {
    "total": 3,
    "success": 3,
    "error": 0
  }
}
```

## Key Notes

- Executes all BUY positions first, followed by SELL orders
- Order tags only valid for intraday positions
- Auto-slicing for orders exceeding exchange freeze quantities
- Status can be `success`, `partial_success`, or `error`

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1108 | Invalid segment |
| UDAPI1111 | No open positions exist |
| UDAPI1112 | More than 10 open positions |
| UDAPI1113 | Outside market trading hours |
| UDAPI1154 | Static IP not whitelisted |
| UDAPI1156 | Invalid X-Algo-Name header |
