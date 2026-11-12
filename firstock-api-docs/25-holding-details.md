# Holding Details

> Source: https://firstock.in/api/docs/holding-details/

> This document details how to use the Holdings API within the Firstock trading platform.

## Overview

The **Holdings Details API** provides a summary of the securities that a user holds, including exchange information and trading symbols. Unlike the **Position Book**, which focuses on open/intraday positions and real-time MTM, the holdings reflect shares actually in the user’s Demat or portfolio (i.e., long-term or delivery-based investments).
**Key benefits:**

- **Clear Portfolio View**: Quickly see all instruments you own for the long term.
- **Exchange & Symbol Data**: Confirm which stocks are on which exchange.
- **Integration with Other Tools**: Combine with real-time quotes or fundamentals to track portfolio value.

## Endpoint & Method

`POST` `/holdingsDetails`

**URL**:

```
https://api.firstock.in/V1/holdingsDetails
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the JSON body for the **Holdings API** request. All fields marked **Mandatory** must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for | SU2707 |
| jKey | string | Yes | Active session token obtained from a successful login. | 135ddfc93f8d0d864bc3ffff3... |

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
curl --location 'https://api.firstock.in/V1/holdingsDetails' \
--header 'Content-Type: application/json' \
--data '{
"userId": "{{userId}}",
    "jKey": "{{jKey}}"
}'
```

**Python**

