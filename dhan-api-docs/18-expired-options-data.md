<!-- Expired Options Data - DhanHQ Ver 2.0 / API Document -->
# Source: https://dhanhq.co/docs/v2/expired-options-data/

# Expired Options Data

This API gives you expired options contract data. We have pre processed data for you to get it on rolling basis i.e. you can fetch last 5 years of strike wise data based on ATM and upto 10 strikes above and below. In addition to that, the data values are open, high, low, close, implied volatility, volume, open interest and spot information as well.

|  |  |  |
| --- | --- | --- |
| POST | /charts/rollingoption | Get Continuous Expired Options Contract data |

Note

“ATM” refers to At The Money. For index options nearing expiry, strikes will be available up to ATM +10 and ATM −10. For all other contracts, strikes will be available up to ATM +3 and ATM −3.

## Historical Rolling Data

Fetch expired options data on a rolling basis, along with the Open Interest, Implied Volatility, OHLC, Volume as well as information about the spot. You can fetch for upto 30 days of data in a single API call. Expired options data is stored on a minute level, based on strike price relative to spot (example ATM, ATM+1, ATM-1, etc.).

You can fetch data upto last 5 years. We have added both Index Options and Stock Options data on this.

```
curl --request POST \
--url https://api.dhan.co/v2/charts/rollingoption \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'access-token: ' \
--data '{}'
```

**Request Structure**

```
    {
    "exchangeSegment": "NSE_FNO",
    "interval": "1",
    "securityId": 13,
    "instrument": "OPTIDX",
    "expiryFlag": "MONTH",
    "expiryCode": 1,
    "strike": "ATM",
    "drvOptionType": "CALL",
    "requiredData": [
        "open",
        "high",
        "low",
        "close",
        "volume"
    ],
    "fromDate": "2021-08-01",
    "toDate": "2021-09-01"
    }
```

**Parameters**

| Field | Field Type | Description |
| --- | --- | --- |
| exchangeSegment *required* | enum string | Exchange & segment for which data is to be fetched - [here](../annexure/#exchange-segment) |
| interval   *required* | enum integer | Minute intervals in timeframe   `1`, `5`, `15`, `25`, `60` |
| securityId *required* | string | Underlying exchange standard ID for each scrip. Refer [here](../instruments/) |
| instrument  *required* | enum string | Instrument type of the scrip. Refer [here](/docs/v2/annexure/#instrument) |
| expiryCode  *required* | enum integer | Expiry of the instruments. Refer [here](../instruments/) |
| expiryFlag  *required* | enum string | Expiry intervale of the instrument  `WEEK` or `MONTH` |
| strike  *required* | enum string | `ATM` for At the Money  Upto `ATM+10 / ATM-10` for Index Options near expiry  Upto `ATM+3 / ATM-3` for all other contracts |
| drvOptionType  *required* | enum string | `CALL` or `PUT` |
| requiredData  *required* | array [] | Array of all required parameters  `open` `high` `low` `close` `iv` `volume` `strike` `oi` `spot` |
| fromDate  *required* | string | Start date of the desired range |
| toDate  *required* | string | End date of the desired range (non-inclusive) |

**Response Structure**

```
{
    "data": {
        "ce": {
        "iv": [],
        "oi": [],
        "strike": [],
        "spot": [],
        "open": [
            354,
            360.3
        ],
        "high": [],
        "low": [],
        "close": [],
        "volume": [],
        "timestamp": [
            1756698300,
            1756699200
        ]
        },
        "pe": null
    }
}
```

**Parameters**

| Field | Field Type | Description |
| --- | --- | --- |
| open | float | Open price of the timeframe |
| high | float | High price in the timeframe |
| low | float | Low price in the timeframe |
| close | float | Close price of the timeframe |
| volume | int | Volume traded in the timeframe |
| timestamp | int | Epoch timestamp |

Note: For description of enum values, refer [Annexure](https://dhanhq.co/docs/v2/annexure)
