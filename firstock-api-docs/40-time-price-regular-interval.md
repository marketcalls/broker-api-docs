# Time Price Regular Interval

> Source: https://firstock.in/api/docs/time-price-regular-interval/

> This document provides an overview of how to use the Time Price Series (Regular Interval) API within the Firstock trading platform.

## Overview

The **Time Price Series (Regular Interval)** API is useful for traders and developers who need **intraday candlestick data** for charting or historical analysis over short intervals (e.g., 1 minute, 2 minutes, etc.). This differs from day-by-day (EOD) data and is particularly helpful for building real-time or intraday charts, backtesting short-term strategies, and analyzing market moves in finer detail.

**Key benefits:**

1. **Intraday Candles**: Access smaller intervals (e.g., *1mi*, *2mi*, *5mi*) for deeper granularity.
2. **Customizable Date Range**: Provide start and end times in *DD-MM-YYYY HH:MM:SS* format.
3. **Seamless Integration**: Combine with other data (like quotes or order book) for robust trading applications.

## Endpoint & Method

`POST` `/timePriceSeries`

**URL**:

```
https://api.firstock.in/V1/timePriceSeries
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body for the Time Price Series (Regular Interval) request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| exchange | string | Yes | The exchange code ("NSE", "BSE", "NFO", etc.) | "NSE" |
| tradingSymbol | string | Yes | The symbol or instrument for which to retrieve time-series data. | NIFTY" |
| startTime | string | Yes | Start date-time in DD-MM-YYYY HH:MM:SS format (24-hour clock). | "09:15:00 23-04-2025" |
| endTime | string | Yes | End date-time in the same format. | "15:29:00 23-04-2025" |
| interval | string | Yes | The candle interval, e.g., "1mi", "2mi", "5mi", etc. | 1mi", "2mi" |

**Request**

```json
{
  "userId": "AB1234",
  "jKey": "6db79eaa7edce0432b012fdfa5fb3d03f40125916344ed9ce87fe701469bc59e",
  "exchange": "NSE",
  "interval": "1mi",
  "tradingSymbol": "NIFTY",
  "startTime": "09:15:00 23-04-2025",
  "endTime": "15:29:00 23-04-2025"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/timePriceSeries' \
--header 'Content-Type: application/json' \
--data '{
  "userId": "{{userId}}",
  "jKey": "6db79eaa7edce0432b012fdfa5fb3d03f40125916344ed9ce87fe701469bc59e",
  "exchange": "NSE",
  "interval": "1mi",
  "tradingSymbol": "NIFTY",
  "startTime": "09:15:00 23-04-2025",
  "endTime": "15:29:00 23-04-2025"
}'
```

**Python**

```python
from firstock import firstock
timePriceSeries = firstock.timePriceSeries(
    userId="{{userId}}",
    exchange="NSE",
    tradingSymbol="NIFTY",
    startTime="09:15:00 23-04-2025",
    endTime="15:29:00 23-04-2025",
    interval="1mi"
)
print(timePriceSeries)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.timePriceSeries(
  {
    userId: "{{userId}}",
    exchange: "NSE",
    tradingSymbol: "NIFTY",
    startTime: "09:15:00 23-04-2025",
    endTime: "15:29:00 23-04-2025",
    interval: "1mi",
  },
  (err, result) => {
    console.log("timePriceSeries Error, ", err);
    console.log("timePriceSeries Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

timePriceSeriesRegularIntervalRequest := Firstock.TimePriceSeriesIntervalRequest{
		UserId:        "{{userId}}",
		Exchange:      "NSE",
		TradingSymbol: "NIFTY",
		Interval:      "1mi",
		StartTime:     "09:15:00 23-04-2025",
		EndTime:       "15:29:00 23-04-2025",
	}
timePriceSeriesRegularInterval, err := Firstock.TimePriceSeriesRegularInterval(timePriceSeriesRegularIntervalRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", timePriceSeriesRegularInterval)
```

## Response Structure

**Success Response**

A valid request will typically return a **200 OK** status and a JSON object containing:

1. **status:** Typically *"success"*.
2. **message:** A note (e.g., "*Successfully fetched charts data*").
3. **data:** An array of candlestick objects.

**Key Fields within *data*:**

- *time*: Candle start time in ISO-like format (YYYY-MM-DDTHH:MM:SS).
- *epochTime*: UNIX epoch (seconds since 1970-01-01).
- *open***,***high***,***low***,***close*: O-H-L-C prices for that interval.
- *volume*: Trading volume during the interval.
- *oi*: Open interest for derivatives, if applicable.

**Failure Response**

If the session token is invalid or required fields are missing, you may receive a **400** or **401** error:

1. **status:** *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **Invalid or missing***jKey*
4. **Empty**interval or invalid format.
5. *startTime*and *endTime*in the wrong format or out of range.

**Response**

**200**

```json
{
          "status": "success",
          "message": "Successfully fetched charts data",
          "data": [
          {
            "time": "2025-02-10T09:15:00",
            "epochTime": 1739159100,
            "open": 23543.8,
            "high": 23548.65,
            "low": 23472.2,
            "close": 23480.1,
            "volume": 0,
            "oi": 0,
          },
          {
            "time": "2025-02-10T09:16:00",
            "epochTime": 1739159160,
            "open": 23480.1,
            "high": 23482.0,
            "low": 23470.0,
            "close": 23475.5,
            "volume": 0,
            "oi": 0,
          }
        ]
    }
```

**400**

```json
{
    "status": "failed",
    "code": "400",
    "name": "MISSING_FIELD",
    "error": {
      "field": "interval",
      "message": "interval cannot be empty"
    }
  }
```

## Usage & Best Practices

1. **Intraday Charting**

  - Ideal for implementing minute-based candlestick charts.
  - For daily or EOD data, see the Time Price Series (Day Interval) API.
2. **Session Validity**

  - Maintain a valid jKey. If INVALID_JKEY arises, prompt the user to log in or refresh their session.
3. **Interval Management**

  - The interval can be "1mi", "2mi", "5mi", etc. Confirm accepted intervals with Firstock docs.
4. **Time Range**

  - Ensure startTime < endTime. The API typically returns data from the start to the end date-time inclusively or exclusively depending on server logic.
5. **Data Parsing**

  - Convert numeric fields (like open, close, etc.) from string to float if needed for calculations or chart rendering.

## Conclusion

The **Time Price Series (Regular Interval)** API is a crucial endpoint for **intraday charting** and shorter-interval analysis. By specifying the **startTime**, **endTime**, and **interval** (like "1mi", "2mi", etc.), developers can construct real-time or historical intraday charts for a wide range of symbols. Always maintain valid authentication (jKey), handle errors for missing fields, and parse the returned candlestick data for visualizations or further analysis.
