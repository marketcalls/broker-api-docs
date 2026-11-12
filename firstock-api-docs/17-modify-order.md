# Modify Order

> Source: https://firstock.in/api/docs/modify-order/

> This document provides instructions on how to use the Modify Order API within the Firstock trading platform.

## Overview

The **Modify Order API** is a key feature that allows traders to update certain fields of their active orders without having to cancel and re-create them. Typical use cases include changing from a limit order to a different limit price, updating the product type, or increasing/decreasing quantity.

**Key benefits:**

- **Real-Time Adjustments**: Adapt to market movements quickly by modifying open orders.
- **Efficiency**: Avoid the overhead of canceling and placing a new order.
- **Flexibility**: Change price type, trigger price, quantity, and more.

## Endpoint & Method

`POST` `/modifyOrder`

**URL**:

```
https://api.firstock.in/V1/modifyOrder
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the JSON body for the **Modify Order API** request. Fields marked **Mandatory** must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| orderNumber | string | Yes | The unique identifier of the order you wish to modify. | "25042100011120" |
| product | string | Yes | Product type (e.g., "C", "M", "I"). | "C" |
| priceType | string | Yes | Pricing model: e.g., "MKT", "LMT", "SL-LMT", "SL-MKT". | "MKT" |
| tradingSymbol | string | Yes | Symbol or instrument identifier (e.g., "IDEA-EQ", "NIFTY06MAR25C22500"). | "IDEA-EQ" |
| mkt_protection | string | No (Yes - MKT/SL-MKT PriceType) | Percentage of market protection to be applied on orders | “1”,”0.1” |
| price | string | No (depends on priceType) | Limit price for limit orders, or 0 for market orders. | "0" (for MKT order) |
| quantity | string | No | Number of shares or lots to trade. | "1" |
| triggerPrice | string (optional) | Yes if SL order | Trigger price for stop-loss orders (set to 0 if not applicable). | "0" |
| retention | string (optional) | Yes | Order duration if required ("DAY", "IOC"). | "DAY" |

**Request:**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}",
  "orderNumber": "25042100011120",
  "priceType": "LMT",
  "tradingSymbol": "IDEA-EQ",
  "price": "418",
  "exchange":"NSE",
  "triggerPrice": "0",
  "quantity": "1",
  "product": "C",
  "retention": "DAY",
  "mkt_protection": "0.5"
}
```

**Note:**

For MKT orders (priceType: "MKT" / "SL-MKT" / "SL-M"), the mkt_protection and exchange fields are mandatory

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/modifyOrder' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}",
    "orderNumber": "25042100011120",
    "priceType": "LMT",
    "tradingSymbol": "IDEA-EQ",
    "mkt_protection": "0.5"
    "price": "418",
    "triggerPrice": "0",
    "quantity": "1",
    "product": "C",
    "retention": "DAY"
}'
```

**Python**

```python
from firstock import firstock
modifyOrder = firstock.modifyOrder(
    userId= "{{userId}}",
    orderNumber="25070100015934",
    quantity="1",
    price="418",
    triggerPrice="0",
    tradingSymbol="IDEA-EQ",
    priceType="LMT",
    retention = "DAY",
    mkt_protection= "0.5",
    product= "C",
)
print(modifyOrder)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
const modifyOrder = (orderNumber) => {
  firstock.modifyOrder(
    {
      userId: "{{userId}}",
      orderNumber: '25070100010584',
      price: "7.01",
      quantity: "1",
      triggerPrice: "0",
      mkt_protection: "0.5",
      tradingSymbol: "IDEA-EQ",
      exchange: "NSE",
      priceType: "LMT",
      product: "C",
      retention: "DAY"
    },
    (err, result) => {
      console.log("modifyOrder Error, ", err);
      console.log("modifyOrder Result: ", result);
    }
  );
};
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

modify_order := Firstock.ModifyOrderRequest{
	UserId:         "{{userId}}",
	OrderNumber:    "12345678901234",
	PriceType:      "MKT",
	TradingSymbol:  "SAWACA",
	Price:          "",
	TriggerPrice:   "",
	Quantity:       "2",
	Product:        "C",
	Retention:      "DAY",
	Mkt_protection: "0.5",
}
modifyOrder := Firstock.ModifyOrder(modify_order)
fmt.Printf("Modify Order:\n%v\n", modifyOrder)
```

## Response Structure

**Success Response**:

If the order is successfully modified, you will receive a **200 OK** status with a JSON object containing:

- ***status***: Typically *"success"*.
- ***message***: A brief description (e.g., *"Order modification details"*).
- ***data***: Holds the updated order information or any relevant remarks.

**Key Fields within data**:

- ***orderNumber***: The identifier of the order you attempted to cancel.
- ***rejreason***: If the order could not be modified (e.g., already filled or canceled), the reason is listed here.
- ***remarks***: Additional info, such as *"Insufficient Balance"* or other warnings.
- ***requestTime***: Timestamp of when the modify request was processed.

**Failure Response**:

If any required field is missing, invalid, or the order can’t be canceled, you may receive a **400** or **401** status code with an error structure:

- **Invalid** **or** **missing** ***jKey***: *"failed"*.
- **Order not modifiable**: Already fully executed, canceled, or rejected..
- **Parameter mismatch**: e.g., providing a *price* for a market order when *priceType* is *"MKT"*.

**Response**

**200**

```json
{
          "status": "success",
          "message": "Order modification details",
          "data": {
             "orderNumber": "25042100011120",
             "rejreason": "SAF:order is not open to modify",
             "requestTime": "18:07:09 21-04-2025"
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
      "field": "orderNumber",
      "message": "required field is empty or missing: orderNumber"
    }
  }
```

## Usage & Best Practices

- **Market Protection (mkt_protection)**

  - When priceType is MKT, SL-MKT the **mkt_protection** field is required and must be greater than 0.
  - **MKT** orders are converted to **LMT** with a price derived from the best bid/ask (or LTP) adjusted by the **mkt_protection** percentage.
  - If **mkt_protection** is missing or ≤ 0 for these order types, the API returns a **400 BAD_REQUEST** error.
- **Check Order Status**

  - Only “open” orders can typically be modified. If an order is already filled or canceled, the modification request will fail.
- **Partial Fills**

  - For orders partially filled, you can adjust the remaining quantity, but note that already filled shares won’t be affected.
- **Parameter Consistency**

  - Ensure *priceType*, *price*, and *triggerPrice* are logically consistent (e.g., if *priceType* is *"MKT"*, *price* should be *0*).
- **Product & Exchange Rules**

  - Make sure the product type (*"C"*, *"M"*, *"I"*, etc.) is valid for the exchange you’re trading on. Some product types might not be supported everywhere.
- **Retry Logic**

  - If you receive a transient error (e.g., network issues), implement retry logic carefully, ensuring you aren’t duplicating requests.
- **Audit & Logs**

  - Always log your modification attempts (orderNumber, date/time, and changes made) for compliance and debugging.

## **Conclusion**

The **Modify Order API** is pivotal for active traders who need to adjust orders in response to shifting market conditions. By updating price, quantity, or other parameters on the fly, you maintain greater control over your trades. Always validate that the order is still open or partially filled before attempting modifications and ensure session credentials (`jKey`) are current.
