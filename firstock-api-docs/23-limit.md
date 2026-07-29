# Limit

> Source: https://firstock.in/api/docs/limits/

> This document explains how to use the Limits API within the Firstock trading platform.

## Overview

The **Limits API** (sometimes referred to as the **RMS Limit API**) provides insights into your current trading limits and margin usage. This includes cash on hand, collateral values, used margins, and any other resources that determine the maximum exposure a user can take in the market.

**Key benefits:**

- **Real-Time Margin Tracking**: See up-to-date available margins, exposure limits, and collateral usage.
- **Risk Management**: Identify if you have sufficient buying power for new trades.
- **Clarity & Transparency**: Keep users informed about how much margin is remaining for additional positions.

## Endpoint & Method

`POST` `/limit`

**URL**:

```
https://api.firstock.in/V1/limit
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the JSON body for the **Limits API** request. Fields marked **Mandatory** must be included.

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
curl --location 'https://api.firstock.in/V1/limit' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}"
}'
```

**Python**

```python
from firstock import firstock
limits = firstock.limit(userId="{{userId}}")
print(limits)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.limit(
  { userId: "{{userId}}" },
  (err, result) => {
    console.log("limit Error, ", err);
    console.log("limit Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

rmsLimitDetails, err := Firstock.RMSLmit("{{userId}}")
fmt.Println("Error:", err)
fmt.Println("Result:", rmsLimitDetails)
```

## Response Structure

**Success Response**:

If the request is valid and limits are retrieved successfully, you’ll receive a **200 OK** status with a JSON object containing:

- ***status***: Typically *"success"*.
- ***message***: Brief description (e.g., *"Successfully fetched RMS limits"*).
- ***data***: An object with detailed limit information.

**Key Fields within data**:

- ***availableMarginForTheOrder***: The margin you still have after accounting for this order.
- ***brkcollamt***: Broker collateral amount (if any).
- ***cash***: Current cash balance in the trading account.
- ***collateral***: Value of any pledged collateral (e.g., shares pledged for margin).
- ***expo***: Exposure margin currently utilized.
- ***marginused***: Total margin used across all open positions and orders.
- ***payin***: Funds transferred in but not yet cleared.
- ***peakmar***: Peak margin utilized during the trading session.
- ***premium***: Total option premium (paid or received).
- ***span***: SPAN margin, applicable for F&O positions.
- ***requestTime***: Timestamp indicating when these limits were fetched.

**Failure Response**:

If any required field is missing, invalid, or the order can’t be canceled, you may receive a **400** or **401** status code with an error structure:

Common error scenarios:

- **Invalid** ***jKey***: Your session might be expired or token incorrect.
- **Missing** ***userId***: The system can’t identify which account’s limits to retrieve.
- **Unauthorized** **Access**: The user might not have permission for this endpoint.

**Response**

**200**

```json
{
          "status": "success",
          "message": "Successfully fetched RMS limits",
          "data": {
            "availableMargin": "2.49",
            "brkcollamt": "0.00",
            "cash": "5.60",
            "collateral": "0.00",
            "expo": "0.00",
            "marginused": "71.49",
            "totalMargin": "2.49",
            "payin": "0.00",
            "peak_mar": "0.00",
            "premium": "0.00",
            "requestTime": "17:14:15 30-04-2025",
            "span": "0.00"
        }
  }
```

**400**

```json
{
    "status": "failed",
    "code": "401",
    "name": "INVALID_USERID",
    "error": {
      "field": "userId",
      "message": "User ID is required"
    }
  }
```

## Usage & Best Practices

- **Real-Time Margin Checks**

  - Always retrieve updated limits before placing new orders to avoid margin rejections.
- **Session Validation**

  - Ensure *jKey*is current. If you receive *INVALID_JKEY*repeatedly, prompt the user to log in again.
- **Monitor Intraday Changes**

  - Intraday trading can significantly alter margin usage. Poll the **Limits API** periodically or after major trades.
- **Combine with Other APIs**

  - Integrate **Limits** with **Order Placement**, **Positions**, and **Order Margin** for a holistic risk management system.
- **Handling Edge Cases**

  - If you see negative or zero values where unexpected, verify whether certain fields (e.g., *collateral*, *exposure*) are relevant to your trading profile.

## Conclusion

The **Limits API** is essential for maintaining proper risk management and ensuring you have sufficient margin for your trades. By regularly checking account limits, you can prevent trade rejections and keep track of how much buying power remains.
