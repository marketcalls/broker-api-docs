# Order Book

> Source: https://firstock.in/api/docs/order-book/

> This document explains how to use the Order Book API on the Firstock trading platform.

## Overview

The **Order Book API** provides a consolidated list of orders that have been placed by the user. It returns both open and closed orders, along with their statuses (e.g., *"REJECTED"*, *"FILLED"*,*"OPEN"*), quantities, and timestamps. This information is essential for tracking and managing active trades in your application.

**Key benefits:**

- **Real-Time Order Tracking**: View open, pending, and completed orders.
- **Detailed Order Info**: Retrieve average prices, filled quantities, reject reasons, and more.
- **Streamlined Management**: Quickly check which orders may need modification or cancellation.

## Endpoint & Method

`POST` `/orderBook`

**URL**:

```
https://api.firstock.in/V1/orderBook
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the JSON body for the **Order Book API** request. All fields marked as **Mandatory** must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
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
curl --location 'https://api.firstock.in/V1/orderBook' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}"
}'
```

**Python**

```python
from firstock import firstock
orderBook = firstock.orderBook(userId="{{userId}}")
print(orderBook)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.orderBook(
  { userId:  "{{userId}}"},
  (err, result) => {
    console.log("orderBook Error, ", err);
    console.log("orderBook Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

orderBookDetails, err := Firstock.OrderBook("{{userId}}")
fmt.Println("Error:", err)
fmt.Println("Result:", orderBookDetails)
```

## Response Structure

**Success Response**:

f the request is valid and your session token (*jKey*) has not expired, you will receive a **200 OK** status, with an object containing:

- **status**: Typically *"success"*.
- **message**: A brief note, e.g., *"Order book"*.
- **data**: An object (or array) containing a list of orders.

**Key Fields for Each Order**:

- **orderNumber**: Unique ID for the order.
- **exchange**: Exchange code (*"NSE"*, *"BSE"*, *"NFO"*, etc.).
- **transactionType**: *"B"* (Buy) or *"S"* (Sell).
- **priceType**: *"MKT"*, *"LMT"*, etc.
- **quantity**: Number of shares or lots.
- **status**: Current state (e.g., *"REJECTED"*, *"FILLED"*, *"OPEN"*).
- **rejectReason**: If the order was rejected, describes the cause.
- **remarks**: Additional notes or user comments.

**Failure Response**:

If any required field is missing, invalid, or the order can’t be canceled, you may receive a **400** or **401** status code with an error structure:

Common error reasons include:

- **Invalid *jKey***: The session may be expired, prompting re-login.
- **Missing *userId***: he API cannot identify which account’s orders to fetch.

**Response**

**200**

```json
{
          "status": "success",
          "message": "Order book",
          "data": [
            {
              "averagePrice": "0.00",
              "exchange": "NSE",
              "fillShares": "",
              "lotSize": "1",
              "orderNumber": "25043000013102",
              "orderTime": "1746004054",
              "price": "0.00",
              "priceType": "MKT",
              "product": "C",
              "quantity": "13",
              "rejectReason": "RED:RULE:{Check Holdings Including BTST except t2t}No
                               Holdings uploaded for C-GH1695 [ONLINE]",
              "remarks": "",
              "retention": "DAY",
              "status": "REJECTED",
              "tickSize": "0.01",
              "token": "14366",
              "tradingSymbol": "IDEA-EQ",
              "transactionType": "S",
              "userId": "AB1234"
            },
            {
              "averagePrice": "0.00",
              "exchange": "NSE",
              "fillShares": "",
              "lotSize": "1",
              "orderNumber": "25043000007328",
              "orderTime": "1745989668",
              "price": "0.00",
              "priceType": "MKT",
              "product": "C",
              "quantity": "5",
              "rejectReason": "RED:Margin Shortfall:INR 4,301.68 Available:INR
                               77.09 for C-GH1695 [ONLINE]",
              "remarks": "",
              "retention": "DAY",
              "status": "REJECTED",
              "tickSize": "0.05",
              "token": "6705",
              "tradingSymbol": "PAYTM-EQ",
              "transactionType": "B",
              "userId": "AB1234"
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
      "message": "JKey is required"
    }
  }
```

## Usage & Best Practices

- **Session Token Validity**

  - Always verify that your *jKey* (or *susertoken*) is current. If you encounter *INVALIDJKEY*, prompt the user to log in again.
- **Check Order Status**

  - The *status* field tells you if an order is pending, filled, partially filled, or rejected. Use this to update user interfaces or trigger post-trade actions.
- **Reject Reason Analysis**

  - If many orders show *"REJECTED"*, review *rejectReason* fields to troubleshoot issues (e.g., product restrictions, insufficient margin).
- **Pagination (If Needed)**

  - For high-activity accounts, the order book can grow large. If the endpoint supports pagination, consider implementing it to avoid performance issues.
- **Real-Time vs. Polling**

  - The Order Book API reflects the state of orders at the time of request. For real-time updates, consider using WebSocket streams if available, or poll at controlled intervals.

## **Conclusion**

The **Order Book API** is crucial for monitoring user trades within the Firstock environment. By calling this endpoint, you gain a real-time snapshot of all orders, their statuses, and any reasons for rejections. Incorporate this data into your trading dashboards or back-office tools to streamline order management and enhance user visibility.
