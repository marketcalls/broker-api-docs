# Place Order - Order API

> Source: https://developer.hdfcsec.com/ir-docs/docs/place_order

## Description

Using the Place Order API, users can initiate orders (both buying and selling) for various instruments such as equities and derivatives. These orders are then transmitted to the Order Management System (OMS). However, it's important to note that the execution of an order is subject to factors like market hours, fund availability, and risk parameters, and there is no guarantee of execution at the exchange.

## EndPoint

```js
Method: POST
`https://developer.hdfcsec.com/oapi/v1/orders/regular?api_key=<api_key>`
```

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Query Params

- `api_key`: The API key used for authentication.

## Glossary of constants

Here are several of the constant enum values used for placing orders.

| Parameters | Values | Description |
| --- | --- | --- |
| order_type | MARKET | Market order |
|  | LIMIT | Limit order |
|  | SL | Stoploss order |
|  | SL-M | Stoploss-market order |
| product | DELIVERY | Cash & Carry for equity |
|  | OVERNIGHT | Overnight for futures and options |
|  | INTRADAY | Intraday Squareoff for Equity, futures and options |
|  | MTF | Margin Trading Facility for Equity |
|  | COLL-SELL | Sell Pledged Equity stocks |
|  | ENCASH | Get funds same day for Equity Sell |
| validity | DAY | Regular order |
|  | IOC | Immediate or Cancel |
|  | GTD | Good Till Date Order |

## Request Parameters

| Parameters | Description | Remarks |
| --- | --- | --- |
| exchange | Name of the exchange (NSE, BSE) | Required |
| security_id | Exchange standard id for each scrip. Find this ID in Security Master. | Required |
| expiry_date | This is applicable for F&O. Format will be YYYY-MM-DD | Required for Futures, Options, Currency Futures and Currency Options |
| strike_price | Strike Price for Options | Required for Options and Currency Options |
| option_type | Type of Options like CALL, PUT | Required for Options and Currency Options |
| transaction_type | BUY or SELL | Required |
| instrument_segment | EQUITY for Equity segment<br>OPTIDX for Index options<br>OPTSTK for Stocks Options<br>FUTIDX for Index Futures<br>FUTSTK for Stock Futures<br>OPTCUR for Currency Options<br>FUTCUR for Currency Futures | Required |
| product | According to product margin will be blocked. `DELIVERY, OVERNIGHT, INTRADAY, MTF etc` | Required |
| quantity | Quantity to transact. For derivatives also mention Quantity. | Required |
| order_type | Order type (MARKET, LIMIT, SL-L, SL-M) | Required |
| price | The price to execute the order at (for LIMIT orders and SL Orders) | Required for LIMIT and SL |
| trigger_price | The price at which an order should be triggered (SL, SL-M) | Required for SL and SL-M |
| disclosed_quantity | Quantity to disclose publicly (for equity trades) | Optional |
| validity | Order validity (DAY, IOC, GTD). | Required |
| amo | After Market Order (true, false) | Optional |
| external_reference_number | An optional reference number can be sent along with order for tracking the order sent (numeric, Max length 20) | Optional |

> **Inconsistencies in the official docs, preserved verbatim above:**
> - `expiry_date` is documented as `YYYY-MM-DD` but every worked example sends `YYYYMMDD`
>   (e.g. `"expiry_date": "20240425"`).
> - `option_type` is documented as `CALL` / `PUT` but the examples send `CE` / `PE`.
> - `transaction_type` is documented as `BUY` / `SELL` but the examples send `Buy`.
> - `order_type` is listed as `SL` in the enum table and `SL-L` in the parameter table.
> - Derivative examples also send an `underlying_symbol` field that is not in the parameter table.

## Equity Limit Order

### Request Curl for Equity Limit Order

```js
curl --location 'https://developer.hdfcsec.com/oapi/v1/orders/regular?api_key=api_key' \
--header 'Authorization: access_token' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '{ 
"exchange": "NSE" ,
"security_id":"WIPLTDEQNR",
"instrument_segment":"EQUITY" ,
"transaction_type":"Buy" ,
"product":"DELIVERY" ,
"order_type":"LIMIT" ,
"price":458,
"trigger_price" : 0,
"quantity":1 ,
"disclosed_quantity": 0,
"validity":"DAY" ,
"amo":false,
"external_reference_number":123456789 
}'
```

### Response for Equity Limit Order

```js
  {
      "status": "success",
      "data": {
          "order_id": "24042500000504"
      }
  }
```

## Index Option

### Request Curl for Index Option

```js
curl --location 'https://developer.hdfcsec.com/oapi/v1/orders/regular/?api_key=<api_key>' \
--header 'Authorization: access_token' \
--header 'Content-Type: application/json' \
--header  'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '
{ "exchange": "NSE" ,
"security_id":"68180",
"underlying_symbol":"NIFTYEQEQNR",
"instrument_segment":"OPTIDX" ,
"transaction_type":"Buy" ,
"product":"OVERNIGHT" ,
"order_type":"MARKET" ,
"price":0,
"trigger_price" : 0,
"quantity":50 ,
"disclosed_quantity": 0,
"option_type":"CE" ,
"strike_price": 22400, 
"expiry_date": "20240425",
"validity":"DAY" ,
"amo":false,
"external_reference_number":123456789 
}'
```

### Response for Index Option

```js
  {
      "status": "success",
      "data": {
          "order_id": "230425002100904"
      }
  }
```

## Index Future

### Request Curl for Index Future

```js
curl --location 'https://developer.hdfcsec.com/oapi/v1/orders/regular/?api_key=<api_key>' \
--header 'Authorization: access_token' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '
{ "exchange": "NSE" ,
"security_id":"52222",
"underlying_symbol":"NIFTYEQEQNR",
"instrument_segment":"FUTIDX" ,
"transaction_type":"Buy" ,
"product":"OVERNIGHT" ,
"order_type":"MARKET" ,
"price":0,
"trigger_price" : 0,
"quantity":50 ,
"disclosed_quantity": 0,
"expiry_date": "20240425",
"validity":"DAY" ,
"amo":false,
"external_reference_number":123456789 
}'
```

### Response for Index Future

```js
  {
      "status": "success",
      "data": {
          "order_id": "23042500000905"
      }
  }
```
