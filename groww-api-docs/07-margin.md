# Source: https://groww.in/trade-api/docs/curl/margin

# Margin

## Get Available User Margin

`GET https://api.groww.in/v1/margins/detail/user`

Returns available and used margin. Groww states that all prices are in rupees.

```bash
curl -X GET 'https://api.groww.in/v1/margins/detail/user' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

Response payload fields include `clear_cash`, `net_margin_used`, `brokerage_and_charges`, `collateral_used`, `collateral_available`, and `adhoc_margin`. Nested `fno_margin_details` contains `net_fno_margin_used`, `span_margin_used`, `exposure_margin_used`, `future_balance_available`, `option_buy_balance_available`, and `option_sell_balance_available`. Nested `equity_margin_details` contains `net_equity_margin_used`, `cnc_margin_used`, `mis_margin_used`, `cnc_balance_available`, and `mis_balance_available`.

```json
{
  "status": "SUCCESS",
  "payload": {
    "clear_cash": 5000,
    "net_margin_used": 35000,
    "brokerage_and_charges": 200,
    "collateral_used": 3000,
    "collateral_available": 7000,
    "adhoc_margin": 1500,
    "fno_margin_details": {
      "net_fno_margin_used": 15000,
      "span_margin_used": 7000,
      "exposure_margin_used": 4000,
      "future_balance_available": 3000,
      "option_buy_balance_available": 11000,
      "option_sell_balance_available": 1000
    },
    "equity_margin_details": {
      "net_equity_margin_used": 10000,
      "cnc_margin_used": 5000,
      "mis_margin_used": 3000,
      "cnc_balance_available": 9000,
      "mis_balance_available": 1000
    }
  }
}
```

## Calculate Required Margin for Orders

`POST https://api.groww.in/v1/margins/detail/orders?segment=CASH`

Calculates margin for an order or basket. Basket orders are supported for `FNO` segments.

```bash
curl -X POST 'https://api.groww.in/v1/margins/detail/orders?segment=CASH' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0' \
  -d '[{"trading_symbol":"WIPRO","transaction_type":"BUY","quantity":1,"price":100,"order_type":"LIMIT","product":"CNC","exchange":"NSE"}]'
```

Each body item requires `trading_symbol`, `quantity`, `exchange`, `segment`, `product`, `order_type`, and `transaction_type`. `price` is optional and is specified in rupees for limit orders.

Response payload fields: `exposure_required`, `span_required`, `option_buy_premium`, `brokerage_and_charges`, `total_requirement`, `cash_cnc_margin_required`, `cash_mis_margin_required`, and `physical_delivery_margin_requirement`. All prices in the response are rupees.
