# Market Analytics

Derivatives and institutional-activity analytics for the NSE segments. Introduced as the "New Market Information APIs" on 11 May 2026.

---

## Open Interest (OI) Data

API for retrieving Open Interest data across all strike prices for an underlying asset on a given expiry and date. It accepts the instrument key, expiry, and date, and returns aggregate call and put OI totals along with a per-strike breakdown of call OI and put OI.

### Endpoint

**GET** `https://api.upstox.com/v2/market/oi`

### Query Parameters

| Name | Required | Description |
| --- | --- | --- |
| instrument_key | Required | Underlying asset instrument key. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern) . |
| expiry | Required | Expiry of the option contract. Accepts either a date in `YYYY-MM-DD` format or a relative expiry keyword. **Weekly:**`current_week` , `next_week` , `far_week` . **Monthly:**`current_month` , `next_month` , `far_month` . Using keywords keeps strategies always up-to-date and rolls over automatically after each expiry. |
| date | Required | Date for which OI data is required, in `YYYY-MM-DD` format. |

#### Response body

```json
{
  "status": "success",
  "data": {
    "total_puts": 12500000,
    "total_calls": 9800000,
    "spot_closing_price": 24450.75,
    "expiry": "2026-05-29",
    "call_put_oi_data_list": [
      {
        "call_oi": 450000,
        "put_oi": 680000,
        "strike_price": 24000.0
      },
      {
        "call_oi": 1200000,
        "put_oi": 950000,
        "strike_price": 24500.0
      }
    ]
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` for successful operations. |
| data | object | OI data object. |
| data.total_puts | integer | Aggregate put open interest across all strikes. |
| data.total_calls | integer | Aggregate call open interest across all strikes. |
| data.spot_closing_price | number | Closing spot price of the underlying asset. |
| data.expiry | string | Expiry date of the option contract. |
| data.call_put_oi_data_list | array | OI data for each strike price. |
| data.call_put_oi_data_list[].call_oi | integer | Call open interest at this strike. |
| data.call_put_oi_data_list[].put_oi | integer | Put open interest at this strike. |
| data.call_put_oi_data_list[].strike_price | number | Strike price. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI100011 | **Invalid instrument_key** — The provided `instrument_key` is invalid or not found. |
| UDAPI1202 | **Invalid expiry date format** — The `expiry` parameter must be in `YYYY-MM-DD` format. |
| UDAPI1203 | **Invalid date format** — The `date` parameter must be in `YYYY-MM-DD` format. |

---

## Change in Open Interest (OI)

API for retrieving the change in Open Interest per strike price for an underlying asset over a specified number of days. It accepts the instrument key, expiry, date, and interval, and returns the net OI change at each strike for both calls and puts — positive values indicate new positions being built, negative values indicate unwinding.

### Endpoint

**GET** `https://api.upstox.com/v2/market/change-oi`

### Query Parameters

| Name | Required | Description |
| --- | --- | --- |
| instrument_key | Required | Underlying asset instrument key. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern) . |
| expiry | Required | Expiry of the option contract. Accepts either a date in `YYYY-MM-DD` format or a relative expiry keyword. **Weekly:**`current_week` , `next_week` , `far_week` . **Monthly:**`current_month` , `next_month` , `far_month` . Using keywords keeps strategies always up-to-date and rolls over automatically after each expiry. |
| date | Required | Date for which Change in OI data is required, in `YYYY-MM-DD` format. |
| interval | Required | Number of days over which the OI difference is calculated. |

#### Response body

