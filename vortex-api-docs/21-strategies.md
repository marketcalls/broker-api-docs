<!-- Source: https://vortex.rupeezy.in/docs/2.2/strategies/ -->

# Greeks & Strategies

Use the below apis:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `POST` | [{{base_url}}/strategies](#pre-built-strategies) | Fetch prebuilt strategies | 1/sec |
| `POST` | [{{base_url}}/strategies/build](#build-strategy) | Find suitable strategy as per your prediction amongst prebuilt strategies | 1/sec |
| `POST` | [{{base_url}}/strategies/payoff](#payoff-graph) | Get payoff graph of any combination of options of same underlying | 1/sec |

## Pre-built strategies

Pre built strategies are a set of some standard options strategies.

```
Endpoint: /strategies
```

### Pre-built Strategy Object

```
{
    "symbol": "BANKNIFTY", 
    "token": 26009,
    "expiry_date": "20240125"
}
```

| params | required | description |
| --- | --- | --- |
| symbol | Y | Symbol of the underlying asset. For e.g. NIFTY, BANKNIFTY,RELIANCE |
| token | Y | Token of the underlying asset. For e.g. NIFTY, BANKNIFTY,RELIANCE |
| expiry_date | Y | Expiry date of options in `YYYYMMDD` format |

### Available Strategies

- Bull Call Spread
- Bull Put Spread
- Ratio Call Spread
- Ratio Put Spread
- Bear Call Spread
- Bear Put Spread
- Short Strangle
- Long Strangle
- Iron Condor
- Iron Butterfly
- Short Straddle
- Long Straddle

### Pre-built Strategies Response

```
{
    "symbol": "BANKNIFTY",
    "underlying_last_trade_price": 44747.35,
    "strategies": [
        .
        .
        .
        {
            "strategy_name": "Bull Call Spread",
            "trading_opportunities": [
                .
                .
                .
                {
                    "legs": [
                        {
                            "option": {
                                "token": 43321,
                                "exchange": "NSE_FO",
                                "last_trade_price": 259.85,
                                "lot_size": 25,
                                "greeks": {
                                    "theta": -21.0399528105652,
                                    "delta": 0.5325763242304223,
                                    "gamma": 0.0000062658546043891884,
                                    "vega": 22.804010475731573,
                                    "iv": 11.064360901855252
                                }
                            },
                            "action": "BUY",
                            "quantity": 1
                        },
                        {
                            "option": {
                                "token": 43323,
                                "exchange": "NSE_FO",
                                "last_trade_price": 206.55,
                                "lot_size": 25,
                                "greeks": {
                                    "theta": -19.2604620643973,
                                    "delta": 0.466499384000364,
                                    "gamma": 0.0000068421241527056196,
                                    "vega": 22.799615376617837,
                                    "iv": 10.130525752174435
                                }
                            },
                            "action": "SELL",
                            "quantity": 1
                        }
                    ],
                    "max_loss": 1332.5,
                    "max_profit": 1167.5,
                    "infinite_loss": false,
                    "infinite_profit": false,
                    "breakevens": [
                        44753.3
                    ]
                },
                .
                .
                .
            ]
        },
        .
        .
        .
    ]
}
```

## Build Strategy

You can use this API to find suitable options strategy amongst the prebuilt strategies based on your prediction. You need to frame your prediction in one of the following ways:

- On expiry day, the price of XYZ underlying will close above 123
- On expiry day, the price of XYZ underlying will close below 123
- On expiry day, the price of XYZ underlying will be between 123 and 456

  Endpoint: /strategies/build

### Strategy Builder Request

```
{
    "expiry_date": "20240207",
    "prediction": "BELOW",
    "price_range": [
        45000
    ],
    "token": 26009,
    "symbol": "BANKNIFTY"
}
```

| param | required | description |
| --- | --- | --- |
| symbol | Y | Symbol name of the underlying instrument whose options you want to trade. e.g. NIFTY, BANKNIFTY, RELIANCE |
| token | Y | Token of the underlying instrument whose options you want to trade. e.g. NIFTY, BANKNIFTY, RELIANCE |
| expiry_date | Y | Expiry date in `YYYYMMDD` format of the options you want to trade in |
| prediction | Y | Can be `ABOVE`, `BETWEEN`, `BELOW` |
| price_range | Y | The price comparator array for the prediction. For `ABOVE` and `BELOW`, the array will have only one value. For `BETWEEN`, array will have two values. |

### Strategy Builder Response

```
{
    "symbol": "NIFTY",
    "underlying_last_trade_price": 19189.05,
    "strategies": [
        .
        .
        .
        {
            "strategy_name": "Bull Call Spread",
            "legs": [
                {
                    "option": {
                        "token": 47068,
                        "exchange": "NSE_FO",
                        "last_trade_price": 73.4,
                        "greeks": {
                            "theta": -6.557030012704283,
                            "delta": 0.4799310187242114,
                            "gamma": 0.002018924995491476400,
                            "vega": 9.799378359840057,
                            "iv": 8.024194533390983
                        }
                    },
                    "action": "BUY",
                    "quantity": 50
                },
                {
                    "option": {
                        "token": 47072,
                        "exchange": "NSE_FO",
                        "last_trade_price": 50.35,
                        "greeks": {
                            "theta": -6.110168123520634,
                            "delta": 0.37801903461535696,
                            "gamma": 0.001972209734122132500,
                            "vega": 9.349491201396154,
                            "iv": 7.837146888959978
                        }
                    },
                    "action": "SELL",
                    "quantity": 50
                }
            ],
            "max_loss": 1152.5,
            "max_profit": 1347.5,
            "infinite_loss": false,
            "infinite_profit": false,
            "breakevens": [
                19223.05
            ]
        },
        .
        .
        .
    ]
}
```

## Payoff Graph

Payoff graph calculation takes any two options and plots the payoff with respect to change in price of underlying instrument. It also calculates portfolio greeks.

```
Endpoint: /strategies/payoff
```

### Payoff Graph Request

```
{
    "exchange": "NSE_FO",
    "legs": [
        {
            "token": 43321,
            "action": "BUY"
        }, 
        {
            "token": 43454,
            "action": "SELL"
        }, 
    ]
}
```

### Payoff Graph Response

```
{
    "status": "success",
    "message": "",
    "payoff": {
        "max_loss": -1332.5,
        "max_profit": 1167.5,
        "infinite_profit": false,
        "infinite_loss": false,
        "underlying_last_trade_price": 44747.35,
        "min_days_to_expiry": 4,
        "breakevens": [
            44775.0
        ],
        "combined_greeks": {
            "theta": -7.683021434580801,
            "delta": 1.7024994338249908,
            "gamma": -0.000276598900187174300,
            "vega": -0.134624688420877
        },
        "leg_greeks": [
            {
                "token": 43321,
                "strike_price": 44700.0,
                "option_type": "CE",
                "expiry_date": "20230706",
                "action": "BUY",
                "quantity": 1,
                "last_trade_price": 259.85,
                "greeks": {
                    "iv": 10.294600364886719,
                    "theta": -19.56778292178049,
                    "delta": 0.5345993613533636,
                    "gamma": 0.00067314845926307500,
                    "vega": 22.794230389080997
                }
            },
            {
                "token": 43323,
                "strike_price": 44800.0,
                "option_type": "CE",
                "expiry_date": "20230706",
                "action": "SELL",
                "quantity": 1,
                "last_trade_price": 206.55,
                "greeks": {
                    "iv": 10.130525752174435,
                    "theta": -19.2604620643973,
                    "delta": 0.466499384000364,
                    "gamma": 0.0006842124152705619600,
                    "vega": 22.799615376617837
                }
            }
        ],
        "pay_offs": [
           .
           .
           .
            {
                "intraday_pay_off": 1055.8099140000006,
                "expiry_pay_off": 1167.5,
                "at": 45700.0
            },
            {
                "intraday_pay_off": 1074.2238729999988,
                "expiry_pay_off": 1167.5,
                "at": 45750.0
            },
            {
                "intraday_pay_off": 1090.0646927499986,
                "expiry_pay_off": 1167.5,
                "at": 45800.0
            },
            .
            .
            .

        ]
    }
}
```
