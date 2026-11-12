# Get Quote

> Source: https://firstock.in/api/docs/get-quote/

> This document explains how to use the Get Quotes API within the Firstock trading platform.

## Overview

The **Get Quotes API** provides developers with an interface to fetch up-to-date pricing and order book data (like best bid/ask prices) for a specific trading symbol on a given exchange. This is critical for building applications that need to display live prices, support rapid trading decisions, or perform market analytics.

**Key benefits:**

1. **Real-Time Pricing** Access current market prices for equities or derivatives.
2. **Market Depth** Receive best bid/ask levels to understand supply/demand at different price points.
3. **Flexible Integration** Works alongside other Firstock APIs (e.g., **Place Order**, **Search Scrips**, etc.).

## Endpoint & Method

`POST` `/getQuote`

**URL**:

```
https://api.firstock.in/V1/getQuote
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body for the Get Quote API request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| exchange | string | Yes | Name of the exchange ("NSE", "BSE", "NFO", etc. | "NSE" |
| tradingSymbol | string | Yes | Symbol or instrument identifier (e.g., "IDEA-EQ", "NIFTY06MAR25C22500") | "IDEA-EQ" |

**Request**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}",
  "exchange": "NSE",
  "tradingSymbol":"RELIANCE-EQ"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/getQuote' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}",
    "exchange": "NSE",
    "tradingSymbol":"RELIANCE-EQ"
}'
```

**Python**

```python
from firstock import firstock
          getQuotes = firstock.getQuote(
    userId="{{userId}}",
    exchange="NSE",
    tradingSymbol="NIFTY"
)
print(getQuotes)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.getQuote(
  {
    userId:  "{{userId}}",
    exchange: "NSE",
    tradingSymbol: "IDEA-EQ",
  },
  (err, result) => {
    console.log("getQuotes Error, ", err);
    console.log("getQuotes Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

getQuoteReq := Firstock.GetInfoRequest{
		UserId:        "{{userId}}",
		Exchange:      "NSE",
		TradingSymbol: "NIFTY",
	}

	getQuoteDetails, err := Firstock.GetQuote(getQuoteReq)
	fmt.Println("Error:", err)
	fmt.Println("Result:", getQuoteDetails)
```

## Response Structure

**Success Response**

If the request is successful and the order can be cancelled, you will receive a **200 OK** status, with:

1. **status:** *"success"*.
2. **message:** A short description indicating the outcome (e.g., *"Quote data retrieved successfully"*).
3. **data:** An object holding the quote fields.

**Key Fields within *data*:**

- ***lastTradedPrice***: The most recent traded price.
- dayHighPrice,dayLowPrice,dayOpenPrice,dayClosePrice:Daily range details.
- bestBuyPriceX/bestSellPriceX: Top bid/ask levels (e.g., bestBuyPrice1).
- ***segment***: The instrument segment, e.g., "Indices", "EQT", etc.
- ***openInterest***: Applicable primarily for F&O instruments.
- ***requestTime***: Timestamp indicating when the data was fetched.

**Failure Response**

If the request is malformed or any required field is missing/invalid, you may receive a **400** or **401** status code with details such as:

1. **status:** *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **name:** A brief descriptor (e.g., *"BAD_REQUEST"*).
4. **error:** An object indicating which field caused the issue and why.

**Response**

**200**

```json
{
          "status": "success",
          "message": "Quote data retrieved successfully",
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
            "dayClosePrice": "2412555",
            "dayHighPrice": "2420165",
            "dayLowPrice": "2407200",
            "dayOpenPrice": "2418540",
            "exchange": "NSE",
            "lastTradedPrice": "2417780",
            "lotSize": "1",
            "multipler": "1",
            "openInterest": "0.00",
            "priceFactor": "(1 / 1 ) * (1 / 1)",
            "pricePrecision": "2",
            "requestTime": "04:08:13 22-04-2025",
            "segment": "Indices",
            "symbolName": "NIFTY",
            "tickSize": "0.05",
            "token": "26000",
            "totalBuyQuantity": "0",
            "totalSellQuantity": "0",
            "tradingSymbol": "NIFTY"
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

1. **Validate Symbol**

  - Ensure the tradingSymbol and exchange pair is correct. Use Search Scrips or symbol files for accurate references.
2. **Polling Strategy**

  - If you need frequent updates, implement a sensible polling interval or consider a WebSocket (if available) to prevent excessive API calls.
3. **Session Management**

  - Confirm that your jKey is still valid. If you see INVALID_JKEY errors, prompt for re-login.
4. **Error Handling**

  - Check the status field. If "failed", review the error object to fix the input fields or authentication.
5. **Data Parsing**

  - Convert numeric fields (e.g., lastTradedPrice, dayHighPrice) from string to number if needed for calculations.

## Conclusion

The **Get Quotes API** is central to any application needing real-time or intraday market data. With features like **last traded price**, **open interest**, and **market depth**, it helps developers create dynamic trading interfaces and analytical tools. Ensure you handle authentication (*jKey*) properly, validate symbols, and manage rate limits to maintain smooth market data experiences. For additional support, consult Firstock’s official documentation or reach out to their support channels.
