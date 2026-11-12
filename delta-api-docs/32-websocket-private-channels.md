# Private Channels

> Source: https://docs.delta.exchange/#private-channels-2

Private channels require clients to authenticate.

## Margins
This channel provides updates on wallet balances. Updates are sent for a specific asset whenever there is a change in wallet balances and margins for that asset. 

> Margins Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "margins"
            }
        ]
    }
}
```
```json
// margin update
{
    "action": "update",
    "asset_id": 2,                           // BTC
    "asset_symbol": "BTC",                   // BTC
    "available_balance": "9.385",            // Available balance for trading = balance - blocked_margin
    "available_balance_for_robo": "9.385",   // Available balance for robo trading = balance - blocked_margin
    "balance": "10",                         // Wallet balance = deposits - withdrawals + realised_cashflows
    "blocked_margin": "0.615",               // Total Margin blocked
    "commission": "0.001",                   // Commissions blocked in isolated margined positions and orders
    "cross_asset_liability": "0",            // Liability between asset in cross margin mode
    "cross_commission": "0.002",             // Commissions blocked in cross margined positions and orders
    "cross_locked_collateral": "0.003",      // Balance blocked for collateral
    "cross_order_margin": "0.004",           // Margin blocked in cross margined open orders
    "cross_position_margin": "0.005",        // Margin blocked in cross margined positions
    "id": 1,                                 // Wallet Id
    "interest_credit": "0",                  // Interest credited
    "order_margin": "0.1",                   // Margin blocked in isolated margined open orders
    "pending_referral_bonus": "0",           // Bonus pending
    "pending_trading_fee_credit": "0",       // Pending trading fee to credit
    "portfolio_margin": "0.2",               // Margin blocked for portfolio margined positions and orders. Same as blocked margin in portfolio margins channel.
    "position_margin": "0.3",                // Margin blocked in isolated margined positions
    "robo_trading_equity": "0",              // Equity for robo trading
    "timestamp": 1719397302569921,           // Unix timestamp in microseconds
    "trading_fee_credit": "0",               // Trading fee credited
    "type": "margins",                       // Margins channel
    "unvested_amount": "0",                  // Amount locked. Relevant only for DETO
    "user_id": 1                             // User id
}
```

## Positions
This channel provides updates whenever there is any change in your open positions.

A snapshot of current open position will be sent after subscribing a symbol, incremental updates will be sent on trade executions.
You need to send the list of symbols for which you would like to subscribe to positions channel. You can also subscribe to positions 
updates for category of products by sending [category-names](25-schemas.md#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.
Please note that if you subscribe to positions channel without specifying the symbols list, you will not receive any data.

> Positions Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "positions",
                "symbols": ["BTCUSD"]
            }
        ]
    }
}

//Subscribe for all the symbols
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "positions",
                "symbols": ["all"]
            }
        ]
    }
}
```

```json
// Position update
{
    "type": "positions",
    "action": "",                       // "create"/"update"/"delete"
    "reason": "",                       // null, "auto_topup"
    "symbol": "BTCUSD",           // Product Symbol
    "product_id": 1,                    // Product ID
    "size": -100,                       // Position size, if > 0 -> long else short
    "margin": "0.0121",                 // Margin blocked in the position
    "entry_price": "3500.0",            // Avg Entry price of the position
    "liquidation_price": "3356.0",      // Liquidation trigger price
    "bankruptcy_price": "3300.0",       // Bankruptcy Price
    "commission": "0.00001212"          // Commissions blocked for closing the position
}

//Snapshot 
{
   "result":[
      {
         "adl_level":"4.3335",
         "auto_topup":false,
         "bankruptcy_price":"261.82",
         "commission":"17.6571408",
         "created_at":"2021-04-29T07:25:59Z",
         "entry_price":"238.023457888493475682",
         "liquidation_price":"260.63",
         "margin":"4012.99",
         "product_id":357,
         "product_symbol":"ZECUSD",
         "realized_funding":"-3.08",
         "realized_pnl":"6364.57",
         "size":-1686,
         "updated_at":"2021-04-29T10:00:05Z",
         "user_id":1,
         "symbol":"ZECUSD"
      }
   ],
   "success":true,
   "type":"positions",
   "action":"snapshot"
}
```

## Orders
Channel provides updates when any order is updated for any action such as fill, quantity change. Need to pass list of product symbols while subscribing.

A snapshot of all open/pending orders will be sent after subscribing a symbol. And all incremental updates will be sent on create/update/delete of orders

All updates including snapshot will have incremental seq_id. seq_id is separate for each symbol.

Any of the following events can be tracked by the reason field in this channel

- fill
- stop_update
- stop_trigger
- stop_cancel
- liquidation
- self_trade

You need to send the list of symbols for which you would like to subscribe to orders channel. You can also subscribe to orders
updates for category of products by sending [category-names](25-schemas.md#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.
Please note that if you subscribe to orders channel without specifying the symbols list, you will not receive any data.

> Orders Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "orders",
                "symbols": ["BTCUSD"]
            }
        ]
    }
}
```
```json
// Order update

