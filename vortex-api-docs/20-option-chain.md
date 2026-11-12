<!-- Source: https://vortex.rupeezy.in/docs/2.2/option_chain/ -->

# Greeks & Option Chain

Use the below apis:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `POST` | [{{base_url}}/strategies/option_chain](#option-chain) | Fetch the option chain | 1/sec |

## Option Chain

```
Endpoint: /strategies/option_chain
```

### Option Chain Payload

```
{   
    "symbol":"NIFTY",
    "token":26000,
    "exchange":"NSE_EQ",
    "expiry_date":"20240201",
    "greeks":true
}
```

| params | required | description |
| --- | --- | --- |
| exchange | Y | Possible values: [NSE_EQ,NSE_FO, NSE_CUR or MCX_FO] |
| symbol | Y | Symbol of the underlying asset. For e.g. NIFTY, BANKNIFTY,RELIANCE |
| expiry_date | Y | Expiry date of options in `YYYYMMDD` format |
| greeks | Y | Should be passed as `true` if you want greeks calculation included, otherwise `false` |

### Option Chain Response

```
{
    "status": "success",
    "message": "",
    "response": {
        "symbol": "NIFTY",
        "expiry_date": "20240201",
        "has_parent_stock": true,
        "expiry_dates": [
           .
           .
            "20240328",
            "20240627",
            .
            .
        ],
        "options": {
            "exchange": "NSE_FO",
            "list": [
               .
               .
               .
                {
                    "strike_price": 21000,
                    "iv": 15.04,
                    "theta": -5.74,
                    "vega": 7.62,
                    "gamma": 0.0003,
                    "CE": {
                        "token": 37954,
                        "instrument_name": "OPTIDX",
                        "lot_size": 50,
                        "security_description": "NIFTY2420121000CE",
                        "eligibility": 1,
                        "ltp": 717.45,
                        "open_interest": 51100,
                        "day_first_tick_oi": 0,
                        "volume": 0,
                        "delta": 0.86
                    },
                    "PE": {
                        "token": 37955,
                        "instrument_name": "OPTIDX",
                        "lot_size": 50,
                        "security_description": "NIFTY2420121000PE",
                        "eligibility": 1,
                        "ltp": 35.95,
                        "open_interest": 512850,
                        "day_first_tick_oi": 0,
                        "volume": 0,
                        "delta": -0.14
                    }
                },
                {
                    "strike_price": 21050,
                    "iv": 14.7,
                    "theta": -6.08,
                    "vega": 8.25,
                    "gamma": 0.0004,
                    "CE": {
                        "token": 37956,
                        "instrument_name": "OPTIDX",
                        "lot_size": 50,
                        "security_description": "NIFTY2420121050CE",
                        "eligibility": 1,
                        "ltp": 628.05,
                        "open_interest": 1250,
                        "day_first_tick_oi": 0,
                        "volume": 0,
                        "delta": 0.85
                    },
                    "PE": {
                        "token": 37957,
                        "instrument_name": "OPTIDX",
                        "lot_size": 50,
                        "security_description": "NIFTY2420121050PE",
                        "eligibility": 1,
                        "ltp": 40.55,
                        "open_interest": 63600,
                        "day_first_tick_oi": 0,
                        "volume": 0,
                        "delta": -0.15
                    }
                },
                {
                    "strike_price": 21100,
                    "iv": 14.52,
                    "theta": -6.54,
                    "vega": 8.99,
                    "gamma": 0.0004,
                    "CE": {
                        "token": 37958,
                        "instrument_name": "OPTIDX",
                        "lot_size": 50,
                        "security_description": "NIFTY2420121100CE",
                        "eligibility": 1,
                        "ltp": 628,
                        "open_interest": 11250,
                        "day_first_tick_oi": 0,
                        "volume": 0,
                        "delta": 0.83
                    },
                    "PE": {
                        "token": 37959,
                        "instrument_name": "OPTIDX",
                        "lot_size": 50,
                        "security_description": "NIFTY2420121100PE",
                        "eligibility": 1,
                        "ltp": 47.2,
                        "open_interest": 484900,
                        "day_first_tick_oi": 0,
                        "volume": 0,
                        "delta": -0.17
                    }
                },
                .
                .

            ]
        },
        "parent": {
            "symbol": "NIFTY",
            "exchange": "NSE_EQ",
            "token": 26000,
            "isin": "",
            "ltp": 21586
        }
    }
```

}   
|field|description|
|---|---|
|status|Possible values: [success,error] |
|message|Error message if any|
|symbol|Symbol of the underlying asset. For e.g. NIFTY, BANKNIFTY,RELIANCE|
|expiry_date|Expiry date for which option chain is returned|
|available_expiry_dates|List of all expiry dates available for the symbol|
|strikes|Array containing CE and PE options of all strike prices|
|iv|IV of both CE and PE. If strike price is grater than spot price, it is CE IV, otherwise it is PE IV|

## IV Calculation

We use Black-76 model, which is a variant of the well known Black Scholes model. It is better suited for the Indian markets and is widely used by professional quants.

In this model, we:

- Assume no interest rate
- Assume no dividend etc
- Use Future Prices instead of Stock Prices for stock options
- Use Index Prices for index options

It is assumed that interest rate and dividends are accounted for in Future Prices.

According to Black Scholes theory and in practical efficient markets,

- IV for call and put options for the same expiry and same strike price should be the same
- IV for call and put options for the same expiry and different strike price should be different

However, this is not always true in India because:

- Securities Transaction Tax affects ITM options and brings down volatility
- Inefficiency due to wide bid-ask spreads

NSE uses Black Scholes model with its own twist. It assumes a constant interest rate of 10% (which is not true as RBI keeps on changing it). Even ATM strikes have two very different IVs, whereas it should be the same.

Put Call Parity says that:

```
Call Price - Put Price = Future Price - Strike Price.
```

If we use different IVs in call and put price calculation, this equation will not add up. So, we use the IV of the OTM option and use it for both Put and Call option.
