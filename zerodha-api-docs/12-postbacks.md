# Postbacks / WebHooks

Sends POST requests with JSON payloads to your registered `postback_url` when order statuses change.

**Target audience:** Platforms and public apps using single API key for multiple users. For individual developers, use WebSocket postbacks instead.

## Checksum Validation

Every postback includes `checksum` = SHA-256(`order_id` + `order_timestamp` + `api_secret`). Validate this to confirm the request originates from Kite Connect.

## Sample Payload

```json
{
  "user_id": "AB1234",
  "unfilled_quantity": 0,
  "app_id": 1234,
  "checksum": "2011845d...",
  "placed_by": "AB1234",
  "order_id": "220303000308932",
  "exchange_order_id": "1000000001482421",
  "parent_order_id": null,
  "status": "COMPLETE",
  "status_message": null,
  "order_timestamp": "2022-03-03 09:24:25",
  "exchange_update_timestamp": "2022-03-03 09:24:25",
  "exchange_timestamp": "2022-03-03 09:24:25",
  "variety": "regular",
  "exchange": "NSE",
  "tradingsymbol": "SBIN",
  "instrument_token": 779521,
  "order_type": "MARKET",
  "transaction_type": "BUY",
  "validity": "DAY",
  "product": "CNC",
  "quantity": 1,
  "disclosed_quantity": 0,
  "price": 0,
  "trigger_price": 0,
  "average_price": 470,
  "filled_quantity": 1,
  "pending_quantity": 0,
  "cancelled_quantity": 0,
  "market_protection": 0,
  "meta": {},
  "tag": null,
  "guid": "XXXXXX"
}
```

## Key Fields

| Field | Type | Description |
|-------|------|-------------|
| order_id | string | Unique order identifier |
| status | string | COMPLETE, REJECTED, CANCELLED, UPDATE |
| average_price | float64 | Execution price |
| filled_quantity | int64 | Executed quantity |
| unfilled_quantity | int64 | Remaining quantity |
| checksum | string | SHA-256 validation hash |
| variety | string | regular, amo, co |
| tag | string | Optional identifier (max 20 chars) |

**Note:** Postback API works even when the user is not logged in.
