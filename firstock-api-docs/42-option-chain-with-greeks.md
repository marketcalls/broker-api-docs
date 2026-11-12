# Option Chain with Greeks

> Source: https://firstock.in/api/docs/option-chain-with-greeks/

## Overview

The **Option Chain with Greeks API** allows traders and developers to fetch nearby option strikes (calls and puts) for a given underlying index or stock, along with their associated Greeks (Delta, Gamma, Theta, Vega, Rho) and implied volatility (IV). You specify the **symbol, exchange, expiry,** and the central **strikePrice,** along with the number of strikes you want above and below that price. Alternatively, pass **count=ALL** to retrieve the complete option chain without specifying a strike price.

**Key benefits:**

• Granular Option Data: Access multiple strikes around a central price to see calls and puts.
• Greeks Included: Each option includes Delta, Gamma, Theta, Vega, Rho, and IV.
• Full Chain Support: Use count=ALL to retrieve the entire option chain in one call.
• Customization: Choose how many strikes (count) you want on either side of the strike price.
• Integration: Use returned tradingSymbol values to place orders or fetch quotes for each option contract.

**Note**: Maximum value allowed for count is 30. Use count=ALL to fetch the complete chain (strikePrice is not
required in this case).

## Endpoint & Method

`POST` `/optionChainGreeks`

**URL**:

```
https://api.firstock.in/V1/optionChainGreeks
```

**Headers:**

| Name | Value |
|---|---|
| Content-Type | application/json |

**Request Body:**

| Field | Type | Mandatory | Description | Example |
|---|---|---|---|---|
| userId | string | Yes | Unique identifier for | AB1234 |
| jKey | string | Yes | Active session token obtained from a successful login. | ce1c4471eb95... |
| exchange | string | Yes | Exchange code. NSE maps to NFO, BSE maps to BFO. | "NSE" |
| symbol | string | Yes | The underlying symbol or index name. | "NIFTY" |
| expiry | string | Yes | Option expiry date in the format DDMONYY. | 17APR25 |
| count | string | Yes | Number of strikes above and below the strike price. Max 30. Use "ALL" for full chain. | 5 or ALL |
| strikePrice | string | Conditional | Central strike price. Required when count is not ALL. | 23150 |

**Request:**

With specific count and strike price:

```json
{
"userId": "{{userId}}",
"jKey": "{{jKey}}",
"exchange": "NFO",
"symbol": "NIFTY",
"expiry": "24JUL25",
"count": "10",
"strikePrice": "25500"
}
```

With count=ALL (no strikePrice needed):

```json
{
"userId": "{{userId}}",
"jKey": "{{jKey}}",
"exchange": "NFO",
"symbol": "NIFTY",
"expiry": "24JUL25",
"count": "ALL"
}
```

## Example Usage

**Curl**

```bash
curl --location 'https://api.firstock.in/V1/optionChainGreeks' \
--header 'Content-Type: application/json' \
--data '{
    "userId": "NP2997",
    "jKey": "4c3acc86bfc1a66788eed5bf2787d8ff6036879b1cff37b7918a8c6d7382a815",
    "exchange": "NFO",
    "symbol": "NIFTY",
    "expiry": "24MAR26",
    "count": "ALL",
    "strikePrice": "25500"
}'
```

**Python**

```python
from firstock import firstock

result = firstock.optionChainGreeks(
exchange="NFO",
symbol="NIFTY",
expiry="17MAR26",
count="10",
strikePrice="25500",
userId='YOUR_USER_ID'
)

print(result)
```

**Nodejs**

```javascript
import (
    "github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)
optionChainGreeksRequest := Firstock.OptionChainGreeksRequest{
    UserId:      "{{userId}}",
    Exchange:    "NFO",
    Symbol:      "RELIANCE",
    Expiry:      "30MAR26",
    Count:       "1",
    StrikePrice: "1420",
}
optionChainGreeks, err := Firstock.OptionChainGreeks(optionChainGreeksRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", optionChainGreeks)
```

**Golang**

