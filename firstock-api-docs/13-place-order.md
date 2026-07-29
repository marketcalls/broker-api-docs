# Place Order

> Source: https://firstock.in/api/docs/place-order/

> This document provides a detailed overview of the Place Order API for the Firstock trading platform.

## Overview

The **Place Order API** allows authenticated clients to create new orders. Depending on the specified parameters (e.g., price type, product type), it can handle multiple order scenarios, such as limit orders, market orders, and stop-loss orders.

**Key benefits:**

- **Versatile Order Types**: Supports market, limit, and SL-based orders.
- **Broad Exchange Coverage**: Place trades on NSE, BSE, NFO, and more.
- **Seamless Integration**: Easily incorporate order placement into your trading application’s workflow.

## Endpoint & Method

`POST` `/placeOrder`

**URL:**

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the general JSON body for the **Place Order API** request. Fields marked as **Mandatory** must be included.

```
https://api.firstock.in/V1/placeOrder
```

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| exchange | string | Yes | Name of the exchange ("NSE", "BSE", "NFO", etc.). | "NSE" |
| retention | string | Yes | Indicates the order’s validity period (e.g., "DAY", "IOC"). | "DAY" |
| product | string | Yes | Product type (e.g., "C", "M", "I"). | "C" |
| priceType | string | Yes | Pricing model: e.g., "MKT", "LMT", "SL-LMT", "SL-MKT". | "MKT" |
| tradingSymbol | string | Yes | Symbol or instrument identifier (e.g., "IDEA-EQ", "NIFTY06MAR25C22500"). | "IDEA-EQ" |
| mkt_protection | string | No (Yes - MKT/SL-MKT PriceType) | Percentage of market protection to be applied on orders | “1”,”0.1” |
| transactionType | string | Yes | "B" (Buy) or "S" (Sell). | "B" |
| price | string | Yes | Limit price for limit orders, or 0 for market orders. | "0" (for MKT order) |
| triggerPrice | string (optional) | No | Trigger price for stop-loss orders. For non-SL orders, set this to 0. | "0" |
| quantity | string | Yes | Number of shares or lots to trade. | "1" |
| remarks | string | Yes | Optional comment or reason for the order. | "Test" |

