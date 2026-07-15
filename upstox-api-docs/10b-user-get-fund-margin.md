# Get Fund And Margin API

## Overview

This API retrieves user funds data for equity and commodity markets, including margin utilization, available margin for trading, and total payin amounts.

## Endpoint

**GET** `https://api.upstox.com/v2/user/get-funds-and-margin`

## Request Headers

- `Content-Type: application/json`
- `Accept: application/json`
- `Authorization: Bearer {your_access_token}`

## Query Parameters

| Name | Required | Type | Description |
|------|----------|------|-------------|
| segment | false | string | Market segment filter. Options: `SEC` (Equity) or `COM` (Commodity). Without specification, response includes both. |

## Response Structure

```json
{
  "status": "success",
  "data": {
    "equity": {
      "used_margin": 0.0,
      "payin_amount": 0.0,
      "span_margin": 0.0,
      "adhoc_margin": 0.0,
      "notional_cash": 0.0,
      "available_margin": 0.0,
      "exposure_margin": 0.0
    },
    "commodity": {
      "used_margin": 0.0,
      "payin_amount": 0.0,
      "span_margin": 0.0,
      "adhoc_margin": 0.0,
      "notional_cash": 0.0,
      "available_margin": 0.0,
      "exposure_margin": 0.0
    }
  }
}
```

## Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| used_margin | float | Positive values = amount blocked in open orders/positions; negative = amount released |
| payin_amount | float | Instant payin amount |
| span_margin | float | Amount blocked for futures/options SPAN |
| adhoc_margin | float | Manually credited payin amount |
| notional_cash | float | Amount reserved for withdrawal |
| available_margin | float | Total margin available for trading |
| exposure_margin | float | Amount blocked for futures/options exposure |

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI100072 | The Funds service is accessible from 5:30 AM to 12:00 AM IST daily |
