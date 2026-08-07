# Position Book

> Source: https://firstock.in/api/docs/position-book/

> This document details how to use the Position Book API on the Firstock trading platform.

**Note:**New fields are added in the Position Book Response, [click here](https://firstock.in/api/docs/change-logs/) to view

## Overview

The **Position Book API** provides a snapshot of open positions held in a user’s account. Each position entry includes details such as the net quantity, day buy/sell amounts, average price, and mark-to-market (MTM) information. This data is crucial for traders who want to monitor their current market exposure and unrealised profit or loss.

**Key benefits:**

- **Real-Time Position Tracking**: Keep tabs on both intraday and positional holdings.
- **Profit/Loss Insights**: Quickly gauge unrealized MTM to assess current market exposure.
- **Data Consolidation**: Combine position data with order and trade books for a complete trading overview.

## Endpoint & Method

`POST` `/positionBook`

**URL**:

```
https://api.firstock.in/V1/positionBook
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the typical JSON body for the **Position Book API** request. Fields marked **Mandatory** must be included.

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
curl --location 'https://api.firstock.in/V1/positionBook' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}"
}'
```

**Python**

```python
from firstock import firstock
positionBook = firstock.positionBook(userId="{{userId}}")
print("positionBook", positionBook)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.positionBook(
  { userId:"{{userId}}"},
  (err, result) => {
    console.log("positionBook Error, ", err);
    console.log("positionBook Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

positionBookDetails, err := Firstock.PositionBook("{{userId}}")
fmt.Println("Error:", err)
fmt.Println("Result:", positionBookDetails)
```

## Response Structure

**Success Response**:

If the request is valid and trades exist for the given account, you will receive a **200 OK** status and a JSON object containing:

- ***status***: Typically *"success"*.
- ***message***: Brief description (e.g., *"Fetched positions"*)
- ***data***: An array of position objects, each detailing a specific position.

**Key Fields per Position Entry**:

- ***dayBuyQuantity***/***daySellQuantity***: The total intraday buy/sell quantities.
- ***dayBuyAveragePrice***/***daySellAveragePrice***: Average prices for intraday trades.
- ***netQuantity***: Net position quantity (buys minus sells).
- ***netAveragePrice***: Weighted average price for the net position.
- ***unrealizedMTOM***: Mark-to-market profit/loss for the open position.
- ***RealizedPNL***: Realized profit/loss for closed portions of the position.
- ***product***: The product type (e.g., *"C"* for CNC, *"M"* for MIS).
- ***tradingSymbol***: Symbol for the security.
- ***exchange***: Exchange code (*"NSE"*, *"BSE"*, *"NFO"*, etc.).
- ***cfBuyAmt***: Total buy amount carried forward from previous trading days.
- ***cfSellAmt***: Total sell amount carried forward from previous trading days.
- ***cfBuyQty***: Total buy quantity carried forward from previous trading days.
- ***cfSellQty***: Total sell quantity carried forward from previous trading days.
- ***totalPNL***: Total profit/loss calculated using current market price versus the upload price (or net average price if upload price is zero).
- ***totalMTM***: Total mark-to-market value combining realized PNL and unrealized MTM based on current market price versus net average price.

**Failure Response**:

If any required field is missing, invalid, or the order can’t be canceled, you may receive a **400** or **401** status code with an error structure:

- **Invalid** ***jKey***: Session expired or token is incorrect.
- **Missing** ***userId***: The system cannot determine which account to reference.
- **No Positions**: If there are truly no open positions, the API may return an empty data array (or a specific message).

**Response**

**200**

```json
      {
    "status": "success",
    "message": "Positions retrieved successfully",
    "data": [
        {
            "RealizedPNL": "0.03",
            "cfBuyAmt": "",
            "cfBuyQty": "",
            "cfSellAmt": "",
            "cfSellQty": "",
            "dayBuyAmount": "7.68",
            "dayBuyAveragePrice": "7.68",
            "dayBuyQuantity": "01",
            "daySellAmount": "7.71",
            "daySellAveragePrice": "7.71",
            "daySellQuantity": "01",
            "exchange": "NSE",
            "lastTradedPrice": "7.72",
            "lotSize": "1",
            "netAveragePrice": "0.00",
            "netQuantity": "0",
            "netUploadPrice": "0.00",
            "product": "C",
            "tickSize": "5.00",
            "token": "14366",
            "totalMTM": "0.03",
            "totalPNL": "0.03",
            "tradingSymbol": "IDEA-EQ",
            "uploadPrice": "00",
            "userId": "NP2997"
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
      "message": "jKey is required"
    }
  }
```

## Usage & Best Practices

- **Monitor Profit/Loss**

  - The *unrealizedMTOM*field is particularly useful for real-time P/L analysis.
- **Partial vs. Full Positions**

  - Some entries might represent partially squared-off positions. Keep track of *netQuantity*to see how many shares/contracts remain.
- **Intraday vs. Carry Forward**

  - Pay attention to the *product*field. For intraday positions (*"M"*, *"MIS"*) vs. delivery/carry forward (*"C"*), the margin requirements and auto-square-off rules differ.
- **Session Validity**

  - Ensure *jKey*is current. If an error indicates *INVALID_JKEY*, prompt for re-login.
- **Data Synchronization**

  - Integrate with the **Order Book**, **Trade Book**, and **RMS Limit** data for a comprehensive real-time view of the user’s account status.

## Conclusion

The **Position Book API** is vital for traders who need up-to-date information on their open positions and real-time profit/loss estimates. Integrating this endpoint into your application allows you to provide users with accurate insights into their current market exposure, helping them make informed trading decisions.
