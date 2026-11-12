# Trade Book API - All Trades

> Source: https://developer.hdfcsec.com/ir-docs/docs/trade_book

## Description

All the Trades placed for the day you will get.

The Trade Book API enables users to access data regarding the trades they've conducted on the platform. It furnishes a detailed overview of the user's trade records, encompassing information such as order ID, traded security, quantity, price, transaction type, and timestamp.

## EndPoint

```js
Method: GET
`https://developer.hdfcsec.com/oapi/v1/trades?api_key=<api_key>`
```

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Glossary of Constants

| Field | Description |
| --- | --- |
| client_id | Unique identifier for the client. |
| trade_id | Unique identifier for the trade. |
| order_id | Unique identifier for the order. |
| exchange | The exchange where the trade occurred. |
| security_id | Unique identifier for the security. |
| product | The type of product (e.g., CNC). |
| average_price | The average price of the trade. |
| filled_quantity | The quantity filled for the trade. |
| pending_quantity | The quantity pending for the trade. |
| exchange_order_id | Unique identifier for the order on the exchange. |
| transaction_type | The type of transaction (e.g., BUY). |
| fill_timestamp | Timestamp when the trade was filled. |
| company_name | Name of the company associated with the security. |
| underlying_symbol | Symbol of the underlying security. |
| instrument_segment | Segment of the instrument (if applicable). |
| expiry_date | Expiry date of the security (if applicable). |
| strike_price | Strike price of the security (if applicable). |
| option_type | Type of option (if applicable). |
| isin | International Securities Identification Number. |
| status | Status of the trade/order. |
| validity | Validity of the order (if applicable). |
| total_traded_value | Total traded value of the security. |
| order_source | Source of the order (e.g. MyCustomApp). |

## Request Curl

```js
curl --location 'https://developer.hdfcsec.com/oapi/v1/trades?api_key=api_key' \
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
            "trade_id": "429366220",
            "order_id": "24043000528594",
            "exchange": "NSE",
            "product": "OVERNIGHT",
            "average_price": 146.35,
            "filled_quantity": 15,
            "pending_quantity": 0,
            "exchange_order_id": "1600000331304144",
            "transaction_type": "SELL",
            "fill_timestamp": "30/04/2024 14:27:49",
            "security_id": "BANKNIFTY",
            "company_name": "BANKNIFTY",
            "underlying_symbol": "BANKNIFTY",
            "instrument_segment": "OPTIDX",
            "expiry_date": "30 APR 2024",
            "strike_price": 49900.0,
            "option_type": "Call",
            "isin": "",
            "status": "Traded",
            "validity": "DAY",
            "total_traded_value": 2195.25,
            "order_source": "C",
            "order_type": "MARKET"
        }
  ]
}
```

> **Note:** this endpoint returns `snake_case` keys. The [Single Trade API](13-single-trade.md)
> returns the same data in `camelCase` — the two are not interchangeable.
