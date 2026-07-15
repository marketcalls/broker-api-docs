> Source: https://docs.arrow.trade/rest-api/symbol-quotes/

# Instrument Quotes APIs

Alongside streaming market data, Arrow exposes **quote** endpoints for on-demand snapshots over HTTP. Each call picks a **mode** in the URL (`ltp`, `ohlcv`, or `full`) so you can trade off payload size against detail. These use the same authentication model as the rest of the Developer API. For continuous ticks, use [Market data](../market-data/) instead.

Numeric price and quantity fields are returned as integers in the exchange’s native scaling (for example NSE cash prices are often quoted in **paise** as integers). `ltt` and `time` are Unix timestamps in **seconds**.

## Base URL and headers

**Base URL**

```
https://edge.arrow.trade
```

**Required headers**

Header | Description
---|---
`appID` | Your application ID
`token` | Access token from the [authentication](../authentication/) flow

Quote requests use `POST` with a JSON body. Include `Content-Type: application/json` on requests that send a body.

* * *

## Endpoint overview

Method | Endpoint | Description
---|---|---
`POST` | `/info/quote/{mode}` | Single-instrument snapshot; `mode` is `ltp`, `ohlcv`, or `full`
`POST` | `/info/quotes/{mode}` | Multiple instruments in one request (JSON array body)

Use `/info/quote/{mode}` with one object when you need a single symbol. Use `/info/quotes/{mode}` with an array for watchlists or basket pricing.

* * *

## Single instrument quote

Returns a real-time snapshot for one `symbol` on the given `exchange`. Replace `{mode}` with `ltp`, `ohlcv`, or `full`.

**Request body (JSON)**

Field | Type | Description
---|---|---
`symbol` | string | Trading symbol (for example `RELIANCE-EQ`, `NIFTY19MAY26C24900`)
`exchange` | string | Exchange segment: `NSE`, `NFO`, `BSE`, `BFO`, `MCX`, or `INDEX`

**Sample request**

```bash
curl --location 'https://edge.arrow.trade/info/quote/ltp' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
    "exchange": "NSE",
    "symbol": "RELIANCE-EQ"
}'
```

**Sample response (LTP)**

```json
{
    "data": {
        "close": 135880,
        "ltp": 137020,
        "token": 2885
    },
    "status": "success"
}
```

**Sample response (OHLCV)**

Same URL pattern with `/info/quote/ohlcv`.

```json
{
    "data": {
        "close": 135880,
        "high": 137800,
        "low": 135850,
        "ltp": 136890,
        "ltt": 1778743365,
        "oi": 0,
        "open": 136520,
        "token": 2885,
        "volume": 7229309
    },
    "status": "success"
}
```

**Sample response (FULL)**

Same URL pattern with `/info/quote/full`.

```json
{
    "data": {
        "asks": [
            {
                "orders": 4,
                "price": 136960,
                "quantity": 145
            },
            {
                "orders": 2,
                "price": 136970,
                "quantity": 148
            },
            {
                "orders": 4,
                "price": 136980,
                "quantity": 526
            },
            {
                "orders": 8,
                "price": 136990,
                "quantity": 261
            },
            {
                "orders": 12,
                "price": 137000,
                "quantity": 1060
            }
        ],
        "avgPrice": 136771,
        "bids": [
            {
                "orders": 3,
                "price": 136940,
                "quantity": 680
            },
            {
                "orders": 8,
                "price": 136930,
                "quantity": 1774
            },
            {
                "orders": 12,
                "price": 136920,
                "quantity": 1652
            },
            {
                "orders": 10,
                "price": 136910,
                "quantity": 1232
            },
            {
                "orders": 14,
                "price": 136900,
                "quantity": 3247
            }
        ],
        "close": 135880,
        "high": 137800,
        "low": 135850,
        "lowerLimit": 122300,
        "ltp": 136960,
        "ltq": 21,
        "ltt": 1778743485,
        "netChange": 79,
        "netChangeIndicator": 43,
        "oi": 0,
        "oiDayHigh": 0,
        "oiDayLow": 0,
        "open": 136520,
        "symbol": "RELIANCE-EQ",
        "time": 1778743487,
        "token": 2885,
        "totalBuyQty": 483299,
        "totalSellQty": 529911,
        "upperLimit": 149460,
        "volume": 7285498
    },
    "status": "success"
}
```

Each depth row in `bids` and `asks` includes `orders` (count of orders at that level), `price`, and `quantity`.

* * *

## Multiple instrument quotes

