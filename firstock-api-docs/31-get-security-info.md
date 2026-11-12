# Get Security Info

> Source: https://firstock.in/api/docs/get-security-info/

> This document outlines the Get Security Info API within the Firstock trading platform.

## Overview

The **Get Security Info API** helps you confirm the internal and display identifiers for a given *tradingSymbol*on a specific exchange. This is particularly useful if you need more precise data about an instrument—beyond just last traded price, especially when working with multiple segments (e.g., EQT, FNO).

**Key benefits:**

1. **Accurate Instrument Details**: Obtain fields like *instrumentName*and *segment*.
2. **Verification Step**: Confirm that a *tradingSymbol*is valid and get its underlying system name (*symbolName*) or numeric token.
3. **Useful for F&O**: Distinguish between futures, options, underlying indices or stocks, etc.

## Endpoint & Method

`POST` `/securityInfo`

**URL**:

```
https://api.firstock.in/V1/securityInfo
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body for the Get Security Info API request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| exchange | string | Yes | Name of the exchange ("NSE", "BSE", "NFO", etc. | "NSE" |
| tradingSymbol | string | Yes | Symbol or instrument identifier (e.g., "IDEA-EQ", "NIFTY06MAR25C22500") | "IDEA-EQ" |

**Request**

```json
{
  "userId": "AB1234",
  "jKey": "51dabe2245368d04bcb90490eb7c9a3ae4d35c034cebacf1aa7d5f78246c8018",
  "exchange": "NSE",
  "tradingSymbol": "NIFTY"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/securityInfo' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "51dabe2245368d04bcb90490eb7c9a3ae4d35c034cebacf1aa7d5f78246c8018",
    "exchange": "NSE",
    "tradingSymbol": "NIFTY"
}'
```

**Python**

```python
from firstock import firstock
getSecurityInfo = firstock.securityInfo(
    userId="{{userId}}",
    exchange="NSE",
    tradingSymbol="NIFTY"

)
print(getSecurityInfo)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.securityInfo(
  {
    userId:  "{{userId}}",
    exchange: "NSE",
    tradingSymbol: "NIFTY",
  },
  (err, result) => {
    console.log("getSecurityInfo Error, ", err);
    console.log("getSecurityInfo Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

getSecurityInfo := Firstock.GetInfoRequest{
		UserId:        "{{userId}}",
		Exchange:      "NSE",
		TradingSymbol: "NIFTY",
	}

getSecurityInfoDetails, err := Firstock.GetSecurityInfo(getSecurityInfo)
fmt.Println("Error:", err)
fmt.Println("Result:", getSecurityInfoDetails)
```

## Response Structure

**Success Response**

A valid request will typically return a **200 OK** status and a JSON object containing:

1. **status:** Usually *"success"*.
2. **message:** A short note (e.g., *"Fetched security info successfully"*).
3. **data:** An object detailing the security’s info.

**Key Fields within *data*:**

- *instrumentName*: The instrument category (e.g., "*EQ*", "*OPTIDX*", "*FUTSTK*", etc.).
- *segment*: The market segment (e.g., "*EQT*", "*FNO*", etc.).
- *symbolName*: The system-recognized name for the instrument.
- *tradingSymbol*: The display-oriented name (may differ from the input if the system has a specific format).
- *token*: Numeric identifier used within Firstock’s system.
- *priceFactor***,***pricePrecision***,***tickSize*: Information about how prices are calculated or displayed.

**Failure Response**

If any required field is missing, invalid, or the session token (`jKey`) is expired, you may receive a **400** or **401** status code with an error object:

1. **status:** *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **Invalid or missing***jKey*.
4. **Empty or incorrect***tradingSymbol*or *exchange*.
5. **Security not found** (the symbol may not exist or be spelled incorrectly).

**Response**

**200**

```json
{
    "status": "success",
    "message": "Fetched security info successfully",
    "data": {
        "companyName": "VODAFONE IDEA LIMITED",
        "exchange": "NSE",
        "freezeQuantity": "15059681",
        "instrumentName": "EQ",
        "lotSize": "1",
        "mult": "1",
        "priceFactor": "(1 / 1 ) * (1 / 1)",
        "pricePrecision": "2",
        "segment": "EQT",
        "symbolName": "IDEA",
        "tickSize": "1.00",
        "token": "14366",
        "tradingSymbol": "IDEA-EQ"
    }
}
```

**400**

```json
{
    "status": "failed",
    "code": "400",
    "name": "BAD_REQUEST",
    "error": {
      "field": "exchange",
      "message": "required field is empty or missing: exchange"
    }
  }
```

## Usage & Best Practices

1. **Verification Before Trading**

  - Use this API to confirm the correct segment, instrumentName, or lotSize before placing F&O orders.
2. **Session Management**

  - Maintain a valid jKey. If INVALID_JKEY or similar errors arise, re-login or refresh tokens as needed.
3. **Error Handling**

  - If status is "failed", review the error.field and error.message to correct any missing or invalid parameters.
4. **Reference Data**

  - Consider storing or caching common results if you repeatedly request the same symbol (e.g., “NIFTY”) to reduce API overhead.
5. **Integration with Other APIs**

  - Combine with Order Margin, Place Order, or Get Quotes for a seamless workflow once you have the correct details for a symbol.

## Conclusion

The **Get Security Info API** is a crucial tool for validating an instrument’s internal details—such as **segment**, **instrumentName**, **lotSize**, and **token**—before you proceed with more advanced operations. Make sure to maintain a valid session (*jKey*), handle errors gracefully, and use this data to ensure you’re interacting with the correct instrument.The **Get Quote LTP API** offers a streamlined approach to fetching the **latest traded price** for a single (or multiple) symbols, perfect for quick checks or lightweight applications. Make sure to maintain valid authentication (*jKey*) and verify your symbol formats. For more advanced data (like best bid/ask levels), consider the full **Get Quotes** API. If you encounter repeated errors or need more details, refer to Firstock’s official documentation or contact support.
