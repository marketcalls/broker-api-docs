# Fetch LTP

> Source: https://developer.hdfcsec.com/ir-docs/docs/fetchltp

## Description

This API used to Fetch LTP details for a given stock.

## EndPoint

```js
Method: PUT
`https://developer.hdfcsec.com/oapi/v1/fetch-ltp?api_key=<api_key>`
```

> **Note:** this is a `PUT`, not a `GET` or `POST`, despite being a read-only snapshot call.

## Headers

- **Authorization**: access_token
- **User-Agent**: User-Agent header is required indicating the client application making the request.

## Query Params

- `api_key`: The API key used for authentication.

## Request Curl

```js
    curl
    --location --request PUT 'https://developer.hdfcsec.com/oapi/v1/fetch-ltp?api_key=<api_key>'
    --header 'Authorization: <access_token>' \
    --header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
    --header 'Content-Type: application/json' 
    --data '{
            "data": [
                        {
                            "exchange": "NSE",
                            "token": "21840"
                        },
                        {
                            "exchange": "BSE",
                            "token": "542809"
                        }
                    ]
            }'
```

## API Response

```js
    {
    "data": [
            {
                "prev_close": 1106.5,
                "ltp": 1089.75,
                "exchange": "NSE",
                "token": 21840
            },
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

## Notes

- The request body is a `data` array of `{exchange, token}` pairs, so multiple instruments can be
  fetched in one call.
- `token` is sent as a string and returned as a number.
- `token` here is the **`exch_security_id`** column of the Security Master CSV (the numeric
  exchange token), not the alphanumeric `security_id` used by
  [Place Order](07-place-order.md). See [Security Master](19-security-master.md).
- This response uses the `data` + `meta` envelope rather than the `status` + `data` envelope used
  by the order and portfolio endpoints.
- Only `ltp` and `prev_close` are returned — for OHLC, volume, market depth, OI and Greeks use the
  [WebSocket feed](17-websocket.md).
