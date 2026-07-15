> Source: https://docs.arrow.trade/rest-api/utility/

# Utility APIs

Alongside the trading APIs used to place and manage orders on the exchange, Arrow exposes **utility** endpoints for calendars, index metadata, option chains, and options Greeks. These use the same authentication model as the rest of the Developer API.

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

* * *

## Endpoint overview

Method | Endpoint | Description
---|---|---
`GET` | `/info/holidays` | Trading holidays and special sessions for the current year
`GET` | `/info/index-list` | Indexes listed on the exchange (name and token)
`GET` | `/info/option-chain-symbols/all` | All Option-underlying symbols with available expiries
`POST` | `/info/option-chain` | Full option chain for an index token and expiry

* * *

## Holidays

Returns exchange holidays (`DD-MM-YYYY` → holiday name) and optional **special trading days** with session windows.

**Sample request**

```bash
curl --location 'https://edge.arrow.trade/info/holidays' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

**Sample response**

```json
{
    "data": {
        "holidays": {
            "01-05-2026": "Maharashtra Day",
            "02-10-2026": "Mahatma Gandhi Jayanti",
            "03-03-2026": "Holi",
            "03-04-2026": "Good Friday",
            "10-11-2026": "Diwali-Balipratipada",
            "14-04-2026": "Dr. Baba Saheb Ambedkar Jayanti",
            "14-09-2026": "Ganesh Chaturthi",
            "15-01-2026": "Municipal Corporation Election in Maharashtra",
            "20-10-2026": "Dussehra",
            "24-11-2026": "Prakash Gurpurb Sri Guru Nanak Dev",
            "25-12-2026": "Christmas",
            "26-01-2026": "Republic Day",
            "26-03-2026": "Shri Ram Navami",
            "26-06-2026": "Muharram",
            "28-05-2026": "Bakri Id",
            "31-03-2026": "Shri Mahavir Jayanti"
        },
        "specialTradingDays": {
            "01-02-2026": [
                [
                    "09:00",
                    400
                ]
            ]
        }
    },
    "status": "success"
}
```

* * *

## Index list

Returns display names and **index tokens** (used with `/info/option-chain` and elsewhere).

**Sample request**

```bash
curl --location 'https://edge.arrow.trade/info/index-list' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

**Sample response**

```json
{
    "data":
        {
            "name": "Nifty 50",
            "token": 26000
        },
        {
            "name": "Nifty IT",
            "token": 26008
        },
        {
            "name": "Nifty 100",
            "token": 26012
        },
        {
            "name": "Nifty Midcap 50",
            "token": 26014
        },
        .....
    ],
    "status": "success"
}
```

* * *

## All Option chain symbols

Returns a map of **underlying symbol** (for example `NIFTY`, `BANKNIFTY`) to a list of **expiry strings** available for that underlying.

**Sample request**

