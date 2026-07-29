# Order Margin

> Source: https://firstock.in/api/docs/order-margin/

> This document details how to use the Order Margin API on the Firstock trading platform.

## Overview

The **Order Margin API** provides a way to preview how much margin is required for a specific order configuration. This includes the total margin needed, the amount of margin you have available, and any remarks or warnings (e.g., insufficient balance).

**Key benefits:**

- **Risk Management**: Quickly check if you have enough funds or margin before placing a live order.
- **Transparency**: Receive detailed breakdowns of margin usage, available margin, and total cash.
- **Efficiency**: Avoid placing orders that might fail or get rejected due to insufficient margin.

## Endpoint & Method

`POST` `/orderMargin`

**URL**:

```
https://api.firstock.in/V1/orderMargin
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the typical JSON body for the **Order Margin API** request. All **Mandatory** fields must be provided.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| exchange | string | Yes | Name of the exchange ("NSE", "BSE", "NFO", etc.). | "NSE" |
| product | string | Yes | Product type (e.g., "C", "M", "I"). | "C" |
| priceType | string | Yes | Pricing model: e.g., "MKT", "LMT", "SL-LMT", "SL-MKT". | "MKT" |
| tradingSymbol | string | Yes | Symbol or instrument identifier (e.g., "IDEA-EQ", "NIFTY06MAR25C22500"). | "IDEA-EQ" |
| transactionType | string | Yes | "B" (Buy) or "S" (Sell). | "B" |
| price | string | Yes | Limit price for limit orders, or 0 for market orders. | "0" (for MKT order) |
| quantity | string | Yes | Number of shares or lots to trade. | "1" |

**Request:**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}",
  "exchange": "NSE",
  "transactionType": "B",
  "product": "C",
  "tradingSymbol": "NIFTY",
  "quantity": "10",
  "priceType": "LMT",
  "price": "780"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/orderMargin' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}",
    "exchange": "NSE",
    "transactionType": "B",
    "product": "C",
    "tradingSymbol": "NIFTY",
    "quantity": "10",
    "priceType": "LMT",
    "price": "780"
}'
```

**Python**

```python
from firstock import firstock
orderMargin = firstock.orderMargin(
    userId="{{userId}}",
    exchange="NSE",
    tradingSymbol="ITC-EQ",
    quantity="1",
    priceType="LMT",
    product="C",
    price="350",
    transactionType="B"
)
print(orderMargin)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.orderMargin(
  {
    userId: "{{userId}}",
    exchange: "NSE",
    tradingSymbol: "IDEA-EQ",
    quantity: "1",
    price: "10.00",
    product: "C",
    transactionType: "B",
    priceType: "LMT",
  },
  (err, result) => {
    console.log("orderMargin Error, ", err);
    console.log("orderMargin Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

orderMarginRequest := Firstock.OrderMarginRequest{
		UserId:          "{{userId}}",
		Exchange:        "BSE",
		TransactionType: "B",
	Product:         "C",
		TradingSymbol:   "SAWACA",
		Quantity:        "1",
	PriceType:       "MKT",
	Price:           "0.50",
	}
orderMargin, err := Firstock.OrderMargin(orderMarginRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", orderMargin)
```

## Response Structure

**Success Response**:

A successful request returns a **200 OK** status with a JSON object containing margin details:

- ***status***: Typically *"success"*.
- ***message***: A short description, such as *"Fetched order margin successfully"*.
- ***data***: Contains specific margin information.

**Key Fields within data**:

- ***availableMarginForTheOrder***: The margin you still have after accounting for this order.
- ***marginOnNewOrder***: The total margin required to place this new order.
- ***remarks***: Additional info, such as *"Insufficient Balance"* or other warnings.
- ***requestTime***: Timestamp when the margin calculation was processed.
- ***totalCash***: The total cash or margin balance in your account.

**Failure Response**:

If the request is malformed or any required field is missing/invalid, you may receive a **400** or **401** status code with details such as:

- ***status***: *"failed"*.
- ***code***: Error code (e.g., *"400"*, *"401"*).
- ***name***: A brief descriptor (e.g., *"BADREQUEST"*).
- ***error***: An object indicating which field caused the issue and why.

**Response**

**200**

```json
{
    "status": "success",
    "message": "Fetched order margin successfully",
    "data": {
      "availableMargin": "459.71299999999974",
      "cash": "7709",
      "marginOnNewOrder": "780468",
      "remarks": "Insufficient Balance",
      "requestTime": "16:21:04 30-04-2025"
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

- **Verify Funds Before Placing Orders**

  - Always check the margin details before placing an order to avoid rejections or partial fills.
- **Handle Remarks**

  - The *remarks* field might warn you about insufficient funds or other constraints. Display these to your users or integrate them into your risk checks.
- **Session Management**

  - The *jKey* must be valid. If it’s expired or incorrect, the API will fail with an *"INVALIDJKEY"* or similar error. Prompt re-login if necessary.
- **Product & Exchange Compatibility**

  - Ensure the *product* type is allowed on the specified *exchange*. For instance, certain product types may not be permitted on some segments.
- **Automation**

  - Many trading bots or algorithmic strategies use the **Order Margin API** to confirm feasibility of trades automatically before attempting order placement.

## **Conclusion**

The **Order Margin API** is a crucial tool for traders and developers looking to manage risk effectively. By checking the required margin in advance, you can confidently execute orders without worrying about insufficient funds or last-minute rejections.