```json
{
  "status": "success",
  "data": {
    "total_put_change_oi": 2500000,
    "total_call_change_oi": -1800000,
    "spot_closing_price": 24450.75,
    "expiry": "2026-05-29",
    "call_put_oi_data_list": [
      {
        "strike_price": 24000.0,
        "call_change_oi": -120000,
        "put_change_oi": 350000
      },
      {
        "strike_price": 24500.0,
        "call_change_oi": 280000,
        "put_change_oi": -150000
      }
    ]
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` for successful operations. |
| data | object | Change in OI data object. |
| data.total_put_change_oi | integer | Net change in put OI across all strikes. |
| data.total_call_change_oi | integer | Net change in call OI across all strikes. |
| data.spot_closing_price | number | Closing spot price of the underlying asset. |
| data.expiry | string | Expiry date of the option contract. |
| data.call_put_oi_data_list | array | Change in OI data for each strike price. |
| data.call_put_oi_data_list[].strike_price | number | Strike price. |
| data.call_put_oi_data_list[].call_change_oi | integer | Change in call OI at this strike. Negative values indicate OI unwinding. |
| data.call_put_oi_data_list[].put_change_oi | integer | Change in put OI at this strike. Negative values indicate OI unwinding. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI100011 | **Invalid instrument_key** — The provided `instrument_key` is invalid or not found. |
| UDAPI1202 | **Invalid expiry date format** — The `expiry` parameter must be in `YYYY-MM-DD` format. |
| UDAPI1203 | **Invalid date format** — The `date` parameter must be in `YYYY-MM-DD` format. |
| UDAPI1204 | **Invalid interval** — The `interval` value is not accepted. |

---

## Put-Call Ratio (PCR)

API for retrieving the Put-Call Ratio for an underlying asset on a given expiry and date. It accepts the instrument key, expiry, date, and bucket interval, and returns the PCR for the requested date along with spot price insights at each interval.

### Endpoint

**GET** `https://api.upstox.com/v2/market/pcr`

### Query Parameters

| Name | Required | Description |
| --- | --- | --- |
| instrument_key | Required | Underlying asset instrument key. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern) . |
| expiry | Required | Expiry of the option contract. Accepts either a date in `YYYY-MM-DD` format or a relative expiry keyword. **Weekly:**`current_week` , `next_week` , `far_week` . **Monthly:**`current_month` , `next_month` , `far_month` . Using keywords keeps strategies always up-to-date and rolls over automatically after each expiry. |
| date | Required | Date for which PCR data is required, in `YYYY-MM-DD` format. |
| bucket_interval | Required | Bucket interval in minutes for intraday PCR insights. |

The `bucket_interval` parameter controls the granularity of the intraday `insights` array — it defines the gap in minutes between consecutive data points. For example, `bucket_interval=60` returns one data point per hour starting from market open (09:15, 10:15, 11:15, ..., 15:15).

#### Response body

```json
{
    "status": "success",
    "data": {
        "instrument_key": "NSE_INDEX|Nifty 50",
        "expiry_date": "19-05-2026",
        "pcr": 0.6162626197672175,
        "spot_closing_price": 24044.35,
        "insights": [
            {
                "pcr": 0.6440030253572708,
                "spot_price": 23955.0,
                "time": "09:15"
            },
            {
                "pcr": 0.6188192668371697,
                "spot_price": 23829.65,
                "time": "10:15"
            },
            {
                "pcr": 0.6011564491753729,
                "spot_price": 23800.0,
                "time": "11:15"
            },
            {
                "pcr": 0.6114701925916205,
                "spot_price": 23905.75,
                "time": "12:15"
            },
            {
                "pcr": 0.6311270125223614,
                "spot_price": 23950.65,
                "time": "13:15"
            },
            {
                "pcr": 0.6493306043015804,
                "spot_price": 24028.5,
                "time": "14:15"
            },
            {
                "pcr": 0.652457692695892,
                "spot_price": 23988.3,
                "time": "15:15"
            }
        ]
    }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` for successful operations. |
