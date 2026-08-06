# Order Status API - All orders

> Source: https://developer.hdfcsec.com/ir-docs/docs/order_status

## Description

The order APIs enable you to place orders of various types, modify and cancel pending orders, retrieve daily orders, and more.

## EndPoint

```js
Method:GET
`https://developer.hdfcsec.com/oapi/v1/orders?api_key=<api_key>`
```

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Query Params

- `api_key`: The API key used for authentication.

## Glossary of constants

| Field Name | Description |
| --- | --- |
| `client_id` | Unique identifier for the client. |
| `order_id` | Unique identifier for the order. |
| `exchange_order_id` | Unique identifier for the order in the exchange. |
| `status` | Status of the order. Possible values: CANCELLED, etc. |
| `status_message` | Additional status message (if any). |
| `status_message_raw` | Raw status message. |
| `order_timestamp` | Timestamp when the order was placed. |
| `exchange` | Exchange where the order was placed. |
| `security_id` | Unique identifier for the security. |
| `company_name` | Name of the company. |
| `underlying_symbol` | Symbol of the underlying asset. |
| `instrument_segment` | Segment of the instrument (if applicable). |
| `expiry_date` | Expiry date (if applicable). |
| `strike_price` | Strike price (if applicable). |
| `option_type` | Type of option (if applicable). |
| `isin` | ISIN (International Securities Identification Number). |
| `transaction_type` | Type of transaction. Possible values: BUY, SELL, etc. |
| `validity` | Validity of the order. Possible values: DAY, etc. |
| `product` | Product code. |
| `quantity` | Total quantity of the order. |
| `disclosed_quantity` | Disclosed quantity (if applicable). |
| `price` | Price per unit. |
| `trigger_price` | Trigger price (if applicable). |
| `filled_quantity` | Quantity filled. |
| `pending_quantity` | Quantity pending. |
| `average_price` | Average price (if applicable). |
| `total_traded_value` | Total traded value. |
| `order_source` | Source of the order. |
| `order_subchannel` | Subchannel of the order. |
| `modification_allowed` | Whether modification is allowed. Possible values: YES, NO. |
| `cancellation_allowed` | Whether cancellation is allowed. Possible values: YES, NO. |
| `order_slot` | Slot of the order. |
| `good_till_date` | Good till date (if applicable). |
| `external_reference_rumber` | External reference number. |

> The glossary lists `external_reference_rumber` (sic); the response payload uses
> `external_reference_number`. The sample response also returns `tradingsymbol`,
> `instrument_type`, `token_id`, `modified`, `instrument_token`, `order_type`,
> `cancelled_quantity` and `market_protection`, which are not listed in the glossary.

## Request Curl

```js
   curl --location 'https://developer.hdfcsec.com/oapi/v1/orders?api_key=api_key' \
--header 'Authorization: access_token' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

## API Response

```js
{
  "status": "success",
  "data": [
   {
            "client_id": "1234567",
            "order_id": "24043000401982",
            "exchange_order_id": "1600000205048078",
            "status": "Traded",
            "status_message": "",
            "status_message_raw": "",
            "order_timestamp": "30/04/2024 12:40:12",
            "exchange": "NSE",
            "tradingsymbol": "49599",
            "security_id": "49599",
            "company_name": "BANKNIFTY",
            "underlying_symbol": "BANKNIFTY",
            "instrument_segment": "OPTIDX",
            "instrument_type": "Equity Derivatives",
            "expiry_date": "30 APR 2024",
            "strike_price": 49900.0,
            "option_type": "Call",
            "isin": "",
            "transaction_type": "Buy",
            "validity": "DAY",
            "product": "OVERNIGHT",
            "quantity": 15,
            "disclosed_quantity": 0,
            "price": 0.0,
            "trigger_price": 0.0,
            "filled_quantity": 15,
            "pending_quantity": 0,
            "average_price": 0.0,
            "total_traded_value": 579.0,
            "order_source": "C",
            "order_subchannel": "C",
            "modification_allowed": "",
            "cancellation_allowed": "",
            "token_id": "NSEDNL49599",
            "order_slot": "Online",
            "good_till_date": "",
            "external_reference_number": "STAPI202404306812180",
            "modified": false,
            "instrument_token": 0,
            "order_type": "MARKET",
            "cancelled_quantity": 0,
            "market_protection": 0
        } 
  ]
}
```

> The official sample has an unterminated string literal on the `instrument_segment` line
> (`"instrument_segment": "OPTIDX,`). It is corrected above so the sample parses as JSON.

## Response field notes

- `expiry_date` comes back as `DD MON YYYY` (`"30 APR 2024"`), unlike the `YYYYMMDD` format sent
  when placing the order.
- `option_type` comes back as `Call` / `Put`, unlike the `CE` / `PE` sent when placing the order.
- `transaction_type` comes back title-cased (`Buy` / `Sell`).
- `order_timestamp` is `DD/MM/YYYY HH:MM:SS`.
- `modification_allowed` and `cancellation_allowed` are documented as `YES` / `NO` but come back
  as empty strings in the sample.
