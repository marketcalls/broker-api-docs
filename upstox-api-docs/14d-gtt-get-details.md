# Get GTT Order Details API

## Endpoint

**GET** `https://api.upstox.com/v3/order/gtt`

## Query Parameters

| Name | Required | Type | Description |
|------|----------|------|-------------|
| gtt_order_id | No | string | The GTT order reference ID |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| type | string | `SINGLE` or `MULTIPLE` |
| exchange | string | `NSE_EQ`, `BSE_EQ`, etc. |
| quantity | integer | Number of units |
| product | string | `I`, `D`, or `MTF` |
| trading_symbol | string | Instrument symbol |
| instrument_token | string | Unique identifier |
| gtt_order_id | string | Unique GTT order ID |
| expires_at | string | Expiration timestamp |
| created_at | string | Creation timestamp |
| rules | array | Execution conditions |

### Rules Array

| Field | Type | Description |
|-------|------|-------------|
| strategy | string | `ENTRY`, `TARGET`, `STOPLOSS` |
| status | string | `SCHEDULED`, `TRIGGERED`, `EXPIRED`, `OPEN`, `COMPLETED`, `CANCELLED`, `PENDING`, `FAILED`, `INACTIVE` |
| trigger_type | string | `BELOW`, `ABOVE`, `IMMEDIATE` |
| trigger_price | float | Price threshold |
| transaction_type | string | `BUY`, `SELL` |
| message | string | Error details if failed |
| order_id | string | Generated order ID (null if not placed) |
| trailing_gap | float | TSL gap (STOPLOSS only) |

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1135 | GTT order ID must start with 'GTT-' |