| data | object | PCR data object. |
| data.instrument_key | string | Underlying asset instrument key. |
| data.expiry_date | string | Expiry date of the option contract. |
| data.pcr | number | Put-Call Ratio for the requested date (total put OI / total call OI). |
| data.spot_closing_price | number | Closing spot price of the underlying asset. |
| data.insights | array | Intraday PCR data points at the requested bucket interval. |
| data.insights[].pcr | number | PCR at this interval. |
| data.insights[].spot_price | number | Spot price at this interval. |
| data.insights[].time | string | Time of the interval in `HH:mm` format. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI100011 | **Invalid instrument_key** — The provided `instrument_key` is invalid or not found. |
| UDAPI1202 | **Invalid expiry date format** — The `expiry` parameter must be in `YYYY-MM-DD` format. |
| UDAPI1203 | **Invalid date format** — The `date` parameter must be in `YYYY-MM-DD` format. |
| UDAPI1205 | **Invalid bucket_interval** — The `bucket_interval` value is not accepted. |

---

## Max Pain

API for retrieving the Max Pain strike price for an underlying asset on a given expiry and date. It accepts the instrument key, expiry, date, and bucket interval, and returns the max pain level for the requested date along with spot price insights at each interval.

### Endpoint

**GET** `https://api.upstox.com/v2/market/max-pain`

### Query Parameters

| Name | Required | Description |
| --- | --- | --- |
| instrument_key | Required | Underlying asset instrument key. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern) . |
| expiry | Required | Expiry of the option contract. Accepts either a date in `YYYY-MM-DD` format or a relative expiry keyword. **Weekly:**`current_week` , `next_week` , `far_week` . **Monthly:**`current_month` , `next_month` , `far_month` . Using keywords keeps strategies always up-to-date and rolls over automatically after each expiry. |
| date | Required | Date for which Max Pain data is required, in `YYYY-MM-DD` format. |
| bucket_interval | Required | Bucket interval in minutes for intraday insights. |

The `bucket_interval` parameter controls the granularity of the intraday `insights` array — it defines the gap in minutes between consecutive data points. For example, `bucket_interval=60` returns one data point per hour starting from market open (09:15, 10:15, 11:15, ..., 15:15).

#### Response body

```json
{
    "status": "success",
    "data": {
        "instrument_key": "NSE_INDEX|Nifty 50",
        "expiry_date": "19-05-2026",
        "max_pain": 24050.0,
        "spot_closing_price": 24044.35,
        "insights": [
            {
                "max_pain": 24250.0,
                "spot_price": 23955.0,
                "time": "09:15"
            },
            {
                "max_pain": 24100.0,
                "spot_price": 23829.65,
                "time": "10:15"
            },
            {
                "max_pain": 24000.0,
                "spot_price": 23800.0,
                "time": "11:15"
            },
            {
                "max_pain": 24000.0,
                "spot_price": 23905.75,
                "time": "12:15"
            },
            {
                "max_pain": 24000.0,
                "spot_price": 23950.65,
                "time": "13:15"
            },
            {
                "max_pain": 24050.0,
                "spot_price": 24028.5,
                "time": "14:15"
            },
            {
                "max_pain": 24050.0,
                "spot_price": 23988.3,
                "time": "15:15"
            }
        ]
    }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` for successful operations. |
| data | object | Max Pain data object. |
| data.instrument_key | string | Underlying asset instrument key. |
| data.expiry_date | string | Expiry date of the option contract. |
| data.max_pain | number | Max Pain strike level for the requested date. |
| data.spot_closing_price | number | Closing spot price of the underlying asset. |
| data.insights | array | Intraday Max Pain data points at the requested bucket interval. |
| data.insights[].max_pain | number | Max Pain strike at this interval. |
| data.insights[].spot_price | number | Spot price at this interval. |
| data.insights[].time | string | Time of the interval in `HH:mm` format. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI100011 | **Invalid instrument_key** — The provided `instrument_key` is invalid or not found. |
| UDAPI1202 | **Invalid expiry date format** — The `expiry` parameter must be in `YYYY-MM-DD` format. |
| UDAPI1203 | **Invalid date format** — The `date` parameter must be in `YYYY-MM-DD` format. |
| UDAPI1205 | **Invalid bucket_interval** — The `bucket_interval` value is not accepted. |

