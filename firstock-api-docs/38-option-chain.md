# Option Chain

> Source: https://firstock.in/api/docs/option-chain/

> This document describes how to use the Get Option Chain API within the Firstock trading platform.

## Overview

The **Get Option Chain API** allows traders and developers to fetch nearby option strikes (calls and puts) for a given underlying index or stock. You specify the **symbol**, **exchange**, **expiry**, and the central **strikePrice**, along with the number of strikes you want above and below that price.

**Key benefits:**

1. **Granular Option Data**: Access multiple strikes around a central price to see calls and puts.
2. **Customization**: Choose how many strikes (*count*) you want on either side of the strike price.
3. **Integration**: Use returned *tradingSymbol*values to place orders or fetch quotes for each option contract.

**Note:** Maximum value allowed for **count**is **30**.

## Endpoint & Method

`POST` `/optionChain`

**URL**:

```
https://api.firstock.in/V1/optionChain
```

**Headers**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Body**

Below is the general JSON body for the Get Option Chain API request. All fields marked as Mandatory must be included.

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for your Firstock account (same as used during login). | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| exchange | string | Yes | Exchange code, typically "NFO" for options. | "NSE" |
| symbol | string | Yes | The underlying symbol or index name. | "IDEA-EQ" |
| expiry | string | Yes | Option expiry date in the format DDMONYY. | "17APR25" |
| count | string | Yes | How many strikes above and below the given strike price to fetch. | "5" |
| strikePrice | string | Yes | The central strike price around which you want options. | "23150" |

**Request**

```json
{
  "userId": "AB1234",
  "jKey": "211b250616fe25067a3b71b24451d1dfd389faabe338770ada62d81fd20b4bda",
  "exchange": "NFO",
  "symbol": "NIFTY",
  "expiry": "17APR25",
  "count": "5",
  "strikePrice": "23150"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/optionChain' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "{{userId}}",
    "jKey": "211b250616fe25067a3b71b24451d1dfd389faabe338770ada62d81fd20b4bda",
    "exchange": "NFO",
    "symbol": "NIFTY",
    "expiry": "17APR25",
    "count": "5",
    "strikePrice": "23150"
}'
```

**Python**

```python
from firstock import firstock
optionChain = firstock.optionChain(
    userId= "{{userId}}",
    exchange="NFO",
    symbol="NIFTY",
    strikePrice="23150",
    expiry= "03JUL25",
    count="5"
            )
print(optionChain)
```

**Nodejs**

```javascript
const {Firstock} = require("firstock");
const firstock = new Firstock();
firstock.optionChain(
  {
    userId:  "{{userId}}",
    exchange: "NFO",
    symbol: "NIFTY",
    expiry: "17APR25",
    count: "5",
    strikePrice: "23150"
  },
  (err, result) => {
    console.log("optionChain Error, ", err);
    console.log("optionChain Result: ", result);
  }
);
```

**Golang**

```go
import (
	"github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)

optionChainRequest := Firstock.OptionChainRequest{
		UserId:      "{{userId}}",
		Exchange:    "NFO",
		Symbol:      "NIFTY",
		Expiry:      "12JUN25", // Format must match broker format
		Count:       "5",       // Number of strikes above/below
		StrikePrice: "23150",   // ATM strike price
	}
optionChain, err := Firstock.OptionChain(optionChainRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", optionChain)
```

## Response Structure

**Success Response**

A valid request will typically return a **200 OK** status and a JSON object containing:

1. **status:** Typically *"success"*.
2. **message:** A note indicating success (e.g., *"Option chain data retrieved successfully"*).
3. **data:** An array of option contract objects.

**Key Fields within *data*:**

- *exchange*: Usually "*NFO*" for NSE derivatives.
- *lotSize*: The number of shares per lot for this option contract.
- *optionType*: *"CE"*for call, *"PE"* for put.
- *strikePrice*: The strike price of this contract.
- *tradingSymbol*: Symbol used to place orders or fetch quotes for this specific contract.
- *token*: Internal numeric identifier recognized by Firstock’s system.
- *lastTradedPrice*: The LTP for the symbol.

**Failure Response**

If the session token (*jKey*) is invalid or the request body is malformed, you may see a **400** or **401** status with error details:

1. **status:** *"failed"*.
2. **code:** Error code (e.g.,*"400"*, *"401"*).
3. **Missing or incorrect**symbol**,**exchange**,**expiry**, or**strikePrice
4. *count*not specified

**Response**

**200**

```json
{
          "status": "success",
          "message": "Option chain data retrieved successfully",
          "data": [
          {
            "exchange": "NFO",
            "lotSize": "75",
            "optionType": "CE",
            "parentToken": "26000",
            "pricePrecision": "2",
            "strikePrice": "22950.00",
            "tickSize": "0.05",
            "token": "79424",
            "tradingSymbol": "NIFTY24APR25C22950",
            "lastTradedPrice": "130.00"
          },
          {
            "exchange": "NFO",
            "lotSize": "75",
            "optionType": "PE",
            "parentToken": "26000",
            "pricePrecision": "2",
            "strikePrice": "23400.00",
            "tickSize": "0.05",
            "token": "79489",
            "tradingSymbol": "NIFTY24APR25P23400",
            "lastTradedPrice": "130.00"
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
      "field": "symbol",
      "message": "Symbol is required"
    }
  }
```

## Usage & Best Practices

1. **Building Option Chains**

  - Perfect for constructing an option chain UI that shows multiple strikes above and below a given price.
2. **Session Maintenance**

  - Ensure your jKey is still valid. If you see INVALID_JKEY, prompt for re-login.
3. **Strike/Expiry Selection**

  - Make sure strikePrice and expiry align with actual market contracts (based on the symbol’s available expiries).
4. **Lot Sizes**

  - The API returns lotSize; use it to place orders or calculate margin if needed.
5. **Integration with Quotes**

  - Once you have the tradingSymbol for a call or put, you can fetch real-time quotes or place trades for that contract.

## Conclusion

The **Get Option Chain API** is essential for quickly assembling a list of nearby call and put contracts around a chosen strike price. This data helps traders analyze potential option strategies (like spreads, straddles, strangles, etc.). Always confirm your session (*jKey*) is valid, handle errors for missing fields, and integrate the returned *tradingSymbol*into further API calls for quotes or order placement.
