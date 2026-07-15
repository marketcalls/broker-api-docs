> Source: https://docs.arrow.trade/rest-api/historical-candle-data/

# Historical Data API

The Historical Data API provides access to comprehensive historical market data, enabling backtesting, technical analysis, and chart visualization. The API supports various timeframes from 1-minute to monthly intervals and includes optional Open Interest data for derivatives.

## Endpoint Reference

### Get Historical Candle Data

Retrieve historical OHLCV data for a specific instrument across configurable time intervals.

Endpoint Details

**Method:** `GET`
**URL:** `/candle/:exchange/:token/:interval`
**Header:** Required (`appID` \+ `token`)

#### URL Parameters

Parameter | Type | Required | Description
---|---|---|---
`exchange` | string | ✓ | Exchange identifier (nse, nfo, bse, etc.)
`token` | string | ✓ | Unique instrument token (e.g., 3045 for SBIN)
`interval` | string | ✓ | Candle interval (see supported intervals below)

#### Supported Intervals

Interval | Description
---|---
`min` | 1 minute
`3min` | 3 minutes
`5min` | 5 minutes
`10min` | 10 minutes
`15min` | 15 minutes
`30min` | 30 minutes
`hour` | 1 hour
`2hours` | 2 hours
`3hours` | 3 hours
`4hours` | 4 hours
`day` | 1 day
`week` | 1 week
`month` | 1 month

#### Query Parameters

Parameter | Type | Required | Description
---|---|---|---
`from` | string | ✓ | Start date/time in `yyyy-MM-ddTHH:mm:ss` format
`to` | string | ✓ | End date/time in `yyyy-MM-ddTHH:mm:ss` format
`oi` | integer | ✗ | Include Open Interest data (1=enabled, NFO only)

#### Request Headers

Header | Type | Required | Description
---|---|---|---
`appID` | string | ✓ | Your application identifier
`token` | string | ✓ | User authentication token

* * *

### NSE Historical Data

Retrieve historical equity data from the National Stock Exchange.

#### Request Example

cURL

```bash
curl --location 'https://historical-api.arrow.trade/candle/nse/3045/day?from=2023-05-01T00:00:00&to=2023-06-29T20:00:00' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

#### Success Response

```json
[
    [
        "2023-05-02T00:00:00+0530",
        58000,
        58085,
        57315,
        57530,
        13667511
    ],
    [
        "2023-05-03T00:00:00+0530",
        57065,
        57500,
        56900,
        57050,
        9699527
    ],
    [
        "2023-05-04T00:00:00+0530",
        57020,
        58080,
        56850,
        58000,
        12533761
    ],
    [
        "2023-05-05T00:00:00+0530",
        58020,
        58825,
        57504,
        57650,
        18163461
    ],
    [
        "2023-05-08T00:00:00+0530",
        57765,
        58760,
        57735,
        58360,
        12990869
    ],
    [
        "2023-05-09T00:00:00+0530",
        58500,
        58645,
        57210,
        57350,
        18959065
    ],
    [
        "2023-05-10T00:00:00+0530",
        57500,
        57500,
        56325,
        57220,
        18561315
    ]
]
```

#### Response Format (NSE)

Each candle is represented as an array with the following structure:

Index | Field | Type | Description
---|---|---|---
0 | Timestamp | string | Date/time in ISO 8601 format with timezone
1 | Open | integer | Opening price × 100
2 | High | integer | Highest price × 100
3 | Low | integer | Lowest price × 100
4 | Close | integer | Closing price × 100
5 | Volume | integer | Total traded volume

Price Scaling for NSE

**IMPORTANT:** Open, High, Low, and Close values are multiplied by 100. To get actual prices, divide by 100.

**Example:**

```json
[
    "2023-05-02T00:00:00+0530",
    58000,
    58085,
    57315,
    57530,
    13667511
]
```

```
Actual Values:
    - Open: ₹580.00 (58000 ÷ 100)
    - High: ₹580.85 (58085 ÷ 100)
    - Low: ₹573.15 (57315 ÷ 100)
    - Close: ₹575.30 (57530 ÷ 100)
    - Volume: 13,667,511 shares
```

* * *

### NFO Historical Data

Retrieve historical derivatives data from the National Stock Exchange Futures & Options segment, with optional Open Interest information.

#### Request Example

```bash
curl --location 'https://historical-api.arrow.trade/candle/nfo/41927/day?from=2024-03-05T00:00:00&to=2024-03-08T00:00:00&oi=1' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

#### Success Response (with Open Interest)

```json
[
    [
        "2024-03-05T00:00:00+0530",
        26000,
        41505,
        21400,
        33330,
        2950530,
        487485
    ],
    [
        "2024-03-06T00:00:00+0530",
        28930,
        60000,
        25520,
        40705,
        13948425,
        1778205
    ],
    [
        "2024-03-07T00:00:00+0530",
        42400,
        44800,
        28810,
        32915,
        26726955,
        3863355
    ]
]
```

#### Response Format (NFO)

Each candle is represented as an array with the following structure:

Index | Field | Type | Description
---|---|---|---
0 | Timestamp | string | Date/time in ISO 8601 format with timezone
1 | Open | integer | Opening price × 100
2 | High | integer | Highest price × 100
3 | Low | integer | Lowest price × 100
4 | Close | integer | Closing price × 100
5 | Volume | integer | Total traded volume
6 | Open Interest | integer | Open Interest (only when `oi=1`)

Price Scaling and Open Interest for NFO

**IMPORTANT:** Open, High, Low, and Close values are multiplied by 100. To get actual prices, divide by 100.

Open Interest data is only included when the `oi=1` query parameter is added to the request.

**Example:**

```json
[
    "2024-03-05T00:00:00+0530",
    26000,
    41505,
    21400,
    33330,
    2950530,
    487485
]
```

```
Actual Values:
    - Open: ₹260.00 (26000 ÷ 100)
    - High: ₹415.05 (41505 ÷ 100)
    - Low: ₹214.00 (21400 ÷ 100)
    - Close: ₹333.30 (33330 ÷ 100)
    - Volume: 2,950,530 contracts
    - Open Interest: 487,485 contracts
```

## Error Handling

The API follows standard HTTP status codes and returns structured error responses:

```json
{
  "status": "error",
  "message": "Invalid date range",
  "code": "INVALID_DATE_RANGE"
}
```

Common Issues

  * **400 Bad Request:** Invalid parameters (exchange, token, interval, or date format)
  * **401 Unauthorized:** Invalid or expired token
  * **403 Forbidden:** Insufficient permissions
  * **404 Not Found:** Invalid instrument token or exchange
  * **422 Unprocessable Entity:** Date range exceeds maximum allowed period
  * **429 Too Many Requests:** Rate limit exceeded
  * **500 Internal Server Error:** Server-side processing error

## Integration Notes

Best Practices

  * Always divide price values (Open, High, Low, Close) by 100 to get actual prices
  * Use appropriate intervals based on your analysis needs (smaller intervals generate more data)
  * Request reasonable date ranges to avoid timeout or size limit issues
  * Cache historical data locally to minimize API calls for backtesting
  * Use the `oi=1` parameter only when Open Interest data is needed (NFO only)
  * Implement proper error handling for missing data or date range issues
  * Validate date formats match `yyyy-MM-ddTHH:mm:ss` specification

Data Availability

Historical data availability varies by instrument and exchange. Some instruments may have limited historical data, especially for newly listed securities or derivatives contracts.

Date Range Limits

There may be maximum date range limits depending on the interval selected. For very large datasets, consider breaking requests into smaller time periods.