---

## FII Activity Data

API for retrieving Foreign Institutional Investor (FII) activity for a specified market segment and interval. It accepts the data type, interval, and an optional start date, and returns buy/sell amounts, contracts, open interest, and long/short position breakdowns across index futures, stock futures, and options segments. Data is available from **1st April 2026** onwards.

- **Daily ( `1D` )** — up to 30 trading days of data per request.
- **Monthly ( `1M` )** — up to 12 months of data per request (data collection started from 1st April 2026; the available range will grow as more months are recorded).

### Endpoint

**GET** `https://api.upstox.com/v2/market/fii`

### Query Parameters

| Name | Required | Description |
| --- | --- | --- |
| data_type | Required | Market segment. Accepts a single value or a comma-separated list. Full values listed below. |
| interval | Required | Data interval. Accepted values: `1D` (daily), `1M` (monthly). |
| from | Optional | Start date for the data range in `YYYY-MM-DD` format. |

**Accepted `data_type` values** — pass one or more segments to retrieve activity data for each independently:

- `NSE_FO|INDEX_FUTURES`
- `NSE_FO|STOCK_FUTURES`
- `NSE_FO|INDEX_OPTIONS`
- `NSE_FO|STOCK_OPTIONS`
- `NSE_EQ|CASH`

#### Response body

```json
{
    "status": "success",
    "data": {
        "NSE_FO|STOCK_FUTURES": [
            {
                "time_stamp": 1777487400000,
                "buy_amount": 23109.75,
                "sell_amount": 24642.52,
                "buy_contracts": 353981,
                "sell_contracts": 384079,
                "oi_contracts": 7245154,
                "oi_amount": 452650.0,
                "total_long_contracts": 4021980,
                "total_short_contracts": 3223174,
                "total_call_long_contracts": 0,
                "total_put_long_contracts": 0,
                "total_call_short_contracts": 0,
                "total_put_short_contracts": 0
            },
            {
                "time_stamp": 1777401000000,
                "buy_amount": 21593.35,
                "sell_amount": 21252.58,
                "buy_contracts": 327164,
                "sell_contracts": 318686,
                "oi_contracts": 7237618,
                "oi_amount": 456065.1,
                "total_long_contracts": 4033261,
                "total_short_contracts": 3204357,
                "total_call_long_contracts": 0,
                "total_put_long_contracts": 0,
                "total_call_short_contracts": 0,
                "total_put_short_contracts": 0
            }
        ],
        "NSE_FO|INDEX_OPTIONS": [
            {
                "time_stamp": 1777487400000,
                "buy_amount": 797967.36,
                "sell_amount": 794438.53,
                "buy_contracts": 5094129,
                "sell_contracts": 5072195,
                "oi_contracts": 1995796,
                "oi_amount": 313760.14,
                "total_long_contracts": 0,
                "total_short_contracts": 0,
                "total_call_long_contracts": 351772,
                "total_put_long_contracts": 715640,
                "total_call_short_contracts": 572110,
                "total_put_short_contracts": 356275
            },
            {
                "time_stamp": 1777401000000,
                "buy_amount": 579943.55,
                "sell_amount": 583822.61,
                "buy_contracts": 3659192,
                "sell_contracts": 3683793,
                "oi_contracts": 1776287,
                "oi_amount": 281482.39,
                "total_long_contracts": 0,
                "total_short_contracts": 0,
                "total_call_long_contracts": 293574,
                "total_put_long_contracts": 653116,
                "total_call_short_contracts": 509632,
                "total_put_short_contracts": 319965
            }
        ]
    }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` for successful operations. |
