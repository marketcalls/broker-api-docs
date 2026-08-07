# Product Conversion

> Source: https://firstock.in/api/docs/product-conversion/

> This document explains how to use the Product Conversion API on the Firstock trading platform.

## Overview

The **Product Conversion API** enables traders to modify the product type for a position already held in their account. Typical use cases include carrying over an intraday position to the next trading day or converting a delivery position to intraday if permitted by the exchange and broker.

**Key benefits:**

- **Flexibility**: Adapt your trading strategy by converting product types without closing and reopening positions.
- **Margin Optimization**: Optimize or free up margins by moving between intraday (MIS) and delivery (CNC) products.
- **Reduced Operational Overhead**: No need to square off and re-enter a new position just to switch product types.

## Endpoint & Method

`POST` `/productConversion`

**URL**:

```
https://api.firstock.in/V1/productConversion
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is a sample JSON body for the **Product Conversion API** request. All fields marked **Mandatory** must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| product | string | Yes | Product type (e.g., "C", "M", "I"). | "C" |
| tradingSymbol | string | Yes | Symbol or instrument identifier (e.g., "IDEA-EQ", "NIFTY06MAR25C22500"). | "IDEA-EQ" |
| exchange | string | Yes | Exchange code ("NSE", "BSE", "NFO", etc.). | "NSE" |
| previousProduct | string | No (depends on priceType) | Current product type (e.g., "M" for MIS, "C" for CNC). | "C" |
| quantity | string (optional) | Yes if SL order | Number of shares or lots to trade. | "1" |
| msgFlag | string (optional) | Yes if not Buy and Day | This parameter specifies the side (Buy/Sell) and position type (Day/CF) for the conversion. | "1","2","3","4" |

**Note:**

**msgFlag -**This parameter specifies the**side (Buy/Sell)** and**position type (Day/CF)** for the conversion.

| Value | Meaning |
|---|---|
| "1" | Buy and Day |
| "2" | Buy and CF |
| "3" | Sell and Day |
| "4" | Sell and CF |

**Request:**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}",
  "tradingSymbol": "IDEA-EQ",
  "exchange": "NSE",
  "previousProduct": "C",
  "product": "I",
  "quantity": "1",
  "msgFlag": "1"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/productConversion' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}",
    "tradingSymbol": "IDEA-EQ",
    "exchange": "NSE",
    "previousProduct": "C",
    "product": "I",
    "quantity": "1",
    "msgFlag": "1"
}'
```

**Python**

```python
from firstock import firstock
convertProduct = firstock.productConversion(
    userId="{{userId}}",
    transactionType="B",
    tradingSymbol="ITC-EQ",
    quantity="1",
    product="C",
    previousProduct="I",
    positionType="DAY",
    exchange="NSE"
)
print(convertProduct)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.productConversion(
  {
    userId: "{{userId}}",
    exchange: "NFO",
    tradingSymbol: "NIFTY",
    quantity: "250",
    product: "C",
    previousProduct: "I"
  },
  (err, result) => {
    console.log("productConversion Error, ", err);
    console.log("productConversion Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

productConversionRequest := Firstock.ProductConversionRequest{
		UserId:          "{{userId}}",
		TradingSymbol:   "AVANCE",
		Exchange:        "BSE",
		PreviousProduct: "I", // B = Buy, S = Sell
		Product:         "C", // C = Delivery, I = Intraday, M = Margin Intraday (MIS)
		Quantity:        "1", // As string
	}

productConversion, err := Firstock.ProductConversion(productConversionRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", productConversion)
```

## Response Structure

**Success Response**:

If the position is successfully converted, you’ll receive a **200 OK** status, with:

- ***status***: *"success"*.
- ***message***: Indicates conversion result (e.g., *"Partial position conversion info fetched"*).
- ***data***: Contains additional details or remarks about the conversion.

**Key Fields in data**:

- ***Status***: A note indicating whether the conversion succeeded or why it was restricted.
- ***requestTime***: Timestamp of the conversion request.

**Failure Response**:

If a required field is missing, invalid, or if the conversion cannot occur, you may receive a **400** or **401** status code:

- **Invalid** ***jKey***: Session may be expired or token is incorrect.
- **Unsupported Conversion**: Certain product types may not be convertible under specific rules.
- **Insufficient Quantity**: You cannot convert more shares/lots than you currently hold.
- **Time Restrictions**: Conversion may be disallowed after a certain time or if the market is closed.

**Response**

**200**

```json
{
          "status": "success",
          "message": "Partial position conversion info fetched",
          "data": {
            "Status": "RED:Product Conversions are disallowed after system square off",
            "requestTime": "18:27:50 21-04-2025"
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

- **Check Position Book First**

  - Verify the current *product*type and available *quantity* in your position before attempting conversion.
- **Partial Conversion**

  - If the API supports partial conversions, ensure *quantity*does not exceed the position size. Otherwise, the request may fail.
- **Session Token Validity**

  - *jKey*must be current. If you see an *INVALID_JKEY*error, prompt the user to log in again.
- **Exchange & Product Rules**

  - Different exchanges may have their own guidelines. Some product conversions might not be supported in certain segments (e.g., F&O vs. equities).
- **Order of Operations**

  - Make sure you’re not trying to convert a position that’s pending in the Order Book (e.g., partially filled or in the process of being squared off).

## **Conclusion**

The **Product Conversion API** provides crucial flexibility for traders who need to switch between product types due to changing market conditions or margin requirements. Always confirm your current holdings, validate session tokens, and check for any conversion restrictions (like late market hours or broker policies) before calling this endpoint.