**Request:**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}",
  "exchange": "NSE",
  "retention": "DAY",
  "product": "C",
  "priceType": "MKT",
  "tradingSymbol": "IDEA-EQ",
  "mkt_protection":"1",
  "transactionType": "B",
  "price": "0",
  "triggerPrice": "0",
  "quantity": "1",
  "remarks": "Test"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/placeOrder' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}",
    "exchange": "NSE",
    "retention": "DAY",
    "product": "C",
    "priceType": "MKT",
    "tradingSymbol": "IDEA-EQ",
    "mkt_protection":"1",
    "transactionType": "B",
    "price": "0",
    "triggerPrice": "0",
    "quantity": "1",
    "remarks": "Test"
}'
```

**Python**

```python
from firstock import firstock
placeOrder = firstock.placeOrder(
    userId="{{userId}}",
    exchange="NSE",
    tradingSymbol="ITC-EQ",
    quantity="1",
    price="300",
    product="I",
    mkt_protection="1",
    transactionType="B",
    priceType="LMT",
    retention="DAY",
    triggerPrice="0",
    remarks="Python Package Order"
)
print(placeOrder)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock")
const firstock = new Firstock();
firstock.placeOrder(
  {
    userId: "{{userId}}",
    exchange: "NSE",
    tradingSymbol: "IDEA-EQ",
    quantity: "1",
    price: "7.00",
    product: "C",
    mkt_protection:"1",
    transactionType: "B",
    priceType: "LMT",
    retention: "DAY",
    triggerPrice: "0",
    remarks: "Add market protection",
  },
  (err, result) => {
    console.log("placeOrder Error, ", err);
    console.log("placeOrder Result: ", result);
    }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

placeOrderRequest := Firstock.PlaceOrderRequest{
		UserId:          "{{userId}}",
		Exchange:        "BSE",
		Retention:       "DAY",
		Product:         "C",
		PriceType:       "LMT",
		TradingSymbol:   "SAWACA",
        Mkt_protection: "0.5",
		TransactionType: "B",
		Price:           "0.42",
		TriggerPrice:    "0.40",
		Quantity:        "1",
		Remarks:         "Test Order",
	}
placeOrder, err := Firstock.PlaceOrder(placeOrderRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", placeOrder)
```

**Note:** If a trading Symbol consists of a special symbol, please use the [URL encoding](https://www.w3schools.com/tags/ref_urlencode.ASP?ref=wikiconnect.thefirstock.com). example: L&TFH-EQ should be sent as L%26TFH-EQ

## Response Structure

**Success Response:**

If the order is placed successfully, you will receive a **200 OK** status with a JSON object containing:

- ***status***: Typically *"success"*.
- ***message***: Brief description of the outcome (e.g., *"Order details"*).
- ***data***: An object with information about the newly placed order.

**Key Fields in the data object**:

- ***orderNumber***: A unique identifier for this order.
- ***requestTime***: Timestamp when the order was processed.

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
     "message": "Order details",
    "data": {
      "orderNumber": "25042100011119",
      "requestTime": "17:50:52 21-04-2025"
      }
  }
```

**200(Sliced Orders)**

```json
{
    "status": "success",
    "message": "Order details",
    "data": [
        {
            "orderNumber": "26033100000012",
            "quantity": "1755",
            "requestTime": "04:16:00 31-03-2026"
        },
        {
            "orderNumber": "26033100000009",
            "quantity": "1755",
            "requestTime": "04:16:00 31-03-2026"
        },
        {
            "orderNumber": "26033100000010",
            "quantity": "1755",
            "requestTime": "04:16:00 31-03-2026"
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
      "field": "exchange",
      "message": "required field is empty or missing: exchange"
    }
  }
```

## Usage & Best Practices

- **Market Protection (mkt_protection)**

  - When priceType is MKT, SL-MKT the **mkt_protection** field is required and must be greater than 0.
  - **MKT** orders are converted to **LMT** with a price derived from the best bid/ask (or LTP) adjusted by the **mkt_protection** percentage.
  - If **mkt_protection** is missing or ≤ 0 for these order types, the API returns a **400 BAD_REQUEST** error.
- **Order Slicing (Freeze Quantity)**

  - Orders exceeding the exchange-defined freeze **quantity** are automatically sliced into multiple sub-orders.
  - The freeze quantity is adjusted to the nearest lower multiple of the instrument's lot size.
  - A maximum of 10 slices is allowed per order, otherwise the API returns a **400 BAD_REQUEST** error.
  - Orders within the freeze quantity limit are placed as a single order with no change in behavior.
- **Order Number Tracking**

  - Store the *orderNumber* returned upon success. You’ll need it to modify, cancel, or check the status of the order later.
- **Price & Trigger Price**

  - If placing a market order, ensure *price* = *0* and *priceType* = *"MKT"*.
  - If placing a **stop-loss** order, set *triggerPrice* to the desired trigger price and priceType to *"SL-LMT"* or *"SL-MKT"*.
- **Quantity & Product Types**

  - Double-check the **product** type (*"C"*, *"I"*, *"M"*, etc.) to match your trading strategy.
  - Ensure the **quantity** is correct (consider lot sizes for F&O instruments).
- **Error Handling**

  - On failure, use the *field* and *message* in the response to debug. Missing or incorrect fields (like *exchange* or *tradingSymbol*) are common mistakes.
- **User Session**

  - The *jKey* must be valid. If you receive an error like *"INVALIDJKEY"*, your session may have expired; prompt a re-login.
- **Exchange Restrictions**

  - Some symbols are only valid on specific exchanges. Validate against your symbol master files or the provided symbol lists to avoid errors.

## Conclusion

The **Place Order API** is a core feature for building trading applications on the Firstock platform. By combining the correct parameters for price type, product type, and quantity, you can execute various trading strategies across multiple exchanges. For advanced features like **stop-loss orders** or **bracket orders**, adjust the relevant fields (*priceType*, triggerPrice) accordingly. If you encounter persistent errors, consult the official Firstock documentation or support.
