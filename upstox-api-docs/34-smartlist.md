# Smartlist

Curated, real-time ranked lists of F&O contracts and MTF-eligible stocks. Launched 29 May 2026.

---

## Futures Smartlist

API for retrieving a ranked list of futures contracts filtered by asset type and category. Each entry includes the instrument key, live price data, and the category-specific metric used for ranking.

A smartlist is a curated, real-time ranked list of instruments grouped by a specific market signal — such as highest traded value, biggest open interest change, or largest premium/discount. Instead of scanning the entire futures market, you get a focused subset of contracts that are most relevant to a given category at that moment.

### Endpoint

**GET** `https://api.upstox.com/v2/market/smartlist/futures`

### Query Parameters

| Name | Required | Description |
| --- | --- | --- |
| asset_type | Required | Asset type. Accepted values: `INDEX` , `STOCK` , `COMMODITY` . |
| category | Required | Ranking category. Accepted values depend on `asset_type` — see the table below. |
| page_number | Optional | Page number, 1-indexed. Defaults to 1. |
| page_size | Optional | Number of records per page. Maximum 50. |

**Accepted category values by asset_type:**

| asset_type | Accepted category values |
| --- | --- |
| INDEX, STOCK | `TOP_TRADED` , `MOST_ACTIVE` , `OI_GAINERS` , `OI_LOSERS` , `PRICE_GAINERS` , `PRICE_LOSERS` , `PREMIUM` , `DISCOUNT` |
| COMMODITY | `TOP_TRADED` , `MOST_ACTIVE` , `OI_GAINERS` , `OI_LOSERS` |

The metric_key field in the response indicates which metric was used for ranking:

| category | metric_key |
| --- | --- |
| TOP_TRADED | total_traded_value |
| MOST_ACTIVE | volume_traded_today |
| OI_GAINERS, OI_LOSERS | open_interest |
| PRICE_GAINERS, PRICE_LOSERS | price |
| PREMIUM | premium |
| DISCOUNT | discount |

#### Response body

```json
{
    "status": "success",
    "data": {
        "asset_type": "INDEX",
        "category": "TOP_TRADED",
        "time_stamp": 1780045636752,
        "metric_key": "total_traded_value",
        "smartlist": [
            {
                "instrument_key": "NSE_FO|62329",
                "price": {
                    "current": 23867.0,
                    "close_price": 23996.7,
                    "change_abs": -129.70,
                    "change_pct": -0.54
                },
                "metric": {
                    "current": 132094775540,
                    "previous": 69295823909,
                    "change_abs": 62798951631.00,
                    "change_pct": 90.62
                }
            },
            {
                "instrument_key": "NSE_FO|62326",
                "price": {
                    "current": 54970.0,
                    "close_price": 55207.0,
                    "change_abs": -237.00,
                    "change_pct": -0.43
                },
                "metric": {
                    "current": 45591018600,
                    "previous": 43236361746,
                    "change_abs": 2354656854.00,
                    "change_pct": 5.45
                }
            },
            {
                "instrument_key": "NSE_FO|61093",
                "price": {
                    "current": 23977.8,
                    "close_price": 24089.6,
                    "change_abs": -111.80,
                    "change_pct": -0.46
                },
                "metric": {
                    "current": 5752633887,
                    "previous": 4917306790.5,
                    "change_abs": 835327096.50,
                    "change_pct": 16.99
                }
            }
        ],
        "page_number": 1,
        "page_size": 3,
        "total_pages": 9
    }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` for successful operations. |
