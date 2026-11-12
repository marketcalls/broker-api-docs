# Cancel Order

> Source: https://firstock.in/api/docs/cancel-order/

> This document provides a comprehensive guide to using the Cancel Order API in the Firstock trading platform.

## Overview

The **Cancel Order API** enables you to invalidate or withdraw a previously placed order that has not yet been fully executed. A successful cancellation ensures that the order will no longer be processed by the exchange or affect your account’s margin or position.

**Key benefits:**

- **Prevent Unwanted Executions**: Stop an order if market conditions change or if the user changes their mind.
- **Real-Time Risk Management**: Free up allocated margin or correct erroneous orders.
- **Simple Integration**: Minimal parameters needed—primarily the order number and session token.

## Endpoint & Method

`POST` `/cancelOrder`

**URL**:

```
https://api.firstock.in/V1/cancelOrder
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the JSON body for the **Cancel Order API** request. All fields marked as **Mandatory** must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| orderNumber | string | Yes | The unique identifier of the order you wish to cancel. | "24121300003425" |

**Request:**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}",
  "orderNumber": "24121300003425"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/cancelOrder' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}",
    "orderNumber": "24121300003425"
}'
```

**Python**

```python
from firstock import firstock
cancelOrder = firstock.cancelOrder(
    userId= "{{userId}}",
    orderNumber="25063000011862"
)
print(cancelOrder)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
const cancelOrder = (orderNumber) => {
  firstock.cancelOrder(
    { userId:  "{{userId}}", orderNumber: '25070100010584' },
    (err, result) => {
      console.log("cancelOrder Error, ", err);
      console.log("cancelOrder Result: ", result);
    }
  );
};
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

order_number := "12345678901234"
cancel_order := Firstock.OrderRequest{
		UserId:      "{{userId}}",
		OrderNumber: order_number,
	}
cancelOrder, err := Firstock.CancelOrder(cancel_order)
fmt.Println("Error:", err)
fmt.Println("Result:", cancelOrder)
```

## Response Structure

**Success Response**:

If the request is successful and the order can be cancelled, you will receive a **200 OK** status, with:

- ***status***: Typically *"success"*.
- ***message***: A short description indicating the outcome (e.g., *"Order cancellation details"*).
- ***data***: Contains details about the cancelled order.

**Key Fields within data**:

- ***orderNumber***: The identifier of the order you attempted to cancel.
- ***rejreason***: Reason if the cancellation request partially or fully failed (e.g., if the order was already executed or rejected).
- ***requestTime***: Additional info, such as *"Insufficient Balance"* or other warnings.
- ***requestTime***: Timestamp of when the cancellation request was processed.

**Failure Response**:

If any required field is missing, invalid, or the order can’t be canceled, you may receive a **400** or **401** status code with an error structure:

- **Invalid** ***jKey***: Session expired or incorrect token..
- **Invalid** *orderNumber*: The order might not exist or already be completed.
- **Missing** ***userId***: The system can’t identify which account is requesting cancellation.

**Response**

**200**

```json
{
          "status": "success",
          "message": "Order cancellation details",
          "data": {
             "orderNumber": "25042100011119",
             "rejreason": "SAF:order is not open to cancel",
             "requestTime": "17:59:57 21-04-2025"
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

- **Check Order Status First**

  - Only orders in an “open” state (e.g., pending, partially filled) can usually be canceled. If an order is already fully executed or rejected, cancellation is either unnecessary or will fail.
- **Store orderNumber**

  - Keep track of the orderNumber from the **Place Order API** or **Order Book** response. This is essential for cancellation.
- **Session Validity**

  - Ensure that *jKey* is valid. If *"INVALIDJKEY"* appears, prompt a re-login or refresh the token as needed.
- **Error Handling**

  - If you receive a reason like *"SAF: order is not open to cancel"*, it typically means the order can’t be canceled at its current status. Inform users accordingly.
- **Timing & Partial Fills**

  - An order might have partial fills between the time you decide to cancel and when the system processes your request. Always confirm the updated status via an **Order Book** call post-cancellation.

## **Conclusion**

The **Cancel Order API** is essential for managing risk and flexibility within your trading application. By canceling an active order that no longer aligns with your strategy or market conditions, you can prevent undesired fills and maintain more precise control over your positions. Always verify order status and ensure you have a valid session token for reliable cancellation requests.
