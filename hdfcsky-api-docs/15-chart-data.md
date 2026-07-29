# Chart Data (Historical Candles)

> Source: https://developer.hdfcsky.com/sky-docs/docs/fetchCandles

This API is used to fetch candles through chart data.

## HTTP Request

```js
     Method: GET
     Endpoint: /oapi/charts-api/charts/v1/fetch-candle
```

## Headers

```json
{
    "Authorization": "<access_token>",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
```

## Query Params

```js
{
    "api_key": "The API key used for authentication",
    "symbol": "Symbol for particular Stock",
    "exchange": "Exchange",
    "chartType":"MINUTES/DAY",
    "seriesType" : "type of derivative",
    "start": "Start Date of data",
    "end":"End Date of data"
}
```

## Request Curl

```js
    curl --location --request GET 'https://uat-developer.hdfcsky.com/oapi/charts-api/charts/v1/fetch-candle?api_key=api_key&symbol=RELIANCE&exchange=NSE&chartType=MINUTE&seriesType=EQ&start=2025-04-10&end=2025-04-15' \
--header 'Authorization: <access_token>' \
--data ''
```

## Response

```json
   {
    "data": {
        "results": [
            [
                4066.0,
                4089.8,
                4006.3501,
                4015.5,
                1928049.0,
                0,
                "22-10-2024"
            ],
            [
                4050.0,
                4163.1499,
                4044.2,
                4156.6001,
                2409223.0,
                0,
                "22-01-2025"
            ],
            [
                4287.5,
                4339.1001,
                4268.1001,
                4306.25,
                1809793.0,
                0,
                "24-07-2024"
            ],
            [
                4113.0,
                4135.8999,
                4056.0,
                4073.1499,
                437172.0,
                0,
                "01-02-2025"
            ]
            ]
            },
        "meta": {
        "displayMessage": "Success",
        "err_code": "Success"
    }
    }
```
