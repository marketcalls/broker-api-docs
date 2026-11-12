# Get Fund and Margin V3

## Overview

API to retrieve a detailed balance breakdown for the user across cash and pledged margin components. The response is organized into two top-level categories:

- **available_to_trade** covers funds and margin that are ready to use for trading, broken down into cash and pledge sub-buckets, each with a full breakdown of margin in use.
- **unavailable_to_trade** covers funds that are present in the account but cannot yet be traded, including unsettled profit and unavailable pledge collateral.

## Endpoint

**GET** `https://api.upstox.com/v3/user/get-funds-and-margin`

## Response

```json
{
    "status": "success",
    "data": {
        "available_to_trade": {
            "total": 5379.03,
            "cash_available_to_trade": {
                "total": 5117.34,
                "cash": {
                    "opening_balance": 5137.34,
                    "added_today": 110.0,
                    "withdrawn_today": -130.0,
                    "amount_from_stock_sale": 0.0,
                    "unpaid_charges": 0
                },
                "margin_used": {
                    "total": 0.0,
                    "mtf": 0.0,
                    "loss": {
                        "total": 0.0,
                        "realised": 0.0,
                        "unrealised": 0.0
                    },
                    "span_exposure": 0.0,
                    "cash_margin_var_elm": 0.0,
                    "premium_present": 0.0,
                    "delivery_margin": {
                        "total": 0.0,
                        "equity": 0.0,
                        "fo_settlement": 0.0
                    }
                }
            },
            "pledge_available_to_trade": {
                "total": 261.69,
                "margin_from_pledge": {
                    "total": 263.49,
                    "equity": 263.49,
                    "mutual_funds": 0.0
                },
                "margin_used": {
                    "total": 1.8,
                    "mtf": 0.0,
                    "span_exposure": 0.0,
                    "cash_margin_var_elm": 1.8,
                    "premium_present": 0.0,
                    "delivery_margin": {
                        "total": 0.0,
                        "equity": 0.0,
                        "fo_settlement": 0.0
                    }
                }
            }
        },
        "unavailable_to_trade": {
            "cash_unavailable_to_trade": {
                "unsettled_profit": {
                    "todays_profit": 0.0,
                    "previous_days": 0.0
                }
            },
            "pledge_unavailable_to_trade": {
                "equity": 0.0,
                "mutual_funds": 0.0
            }
        }
    }
}
```

### Response

| Name | Type | Description |
| --- | --- | --- |
| status | string | Outcome of the request. Possible values: `success` , `error` |
| data | object | Top-level data object. |

### `available_to_trade`

| Name | Type | Description |
| --- | --- | --- |
| total | float | Total amount available to trade across cash and pledged margin. |
| cash_available_to_trade | object | Cash balance and margin usage breakdown. |
| pledge_available_to_trade | object | Pledge collateral and margin usage breakdown. |

### `cash_available_to_trade`

| Name | Type | Description |
| --- | --- | --- |
| total | float | Net cash available to trade. |
| cash.opening_balance | float | Amount available in your account from yesterday (closing balance) along with any blocked cash due to Exchange margin requirements and after deducting any applicable charges. |
| cash.added_today | float | Successful amount added today. |
| cash.withdrawn_today | float | Successful amount withdrawn today. |
| cash.amount_from_stock_sale | float | Amount received from selling stocks. |
| cash.unpaid_charges | float | Outstanding charges that are due but not levied due to insufficient balance in the account. These charges include maintenance and other related fees. |
| margin_used.total | float | Total cash margin currently in use. |
| margin_used.span_exposure | float | When you buy or sell any F&O contracts, brokers need to keep an amount of cash known as 'margin'. This is to cover them against the risk of adverse price movements. There are 2 broad types of margins: the SPAN margin and the exposure margin. |
| margin_used.cash_margin_var_elm | float | VAR (Value at Risk) margins are collected to cover for potential losses during a particular time frame. For liquid securities, VAR margin covers losses for a single day. For illiquid securities, it covers losses that may occur over 3 days. ELM (Extreme Loss Margin) is the margin blocked over and above VAR margin for risk situations that are not covered in the VAR estimation. |
| margin_used.premium_present | float | The amount paid to buy options. |
| margin_used.delivery_margin.total | float | Total delivery margin blocked. |
| margin_used.delivery_margin.equity | float | Cash blocked for equity delivery buy/sell. |
| margin_used.delivery_margin.fo_settlement | float | Cash blocked for F&O physical settlement. |
| margin_used.mtf | float | Cash blocked for MTF (Margin Trading Facility) trades. |
| margin_used.loss.total | float | Total loss amount. |
| margin_used.loss.realised | float | Realised losses are losses on trades that have been exited / sold. |
| margin_used.loss.unrealised | float | Unrealised losses are losses on open positions. |

### `pledge_available_to_trade`

| Name | Type | Description |
| --- | --- | --- |
| total | float | Net pledge margin available to trade after deducting margin used. |
| margin_from_pledge.total | float | Total margin available from pledged securities. |
| margin_from_pledge.equity | float | Margin against stocks pledged. |
| margin_from_pledge.mutual_funds | float | Cash margin against mutual funds pledged. |
| margin_used.total | float | Total pledge margin currently in use. |
| margin_used.span_exposure | float | When you buy or sell any F&O contracts, brokers need to keep an amount of cash known as 'margin'. This is to cover them against the risk of adverse price movements. There are 2 broad types of margins: the SPAN margin and the exposure margin. |
| margin_used.cash_margin_var_elm | float | VAR (Value at Risk) margins are collected to cover for potential losses during a particular time frame. For liquid securities, VAR margin covers losses for a single day. For illiquid securities, it covers losses that may occur over 3 days. ELM (Extreme Loss Margin) is the margin blocked over and above VAR margin for risk situations that are not covered in the VAR estimation. |
| margin_used.premium_present | float | The amount paid to buy options. |
| margin_used.delivery_margin.total | float | Total delivery margin blocked. |
| margin_used.delivery_margin.equity | float | Cash blocked for equity delivery buy/sell. |
| margin_used.delivery_margin.fo_settlement | float | Cash blocked for F&O physical settlement. |
| margin_used.mtf | float | Collateral margin blocked for MTF trades. |

### `unavailable_to_trade`

| Name | Type | Description |
| --- | --- | --- |
| cash_unavailable_to_trade.unsettled_profit.todays_profit | float | Today's unsettled profit/loss from positions. |
| cash_unavailable_to_trade.unsettled_profit.previous_days | float | Unsettled profit/loss carried over from previous days. |
| pledge_unavailable_to_trade.equity | float | All pledged stocks which can't be used. |
| pledge_unavailable_to_trade.mutual_funds | float | Cash margin against mutual funds which are pledged but can't be used. |

## Error Codes

| Error code | Description |
| --- | --- |
| UDAPI100072 | **The Funds service is accessible from 5:30 AM to 12:00 AM IST daily** — Thrown when the funds API is called between midnight and 5:30 AM. The response status will be `423 Locked` during this maintenance window. |
