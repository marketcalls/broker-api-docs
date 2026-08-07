# Index List

> Source: https://firstock.in/api/docs/index-list/

> This document outlines how to use the Get Multi Quotes LTP API within the Firstock trading platform.

## Overview

The **Get Index List API** provides a quick way to discover and enumerate major stock market indices. This is particularly helpful for traders or developers who need a reference of index symbols or tokens to fetch quotes (e.g., NIFTY50, SENSEX, BANKNIFTY, etc.).

**Key benefits:**

1. **Centralized Reference**: Obtain a consolidated list of commonly traded or tracked indices.
2. **Integration with Other APIs**: Use returned *tokens*or *tradingSymbol*fields for calls to quotes or historical data.
3. **Time Saver**: No need to maintain your own static list of indices.

## Endpoint & Method

`POST` `/indexList`

**URL**:

```
https://api.firstock.in/V1/indexList
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body for the Get Index List API request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |

**Request**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/indexList' \
--header 'Content-Type: application/json' \
--data '{
  "userId": "{{userId}}",
  "jKey": "211b250616fe25067a3b71b24451d1dfd389faabe338770ada62d81fd20b4bda"
}'
```

**Python**

```python
from firstock import firstock
getIndexList = firstock.indexList(userId="{{userId}}")
print(getIndexList)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.indexList(
  { userId: "{{userId}}", exchange: "NSE" },
  (err, result) => {
    console.log("getIndexList Error, ", err);
    console.log("getIndexList Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

indexList, err := Firstock.IndexList("{{userId}}")
fmt.Println("Error:", err)
fmt.Println("Result:", indexList)
```

## Response Structure

**Success Response**

A valid request will typically return a **200 OK** status and a JSON object containing:

1. **status:** Typically *"success"*.
2. **message:** Short description (e.g., "All indexes").
3. **data:** An array of index objects, each detailing a specific index.

**Key Fields within *data*:**

- exchange: Exchange code (e.g., "NSE", "BSE").
- token: Numeric identifier for the index.
- tradingSymbol: The symbol used for further quote retrieval or references.
- symbol: Sometimes the same as tradingSymbol or a shorter reference.
- idxname: A descriptive name for the index, e.g., "NIFTY 50", "SENSEX".

**Failure Response**

If the session token (*jKey*) is invalid or the request body is malformed, you may see a **400** or **401** status with error details:

1. **status:** *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **Invalid or missing**jKey
4. **Missing**userId
5. Server issues or internal errors

**Response**

**200**

```json
{
          "status": "success",
          "message": "All indexes",
          "data": [
          {
            "exchange": "NSE",
            "token": "26000",
            "tradingSymbol": "NIFTY",
            "symbol": "NIFTY",
            "idxname": "NIFTY 50"
          },
          {
            "exchange": "NSE",
            "token": "26009",
            "tradingSymbol": "BANKNIFTY",
            "symbol": "BANKNIFTY",
            "idxname": "NIFTY BANK"
          },
          {
            "exchange": "BSE",
            "token": "1",
            "tradingSymbol": "SENSEX",
            "symbol": "SENSEX",
            "idxname": "SENSEX"
          }
        ]
    }
```

**400**

```json
{
    "status": "failed",
    "code": "401",
    "name": "INVALID_JKEY",
    "error": {
      "field": "jKey",
      "message": "JKey is required"
    }
  }
```

## Usage & Best Practices

1. **Index Reference for Quotes**

  - Once you have the tradingSymbol (e.g., "NIFTY", "BANKNIFTY", "SENSEX"), you can call Get Quotes or Get Multi Quotes to fetch real-time prices.
2. **Session Management**

  - Make sure your jKey is valid. If INVALID_JKEY occurs, prompt for re-login or refresh tokens.
3. **Partial or Full List**

  - Typically, this API returns a standard set of major indices. If you need smaller custom sets, store them locally or filter the results.
4. **Error Handling**

  - Always check status. If "failed", parse the error object to pinpoint the missing/invalid parameter.
5. **Caching**

  - Since the list of indices may not change frequently, consider caching or storing it to reduce repeated calls.

## Conclusion

The **Get Index List API** provides a straightforward way to obtain identifiers for major market indices across exchanges like NSE and BSE. Use these *tokens*or *tradingSymbol*fields in subsequent quote APIs to track index prices. Always maintain a valid session (*jKey*) and handle any errors gracefully.
