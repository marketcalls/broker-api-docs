# Regular Orders

Place, modify and delete regular and After Market Orders (AMO).

## Contents

- [Place Regular Order](#place-regular-order)
- [Modify Regular Order](#modify-regular-order)
- [Delete Regular Order](#delete-regular-order)
- [Place AMO Order](#place-amo-order)
- [Modify AMO Order](#modify-amo-order)
- [Delete AMO Order](#delete-amo-order)

---

## Place Regular Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/regular_order/placeregularorder

This API is used to place regular orders. This type of order will get executed immediately as the buyers are willing to pay a higher price for the stock than its current market price, however, if the buyer wants to wait for the market price of the stock to rise till Rs. 512, in that case, he can place a market SL Trigger Order at trigger price of Rs.512.

### HTTP Request

```js
    Method: POST
    Endpoint: /oapi/v1/orders
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
    "client_id": "DEMO1",
    "api_key": "The API key used for authentication"
}
```

### Body Params

| Field Name | Data Type | Description |
|---|---|---|
| exchange | String | NSE, BSE, NFO, CDS, MCX |
| instrument_token | String | Represents the unique id of instrument. |
| client_id | String | Represents the unique id of user or username. |
| order_type | String | LIMIT, MARKET, SL, SLM |
| amo | Boolean | TRUE or FALSE |
| price | Number | It can't be Zero. |
| quantity | Number | It can't be Zero. |
| disclosed_quantity | Number | It can't be negative number. |
| validity | String | DAY or IOC |
| product | String | CNC, MIS, NRML |
| order_side | String | BUY or SELL |
| device | String | Web or Mobile |
| user_order_id | Number | Represents the unique id of order. |
| trigger_price | Number | It can't be Zero. |
| execution_type | String | REGULAR |
| source | String | Order source (optional). Default will be the host URL calling the API |
| tags | Array | Array of strings representing order tags (optional) |

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/orders?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json' \
--data '{
      "client_id": "TEST123",
      "device": "WEB",
      "disclosed_quantity": 0,
      "execution_type": "REGULAR",
      "exchange": "NSE",
      "instrument_token": "10666",
      "is_trailing": true,
      "order_side": "BUY",
      "order_type": "LIMIT",
      "price": 127.10,
      "product": "MIS",
      "quantity": 1,
      "trailing_stop_loss": "0.00",
      "trigger_price": 0.00,
      "user_order_id": 10002,
      "validity":"DAY"
}
     '
```

### Response

```js
{
    "data":
    {
    "oms_order_id": "200018000000003",
    "user_order_id": 10002
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

## Modify Regular Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/regular_order/modifyregularorder

You can't be modified the product_type of the orders. However, you can change the order_type & validity on the basis of execution_type of the instruments. You can also change the exchange type along with quantity, price, trigger_price and disclosed_quantity.

### HTTP Request

```js
    Method: PUT
    Endpoint: /oapi/v1/orders
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
    "api_key": "The API key used for authentication"
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
| oms_order_id | Number | Represents the unique id of order given by OMS. |
| trigger_price | Number | It can't be Zero. |
| execution_type | String | REGULAR, BO, CO, AMO |

### Request Curl

```js
curl --location --request PUT 'https://developer.hdfcsky.com/oapi/v1/orders?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json' \
--data '     {
    "exchange": "NSE",
    "instrument_token": 10666,
    "client_id": "DEMO1",
    "order_type": "LIMIT",
    "price": "34.30",
    "quantity": 1,
    "disclosed_quantity": 0,
    "validity": "DAY",
    "product": "MIS",
    "oms_order_id": "200018000000003",
    "trigger_price": 0,
    "execution_type": "REGULAR"
  }'
```

### Response

```js
{
    "data":{"oms_order_id": "200018000000003"},
    "message": "Order modification request submitted",
    "status": "success"
}
```

### Error Response

```js
{
   "data":{},
   "error_code": 45010,
   "message": "Something went wrong",
   "status": "error"
}
```

---

## Delete Regular Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/regular_order/deleteregularorder

This API is used to delete/cancel order the existing orders.

### HTTP Request

```js
  Method: DELETE
  Endpoint: /oapi/v1/orders/<oms_order_id>
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
    "client_id": "SC3013",
    "execution_type": "REGULAR",
    "api_key": "The API key used for authentication"
}
```

### Request Curl

```js
curl --location --request DELETE 'https://developer.hdfcsky.com/oapi/v1/orders/<oms_order_id>?api_key=api_key&client_id=test123@gmail.com&execution_type=REGULAR' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json'
```

### Response

```js
{
    "data": {"oms_order_id": "20211103-50"},
    "message": "Order cancellation request submitted for OMS Order: 20211103-50",
    "status": "success"
}
```

### Error Response

```js
{
    "status": "error",
    "message": "Request Unauthorised",
    "error_code": 40000,
    "data":{}
}
```

---

## Place AMO Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/regular_order/placeamoorder

This API is used to place After Market Orders(AMO).This allows buyers/sellers to place buy/sell orders after regular market hours. When placing an AMO order, the closing price must be considered.

### HTTP Request

```js
Method: POST
Endpoint: /oapi/v1/orders
```

### Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
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
| trigger_price | Number | It can't be Zero. |
| execution_type | String | BO |

### Query Params

```js
{
    "api_key": "The API key used for authentication"
}
```

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/orders?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '{
"exchange": "NSE",
"instrument_token": "22",
"client_id": "TEST123",
"order_type": "LIMIT",
"price": 2208.45,
"quantity": 1,
"disclosed_quantity": 0,
"validity": "DAY",
"product": "MIS",
"order_side": "BUY",
"device": "WEB",
"user_order_id": 10002,
"trigger_price": 0,
"execution_type": "AMO"
}'
```

### Response

```js
{
    "data": {
      "oms_order_id": "20211103-25"
    },
    "message": "Order Placed Successfully",
    "status": "success"
}
```

### Error Response

```js
{
    "data": {},
    "error_code": 45000,
    "message": "Error from backend: (1)-Trigger price cannot be less than last trade price.",
    "status": "error"
}
```

---

## Modify AMO Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/regular_order/modifyamoorder

Here,you can modify the placed amo orders.you can change the order_type & validity on the basis of execution_type of the instruments. You can also change the exchange type along with quantity, price and disclosed_quantity.

### HTTP Request

```js
Method: PUT
Endpoint: oapi/v1/orders
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
    "api_key": "The API key used for authentication"
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
| product | String | CNC, MIS, NORMAL |
| user_order_id | Number | Represents the unique id of order. |
| filled_quantity | Number | Number of quantity which are traded. |
| remaining_quantity | Number | Number of quantity which are pending. |
| last_activity_reference | Number | Unique id of Last modification. |
| trigger_price | Number | It can't be Zero. |
| execution_type | String | AMO |

### Request Curl

```js
curl --location --request PUT 'https://developer.hdfcsky.com/oapi/v1/orders?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '{
"exchange": "NSE",
"instrument_token": 10666,
"client_id": "TEST123",
"order_type": "LIMIT",
"price": 130.25,
"quantity": "1",
"disclosed_quantity": 1,
"validity": "DAY",
"product": "MIS",
"oms_order_id": "202405088",
"exchange_order_id": "",
"filled_quantity": 0,
"remaining_quantity": 2,
"last_activity_reference": 0,
"trigger_price": 0,
"execution_type": "AMO"
}'
```

### Response

```js
{
    "data":{
        "oms_order_id": "20220106-117"
    },
    "message": "Order modification request submitted",
    "status": "success"
}
```

### Error Response

```js
{
    "data":{
    },
    "error_code": 45010,
    "message": "Something went wrong",
    "status": "error"
}
```

---

## Delete AMO Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/orders/regular_order/deleteamoorder

Here,you can modify the placed amo orders.you can change the order_type & validity on the basis of execution_type of the instruments. You can also change the exchange type along with quantity, price and disclosed_quantity.

### HTTP Request

```js
Method: DELETE
Endpoint: oapi/v1/orders
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
    "client_id": "SC3013",
    "execution_type": "AMO",
    "api_key": "The API key used for authentication"
}
```

### Request Curl

```js
curl --location --request DELETE 'https://developer.hdfcsky.com/oapi/v1/orders/kart/<oms_order_id>?api_key=api_key&client_id=test123@gmail.com&execution_type=AMO' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

### Response

```js
{
    "data": {"oms_order_id": "20220106-77"},
    "message": "Order cancellation request submitted for OMS Order: 20220106-77",
    "status": "success"
}
```

### Error Response

```js
{
    "status": "error",
    "message": "Request Unauthorised",
    "error_code": 40000,
    "data":{}
}
```
