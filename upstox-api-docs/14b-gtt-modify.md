# Modify GTT Order API

## Endpoint

**PUT** `https://api.upstox.com/v3/order/gtt/modify`

## Request Body

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| type | Yes | string | `SINGLE` or `MULTIPLE` |
| quantity | Yes | integer | Order quantity (cannot modify once OPEN) |
| gtt_order_id | Yes | string | GTT order ID (format: `GTT-XXXXXXXXXX`) |
| rules | Yes | array | Trigger conditions |
| rules[].strategy | Yes | string | `ENTRY`, `TARGET`, or `STOPLOSS` |
| rules[].trigger_type | Yes | string | `ABOVE`, `BELOW`, or `IMMEDIATE` |
| rules[].trigger_price | Yes | float | Price threshold |
| rules[].trailing_gap | No | float | For trailing stop loss |

## Response

```json
{
  "status": "success",
  "data": {
    "gtt_order_ids": ["GTT-CU25280200021013"]
  },
  "metadata": {
    "latency": 74
  }
}
```

## Key Constraints

- Quantity cannot be modified after order reaches OPEN status
- In OPEN status, only IMMEDIATE trigger_type allowed for ENTRY
- Non-ENTRY strategies must use IMMEDIATE only
- Duplicate strategies not permitted

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1126-1145 | Validation errors for type, rules, strategy, trigger_type, trigger_price |
| UDAPI1150 | Only IMMEDIATE trigger type for open GTT orders |
| UDAPI1154 | Static IP restrictions |
| UDAPI1158 | Market orders blocked; use limit orders |