```go
import (
    "github.com/the-firstock/firstock-developer-sdk-golang/Firstock"
)
optionChainGreeksRequest := Firstock.OptionChainGreeksRequest{
    UserId:      "{{userId}}",
    Exchange:    "NFO",
    Symbol:      "RELIANCE",
    Expiry:      "30MAR26",
    Count:       "1",
    StrikePrice: "1420",
}
optionChainGreeks, err := Firstock.OptionChainGreeks(optionChainGreeksRequest)
fmt.Println("Error:", err)
fmt.Println("Result:", optionChainGreeks)
```

## Response Structure

**Success Response (200 OK)**:

A valid request returns a **200 OK** status and a JSON object containing:

- ***status***: *"success"*.
- ***message***: "Option chain with Greeks retrieved successfully"
- ***data***: An array of option contract objects with Greeks.

**Key Fields within data:**

| Field | Type | Description |
|---|---|---|
| exchange | string | Exchange code (e.g. NFO, BFO). |
| token | string | Internal numeric identifier for the contract |
| tradingSymbol | string | Symbol used to place orders or fetch quotes. |
| optionType | string | CE for call, PE for put. |
| pricePrecision | string | Decimal precision for price (e.g. 2). |
| lotSize | string | Number of shares per lot for this contract. |
| tickSize | string | Minimum price movement (e.g. 0.05). |
| strikePrice | string | Strike price of the contract. |
| lastTradedPrice | string | Last traded price (LTP) in rupees. |
| parentToken | string | Token of the parent index (if applicable). |
| delta | string | Rate of change of option price vs underlying. |
| gamma | string | Rate of change of delta vs underlying. |
| theta | string | Time decay - option value lost per day. |
| vega | string | Sensitivity to volatility changes. |
| rho | string | Sensitivity to interest rate changes. |
| iv | string | Implied Volatility of the option. |
| oi | string | Open Interest for the option contract. |

**Response**

**200**

```json
{
"status": "success",
"message": "Option chain with Greeks retrieved successfully",
"data": [
{
"exchange": "NFO",
"token": "79424",
"tradingSymbol": "NIFTY24APR25C22950",

"optionType": "CE",
"pricePrecision": "2",
"lotSize": "75",
"tickSize": "0.05",
"strikePrice": "22950.00",
"lastTradedPrice": "130.00",
"parentToken": "26000",
"delta": "0.45",
"gamma": "0.002",
"theta": "-12.5",
"vega": "8.3",
"rho": "0.15",
"iv": "14.25",
"oi": "125400"
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

**Common Error Scenarios:**

| Field | Error Message |
|---|---|
| userId | User ID is required |
| jKey | JKey is required |
| exchange | Invalid exchange provided |
| symbol | Symbol is required |
| expiry | Invalid expiry format |
| count | Count must be a valid positive number or ALL |
| count | Count cannot exceed 30 |
| strikePrice | Strike Price is required when count is not ALL |
| strikePrice | Strike Price must be a valid positive number |

## Usage & Best Practices

- **Building Option Chains**

  - Perfect for constructing an option chain UI that shows multiple strikes above and below a given price with Greeks.
- **Full Chain Retrieval**

  - Use count=ALL when you need the complete option chain. strikePrice is not
    required in this case.
- **Session Maintenance**

  - Ensure your jKey is still valid. If you see an invalid session error, prompt for
    re-login.
- **Strike / Expiry Selection**

  - Make sure strikePrice and expiry align with actual market contracts based on the symbol's available expiries.
- **Lot Sizes**

  - The API returns lotSize; use it to place orders or calculate margin if needed.
- **Greeks Usage**

  - Use Delta and IV to assess option sensitivity and pricing. Theta helps understand time decay impact day over day.
- **Integration with Quotes**

  - Once you have the tradingSymbol for a call or put, use it to fetch real-time
    quotes or place trades for that contract.

## **Conclusion**

The **Option Chain with Greeks API** is essential for quickly assembling a list of nearby call and put contracts around a chosen strike price, complete with Greeks and implied volatility. This data helps traders analyze potential option strategies such as spreads, straddles, and strangles. Always confirm your session (jKey) is
valid, handle errors for missing fields, and integrate the returned tradingSymbol into further API calls for quotes or order placement. Use count=ALL for complete chain analysis when a specific strike is not required.