Returns one object per requested leg inside `data` as a **JSON array**. The request body is a **JSON array** of `{ "symbol", "exchange" }` objects.

**Request body (JSON)**

Each element of the array:

Field | Type | Description
---|---|---
`symbol` | string | Trading symbol
`exchange` | string | Exchange segment (`NSE`, `NFO`, `BSE`, `BFO`, `MCX`, `INDEX`)

**Sample request**

```bash
curl --location 'https://edge.arrow.trade/info/quotes/ltp' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>' \
--header 'Content-Type: application/json' \
--data '[
    {"exchange": "NSE", "symbol": "RELIANCE-EQ"},
    {"exchange": "NSE", "symbol": "INFY-EQ"},
    {"exchange": "NFO", "symbol": "NIFTY19MAY26C24900"}
]'
```

**Sample response (LTP)**

Each array element uses the same shape as single-instrument **LTP** (`close`, `ltp`, `token`).

```json
{
    "data": [
        {
            "close": 135880,
            "ltp": 137020,
            "token": 2885
        },
        {
            "close": 112310,
            "ltp": 109000,
            "token": 1594
        },
        {
            "close": 350,
            "ltp": 290,
            "token": 51450
        }
    ],
    "status": "success"
}
```

**Sample response (OHLCV)**

Use `/info/quotes/ohlcv` with the same array body.

```json
{
    "data": [
        {
            "close": 135880,
            "high": 137800,
            "low": 135850,
            "ltp": 136870,
            "ltt": 1778743394,
            "oi": 0,
            "open": 136520,
            "token": 2885,
            "volume": 7252091
        },
        {
            "close": 112310,
            "high": 112190,
            "low": 109000,
            "ltp": 109000,
            "ltt": 1778743394,
            "oi": 0,
            "open": 111980,
            "token": 1594,
            "volume": 7782684
        },
        {
            "close": 350,
            "high": 375,
            "low": 0,
            "ltp": 290,
            "ltt": 1778743378,
            "oi": 1527890,
            "open": 335,
            "token": 51450,
            "volume": 9888905
        }
    ],
    "status": "success"
}
```

**Sample response (FULL)**

Use `/info/quotes/full` with the same array body. Shape matches single **FULL** , repeated per instrument (including `openingOI` when applicable).

