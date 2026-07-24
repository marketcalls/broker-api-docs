# Brokerage

> Source: https://developer.hdfcsky.com/sky-docs/docs/brokerage/calculateBrokerage

This API used to calculate brokerage details for a given stock order details.

## HTTP Request

```js
     Method: GET
     Endpoint: /oapi/v1/brokerage/calculate
```

## Headers

```json
{
    "Authorization": "<access_token>",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

## Query Params

| FieldName | Datatype | Description |
|---|---|---|
| client-id | String | Represents the unique id of user or username. |
| exchange | String | NSE,BSE,CDS,NFO,MCX |
| product | String | CNC, MIS, NRML |
| trading_symbol | String | Represents the name of the instrument. |
| price | String | order price |
| buy-sell | String | B for buy and S for sell |

## Request Curl

```js
    curl
    --location 'https://developer.hdfcsky.com/oapi/v1/brokerage/calculate?client-id=HDFCSKY1&exchange=BSE&product=MIS&trading-symbol=SPICEJET-B&buy-sell=B&quantity=1&price=41.6'
    --header 'Authorization: <access_token>' \
    --header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

## Response

```json
    {
        "success": true,
        "message": "Data Fetched from Map Succesfully.",
        "data": {
            "brokerage": "0.0416",
            "stt": "0.0000",
            "gst": "0.0078",
            "stamp_charges": "0.0012",
            "transaction_charges": "0.0016",
            "sebi_chrges_per_crore": "0.0000",
            "total_charges": "0.0522"
        }
    }
```
