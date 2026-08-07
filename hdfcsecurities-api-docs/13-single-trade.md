# Single Trade API

> Source: https://developer.hdfcsec.com/ir-docs/docs/trade_book_single_trading

## Description

Get the trade based on specific order id for the day.

## EndPoint

```js
Method: GET
`https://developer.hdfcsec.com/oapi/v1/orders/:order_id/trades?api_key=<api_key>`
```

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Query Params

- `api_key`: The API key used for authentication.

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
curl --location 'https://developer.hdfcsec.com/oapi/v1/orders/3344520000068685309/trades?api_key=api_key' \
--header 'Authorization: access_token' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

## API Response

```js
{
    "status": "success",
    "data": [
        {
            "tradeId": "429366220",
            "orderId": "24043000528594",
            "exchange": "NSE",
            "securityId": "BANKNIFTY",
            "product": "OVERNIGHT",
            "averagePrice": 146.35,
            "filledQuantity": 15,
            "pendingQuantity": 0,
            "exchangeOrderId": "1600000331304144",
            "transactionType": "SELL",
            "fillTimestamp": "30/04/2024 14:27:49",
            "companyName": "BANKNIFTY",
            "underlyingSymbol": "BANKNIFTY",
            "instrumentSegment": "OPTIDX",
            "expiryDate": "30 APR 2024",
            "strikePrice": 49900.0,
            "optionType": "Call",
            "isin": "",
            "status": "Traded",
            "validity": "1",
            "totalTradedValue": 2195.25,
            "orderSource": "C",
            "instrumentToken": null,
            "orderTimestamp": null,
            "exchangeTimestamp": null,
            "orderType": "MARKET",
            "client_id": "1234567"
        }
    ]
}
```

> **Key-casing warning:** the glossary above is written in `snake_case` (copied from the Trade Book
> page) but this endpoint actually returns **`camelCase`** keys — `tradeId`, `orderId`,
> `averagePrice`, `filledQuantity`, and so on. The single exception is `client_id`, which stays
> `snake_case`. Also note `validity` is returned as the numeric string `"1"` here rather than
> `"DAY"`, and `instrumentToken` / `orderTimestamp` / `exchangeTimestamp` are `null`.