```python
from firstock import firstock

holdings_details = firstock.getHoldingsDetails(
    userId="{{userId}}"
)
print(holdings_details)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.getHoldingsDetails(
  {
    userId: "{{userId}}",
  },
  (err, result) => {
    console.log("getHoldingsDetails Error, ", err);
    console.log("getHoldingsDetails Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

holdingsDetails, err := Firstock.HoldingsDetails("{{userId}}")
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
- ***token***: Unique token or identifier for the scrip.
- ***pricePrecision***: Number of decimal places to which the price of the scrip can be specified.
- ***tickSize***: Minimum price movement of the scrip.
- ***lotSize***: Quantity of the underlying asset in one contract of the scrip.

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
            "exchangeTradingSymbol": [
                {
                    "exchange": "NSE",
                    "token": "18562",
                    "tradingSymbol": "MITTAL-EQ",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                }
            ],
            "sellAmount": "0.000000",
            "holdQuantity": "1",
            "hairCut": "1.00",
            "dpQuantity": "0",
            "unPledgeQuantity": "0",
            "uploadPrice": "2.23",
            "BTSTQuantity": "0",
            "usedQuantity": "0",
            "tradeQuantity": "0",
            "brokerCollateralQuantity": "0",
            "beneficiaryQuantity": "0",
            "collateralQuantity": "0"
        },
        {
            "exchangeTradingSymbol": [
                {
                    "exchange": "NSE",
                    "token": "11915",
                    "tradingSymbol": "YESBANK-EQ",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                },
                {
                    "exchange": "BSE",
                    "token": "532648",
                    "tradingSymbol": "YESBANK",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                }
            ],
            "sellAmount": "37.540000",
            "holdQuantity": "2",
            "hairCut": "0.20",
            "dpQuantity": "0",
            "unPledgeQuantity": "0",
            "uploadPrice": "20.13",
            "BTSTQuantity": "0",
            "usedQuantity": "2",
            "tradeQuantity": "2",
            "brokerCollateralQuantity": "0",
            "beneficiaryQuantity": "0",
            "collateralQuantity": "0"
        },
        {
            "exchangeTradingSymbol": [
                {
                    "exchange": "NSE",
                    "token": "14366",
                    "tradingSymbol": "IDEA-EQ",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                },
                {
                    "exchange": "BSE",
                    "token": "532822",
                    "tradingSymbol": "IDEA",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                }
            ],
            "sellAmount": "19.650000",
            "holdQuantity": "22",
            "hairCut": "0.23",
            "dpQuantity": "0",
            "unPledgeQuantity": "0",
            "uploadPrice": "7.26",
            "BTSTQuantity": "0",
            "usedQuantity": "3",
            "tradeQuantity": "3",
            "brokerCollateralQuantity": "0",
            "beneficiaryQuantity": "0",
            "collateralQuantity": "0"
        },
        {
            "exchangeTradingSymbol": [
                {
                    "exchange": "NSE",
                    "token": "25851",
                    "tradingSymbol": "VAL30IETF-EQ",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                },
                {
                    "exchange": "BSE",
                    "token": "544275",
                    "tradingSymbol": "VAL30IETF",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                }
            ],
            "sellAmount": "0.000000",
            "holdQuantity": "0",
            "hairCut": "0",
            "dpQuantity": "0",
            "unPledgeQuantity": "0",
            "uploadPrice": "12.90",
            "BTSTQuantity": "2",
            "usedQuantity": "0",
            "tradeQuantity": "0",
            "brokerCollateralQuantity": "0",
            "beneficiaryQuantity": "0",
            "collateralQuantity": "0"
        },
        {
            "exchangeTradingSymbol": [
                {
                    "exchange": "BSE",
                    "token": "505343",
                    "tradingSymbol": "MONOT",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                }
            ],
            "sellAmount": "0.000000",
            "holdQuantity": "1",
            "hairCut": "1.00",
            "dpQuantity": "0",
            "unPledgeQuantity": "0",
            "uploadPrice": "1.74",
            "BTSTQuantity": "0",
            "usedQuantity": "0",
            "tradeQuantity": "0",
            "brokerCollateralQuantity": "0",
            "beneficiaryQuantity": "0",
            "collateralQuantity": "0"
        },
        {
            "exchangeTradingSymbol": [
                {
                    "exchange": "NSE",
                    "token": "10753",
                    "tradingSymbol": "UNIONBANK-EQ",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                },
                {
                    "exchange": "BSE",
                    "token": "532477",
                    "tradingSymbol": "UNIONBANK",
                    "pricePrecision": "2",
                    "tickSize": "0.05",
                    "lotSize": "1"
                }
            ],
            "sellAmount": "136.230000",
            "holdQuantity": "2",
            "hairCut": "0.20",
            "dpQuantity": "0",
            "unPledgeQuantity": "0",
            "uploadPrice": "69.85",
            "BTSTQuantity": "0",
            "usedQuantity": "1",
            "tradeQuantity": "1",
            "brokerCollateralQuantity": "0",
            "beneficiaryQuantity": "0",
            "collateralQuantity": "0"
        },
        {
            "exchangeTradingSymbol": [
                {
                    "exchange": "NSE",
                    "token": "25756",
                    "tradingSymbol": "VIKASECO-EQ",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                },
                {
                    "exchange": "BSE",
                    "token": "530961",
                    "tradingSymbol": "VIKASECO",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                }
            ],
            "sellAmount": "0.000000",
            "holdQuantity": "2",
            "hairCut": "1.00",
            "dpQuantity": "0",
            "unPledgeQuantity": "0",
            "uploadPrice": "2.57",
            "BTSTQuantity": "0",
            "usedQuantity": "0",
            "tradeQuantity": "0",
            "brokerCollateralQuantity": "0",
            "beneficiaryQuantity": "0",
            "collateralQuantity": "0"
        },
        {
            "exchangeTradingSymbol": [
                {
                    "exchange": "NSE",
                    "token": "20532",
                    "tradingSymbol": "AXISGOLD-EQ",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                },
                {
                    "exchange": "BSE",
                    "token": "533570",
                    "tradingSymbol": "AXISGOLD",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                }
            ],
            "sellAmount": "0.000000",
            "holdQuantity": "0",
            "hairCut": "0",
            "dpQuantity": "0",
            "unPledgeQuantity": "0",
            "uploadPrice": "83.90",
            "BTSTQuantity": "1",
            "usedQuantity": "0",
            "tradeQuantity": "0",
            "brokerCollateralQuantity": "0",
            "beneficiaryQuantity": "0",
            "collateralQuantity": "0"
        },
        {
            "exchangeTradingSymbol": [
                {
                    "exchange": "NSE",
                    "token": "9931",
                    "tradingSymbol": "VIKASLIFE-EQ",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                },
                {
                    "exchange": "BSE",
                    "token": "542655",
                    "tradingSymbol": "VIKASLIFE",
                    "pricePrecision": "2",
                    "tickSize": "0.01",
                    "lotSize": "1"
                }
            ],
            "sellAmount": "0.000000",
            "holdQuantity": "0",
            "hairCut": "1.00",
            "dpQuantity": "1",
            "unPledgeQuantity": "0",
            "uploadPrice": "2.58",
            "BTSTQuantity": "0",
            "usedQuantity": "0",
            "tradeQuantity": "0",
            "brokerCollateralQuantity": "0",
            "beneficiaryQuantity": "0",
            "collateralQuantity": "0"
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

The **Holdings Details API** is a straightforward endpoint that allows users and developers to quickly list securities in their portfolio. This data can be combined with other endpoints (such as quotes, order books, and position books) to deliver a comprehensive view of a user’s trading and investment activities.
