# Source: https://groww.in/trade-api/docs/curl/portfolio

# Portfolio

Portfolio endpoints return demat holdings and current positions. Requests use the shared Groww API headers described in [the cURL API introduction](https://groww.in/trade-api/docs/curl).

## Get Holdings

`GET https://api.groww.in/v1/holdings/user`

Returns current stock holdings stored in the user's Demat account.

```bash
curl -X GET 'https://api.groww.in/v1/holdings/user' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

Example response:

```json
{
  "status": "SUCCESS",
  "payload": {
    "holdings": [
      {
        "isin": "INE545U01014",
        "trading_symbol": "RELIANCE",
        "quantity": 10,
        "average_price": 100,
        "pledge_quantity": 2,
        "demat_locked_quantity": 1,
        "groww_locked_quantity": 1.5,
        "repledge_quantity": 0.5,
        "t1_quantity": 3,
        "demat_free_quantity": 5,
        "corporate_action_additional_quantity": 1,
        "active_demat_transfer_quantity": 1
      }
    ]
  }
}
```

| Field | Type | Description |
| --- | --- | --- |
| `isin` | string | Instrument ISIN. |
| `trading_symbol` | string | Holding's trading symbol. |
| `quantity` | integer | Net holding quantity. |
| `average_price` | decimal | Average holding price in rupees. |
| `pledge_quantity` | decimal | Quantity pledged. |
| `demat_locked_quantity` | decimal | Quantity locked in Demat. |
| `groww_locked_quantity` | decimal | Quantity locked by Groww. |
| `repledge_quantity` | decimal | Quantity repledged. |
| `t1_quantity` | decimal | T+1 quantity. |
| `demat_free_quantity` | decimal | Free quantity in Demat. |
| `corporate_action_additional_quantity` | integer | Additional quantity from corporate action. |
| `active_demat_transfer_quantity` | integer | Quantity in an active Demat transfer. |

## Get User Positions

`GET https://api.groww.in/v1/positions/user`

Returns positions for the user. The `segment` query parameter is documented as `CASH` or `FNO`.

```bash
curl -X GET 'https://api.groww.in/v1/positions/user?segment=CASH' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

## Get Position by Trading Symbol

`GET https://api.groww.in/v1/positions/trading-symbol`

Required query parameters: `trading_symbol` and `segment` (`CASH` or `FNO`).

```bash
curl -G 'https://api.groww.in/v1/positions/trading-symbol' \
  --data-urlencode 'trading_symbol=RELIANCE' \
  --data-urlencode 'segment=CASH' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

Example position object (also used by the symbol query):

```json
{
  "trading_symbol": "RELIANCE",
  "credit_quantity": 10,
  "credit_price": 12500,
  "debit_quantity": 5,
  "debit_price": 12000,
  "carry_forward_credit_quantity": 8,
  "carry_forward_credit_price": 12300,
  "carry_forward_debit_quantity": 3,
  "carry_forward_debit_price": 11800,
  "exchange": "NSE",
  "symbol_isin": "INE123A01016",
  "quantity": 15,
  "product": "CNC",
  "net_carry_forward_quantity": 10,
  "net_price": 12400,
  "net_carry_forward_price": 12200,
  "realised_pnl": 500
}
```

| Field | Type | Description |
| --- | --- | --- |
| `trading_symbol` | string | Instrument trading symbol. |
| `segment` | string | Instrument segment (`CASH`, `FNO`). |
| `credit_quantity` / `debit_quantity` | integer | Credited/debited quantity. |
| `credit_price` / `debit_price` | integer | Average credited/debited price, in rupees. |
| `carry_forward_credit_quantity` / `carry_forward_debit_quantity` | integer | Carry-forward credited/debited quantity. |
| `carry_forward_credit_price` / `carry_forward_debit_price` | integer | Average carry-forward prices, in rupees. |
| `exchange` | string | Exchange. |
| `symbol_isin` | string | Instrument ISIN. |
| `quantity` | integer | Net quantity. |
| `product` | string | Product type. |
| `net_carry_forward_quantity` | integer | Net carry-forward quantity. |
| `net_price` | integer | Net average price, in rupees. |
| `net_carry_forward_price` | integer | Net average carry-forward price, in rupees. |
| `realised_pnl` | integer | Realised profit or loss, in rupees. |

All endpoint responses are wrapped in a `status` and `payload` object. Groww explicitly describes the position prices above as rupee values; do not convert these documented prices from paise.
