<!-- Source: https://vortex.rupeezy.in/docs/2.2/historical/ -->

# Data

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `GET` | [{{base_url}}/data/quotes?q=ticker&mode=mode](#fetch-price-quotes) | Fetch quotes of upto 1000 scrips | 1/sec |
| `GET` | [{{base_url}}/data/history?ticker={ticker}&to={to}&from={from}&resolution={resolution}](#fetch-historical-candle-data) | Fetch minute level historical candles | 1/sec |

## Fetch Price Quotes

```
Endpoint: {{base_url}}/data/quotes?q=ticker&mode=mode
```

| Query Param | Description |
| --- | --- |
| q | List of instrument tickers (recommended) e.g. `q=NSE:RELIANCE&q=NSE:NIFTY26JUL25000CE`. |
| mode | Type of quote needed. Possible values: [full,ohlc,ltp] |

> [!NOTE]
>
> It is possible that not all the symbol identifiers you passed had a quote available. Those inputs will be missing from the response. Also, the order of output might be different than the order of input

### Fetch Price Quote response

The keys in the response map match the form of `q` that you sent (`NSE:RELIANCE` or `NSE_EQ-22`).

```
{
    "status": "success",
    "data": {
        "NSE:ACC": {
            "ticker": "NSE:ACC",
            "exchange": "NSE_EQ",
            "token": 22,
            "last_trade_time": 1681122520,
            "last_update_time": 1681122520,
            "last_trade_price": 1740.95,
            "volume": 407043,
            "average_trade_price": 1736.52,
            "total_buy_quantity": 586,
            "open_price": 1718,
            "high_price": 1915,
            "low_price": 1566.85,
            "close_price": 1712,
            "depth": {
                "buy": [
                    {
                        "price": 1740.95,
                        "quantity": 586
                    },
                    {},
                    {},
                    {},
                    {}
                ],
                "sell": [
                    {},
                    {},
                    {},
                    {},
                    {}
                ]
            },
            "dpr_high": 188320,
            "dpr_low": 154080
        },
        "NSE:NIFTY": {
            "ticker": "NSE:NIFTY",
            "exchange": "NSE_EQ",
            "token": 26000,
            "last_trade_time": 316111421,
            "last_update_time": 1681120911,
            "last_trade_price": 17624.05,
            "total_buy_quantity": 7738434276633480,
            "open_price": 17634.9,
            "high_price": 17694.1,
            "low_price": 17597.95,
            "close_price": 17599.15,
            "depth": {
                "buy": [
                    {},
                    {},
                    {},
                    {},
                    {}
                ],
                "sell": [
                    {},
                    {},
                    {},
                    {},
                    {}
                ]
            }
        },
        "NSE:NIFTY26JUL25000CE": {
            "ticker": "NSE:NIFTY26JUL25000CE",
            "exchange": "NSE_FO",
            "token": 135938,
            "last_trade_time": 1681120758,
            "last_update_time": 1681120758,
            "last_trade_price": 104.1,
            "volume": 23700,
            "average_trade_price": 103.33,
            "total_buy_quantity": 19500,
            "total_sell_quantity": 12450,
            "open_interest": 15450,
            "open_price": 100.15,
            "high_price": 299.85,
            "low_price": 0.05,
            "close_price": 99.8,
            "depth": {
                "buy": [
                    {
                        "price": 102.15,
                        "quantity": 150,
                        "orders": 1
                    },
                    {
                        "price": 102.1,
                        "quantity": 150,
                        "orders": 1
                    },
                    {
                        "price": 102.05,
                        "quantity": 150,
                        "orders": 1
                    },
                    {
                        "price": 96.5,
                        "quantity": 150,
                        "orders": 1
                    },
                    {
                        "price": 87,
                        "quantity": 4500,
                        "orders": 1
                    }
                ],
                "sell": [
                    {
                        "price": 106.55,
                        "quantity": 150
                    },
                    {
                        "price": 106.6,
                        "quantity": 150,
                        "orders": 1
                    },
                    {
                        "price": 106.65,
                        "quantity": 300,
                        "orders": 2
                    },
                    {
                        "price": 107.75,
                        "quantity": 150,
                        "orders": 1
                    },
                    {
                        "price": 111.8,
                        "quantity": 150,
                        "orders": 1
                    }
                ]
            },
            "dpr_high": 28380,
            "dpr_low": 5
        }
    }
}
```

## Fetch Historical Candle Data

```
Endpoint: {{base_url}}/data/history?ticker={ticker}&to={to}&from={from}&resolution={resolution}
```

| param | description |
| --- | --- |
| ticker | Instrument ticker in `EXCHANGE:SYMBOL` form (e.g. `NSE:RELIANCE`). Recommended. Pass **either** `ticker` **or** (`exchange` + `token`). |
| exchange | Exchange in which the token is listed. Possible values: [NSE_EQ,NSE_FO,NSE_CUR,MCX_FO]. Required if `ticker` is not provided. |
| token | Token assigned to the instrument. Required if `ticker` is not provided. |
| from | Unix timestamp in seconds, from which you want your data |
| to | Unix timestamp in seconds, up to which you want your data |
| resolution | Candle resolution. Minute resolutions supported: [1,2,3,4,5,10,15,30,45,60,120,180,240]. Aggregate resolutions: [1D,1W,1M] |

### Historical Data Response

```
{
    "s": "ok",
    "t": [
        1683540900,
        1683537300,
        1683299700,
        ...
    ],
    "c": [
        1765.7,
        1766.7,
        1765.9,
        ...
    ],
    "o": [
        1765.9,
        1760.65,
        1766.55,
        ...
    ],
    "h": [
        1765.95,
        1769.35,
        1766.85,
        ...
    ],
    "l": [
        1764.7,
        1760.65,
        1765,
        ...
    ],
    "v": [
        850,
        3625,
        3910,
        ...
    ]
}
```

| field | description |
| --- | --- |
| t | Array of timestamps containing unix timestamp of beginning of the candle |
| o | Array of open price |
| h | Array of high price |
| l | Array of low price |
| c | Array of close price |
| v | Array of volume |
