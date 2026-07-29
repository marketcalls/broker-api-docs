# Market Data - LTP Data

> Source: https://developer.hdfcsky.com/sky-docs/docs/fetchltp

This API used to Fetch LTP details for a given stock.

## HTTP Request

```js
     Method: PUT
     Endpoint: /oapi/v1/fetch-ltp
```

## Headers

```json
{
    "Authorization": "<access_token>",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

## Request Curl

```js
    curl
    --location --request PUT 'https://uat-developer.hdfcsky.com/oapi/v1/fetch-ltp?api_key=<api_key>'
    --header 'Authorization: <access_token>' \
    --header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
    --header 'Content-Type: application/json'
    --data '{
            "data": [

                        {
                            "exchange": "BSE",
                            "token": "542809"
                        }
                    ]
            }'
```

## Response

```json
    {
    "data": [
            {
                "prev_close": 0.28,
                "ltp": 0.29,
                "exchange": "BSE",
                "token": 542809
            }
        ],
        "meta": {
            "statusCode": "OK",
            "statusMsg": "OK"
        }
    }
```
