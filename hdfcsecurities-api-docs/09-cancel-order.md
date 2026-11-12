# Cancel Order

> Source: https://developer.hdfcsec.com/ir-docs/docs/cancel_order

## Description

This API grants users the ability to cancel orders, restricting cancellation solely to pending orders.

## EndPoint

```js
Method: DELETE
`https://developer.hdfcsec.com/oapi/v1/orders/regular/:order_id?api_key=<api_key>`
```

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Query Params

- `api_key`: The API key used for authentication.

## Request Curl

```js
   curl --location --request DELETE 'https://developer.hdfcsec.com/oapi/v1/orders/regular/22050200000634?api_key=api_key' \
--header 'Authorization: access_token' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
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
