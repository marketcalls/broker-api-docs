# Groww Orders API

Source: [Groww API Orders](https://groww.in/trade-api/docs/curl/orders)

Base URL: https://api.groww.in

All endpoints require Authorization: Bearer {ACCESS_TOKEN} and X-API-VERSION: 1.0. Send Accept: application/json. Requests with a JSON body also send Content-Type: application/json. Successful examples use the envelope {"status":"SUCCESS","payload":{...}}. Groww documents status as SUCCESS or FAILURE.

Prices documented for order fields are in rupees. The usual segments are CASH and FNO.

## Place order

POST /v1/order/create

Creates a market or priced order.

Example body:

    {
      "trading_symbol": "WIPRO",
      "quantity": 100,
      "price": 2500,
      "trigger_price": 2450,
      "validity": "DAY",
      "exchange": "NSE",
      "segment": "CASH",
      "product": "CNC",
      "order_type": "SL",
      "transaction_type": "BUY",
      "order_reference_id": "Ab-654321234-1628190"
    }

| Field | Type | Required | Description |
|---|---|---:|---|
| trading_symbol | string | Yes | Exchange-defined trading symbol |
| quantity | integer | Yes | Instrument quantity |
| price | decimal | No | Limit order price in rupees |
| trigger_price | decimal | No | Trigger price in rupees |
| validity | string | Yes | Order validity |
| exchange | string | Yes | Stock exchange |
| segment | string | Yes | Instrument segment, such as CASH or FNO |
| product | string | Yes | Product type |
| order_type | string | Yes | Order type |
| transaction_type | string | Yes | Trade direction |
| order_reference_id | string | Yes* | User reference, 8–20 alphanumeric characters and at most two hyphens |

Example response payload:

    {
      "groww_order_id": "GMK39038RDT490CCVRO",
      "order_status": "OPEN",
      "order_reference_id": "Ab-654321234-1628190",
      "remark": "Order placed successfully"
    }

## Modify order

POST /v1/order/modify

Modifies pending and open orders. Example body:

    {
      "quantity": 100,
      "price": 2500,
      "trigger_price": 2450,
      "order_type": "SL",
      "segment": "CASH",
      "groww_order_id": "GMK39038RDT490CCVRO"
    }

| Field | Type | Required | Description |
|---|---|---:|---|
| quantity | integer | No | Quantity |
| price | decimal | No | Limit order price in rupees |
| trigger_price | decimal | No | Trigger price in rupees |
| order_type | string | Yes | Order type |
| segment | string | Yes | Segment such as CASH or FNO |
| groww_order_id | string | Yes | Groww-generated order ID |

Response payload: groww_order_id and order_status.

## Cancel order

POST /v1/order/cancel

Cancels pending and open orders. Request body:

    {"segment":"CASH","groww_order_id":"GMK39038RDT490CCVRO"}

Both fields are required. Example response payload has groww_order_id and order_status, such as CANCELLED.

## Get trades for an order

GET /v1/order/trades/{groww_order_id}?segment=CASH&page=0&page_size=50

The order ID and segment are required; page is optional, and page_size is optional with a maximum of 50. An order may have multiple trade fills.

Successful payload contains trade_list, an array with these documented fields:

| Field | Type | Description |
|---|---|---|
| price | decimal | Instrument price in rupees |
| isin | string | ISIN |
| quantity | integer | Trade quantity |
| groww_order_id | string | Groww order ID |
| groww_trade_id | string | Groww trade ID |
| exchange_trade_id | string | Exchange trade ID |
| exchange_order_id | string | Exchange order ID |
| trade_status | string | Trade status |
| trading_symbol | string | Trading symbol |
| remark | string | Trade remark |
| exchange, segment, product, transaction_type | string | Venue/order attributes |
| created_at, trade_date_time | string | Timestamps |
| settlement_number | string | Settlement number |

## Get order status

GET /v1/order/status/{groww_order_id}?segment=CASH

Required inputs are the path order ID and segment query parameter. Response payload fields: groww_order_id, order_status, remark, filled_quantity, order_reference_id.

## Get order status by reference ID

GET /v1/order/status/reference/{order_reference_id}?segment=CASH

Required inputs are the reference ID and segment. Response payload has the same fields as order status lookup.

## List orders

GET /v1/order/list?segment=CASH&page=0&page_size=100

Returns the day's orders, including open, pending, and executed orders. Schema marks segment optional, but the example includes it. page_size maximum is 100.

Response payload contains order_list. Documented order fields:

| Field | Type | Description |
|---|---|---|
| groww_order_id, trading_symbol, order_status, remark | string | Order identity and status |
| quantity, filled_quantity, remaining_quantity, deliverable_quantity | integer | Order/fill quantities |
| price, trigger_price, average_fill_price | decimal | Prices; price and trigger_price are documented in rupees |
| amo_status, validity, exchange, order_type, transaction_type, segment, product | string | Order attributes |
| created_at, exchange_time, trade_date | string | Timestamps |
| order_reference_id | string | User reference |

## Get order details

GET /v1/order/detail/{groww_order_id}?segment=CASH

Both the order ID and segment are required. Response payload includes the same order fields documented for order_list: IDs, symbol/status, quantities, prices, AMO state, validity, exchange/product/order attributes, timestamps, and reference ID.

## Documentation notes

* Groww's create-order overview calls order_reference_id optional, but its request schema marks it required. This page preserves the schema's required marker; verify behavior with Groww for your API version.
* The cancel endpoint's published request schema includes a stray status row under Request schema. The actual example request body and required fields are segment and groww_order_id.
* Exact error payloads are not specified in this page.

*Required marker follows the published schema.
