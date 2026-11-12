# Place After Market Order (AMO)

> Source: https://firstock.in/api/docs/place-after-market-order-amo/

> This document provides a detailed overview of the **Place After Market Order (AMO)** API for the Firstock trading platform. This endpoint is designed for placing orders outside of regular market hours.

## Overview

The **Place Order AMO API** allows authenticated clients to create new orders. Depending on the specified parameters (e.g., price type, product type), it can handle multiple order scenarios, such as limit orders, market orders, and stop-loss orders.

**Key benefits:**

- **Versatile Order Types**: Supports market, limit, and SL-based orders.
- **Broad Exchange Coverage**: Place trades on NSE, BSE, NFO, and more.
- **Seamless Integration**: Easily incorporate order placement into your trading application’s workflow.

## Endpoint & Method

`POST` `/placeAfterMarketOrder`

**URL**:

```
https://api.firstock.in/V1/placeAfterMarketOrder
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the JSON body for the request. All fields must be sent as **strings**

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| exchange | string | Yes | Exchange name ("NSE", "BSE", "NFO", etc.). | "NSE" |
| retention | string | Yes | Order validity (Default: "DAY"). | "DAY" |
| product | string | Yes | Product type (e.g., "C" for CNC, "I" for MIS). | "C" |
| priceType | string | Yes | Pricing model: "LMT", "MKT", "SL-LMT". | "LMT" |
| tradingSymbol | string | Yes | Instrument identifier. | "RELIANCE-EQ" |
| mkt_protection | string | No (Yes - MKT/SL-MKT PriceType) | Percentage of market protection to be applied on orders | “1”,”0.1” |
| transactionType | string | Yes | "B" (Buy) or "S" (Sell). | "B" |
| price | string | Yes | Limit price in Rupees. (e.g., "150.50"). | "150.50" |
| triggerPrice | string | No | rigger price in Rupees. | "145.00" |
| quantity | string | Yes | Number of shares/lots. | "10" |
| remarks | string | No | Optional order comment | "After hours trade" |

**Request:**

```json
{
  "userId": "AB1234",
  "jKey": "session_token_here",
  "exchange": "NSE",
  "retention": "DAY",
  "product": "C",
  "priceType": "LMT",
  "tradingSymbol": "IDEA-EQ",
  "mkt_protection":"1",
  "transactionType": "B",
  "price": "8.9",
  "triggerPrice": "0",
  "quantity": "100",
  "remarks": "AMO Test"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/placeAMO' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}",
    "exchange": "NSE",
    "retention": "DAY",
    "product": "C",
    "priceType": "LMT",
    "tradingSymbol": "IDEA-EQ",
    "mkt_protection":"1",
    "transactionType": "B",
    "price": "8.90",
    "triggerPrice": "0",
    "quantity": "1",
    "remarks": "AMO Order"
}'
```

**Python**

```python
from firstock import firstock

placeAMO = firstock.placeAMO(
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
    remarks="Python Package AMO"
)

print(placeAMO)
```

**Nodejs**

```javascript
const { Firstock } = require("firstock");
const firstock = new Firstock();

firstock.placeAMO(
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
    remarks: "NodeJS AMO Order",
  },
  (err, result) => {
    if (err) {
        console.log("AMO Error: ", err);
    } else {
        console.log("AMO Result: ", result);
    }
  }
);
```

**Golang**

```go
import (
    "fmt"
    "github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

func main() {
    placeAMORequest := Firstock.PlaceOrderRequest{
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
        Remarks:         "Golang AMO Order",
    }

    placeAMO, err := Firstock.PlaceAMO(placeAMORequest)

    fmt.Println("Error:", err)
    fmt.Println("Result:", placeAMO)
}
```

## Response Structure

**Success Response (200 OK)**:

If the **After Market Order (AMO)** is placed successfully, you will receive a **200 OK** status. The logic ensures that even if there is a slight delay in the backend, the API will attempt to retrieve the order number from the order book or Redis before responding.

- ***status***: Typically *"success"*.
- ***message***: Brief description of the outcome (e.g., *"Order details"*).
- ***data***: An object containing the processed order details.

**Key Fields in the data object**:

- ***orderNumber***: A unique identifier for the placed order (Noren Order Number)..
- ***requestTime***: The timestamp when the order was processed, formatted as **HH:MM:SS DD-MM-YYYY**.

**Failure Response (400/401)**:

If the request is malformed, authentication fails, or the downstream gRPC service is unavailable, you will receive a failure response.

- **status**: ***failed***.
- **code**: The HTTP status code (e.g., "**400**", "**401**").
- **name** : A brief descriptor of the error category (e.g., "**BAD_REQUEST**", "**UNAUTHORIZED**", "**SERVICE_UNAVAILABLE**")
- **error**: An object or string indicating which field caused the issue and a descriptive error message.

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
    "code": 400,
    "name": "BAD_REQUEST",
    "error": {
        "field": "price",
        "message": "Invalid price format. Must be a numeric string."
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
- **Mandatory Defaults**

  - If you send an empty `retention` field, it will default to `"DAY"`. ordersource is always mapped to `"API"`
- **Numeric Fields**

  - Even though fields like `price` and `quantity` represent numbers, they **must** be sent as strings in the JSON payload to ensure strict parsing.

## **Conclusion**

The **Place After Market Order (AMO) API** is a vital component for developers building comprehensive trading applications on the Firstock platform. It bridges the gap between market sessions, allowing users to plan and queue their trades with confidence while the exchange is closed.