{
    "type": "orders",
    "action": "create",                 // "create"/"update"/"delete"
    "reason": "",                       // "fill"/"stop_update"/"stop_trigger"/"stop_cancel"/"liquidation"/"self_trade"/null
    "symbol": "BTCUSD",           // Product Symbol
    "product_id": 27,                    // Product ID
    "order_id": 1234,                    // Order id
    "client_order_id": "",              // Client order id
    "size": 100,                        // Order size
    "unfilled_size": 55,                // Unfilled size
    "average_fill_price": "8999.00",     // nil for unfilled orders
    "limit_price": "9000.00",                  // Price of the order
    "side": "buy",                       // Order side (buy or sell)
    "cancellation_reason": "cancelled_by_user",        // Cancellation reason in case of cancelled order, null otherwise
    "stop_order_type": "stop_loss_order",             // If a Stop Order -> "stop_loss_order"/"take_profit_order", null otherwise
    "bracket_order": false,              // true for a bracket_order, false otherwise
    "state": "open",                     // "open"/"pending"/"closed"/"cancelled"
    "seq_no": 1,                         // Incremental sequence number
    "timestamp": 1594105083998848,       // Unix timestamp in microseconds
    "stop_price": "9010.00",                             // stop_price of stop order        
    "trigger_price_max_or_min": "9020.00",               // for trailing stop orders
    "bracket_stop_loss_price": "8090.00",
    "bracket_stop_loss_limit_price": "8090.00",
    "bracket_take_profit_price": "9020",      
    "bracket_take_profit_limit_price": "9020",
    "bracket_trail_amount": "10.00"
}
```

```json
// Snapshot
{
  "meta": {
    "seq_no": 7,
    "timestamp": 1594149235554045
  },
  "result": [
    {
      "id": 1592130,
      "limit_price": "9000",
      "order_type": "limit_order",
      "product_id": 13,
      "reduce_only": false,
      "side": "buy",
      "size": 1,
      "state": "open",
      "stop_order_type": null,
      "stop_price": null,
      "time_in_force": "gtc",
      "trail_amount": null,
      "unfilled_size": 1,
      "average_fill_price": "8999.00",
      "user_id": 1132
    }
  ],
  "success": true,
  "symbol": "BTCUSD",
  "type": "orders",
  "action": "snapshot"
}
```

## UserTrades
Please use "v2/user_trades" channel for better latency.

Channel provides updates for fills. Need to pass list of product symbols while subscribing.

All updates will have incremental seq_id. seq_id is separate for each symbol.

Auto Deleverage Liquidations of a position can be tracked by reason: "adl" in the user_trades channel.
You need to send the list of symbols for which you would like to subscribe to user trades channel. You can also subscribe to user trades
updates for category of products by sending [category-names](25-schemas.md#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.
Please note that if you subscribe to user trades channel without specifying the symbols list, you will not receive any data.

> User Trades Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "user_trades",
                "symbols": ["BNBBTC_30Nov"]
            }
        ]
    }
}
```
```json
// user_trades
{
    "symbol": "BNBBTC_30Nov",
    "fill_id": "1234-abcd-qwer-3456",
    "reason": "normal",                      // "normal" or "adl"
    "product_id": 7,
    "type": "user_trades",
    "user_id": 1998,
    "order_id": 3283999,
    "side": "buy",
    "size": 190,
    "price": "0.00145791",
    "role": "taker",
    "client_order_id": "GA123",
    "timestamp": 1544091555086559,
    "seq_no": 1
}
    
```

## v2/user_trades
Channel provides updates for fills. Need to pass list of product symbols while subscribing. This channel is similar to user_trades channel, only difference is that, it is faster than user_trades and doesn't contain commission data.

All updates will have incremental sequence_id. sequence_id is separate for each symbol, useful for identifying if any v2/user_trades messages were missed/dropped. The sequence_id will reset to 1 after our systems restart. (usually after maintainaince/market disruption).

Auto Deleverage Liquidations of a position can be tracked by reason: "adl".
Liquidation of a position can be tracked by reason: "liquidation".  
You need to send the list of symbols for which you would like to subscribe to v2/user_trades channel. You can also subscribe to v2/user_trades updates for category of products by sending [category-names](25-schemas.md#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "futures"]}`.  
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.  
Please note that if you subscribe to v2/user_trades channel without specifying the symbols list, you will not receive any data.

> v2/user_trades Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "v2/user_trades",
                "symbols": ["BTCUSD"]
            }
        ]
    }
}
```
```json
// v2/user_trades
{
    "type": "v2/user_trades",
    "sy": "BTCUSD",              // symbol
    "f": "1234-abcd-qwer-3456",  // fill_id
    "R": "normal",               // reason: "normal", "adl", "liquidation"
    "u": 1998,                   // user_id
    "o": 3283999,                // order_id
    "S": "buy",                  // side: "buy" or "sell"
    "s": 190,                    // size in contracts
    "p": "17289.2",              // price
    "po": 5,                     // position (in contracts) after this fill.
    "r": "taker",                // role: "taker" or "maker"
    "c": "GA123",                // client_order_id
    "t": 1685794274866438,       // timestamp of fill creation
    "se": 4                      // incremental sequence_no
}
    
