# Place GTT Order API

## Overview

Good Till Triggered (GTT) orders execute automatically when specified trigger conditions are met. Supports single-leg triggers, multi-leg triggers with targets/stop-losses, and trailing stop-loss orders.

## Order Types

### Single-Leg Trigger (ENTRY Strategy)
Places an order when a defined condition is satisfied. Specify BUY or SELL when price moves above, below, or equals the trigger price.

### Multi-Leg Trigger
Expands on single-leg with follow-up actions:
- **TARGET:** Exit position at desired price level
- **STOPLOSS:** Exit position when price moves unfavorably

### Trailing Stop Loss (Beta)
A dynamic order that automatically adjusts with market price movements, maintaining a consistent distance from the current market price.

## Endpoint

**POST** `https://api.upstox.com/v3/order/gtt/place`

## Request Headers

- `Authorization: Bearer {access_token}`
- `Content-Type: application/json`
- `Accept: application/json`
- `X-Algo-Name` (optional)

## Request Body Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| type | Yes | string | `SINGLE` or `MULTIPLE` |
| quantity | Yes | integer | Order quantity |
| product | Yes | string | `I` (Intraday), `D` (Delivery), `MTF` |
| instrument_token | Yes | string | Instrument identifier |
| transaction_type | Yes | string | `BUY` or `SELL` |
| rules | Yes | array | Trigger conditions array |
| rules[].strategy | Yes | string | `ENTRY`, `TARGET`, or `STOPLOSS` |
| rules[].trigger_type | Yes | string | `BELOW`, `ABOVE`, or `IMMEDIATE` |
| rules[].trigger_price | Yes | float | Activation price level |
| rules[].trailing_gap | No | float | TSL parameter (10% min of LTP-SL difference) |
| rules[].market_protection | No | integer | -1 to 25 |

## Response

```json
{
  "status": "success",
  "data": {
    "gtt_order_ids": ["GTT-CU25280200021013"]
  },
  "metadata": {
    "latency": 88
  }
}
```

## Validation Rules

- SINGLE type: exactly one rule
- MULTIPLE type: 2-3 rules
- ENTRY strategy is mandatory
- Non-ENTRY strategies accept only IMMEDIATE trigger type
- Trigger prices must be positive
- Each strategy can appear only once
- Market protection cannot exceed 25%

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1126 | Valid GTT type required |
| UDAPI1136 | SINGLE type requires exactly one rule |
| UDAPI1137 | MULTIPLE type requires 2-3 rules |
| UDAPI1141 | ENTRY strategy mandatory |
| UDAPI1143 | Non-ENTRY strategies require IMMEDIATE trigger type |
| UDAPI1151 | Trailing gap below minimum threshold |
| UDAPI1158 | Market orders blocked; use limit orders with market protection |
