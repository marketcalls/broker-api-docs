# Modify After Market Order (AMO)

> Source: https://firstock.in/api/docs/modify-after-market-order-amo/

> This document provides a detailed overview of the **Modify After Market Order (AMO)** API for the Firstock trading platform. This endpoint allows you to update the parameters of a pending AMO before the market opens.

## Overview

The **Place Order API** allows authenticated clients to create new orders. Depending on the specified parameters (e.g., price type, product type), it can handle multiple order scenarios, such as limit orders, market orders, and stop-loss orders.

**Key benefits:**

- **Versatile Order Types**: Supports market, limit, and SL-based orders.
- **Broad Exchange Coverage**: Place trades on NSE, BSE, NFO, and more.
- **Seamless Integration**: Easily incorporate order placement into your trading application’s workflow.

## Endpoint & Method

`POST` `/modifyAfterMarketOrder`

**URL**:

```
https://api.firstock.in/V1/modifyAfterMarketOrder
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

The following fields must be sent in the JSON body. All values must be strictly in string format.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Your Firstock account ID. | AB1234 |
| orderNumber | string | Yes | The original Noren Order Number received during placement. | 26030400001234 |
| quantity | string | Yes | New number of shares or lots. | "50" |
| price | string | Yes | New limit price in Rupees. (Set "0" for MKT). | "9.10" |
| priceType | string | Yes | "LMT", "MKT", "SL-LMT", "SL-MKT". | "LMT" |
| product | string | Yes | Product type ("C", "M", "I"). | "C" |
| mkt_protection | string | No (Yes - MKT/SL-MKT PriceType) | Percentage of market protection to be applied on orders | “1”,”0.1” |
| triggerPrice | string | No | New trigger price in Rupees. | "9.00" |

**Request:**

```json
 {
    "userId": "NP2997",
    "jKey": "af4dbecbf49c73ad362369be50b95369b83a31d064ef0779d9c64c460c5e5cb0",
    "orderNumber": "26030400001234",
    "quantity": "50",
    "price": "9.10",
    "priceType": "LMT",
    "product": "C",
    "mkt_protection":"1",
    "triggerPrice": "9.00"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/modifyAMO' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "NP2997",
    "jKey": "af4dbecbf49c73ad362369be50b95369b83a31d064ef0779d9c64c460c5e5cb0",
    "orderNumber": "26030400001234",
    "quantity": "50",
    "price": "9.10",
    "priceType": "LMT",
    "product": "C",
    "mkt_protection":"1",
    "triggerPrice": "9.00"
}'
```

**Python**

```python
from firstock import firstock

modifyAMO = firstock.modifyAMO(
    userId="{{userId}}",
    orderNumber="26030400001234",
    quantity="20",
    price="305",
    product="I",
    priceType="LMT",
    retention="DAY",
    mkt_protection="1",
    triggerPrice="302"
)
print(modifyAMO)
```

**Nodejs**

```javascript
const { Firstock } = require("firstock");
const firstock = new Firstock();

firstock.modifyAMO(
  {
    userId: "{{userId}}",
    orderNumber: "26030400001234",
    quantity: "50",
    price: "7.15",
    product: "C",
    priceType: "LMT",
    mkt_protection:"1",
    triggerPrice: "7.05",
  },
  (err, result) => {
    console.log("Modify AMO Result: ", result);
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
    modifyAMORequest := Firstock.ModifyOrderRequest{
        UserId:          "{{userId}}",
        OrderNumber:     "26030400001234",
        Exchange:        "BSE",
        TradingSymbol:   "SAWACA",
        Quantity:        "10",
        Price:           "0.45",
        PriceType:       "LMT",
        Product:         "C",
        TransactionType: "B",
        Retention:       "DAY",
        Mkt_protection: "0.5",
        TriggerPrice:    "0.43",
    }

    modifyAMO, err := Firstock.ModifyAMO(modifyAMORequest)
    fmt.Println("Result:", modifyAMO)
}
```

## Response Structure

**Success Response (200 OK)**:

If the order is modified successfully, you will receive a **200 OK** status with a JSON object containing:

- ***status***: Typically *"success"*.
- ***message***: Brief description of the outcome (e.g., "Order details").
- ***data***: An object with information about the newly modified order.

**Key Fields in the data object:**:

- ***orderNumber***:A unique identifier for this order.
- ***requestTime***: Timestamp when the modification request was processed.

**Failure Response**:

If the request is malformed or any required field is missing/invalid, you may receive a 400, 401 status code with details such as:

- **status**: ***failed***.
- **code**: Error code (e.g., "**400**", "**401**").
- **name** : A brief descriptor (e.g., "**BAD_REQUEST**", "**UNAUTHORIZED**", "**SERVICE_UNAVAILABLE**")
- **error**: An object or string indicating which field caused the issue and why.

**Response**

**200**

```json
{
    "status": "success",
    "message": "Order details",
    "data": {
      "orderNumber": "26030400001234",
      "requestTime": "10:15:22 04-03-2026"
    }
}
```

**400**

```json
{
    "status": "failed",
    "code": 400,
    "name": "BAD_REQUEST",
    "error": {
        "field": "orderNumber",
        "message": "The order number provided is invalid or has already been executed."
    }
}
```

## Usage & Best Practices

- **Market Protection (mkt_protection)**

  - When priceType is MKT, SL-MKT the **mkt_protection** field is required and must be greater than 0.
  - **MKT** orders are converted to **LMT** with a price derived from the best bid/ask (or LTP) adjusted by the **mkt_protection** percentage.
  - If **mkt_protection** is missing or ≤ 0 for these order types, the API returns a **400 BAD_REQUEST** error.

## **Conclusion**

The **Modify After Market Order (AMO) API** is a core feature for building trading applications on the Firstock platform. By combining the correct parameters for price type, product type, and quantity, you can execute various trading strategies across multiple exchanges. For advanced features like **stop-loss orders** or **bracket orders**, adjust the relevant fields (priceType, triggerPrice) accordingly. If you encounter persistent errors, consult the official Firstock documentation or support.