| data | object | Map of `data_type` key to an array of FII activity records. |
| data[key][].time_stamp | integer | Unix timestamp of the record in milliseconds. |
| data[key][].buy_amount | number | Total buy value in INR. |
| data[key][].sell_amount | number | Total sell value in INR. |
| data[key][].buy_contracts | integer | Number of contracts bought. |
| data[key][].sell_contracts | integer | Number of contracts sold. |
| data[key][].oi_contracts | integer | Open interest in number of contracts. |
| data[key][].oi_amount | number | Open interest value in INR. |
| data[key][].total_long_contracts | integer | Total long contracts held. |
| data[key][].total_short_contracts | integer | Total short contracts held. |
| data[key][].total_call_long_contracts | integer | Total long call option contracts. |
| data[key][].total_put_long_contracts | integer | Total long put option contracts. |
| data[key][].total_call_short_contracts | integer | Total short call option contracts. |
| data[key][].total_put_short_contracts | integer | Total short put option contracts. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1198 | **Invalid data_type** — The `data_type` value is not one of the accepted segments. |
| UDAPI1199 | **Invalid interval** — The `interval` value must be `1D` or `1M` . |
| UDAPI1200 | **Invalid from date format** — The `from` parameter must be in `YYYY-MM-DD` format. |

---

## DII Activity Data

API for retrieving Domestic Institutional Investor (DII) activity data. It accepts the data type, interval, and an optional start date, and returns buy/sell amounts for domestic institutional flows in the equities market. Data is available from **1st April 2026** onwards.

- **Daily ( `1D` )** — up to 30 trading days of data per request.
- **Monthly ( `1M` )** — up to 12 months of data per request (data collection started from 1st April 2026; the available range will grow as more months are recorded).

### Endpoint

**GET** `https://api.upstox.com/v2/market/dii`

### Query Parameters

| Name | Required | Description |
| --- | --- | --- |
| data_type | Required | Market segment. Only accepted value is `NSE_EQ` cash segment — see full value below. |
| interval | Required | Data interval. Accepted values: `1D` (daily), `1M` (monthly). |
| from | Optional | Start date for the data range in `YYYY-MM-DD` format. |

**Accepted `data_type` value** — DII data is currently available only for the NSE equity cash segment:

- `NSE_EQ|CASH`

#### Response body

```json
{
  "status": "success",
  "data": {
    "NSE_EQ|CASH": [
      {
        "time_stamp": 1746633600000,
        "buy_amount": 8523456789.0,
        "sell_amount": 7234567890.5,
        "buy_contracts": 0,
        "sell_contracts": 0,
        "oi_contracts": 0,
        "oi_amount": 0.0,
        "total_long_contracts": 0,
        "total_short_contracts": 0,
        "total_call_long_contracts": 0,
        "total_put_long_contracts": 0,
        "total_call_short_contracts": 0,
        "total_put_short_contracts": 0
      }
    ]
  }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` for successful operations. |
| data | object | Map of `data_type` key to an array of DII activity records. |
| data[key][].time_stamp | integer | Unix timestamp of the record in milliseconds. |
| data[key][].buy_amount | number | Total buy value in INR. |
| data[key][].sell_amount | number | Total sell value in INR. |
| data[key][].buy_contracts | integer | Number of contracts bought. |
| data[key][].sell_contracts | integer | Number of contracts sold. |
| data[key][].oi_contracts | integer | Open interest in number of contracts. |
| data[key][].oi_amount | number | Open interest value in INR. |
| data[key][].total_long_contracts | integer | Total long contracts held. |
| data[key][].total_short_contracts | integer | Total short contracts held. |
| data[key][].total_call_long_contracts | integer | Total long call option contracts. |
| data[key][].total_put_long_contracts | integer | Total long put option contracts. |
| data[key][].total_call_short_contracts | integer | Total short call option contracts. |
| data[key][].total_put_short_contracts | integer | Total short put option contracts. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1198 | **Invalid data_type** — The `data_type` parameter is invalid. DII supports only the NSE equity cash segment. |
| UDAPI1199 | **Invalid interval** — The `interval` value must be `1D` or `1M` . |
| UDAPI1200 | **Invalid from date format** — The `from` parameter must be in `YYYY-MM-DD` format. |