| data | object | Response data object. |
| data.asset_type | string | Asset type from the request. |
| data.category | string | Category from the request. |
| data.time_stamp | integer | Unix timestamp in milliseconds when the data was generated. |
| data.metric_key | string | The metric used for ranking in this response. |
| data.smartlist | array | Ranked list of futures instruments. |
| data.smartlist[].instrument_key | string | Unique instrument identifier. See [Instrument keys](https://upstox.com/developer/api-documentation/instruments) . |
| data.smartlist[].price.current | number | Last traded price (LTP). |
| data.smartlist[].price.close_price | number | Previous close price. |
| data.smartlist[].price.change_abs | number | Absolute price change ( `current - close_price` ). |
| data.smartlist[].price.change_pct | number | Percentage price change. |
| data.smartlist[].metric.current | number | Current value of the ranking metric. |
| data.smartlist[].metric.previous | number | Previous value of the ranking metric. |
| data.smartlist[].metric.change_abs | number | Absolute change in the metric. |
| data.smartlist[].metric.change_pct | number | Percentage change in the metric. |
| data.page_number | integer | Current page number. |
| data.page_size | integer | Number of records in the current page. |
| data.total_pages | integer | Total number of pages available. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1212 | **Invalid asset_type** — The `asset_type` value must be `INDEX` , `STOCK` , or `COMMODITY` . |
| UDAPI1213 | **Invalid category for the given asset_type** — The `category` value is not supported for the provided `asset_type` . |
| UDAPI1214 | **Invalid page_size** — The `page_size` value exceeds the maximum allowed value of 50. |

---

## Options Smartlist

API for retrieving a ranked list of options contracts filtered by asset type and category. Each entry includes the instrument key, live price data, and the category-specific metric used for ranking.

A smartlist is a curated, real-time ranked list of instruments grouped by a specific market signal — such as highest traded value, biggest open interest change, or strongest implied volatility move. Instead of scanning the entire options market, you get a focused subset of contracts that are most relevant to a given category at that moment.

For more information on how the options smartlist feature works, see the [Upstox community post](https://community.upstox.com/t/seamless-options-trading-instantly-access-options-smartlist-via-search-on-upstox/8236) .

### Endpoint

**GET** `https://api.upstox.com/v2/market/smartlist/options`

### Query Parameters

| Name | Required | Description |
| --- | --- | --- |
| asset_type | Required | Asset type. Accepted values: `INDEX` , `STOCK` , `COMMODITY` . |
| category | Required | Ranking category. Accepted values depend on `asset_type` — see the table below. |
| page_number | Optional | Page number, 1-indexed. Defaults to 1. |
| page_size | Optional | Number of records per page. Maximum 50. |

**Accepted category values by asset_type:**

| asset_type | Accepted category values |
| --- | --- |
| INDEX, STOCK | `TOP_TRADED` , `MOST_ACTIVE` , `OI_GAINERS` , `OI_LOSERS` , `PRICE_GAINERS` , `PRICE_LOSERS` , `IV_GAINERS` , `IV_LOSERS` , `UNDER_5000` , `UNDER_10000` |
| COMMODITY | `TOP_TRADED` , `MOST_ACTIVE` , `OI_GAINERS` , `OI_LOSERS` |

The metric_key field in the response indicates which metric was used for ranking:

| category | metric_key |
| --- | --- |
| TOP_TRADED | total_traded_value |
| MOST_ACTIVE | volume_traded_today |
| OI_GAINERS, OI_LOSERS | open_interest |
| PRICE_GAINERS, PRICE_LOSERS | price |
| IV_GAINERS, IV_LOSERS | implied_volatility |
| UNDER_5000, UNDER_10000 | buy_margin |

#### Response body

```json
{
  "status": "success",
  "data": {
    "asset_type": "INDEX",
    "category": "TOP_TRADED",
    "time_stamp": 1780041069287,
    "metric_key": "total_traded_value",
    "smartlist": [
      {
        "instrument_key": "NSE_FO|57047",
        "price": {
          "current": 177.4,
          "close_price": 125.5,
          "change_abs": 51.9,
          "change_pct": 41.35
        },
        "metric": {
          "current": 53889598074,
          "previous": 4351865287721.25,
          "change_abs": -4297975689647.25,
          "change_pct": -98.76
        }
      },
      {
        "instrument_key": "NSE_FO|57051",
        "price": {
          "current": 241.65,
          "close_price": 172.35,
          "change_abs": 69.3,
          "change_pct": 40.21
        },
        "metric": {
          "current": 36473443958.25,
          "previous": 2391714654137.25,
          "change_abs": -2355241210179,
          "change_pct": -98.48
        }
      },
      {
        "instrument_key": "NSE_FO|57049",
        "price": {
          "current": 208.15,
          "close_price": 148,
          "change_abs": 60.15,
          "change_pct": 40.64
        },
        "metric": {
          "current": 29500456316.5,
          "previous": 2171128196155.75,
          "change_abs": -2141627739839.25,
          "change_pct": -98.64
        }
      }
    ],
    "page_number": 1,
    "page_size": 3,
    "total_pages": 3354
  }
}
```

- For **UNDER_5000** and **UNDER_10000** categories, `metric.previous` , `metric.change_abs` , and `metric.change_pct` are returned as `null` — no previous metric value is available for these categories.

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` for successful operations. |
| data | object | Response data object. |
| data.asset_type | string | Asset type from the request. |
| data.category | string | Category from the request. |
| data.time_stamp | integer | Unix timestamp in milliseconds when the data was generated. |
| data.metric_key | string | The metric used for ranking in this response. |
| data.smartlist | array | Ranked list of options instruments. |
| data.smartlist[].instrument_key | string | Unique instrument identifier. See [Instrument keys](https://upstox.com/developer/api-documentation/instruments) . |
| data.smartlist[].price.current | number | Last traded price (LTP). |
| data.smartlist[].price.close_price | number | Previous close price. |
| data.smartlist[].price.change_abs | number | Absolute price change ( `current - close_price` ). |
| data.smartlist[].price.change_pct | number | Percentage price change. |
| data.smartlist[].metric.current | number | Current value of the ranking metric. |
| data.smartlist[].metric.previous | number \| null | Previous value of the ranking metric. `null` for `UNDER_5000` and `UNDER_10000` . |
| data.smartlist[].metric.change_abs | number \| null | Absolute change in the metric. `null` for `UNDER_5000` and `UNDER_10000` . |
| data.smartlist[].metric.change_pct | number \| null | Percentage change in the metric. `null` for `UNDER_5000` and `UNDER_10000` . |
| data.page_number | integer | Current page number. |
| data.page_size | integer | Number of records in the current page. |
| data.total_pages | integer | Total number of pages available. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1212 | **Invalid asset_type** — The `asset_type` value must be `INDEX` , `STOCK` , or `COMMODITY` . |
| UDAPI1213 | **Invalid category for the given asset_type** — The `category` value is not supported for the provided `asset_type` . |
| UDAPI1214 | **Invalid page_size** — The `page_size` value exceeds the maximum allowed value of 50. |

---

## MTF Smartlist

API for retrieving a ranked list of Margin Trade Funding (MTF) eligible stocks enriched with live LTP data. Each entry shows the actual market price, the effective MTF price after margin, and the total margin saved.

### Endpoint

**GET** `https://api.upstox.com/v2/market/smartlist/mtf`

### Query Parameters

| Name | Required | Description |
| --- | --- | --- |
| page_number | Optional | Page number, 1-indexed. Defaults to 1. |
| page_size | Optional | Number of records per page. Maximum 50. |

#### Response body

```json
{
    "status": "success",
    "data": {
        "asset_type": "STOCK",
        "category": "MTF",
        "time_stamp": 1780045827238,
        "metric_key": "margin_saved",
        "smartlist": [
            {
                "instrument_key": "NSE_EQ|INE040A01034",
                "price": {
                    "actual_price": 755.1,
                    "mtf_price": 555.00,
                    "margin_saved": 200.10,
                    "close_price": 758.65
                },
                "mtf_percent": 26.5
            },
            {
                "instrument_key": "NSE_EQ|INE463A01038",
                "price": {
                    "actual_price": 505.8,
                    "mtf_price": 363.67,
                    "margin_saved": 142.13,
                    "close_price": 526.95
                },
                "mtf_percent": 28.1
            },
            {
                "instrument_key": "NSE_EQ|INE750A01020",
                "price": {
                    "actual_price": 95.3,
                    "mtf_price": 61.94,
                    "margin_saved": 33.36,
                    "close_price": 97.55
                },
                "mtf_percent": 35.0
            }
        ],
        "page_number": 1,
        "page_size": 3,
        "total_pages": 469
    }
}
```

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Typically `success` for successful operations. |
| data | object | Response data object. |
| data.asset_type | string | Always `STOCK` for MTF. |
| data.category | string | Always `MTF` . |
| data.time_stamp | integer | Unix timestamp in milliseconds when the data was generated. |
| data.metric_key | string | Always `margin_saved` for MTF. |
| data.smartlist | array | Ranked list of MTF-eligible stocks. |
| data.smartlist[].instrument_key | string | Unique instrument identifier. See [Instrument keys](https://upstox.com/developer/api-documentation/instruments) . |
| data.smartlist[].price.actual_price | number | Current market price (LTP). |
| data.smartlist[].price.mtf_price | number | Effective price after applying MTF margin ( `actual_price - margin_saved` ). |
| data.smartlist[].price.margin_saved | number | Margin amount saved via MTF ( `mtf_percent` of `actual_price` ). |
| data.smartlist[].price.close_price | number | Previous close price. |
| data.smartlist[].mtf_percent | number | MTF margin percentage for this stock. |
| data.page_number | integer | Current page number. |
| data.page_size | integer | Number of records in the current page. |
| data.total_pages | integer | Total number of pages available. |

### Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1214 | **Invalid page_size** — The `page_size` value exceeds the maximum allowed value of 50. |
