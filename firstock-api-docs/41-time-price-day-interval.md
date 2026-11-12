# Time Price Day Interval

> Source: https://firstock.in/api/docs/time-price-day-interval/

> This document explains how to use the Time Price Series (Day Interval) API within the Firstock trading platform.

## Overview

The **Time Price Series (Day Interval)** API is used for fetching **daily candlestick data**—including open, high, low, close (OHLC) values, trading volume, and open interest—over a specified date range. This is ideal for plotting **EOD (end-of-day) charts** or performing longer-term backtesting and analysis.

**Key benefits:**

1. **Historical EOD Data**: Access daily candles for various symbols and exchanges.
2. **Custom Date Range**: Provide start and end times in *DD-MM-YYYY HH:MM:SS* (though typically you’ll focus on the date).
3. **Long-Term Analysis**: Suitable for daily charts, swing trading strategies, or historical performance reviews.

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

Below is the general JSON body for the Time Price Series (Day Interval) request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| exchange | string | Yes | The exchange code ("NSE", "BSE", "NFO", etc.) | "NSE" |
| tradingSymbol | string | Yes | The symbol or instrument for which to retrieve time-series data. | NIFTY" |
| startTime | string | Yes | Start date-time in DD-MM-YYYY HH:MM:SS format (24-hour clock). | "09:15:00 23-04-2025" |
| endTime | string | Yes | End date-time in the same format. | "15:29:00 23-04-2025" |
| interval | string | Yes | The candle interval, e.g., "1mi", "2mi", "5mi", etc. | 1d" |

**Request**

```json
{
  "userId": "AB1234",
  "jKey": "6db79eaa7edce0432b012fdfa5fb3d03f40125916344ed9ce87fe701469bc59e",
  "exchange": "NSE",
  "interval": "1d",
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
    "interval": "1d",
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
    interval="1d"
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
    interval: "1d",
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

timePriceSeriesDayIntervalRequest := Firstock.TimePriceSeriesIntervalRequest{
		UserId:                "{{userId}}",
		Exchange:           "NSE",
		TradingSymbol:   "NIFTY",
		Interval:               "1d",
		StartTime:           "09:15:00 20-04-2025",
		EndTime:            "15:29:00 23-04-2025",
	}
timePriceSeriesDayInterval, err := Firstock.TimePriceSeriesDayInterval(timePriceSeriesDayIntervalRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", timePriceSeriesDayInterval)
```

## Response Structure

**Success Response**

A valid request will typically return a **200 OK** status and a JSON object containing:

1. **status:** Typically *"success"*.
2. **message:** A note (e.g., "*Successfully fetched charts data*").
3. **data:** An array of candlestick objects.

**Key Fields within *data*:**

- *time*: The date in ISO-like format for that day.
- *epochTime*: UNIX epoch (seconds since 1970-01-01).
- *open***,***high***,***low***,***close*: O-H-L-C prices for that interval.
- *volume*: Trading volume during the interval.
- *oi*: Open interest, mostly relevant for futures/options.

**Failure Response**

If the session token is invalid or required fields are missing, you may receive a **400** or **401** error:

1. **status:** *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **Invalid or missing***jKey*
4. *interval*is not "*1d*" or missing.
5. **Date/time format** issues with *startTime*or *endTime*.

**Response**

**200**

```json
{
          "status": "success",
          "message": "Successfully fetched charts data",
          "data": [
          {
              "time": "00:00:00 23-04-2025",
              "epochTime": 1745346600,
              "open": 24277.9,
              "high": 24347.85,
              "low": 24216.15,
              "close": 24246.7,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 24-04-2025",
              "epochTime": 1745433000,
              "open": 24289,
              "high": 24365.45,
              "low": 23847.85,
              "close": 24039.35,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 25-04-2025",
              "epochTime": 1745519400,
              "open": 24289,
              "high": 24365.45,
              "low": 23847.85,
              "close": 24039.35,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 26-04-2025",
              "epochTime": 1745605800,
              "open": 24289,
              "high": 24365.45,
              "low": 23847.85,
              "close": 24039.35,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 27-04-2025",
              "epochTime": 1745692200,
              "open": 24070.25,
              "high": 24355.1,
              "low": 24054.05,
              "close": 24328.5,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 28-04-2025",
              "epochTime": 1745778600,
              "open": 24370.7,
              "high": 24457.65,
              "low": 24290.75,
              "close": 24335.95,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 29-04-2025",
              "epochTime": 1745865000,
              "open": 24370.7,
              "high": 24457.65,
              "low": 24290.75,
              "close": 24335.95,
              "volume": 0,
              "oi": 0
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

1. **Long-Term Charting**

  - Use this API for daily or end-of-day candles. For intraday intervals, see the Time Price Series (Regular Interval) API.
2. **Session Validity**

  - Maintain a valid jKey. If INVALID_JKEY arises, prompt the user to log in or refresh their session.
3. **Date Range**

  - Provide a reasonable start and end date range. Large ranges might impact performance or data availability.
4. **Data Parsing**

  - Convert numeric fields from strings to floats as needed for charting or calculations.
5. **Integration with Other APIs**

  - Combine daily chart data with quotes or fundamental data for a robust trading dashboard.

## Conclusion

The **Time Price Series (Day Interval)** API offers an easy way to **fetch daily OHLC candlestick data** within a specified date range. This is critical for **EOD charting**, **longer-term backtesting**, and **historical analytics**. Always keep your session token (*jKey*) valid, ensure the date/time format is correct, and parse the returned data appropriately.
