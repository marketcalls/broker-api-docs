# Get Multi Quote Ltp

> Source: https://firstock.in/api/docs/get-multi-quote-ltp/

> This document outlines how to use the Get Multi Quotes LTP API within the Firstock trading platform.

## Overview

The **Get Multi Quotes LTP API** enables you to retrieve a list of **last traded prices** (and a few associated fields) for multiple instruments at once. This is especially useful if you need to monitor a portfolio or watchlist of stocks and/or derivatives in near real-time.

**Key benefits:**

1. **Batch Retrieval**: Get LTPs for multiple symbols in one request.
2. **Efficiency**: Reduce the overhead of separate API calls for each symbol.
3. **Quick Updates**: Ideal for watchlists or summary views where only LTP is required.

## Endpoint & Method

`POST` `/getMultiQuotes/ltp`

**URL**:

```
https://api.firstock.in/V1/getMultiQuotes/ltp
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body for the Get Multi Quote LTP API request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| data | array of objects | Yes | An array of instruments for which you want the LTP. Each object must include exchange and tradingSymbol. | See "data" example below |

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
  "jKey": "6db79eaa7edce0432b012fdfa5fb3d03f40125916344ed9ce87fe701469bc59e",
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
curl --location 'https://api.firstock.in/V1/getMultiQuotes/ltp' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "6db79eaa7edce0432b012fdfa5fb3d03f40125916344ed9ce87fe701469bc59e",
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
mQLTP = firstock.getMultiQuotesltp(
    userId="{{userId}}",
    dataToken=[
        {
            "exchange": "NSE",
            "tradingSymbol": "Nifty 50"
        },
        {
            "exchange": "NSE",
            "tradingSymbol": "Nifty Bank"
        }
    ]
)
print(mQLTP)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.getMultiQuotesltp(
  {
    userId:  "{{userId}}",
    data: [{ exchange: "NSE", tradingSymbol: "Nifty 50" }],
  },
  (err, result) => {
    console.log("getMultiQuotesltp Error, ", err);
    console.log("getMultiQuotesltp Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

getMultiQuotesLtpReq := Firstock.GetMultiQuotesRequest{
		UserId: userId, // replace with actual value
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
getMultiQuotesLtp, err := Firstock.GetMultiQuotesLtp(getMultiQuotesLtpReq)
fmt.Println("Error:", err)
fmt.Println("Result:", getMultiQuotesLtp)
```

## Response Structure

**Success Response**

A valid request will typically return a **200 OK** status and a JSON object containing:

1. **status:** Typically *"success"*.
2. **message:** Short description (e.g., "Multiple quotes LTP data retrieved successfully").
3. **data:** An array of objects—one for each symbol requested, containing LTP and related fields.

**Key Fields within *data*:**

- *companyName*: Display name for the instrument.
- *exchange*: The exchange code.
- *identifier*: Unique ID combining the exchange and symbol.
- *lastTradedPrice*: The LTP for the symbol.
- *requestTime*: The time at which this data was fetched.
- *token*: Numeric identifier for the instrument.
- *tradingSymbol*: The symbol for which the LTP applies.

**Failure Response**

If any required fields are missing, invalid, or the session is expired, the API may respond with a **400** or **401** status:

1. **status:** *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **Invalid or missing `jKey`**
4. **Empty or incorrectly formatted `data`** array
5. **Incorrect***exchange**or**tradingSymbol*

**Response**

**200**

```json
{
          "status": "success",
          "message": "Multiple quotes LTP data retrieved successfully",
          "data": [
          {
            "companyName": "RELIANCE INDUSTRIES LTD",
            "exchange": "NSE",
            "identifier": "NSE:RELIANCE-EQ",
            "lastTradedPrice": "1300.00",
            "requestTime": "09:13:20 22-04-2025",
            "token": 2885,
            "tradingSymbol": "RELIANCE-EQ"
          },
          {
            "companyName": "VODAFONE IDEA LIMITED",
            "exchange": "NSE",
            "identifier": "NSE:IDEA-EQ",
            "lastTradedPrice": "8.08",
            "requestTime": "09:13:20 22-04-2025",
            "token": 14366,
            "tradingSymbol": "IDEA-EQ"
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

  - Perfect for displaying multiple LTPs in real-time.
  - Consolidate user symbols into a single request to reduce overhead.
2. **Error Handling**

  - Inspect the response for partial or total failures. If status = "failed", check the error object.
3. **Session Maintenance**

  - Keep your jKey fresh; if the server responds with INVALID_JKEY, prompt the user to log in again.
4. **Reasonable Polling**

  - If you’re polling, ensure you set a suitable interval to avoid API rate limits and performance bottlenecks.
5. **Integration with Other Data**

  - Combine LTP results with user holdings, open positions, or other analytics for a complete trading overview.

## Conclusion

The **Get Multi Quotes LTP API** is a streamlined solution for retrieving **last traded prices** for multiple instruments in a single request. This helps developers create efficient watchlists and dashboards without retrieving full market-depth data. Always maintain a valid session (*jKey*), handle errors gracefully, and structure your requests to minimize API overhead. If you need detailed quotes (like best bid/ask levels or other fields), consider the **Get Multi Quotes** or **Get Quotes** APIs.
