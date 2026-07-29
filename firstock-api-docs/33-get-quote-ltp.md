# Get Quote Ltp

> Source: https://firstock.in/api/docs/get-quote-ltp/

> This document provides an overview of the Get Quote LTP (Last Traded Price) API within the Firstock trading platform. By invoking this endpoint, you can retrieve the most recent traded price.

## Overview

The **Get Quote LTP API** focuses on retrieving the **latest price** (LTP) for a specific trading symbol, which can be essential for real-time pricing, simple displays, or quick checks of market movement. This streamlined version of quote data often excludes depth-of-market details (like best bid/ask levels) but returns a faster or simpler response.

**Key benefits:**

1. **Lightweight Data** Get the last traded price without the overhead of full market depth.
2. **Real-Time Checks** Quickly confirm the most recent market price for trades or alerts.
3. **Easy Integration** Ideal for scenarios needing just LTP and a few supporting fields.

## Endpoint & Method

`POST` `/getQuote/ltp`

**URL**:

```
https://api.firstock.in/V1/getQuote/ltp
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body for the Get Quote LTP API request. All fields marked as Mandatory must be included.

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
curl --location 'https://api.firstock.in/V1/getQuote/ltp' \
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
getQuoteLtp = firstock.getQuoteltp(
    userId="{{userId}}",
    exchange="NSE",
    tradingSymbol="RELIANCE-EQ"
)
print(getQuoteLtp)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.getQuoteltp(
  {
    userId:  "{{userId}}",
    exchange: "NSE",
    tradingSymbol: "RELIANCE-EQ",
  },
  (err, result) => {
    console.log("getQuoteltp Error, ", err);
    console.log("getQuoteltp Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

getQuoteLtpReq := Firstock.GetInfoRequest{
		UserId:        "{{userId}}",
		Exchange:      "NSE",
		TradingSymbol: "NIFTY",
	}

getQuoteDetails, err := Firstock.GetQuoteLtp(getQuoteLtpReq)
fmt.Println("Error:", err)
fmt.Println("Result:", getQuoteDetails)
```

## Response Structure

**Success Response**

A valid request will typically return a **200 OK** status and a JSON object containing:

1. **status:** Usually *"success"*.
2. **message:** A short outcome message (e.g., *"Quote LTP data retrieved successfully"*).
3. **data:** An **array** of objects holding the LTP data, often allowing for multiple symbols (though typically one is requested).

**Key Fields within *data*:**

- *companyName*: Display label or name for the security/contract.
- *exchange*: The exchange code.
- *lastTradedPrice*: The most recent traded price for the symbol.
- *requestTime*: Timestamp when the data was fetched.
- *token*: Numeric identifier for the instrument.

**Failure Response**

If required fields are missing, invalid, or the `tradingSymbol` is incorrect, the API may return a **400** or **401** status with an error object:

1. **status:** *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **Invalid *jKey***: Session expired or incorrect token.
4. **Invalid *tradingSymbol***: The order might not exist or already be completed.
5. **Missing *userId***: The system can’t identify which account is requesting cancellation.

**Response**

**200**

```json
{
          "status": "success",
          "message": "Quote LTP data retrieved successfully",
          "data": [
          {
              "companyName": "RELIANCE INDUSTRIES LTD",
              "exchange": "NSE",
              "lastTradedPrice": "1405.00",
              "requestTime": "17:38:16 30-04-2025",
              "token": "2885"
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
      "field": "orderNumber",
      "message": "required field is empty or missing: orderNumber"
    }
  }
```

## Usage & Best Practices

1. **Check Order Status First**

  - Only orders in an “open” state (e.g., pending, partially filled) can usually be canceled. If an order is already fully executed or rejected, cancellation is either unnecessary or will fail.
2. **Store Order Number**

  - Keep track of the orderNumber from the Place Order API or Order Book response. This is essential for cancellation..
3. **Session Validity**

  - Ensure that jKey is valid. If "INVALID_JKEY" appears, prompt a re-login or refresh the token as needed.
4. **Error Handling**

  - If you receive a reason like "SAF: order is not open to cancel", it typically means the order can’t be canceled at its current status. Inform users accordingly.
5. **Timing & Partial Fills**

  - An order might have partial fills between the time you decide to cancel and when the system processes your request. Always confirm the updated status via an Order Book call post-cancellation.

## Conclusion

The **Get Quote LTP API** offers a streamlined approach to fetching the **latest traded price** for a single (or multiple) symbols, perfect for quick checks or lightweight applications. Make sure to maintain valid authentication (*jKey*) and verify your symbol formats. For more advanced data (like best bid/ask levels), consider the full **Get Quotes** API. If you encounter repeated errors or need more details, refer to Firstock’s official documentation or contact support.
