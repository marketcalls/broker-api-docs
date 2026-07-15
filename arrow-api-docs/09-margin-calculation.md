> Source: https://docs.arrow.trade/rest-api/margin-calculation/

# Margin API

Calculate margin requirements and trading charges for individual orders and basket orders, taking into account existing positions and open orders.

## Overview

The Margin API enables precise calculation of capital requirements before order placement, helping traders assess available margin and understand the cost structure of their trades. The API supports both individual order margin calculations with detailed charge breakdowns and basket-level margin calculations for multi-instrument strategies.

Basket margin

For multi-leg basket margin (`POST /margin/basket`), see the full request/response examples in [order-margin.md](../order-margin/).

## Endpoint Reference

### Calculate Order Margin

Calculate margin requirements and detailed charges for a single order, considering existing positions and open orders.

Endpoint Details

**Method:** `POST`
**URL:** `/margin/order`
**Header:** Required (`appID` \+ `token`)

#### Request Headers

Header | Type | Required | Description
---|---|---|---
`appID` | string | ✓ | Your application identifier
`token` | string | ✓ | User authentication token
`Content-Type` | string | ✓ | Must be `application/json`

#### Request Body

Field | Type | Required | Description
---|---|---|---
`exchange` | string | ✓ | Exchange identifier (NSE, BSE, NFO, etc.)
`token` | string | ✓ | Unique instrument token
`quantity` | string | ✓ | Order quantity
`product` | string | ✓ | Product type (M=Margin, C=Cash, etc.)
`price` | string | ✓ | Order price
`transactionType` | string | ✓ | Transaction type (B=Buy, S=Sell)
`order` | string | ✓ | Order type (LMT=Limit, MKT=Market, etc.)

#### Request Example

```bash
    curl --location 'https://edge.arrow.trade/margin/order' \
    --header 'appID: <YOUR_APP_ID>' \
    --header 'token: <YOUR_TOKEN>' \
    --header 'Content-Type: application/json' \
    --data '{
        "exchange": "NSE",
        "symbol": "SBIN-EQ"
        "quantity": "100",
        "product": "C",
        "price": "800",
        "transactionType": "B",
        "order": "LMT"
    }'
```

#### Success Response

```json
{
    "data": {
        "requiredMargin": 80000,
        "minimumCashRequired": 80000,
        "marginUsedAfterTrade": 0,
        "charge": {
            "brokerage": 0,
            "exchangeTxnFee": 2.376,
            "gst": {
                "cgst": 0,
                "igst": 0.45648000000000005,
                "sgst": 0,
                "total": 0.45648000000000005
            },
            "ipft": 0.08,
            "sebiCharges": 0.08,
            "stampDuty": 12,
            "total": 94.99248,
            "transactionTax": 80
        }
    },
    "status": "success"
}
```

## Integration Notes

Best Practices

  * Use Order Margin API for single orders to get detailed charge breakdowns
  * Use Basket Margin API for multi-leg strategies to benefit from portfolio-level margin optimization
  * Always validate margin availability before order placement
  * Cache margin calculations appropriately to minimize API calls
  * Implement proper error handling and retry logic
  * Consider margin requirements when designing trading strategies

Margin vs Charges

The `margin` field represents the capital blocked for the position, while `charge.total` represents the transaction costs. Both are deducted from available cash upon order execution.

Product Types

Different product types (M=Margin, C=Cash) have different margin requirements and leverage. Ensure you understand the implications before trading.
