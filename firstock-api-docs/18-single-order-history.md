# Single Order History

> Source: https://firstock.in/api/docs/single-order-history/

> This document provides a detailed guide to using the Single Order History API on the Firstock trading platform.

## Overview

The **Single Order History API** shows each step or fill event for a particular order. This includes timestamps, fill quantities, average prices, and rejection reasons if applicable. It’s an essential tool for developers looking to provide transparent and granular updates to their end users.

**Key benefits:**

- **Detailed Order Lifecycle**: Understand every state change, partial fill, or rejection in one place.
- **Enhanced Transparency**: Provide end users with accurate insights into how their orders were executed.
- **Troubleshooting Tool**: Quickly identify order rejections or partial fills and the reasons behind them.

## Endpoint & Method

`POST` `/singleOrderHistory`

**URL**:

```
https://api.firstock.in/V1/singleOrderHistory
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the typical JSON request body for the **Single Order History API**. Fields marked **Mandatory** must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| orderNumber | string | Yes | The unique identifier of the order you wish to get history. | "24121300003425" |

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
curl --location 'https://api.firstock.in/V1/singleOrderHistory' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}",
    "orderNumber": "25040800002296"
}'
```

**Python**

```python
from firstock import firstock
singleOrderHistory = firstock.singleOrderHistory(
    userId= "{{userId}}",
    orderNumber="25063000011911"
)
print(singleOrderHistory)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
const singleOrderHistory = (orderNumber) => {
  firstock.singleOrderHistory(
    { userId: "{{userId}}",
      orderNumber: '25070100010584' },
    (err, result) => {
      console.log("singleOrderHistory Error, ", err);
      console.log("singleOrderHistory Result: ", result);
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
single_order_history := Firstock.OrderRequest{
		UserId:      "{{userId}}",
		OrderNumber: order_number,
	}
singleOrderHistory, err := Firstock.SingleOrderHistory(single_order_history)
fmt.Println("Error:", err)
fmt.Println("Result:", singleOrderHistory)
```

## Response Structure

**Success Response**:

When the request is valid and the order exists under the user’s account, you will receive a **200 OK** status with:

- ***status***: Typically *"success"*.
- ***message***: Short description (e.g., *"Order history data received"*).
- ***data***: An array of objects, each representing a step or fill in the order’s lifecycle.

**Key Fields per History Entry**:

- ***averagePrice***: The average fill price at this stage.
- ***exchange***: Exchange name or code (*"NFO"*, *"NSE"*, etc.).
- ***fillShares***: Shares (or lots) filled during this phase.
- ***orderNumber***: Unique identifier for the order.
- ***orderTime***: When the order transitioned to this state.
- ***price***: The price specified for this order step.
- ***status***: Current status (e.g., *"Rejected"*, *"Filled"*, *"Open"*).
- ***rejectReason***: Explanation if the status is *"Rejected"*.
- ***tradingSymbol***: The instrument’s symbol.
- ***transactionType***: *"B"* for buy, *"S"* for sell.

**Failure Response**:

If any required field is missing, invalid, or the order can’t be canceled, you may receive a **400** or **401** status code with an error structure:

- **Invalid** ***jKey***: Session may be expired or incorrect, prompting re-login.
- ***code***: Error code (e.g., *"400"*, *"401"*).
- **Non-existent or already purged orderNumber**: The platform may not have any data if the order is extremely old or invalid.
- **Missing** ***userId***: The API cannot identify which user’s order history to fetch.

**Response**

**200**

```json
{
    "status": "success",
    "message": "Order history data received",
    "data": [
        {
            "averagePrice": "0.00",
            "exchange": "NFO",
            "exchangeOrderNum": "1400000007552574",
            "exchangeTime": "07-May-2025 09:30:33",
            "fillShares": "0",
            "orderNumber": "25050700001776",
            "orderTime": "09:30:33 07-05-2025",
            "price": "190.00",
            "priceType": "LMT",
            "product": "M",
            "quantity": "750",
            "rejectReason": " ",
            "remarks": "Mobile App Order",
            "reportType": "Cancelled",
            "retention": "DAY",
            "status": "CANCELED",
            "tickSize": "0.05",
            "token": "38605",
            "tradingSymbol": "NIFTY08MAY25P24350",
            "transactionType": "S",
            "userId": "TV0001"
        }
        {
            "averagePrice": "0.00",
            "exchange": "NFO",
            "exchangeOrderNum": "",
            "exchangeTime": "01-Jan-1970 05:30:00",
            "fillShares": "0",
            "orderNumber": "25050700001776",
            "orderTime": "09:22:08 07-05-2025",
            "price": "190.00",
            "priceType": "LMT",
            "product": "M",
            "quantity": "750",
            "rejectReason": " ",
            "remarks": "Mobile App Order",
            "reportType": "Pending New",
            "retention": "DAY",
            "status": "PENDING",
            "tickSize": "0.05",
            "token": "38605",
            "tradingSymbol": "NIFTY08MAY25P24350",
            "transactionType": "S",
            "userId": "TV0001"
        },
        {
            "averagePrice": "0.00",
            "exchange": "NFO",
            "exchangeOrderNum": "",
            "exchangeTime": "01-Jan-1970 05:30:00",
            "fillShares": "0",
            "orderNumber": "25050700001776",
            "orderTime": "09:22:08 07-05-2025",
            "price": "190.00",
            "priceType": "LMT",
            "product": "M",
            "quantity": "750",
            "rejectReason": " ",
            "remarks": "Mobile App Order",
            "reportType": "New Ack",
            "retention": "DAY",
            "status": "OPEN",
            "tickSize": "0.05",
            "token": "38605",
            "tradingSymbol": "NIFTY08MAY25P24350",
            "transactionType": "S",
            "userId": "TV0001"
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
      "field": "orderNumber",
      "message": "required field is empty or missing: orderNumber"
    }
  }
```

## Usage & Best Practices

- **Data Correlation**

  - Correlate the returned history entries with your **Order Book** data to provide a holistic view of all orders and their histories.
- **Session Validity**

  - Ensure the **jKey** (or **susertoken**) is current. If your session expires, you’ll need to re-authenticate before fetching order history.
- **Partial vs. Complete Fills**

  - For partially filled orders, you may see multiple entries with incremental fill quantities and updated average prices.
- **Error Handling**

  - If you encounter repeated **BAD_REQUEST** or **INVALID_JKEY** errors, check whether the request body is correct, and confirm your session token is valid.
- **Archival**

  - If your application needs to store or display historical data long-term, consider archiving these responses. The platform may only hold order details for a limited time.

## **Conclusion**

The **Single Order History API** is invaluable for traders and developers requiring a fine-grained breakdown of each order’s lifecycle. By combining this data with broader **Order Book** queries, you can offer users a comprehensive view of how and when their trades executed or failed.
