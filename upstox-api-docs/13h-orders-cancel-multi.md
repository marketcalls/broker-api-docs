# Cancel Multi Order API

## Overview

Enables bulk cancellation of open orders across your portfolio with optional filtering by segment or tag. Maximum 10 orders per request.

## Endpoint

**DELETE** `https://api.upstox.com/v2/order/multi/cancel`

## Supported Filters

- **Segment:** NSE_EQ, BSE_EQ, NSE_FO, BSE_FO, MCX_FO, NCD_FO, BCD_FO, NSE_COM
- **Tag:** custom identifier

## Response Status Values

- `success` - all cancellations completed
- `partial_success` - some orders cancelled, others failed
- `error` - all cancellation attempts failed

## Response Structure

Includes `order_ids` array, `summary` object tracking total/successful/failed, and `errors` array for failures.

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1108 | Invalid segment parameter |
| UDAPI1109 | No open/pending orders available |
| UDAPI1110 | More than 10 open orders present |
| UDAPI1154 | Static IP not whitelisted |
| UDAPI1156 | Invalid X-Algo-Name header |
