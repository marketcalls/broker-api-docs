# Funds

- [Get Funds Summary](#get-funds-summary)

## Get Funds Summary

Source: https://developer.paytmmoney.com/docs/api/get-funds-summary/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/accounts/v1/funds/summary?config=true`  

### Description

> Gets all the **information of a user trading account** like current balance, funds utilized during order execution, opening balance, displays whether the funds added or not.

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | optional | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `config` | string | optional | Boolean value (True/False) |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `trade_balance` | string | optional | Displays current trade balance |
| `utilised_amount` | string | optional | Amount/Funds Utilized during order execution |
| `withdrawal_balance` | string | optional | Withdrawable Balance from the user account |
| `adhoc_limit` | string | optional | Adhoc Limit |
| `opening_balance` | string | optional | Opening Balance of the user |
| `funds_added` | string | optional | Displays whether Funds added or not |
| `collaterals` | string | optional | - |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/accounts/v1/funds/summary?config=true' \
--header 'x-jwt-token: {{JWT-TOKEN}}'
```

### Sample Responses

#### SUCCESS

```json
{
   "meta":{},
   "data":{
      "funds_summary":{
         "trade_balance":13941.56,
         "utilised_amount":0.0,
         "withdrawal_balance":3341.56,
         "adhoc_limit":0.0,
         "opening_balance":-658.44,
         "funds_added":14600.0,
         “collaterals”:0.0

      },
      "config":{
         "credit":{
            "min":50,
            "max":20000000,
            "decimal_length":0
         },
         "debit":{
            "min":1,
            "max":10000000,
            "decimal_length":2
         }
      }
   }
}
```

### Notes

### Query Parameters

| Attribute | Description |
| --- | --- |
| config  string  mandatory | Boolean value (True/False) |
