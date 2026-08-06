# Single Order Status API

> Source: https://developer.hdfcsec.com/ir-docs/docs/single_order

## Description

The API gives you detail about the order placed by User.

## EndPoint

```js
Method: GET
`https://developer.hdfcsec.com/oapi/v1/orders/:order_id?api_key=<api_key>`
```

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Query Params

- `api_key`: The API key used for authentication.

## Glossary of constants

| Field Name | Description |
| --- | --- |
| `status` | Indicates the status of the order (success for successful operation). |
| `data` | Contains an array of order objects. |
| `client_id` | Unique identifier for the client. |
| `order_id` | Unique identifier for the order. |
| `exchange_order_id` | Unique identifier for the order in the exchange. |
| `status_message` | Rejection or RMS error reason (needs mapping with Snapwork). |
| `status_message_raw` | Raw status message for rejection or RMS error (needs mapping with Snapwork). |
| `order_timestamp` | Timestamp when the order was placed. |
| `exchange` | Exchange where the order was placed. |
| `security_id` | Unique identifier for the security. |
| `company_name` | Name of the company associated with the security. |
| `underlying_symbol` | Symbol of the underlying asset. |
| `instrument_segment` | Segment of the instrument (EQUITY, FUTSTK, OPTSTK, etc.). |
| `expiry_date` | Expiry date of the instrument (yyyymmdd). |
| `strike_price` | Strike price of the instrument. |
| `option_type` | Type of option (CALL or PUT). |
| `isin` | ISIN (International Securities Identification Number) of the security. |
| `transaction_type` | Type of transaction (BUY or SELL). |
| `validity` | Validity of the order (typically DAY). |
| `product` | Product code. |
| `quantity` | Total quantity of the order. |
| `disclosed_quantity` | Disclosed quantity (if applicable). |
| `price` | Price per unit. |
| `trigger_price` | Trigger price (if applicable). |
| `filled_quantity` | Quantity filled. |
| `pending_quantity` | Quantity pending. |
| `average_price` | Average price (optional, retrieved from Trade Book API of TCS). |
| `total_traded_value` | Total traded value. |
| `order_source` | Source of the order. |
| `order_subchannel` | Subchannel of the order. |
| `modification_allowed` | Indicates if modification is allowed (YES or NO). |
| `cancellation_allowed` | Indicates if cancellation is allowed (YES or NO). |
| `token_id` | Token identifier. |
| `order_slot` | Slot of the order (Online or AMO). |
| `good_till_date` | Good till date (yyyymmdd). |
| `external_reference_rumber` | External reference number associated with the order. |

## Request Curl

```js
   curl --location 'https://developer.hdfcsec.com/oapi/v1/orders/24043000292428?api_key=api_key' \
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
            "order_id": "24043000292428",
            "exchange_order_id": "1600000131156899",
            "status": "Traded",
            "status_message": "",
            "status_message_raw": "",
            "order_timestamp": "30/04/2024 10:59:27",
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
            "transaction_type": "Sell",
            "validity": "DAY",
            "product": "INTRADAY",
            "quantity": 15,
            "disclosed_quantity": 0,
            "price": 0.0,
            "trigger_price": 0.0,
            "filled_quantity": 15,
            "pending_quantity": 0,
            "average_price": 0.0,
            "total_traded_value": 876.75,
            "order_source": "C",
            "order_subchannel": "C",
            "modification_allowed": "",
            "cancellation_allowed": "",
            "token_id": "NSEDNL49599",
            "order_slot": "Online",
            "good_till_date": "",
            "external_reference_number": "STAPI202404306801535",
            "modified": false,
            "instrument_token": 0,
            "order_type": "MARKET",
            "cancelled_quantity": 0,
            "market_protection": 0
        }
  ]
}
```

> Note that `data` is an array even for a single order, and that the response shape is identical
> to [Order Status API - All orders](10-order-book.md). The `expiry_date` is documented as
> `yyyymmdd` and `option_type` as `CALL`/`PUT`, but the sample returns `30 APR 2024` and `Call`.
