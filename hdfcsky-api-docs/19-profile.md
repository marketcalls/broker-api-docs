# Profile

> Source: https://developer.hdfcsky.com/sky-docs/docs/profile

This API is used to fetch user profile. The query param is client id. In response it provides user data like user's name, id, Bank Account number, etc. In case of error, It shows 'Request forbidden'.

## HTTP Request

```js
     Method: GET
     Endpoint: /oapi/v1/user/trading_info
```

## Headers

```js
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

## Query Params

```js
{
    "client_id": "DEMO1",
    "api_key": "The API key used for authentication"
}
```

## Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/user/trading_info?client_id=DEMO1&api_key=api_key' \
--header 'Authorization: <access_token>' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
```

## Response

```js
{
   "data": {
            "client_id": "TEST1",
            "ddpi": false,
            "exchanges_subscribed": [
                "NFO",
                "NSE",
                "BSE",
                "CDS"
            ],
            "name": "DEMO",
            "poa_enabled": true,
            "products_enabled": [
                "NRML",
                "CNC",
                "MIS"
            ],
            "status": "active"
        },
        "message": "",
        "status": "success"
}
```

## Error Response

```js
    {
      "status": "error",
      "message": "Request forbidden",
      "error_code": 40000,
      "data":{
      }
    }
```
