# Trade Book

> Source: https://firstock.in/api/docs/trade-book/

> This document explains how to use the Trade Book API on the Firstock trading platform.

## Overview

The **Trade Book API** returns a record of trades (executions) that have occurred for the user’s account. Unlike the **Order Book**, which may contain pending or partially filled orders, the trade book focuses on completed or partially completed trades, listing the actual fill prices and quantities.

**Key benefits:**

- **Accurate Execution Data**: Access confirmed trades with fill quantities and prices.
- **Historical Analysis**: Ideal for profit/loss calculations, analytics, or compliance audits.
- **Transparency**: Detailed breakdown of all trades to ensure clarity for both users and developers.

## Endpoint & Method

`POST` `/tradeBook`

**URL**:

```
https://api.firstock.in/V1/tradeBook
```

**Headers:**

Below is the typical JSON body for a **Trade Book API** request. All fields marked as **Mandatory** must be included.

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
curl --location 'https://api.firstock.in/V1/tradeBook' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "{{jKey}}"
}'
```

**Python**

```python
from firstock import firstock
tradeBook = firstock.tradeBook(userId="{{userId}}")
print(tradeBook)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.tradeBook(
  { userId:  "{{userId}}"},
  (err, result) => {
    console.log("tradeBook Error, ", err);
    console.log("tradeBook Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

tradeBook, err := Firstock.TradeBook("{{userId}}")
fmt.Println("Error:", err)
fmt.Println("Result:", tradeBook)
```

## Response Structure

**Success Response:**

If the request is valid and trades exist for the given account, you will receive a **200 OK** status and a JSON object containing:

- **status**: Usually *"success"*.
- **message**: A short description (e.g., *"Trade history data received"*).
- **data**: An array or object detailing the trades.

**Key Fields for Each Trade Entry**:

- *exchange*: The market where the trade was executed (*"NSE"*, *"BSE"*,*"NFO"*, etc.).
- ***fillId***: Unique identifier for this fill (trade execution).
- ***fillPrice***: The actual price at which the shares or lots were filled.
- ***fillQuantity***: Number of shares or lots filled in this trade.
- ***fillTime***: Timestamp indicating when the trade was executed.
- ***orderNumber***: The order associated with this particular trade.
- *transactionType*: *"B"* for buy, *"S"* for sell.
- ***tradingSymbol***: The instrument symbol.
- *product*: Product code (e.g., *"C"*,*"I"*, *"M"*).

**Failure Response:**

If any required field is missing, invalid, or the order can’t be canceled, you may receive a **400** or **401** status code with an error structure:

- **Invalid or missing *jKey***: Session may be expired; re-login may be required.
- **Missing *userId***: The API cannot identify your account.
- **No Trades Found**: In some cases, the API might return an empty ***data***array if no trades exist.

**Response**

**200**

```json
{
          "status": "success",
          "message": "Trade history data received",
          "data": [
          {
            "exchange": "NSE",
            "exchangeUpdateTime": "21-04-2025 09:30:02",
            "exchordid": "1200000006968574",
            "fillId": "401070025",
            "fillPrice": 2837,
            "fillQuantity": "1",
            "fillTime": "21-04-2025 09:30:02",
            "fillshares": "1",
            "lotSize": "25",
            "orderNumber": "25042100002340",
            "orderTime": "09:30:02 21-04-2025",
            "priceFactor": "1.000000",
            "pricePrecision": "2",
            "priceType": "MKT",
            "product": "C",
            "quantity": "1",
            "retention": "DAY",
            "tickSize": "0.05",
            "token": "21001",
            "tradingSymbol": "PSB-EQ",
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
    "code": "400",
    "name": "BAD_REQUEST",
    "error": {
      "field": "orderNumber",
      "message": "required field is empty or missing: orderNumber"
    }
  }
```

## Usage & Best Practices

- **Data Reconciliation**

  - Compare the trade book entries to your **Order Book** to confirm partial fills, average prices, or unexpected executions.
- **Rate Limits & Time Intervals**

  - If you’re pulling trade data frequently, be mindful of any rate limits or overhead. For real-time updates, see if WebSocket feeds are available.
- **Session Management**

  - Always ensure your *jKey*is current. If you receive recurring *"INVALID_JKEY"* errors, prompt the user to log in again.
- **Historical Storage**

  - You might want to archive trade data locally for performance or compliance reasons. The platform may only store data for a specific time window.
- **Error Handling**

  - Inspect *field*and *message*in the *error*object to correct any missing or invalid parameters.

## Conclusion

The **Trade Book API** is essential for understanding completed trades and their financial details. By integrating it with your application, you provide users with real-time insights into their trading activities, ensuring accuracy in profit/loss calculations, portfolio management, and overall transparency.
