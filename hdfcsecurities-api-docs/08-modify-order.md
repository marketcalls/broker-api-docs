# Modify Order

> Source: https://developer.hdfcsec.com/ir-docs/docs/modify_order

## Description

When an order is in a pending state within the system, the modify functionality enables users to adjust certain parameters of the order, such as price, quantity, and validity.

## EndPoint

```js
Method: PUT
`https://developer.hdfcsec.com/oapi/v1/orders/regular/:order_id?api_key=<api_key>`
```

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Query Params

- `api_key`: The API key used for authentication.

## Glossary of constants

| Parameter | Description |
| --- | --- |
| **product** | The updated trading product type (e.g., INTRADAY). |
| **quantity** | The updated quantity of the security to be traded. |
| **order_type** | The updated type of order (e.g. MARKET). **(Required)** |
| **price** | The updated price at which the order is placed (for LIMIT orders). |
| **trigger_price** | The updated trigger price (for stop-loss orders). |
| **disclosed_quantity** | The updated disclosed quantity for the order. |
| **validity** | The updated validity of the order (e.g. DAY). |
| **amo** | The updated AMO of the order (true,false) |

## Request Curl

```js

curl --location --request PUT '
https://developer.hdfcsec.com/oapi/v1/orders/regular/24042500000504?api_key=api_key'
\
--header 'Authorization: access_token' \
--header 'Content-Type: application/json' \
--header  'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '{
"quantity":3 ,
"order_type":"MARKET" ,
"validity":"DAY" ,
"disclosed_quantity": 0,
"product":"DELIVERY" ,
"price":0,
"trigger_price" : 0,
"amo":false
}'
```

## API Response

```js
{
    "status": "success",
    "data": {
      "order_id": "22050200000634"
    }
}
```
