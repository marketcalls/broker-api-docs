# Combined Holdings

> Source: https://firstock.in/api/docs/combined-holdings/

> This document details how to use the Combined Holdings API within the Firstock trading platform.

## Overview

The **Combined Holdings API** provides a unified view of a user's entire portfolio, consolidating both Mutual Funds and Stock holdings into a single endpoint. It aggregates absolute totals for investments, current valuations, day returns, and long-term portfolio performance, reducing the need to make multiple disjointed balance or asset-type requests.

**Key benefits:**

- **Unified Portfolio View:** See your mutual funds and equity holdings alongside aggregated totals simultaneously.
- **Integrated Performance Metrics:** Instantly receive combined calculations for totalInvested, totalCurrentValue, and percentage gains across all asset types
- **Demat Tracking:** Reflects settled long-term delivery assets alongside up-to-date net asset values (NAV) and closing prices.

## Endpoint & Method

`POST` `/combinedHoldings`

**URL**:

```
https://api.firstock.in/V1/combinedHoldings
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the JSON body for the Combined Holdings API request. All fields marked Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | 6c83407h89jbt8om0n8... |

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
Bash
curl --location 'https://api.firstock.in/V1/combinedHoldings' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}"
}'
```

**Python**

```python
Python
from firstock import firstock

combined_holdings = firstock.combinedHoldings(
    userId="{{userId}}"
)
print(combined_holdings)
```

**Nodejs**

```javascript
JavaScript
const {Firstock} = require("firstock");
const firstock = new Firstock();

firstock.combinedHoldings(
    {
        userId: "{{userId}}",
    },
    (err, result) => {
        console.log("getCombinedHoldings Error, ", err);
        console.log("getCombinedHoldings Result: ", result);
    }
);
```

**Golang**

```go
Go
import (
    "github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
    "fmt"
)

combinedHoldings, err := Firstock.CombinedHoldings("{{userId}}")
fmt.Println("Error:", err)
fmt.Println("Result:", combinedHoldings)
```

## Response Structure

**Success Response**:

If the request is valid and holdings data exists, you will receive a 200 OK status and a JSON object containing:

- ***status***: Typically *"success"*.
- ***message***: Short description (e.g., "Holdings fetched successfully").
- ***data***: A nested JSON object returning segmented sections for

  mutualFunds, stocks, and aggregated combinedHoldings.

**Key Fields in the data object**:

- ***mutualFunds***: Array of individual asset details holding fields like isin, avgNav, currentNav, pnlAmount, and unit values, along with summary objects mapping total returns.
- ***stocks***: Array tracking your core equities with exchangeTradingSymbol, listing status, margins (hairCut), and hold allocations.
- ***combinedHoldings***: Absolute structural calculation combining values from both categories to present a complete baseline of your net worth across the broker ecosystem.

**Failure Response**:

If any required field is missing, invalid, or expired, you will receive a 400 or 401 status code with an error payload configuration indicating an expired session token or incorrect user properties.

**Response**

**200**

```json
{
    "status": "success",
    "message": "Holdings fetched successfully",
    "data": {
        "mutualFunds": {
            "holdings": [
                {
                    "fundName": "Whiteoak Capital Large Cap Fund Direct Plan - Growth",
                    "isin": "INF03VN01696",
                    "avgNav": 15.79,
                    "currentNav": 15.89,
                    "navDate": "2026-07-17",
                    "investedAmount": 98.49,
                    "currentValue": 99.14,
                    "pnlAmount": 0.64,
                    "pnlPercent": 0.65,
                    "holdingQuantity": 6.238,
                    "customAvailableToPledgeQty": 6.238,
                    "customEdisAuthorizedQty": 0,
                    "customEdisQty": 6.238,
                    "customEdisToAuthorizeQty": 0,
                    "customPledgeQty": 0,
                    "isPledge": true,
                    "pledgeReqQty": 0,
                    "sipDetails": {
                        "totalSips": 0,
                        "totalAmount": 0,
                        "nextInvestmentAmount": 0,
                        "frequency": "",
                        "nextDueDate": ""
                    },
                    "approvedPrevClose": 15.89,
                    "folioNum": "",
                    "availableToRedeemUnits": 6.238,
                    "availableToRedeemAmount": 99.14
                }
            ],
            "totalInvested": 13619.94,
            "totalCurrentValue": 18372.48,
            "totalReturns": 4752.54,
            "totalReturnsPercent": 34.89,
            "numberOfHoldings": 29,
            "dayReturns": 68.29,
            "dayReturnsPercent": 0.37
        },
        "stocks": {
            "holdings": [
                {
                    "exchangeTradingSymbol": [
                        {
                            "exchange": "BSE",
                            "token": "519307",
                            "tradingSymbol": "VIKASWSP",
                            "pricePrecision": "2",
                            "tickSize": "0.01",
                            "lotSize": "1"
                        }
                    ],
                    "sellAmount": "0.000000",
                    "holdQuantity": "2",
                    "hairCut": "1.00",
                    "uploadPrice": "0.99",
                    "BTSTQuantity": "0",
                    "usedQuantity": "0",
                    "tradeQuantity": "0",
                    "beneficiaryQuantity": "0",
                    "collateralQuantity": "0"
                }
            ],
            "totalInvested": 123.1,
            "totalCurrentValue": 120.54,
            "totalReturns": -2.56,
            "totalReturnsPercent": -2.08,
            "dayReturns": 5.34,
            "dayReturnsPercent": 4.64,
            "numberOfHoldings": 5
        },
        "combinedHoldings": {
            "totalInvested": 13743.04,
            "totalCurrentValue": 18493.02,
            "totalReturns": 4749.98,
            "totalReturnsPercent": 34.56,
            "dayReturns": 73.63,
            "dayReturnsPercent": 0.4,
            "numberOfHoldings": 34
        }
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

- **Multi-Asset Portfolio Calculations**

  - By consuming the structured totals under the combinedHoldings object, frontend interfaces can map complete user balance graphs directly without manually looping over distinct data points for different assets.
- **Refresh Interventions**

  - Mutual fund NAV files traditionally settle and publish late in the evening on market days. Be aware that the mutualFunds values will reflect updates according to the timestamp in navDate, while stocks track intraday closing values or previous end-of-day pricing batches.
- **Pledging and Margin Utility**

  - The payload contains margin eligibility parameters such as customAvailableToPledgeQty and hairCut. Use these fields to calculate how much collateral margin can be unlocked by the trader across both asset segments for active margin trading blocks.
