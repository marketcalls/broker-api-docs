# Basket Margin

> Source: https://firstock.in/api/docs/basket-margin-2/

> This document explains how to use the Basket Margin API within the Firstock trading platform.

## Overview

The **Basket Margin API** allows you to calculate the required margin for a group of orders submitted together. Rather than checking each order individually, you can see the net effect of multiple buys and sells—particularly useful for complex strategies like spreads or baskets of stocks.

**Key benefits:**

- **Unified Margin Check**: Evaluate multiple orders at once.
- **Risk Management**: Avoid partial rejections by confirming you have enough margin for the entire basket.
- **Efficiency**: Cuts down on repeated margin checks for each order in complex trading scenarios.

## Endpoint & Method

`POST` `/basketMargin`

**URL**:

```
https://api.firstock.in/V1/basketMargin
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is a sample JSON body for the **Basket Margin API** request. Fields marked **Mandatory** must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| exchange | string | Yes | Exchange code ("NSE", "BSE", "NFO", etc.). | "NSE" |
| transactionType | string | Yes | "B" (Buy) or "S" (Sell) for the first order. | "B" |
| product | string | Yes | Product type (e.g., "C", "M", "I"). | "C" |
| tradingSymbol | string | Yes | Symbol or instrument identifier (e.g., "IDEA-EQ", "NIFTY06MAR25C22500"). | "IDEA-EQ" |
| quantity | string | Yes | Number of shares or lots to trade. | "1" |
| priceType | string | Yes | Pricing model ("MKT", "LMT", etc.) for the first order. | "MKT" |
| price | string | Yes | Limit price or 0 if priceType is "MKT". | "0" |
| BasketList_Params | array of objects | Yes | An array of additional orders, each with the same fields as above (exchange, transactionType, etc.). | See example below |

**Request:**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}",
  "exchange": "NSE",
  "transactionType": "B",
  "product": "C",
  "tradingSymbol": "RELIANCE-EQ",
  "quantity": "1",
  "priceType": "MKT",
  "price": "0",
  "BasketList_Params": [
    {
      "exchange": "NSE",
      "transactionType": "B",
      "product": "C",
      "tradingSymbol": "IDEA-EQ",
      "quantity": "1",
      "priceType": "MKT",
      "price": "0"
    }
  ]
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/basketMargin' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}",
    "exchange": "NSE",
    "transactionType": "B",
    "product": "C",
    "tradingSymbol": "RELIANCE-EQ",
    "quantity": "1",
    "priceType": "MKT",
    "price": "0",
    "BasketList_Params": [
        {
            "exchange": "NSE",
            "transactionType": "B",
            "product": "C",
            "tradingSymbol": "IDEA-EQ",
            "quantity": "1",
            "priceType": "MKT",
            "price": "0"
        }
    ]
}'
```

**Python**

```python
from firstock import firstock
basketMargin = firstock.basketMargin(
    userId="{{userId}}",
    exchange="NSE",
    transactionType="B",
    product="C",
    tradingSymbol="RELIANCE-EQ",
    quantity="1",
    priceType="MKT",
    price="0",
    BasketList_Params=[
        {
            "exchange": "NSE",
            "tradingSymbol": "IDEA-EQ",
            "quantity": "1",
            "transactionType": "B",
            "price": "0",
            "product": "C",
            "priceType": "MKT"
        }
    ]
)
print(basketMargin)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.basketMargin(
  {
    userId: "{{userId}}",
    exchange: "NSE",
    transactionType: "B",
    product: "C",
    tradingSymbol: "RELIANCE-EQ",
    quantity: "1",
    priceType: "MKT",
    price: "0",
    BasketList_Params: [
      {
        exchange: "NSE",
        transactionType: "B",
        product: "C",
        tradingSymbol: "IDEA-EQ",
        quantity: "1",
        priceType: "MKT",
        price: "0"
      }
    ],
  },
  (err, result) => {
    console.log("basketMargin Error, ", err);
    console.log("basketMargin Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

basketMarginRequest := Firstock.BasketMarginRequest{
		UserId:          "{{userId}}",
		Exchange:        "NSE",
		TransactionType: "B",           // B = Buy, S = Sell
		Product:         "C",           // C = Delivery, I = Intraday, M = Margin Intraday (MIS)
		TradingSymbol:   "RELIANCE-EQ", // Ensure it's the correct symbol
		Quantity:        "1",           // As string
		PriceType:       "MKT",         // Example: "LMT" for Limit, "MKT" for Market
		Price:           "0",           // As string
		BasketListParams: []Firstock.BasketListParam{
			{
				Exchange:        "NSE",
				TransactionType: "B",
				Product:         "C",
				TradingSymbol:   "IDEA-EQ",
				Quantity:        "1",
				PriceType:       "MKT",
				Price:           "0",
			},
		},
	}

basketMargin, err := Firstock.BasketMargin(basketMarginRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", basketMargin)
```

## Response Structure

**Success Response**:

On a valid request, the API returns a **200 OK** status and a JSON object containing:

- ***status***: Typically *"success"*.
- ***message***: Short description (e.g., *"Fetched basket margin successfully"*)
- ***data***: Object with margin calculation details.

**Key Fields within data**:

- ***BasketMargin***: An array with various margin metrics for the combined orders.
- ***MarginOnNewOrder***: The total additional margin required if you were to place this basket now.
- ***PreviousMargin***: The margin used before factoring in the new basket.
- ***TradedMargin***: The updated total margin usage after this basket is accounted for.
- ***Remarks***: Additional info or warnings, if any.

**Failure Response**:

If a required field is missing, invalid, or if the conversion cannot occur, you may receive a **400** or **401** status code:

Common error scenarios:

- **Invalid** **or** **expired** ***jKey***
- **Missing** ***userId***
- **Poorly structured** ***BasketListParams***
- **Exchange constraints** (e.g., product not supported for the given exchange)

**Response**

**200**

```json
{
          "status": "success",
          "message": "Fetched basket margin successfully",
          "data": {
            "BasketMargin": [
              126075.6,
              126783.0242,
              2
            ],
            "MarginOnNewOrder": 126783.0242,
            "PreviousMargin": 0,
            "Remarks": "",
            "TradedMargin": 126783.0242
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

- **Pre-Check Before Placing Orders**

  - Always check basket margin beforehand to prevent partial order placements or rejections.
- **Combine with RMS Limit**

  - After obtaining the basket margin, refer to the **Limits API** to ensure you have the needed free margin.
- **Session Token Validity**

  - If *INVALID_JKEY*errors appear frequently, prompt the user to log in again or refresh the session.
- **Detailed Basket Items**

  - Provide accurate *product*, *exchange*, *transactionType*, and *priceType*for each item in *BasketList_Params*to avoid miscalculations.
- **Edge Cases**

  - Some strategies or instruments (like certain derivatives) may require additional margin parameters or might not be fully supported. Verify with Firstock if specialized fields are needed.

## Conclusion

The **Basket Margin API** is essential for traders who execute multi-leg strategies or multiple orders simultaneously. By checking combined margin requirements in one call, you can ensure you have adequate buying power for all planned orders.
