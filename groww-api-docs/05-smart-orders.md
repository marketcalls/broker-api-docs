# Groww Smart Orders API

Source: [Groww API Smart Orders](https://groww.in/trade-api/docs/curl/smart-orders)

Base URL: https://api.groww.in

All endpoints require Authorization: Bearer {ACCESS_TOKEN}, X-API-VERSION: 1.0 and Accept: application/json. JSON-body requests also require Content-Type: application/json. Smart Orders support CASH and FNO; COMMODITY is not supported. API-created GTT orders default to one year of validity from creation.

Groww defines GTT (Good Till Triggered) as a single order armed when its trigger condition is met. OCO (One Cancels the Other) pairs target and stop-loss legs; execution of one cancels the other.

## Create GTT

POST /v1/order-advance/create

Example body:

    {
      "reference_id": "sref-unique-123",
      "smart_order_type": "GTT",
      "segment": "CASH",
      "trading_symbol": "TCS",
      "quantity": 10,
      "trigger_price": "3985.00",
      "trigger_direction": "DOWN",
      "order": {"order_type":"LIMIT","price":"3990.00","transaction_type":"BUY"},
      "product_type": "CNC",
      "exchange": "NSE",
      "duration": "DAY"
    }

| Field | Type | Required | Description |
|---|---|---:|---|
| reference_id | string | Yes | 8–20 character alphanumeric idempotency key; at most two hyphens |
| smart_order_type | string | Yes | GTT |
| segment | string | Yes | CASH or FNO |
| trading_symbol | string | Yes | Exchange trading symbol |
| quantity | integer | Yes | Post-trigger quantity; FNO must respect lot size |
| trigger_price | string | Yes | Decimal trigger price |
| trigger_direction | string | Yes | UP or DOWN |
| order.order_type | string | Yes | Post-trigger type, e.g. LIMIT or SL |
| order.price | string | Conditional | Required for LIMIT or SL |
| order.transaction_type | string | Yes | BUY or SELL |
| child_legs | object | No | Optional bracket target/stop-loss legs |
| product_type | string | Yes | Product type |
| exchange | string | Yes | Exchange |
| duration | string | Yes | Post-trigger order validity |

HTTP 201 example payload includes smart_order_id, smart_order_type, status, symbol, exchange, quantity, product_type, duration, order, trigger fields, cancellation/modification permissions, and created_at/expire_at/triggered_at/updated_at timestamps.

## Create OCO

POST /v1/order-advance/create

Example body:

    {
      "reference_id": "sref-unique-456",
      "smart_order_type": "OCO",
      "segment": "FNO",
      "trading_symbol": "NIFTY25OCT24000CE",
      "quantity": 50,
      "net_position_quantity": 50,
      "transaction_type": "SELL",
      "target": {"trigger_price":"120.50","order_type":"LIMIT","price":"121.00"},
      "stop_loss": {"trigger_price":"95.00","order_type":"SL_M","price":null},
      "product_type": "NRML",
      "exchange": "NSE",
      "duration": "DAY"
    }

| Field | Type | Required | Description |
|---|---|---:|---|
| reference_id | string | Yes | Idempotency key, 8–20 alphanumeric characters and at most two hyphens |
| smart_order_type | string | Yes | OCO |
| segment | string | Yes | CASH or FNO |
| trading_symbol | string | Yes | Exchange trading symbol |
| quantity | integer | Yes | Quantity for both legs; no greater than absolute net position |
| net_position_quantity | integer | Yes | Current net position used for leg direction and validation |
| transaction_type | string | Yes | BUY or SELL |
| target.trigger_price | string | Yes | Target trigger |
| target.order_type | string | Yes | LIMIT or MARKET |
| target.price | string | Conditional | Required when target order type is LIMIT |
| stop_loss.trigger_price | string | Yes | Stop-loss trigger |
| stop_loss.order_type | string | Yes | SL or SL_M |
| stop_loss.price | string | Conditional | Required when stop-loss order type is SL |
| product_type | string | Yes | CASH OCO supports MIS; FNO OCO supports NRML |
| exchange | string | Yes | Exchange |
| duration | string | Yes | Validity for both legs |

HTTP 201 example returns smart_order_id, type, status, symbol, exchange, quantity, product, duration, legs, and timestamps. When either leg executes, the other is cancelled.

## Modify Smart Order

PUT /v1/order-advance/modify/{smart_order_id}

Only fields listed for the relevant flow are honored. Use cancel and create for other changes.

GTT modifiable fields: quantity, trigger_price, trigger_direction, order.order_type, order.price, child_legs. order.transaction_type is required in the modification request but is not modifiable.

Example GTT request body:

    {
      "smart_order_type": "GTT",
      "segment": "CASH",
      "quantity": 12,
      "trigger_price": "3980.00",
      "trigger_direction": "DOWN",
      "order": {"order_type":"LIMIT","price":"3985.00","transaction_type":"BUY"}
    }

For GTT, order.price is required for LIMIT/SL; set it to null for MARKET/SL_M.

OCO modifiable fields: quantity, duration, product_type, target.trigger_price, stop_loss.trigger_price.

Example OCO request body:

    {
      "smart_order_type": "OCO",
      "segment": "FNO",
      "duration": "DAY",
      "quantity": 40,
      "product_type": "NRML",
      "target": {"trigger_price":"122.00"},
      "stop_loss": {"trigger_price":"97.50"}
    }

Groww's example HTTP 202 payload contains smart_order_id, smart_order_type, status, and quantity.

| Change | GTT | OCO |
|---|---|---|
| Quantity and trigger price | Modify | Modify |
| Trigger direction | Modify | Not applicable |
| Order type and limit price | Modify | Cancel and recreate |
| Duration and product type | Cancel and recreate | Modify |
| Symbol, exchange, segment, smart-order type | Cancel and recreate | Cancel and recreate |

## Cancel Smart Order

POST /v1/order-advance/cancel/{segment}/{smart_order_type}/{smart_order_id}

Cancels an active smart order. All path values are required. Example:

    POST https://api.groww.in/v1/order-advance/cancel/CASH/GTT/gtt_91a7f4

HTTP 202 response payload contains smart_order_id, smart_order_type and status (CANCELLED).

## Get Smart Order

GET /v1/order-advance/status/{segment}/{smart_order_type}/internal/{smart_order_id}

Path fields: segment (CASH/FNO), smart_order_type (GTT/OCO), smart_order_id. HTTP 200 response is a SUCCESS envelope whose payload follows the GTT or OCO response schema.

## List Smart Orders

GET /v1/order-advance/list

| Query parameter | Type | Description |
|---|---|---|
| segment | string | Segment, e.g. FNO or CASH |
| smart_order_type | string | GTT or OCO; default OCO |
| status | string | ACTIVE, CANCELLED, COMPLETED; default ACTIVE |
| page | integer | 0–500; default 0 |
| page_size | integer | 1–50; default 10 |
| start_date_time | string | Inclusive ISO 8601 start; default start of today in server timezone |
| end_date_time | string | Inclusive ISO 8601 end; default start of next day in server timezone |

Date range cannot exceed one month. end_date_time must not precede start_date_time. Response payload contains orders, an array of GTT/OCO objects.

Example query values: segment=FNO, smart_order_type=OCO, status=ACTIVE, page=0, page_size=10, start_date_time=2025-01-16T09:15:00, end_date_time=2025-01-16T15:30:00.

## Response fields

GTT objects may contain smart_order_id, smart_order_type, status, trading_symbol, exchange, quantity, product_type, duration, order details, ltp, trigger_direction, trigger_price, segment, remark, display_name, child_legs, cancellation/modification flags, and created_at, expire_at, triggered_at, updated_at.

OCO objects may contain smart_order_id, smart_order_type, status, trading_symbol, exchange, quantity, product_type, duration, target and stop_loss leg details, permission flags, and timestamps.

## Notes

* Use a unique reference_id for each new smart order to avoid accidental duplicates.
* For OCO, quantity must be less than or equal to abs(net_position_quantity).
* For symbol, segment, exchange, or GTT/OCO type changes, cancel the existing order and create another one.

