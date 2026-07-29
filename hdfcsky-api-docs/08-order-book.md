# Order Book

Retrieve pending and completed orders, per-order history, and the trade book.

## Contents

- [Fetch Pending Order](#fetch-pending-order)
- [Fetch Completed Order](#fetch-completed-order)
- [Order History](#order-history)
- [Trade Book](#trade-book)

---

## Fetch Pending Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/order_book/fetchpendingorder

This API is used to fetch all the pending orders.

### HTTP Request

```js
Method: GET
Endpoint: /oapi/v1/orders
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

### Query Params

| Field Name | Data Type | Description |
|---|---|---|
| type | String | Can be among ("pending", "completed") |
| client_id | String | Client's ID |
| source | String | Order source (optional). Default will be the host URL calling the API |
| tags | Array of String | Order tags (optional) |
| api_key | String | The API key used for authentication |

```js
{
    "type": "pending",
    "client_id": "DEMO1",
    "api_key": "The API key used for authentication"
}
```

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/orders?type=pending&client_id=DEMO1&api_key=api_key' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Authorization: <access_token>'
```

### Response

```js
         {
    "data":{
        "orders": [
        {
            "trading_symbol": "PNB-EQ",
            "average_trade_price": 0,
            "exchange": "NSE",
            "pro_cli": "CLIENT",
            "market_protection_percentage": 0,
            "order_entry_time": 1605682535,
            "mode": "NEW",
            "oms_order_id": "200018000000003",
            "trailing_stop_loss":{
            },
            "deposit": 0,
            "square_off_value":{
            },
            "disclosed_quantity": 0,
            "stop_loss_value":{
            },
            "price": 27.8,
            "order_tag": "",
            "device": "WEB",
            "remaining_quantity": 1,
            "last_activity_reference": 1290169535358022400,
            "average_price": 0,
            "square_off?": false,
            "order_status_info": "",
            "quantity": 1,
            "execution_type": "REGULAR",
            "client_id": "DEMO1",
            "exchange_time": 1605682535,
            "order_side": "BUY",
            "login_id": "DEMO1",
            "validity": "DAY",
            "instrument_token": 10666,
            "product": "MIS",
            "trigger_price": 0,
            "segment": "",
            "trade_price": 0,
            "order_type": "LIMIT",
            "contract_description":{
            }
            "rejection_code": 0,
            "leg_order_indicator": "",
            "exchange_order_id": "1200000007823258",
            "order_status": "CONFIRMED",
            "filled_quantity": 0,
            "target_price_type": "absolute",
            "is_trailing": false,
            "user_order_id": "10002",
            "lot_size": 1,
            "series": "",
            "nnf_id": 111111111111100,
            "rejection_reason": "NONE"
        }]
    },
    "message": "",
    "status": "success"
}
```

### Error Response

```js
{
    "status": "error",
    "message": "Request forbidden",
    "error_code": 40000,
    "data":{}
}
```

---

## Fetch Completed Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/order_book/fetchcompletedorder

This API is used to fetch all the completed orders.

### HTTP Request

```js
Method: GET
Endpoint: /oapi/v1/orders
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

### Query Params

| Field Name | Data Type | Description |
|---|---|---|
| type | String | Can be among ("pending", "completed") |
| client_id | String | Client's ID |
| source | String | Order source (optional). Default will be the host URL calling the API |
| tags | Array of String | Order tags (optional) |
| api_key | String | The API key used for authentication |

```js
{
    "type": "completed",
    "client_id": "DEMO1",
    "api_key": "The API key used for authentication"
}
```

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/orders?type=completed&client_id=DEMO1&api_key=api_key' \
--header 'Authorization: <access_toke>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

### Response

```js
{
 "data":{
     "orders": [
     {
         "trading_symbol": "GOLDGUINEA20DECFUT",
         "average_trade_price": 0,
         "exchange": "MCX",
         "pro_cli": "CLIENT",
         "market_protection_percentage": 100,
         "order_entry_time": 1605683238,
         "mode": "NEW",
         "oms_order_id": "200018000000003",
         "trailing_stop_loss":{
         },
         "deposit": 0,
         "square_off_value":{
         },
         "disclosed_quantity": 1,
         "stop_loss_value":{
         },
         "price": 40692,
         "order_tag": "",
         "device": "UNKNOWN",
         "remaining_quantity": 0,
         "last_activity_reference": 0,
         "average_price": 40692,
         "square_off?": false,
         "order_status_info": "",
         "quantity": 1,
         "execution_type": "REGULAR",
         "client_id": "DEMO1",
         "exchange_time": 1605683260,
         "order_side": "BUY",
         "login_id": "ADMIN1",
         "validity": "DAY",
         "instrument_token": 224417,
         "product": "NRML",
         "trigger_price": 0,
         "segment": "",
         "trade_price": 0,
         "order_type": "MARKET",
         "contract_description":{
         },
         "rejection_code": 0,
         "leg_order_indicator": "",
         "exchange_order_id": "202032300187889",
         "order_status": "COMPLETE",
         "filled_quantity": 1,
         "target_price_type": "absolute",
         "is_trailing": false,
         "user_order_id": "900005",
         "lot_size": 8,
         "series": "",
         "nnf_id": 500029001001010,
         "rejection_reason": "NONE"
     }]
 },
 "message": "",
 "status": "success"
}
```

### Error Response

```js
{
    "status": "error",
    "message": "Request forbidden",
    "error_code": 40000,
    "data":{
    }
}
```

---

## Order History

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/order_book/orderhistory

This API is used to get the history of Pending & Completed Orders. You can get the information like status, order type, Avg. & trigger price etc.

### HTTP Request

```js
Method: GET
Endpoint: /oapi/v1/order/<oms_order_id>/history
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

### Query Params

```js
{
    "client_id": "DEMO1",
    "api_key": "The API key used for authentication"
}
```

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1//oapi/v1/order/<oms_order_id>/history?api_key=api_key&client_id=DEMO1' \
--header 'Authorization: <access_token>'\
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

### Response

```js
{
    "data":{
        "order history": [
        {
            "avg_price": 40672,
            "client_id": "DEMO1",
            "client_order_id": "900005",
            "created_at": 1605683202,
            "disclosed_quantity": 1,
            "exchange": "MCX",
            "exchange_order_id": "202032300187427",
            "exchange_time": 0,
            "fill_quantity": 1,
            "last_modified": 1605683202477299000,
            "login_id": "DEMO1",
            "modified_at": 1605683202,
            "order_id": "63904ddd-df0c-4546-bbdc-4c21c0796f5b",
            "order_mode": "NEW",
            "order_side": "SELL",
            "order_type": "LIMIT",
            "price": 40672,
            "product": "NRML",
            "quantity": 1,
            "reject_reason": "NONE",
            "remaining_quantity": 0,
            "segment": "FutOpt",
            "status": "COMPLETE",
            "symbol": "GOLDGUINEA",
            "token": 224417,
            "trigger_price": 0,
            "underlying_token": 425,
            "validity": "DAY"
        }],
        "message": "",
        "status": "success"
    }
}
```

### Error Response

```js
{
    "status": "error",
    "message": "Request forbidden",
    "error_code": 40000,
    "data":{}
}
```

---

## Trade Book

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/order_book/tradebook

This API is used to get all the detailes of trading.

### HTTP Request

```js
Method: GET
Endpoint: /oapi/v1/trades
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

### Query Params

```js
{
    "client_id": "DEMO1",
    "api_key": "The API key used for authentication"
}
```

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/trades?type=pending&client_id=DEMO1&api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

### Response

```js
{
 "data":{
     "trades": [
     {
         "book_type": "0",
         "broker_id": "12345",
         "client_id": "DEMO1",
         "disclosed_vol": 0,
         "disclosed_vol_remaining": 0,
         "exchange": "NSE",
         "exchange_order_id": "1300000005790553",
         "exchange_time": 1605677129,
         "fill_number":{
         },
         "filled_quantity": 1,
         "good_till_date": 0,
         "instrument_token": 11915,
         "login_id": "DEMO1",
         "oms_order_id": "200018000000003",
         "order_entry_time": 1605677128,
         "order_price": 14.7,
         "order_side": "BUY",
         "order_type": "MARKET",
         "original_vol": 1,
         "pro_cli": 0,
         "product": "MIS",
         "remaining_quantity": 0,
         "trade_number": "76817533",
         "trade_price": 14.7,
         "trade_quantity": 1,
         "trade_time": 1605677129,
         "trading_symbol": "YESBANK-EQ",
         "trigger_price":{
         },
         "v_login_id":{
         },
         "vol_filled_today": 1
     }]
 },
 "message": "",
 "status": "success"
}
```

### Error Response

```js
{
    "status": "error",
    "message": "Request forbidden",
    "error_code": 40000,
    "data":{}
}
```
