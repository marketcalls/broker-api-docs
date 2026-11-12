# Get Expiry

> Source: https://firstock.in/api/docs/get-expiry/

This document explains how to use the **Get Expiry** API within the Firstock trading platform. By calling this endpoint, you can retrieve a list of upcoming expiry dates for a particular **tradingSymbol** on a given **exchange**-especially useful if you’re working with derivatives like **Futures & Options**.

## Overview

The **Get Expiry API** provides a straightforward way to **fetch all available expiry dates** relevant to a specified instrument. Developers can then use these expiry dates to request option chains, place F&O orders, or build user-friendly dropdowns for selecting expiry terms in a trading interface.

**Key benefits:**

1. **Direct Access**: Quickly obtain valid expiry dates for any F&O-enabled symbol.
2. **Up-to-Date**: Automates the process of listing new/rolling expiries.
3. **Integration**: Use returned expiry strings in subsequent calls (e.g., time price series, option chain retrieval).

## Endpoint & Method

`POST` `/getExpiry`

**URL**:

```
https://api.firstock.in/V1/getExpiry
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the typical JSON body for the Get Expiry API request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Your Firstock account ID (used during login). | AB1234 |
| jKey | string | Yes | Valid session token obtained after a successful login. | ce1c4471eb95... |
| exchange | string | Yes | Exchange code (e.g., "NSE", "BSE", "NFO", etc.). | "NSE" |
| tradingSymbol | string | Yes | The symbol to fetch expiry dates for. Typically an index or F&O instrument. | "NIFTY" |

**Request**

```json
{
    "userId": "AB1234",
    "jKey": "cc5b8ec8450c8d639ba5c46c6e5164f435638956603b1b4bf50b916a1a3db6f2",
    "exchange": "NSE",
    "tradingSymbol": "NIFTY"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/getExpiry' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "cc5b8ec8450c8d639ba5c46c6e5164f435638956603b1b4bf50b916a1a3db6f2",
    "exchange": "NSE",
    "tradingSymbol": "NIFTY"
}'
```

**Python**

```python
from firstock import firstock
fExpiry = firstock.getExpiry(
    userId="{{userId}}",
    exchange="NSE",
    tradingSymbol="NIFTY"
)
print(fExpiry)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.getExpiry(
  {
    userId:  "{{userId}}",
    exchange: "NSE",
    tradingSymbol: "NIFTY"
  },
  (err, result) => {
    console.log("getExpiry Error, ", err);
    console.log("getExpiry Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

getExpiryReq := Firstock.GetInfoRequest{
		UserId:        "{{userId}}",
		Exchange:      "NSE",
		TradingSymbol: "NIFTY",
	}
getExpiryDetails, err := Firstock.GetExpiry(getExpiryReq)
fmt.Println("Error:", err)
fmt.Println("Result:", getExpiryDetails)
```

## Response Structure

**Success Response**

If the request is valid and data is found, the API returns a **200 OK** status with a JSON object containing:

1. **status**: Typically *"success"*.
2. **message**: A note indicating success (e.g., "Expiry dates retrieved successfully").
3. **data**: An object with an array of expiry strings (expiryDates).
4. **Key Field**s within data:

  - expiryDates: An array of string values representing valid expiry dates in *DDMONYYYY* format (e.g., *"08MAY2025"*, *"15MAY2025"*).

**Failure Response**

If required fields (e.g., *jKey*, *tradingSymbol*) are missing or invalid, or if the token has expired, you may receive a **400** or **401** status code with an error structure

1. **status:** *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **Missing or incorrect**tradingSymbol**,**exchange.
4. *count*not specified

**Response**

**200**

```json
{
          "status": "success",
          "message": "Expiry dates retrieved successfully",
          "data": {
            "expiryDates": [
                "08MAY2025",
                "15MAY2025",
                "22MAY2025",
                "29MAY2025",
                "05JUN2025",
                "26JUN2025",
                "31JUL2025",
                "25SEP2025",
                "24DEC2025",
                "25MAR2026",
                "24JUN2026",
                "30DEC2026",
                "23JUN2027",
                "29DEC2027",
                "29JUN2028",
                "28DEC2028",
                "28JUN2029",
                "27DEC2029"
            ]
        }
    }
```

**400**

```json
{
    "status": "failed",
    "code": "400",
    "name": "MISSING_FIELD",
    "error": {
      "field": "tradingSymbol",
      "message": "Trading symbol is required"
    }
  }
```

## Usage & Best Practices

1. **Populate Dropdowns or Lists**

  - Once you have the array of *expiryDates*, you can display them in a UI dropdown, letting users pick which contract expiry they want to view or trade
2. **Session Validation**

  - Ensure your *jKey* is valid. If you see *INVALIDJKEY* or similar, re-authenticate the user or refresh the token.
3. **Refresh Expiry Regularly**

  - Expiry lists can change as contracts expire or new contracts appear. If building a persistent UI, fetch updated expiries periodically.
4. **Error Handling**

  - If status = *"failed"*, check the *error.field* and *error.message* to see if missing parameters or invalid session tokens are the cause.

## Conclusion

The **Get Expiry** API offers a convenient way to **list valid expiry dates** for a given symbol on a target exchange—especially valuable for **Futures & Options** workflows. Whether you’re constructing an option chain UI, placing F&O orders, or just providing user-friendly contract selection, this endpoint streamlines the process:

1. **Minimal Input**: Provide your **userId**, **jKey**, **exchange**, and **tradingSymbol**.
2. **Clear Output**: An array of expiry strings in *DDMONYYYY*format.
3. **Easy Integration**: Use these dates to fetch deeper details (like option chains, daily charts, or intraday data on each contract).

Keep your session tokens valid and handle errors properly for a seamless experience. For advanced usage or persistent issues, refer to Firstock’s official documentation or contact support.