```bash
curl --location 'https://edge.arrow.trade/info/option-chain-symbols/all' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

**Sample response**

```json
{
    "data": {
        "equity": {
          ...
            "NSE:POLICYBZR-EQ": [
                "26-MAY-2026",
                "30-JUN-2026",
                "28-JUL-2026"
            ],
            "NSE:POLYCAB-EQ": [
                "26-MAY-2026",
                "30-JUN-2026",
                "28-JUL-2026"
            ],
            "NSE:POWERGRID-EQ": [
                "26-MAY-2026",
                "30-JUN-2026",
                "28-JUL-2026"
            ],
          ...
        },
        "indices": {

            "INDEX:BANKNIFTY": [
                "26-MAY-2026",
                "30-JUN-2026",
                "28-JUL-2026",
                "29-SEP-2026",
                "29-DEC-2026",
                "30-MAR-2027"
            ],

            "INDEX:NIFTY": [
                "12-MAY-2026",
                "19-MAY-2026",
                "26-MAY-2026",
                "02-JUN-2026",
                "09-JUN-2026",
                "30-JUN-2026",
                "28-JUL-2026",
                "29-SEP-2026",
                "29-DEC-2026",
                "30-MAR-2027",
                "29-JUN-2027",
                "28-DEC-2027",
                "27-JUN-2028",
                "26-DEC-2028",
                "26-JUN-2029",
                "24-DEC-2029",
                "25-JUN-2030",
                "31-DEC-2030"
            ],

            "INDEX:SENSEX": [
                "07-MAY-2026",
                "14-MAY-2026",
                "21-MAY-2026",
                "27-MAY-2026",
                "04-JUN-2026",
                "11-JUN-2026",
                "18-JUN-2026",
                "25-JUN-2026",
                "30-JUL-2026",
                "24-SEP-2026",
                "31-DEC-2026",
                "25-MAR-2027",
                "24-JUN-2027",
                "30-DEC-2027",
                "29-JUN-2028",
                "28-DEC-2028",
                "28-JUN-2029",
                "27-DEC-2029",
                "27-JUN-2030",
                "26-DEC-2030"
            ],

        }
    },
    "status": "success"
}
```

* * *

## Option chain

Returns option instruments (calls and puts) for a given **index token** , **exchange** segment, **expiry** , and strike **count**.

**Request body (JSON)**

Field | Type | Description
---|---|---
`token` | string | Index token from `/info/index-list`
`exchange` | string | Segment, for example `INDEX`
`count` | string | Number of strikes around ATM to return
`expiry` | string | Expiry in `DD-MMM-YYYY` form (for example `03-APR-2024`)

**Sample request**

```bash
curl --location 'https://edge.arrow.trade/info/option-chain' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
    "token": "26009",
    "exchange": "INDEX",
    "count": "10",
    "expiry": "03-APR-2024"
}'
```

**Sample response**

```json
{
  "data": [
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24C45100",
      "token": "66652",
      "optionType": "CE",
      "strikePrice": "45100.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24C45200",
      "token": "66654",
      "optionType": "CE",
      "strikePrice": "45200.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24C45300",
      "token": "66656",
      "optionType": "CE",
      "strikePrice": "45300.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24C45400",
      "token": "66658",
      "optionType": "CE",
      "strikePrice": "45400.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24C45500",
      "token": "66660",
      "optionType": "CE",
      "strikePrice": "45500.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24C45000",
      "token": "52219",
      "optionType": "CE",
      "strikePrice": "45000.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24C44900",
      "token": "66650",
      "optionType": "CE",
      "strikePrice": "44900.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24C44800",
      "token": "66648",
      "optionType": "CE",
      "strikePrice": "44800.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24C44700",
      "token": "66644",
      "optionType": "CE",
      "strikePrice": "44700.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24C44600",
      "token": "66642",
      "optionType": "CE",
      "strikePrice": "44600.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24P45100",
      "token": "66653",
      "optionType": "PE",
      "strikePrice": "45100.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24P45200",
      "token": "66655",
      "optionType": "PE",
      "strikePrice": "45200.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24P45300",
      "token": "66657",
      "optionType": "PE",
      "strikePrice": "45300.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24P45400",
      "token": "66659",
      "optionType": "PE",
      "strikePrice": "45400.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24P45500",
      "token": "66661",
      "optionType": "PE",
      "strikePrice": "45500.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24P45000",
      "token": "52221",
      "optionType": "PE",
      "strikePrice": "45000.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24P44900",
      "token": "66651",
      "optionType": "PE",
      "strikePrice": "44900.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24P44800",
      "token": "66649",
      "optionType": "PE",
      "strikePrice": "44800.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24P44700",
      "token": "66647",
      "optionType": "PE",
      "strikePrice": "44700.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    },
    {
      "exchange": "NFO",
      "symbol": "BANKNIFTY28MAR24P44600",
      "token": "66643",
      "optionType": "PE",
      "strikePrice": "44600.00",
      "pricePrecision": "2",
      "tickSize": "0.05",
      "lotSize": "15"
    }
  ],
  "status": "success"
}
```

Each leg includes `exchange`, `symbol`, `token`, `optionType` (`CE` / `PE`), `strikePrice`, `pricePrecision`, `tickSize`, and `lotSize`.

* * *

## Error handling

Failures follow the same patterns as other REST APIs: see [Error codes](../error-codes/) and [Response structure](../response-structure/).
