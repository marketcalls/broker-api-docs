# Basket Orders

> Source: https://firstock.in/api/docs/basket-orders/

> This document provides a detailed overview of the **Basket Order API** for the Firstock trading platform.

## Overview

The **Basket Order API** allows authenticated clients to place multiple orders in a single API request. Each individual order is treated as a separate leg inside the basket. This API is useful for executing multi-leg strategies, option spreads, hedging strategies, and grouped order placements efficiently.

**Key benefits:**

- **Multi-Leg Order Placement**: Place multiple buy/sell orders together in a single request.
- **Strategy Execution**: Suitable for spreads, hedging, and basket-based trading strategies.
- **Reduced API Calls**: Execute several orders using one API request.
- **Broad Exchange Coverage**: Supports NSE, BSE, NFO, and other supported exchanges.
- **Seamless Integration**: Easily integrate basket order workflows into trading applications.

## Endpoint & Method

`POST` `/basketOrder`

**URL**:

```
https://api.firstock.in/V1/basketOrder
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the general JSON body for the Basket Order API request. Fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| legs | string | Yes | Array containing multiple order legs to be executed. | [] |

**Legs Object Parameters**

Each object inside the legs array represents an individual order.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| exchange | string | Yes | Name of the exchange ("NSE", "BSE", "NFO", etc.). | "NFO" |
| retention | string | Yes | Indicates the order validity period (e.g., "DAY", "IOC"). | "DAY" |
| product | string | Yes | Product type (e.g., "C", "M", "I"). | "M" |
| priceType | string | Yes | Pricing model: e.g., "MKT", "LMT", "SL-LMT", "SL-MKT". | "MKT" |
| tradingSymbol | string | Yes | Symbol or instrument identifier. | "NIFTY28APR26C23700" |
| transactionType | string | Yes | "B" (Buy) or "S" (Sell). | "B" |
| price | string | Yes | Limit price for limit orders, or 0 for market orders. | "0" |
| triggerPrice | string | No | Trigger price for stop-loss orders. For non-SL orders, set this to 0. | "0" |
| quantity | string | Yes | Number of shares or lots to trade. | "65" |
| mkt_protection | string | No | NMarket protection percentage for market orders. Only user-defined values are accepted. | "1" |
| remarks | string | Yes | Optional comment or identifier for the order leg. | "Basket Leg 1" |

**Request:**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}",
  "legs": [
    {
      "exchange": "NFO",
      "retention": "DAY",
      "product": "M",
      "priceType": "MKT",
      "tradingSymbol": "NIFTY28APR26C23700",
      "transactionType": "S",
      "price": "70.00",
      "triggerPrice": "0",
      "quantity": "65",
      "mkt_protection": "1",
      "remarks": "seq-leg1-buy-call"
    },
    {
      "exchange": "NFO",
      "retention": "DAY",
      "product": "M",
      "priceType": "MKT",
      "tradingSymbol": "NIFTY28APR26C23800",
      "transactionType": "B",
      "price": "65.00",
      "triggerPrice": "0",
      "quantity": "65",
      "mkt_protection": "1",
      "remarks": "seq-leg2-sell-put"
    },
    {
      "exchange": "NFO",
      "retention": "DAY",
      "product": "M",
      "priceType": "LMT",
      "tradingSymbol": "NIFTY28APR26C23900",
      "transactionType": "B",
      "price": "65.00",
      "triggerPrice": "0",
      "quantity": "65",
      "remarks": "seq-leg3-buy-call"
    }
  ]
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/basketOrder' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "AR23",
    "jKey": "f93fdb03c7a9dc2f9612b6b4c70f",
    "legs": [
        {
            "exchange": "NFO",
            "retention": "DAY",
            "product": "M",
            "priceType": "MKT",
            "tradingSymbol": "NIFTY28APR26C23700",
            "transactionType": "S",
            "price": "70.00",
            "triggerPrice": "0",
            "quantity": "65",
            "mkt_protection": "1",
            "remarks": "seq-leg1-buy-call"
        },
        {
            "exchange": "NFO",
            "retention": "DAY",
            "product": "M",
            "priceType": "MKT",
            "tradingSymbol": "NIFTY28APR26C23800",
            "transactionType": "B",
            "price": "65.00",
            "triggerPrice": "0",
            "quantity": "65",
            "mkt_protection": "1",
            "remarks": "seq-leg2-sell-put"
        },
        {
            "exchange": "NFO",
            "retention": "DAY",
            "product": "M",
            "priceType": "LMT",
            "tradingSymbol": "NIFTY28APR26C23900",
            "transactionType": "B",
            "price": "65.00",
            "triggerPrice": "0",
            "quantity": "65",
            "remarks": "seq-leg3-buy-call"
        }
    ]
}'
```

**Python**

```python
from firstock import firstock

basketOrder = firstock.basketOrder(
    userId="{{userId}}",
    legs=[
        {
            "exchange": "NFO",
            "retention": "DAY",
            "product": "M",
            "priceType": "MKT",
            "tradingSymbol": "NIFTY28APR26C23700",
            "transactionType": "S",
            "price": "70.00",
            "triggerPrice": "0",
            "quantity": "65",
            "mkt_protection": "1",
            "remarks": "Python Basket Leg 1"
        },
        {
            "exchange": "NFO",
            "retention": "DAY",
            "product": "M",
            "priceType": "LMT",
            "tradingSymbol": "NIFTY28APR26C23900",
            "transactionType": "B",
            "price": "65.00",
            "triggerPrice": "0",
            "quantity": "65",
            "remarks": "Python Basket Leg 2"
        }
    ]
)

print(basketOrder)
```

