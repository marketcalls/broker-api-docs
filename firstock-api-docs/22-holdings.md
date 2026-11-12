# Holdings

> Source: https://firstock.in/api/docs/holdings/

> This document details how to use the Holdings API within the Firstock trading platform.

## Overview

The **Holdings API** provides a summary of the securities that a user holds, including exchange information and trading symbols. Unlike the **Position Book**, which focuses on open/intraday positions and real-time MTM, the holdings reflect shares actually in the user’s Demat or portfolio (i.e., long-term or delivery-based investments).
**Key benefits:**

- **Clear Portfolio View**: Quickly see all instruments you own for the long term.
- **Exchange & Symbol Data**: Confirm which stocks are on which exchange.
- **Integration with Other Tools**: Combine with real-time quotes or fundamentals to track portfolio value.

## Endpoint & Method

`POST` `/holdings`

**URL**:

```
https://api.firstock.in/V1/holdings
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the JSON body for the **Holdings API** request. All fields marked **Mandatory** must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |

**Request:**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/holdings' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}"
}'
```

**Python**

```python
from firstock import firstock
holdings = firstock.holdings(userId="{{userId}}")
print(holdings)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.holdings(
  { userId: "{{userId}}" },
  (err, result) => {
    console.log("holdings Error, ", err);
    console.log("holdings Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

holdingsDetails, err := Firstock.Holdings("{{userId}}")
fmt.Println("Error:", err)
fmt.Println("Result:", holdingsDetails)
```

## Response Structure

**Success Response**:

If the request is valid and trades exist for the given account, you will receive a **200 OK** status and a JSON object containing

- ***status***: Typically *"success"*.
- ***message***: Short description (e.g., *"Fetched holdings"*).
- ***data***: An array of holding objects, each representing a unique security in your portfolio.

**Key Fields per Holding**:

- ***exchange***: The market where the security is listed, such as *"NSE"* or *"BSE"*.
- ***tradingSymbol***: The symbol or identifier representing the security.

**Failure Response**:

If any required field is missing, invalid, or the order can’t be canceled, you may receive a **400** or **401** status code with an error structure:

Common error scenarios:

- **Invalid** ***jKey***: Session might have expired; log in again.
- **Missing** ***userId***: The system can’t identify which account to retrieve holdings for.
- **No Holdings**: If you truly have no holdings, the data array may be empty, or a specific message might be returned.

**Response**

**200**

```json
{
          "status": "success",
          "message": "Fetched holdings",
          "data": [
          {
            "exchange": "BSE",
            "tradingSymbol": "INDINFO"
          },
          {
            "exchange": "NSE",
            "tradingSymbol": "VIKASECO-EQ"
          },
          {
            "exchange": "BSE",
            "tradingSymbol": "VIKASECO"
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

- **Combine with Real-Time Quotes**

  - Integrate holdings with quote data (e.g., last traded price) to show live portfolio valuations.
- **Session Management**

  - Always ensure `jKey` is valid. If `INVALID_JKEY` appears, prompt re-login or refresh.
- **Accuracy & Timing**

  - Holdings data typically updates after trades settle (T+1 or T+2 days for equities). Intraday changes may not reflect immediately.
- **Logging & Audits**

  - Keep track of user ID and timestamp of retrieval if your application requires compliance logging.
- **Error Handling**

  - Validate any “failed” response. The `field` and `message` can help you correct missing or incorrect parameters.

## **Conclusion**

The **Holdings API** is a straightforward endpoint that allows users and developers to quickly list securities in their portfolio. This data can be combined with other endpoints (such as quotes, order books, and position books) to deliver a comprehensive view of a user’s trading and investment activities.
