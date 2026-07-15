# Webhook

Upstox allows developers to configure webhooks during app registration to receive real-time updates via POST requests to their specified endpoint.

## Supported Update Types

1. **Order Updates** - enabled by default
2. **GTT Order Updates** - must be explicitly enabled through the My Apps configuration page

## Webhook Requirements

The endpoint must meet these specifications:

- Accept POST requests without requiring authentication
- Return a 2XX HTTP status code
- Remain accessible and operational

## Payload Structure

### Order Update Example

```json
{
  "update_type": "order",
  "user_id": "******",
  "exchange": "NSE",
  "instrument_token": "NSE_EQ|INE848E01016",
  "instrument_key": "NSE_EQ|INE848E01016",
  "trading_symbol": "NHPC-EQ",
  "product": "D",
  "order_type": "MARKET",
  "average_price": 0,
  "price": 0,
  "trigger_price": 0,
  "quantity": 1,
  "disclosed_quantity": 0,
  "pending_quantity": 1,
  "transaction_type": "BUY",
  "order_ref_id": "57744821658411",
  "exchange_order_id": "",
  "validity": "DAY",
  "status": "put order req received",
  "is_amo": false,
  "variety": "SIMPLE",
  "order_id": "240221025997024",
  "order_timestamp": "2024-02-21 14:40:02",
  "filled_quantity": 0,
  "placed_by": "******"
}
```

### GTT Order Update Example

```json
{
  "update_type": "gtt_order",
  "type": "MULTIPLE",
  "exchange": "NSE_EQ",
  "instrument_token": "NSE_EQ|INE806A01020",
  "quantity": 1,
  "product": "D",
  "gtt_order_id": "GTT-CU25270200024002",
  "rules": [
    {
      "strategy": "ENTRY",
      "status": "FAILED",
      "trigger_price": 7.7,
      "transaction_type": "BUY",
      "message": "The price set should be within the circuit limits..."
    }
  ]
}
```

## Key Notes

- Webhook payloads mirror WebSocket update structures
- Avoid using public endpoints for webhook URLs
- Deprecated: lowercase field names like `tradingsymbol` will be removed; use snake_case versions
