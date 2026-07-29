# Conditional Orders (Bracket & Cover)

Bracket Orders (BO) and Cover Orders (CO) — place, modify and exit.

## Contents

- [Place BO Order](#place-bo-order)
- [Modify BO Order](#modify-bo-order)
- [Exit BO Order](#exit-bo-order)
- [Place CO Order](#place-co-order)
- [Modify CO Order](#modify-co-order)
- [Exit CO Order](#exit-co-order)

---

## Place BO Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/conditional_orders/placeboorder

Bracket order is used to place a stop loss and a target order alongside a regular order . Stoploss order covers the loss for the trader while the target order ensures the profitability in the trade.

### HTTP Request

```js
   Method: POST
   Endpoint: /oapi/v1/orders/kart
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}
```

### Query Params

```js
{
    "api_key": "The API key used for authentication",
}
```

### Body Params

| Field Name | Data Type | Description |
|---|---|---|
| exchange | String | NSE,BSE,NFO,CDS,MCX |
| instrument_token | String | Represents the unique id of instrument. |
| client_id | String | Represents the unique id of user or username. |
| order_type | String | LIMIT,MARKET,SL,SLM |
| price | Number | It can't be Zero. |
| quantity | Number | It can't be Zero. |
| disclosed_quantity | Number | It can't be negative number. |
| validity | String | DAY or IOC |
| product | String | CNC,MIS,NRML |
| order_side | String | BUY or SELL |
| device | String | Web or Mobile |
| user_order_id | Number | Represents the unique id of order. |
| trigger_price | Number | It can't be Zero. |
| stop_loss_value | Number | It can't be negative number. |
| square_off_value | Number | It can't be negtive number. |
| trailing_stop_loss | Number | It can't be negative number. |
| is_trailing | Boolean | TRUE or FALSE |
| execution_type | String | BO |

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/orders/kart?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '      {
         "client_id": "TEST123",
         "device": "WEB",
         "disclosed_quantity": 0,
         "exchange": "NSE",
         "execution_type": "BO",
         "instrument_token": "3045",
         "is_trailing": true,
         "order_side": "BUY",
         "order_type": "LIMIT",
         "price": 740.95,
         "product": "MIS",
         "quantity": 1,
         "square_off_value": 1,
         "stop_loss_value": 1,
         "trailing_stop_loss": "0.05",
         "trigger_price": 0,
         "user_order_id": 10002,
         "validity": "DAY"
      }'
```

### Response

```js
{
"data": {
   "data": {
      "basket_id": "20210531-19",
      "message": "basket Order Placed Successfully"
   }
},
"message": "Order place successfully",
"status": "success"
}
```

### Error Response

```js
{
     "data": {},
     "error_code": 48001,
     "message": "`order_info` Hedge basket feature enabled only for NIFTY 50 & NIFTY BANK as underlying",
     "status": "error"
}
```

---

## Modify BO Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/conditional_orders/modifyboorder

This API is used to modify Bracket Orders.

### HTTP Request

```js
Method: PUT
Endpoint: /oapi/v1/orders/kart
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}
```

### Query Params

```js
{
    "api_key": "The API key used for authentication",
}
```

### Body Params

| Field Name | Data Type | Description |
|---|---|---|
| exchange | String | NSE, BSE, NFO, CDS, MCX |
| instrument_token | String | Represents the unique id of instrument. |
| client_id | String | Represents the unique id of user or username. |
| order_type | String | LIMIT, MARKET, SL, SLM |
| price | Number | It can't be Zero. |
| quantity | Number | It can't be Zero. |
| disclosed_quantity | Number | It can't be negative number. |
| validity | String | DAY or IOC |
| product | String | CNC, MIS, NRML |
| user_order_id | Number | Represents the unique id of order. |
| filled_quantity | Number | Number of quantity which are traded. |
| remaining_quantity | Number | Number of quantity which are pending. |
| last_activity_reference | Number | Unique id of Last modification. |
| trigger_price | Number | It can't be Zero. |
| stop_loss_value | Number | It can't be negative number. |
| square_off_value | Number | It can't be negative number. |
| trailing_stop_loss | Number | It can't be negative number. |
| is_trailing | Boolean | TRUE or FALSE |
| execution_type | String | BO |

### Request Curl

```js
      curl --location --request PUT 'https://developer.hdfcsky.com/oapi/v1/orders/kart?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '      {
      "exchange": "NSE",
      "instrument_token": 3045,
      "client_id": "TEST123",
      "order_type": "LIMIT",
      "price": 456.95,
      "quantity": "3",
      "disclosed_quantity": 0,
      "validity": "DAY",
      "product": "MIS",
      "oms_order_id": "20220106-88",
      "exchange_order_id": "1100000000004797",
      "filled_quantity": 0,
      "remaining_quantity": 2,
      "last_activity_reference": 1325938440097498600,
      "trigger_price": 0,
      "stop_loss_value": 0,
      "square_off_value": 0,
      "trailing_stop_loss": 0,
      "is_trailing": false,
      "execution_type": "BO"
  }   '
```

### Response

```js
{
    "data": {
        "basket_id": "",
        "message": "basket Order modified Successfully"
    },
    "message": "Order modified successfully",
    "status": "success"
}
```

### Error Response

```js
{
    "data": {},
    "error_code": 44000,
    "message": "`trigger_price` is invalid",
    "status": "error"
}
```

---

## Exit BO Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/conditional_orders/exitboorder

This API is used to EXIT Bracket Orders.

### HTTP Request

```js
Method: DELETE
Endpoint: /oapi/v1/orders/kart/<oms_order_id>
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}
```

### Query Params

```js
{
    "api_key": "The API key used for authentication",
}
```

### Body Params

| Field Name | Data Type | Description |
|---|---|---|
| client_id | String | Represents the unique id of user or username. |
| user_order_id | Number | Represents the unique id of order. |
| execution_type | String | BO |
| exchange_order_id | Number | Represents the unique id of order. |
| leg_order_indicator | String | Entry, Second or Third |
| status | String | Confirmed |

### Request Curl

```js
curl --location --request DELETE 'https://developer.hdfcsky.com/oapi/v1/orders/kart/<oms_order_id>?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '{
    "client_id": "TEST123",
    "exchange_order_id": "1100000000006951",
    "execution_type": "BO",
    "leg_order_indicator": "ENTRY",
    "oms_order_id": "20220106-106",
    "status": "CONFIRMED"
}'
```

### Response

```js
     {
         "data": {
             "basket_id": "",
             "message": "Order Cancelled Successfully"
         },
         "message": "",
         "status": "success"
     }
```

### Error Response

```js
{
   "data": {},
   "error_code": 44000,
   "message": "`exchange_order_id` can't be blank",
   "status": "error"
}
```

---

## Place CO Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/conditional_orders/placecoorder

Cover Order is used to place a stop loss order alongside a regular order. This is to cover the losses when the price goes against the expected behaviour of trader. When buying a CO order, limit price has to be higher than the stop-loss trigger price, and when selling a CO order, the limit price has to be lower than the stop loss trigger price.

### HTTP Request

```js
Method: POST
Endpoint: /oapi/v1/orders/kart
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}
```

### Query Params

```js
{
    "api_key": "The API key used for authentication",
}
```

### Body Params

| Field Name | Data Type | Description |
|---|---|---|
| exchange | String | NSE, BSE, NFO, CDS, MCX |
| instrument_token | String | Represents the unique id of instrument. |
| client_id | String | Represents the unique id of user or username. |
| order_type | String | LIMIT, MARKET, SL, SLM |
| price | Number | It can't be Zero. |
| quantity | Number | It can't be Zero. |
| disclosed_quantity | Number | It can't be negative number. |
| validity | String | DAY or IOC |
| product | String | CNC, MIS, NRML |
| order_side | String | BUY or SELL |
| device | String | Web or Mobile |
| user_order_id | Number | Represents the unique id of order. |
| execution_type | String | CO |
| stop_loss_value | Number | It can't be negative number. |
| trailing_stop_loss | Number | It can't be negative number. |

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/orders/kart?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '  {
      "exchange": "NSE",
      "instrument_token": "1624",
      "client_id": "TEST123",
      "order_type": "LIMIT",
      "price": 91.3,
      "quantity": 1,
      "disclosed_quantity": 0,
      "validity": "DAY",
      "product": "MIS",
      "order_side": "BUY",
      "device": "WEB",
      "user_order_id": 10002,
      "execution_type": "CO",
      "stop_loss_value": 2,
      "trailing_stop_loss": 0
    }'
```

### Response

```js
       {
         "data":{
            "data":{
                  "basket_id": "20210531-23",
                  "message": "basket Order Placed Successfully"}
            },
            "message": "Order place successfully",
            "status": "success"
       }
```

### Error Response

```js
 {
    "data": {},
    "error_code": 44000,
    "message": "`product` is invalid",
    "status": "error"
 }
```

---

## Modify CO Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/conditional_orders/modifycoorder

This API is used to modify Cover Orders.

### HTTP Request

```js
   Method: PUT
   Endpoint: /oapi/v1/orders/kart
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}
```

### Query Params

```js
{
    "api_key": "The API key used for authentication",
}
```

### Body Params

| Field Name | Data Type | Description |
|---|---|---|
| exchange | String | NSE, BSE, NFO, CDS, MCX |
| exchange_order_id | Number |  |
| instrument_token | String | Represents the unique id of instrument. |
| client_id | String | Represents the unique id of user or username. |
| order_type | String | LIMIT, MARKET, SL, SLM |
| price | Number | It can't be Zero. |
| quantity | Number | It can't be Zero. |
| disclosed_quantity | Number | It can't be negative number. |
| validity | String | DAY or IOC |
| product | String | CNC, MIS, NRML |
| user_order_id | Number | Represents the unique id of order. |
| filled_quantity | Number | Number of quantity which are traded. |
| remaining_quantity | Number | Number of quantity which are pending. |
| last_activity_reference | Number | Unique id of Last modification. |
| stop_loss_value | Number | It can't be negative number. |
| trailing_stop_loss | Number | It can't be negative number. |
| execution_type | String | BO |

### Request Curl

```js
curl --location --request PUT 'https://developer.hdfcsky.com/oapi/v1/orders/kart?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '      {
         "client_id": "TEST123",
         "disclosed_quantity": 0,
         "exchange": "NSE",
         "exchange_order_id": "1100000000007793",
         "execution_type": "CO",
         "filled_quantity": 0,
         "instrument_token": 3045,
         "last_activity_reference": 1325941635181246200,
         "oms_order_id": "20220106-114",
         "order_type": "LIMIT",
         "price": 456.95,
         "product": "MIS",
         "quantity": "3",
         "remaining_quantity": 2,
         "stop_loss_value": 0,
         "trailing_stop_loss": 0,
         "validity": "DAY"
      }'
```

### Response

```js
{
   "data": {
      "basket_id": "",
      "message": "basket Order modified Successfully"
   },
   "message": "Order modified successfully",
   "status": "success"
}
```

### Error Response

```js
{
      "data": {},
      "error_code": 44000,
      "message": "`square_off_value` is invalid",
      "status": "error"
}
```

---

## Exit CO Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/conditional_orders/exitcoorder

This API is used to EXIT Cover Orders.

### HTTP Request

```js
    Method: DELETE
    Endpoint: /oapi/v1/orders/kart/<oms_order_id>
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}
```

### Query Params

```js
{
    "api_key": "The API key used for authentication",
}
```

### Body Params

| Field Name | Data Type | Description |
|---|---|---|
| client_id | String | Represents the unique id of user or username. |
| user_order_id | Number | Represents the unique id of order. |
| execution_type | String | BO |
| exchange_order_id | Number | Represents the unique id of order. |
| leg_order_indicator | String | Entry, Second or Third |
| status | String | Confirmed |

### Request Curl

```js
    curl --location --request DELETE 'https://developer.hdfcsky.com/oapi/v1/orders/kart/<oms_order_id>?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '     {
         "client_id": "TEST123",
         "exchange_order_id": "1100000000006951",
         "execution_type": "CO",
         "leg_order_indicator": "ENTRY",
         "oms_order_id": "20220106-106",
         "status": "CONFIRMED"
     }'
```

### Response

```js
     {
         "data": {
             "basket_id": "",
             "message": "Order Cancelled Successfully"
         },
         "message": "",
         "status": "success"
     }
```

### Error Response

```js
{
   "data": {},
   "error_code": 44000,
   "message": "`exchange_order_id` can't be blank",
   "status": "error"
}
```
