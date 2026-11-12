# Get Multi Quote

> Source: https://firstock.in/api/docs/get-multi-quote/

> This document explains how to use the Get Multi Quotes API within the Firstock trading platform.

## Overview

The **Get Multi Quotes API** is designed to fetch more comprehensive quote information for multiple instruments at once. Unlike the **Get Multi Quotes LTP** API, which focuses primarily on last traded prices, this endpoint can return additional quote details (e.g., best bid/ask levels, daily price range, volume-weighted average price, etc.).

**Key benefits:**

1. **Batch Retrieval**: Gather quote data for multiple symbols in a single call.
2. **Detailed Market Data**: Includes fields like bestBuyPriceX, bestSellPriceX, dayHighPrice, dayLowPrice, and more.
3. **Efficient Integration**: Ideal for watchlists or dashboards that require more context than just the last traded price.

## Endpoint & Method

`POST` `/getMultiQuotes`

**URL**:

```
https://api.firstock.in/V1/getMultiQuotes
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body for the Get Multi Quote API request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| data | array of objects | Yes | symbols/exchanges to retrieve quotes for. | See "data" example below |

#### **Inside***data**:***

Each object in the *data*array should include:

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| exchange | string | Yes | Exchange code ("NSE", "BSE", "NFO", etc.) | "NSE" |
| tradingSymbol | string | Yes | Symbol or instrument identifier | "Nifty 50" |

**Request**

```json
{
  "userId": "AB1234",
  "jKey": "43426d92f3f877aacc99e8363914a8407a472a5ace34f135ba506b4956d02cb6",
  "data": [
    {
      "exchange": "NSE",
      "tradingSymbol": "Nifty 50"
    },
    {
      "exchange": "NFO",
      "tradingSymbol": "NIFTY03APR25C23500"
    }
  ]
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/getMultiQuotes' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "43426d92f3f877aacc99e8363914a8407a472a5ace34f135ba506b4956d02cb6",
    "data": [
        {
            "exchange": "NSE",
            "tradingSymbol": "Nifty 50"
        },
        {
            "exchange": "NFO",
            "tradingSymbol": "NIFTY03APR25C23500"
        }
    ]
}'
```

**Python**

```python
from firstock import firstock
mQ = firstock.getMultiQuotes(
    userId="{{userId}}",
    dataToken=[
        {
            "exchange": "NSE",
            "tradingSymbol": "Nifty 50"
        },
        {
            "exchange": "NFO",
            "tradingSymbol": "NIFTY03APR25C23500"
        }
    ]
)
print(mQ)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.getMultiQuotes(
  {
    userId: "{{userId}}",
    data: [
      { exchange: "NSE", tradingSymbol: "Nifty 50" },
      { exchange: "NSE", tradingSymbol: "NIFTY03APR25C23500" },
      { exchange: "NFO", tradingSymbol: "Nifty 50" },
      { exchange: "NFO", tradingSymbol: "NIFTY03APR25C23500" },
    ],
  },
  (err, result) => {
    console.log("getMultiQuotes Error, ", err);
    console.log("getMultiQuotes Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

	getMultiQuotesReq := Firstock.GetMultiQuotesRequest{
		UserId: "{{userId}}",
		Data: []Firstock.MultiQuoteData{
			{
				Exchange:      "NSE",
				TradingSymbol: "Nifty 50", // Ensure this matches the broker’s expected format
			},
			{
				Exchange:      "NFO",
				TradingSymbol: "NIFTY03APR25C23500",
			},
		},
	}

getMultiQuotes, err := Firstock.GetMultiQuotes(getMultiQuotesReq)
fmt.Println("Error:", err)
fmt.Println("Result:", getMultiQuotes)
```

## Response Structure

**Success Response**

A valid request will typically return a **200 OK** status and a JSON object containing:

1. **status:** Typically *"success"*.
2. **message:** Short description (e.g., "Multiple quotes data retrieved successfully").
3. **data:** An array of quote objects, each corresponding to the requested symbols.

**Key Fields within *data*:**

- *bestBuyPriceX**/**bestSellPriceX*: Top bid/ask prices at various levels (X = 1–5).
- *dayHighPrice***,***dayLowPrice***,***dayOpenPrice***,***dayClosePrice*: Daily trading range.
- *VWAP*: Volume-weighted average price, if applicable.
- *segment*: The instrument’s segment (e.g., `"Indices"`, `"Options"`, etc.).
- *lastTradedPrice*: The most recent traded price.
- *openInterest*: Particularly relevant for F&O instruments.

**Failure Response**

If any required fields are missing, invalid, or the session is expired, the API may respond with a **400** or **401** status:

1. **status:** *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **Invalid***jKey*or missing authentication fields.
4. **Empty or malformed***data*array.
5. **Incorrect***exchange*or invalid *tradingSymbol*

**Response**

**200**

```json
{
          "status": "success",
          "message": "Multiple quotes data retrieved successfully",
          "data": [
          {
              "VWAP": "0.00",
              "bestBuyOrder1": "0",
              "bestBuyOrder2": "0",
              "bestBuyOrder3": "0",
              "bestBuyOrder4": "0",
              "bestBuyOrder5": "0",
              "bestBuyPrice1": "0.00",
              "bestBuyPrice2": "0.00",
              "bestBuyPrice3": "0.00",
              "bestBuyPrice4": "0.00",
              "bestBuyPrice5": "0.00",
              "bestBuyQuantity1": "0",
              "bestBuyQuantity2": "0",
              "bestBuyQuantity3": "0",
              "bestBuyQuantity4": "0",
              "bestBuyQuantity5": "0",
              "bestSellOrder1": "0",
              "bestSellOrder2": "0",
              "bestSellOrder3": "0",
              "bestSellOrder4": "0",
              "bestSellOrder5": "0",
              "bestSellPrice1": "0.00",
              "bestSellPrice2": "0.00",
              "bestSellPrice3": "0.00",
              "bestSellPrice4": "0.00",
              "bestSellPrice5": "0.00",
              "bestSellQuantity1": "0",
              "bestSellQuantity2": "0",
              "bestSellQuantity3": "0",
              "bestSellQuantity4": "0",
              "bestSellQuantity5": "0",
              "companyName": "Nifty 50",
              "dayClosePrice": "24335.95",
              "dayHighPrice": "24396.15",
              "dayLowPrice": "24198.75",
              "dayOpenPrice": "24342.05",
              "exchange": "NSE",
              "identifier": "NSE:NIFTY",
              "instrumentName": "",
              "lastTradedPrice": "24334.20",
              "lotSize": "1",
              "multipler": "1",
              "openInterest": "0.00",
              "priceFactor": "(1 / 1 ) * (1 / 1)",
              "pricePrecision": "2",
              "requestTime": "17:44:35 30-04-2025",
              "segment": "Indices",
              "symbolName": "NIFTY",
              "tickSize": "0.05",
              "token": "26000",
              "totalBuyQuantity": "0",
              "totalSellQuantity": "0",
              "tradingSymbol": "NIFTY"
          },
          {
              "VWAP": "0.00",
              "bestBuyOrder1": "0",
              "bestBuyOrder2": "0",
              "bestBuyOrder3": "0",
              "bestBuyOrder4": "0",
              "bestBuyOrder5": "0",
              "bestBuyPrice1": "0.00",
              "bestBuyPrice2": "0.00",
              "bestBuyPrice3": "0.00",
              "bestBuyPrice4": "0.00",
              "bestBuyPrice5": "0.00",
              "bestBuyQuantity1": "0",
              "bestBuyQuantity2": "0",
              "bestBuyQuantity3": "0",
              "bestBuyQuantity4": "0",
              "bestBuyQuantity5": "0",
              "bestSellOrder1": "0",
              "bestSellOrder2": "0",
              "bestSellOrder3": "0",
              "bestSellOrder4": "0",
              "bestSellOrder5": "0",
              "bestSellPrice1": "0.00",
              "bestSellPrice2": "0.00",
              "bestSellPrice3": "0.00",
              "bestSellPrice4": "0.00",
              "bestSellPrice5": "0.00",
              "bestSellQuantity1": "0",
              "bestSellQuantity2": "0",
              "bestSellQuantity3": "0",
              "bestSellQuantity4": "0",
              "bestSellQuantity5": "0",
              "companyName": "NIFTY 28 29JUN 39000 P",
              "dayClosePrice": "0.05",
              "exchange": "NFO",
              "identifier": "NFO:NIFTY28JUN29P39000",
              "instrumentName": "OPTIDX",
              "lastTradedPrice": "0.05",
              "lotSize": "1",
              "multipler": "1",
              "openInterest": "0.00",
              "priceFactor": "(1 / 1 ) * (1 / 1)",
              "pricePrecision": "2",
              "requestTime": "17:44:35 30-04-2025",
              "segment": "Options",
              "symbolName": "NIFTY28JUN29P39000",
              "tickSize": "0.05",
              "token": "89665",
              "totalBuyQuantity": "0",
              "totalSellQuantity": "0",
              "tradingSymbol": "NIFTY28JUN29P39000"
          }
        ]
    }
```

**400**

```json
{
    "status": "failed",
    "code": "400",
    "name": "BAD_REQUEST",
    "error": {
      "field": "tradingSymbol",
      "message": "Trading Symbol is required"
    }
  }
```

## Usage & Best Practices

1. **Watchlists & Dashboards**

  - Perfect for real-time updates of multiple symbols with deeper quote data, beyond just LTP.
2. **Session Management**

  - Maintain a valid jKey. If repeated INVALID_JKEY errors appear, prompt re-login or refresh tokens.
3. **Rate Limits & Polling**

  - If you need frequent updates, implement a sensible polling interval or consider a streaming approach (if available) to avoid overwhelming the API.
4. **Data Parsing**

  - Convert numeric fields from strings (e.g., "2418540") to numbers if needed for calculations (like charting or analytics).
5. **Error Handling**

  - If status = "failed", parse the error object. A partially incorrect data array may cause the entire request to fail.

## Conclusion

The **Get Multi Quotes API** is an efficient way to retrieve **detailed quote information** for multiple symbols simultaneously—ideal for watchlists, dashboards, and advanced market analysis. Always maintain a valid session (jKey), handle response errors carefully, and structure your requests for efficient usage. If you need only LTP data, consider the **Get Multi Quotes LTP** API.
