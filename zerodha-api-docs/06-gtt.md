# GTT Orders (Good Till Triggered)

## Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/gtt/triggers` | Create GTT order |
| GET | `/gtt/triggers` | Retrieve all GTT orders |
| GET | `/gtt/triggers/:id` | Get specific GTT details |
| PUT | `/gtt/triggers/:id` | Modify active GTT |
| DELETE | `/gtt/triggers/:id` | Remove active GTT |

## Placing Triggers

### Core Parameters

1. **type** - `single` or two-leg (OCO)
2. **condition** - JSON object with trigger specifications
3. **orders** - JSON array of orders to execute

### Condition Parameters

| Parameter | Description |
|-----------|-------------|
| exchange | Exchange name (e.g., NSE) |
| tradingsymbol | Instrument trading symbol |
| trigger_values | Array of price trigger points |
| last_price | Current price at placement |

### Order Parameters

| Parameter | Description |
|-----------|-------------|
| exchange | Exchange identifier |
| tradingsymbol | Instrument symbol |
| transaction_type | BUY or SELL |
| quantity | Units to transact |
| order_type | LIMIT |
| product | Margin product (e.g., CNC) |
| price | Execution price |

### GTT Types

**Single Trigger:** One order when single trigger value reached. Requires exactly one value in `trigger_values`.

**Two-Leg (OCO):** One Cancels Other. Two trigger values; when either triggers, corresponding order executes.

## Status Values

| Status | Meaning |
|--------|---------|
| active | Monitoring conditions |
| triggered | Condition met; execution initiated |
| disabled | Inactive; user action required |
| expired | Exceeded expiry date |
| cancelled | System-initiated cancellation |
| rejected | System rejection |
| deleted | User removed trigger |

## Retrieving

- **All:** GET `/gtt/triggers` - Active and last 7 days history
- **Specific:** GET `/gtt/triggers/:id` - Any trigger regardless of age/status
