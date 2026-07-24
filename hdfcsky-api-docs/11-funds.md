# Funds

## Contents

- [Fetch Funds V1](#fetch-funds-v1)
- [Fetch Funds V2](#fetch-funds-v2)

---

## Fetch Funds V1

> Source: https://developer.hdfcsky.com/sky-docs/docs/funds

This API is used to fetch Funds. The query params are client id and type is all. In response the V1 fund's data like id, title, message etc. is provided. In case of error, It shows `Request Unauthorised`.

### HTTP Request

```js
    Method: GET
    Endpoint: /oapi/v1/funds/view
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
    "type": "all",
    "api_key": "The API key used for authentication"
}
```

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/funds/view?api_key=api_key&client_id=demo1@gmail.com&type=all' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

### Response

```js
{
    "data": [
    {
    "id": "all",
    "title": "ALL"
    }],
    "message": "",
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

## Fetch Funds V2

> Source: https://developer.hdfcsky.com/sky-docs/docs/funds/fetchfundsv2

This API is used to fetch Funds. The query params are client id and type is all. In response the V2 fund's data like clien† id, headers, description etc. is provided. In case of error, It shows `Request Unauthorised`.

### HTTP Request

```js
    Method: GET
    Endpoint: /oapi/v2/funds/view
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
   "type": "all"
}
```

### Response

```js
{
    "data":{
    "client_id": "DEMO1",
    "headers": [
    "Description",
    ""],
    "values": [
    {
    "0": "Available Margin",
    "1": "8239.85"}{
    "0": "Margin Used",
    "1": "19.34"}{
    "0": "Opening Balance",
    "1": "1781.24"}{
    "0": "Adhoc Deposit",
    "1": "6500.00"}{
    "0": "Notion",
    "1": "0.00"}{
    "0": "Pay In",
    "1": "0.00"}{
    "0": "Pay out",
    "1": "0.00"}{
    "0": "Pledge Benefit",
    "1": "0.00"}{
    "0": "Equity Credit Sell",
    "1": "0.00"}{
    "0": "Option Credit For Sell",
    "1": "0.00"}{
    "0": "Realized MTM",
    "1": "0.00"}{
    "0": "Unrealized MTM",
    "1": "-0.05"}]
    },
    "message": "",
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
