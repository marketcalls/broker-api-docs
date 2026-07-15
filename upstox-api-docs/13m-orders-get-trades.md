# Get Trades API

## Overview

Retrieves all trades executed for the current day. An order can be executed in smaller segments based on market situation - each partial execution constitutes a trade.

## Endpoint

**GET** `https://api.upstox.com/v2/order/trades/get-trades-for-day`

## Request Headers

- `Content-Type: application/json`
- `Accept: application/json`
- `Authorization: Bearer {your_access_token}`

## Response (200)

```json
{
  "status": "success",
  "data": [
    {
      "exchange": "NSE",
      "product": "D",
      "trading_symbol": "GMRINFRA-EQ",
      "instrument_token": "151064324",
      "order_type": "MARKET",
      "transaction_type": "BUY",
      "quantity": 1,
      "exchange_order_id": "221013001021540",
      "order_id": "221013001021539",
      "exchange_timestamp": "03-Aug-2017 15:03:42",
      "average_price": 299.4,
      "trade_id": "50091502",
      "order_ref_id": "udapi-aqwsed14356",
      "order_timestamp": "23-Apr-2021 14:22:06"
    }
  ]
}
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| exchange | string | Exchange (NSE, BSE, etc.) |
| product | string | I, D, CO, or MTF |
| trading_symbol | string | Trading symbol |
| instrument_token | string | Instrument key |
| order_type | string | MARKET, LIMIT, SL, SL-M |
| transaction_type | string | BUY or SELL |
| quantity | int32 | Total quantity traded |
| average_price | float | Execution price |
| trade_id | string | Exchange-generated trade ID |
