# Brokerage Details API

## Overview

The Brokerage Details API calculates fees associated with stock orders. It accepts parameters like instrument, quantity, product type, transaction type, and price, then returns a comprehensive charges breakdown.

## Endpoint

**GET** `https://api.upstox.com/v2/charges/brokerage`

## Authentication

Requires Bearer token: `Authorization: Bearer {your_access_token}`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| instrument_token | Yes | string | Key of the instrument (see Field Pattern Appendix for regex) |
| quantity | Yes | integer | Order quantity (cannot be zero) |
| product | Yes | string | Product type (D for delivery, I for intraday) |
| transaction_type | Yes | string | BUY or SELL |
| price | Yes | float | Order price (cannot be zero) |

## Response Structure

```json
{
  "status": "success",
  "data": {
    "charges": {
      "total": 208.27,
      "brokerage": 0.0,
      "taxes": {
        "gst": 1.02,
        "stt": 175.0,
        "stamp_duty": 26.23
      },
      "other_charges": {
        "transaction": 5.68,
        "clearing": 0.0,
        "ipft": 0.17,
        "sebi_turnover": 0.17
      },
      "dp_plan": {
        "name": "DP3A",
        "min_expense": 18.5
      }
    }
  }
}
```

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1059 | Invalid instrument_token format |
| UDAPI1060 | Missing quantity field |
| UDAPI1064 | Quantity cannot be zero |
| UDAPI1063 | Missing product field |
| UDAPI1054 | Invalid product value |
| UDAPI1062 | Missing transaction_type field |
| UDAPI1057 | Invalid transaction_type value |
| UDAPI1061 | Missing price field |
| UDAPI1065 | Price cannot be zero |