```

## PortfolioMargins
Channel provides updates for portfolio margin values of the selected sub-account. These updates are sent every 2 seconds. In case portfolio margin is not enabled on the selected sub-account, no updates will be sent on this channel.

For detailed description of portfolio margin please see [user guide](https://guides.delta.exchange/delta-exchange-india-user-guide/trading-guide/margin-explainer/portfolio-margin)

UCF: is unrealised cashflows of your portfolio. These are the cashflows (negative for outgoing and positive for incoming) that will take place if all the positions in your portfolio are closed at prevailing mark prices.

> Portfolio Margin Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "portfolio_margins",
                "symbols": [".DEXBTUSD"]
            }
        ]
    }
}
```
```json
// portfolio margin update

{
    "type": "portfolio_margins",
    "user_id": 1,
    "asset_id": 2,                   // BTC
    "index_symbol": ".DEXBTUSD",
    "liquidation_risk": false,
    "blocked_margin": "100", // Margin blocked for current portfolio. Same as portfolio_margin in margins channel.
    "mm_wo_ucf": "80",
    "mm_w_ucf": "80",
    "im_wo_ucf": "100",
    "im_w_ucf": "100",
    "positions_upl": "0", 
    "risk_margin": "100",
    "risk_matrix":{"down":[{"is_worst":false,"pnl":"230.03686162","price_shock":"10"}],"unchanged":[{"is_worst":false,"pnl":"230.03686162","price_shock":"10"}],"up":[]},
    "futures_margin_floor": "20",
    "short_options_margin_floor": "20",
    "long_options_margin_floor": "20",
    "under_liquidation": false,
    "commission": "3.444",
    "margin_floor": "60",
    "timestamp": 1544091555086559, //timestamp in microseconds
    "margin_shortfall": "4.5"             // key sent when liquidation_risk is true 
}

```

Keys - 

- **index_symbol** — This is the coin on which portfolio margin is enabled.
- **positions_upl** — This is unrealised cashflows (UCF) of your portfolio. These are the cashflows (negative for outgoing and positive for incoming) that will take place if all the positions in your portfolio are closed at prevailing mark prices. Unrealised cashflow is positive for long options and negative for short options.
- **im_w_ucf** — This is the initial margin (IM) requirement for the portfolio. IM is computed as max(risk_margin, margin_floor) - UCF.
  - If UCF > max(risk_margin, margin_floor) then IM is negative. Negative margin requirement results in increase in your balance available for trading.
  - If the Wallet Balance (ex spot orders) is less than IM then you would only be able to place orders that reduce the risk of the portfolio.
- **im_wo_ucf** — This is IM without UCF.
- **mm_w_ucf** — This is the maintenance margin (MM) requirement for the portfolio. MM is computed as 80% * max(risk_margin, margin_floor) - UCF.
  - If the Wallet Balance (ex spot orders) is less than MM then the portfolio will go into liquidation.
- **mm_wo_ucf** — This is MM without UCF.
- **commission** — This is the trading fees blocked for the open orders/positions (for closing the positions) in the portfolio.
  - This is in addition to the IM requirement.
- **blocked_margin** — The margin actually blocked for your portfolio. If your Wallet Balance (ex spot orders) is greater than IM + commission then blocked_margin = IM + commissions. Otherwise blocked_margin is equal to the maximum amout we are able to block to meet the portfolio margin requirement.
  - If blocked_margin < MM then the portfolio goes into liquidation.
- **liquidation_risk** — This flag indicates if the portfolio is at liquidation risk.
  - This flag is set to TRUE when blocked_margin < im_w_ucf + commissions.
- **under_liquidation** — This flag is set to TRUE when the portfolio is under liquidation.
- **margin_shortfall** — This is the minimum topup amount needed to bring the portfolio out of liquidation risk state.
- **risk_margin** — The maximum likely loss of the portfolio under the various simulated stress scenarios.
- **risk_matrix** — Matrix showing the profit/loss of the portfolio under various simulated stress scenarios.
  - Profit/loss for each position and open order is computed with reference to the prevailing mark prices. Positive numbers indicate profit and negative numbers indicate loss.
- **margin_floor** — Margin Floor is the minimum risk_margin required for a portfolio.
  - It is comprised of sum of futures_margin_floor, long_options_margin_floor, short_options_margin_floor

## MMP Trigger
Channel provides updates when MMP is triggered. Market maker protection is available to registered market makers by default.
> MMP Trigger Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "mmp_trigger"
            }
        ]
    }
}
```
```json
// mmp_trigger response
{
    "user_id": 1,
    "asset": "BTC",
    "frozen_till": 1561634049751430     # timestamp is microseconds, will be -1 if manual reset is enabled 
}
```
