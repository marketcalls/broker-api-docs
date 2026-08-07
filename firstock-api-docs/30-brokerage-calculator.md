# Brokerage Calculator

> Source: https://firstock.in/api/docs/brokerage-calculator/

> This document explains how to use the Brokerage Calculator API within the Firstock trading platform.

## Overview

The **Brokerage Calculator API** allows you to calculate the total brokerage, taxes, and final charges for a trade across multiple asset classes like equities, and derivatives.
It provides real-time estimation of trading costs based on your input parameters such as order type, quantity, price, and exchange.

This helps traders and investors to accurately predict the net profitability or cost of a trade before execution.

**Key benefits:**

- **Real-time Cost Estimation**: Instantly calculate total charges before placing trades.
- **Trade Planning**: Helps in determining breakeven points and potential profitability.
- **Supports Multiple Asset Classes**: Equity, and derivatives markets.
- **Improved Transparency**: Provides clear breakup of all transaction costs.

## Endpoint & Method

`POST` `/brokerageCalculator`

**URL**:

```
https://api.firstock.in/V1/brokerageCalculator
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body:**

Below is the general JSON body for the **Get Security Info API** request. All **Mandatory** fields must be included.

| Field | Value | Type | Mandatory |
|---|---|---|---|
| userId | AB1234 | String | Yes |
| jKey | {{jKey}} | String | Yes |
| exchange | NFO | String | Yes |
| tradingSymbol | RELIANCE27FEB25F | String | Yes |
| transactionType | B | String | Yes |
| product | M | String | Yes |
| quantity | 500 | String | Yes |
| price | 125930 | String | Yes |
| strike_price | 0 | String | NO (should not be =0 for |
| inst_name | FUTSTK | String | NO (value required** for future & options) future : FUTSTK, FUTIDX options: OPTSTK, OPTIDX for NFO |
| lot_size | 1 | String | NO (if not essential, need to send default value) |

**Request:**

```json
{
    "userId": "AB1234",
    "jKey": "137dea860c50cbe7077dd8455569cac08f3b6fdd5512b48bde71c3110e4b8788",
    "exchange": "NFO",
    "tradingSymbol": "RELIANCE27FEB25F",
    "transactionType": "B",
    "Product": "M",
    "quantity": "500",
    "price": "125930",
    "strike_price": "0",
    "inst_name": "FUTSTK",
    "lot_size": "1"

}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/brokerageCalculator' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "137dea860c50cbe7077dd8455569cac08f3b6fdd5512b48bde71c3110e4b8788",
    "exchange": "NFO",
    "tradingSymbol": "RELIANCE27FEB25F",
    "transactionType": "B",
    "Product": "M",
    "quantity": "500",
    "price": "125930",
    "strike_price": "0",
    "inst_name": "FUTSTK",
    "lot_size": "1"
}'
```

**Python**

```python
from firstock import firstock

bc = firstock.brokerageCalculator(
    userId="{{userId}}",
    exchange="NFO",
    tradingSymbol="RELIANCE27FEB25F",
    transactionType="B",
    product="M",
    quantity="500",
    price="125930",
    strike_price="0",
    inst_name="FUTSTK",
    lot_size="1"
)

print(bc)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");

const firstock = new Firstock();

firstock.brokerageCalculator(
  {
    userId:  "{{userId}}",
    exchange: "NFO",
    tradingSymbol: "RELIANCE27FEB25F",
    transactionType: "B",
    Product: "M",
    quantity: "500",
    price: "125930",
    strike_price: "0",
    inst_name: "FUTSTK",
    lot_size: "1"
  },
  (err, result) => {
    console.log("brokerageCalculator Error, ", err);
    console.log("brokerageCalculator Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

brokerageCalculatorRequest := Firstock.BrokerageCalculatorRequest{
		UserId:          "{{userId}}",
		Exchange:        "NSE",
		TradingSymbol:   "SAWACA",
		TransactionType: "B",
		Product:         "C",
		Quantity:        "1",
		Price:           "0.50",
		StrikePrice:     "0.00",
		InstName:        "EQ",
		LotSize:         "1",
	}
brokerageCalculator, err := Firstock.BrokerageCalculator(brokerageCalculatorRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", brokerageCalculator)
```

## Response Structure

**Success Response**:

If your request is valid and the security is found, you will receive a **200 OK** status with a JSON object containing:

- ***status***: Typically *"success"*.
- ***message***: A short note (e.g., *"Fetched security info successfully"*).
- ***data***: An object detailing the security’s info.

**Key Fields in data**:

- ***instrumentName***: The instrument category (e.g., *"EQ"*, *"OPTIDX"*, *"FUTSTK"*, etc.).
- ***segment***: The market segment (e.g., *"EQT"*, *"FNO"*, etc.).
- ***symbolName***: The system-recognized name for the instrument.
- ***tradingSymbol***: The display-oriented name (may differ from the input if the system has a specific format).
- ***token***: Numeric identifier used within Firstock’s system.
- ***priceFactor***, ***pricePrecision***, ***tickSize***: Information about how prices are calculated or displayed.

**Failure Response**:

If any required field is missing, invalid, or the session token (jKey) is expired, you may receive a **400** or **401** status code with an error object:

- **Invalid or missing** ***jKey***.
- **Empty or incorrect** ***tradingSymbol*** or *exchange*.
- **Security not found** (the symbol may not exist or be spelled incorrectly).

**Response**

**200**

```json
{
          "status": "success",
          "message": "Brokerage Data",
          "data": {
            "exchange": "NSE",
            "instrumentName": "UNDIND",
            "lotSize": "1",
            "mult": "1",
            "priceFactor": "(1 / 1 ) * (1 / 1)",
            "pricePrecision": "2",
            "segment": "EQT",
            "symbolName": "NIFTY",
            "tickSize": "0.00",
            "token": "26000",
            "tradingSymbol": "Nifty 50"
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

- **Verification Before Trading**

  - Use this API to confirm the correct *segment*, *instrumentName*, or *lotSize*before placing F&O orders.
- **Session Management**

  - Maintain a valid *jKey*. If *INVALID_JKEY*or similar errors arise, re-login or refresh tokens as needed.
- **Error Handling**

  - If *status*is *"failed"*, review the *error.field* and *error.message* to correct any missing or invalid parameters.
- **Reference Data**

  - Consider storing or caching common results if you repeatedly request the same symbol (e.g., “NIFTY”) to reduce API overhead.
- **Integration with Other APIs**

  - Combine with **Order Margin**, **Place Order**, or **Get Quotes** for a seamless workflow once you have the correct details for a symbol.

## **Conclusion**

The **Get Security Info API** is a crucial tool for validating an instrument’s internal details—such as **segment**, **instrumentName**, **lotSize**, and **token**—before you proceed with more advanced operations. Make sure to maintain a valid session (*jKey*), handle errors gracefully, and use this data to ensure you’re interacting with the correct instrument.
