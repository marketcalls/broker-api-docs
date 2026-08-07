# Search Scrips

> Source: https://firstock.in/api/docs/search-scrips/

> This document provides a comprehensive guide to using the Search Scrips API in the Firstock trading platform.

## Overview

The **Search Scrips API** enables you to discover and filter potential trading symbols across multiple exchanges. You can then use these valid symbols with other endpoints, such as **Get Quotes**, **Place Order**, or **Order Margin**.

**Key benefits:**

1. **User-Friendly Lookups**: Allow end users to find instruments by name or partial symbol.
2. **Multi-Exchange Support**: Retrieve matched scrips from NSE, BSE, NFO, or other supported segments.
3. **Integration with Other APIs**: Once you have the correct `tradingSymbol`, you can fetch quotes or place trades accurately.

## Endpoint & Method

`POST` `/searchScrips`

**URL**:

```
https://api.firstock.in/V1/searchScrips
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body, for the Search Scrips API request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| stext | string | Yes | text or partial symbol to match. | "ITC" |

**Request**

```json
{
  "userId": "AB1234",
  "jKey": "1478b9b71707210d8851258599b23a6a73d31b19809ac5068560f38dad493d35",
  "stext": "ITC"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/searchScrips' \
--header 'Content-Type: application/json' \
--data '{
  "userId": "{{userId}}",
  "jKey": "1478b9b71707210d8851258599b23a6a73d31b19809ac5068560f38dad493d35",
  "stext": "ITC"
}'
```

**Python**

```python
from firstock import firstock
searchScrips = firstock.searchScrips(
     userId= "{{userId}}",
     stext="ITC"
 )
 print(searchScrips)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.searchScrips(
  { userId: "{{userId}}", stext: "ITC" },
  (err, result) => {
    console.log("searchScrips Error, ", err);
    console.log("searchScrips Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

searchScripsRequest := Firstock.SearchScripsRequest{
		UserId: "{{userId}}",
		SText:  "RELIANCE",
	}
searchScrips, err := Firstock.SearchScrips(searchScripsRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", searchScrips)
```

## Response Structure

**Success Response**

A valid request will typically return a **200 OK** status and a JSON object containing:

1. **status:** Typically *"success"*.
2. **message:** A short note (e.g., "Search symbols").
3. **data:** An array of objects, each representing a matched scrip.

**Key Fields within *data*:**

- *token*: Numeric identifier for the symbol.
- *exchange*: Exchange code ("NSE", "BSE", "NFO", etc.).
- *companyName*: The entity’s official name or descriptor.
- *representationName*: A user-friendly or short name for display.
- *instrumentName*: Category (e.g., "Equity", "Options").
- *tradingSymbol*: The symbol to be used in subsequent calls (e.g., placing orders, fetching quotes).

**Failure Response**

If any required field is missing, invalid, or the order can’t be canceled, you may receive a **400** or **401** status code with an error structure:

1. **status:** *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **Invalid or missing***jKey*
4. **Missing***stext*
5. **Internal server errors** or empty result set if no matches are found (may or may not be an error).

**Response**

**200**

```json
{
          "status": "success",
          "message": "Search symbols",
          "data": [
          {
            "token": "1660",
            "exchange": "NSE",
            "companyName": "ITC LTD",
            "representationName": "ITC",
            "instrumentName": "Equity",
            "tradingSymbol": "ITC-EQ"
          },
          {
            "token": "29251",
            "exchange": "NSE",
            "companyName": "ITC HOTELS LIMITED",
            "representationName": "ITCHOTELS",
            "instrumentName": "Equity",
            "tradingSymbol": "ITCHOTELS-EQ"
          },
          {
            "token": "500875",
            "exchange": "BSE",
            "companyName": "ITC LTD.",
            "representationName": "ITC",
            "instrumentName": "Equity",
            "tradingSymbol": "ITC"
          },
          {
            "token": "96871",
            "exchange": "NFO",
            "companyName": "Monthly",
            "representationName": "ITC APR 425 CE",
            "instrumentName": "Options",
            "tradingSymbol": "ITC APR 425 CE"
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
      "field": "stext",
      "message": "stext is required"
    }
  }
```

## Usage & Best Practices

1. **Autocomplete Integration**

  - This endpoint is perfect for implementing a search bar where users can type partial company names or tickers, then pick the correct tradingSymbol.
2. **Session Validation**

  - Ensure jKey is valid. If repeated INVALID_JKEY errors appear, prompt the user to log in again.
3. **Stext Minimally**

  - Provide at least a few letters to avoid huge result sets or potential timeouts. Some APIs set a minimum length (e.g., 2-3 characters).
4. **Rate Limits**

  - If you’re querying rapidly as a user types, implement client-side throttling or debouncing to reduce excessive server hits.
5. **Use the Returned tradingSymbol**

  - Once you have a match, use tradingSymbol in subsequent API calls (e.g., Get Quotes, Place Order).

## Conclusion

The **Search Scrips API** is a valuable endpoint for helping users quickly find valid instruments. By returning key fields like *tradingSymbol*, *exchange*, and *instrumentName*, it simplifies subsequent operations like fetching quotes or placing orders. Always maintain a valid session (*jKey*), handle partial input carefully, and consider server-side constraints when implementing real-time search features.
