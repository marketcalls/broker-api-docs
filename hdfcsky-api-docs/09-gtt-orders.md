# GTT Orders

Good Till Triggered (GTT) orders — place, modify, cancel and fetch.

## Contents

- [Create GTT Order](#create-gtt-order)
- [Modify GTT Orders](#modify-gtt-orders)
- [Cancel GTT order](#cancel-gtt-order)
- [Fetch GTT order](#fetch-gtt-order)

---

## Create GTT Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/gttorders/placegttorder

This API is used to place the gtt order. We can search the instrument and place order accordingly. Good Till Triggered is active until the trigger condition is met. The trigger is valid for a year. And whenever the price condition within this period is met, the order will be placed and executed, provided there are enough funds in the trading account, and the limit price order is filled on the exchange.

### HTTP request

```js
      Method : POST
      Endpoint : oapi/v1/event/gtt
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

| FieldName | Datatype | Description |
|---|---|---|
| action_type | String | singe_order |
| expiry_time | String | Represents particular date of expiry. |
| client_id | String | Represents unique id of user or username. |
| device | String | Web,Mobile |
| disclosed_quantity | Number | It can't be negative number. |
| exchange | String | NSE,BSE,NFO,CDS,MCX |
| instrument_token | String | Represents the unique id of instrument. |
| market_protection_percentage | String |  |
| order_side | String | BUY or SELL |
| order_type | String | LIMIT,MARKET,SL,SLM |
| price | Number | It can't be Zero. |
| product | String | CNC,MIS,NRML |
| quantity | Number | It can't be Zero. |
| sl_order_price | Number | It can't be Zero. |
| sl_order_quantity | Number | It can't be Zero. |
| sl_tigger_price | Number | It can't be Zero. |
| trigger_price | Number | It can't be Zero. |
| user_order_id | Number | Represents the unique id of order. |

### Request Curl

```js
curl --location --request POST 'https://uat-developer.hdfcsky.com/oapi/v1/event/gtt?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '
   {
        "action_type": "single_order"
        "expiry_time": "2022-10-17"
        "order": {
            "client_id": "DEMO1"
            "device": "web"
            "disclosed_quantity": 0
            "exchange": "NSE"
            "instrument_token": "11536"
            "market_protection_percentage": 0
            "order_side": "BUY"
            "order_type": "LIMIT"
            "price": 3611.45
            "product": "CNC"
            "quantity": 1
            "sl_order_price": 0
            "sl_order_quantity": 0
            "sl_trigger_price": 0
            "trigger_price": 3611.45
            "user_order_id": 10002
        }
    }
'
```

### Response

```js
    {
        "data": {
            "id": "673a20c8-80d5-4a0c-8a34-23f20fe79661"
        },
        "message": "gtt created successfully",
        "status": "success"
    }
```

### Error response

```js
    {
        "data": {},
        "error_code": 44000,
        "message": "`order` `product` is invalid",
        "status": "error"
    }
```

---

## Modify GTT Orders

> Source: https://developer.hdfcsky.com/sky-docs/docs/gttorders/modifygttorder

This API is used to modify the existing gtt orders. We can modify the price and trigger price etc.

### HTTP Request

```js
    Method: PUT
    Endpoint: oapi/v1/event/gtt
```

### Header

```json
    {
        "Authorization": "<access_token>"
    }
```

### Request Curl

```js
curl --location --request PUT 'https://uat-developer.hdfcsky.com/oapi/v1/event/gtt?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

### Response

```json
    {
        "data": {
            "id": "673a20c8-80d5-4a0c-8a34-23f20fe79661"
        },
        "message": "gtt request modified successfully",
        "status": "success"
    }
```

### Error Response

```json
    {
        "data": {},
        "error_code": 45000,
        "message": "Error from backend: (1600)-cannot modify, no data found with this id",
        "status": "error"
    }
```

---

## Cancel GTT order

> Source: https://developer.hdfcsky.com/sky-docs/docs/gttorders/cancelgttorder

This API is used to delete the existing gtt order. The gtt order list should not be empty.

### HTTP request

```js
     Method : DELETE
     End : oapi/v1/event/gtt/<client_id>/<id>
```

### Headers

```js
     {
      "Authorization": "<access_token>",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
      "Content-Type": "application/json"
    }
```

### Query params

```js
     {
         "client_id":"<client_id>"
     }
```

### Request Curl

```js
    curl --location --request DELETE 'https://uat-developer.hdfcsky.com/oapi/v1/event/gtt/<client_id>/<id>?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

### Response

```js
     {
          "data": {
               "id": "5d712b9f-53c6-4eb9-af55-733fae0a19a2"
               },
          "message": "event cancelled succesfully",
          "status": "success"
     }
```

### Error response

```js
     {
          "data": {},
          "error_code": 45000,
          "message": "Error from backend: (500)-event id not found",
          "status": "error"
     }
```

---

## Fetch GTT order

> Source: https://developer.hdfcsky.com/sky-docs/docs/gttorders/fetchgttorder

This API is used to fetch the details of the existing gtt orders. This API fetch details like actiontype, exchange,instrument token etc.

### HTTP Request

```js
    Method : GET
    Endpoint : oapi/v1/event/gtt/<client_id>
```

### Headers

```js
    {
        "Authorization": "<access_token>"
    }
```

### Query params

```js
    {
        "client_id" : "<client_id>"
    }
```

### Request Curl

```js
    curl --location 'https://uat-developer.hdfcsky.com/oapi/v1/event/gtt/<client_id>?api_key=api_key' \
--header 'Authorization: <access_token>'
```

### Response

```js
  {

      action_type: "single_order"
      client_id: "DEMO1"
      created_at: "2021-10-17 18:14:01"
      expiry_time: "2022-10-17"
      id: "673a20c8-80d5-4a0c-8a34-23f20fe79661"
      login_id: "DEMO1"
      order : {
          disclosed_qty: 0
          exchange: "BSE"
          execution_type: ""
          mode: "NEW"
          order_side: "BUY"
          order_type: "LIMIT"
          price: 3611.5
          pro_cli: "CLIENT"
          prod_type: "CNC"
          quantity: 1
          segment: "Capital"
          sl_order_price: 0
          sl_order_quantity: 0
          sl_trigger_price: 0
          square_off_price: 0
          token: 11536
          trading_symbol: "TCS-EQ"
          trailing_stop_loss: 0
          trigger_price: 3611.45
          validity: ""
          vendor_code: "00"
          reject_code: 0
          reject_reason: ""
          status: "Active"
          type: "GTTStock"
          updated_at: "2021-10-17 18:18:12"
          message: ""
          status: "success"
      }

  }
```

### Error Response

```json
{
   "data": {},
   "error_code": 45000,
   "message": "Error from backend: (500)-no gtt data found",
   "status": "error"
}
```
