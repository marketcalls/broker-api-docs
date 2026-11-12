<!-- Source: https://vortex.rupeezy.in/docs/2.2/reports/ -->

# Backoffice Reports

Use the below apis to fetch reports:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `GET` | [{{base_url}}/reports/trades/{segment}?from_date={from_date}&to_date={to_date}](#trades) | Fetch segment wise trades | 1/sec |
| `GET` | [{{base_url}}/reports/turnover/details/{segment}?from_date={from_date}&to_date={to_date}](#turnover-summary) | Fetch segment wise turnover details | 1/sec |
| `GET` | [{{base_url}}/reports/turnover/summary/{segment}?from_date={from_date}&to_date={to_date}](#turnover-details) | Fetch segment wise turnover summary | 1/sec |
| `GET` | [{{base_url}}/reports/pnl/{segment}?from_date={from_date}&to_date={to_date}](#profit-loss) | Fetch segment wise pnl | 1/sec |
| `GET` | [{{base_url}}/reports/mft_interest?from_date={from_date}&to_date={to_date}](#pay-latermtf-interest) | Fetch MTF interest report | 1/sec |

## Common Parameters

| field | description |
| --- | --- |
| `segment` | Can be [`EQUITY`, `EQUITY_DERIVATIVE`, `CURRENCY`, `COMMODITY`, `MTF`]. `MTF` segment is available only in trade report. |
| `from_date` | Report starting date in `YYYY-MM-DD` format |
| `to_date` | Report ending date in `YYYY-MM-DD` format |

## Trades

### Fetching Trades

```
Endpoint: {{base_url}}/reports/trades/{segment}?from_date={from_date}&to_date={to_date}
```

### Trades report response

```
{
    "status":"success",
    "data": [
        {
            "symbol": "NIFTY",
            "instrument_type": "FUTIDX",
            "option_type": "",
            "expiry_date": "2023-07-27",
            "strike_price": 0,
            "traded_at_date": "2023-07-13",
            "traded_at_time": "13:47:25",
            "traded_at": "2023-07-13T13:47:25+05:30",
            "tradingsymbol": "NIFTY FUTIDX 27/07/23",
            "quantity": 100,
            "price": 19573,
            "order_id": "1900000053763593",
            "trade_id": "775396828",
            "series": "",
            "segment": "EQUITY_DERIVATIVES",
            "side": "SELL"
        },
        {
            "symbol": "BANKNIFTY",
            "instrument_type": "FUTIDX",
            "option_type": "",
            "expiry_date": "2023-07-27",
            "strike_price": 0,
            "traded_at_date": "2023-07-13",
            "traded_at_time": "13:43:56",
            "traded_at": "2023-07-13T13:43:56+05:30",
            "tradingsymbol": "BANKNIFTY FUTIDX 27/07/23",
            "quantity": 30,
            "price": 44980,
            "order_id": "1300000053908670",
            "trade_id": "258506973",
            "series": "",
            "segment": "EQUITY_DERIVATIVES",
            "side": "SELL"
        }
    ]
}
```

## Turnover Details

### Fetching Turnover Details

```
Endpoint: {{base_url}}/reports/turnover/details/{segment}?from_date={from_date}&to_date={to_date}
```

### EQUITY Turnover report response

```
{
    "status": "success"
    "data": [
        {
            "particular": "HDFCBANK",
            "series": "EQ",
            "name": "HDFC BANK LTD",
            "trading_turnover": 3300.65,
            "delivery_turnover": 0,
            "total_turnover": 3300.65,
            "buy_side_trading_brokerage": 1,
            "sell_side_trading_brokerage": 1,
            "buy_side_delivery_brokerage": 0,
            "sell_side_delivery_brokerage": 0,
            "service_tax": 0.38
        },
        {
            "particular": "ITC",
            "series": "EQ",
            "name": "ITC LTD",
            "trading_turnover": 4379.7,
            "delivery_turnover": 0,
            "total_turnover": 4379.7,
            "buy_side_trading_brokerage": 6,
            "sell_side_trading_brokerage": 6,
            "buy_side_delivery_brokerage": 0,
            "sell_side_delivery_brokerage": 0,
            "service_tax": 2.19
        },
        {
            "particular": "JPPOWER",
            "series": "EQ",
            "name": "JAIPRAKASH POWER VEN. LTD",
            "trading_turnover": 26.7,
            "delivery_turnover": 0,
            "total_turnover": 26.7,
            "buy_side_trading_brokerage": 0.35,
            "sell_side_trading_brokerage": 0.35,
            "buy_side_delivery_brokerage": 0,
            "sell_side_delivery_brokerage": 0,
            "service_tax": 0.13
        },
        {
            "particular": "RELIANCE",
            "series": "EQ",
            "name": "RELIANCE INDUSTRIES LTD",
            "trading_turnover": 9742.85,
            "delivery_turnover": 0,
            "total_turnover": 9742.85,
            "buy_side_trading_brokerage": 2,
            "sell_side_trading_brokerage": 1,
            "buy_side_delivery_brokerage": 0,
            "sell_side_delivery_brokerage": 0,
            "service_tax": 0.6
        },
        {
            "particular": "SBIN",
            "series": "EQ",
            "name": "STATE BANK OF INDIA",
            "trading_turnover": 32541.75,
            "delivery_turnover": 0,
            "total_turnover": 32541.75,
            "buy_side_trading_brokerage": 16,
            "sell_side_trading_brokerage": 24,
            "buy_side_delivery_brokerage": 0,
            "sell_side_delivery_brokerage": 0,
            "service_tax": 7.41
        },
        {
            "particular": "SUB-TOTAL  FOR CLIENT CODE: XXXXX  (YYYY)",
            "series": "",
            "name": "",
            "trading_turnover": 49991.65,
            "delivery_turnover": 0,
            "total_turnover": 49991.65,
            "buy_side_trading_brokerage": 25.35,
            "sell_side_trading_brokerage": 32.35,
            "buy_side_delivery_brokerage": 0,
            "sell_side_delivery_brokerage": 0,
            "service_tax": 10.71
        },
        {
            "particular": "TOTALS",
            "series": "",
            "name": "",
            "trading_turnover": 49991.65,
            "delivery_turnover": 0,
            "total_turnover": 49991.65,
            "buy_side_trading_brokerage": 25.35,
            "sell_side_trading_brokerage": 32.35,
            "buy_side_delivery_brokerage": 0,
            "sell_side_delivery_brokerage": 0,
            "service_tax": 10.71
        }
    ]
}
```

### Derivatives Turnover report response

```
{
    "status": "success"
    "data": [
        {
            "symbol": "BANKNIFTY",
            "instrument_type": "OPTIDX",
            "expiry_date": "2023-02-23",
            "strike_price": 39800,
            "option_type": "CE",
            "futures_traded_value": 0,
            "options_traded_value": 6177.5,
            "exercise_value": 0,
            "assignment_value": 0,
            "close_out_value": 0,
            "total": 6177.5,
            "brokerage": 0.02,
            "service_tax": 0.594,
            "stt": 1.5638,
            "turnover_tax": 3.2741,
            "sebi_tax": 0.0062,
            "stamp_duty": 0,
            "clearing_charges": 0,
            "ctt_charges": 0,
            "sbc_charges": 0,
            "kkc_charges": 0
        },
        {
            "symbol": "BANKNIFTY",
            "instrument_type": "OPTIDX",
            "expiry_date": "2023-02-23",
            "strike_price": 39900,
            "option_type": "CE",
            "futures_traded_value": 0,
            "options_traded_value": 4211.25,
            "exercise_value": 0,
            "assignment_value": 0,
            "close_out_value": 0,
            "total": 4211.25,
            "brokerage": 0.02,
            "service_tax": 0.4061,
            "stt": 1.0369,
            "turnover_tax": 2.232,
            "sebi_tax": 0.0042,
            "stamp_duty": 0,
            "clearing_charges": 0,
            "ctt_charges": 0,
            "sbc_charges": 0,
            "kkc_charges": 0
        },
        {
            "symbol": "BANKNIFTY",
            "instrument_type": "OPTIDX",
            "expiry_date": "2023-02-23",
            "strike_price": 40000,
            "option_type": "CE",
            "futures_traded_value": 0,
            "options_traded_value": 12057.5,
            "exercise_value": 0,
            "assignment_value": 0,
            "close_out_value": 0,
            "total": 12057.5,
            "brokerage": 0.02,
            "service_tax": 1.1558,
            "stt": 3.308,
            "turnover_tax": 6.3904,
            "sebi_tax": 0.012,
            "stamp_duty": 0,
            "clearing_charges": 0,
            "ctt_charges": 0,
            "sbc_charges": 0,
            "kkc_charges": 0
        }
    ]
}
```

## Turnover Summary

### Fetching Turnover Summary

```
Endpoint: {{base_url}}/reports/turnover/summary/{segment}?from_date={from_date}&to_date={to_date}
```

### EQUITY Turnover summary report response

```
{
    "status": "success"
    "data": [
        {
        "trading_turnover": 924666.06,
        "delivery_turnover": 665236.5,
        "total_turnover": 1589902.5,
        "buy_side_trading_brokerage": 183.6,
        "sell_side_trading_brokerage": 168.53,
        "buy_side_delivery_brokerage": 4.58,
        "sell_side_delivery_brokerage": 2.08,
        "service_tax": 73.62
    }
    ]
}
```

### Derivatives Turnover report response

```
{
    "status": "success"
    "data": [
       {
            "futures_traded_value": 10221290,
            "options_traded_value": 1045337.5,
            "exercise_value": 0,
            "assignment_value": 0,
            "close_out_value": 0,
            "total": 11266628,
            "brokerage": 20.48,
            "service_tax": 140.4188,
            "stt": 863,
            "turnover_tax": 748.4407,
            "sebi_tax": 11.2562,
            "stamp_duty": 113,
            "clearing_charges": 0,
            "ctt_charges": 0,
            "sbc_charges": 0,
            "kkc_charges": 0
        }
    ]
}
```

## Profit & Loss

### Fetching Profit & Loss report

```
Endpoint: {{base_url}}/reports/pnl/{segment}?from_date={from_date}&to_date={to_date}
```

### EQUITY Profit & Loss report response

```
{
    "status":"success",
    "data": [
        {
            "symbol": "DOLLAR",
            "name": "DOLLAR INDUSTRIES LIMITED",
            "isin": "INE325C01035",
            "sell_quantity": 9,
            "sell_price": 454.15,
            "sell_value": 0,
            "buy_quantity": 9,
            "buy_price": 440.58,
            "buy_value": 0,
            "close_price": 0,
            "close_value": 0,
            "pnl": 122.17,
            "tax": 18.33,
            "type": "SHORT TERM"
        },
        {
            "symbol": "ITC",
            "name": "ITC LTD",
            "isin": "INE154A01025",
            "sell_quantity": 0,
            "sell_price": 0,
            "sell_value": 0,
            "buy_quantity": 2,
            "buy_price": 338.97,
            "buy_value": 0,
            "close_price": 472,
            "close_value": 944,
            "pnl": 266.06,
            "tax": 0,
            "type": "FREE"
        },
        {
            "symbol": "ACC",
            "name": "ACC LIMITED",
            "isin": "INE012A01025",
            "sell_quantity": 5,
            "sell_price": 2051.44,
            "sell_value": 0,
            "buy_quantity": 5,
            "buy_price": 2052.67,
            "buy_value": 0,
            "close_price": 0,
            "close_value": 0,
            "pnl": -6.13,
            "tax": -1.84,
            "type": "SPECULATION"
        }
    ]
}
```

### Derivatives Profit & Loss report response

```
{
    "status":"success",
    "data": [
        {
            "symbol": "BANKNIFTY",
            "instrument_type": "FUTIDX",
            "expiry_date": "2023-07-27",
            "strike_price": 0,
            "option_type": "",
            "open_quantity": 0,
            "buy_quantity": 30,
            "buy_value": 1338990,
            "buy_price": 44633,
            "sell_quantity": 30,
            "sell_value": 1349400,
            "sell_price": 44980,
            "net_quantity": 0,
            "net_value": -10410,
            "pnl": 10410
        }
    ]
}
```

## Pay Later(MTF) Interest

### Fetching Pay Later(MTF) Interest report

```
Endpoint: {{base_url}}/reports/mtf_interest?from_date={from_date}&to_date={to_date}
```

### Pay Later(MTF) Interest report response

```
{
    "status":"success",
    "data": [
        {
            "date": "2023-07-12",
            "running_balance": 319.79,
            "interest_rate": 14.9,
            "interest_amount": 0.13
        },
        {
            "date": "2023-07-11",
            "running_balance": 318.96,
            "interest_rate": 14.9,
            "interest_amount": 0.13
        },
        {
            "date": "2023-07-10",
            "running_balance": 319.07,
            "interest_rate": 14.9,
            "interest_amount": 0.13
        }
    ]
}
```
