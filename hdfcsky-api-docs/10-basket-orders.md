# Basket Orders

Create and manage baskets of instruments, then execute them as a group.

## Contents

- [Create Basket](#create-basket)
- [Fetch Basket](#fetch-basket)
- [Rename Basket](#rename-basket)
- [HTTP request](#http-request)
- [Edit Basket Details](#edit-basket-details)
- [Delete Basket](#delete-basket)
- [Add basket Instrument](#add-basket-instrument)
- [Edit Basket Instrument](#edit-basket-instrument)
- [Delete Basket Instrument](#delete-basket-instrument)
- [Execute Basket Order](#execute-basket-order)
- [Body Params](#body-params)

---

## Create Basket

> Source: https://developer.hdfcsky.com/sky-docs/docs/basketorders/createbasket

This API used to create basket order. It can create two types of Basket i.e. Normal or Hedge. The Hedge Basket can have order type as LIMIT, MARKET, SL or SLM.  And the product type can be CNC, MIS or NRML.

### HTTP Request

```js
     Method: POST
     Endpoint: /oapi/v1/basket
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
| login_id | String | Represents the unique id of user or username. |
| name | String | Represents the name of the basket. |
| type | String | NORMAL, HEDGE |
| product_type | String | CNC, MIS, NRML |
| order_type | String | LIMIT, MARKET, SL, SLM |

### Request Curl

```js
curl --location 'https://uat-developer.hdfcsky.com/oapi/v1/basket/order?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json' \
--data ' {
      "login_id": "DEMO1",
      "name": "b1",
      "type": "NORMAL",
      "product_type": "ALL",
      "order_type": "ALL"
    }
     '
```

### Response

```js
    {
    "data":
        {
         "login_id": "DEMO1",
         "name": "b1",
         "type": "NORMAL",
         "product_type": "ALL",
         "order_type": "ALL"
         }
        "message": "Order place successfully",
        "status": "success"
      }
```

### Error Response

```js
    {
      data: {}
      error_code: 48001
      message: "name has already been taken"
      status: "error"
    }
```

---

## Fetch Basket

> Source: https://developer.hdfcsky.com/sky-docs/docs/basketorders/fetchbasket

This API used to fetch details of the basket order like basketid, baskettype, name, loginid etc. It displays total number of baskets created along with the added instrument details.

### HTTP Request

```js
    Method : GET
    Endpoint : oapi/v1/basket/{login_id}
```

### Headers

```json
    {
      "Authorization": "<access_token>",
    }
```

### Query Params

```json
    {
        "login_id" : "<login_id>"
    }
```

### Request Curl

```js
curl 'https://uat-developer.hdfcsky.com/oapi/v1/basket/<login_id>?api_key=api_key' \
--header 'Authorization: <access_token>'
```

### Response

```json
      {

         "data":[
            {
               "basket_id":"53575501-5aeb-4b6d-b660-7aeda251b75f",
               "basket_type":"NORMAL",
               "login_id":"DEMO1",
               "name":"jj",
               "order_type":"ALL",
               "orders":[
                  {
            "order_id":"2334596c-881c-4a87-be6c-a01f444927e9",
            "order_info":{
               "trigger_price":0,
               "underlying_token":"3045",
               "series":"",
               "user_order_id":10002,
               "exchange":"NSE",
               "square_off":false,
               "mode":"NEW",
               "remaining_quantity":0,
               "average_trade_price":0,
               "trade_price":0,
               "order_tag":"",
               "order_status_info":"",
               "order_side":"BUY",
               "square_off_value":0.0,
               "contract_description":{},
               "segment":"",
               "client_id":"DEMO1",
               "trading_symbol":"SBIN-EQ",
               "rejection_code":0,
               "lot_size":0,
               "quantity":1,
               "last_activity_reference":0,
               "nnf_id":0,
               "pro_cli":"CLIENT",
               "price":506.5,
               "order_type":"LIMIT",
               "validity":"DAY",
               "target_price_type":"absolute",
               "instrument_token":3045,
               "sl_trigger_price":0.0,
               "is_trailing":false,
               "sl_order_quantity":0,
               "order_entry_time":0,
               "exchange_time":0,
               "leg_order_indicator":null,
               "trailing_stop_loss":0.0,
               "login_id":null,
               "oms_order_id":"",
               "market_protection_percentage":0,
               "execution_type":"BO",
               "disclosed_quantity":0,
               "rejection_reason":"",
               "stop_loss_value":0.0,
               "device":null,
               "product":"MIS",
               "sl_order_price":0.0,
               "filled_quantity":0,
               "exchange_order_id":"",
               "deposit":0,
               "average_price":0,
               "spread_token":null,
               "order_status":null
            }
         }
      ],
      "product_type":"ALL"
   },
   {
      "basket_id":"2928fcf5-4633-468b-82bf-c393920e8bec",
      "basket_type":"HEDGE",
      "login_id":"DEMO1",
      "name":"hedge",
      "order_type":"MARKET",
      "orders":[
         {
            "order_id":"bef5f4d8-422d-4092-b321-c30af342543c",
            "order_info":{
               "trigger_price":0,
               "underlying_token":"26000",
               "series":"",
               "user_order_id":10002,
               "exchange":"NFO",
               "square_off":false,
               "mode":"NEW",
               "remaining_quantity":0,
               "average_trade_price":0,
               "trade_price":0,
               "order_tag":"",
               "order_status_info":"",
               "order_side":"BUY",
               "square_off_value":null,
               "contract_description":{

               },
               "segment":"",
               "client_id":"DEMO1",
               "trading_symbol":"NIFTY21DECFUT",
               "rejection_code":0,
               "lot_size":0,
               "quantity":50,
               "last_activity_reference":0,
               "nnf_id":0,
               "pro_cli":"CLIENT",
               "price":0,
               "order_type":"MARKET",
               "validity":"DAY",
               "target_price_type":"absolute",
               "instrument_token":71321,
               "sl_trigger_price":0.0,
               "is_trailing":false,
               "sl_order_quantity":0,
               "order_entry_time":0,
               "exchange_time":0,
               "leg_order_indicator":null,
               "trailing_stop_loss":null,
               "login_id":null,
               "oms_order_id":"",
               "market_protection_percentage":0,
               "execution_type":"REGULAR",
               "disclosed_quantity":0,
               "rejection_reason":"",
               "stop_loss_value":null,
               "device":null,
               "product":"MIS",
               "sl_order_price":0.0,
               "filled_quantity":0,
               "exchange_order_id":"",
               "deposit":0,
               "average_price":0,
               "spread_token":null,
               "order_status":null
            }
         }
      ],
      "product_type":"MIS"
   }
      ],
      "message":"",
      "status":"success"
   }
```

### Error Response

```json
{
   "data": {},
   "error_code": 48001,
   "message": "`order_info` Hedge basket feature enabled only for NIFTY 50 & NIFTY BANK as underlying",
   "status": "error"
}
```

---

## Rename Basket

> Source: https://developer.hdfcsky.com/sky-docs/docs/basketorders/renamebasket

This API used to rename the existing basket.

## HTTP request

```js
    Method : PUT
    Endpoint : oapi/v1/basket
```

### Headers

```js
     {
      "Authorization": "<access_token>",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
      "Content-Type": "application/json"
    }
```

### BodyParams

| FieldName | Datatype | Description |
|---|---|---|
| basket_id | String | Represents the unique id of basket. |
| name | String | Represents the name of the basket. |

### Sample Request

```js
curl --location --request PUT 'https://uat-developer.hdfcsky.com/oapi/v1/basket?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '{
        "basket_id": "0786e757-2e8f-44b2-9559-deeac2e00214",
        "name": "TEST_NAME"
    }'

```

### Response

```js
    {
        basket_id: "0786e757-2e8f-44b2-9559-deeac2e00214"
        basket_type: "NORMAL"
        login_id: "NA003"
        name: "TEST_NAME"
        order_type: "ALL"
        orders: []
        product_type: "ALL"
        message: "Basket name updated successfully"
        status: "success"
    }
```

### Error Response

```json
{
 "data": {},
 "error_code": 48001,
 "message": "`name` Basket name restricted to 20 characters",
 "status": "error"
}
```

---

## Edit Basket Details

> Source: https://developer.hdfcsky.com/sky-docs/docs/basketorders/editbasketorder

This API used to edit the basket. We can edit the name of the basket and we can add or remove the instruments present in the basket.

### HTTP Request

```js
    Method : PUT
    Endpoint: oapi/v1/basket/order
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
| basket_id | String | Represents the unique id of basket. |
| name | String | Represents the name of the basket. |
| exchange | String | NSE,BSE,CDS,NFO,MCX |
| instrument_token | String | Represents unique id of particular instrument. |
| client_id | String | Represents the unique id of user or username. |
| order_type | String | LIMIT, MARKET, SL, SLM |
| price | String | It can't be Zero. |
| quantity | Number | It can't be Zero. |
| disclose_quantity | Number | It can't be negative number. |
| validity | String | Day or IOC |
| trading_symbol | String | Represents the name of the instrument. |
| order_side | String | BUY or SELL |
| user_order_id | Number | Unique id |
| underlying_token | Number | It is the token of base equity Instrument. |
| series | String | Represents the particular series based on exchange. |
| device | String | web,mobile |
| trigger_price | Number | It can't be zero. |
| product_type | String | CNC, MIS, NRML |
| execution_type | String | REGULAR,BO,CO,AMO |

### Request Curl

```js
curl --location --request PUT 'https://uat-developer.hdfcsky.com/oapi/v1/basket/order?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '{
        "basket_id": "b993d276-4fe9-4050-ab80-6ab1f5f9863f",
        "name": "test",
        "order_info":
    {
        "exchange": "BSE",
        "instrument_token": "3045",
        "client_id": "NA003",
        "order_type": "MARKET",
        "price": 0,
        "quantity": 1,
        "disclosed_quantity": 0,
        "validity": "DAY",
        "product": "MIS",
        "trading_symbol": "SBIN-EQ",
        "order_side": "BUY",
        "user_order_id": 10002,
        "underlying_token": "3045",
        "series": "EQ",
        "device": "WEB",
        "trigger_price": 0,
        "execution_type": "REGULAR"
    }
    }'

```

### Response

```json
     {

      basket_id: "b993d276-4fe9-4050-ab80-6ab1f5f9863f"
     {
        basket_type: "NORMAL"
        login_id: "NA003"
        name: "test"
        order_type: "ALL"
        orders: [{order_id: "a38f3470-2a26-4f88-839c-7d4e1987c97a",…}]
        0: {order_id: "a38f3470-2a26-4f88-839c-7d4e1987c97a",…}
        order_id: "a38f3470-2a26-4f88-839c-7d4e1987c97a"
        order_info: {instrument_token: 3045, validity: "DAY", pro_cli: "CLIENT", exchange: "BSE", product: "MIS",…}
        average_price: 0
        average_trade_price: 0
        client_id: "NA003"
        contract_description: {}
        deposit: 0
        device: null
        disclosed_quantity: 0
        exchange: "BSE"
        exchange_order_id: ""
        exchange_time: 0
        execution_type: "REGULAR"
        filled_quantity: 0
        instrument_token: 3045
        is_trailing: false
        last_activity_reference: 0
        leg_order_indicator: null
        login_id: null
        lot_size: 0
        market_protection_percentage: 0
        mode: "NEW"
        nnf_id: 0
        oms_order_id: ""
        order_entry_time: 0
        order_side: "BUY"
        order_status: null
        order_status_info: ""
        order_tag: ""
        order_type: "MARKET"
        price: 0
        pro_cli: "CLIENT"
        product: "MIS"
        quantity: 1
        rejection_code: 0
        rejection_reason: ""
        remaining_quantity: 0
        segment: ""
        series: ""
        spread_token: null
        square_off: false
        square_off_value: null
        stop_loss_value: null
        target_price_type: "absolute"
        trade_price: 0
        trading_symbol: "SBIN-EQ"
        trailing_stop_loss: null
        trigger_price: 0
        underlying_token: "3045"
        user_order_id: 10002
        validity: "DAY"
        product_type: "ALL"
        message: "Order added in the basket test."
        status: "success"

        }

      }
```

### Error Response

```json
{
 "data": {},
 "error_code": 46001,
 "message": "Instrumetn already added",
 "status": "error"
}
```

---

## Delete Basket

> Source: https://developer.hdfcsky.com/sky-docs/docs/basketorders/deletebasket

This API used to delete the existing Baskets. It uses basketID to delete the basket

### HTTP Request

```js
     Method: DELETE
     Endpoint: /oapi/v1/basket
```

### Headers

```js
    {
      "Authorization": "<access_token>",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
      "Content-Type": "application/json"
    }
```

### Request Curl

```js
    curl --location --request DELETE 'https://uat-developer.hdfcsky.com/oapi/v1/basket?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '{
  "basket_id":"0062e94b-c3ef-4203-86f5-819c4002b5d6",
  "name":"RICH",
  "sip_count":0
}'
```

### Response

```js
    {
  "data": [
    {
      "basket_id": "44a9e300-8565-4319-8f78-391440a774ec",
      "basket_type": "NORMAL",
      "created_at": 1726723471,
      "is_executed": false,
      "login_id": "S245103",
      "name": "TEST2",
      "order_type": "ALL",
      "orders": [],
      "product_type": "ALL",
      "sip_eligible": true,
      "sip_enabled": false
    }
  ],
  "message": "Kart TEST1 deleted",
  "status": "success"
}
```

### Error Response

```js
    {
      "data": {},
      "error_code": 48001,
      "message": "Basket doesnt exists",
      "status": "error"
    }
```

---

## Add basket Instrument

> Source: https://developer.hdfcsky.com/sky-docs/docs/basketorders/addbasketinstrument

This API used to add Instrument in the created baskets. We can add only limited number of instruments in the basket and repeated instrument can't be added.

### HTTP Request

```js
     Method: POST
     Endpoint: /oapi/v1/basket/order
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
| basket_id | String | Represents the unique id of basket. |
| name | String | Represents the name of the basket. |
| exchange | String | NSE,BSE,CDS,NFO,MCX |
| instrument_token | String | Represents unique id of particular instrument. |
| client_id | String | Represents the unique id of user or username. |
| order_type | String | LIMIT, MARKET, SL, SLM |
| price | String | It can't be Zero. |
| product | String | CNC, MIS, NRML |
| client_id | String | Represents the unique id of user or username. |
| device | String | web,mobile |
| disclose_quantity | Number | It can't be negative number. |
| execution_type | String | REGULAR,BO,CO,AMO |
| order_side | String | BUY or SELL |
| order_type | String | LIMIT,MARKET,SL,SLM |
| quantity | Number | It can't be Zero. |
| series | String | Represents the particular series based on exchange. |
| trading_symbol | String | Represents the name of the instrument. |
| trigger_price | Number | It can't be zero. |
| underlying_token | Number | It is token of base equity instrument |
| user_order_id | Number | unique id of order placed. |
| validity | String | Day or IOC |

### Request Curl

```js
curl --location 'https://uat-developer.hdfcsky.com/oapi/v1/basket/order?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json' \
--data ' {
            "basket_id": "0786e757-2e8f-44b2-9559-deeac1e30114",
            "name": "TEST",
            "order_info": {
              "exchange": "BSE",
              "instrument_token": "3045",
              "client_id": "TEST1",
              "order_type": "MARKET",
              "price": 0,
              },
            "client_id": "TEST1",
            "device": "WEB",
            "disclosed_quantity": 0,
            "exchange": "NSE",
            "execution_type": "REGULAR",
            "instrument_token": "3045",
            "order_side": "BUY",
            "order_type": "MARKET",
            "price": 0,
            "product": "MIS",
            "quantity": 1,
            "series": "EQ",
            "trading_symbol": "SBIN-EQ",
            "trigger_price": 0,
            "underlying_token": "3045",
            "user_order_id": 10002,
            "validity": "DAY",
         }
     '
```

### Response

```json
      {
      "data":{
          "basket_id":"72fa28f8-7c08-4a4d-ba7a-fedd462744a1",
          "basket_type":"NORMAL",
          "login_id":"DEMO1",
          "name":"h",
          "order_type":"ALL",
      "orders":[
         {
            "order_id":"a5d13c1f-f99c-4230-ad19-9ed82826ee74",
            "order_info":{
               "sl_trigger_price":0.0,
               "spread_token":null,
               "exchange_time":0,
               "last_activity_reference":0,
               "exchange":"NSE",
               "target_price_type":"absolute",
               "leg_order_indicator":null,
               "mode":"NEW",
               "average_price":0,
               "trigger_price":0,
               "sl_order_quantity":0,
               "deposit":0,
               "order_type":"LIMIT",
               "is_trailing":false,
               "product":"MIS",
               "trailing_stop_loss":0.0,
               "underlying_token":"3045",
               "user_order_id":10002,
               "rejection_code":0,
               "order_tag":"",
               "filled_quantity":0,
               "quantity":1,
               "trade_price":0,
               "client_id":"DEMO1",
               "average_trade_price":0,
               "trading_symbol":"SBIN-EQ",
               "series":"",
               "lot_size":0,
               "disclosed_quantity":0,
               "instrument_token":3045,
               "pro_cli":"CLIENT",
               "contract_description":{

               },
               "validity":"DAY",
               "remaining_quantity":0,
               "rejection_reason":"",
               "segment":"",
               "price":506.5,
               "market_protection_percentage":0,
               "stop_loss_value":0.0,
               "nnf_id":0,
               "order_status_info":"",
               "login_id":null,
               "sl_order_price":0.0,
               "execution_type":"BO",
               "square_off_value":0.0,
               "order_side":"BUY",
               "order_entry_time":0,
               "exchange_order_id":"",
               "device":null,
               "oms_order_id":"",
               "order_status":null,
               "square_off":false
            }
         }
      ],
      "product_type":"ALL"
     },
      "message":"Order added in the basket h.",
      "status":"success"
     }
```

### Error Response

```json
 {
    "data": {},
    "error_code": 46001,
    "message": "Instrumetn already added",
    "status": "error"
 }
```

---

## Edit Basket Instrument

> Source: https://developer.hdfcsky.com/sky-docs/docs/basketorders/editbasketinstrument

This API used to edit the basket instrument present in the basket. In this we are able to edit the basket instrument details like quantity.

### HTTP Request

```js
    Method : PUT
    Endpoint: oapi/v1/basket/order
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
| basket_id | String | Represents the unique id of basket. |
| name | String | Represents the name of the basket. |
| exchange | String | NSE,BSE,CDS,NFO,MCX |
| instrument_token | String | Represents unique id of particular instrument. |
| client_id | String | Represents the unique id of user or username. |
| order_type | String | LIMIT, MARKET, SL, SLM |
| price | String | It can't be Zero. |
| quantity | Number | It can't be Zero. |
| disclose_quantity | Number | It can't be negative number. |
| validity | String | Day or IOC |
| product | String | CNC,MIS,NRML |
| trading_symbol | String | Represents the name of the instrument. |
| order_side | String | BUY or SELL |
| user_order_id | Number | Unique id |
| underlying_token | Number | It is the token of base equity Instrument. |
| series | String | Represents the particular series based on exchange. |
| oms_order_id | String | Represents the unique id given by oms. |
| exchange_order_id | String | Represents the unique id given by exchange. |
| trigger_price | Number | It can't be zero. |
| stop_loss_value | Number | It can't be Zero. |
| square_off_value | Number | It can't be Zero. |
| trailing_stop_loss | Number | It can't be Zero. |
| is_trailing | Boolean | True or False. |
| execution_type | String | REGULAR,BO,CO,AMO |
| order_id | String | Represents unique id of order. |

### Request Curl

```js
curl --location --request PUT 'https://uat-developer.hdfcsky.com/oapi/v1/basket/order?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '{
        "basket_id":"72fa28f8-7c08-4a4d-ba7a-fedd461244a1",
        "name":"test",
        "order_info":{
          "exchange":"BSE",
          "instrument_token":3045,
          "client_id":"DEMO1",
          "order_type":"LIMIT",
          "price":506.5,
          "quantity":1,
          "disclosed_quantity":0,
          "validity":"DAY",
          "product":"MIS",
          "trading_symbol":"SBIN-EQ",
          "order_side":"BUY",
          "user_order_id":10002,
          "underlying_token":"3045",
          "series":"EQ",
          "oms_order_id":"a5d13c1f-f99c-4230-ad19-9ed8e826ee74",
          "exchange_order_id":"",
          "trigger_price":0,
          "stop_loss_value":0,
          "square_off_value":0,
          "trailing_stop_loss":0,
          "is_trailing":false,
          "execution_type":"BO"
          },
      "order_id":"a5d13c1f-f99c-4230-ad19-9ed8e826ee74"
    }'

```

### Response

```json
     {

        "data": {
            "basket_id": "b993d276-4fe9-4050-ab80-6ab1f5f9863f",
            "basket_type": "NORMAL",
            "login_id": "NA003",
            "name": "test",
            "order_type": "ALL",
    "orders": [
      {
        "order_id": "a38f3470-2a26-4f88-839c-7d4e1987c97a",
        "order_info": {

          "instrument_token": 3045,
          "validity": "DAY",
          "pro_cli": "CLIENT",
          "exchange": "BSE",
          "product": "MIS",
          "trigger_price": 0,
          "client_id": "NA003",
          "mode": "NEW",
          "contract_description": {},
          "last_activity_reference": 0,
          "rejection_reason": "",
          "oms_order_id": "",
          "trading_symbol": "SBIN-EQ",
          "order_entry_time": 0,
          "trade_price": 0,
          "rejection_code": 0,
          "nnf_id": 0,
          "execution_type": "REGULAR",
          "quantity": 1,
          "price": 0,
          "series": "",
          "user_order_id": 10002,
          "filled_quantity": 0,
          "exchange_order_id": "",
          "order_status_info": "",
          "trailing_stop_loss": null,
          "disclosed_quantity": 0,
          "login_id": null,
          "target_price_type": "absolute",
          "lot_size": 0,
          "order_type": "MARKET",
          "square_off": false,
          "exchange_time": 0,
          "is_trailing": false,
          "spread_token": null,
          "average_price": 0,
          "order_tag": "",
          "market_protection_percentage": 0,
          "average_trade_price": 0,
          "order_side": "BUY",
          "order_status": null,
          "device": null,
          "deposit": 0,
          "leg_order_indicator": null,
          "stop_loss_value": null,
          "underlying_token": "3045",
          "square_off_value": null,
          "remaining_quantity": 0,
          "segment": ""
        }
      },
    ],
    "product_type": "ALL"
     },
      "message": "Order updated successfully.",
      "status": "success"
    }
```

### Error Response

```json
{
 "data": {},
 "error_code": 48004,
 "message": "`order_info` order price cannot be zero in SL/LIMIT order",
 "status": "error"
}
```

---

## Delete Basket Instrument

> Source: https://developer.hdfcsky.com/sky-docs/docs/basketorders/deletebasketinstrument

This API used to delete basket Instrument inside the basket. This requires basketId to delete the basket instrument in the basket.

### HTTP Request

```js
     Method: DELETE
     Endpoint: oapi/v1/basket/order
```

### Headers

```js
    {
      "Authorization": "<access_token>",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
      "Content-Type": "application/json"
    }
```

### Request curl

```js
curl --location --request DELETE 'https://uat-developer.hdfcsky.com/oapi/v1/basket/order?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '     {
      "basket_id": "0786e757-2e8f-44b2-9559-deeac2e00114",
      "name": "test",
      "order_id": "a6ed501a-55b4-402d-b152-5207f7b7ae8f"
    }'

```

### Error Response

```js
  {
   "data": {},
   "error_code": 48001,
   "message": "Basket doesnt exists",
   "status": "error"
 }
```

---

## Execute Basket Order

> Source: https://developer.hdfcsky.com/sky-docs/docs/basketorders/executebasket

This API used to execute the orders of the instruments present in the basket.

### HTTP Request

```js
    Method : POST
    Endpoint: oapi/v1/orders/kart
```

### Headers

```js
     {
      "Authorization": "<access_token>",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
      "Content-Type": "application/json"
    }
```

## Body Params

| FieldName | Datatype | Description |
|---|---|---|
| basket_id | String | Represents the unique id of basket. |
| execution_type | String | REGULAR ,LIMIT ,MARKET |
| name | String | Represents the name of the basket. |
| square_off | Boolean | TRUE or FALSE |

### Request Curl

```js
curl --location --request POST 'https://uat-developer.hdfcsky.com/oapi/v1/orders/kart?api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '
  {
        "basket_id": "b993d276-4fe9-4050-ab80-6ab1f5f9863f"
        "execution_type": "NML"
        "name": "test"
        "square_off": false
  }
'
```

### Response

```js
    {

      "data": {
        "data": {
        "basket_id": "20211017-4",
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
       "data":{},
       "error_code":49002,
       "message":"instrument `SBIN-EQ` is disabled for hedging",
       "status":"error"
  }
```
