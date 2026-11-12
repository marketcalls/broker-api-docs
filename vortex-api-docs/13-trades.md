<!-- Source: https://vortex.rupeezy.in/docs/2.2/trades/ -->

# Trades

Use the below apis to see and manage positions:

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `GET` | [{{base_url}}/trading/trades](#get-trades) | Fetch all trades | 10/sec |

## Get Trades

```
Endpoint: {{base_url}}/trading/trades
```

### Trade Book Response

```
{
    "status": "success",
    "trades": [
        {
            "order_id": "NXAAE00002@6",
            "ticker": "NSE:ACC",
            "exchange": "NSE_EQ",
            "token": 22,
            "trade_no": "2416756",
            "exchange_order_no": "1000000016120889",
            "transaction_type": "SELL",
            "product": "INTRADAY",
            "variety": "RL",
            "trade_quantity": 1,
            "trade_price": 1856.75,
            "symbol": "ACC",
            "series": "EQ",
            "instrument_name": "",
            "expiry_date": "",
            "strike_price": 0.00,
            "option_type": "",
            "traded_at": "2023-06-16 13:06:43",
            "initiated_by": "MOBILE-Ex",
            "modified_by": "MOBILE-Ex",
            "order_identifier": "app=DEMO"
        },
        {
            "order_id": "NXAAE00001@6",
            "ticker": "NSE:ACC",
            "exchange": "NSE_EQ",
            "token": 22,
            "trade_no": "2413994",
            "exchange_order_no": "1000000016098874",
            "transaction_type": "BUY",
            "product": "INTRADAY",
            "variety": "RL",
            "trade_quantity": 1,
            "trade_price": 1857.00,
            "symbol": "ACC",
            "series": "EQ",
            "instrument_name": "",
            "expiry_date": "",
            "strike_price": 0.00,
            "option_type": "",
            "traded_at": "2023-06-16 13:06:17",
            "initiated_by": "MOBILE-Ex",
            "modified_by": "MOBILE-Ex",
            "order_identifier": "app=DEMO"
        }
    ],
    "metadata": {
        "total_records": 2
    }
}
```