**Nodejs**

```javascript
const { Firstock } = require("firstock");
const firstock = new Firstock();

firstock.basketOrder(
  {
    userId: "{{userId}}",
    legs: [
      {
        exchange: "NFO",
        retention: "DAY",
        product: "M",
        priceType: "MKT",
        tradingSymbol: "NIFTY28APR26C23700",
        transactionType: "S",
        price: "70.00",
        triggerPrice: "0",
        quantity: "65",
        mkt_protection: "1",
        remarks: "Node Basket Leg 1"
      },
      {
        exchange: "NFO",
        retention: "DAY",
        product: "M",
        priceType: "LMT",
        tradingSymbol: "NIFTY28APR26C23900",
        transactionType: "B",
        price: "65.00",
        triggerPrice: "0",
        quantity: "65",
        remarks: "Node Basket Leg 2"
      }
    ]
  },
  (err, result) => {
    console.log("basketOrder Error:", err);
    console.log("basketOrder Result:", result);
  }
);
```

**Golang**

```go
package main

import (
    "fmt"
    "github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

func main() {

    basketOrderRequest := Firstock.BasketOrderRequest{
        UserId: "{{userId}}",
        Legs: []Firstock.PlaceOrderRequest{
            {
                Exchange:        "NFO",
                Retention:       "DAY",
                Product:         "M",
                PriceType:       "MKT",
                TradingSymbol:   "NIFTY28APR26C23700",
                TransactionType: "S",
                Price:           "70.00",
                TriggerPrice:    "0",
                Quantity:        "65",
                MktProtection:   "1",
                Remarks:         "Go Basket Leg 1",
            },
            {
                Exchange:        "NFO",
                Retention:       "DAY",
                Product:         "M",
                PriceType:       "LMT",
                TradingSymbol:   "NIFTY28APR26C23900",
                TransactionType: "B",
                Price:           "65.00",
                TriggerPrice:    "0",
                Quantity:        "65",
                Remarks:         "Go Basket Leg 2",
            },
        },
    }

    basketOrder, err := Firstock.BasketOrder(basketOrderRequest)
    fmt.Println("Error:", err)
    fmt.Println("Result:", basketOrder)
}
```

## Response Structure

**Success Response**:

If the basket order request is accepted successfully, you will receive a 200 OK status with a JSON object containing:

- ***status***: Typically *"success"*.
- ***message***: Brief description of the outcome.
- ***data***: Array containing order details for each basket leg.

**Key Fields in the data object**:

- ***orderNumber***: A unique identifier for the placed order.
- ***requestTime***: Timestamp when the order was processed..

**Failure Response**:

If the request is malformed or any required field is missing/invalid, you may receive a 400 or 401 status code with details such as:

- **status**: ***failed***.
- **code**: Error code (e.g., "**400**", "**401**").
- **name** : Brief descriptor (e.g., "**BAD_REQUEST**")
- **error**: Object indicating which field caused the issue and why.

**Response**

**200**

```json
{
    "status": "success",
    "message": "Order details",
    "data": {
      "orderNumber": "26030400001234",
      "requestTime": "09:45:08 04-03-2026"
    }
}
```

**200(Sliced Orders)**

```json
{
  "status": "success",
  "message": "Basket order details",
  "data": [
    {
      "orderNumber": "25042100011119",
      "requestTime": "17:50:52 21-04-2025"
    },
    {
      "orderNumber": "25042100011120",
      "requestTime": "17:50:52 21-04-2025"
    },
    {
      "orderNumber": "25042100011121",
      "requestTime": "17:50:53 21-04-2025"
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
    "field": "legs",
    "message": "required field is empty or missing: legs"
  }
}
```

## Usage & Best Practices

- **Basket Strategy Execution**

  - Use basket orders for option spreads, hedging strategies, and multi-leg execution workflows.
- **Market Protection**

  - When priceType is MKT, SL-MKT the mkt_protection field is required and must be greater than 0.
  - MKT orders are converted to LMT with a price derived from the best bid/ask (or LTP) adjusted by the mkt_protection percentage.
  - If mkt_protection is missing or ≤ 0 for these order types, the API returns a 400 BAD_REQUEST error.
  - Only user-defined values are accepted for market protection.
- **Quantity & Product Types**

  - Ensure correct lot sizes for derivatives and F&O instruments.
  - Verify product types (C, M, I) before order placement.
- **Error Handling**

  - One invalid leg may result in basket order validation failure.
  - Validate trading symbols and exchanges before placing requests.
- **Exchange Restrictions**

  - Certain symbols are valid only on specific exchanges.
  - Validate symbols against the latest master contract files.
- **Special Character Symbols**

  - If a trading symbol contains special characters, use URL encoding.
  - Example: L&TFH-EQ should be sent as L%26TFH-EQ.

## **Conclusion**

The Basket Order API is designed for advanced trading workflows where multiple orders need to be executed together in a single request. By grouping multiple order legs into one API call, developers can efficiently build strategies such as spreads, hedges, and basket-based executions while reducing API overhead and improving execution flow consistency.

For advanced usage, ensure proper validation of trading symbols, product types, and order parameters before submission.