```json
{
    "data": [
        {
            "asks": [
                {
                    "orders": 2,
                    "price": 136870,
                    "quantity": 48
                },
                {
                    "orders": 1,
                    "price": 136880,
                    "quantity": 478
                },
                {
                    "orders": 8,
                    "price": 136890,
                    "quantity": 1609
                },
                {
                    "orders": 8,
                    "price": 136900,
                    "quantity": 1339
                },
                {
                    "orders": 12,
                    "price": 136910,
                    "quantity": 1360
                }
            ],
            "avgPrice": 136796,
            "bids": [
                {
                    "orders": 2,
                    "price": 136830,
                    "quantity": 237
                },
                {
                    "orders": 3,
                    "price": 136820,
                    "quantity": 404
                },
                {
                    "orders": 11,
                    "price": 136810,
                    "quantity": 922
                },
                {
                    "orders": 11,
                    "price": 136800,
                    "quantity": 1763
                },
                {
                    "orders": 7,
                    "price": 136790,
                    "quantity": 1971
                }
            ],
            "close": 135880,
            "high": 137800,
            "low": 135850,
            "lowerLimit": 122300,
            "ltp": 136820,
            "ltq": 54,
            "ltt": 1778747141,
            "netChange": 69,
            "netChangeIndicator": 43,
            "oi": 0,
            "oiDayHigh": 0,
            "oiDayLow": 0,
            "open": 136520,
            "openingOI": 0,
            "symbol": "RELIANCE-EQ",
            "time": 1778747141,
            "token": 2885,
            "totalBuyQty": 517653,
            "totalSellQty": 535585,
            "upperLimit": 149460,
            "volume": 10552645
        },
        {
            "asks": [
                {
                    "orders": 8,
                    "price": 109740,
                    "quantity": 352
                },
                {
                    "orders": 17,
                    "price": 109750,
                    "quantity": 799
                },
                {
                    "orders": 5,
                    "price": 109760,
                    "quantity": 299
                },
                {
                    "orders": 10,
                    "price": 109770,
                    "quantity": 422
                },
                {
                    "orders": 10,
                    "price": 109780,
                    "quantity": 505
                }
            ],
            "avgPrice": 109949,
            "bids": [
                {
                    "orders": 1,
                    "price": 109730,
                    "quantity": 991
                },
                {
                    "orders": 2,
                    "price": 109690,
                    "quantity": 57
                },
                {
                    "orders": 3,
                    "price": 109680,
                    "quantity": 806
                },
                {
                    "orders": 5,
                    "price": 109670,
                    "quantity": 924
                },
                {
                    "orders": 10,
                    "price": 109660,
                    "quantity": 2682
                }
            ],
            "close": 112310,
            "high": 112190,
            "low": 108900,
            "lowerLimit": 101080,
            "ltp": 109730,
            "ltq": 991,
            "ltt": 1778747141,
            "netChange": 229,
            "netChangeIndicator": 45,
            "oi": 0,
            "oiDayHigh": 0,
            "oiDayLow": 0,
            "open": 111980,
            "openingOI": 0,
            "symbol": "INFY-EQ",
            "time": 1778747141,
            "token": 1594,
            "totalBuyQty": 505093,
            "totalSellQty": 562611,
            "upperLimit": 123540,
            "volume": 10806977
        },
        {
            "asks": [
                {
                    "orders": 102,
                    "price": 305,
                    "quantity": 153335
                },
                {
                    "orders": 21,
                    "price": 310,
                    "quantity": 21840
                },
                {
                    "orders": 12,
                    "price": 315,
                    "quantity": 13780
                },
                {
                    "orders": 17,
                    "price": 320,
                    "quantity": 18720
                },
                {
                    "orders": 11,
                    "price": 325,
                    "quantity": 11180
                }
            ],
            "avgPrice": 256,
            "bids": [
                {
                    "orders": 95,
                    "price": 300,
                    "quantity": 136370
                },
                {
                    "orders": 103,
                    "price": 295,
                    "quantity": 144170
                },
                {
                    "orders": 96,
                    "price": 290,
                    "quantity": 139945
                },
                {
                    "orders": 87,
                    "price": 285,
                    "quantity": 133770
                },
                {
                    "orders": 78,
                    "price": 280,
                    "quantity": 122005
                }
            ],
            "close": 350,
            "high": 375,
            "low": 0,
            "lowerLimit": 5,
            "ltp": 300,
            "ltq": 65,
            "ltt": 1778747133,
            "netChange": 350,
            "netChangeIndicator": 45,
            "oi": 1422330,
            "oiDayHigh": 2314195,
            "oiDayLow": 1392625,
            "open": 335,
            "openingOI": 2168400,
            "symbol": "NIFTY19MAY26C24900",
            "time": 1778747141,
            "token": 51450,
            "totalBuyQty": 5659030,
            "totalSellQty": 1225289745039360,
            "upperLimit": 3825,
            "volume": 12070630
        }
    ],
    "status": "success"
}
```

The service may not return rows in the same order as the request. **LTP** and **OHLCV** legs are easiest to match using `token` (and your request list). **FULL** responses usually include `symbol` and `token`.

* * *

## Response fields by mode

### LTP

Field | Description
---|---
`token` | Instrument token
`ltp` | Last traded price (scaled integer)
`close` | Previous close / reference close (scaled integer)

### OHLCV

Includes **LTP** fields plus:

Field | Description
---|---
`open` | Open price (scaled integer)
`high` | High price (scaled integer)
`low` | Low price (scaled integer)
`volume` | Traded volume
`ltt` | Last trade time (Unix seconds)
`oi` | Open interest (useful for derivatives; may be `0` on cash)

### FULL

Includes **OHLCV** -style fields where applicable, plus:

Field | Description
---|---
`symbol` | Trading symbol
`ltq` | Last traded quantity
`avgPrice` | Average traded price (scaled integer)
`time` | Quote / book timestamp (Unix seconds)
`netChange` | Net change vs reference
`netChangeIndicator` | Direction flag (for example `43` up, `45` down; aligns with streaming conventions)
`upperLimit` | Upper price band / circuit
`lowerLimit` | Lower price band / circuit
`totalBuyQty` | Total buy quantity on book
`totalSellQty` | Total sell quantity on book
`oiDayHigh` | Day high open interest
`oiDayLow` | Day low open interest
`openingOI` | Session open OI (when sent by the service)
`bids` | Up to five bid levels: `price`, `quantity`, `orders`
`asks` | Up to five ask levels: `price`, `quantity`, `orders`

Use the same `TradingSymbol` and exchange codes as in the [symbols](../symbols/) instrument download so request symbols stay aligned with the rest of the platform.

* * *

## Error handling

Failures follow the same patterns as other REST APIs: see [Error codes](../error-codes/) and [Response structure](../response-structure/).
