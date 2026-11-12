# Public Channels

> Source: https://docs.delta.exchange/#public-channels

## ticker
This channel is available on the new public api websocket endpoint.

**ticker** channel provides **price change data** for the last **24 hrs** (rolling window).  
It is published every **5 seconds**.

To subscribe to the ticker channel, you need to send the list of **symbols** for which you would like to receive updates.

You need to send the list of symbols for which you would like to subscribe to this channel. You can also subscribe to this channel for all symbols in an Option Chain. e.g. To subscribe to all Put and Call Options updates for BTC Options expiring on 31st March 2026, send symbol = "BTC-310326". ("ASSET-DDMMYY") 

**Important:**  
If you subscribe to the ticker channel without specifying a symbols list, you will **not** receive any data.

> **Ticker Sample**

```json
// Subscribe to specific symbol
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "ticker",
                "symbols": [
                    "XRPUSD",
                    "ETH-200426" // For all ETH options expiring on 20th April 2026.
                ]
            }
        ]
    }
}
```

```json
// Response
{
    "d": [
        {
            "g": [                  // Greeks (Options-related metrics, will be null for Futures and Spot products)
                "0.01939861",       // delta: Rate of change of the option price with respect to the underlying asset's price
                "0.00006382",       // gamma: Rate of change of delta with respect to the underlying asset's price
                "0.00718630",       // rho: Rate of change of option price with respect to interest rate
                "-81.48397021",     // theta: Rate of change of option price with respect to time (time decay)
                "0.72486575"        // vega: Sensitivity of the option price to volatility changes
            ],
            "i": 27,                // product_id: The unique identifier for the product
            "m": "72124.53970358",  // mark_price: The current mark price
            "m24hc": "1.5902",      // mark_change_24h: Percentage change in mark price over the last 24 hours
            "ohlc": [               // [open, high, low, close] prices for the last 24-hour period
                71009.0,            // open
                73135.5,            // high
                70495.0,            // low
                72123.5             // close
            ],
            "oi": [
                "537395",           // oi_contracts: Open interest in contracts
                "4457821.6900"      // oi_change_usd_6h: Change in open interest value in settling symbol
            ],
            "pb": [
                "68495.16304969",   // price_band_lower: Lower price band limit
                "75705.18021281"    // price_band_upper: Upper price band limit
            ],
            "q": [                  // Quotes
                "72101",            // best_ask: The best ask price
                "822",              // ask_size: The size of the ask
                "72100",            // best_bid: The best bid price
                "2123",             // bid_size: The size of the bid
                null                // impact_mid_price: Mid price impact (null if not available)
            ],
            "qiv": [                // Implied volatility (Options only, null for Futures/Spot)
                "0.25",             // ask_iv: Implied volatility for the ask price
                "0.25",             // bid_iv: Implied volatility for the bid price
                "-0.37846136"       // mark_iv: Mark volatility
            ],
            "s": "BTCUSD",          // symbol: The symbol of the contract
            "to": [
                1153493034.0710223, // turnover: Total turnover in the settling symbol
                1153493034.0710223  // turnover_usd: Turnover value in USD
            ]
        }
    ],
    "sp": "72154.6",                // spot_price: Spot price at the time of the ticker
    "sy": "BTCUSD",                 // symbol: The symbol of the contract
    "ts": 1775801092453559,         // timestamp: The timestamp of the data (in microseconds)
    "type": "ticker"
}
```

## ob_l1

This channel is available on the new public api websocket endpoint.

**ob_l1** channel provides best ask/bid or top level orderbook updates. You need to send the list of symbols for which you would like to subscribe to this channel. You can also subscribe to this channel for all symbols in an Option Chain. e.g. To subscribe to all Put and Call Options updates for BTC Options expiring on 31st March 2026, send symbol = "BTC-310326". ("ASSET-DDMMYY")

Please note that if you subscribe to L1 channel without specifying the symbols list, you will not receive any data.  
Publish interval: 100 millisecs  
Max interval (in case of same data): 5 secs

> ob_l1 Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "ob_l1",
                "symbols": [
                    "ETHUSD",
                    "BTC-310326"
                ]
            }
        ]
    }
}
```

```json
// ob_l1 Response

{
    "ap": "68519.0",
	"as": "285",
	"bp": "68518.0",
	"bs": "2452",
	"lts": 1775037882675402,
	"sy": "BTCUSD",
	"ts": 1775037882748105,
	"type": "ob_l1"
}
```

## ob_l2

This channel is available on the new public api websocket endpoint.

**ob_l2** channel provides the top 15 level of orderbook data for the specified list of symbols at a pre-determined frequency. The frequency of updates may vary for different symbols. You can only subscribe to upto 100 symbols on a single connection. Unlike ob_l1 channel, ob_l2 channel does not accept 'options expiry' as valid symbols. 
Please note that if you subscribe to ob_l2 channel without specifying the symbols list, you will not receive any data.  
To get full orderbook (All levels of orderbook) use [ob_updates](#ob_updates) channel  
Publish interval: 500 millisecs  
Max interval (in case of same data): 10 secs

> ob_l2 Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "ob_l2",
                "symbols": [
                    "ETHUSD"
                ]
            }
        ]
    }
}
```

```json
// ob_l2 Response
{
    "a": [
        [
            "68525.0",  // price
            "3313" // size in contracts
        ],
        [
            "68525.5",
            "3009"
        ],...
        // Top 15 levels
    ],
    "b": [
        [
            "68524.0", // price
            "2452" // size in contracts
        ],
        [
            "68523.5",
            "3000"
        ],...
        // Top 15 levels
    ],
    "lts": 1775038313132415, // last orderbook updated timestamp
    "sy": "BTCUSD", // symbol
    "ts": 1775038313632092, // publish timestamp
    "type": "ob_l2"
}
```

## ob_updates

This channel is available on the new public api websocket endpoint.

**ob_updates** channel provides initial snapshot and then incremental orderbook data. The frequency of updates may vary for different symbols. You can only subscribe to upto 100 symbols on a single connection. ob_updates channel does not accept product category names or "all" as valid symbols.
Please note that if you subscribe to ob_updates channel without specifying the symbols list, you will not receive any data.  
Publish interval: 100 millisecs  
"action"="update" messages wont be published till there is an orderbook change.

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "ob_updates",
                "symbols": [
                    "BTCUSD"
                ]
            }
        ]
    }
}

// Initial snapshot response
{
  "action":"snapshot",
  "a":[["16919.0", "1087"], ["16919.5", "1193"], ["16920.0", "510"]], // asks
  "b":[["16918.0", "602"], ["16917.5", "1792"], ["16917.0", "2039"]], // bids
  "ts":1671140718980723,  // update timestamps
  "seq":6199, // sequence_no
  "sy":"BTCUSD", // symbol
  "type":"ob_updates", // channel_name
  "cs":2178756498 // checksum
}

// Incremental update response
{
  "action":"update",
  "a":[["16919.0", "0"], ["16919.5", "710"]], // asks
  "b":[["16918.5", "304"]], // bids
  "seq":6200, // sequence_no
  "sy":"BTCUSD", // symbol
  "type":"ob_updates", // channel_name
  "ts": 1671140769059031, // update timestamps
  "cs":3409694612 // checksum
}

// Error response
{
  "action":"error",
  "symbol":"BTCUSD",
  "type":"ob_updates",
  "msg":"Snapshot load failed. Verify if product is live and resubscribe after a few secs."
}
```

### How to maintain orderbook locally using this channel:

1) When you subscribe to this channel, the first message with "action"= "snapshot" resembles the complete orderbook at this time. json_key "a" (asks) and json_key "b" (bids) are arrays of ["price", "size"]. (size is number of contracts at this price)

2) After the initial snapshot, messages will be with "action" = "update", resembling the difference between current and previous orderbook state. "asks" and "bids" are arrays of ["price", "new size"]. "asks" are sorted in increasing order of price. "bids" are sorted in decreasing order of price. This is true for both "snapshot" and "update" messages.

3) "seq" (sequence_no) field must be used to check if any messages were dropped. "sequence_no" must be +1 of the last message.  
e.g. In the snapshot message it is 6199, and the update message has 6200. The next update message must have 6201. In case of sequence_no mismatch, resubscribe to the channel, and start from the beginning.

4) If sequence_no is correct, edit the in-memory orderbook using the "update" message.  
Case 1: price already exists, new size is 0 -> Delete this price level.  
Case 2: price already exists, new size isn't 0 -> Replace the old size with new size.  
Case 3: price doesn't exists -> insert the price level.  
e.g. for the shown snapshot and update messages to create the new orderbook: in the ask side, price level of "16919.0" will be deleted. Size at price level "16919.5" will be changed from "1193" to "710". In the bids side there was no price level of "16918.5", so add a new level of "16918.5" of size "304". Other price levels from the snapshot will remain the same.

5) If "action":"error" message is received, resubscribe this symbol after a few seconds. Can occur in rare cases, e.g. Failed to send "action":"snapshot" message after subscribing due to a race condition, instead an "error" message will be sent.

Checksum: Using this, users can verify the accuracy of orderbook data created using ob_updates. checksum is the "cs" key in the message payload.  
Steps to calculate checksum:  
1) Edit the old in-memory orderbook with the "update" message received.  
2) Create asks_string and bids_string as shown below. where priceN = price at Nth level, sizeN = size at Nth level. Asks are sorted in increasing order and bids in decreasing order by price.  
asks_string = price0:size0,price1:size1,…,price9:size9  
bids_string = price0:size0,price1:size1,…,price9:size9  
checksum_string = asks_string + "|" + bids_string  
Only consider the first 10 price levels on both sides. If orderbook as less than 10 levels, use only them.  
e.g. If after applying the update, the new orderbook becomes ->  
asks = [["100.00", "23"], ["100.05", "34"]]  
bids = [["99.04", "87"], ["98.65", "102"], ["98.30", "16"]]  
checksum_string = "100.00:23,100.05:34|99.04:87,98.65:102,98.30:16"  
3) Calculate the CRC32 value (32-bit unsigned integer) of checksum_string. This should be equal to the checksum provided in the "update" message.

## trades
This channel is available on the new public api websocket endpoint.

**trades** channel provides a real time feed of all trades (fills).
You need to send the list of symbols for which you would like to subscribe to trades channel. You can also subscribe to
trades updates for category of products by sending [category-names](25-schemas.md#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "perpetual_futures"]}`.  
You can subscribe to trades for an options chain by subcribing symbols as ASSET-DDMMYY. e.g. "BTC-150426"
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.
Please note that if you subscribe to trades channel without specifying the symbols list, you will not receive any data.

> Trades Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "trades",
                "symbols": [
                    "BTCUSD"
                ]
            }
        ]
    }
}
```

```json
// Trades Response
{
    "p": "72141.5", // price
    "r": "m", // buyer_role. "m" = maker, "t" = taker
    "s": 1.0, // size in contracts
    "sy": "BTCUSD", // symbol
    "t": 1775800366578410, // time of the trade.
    "ts": 1775800367003029, // publish from server timestamps
    "type": "trades"
}

```

## mark_price
This channel is available on the new public api websocket endpoint.

**mark_price** channel provides mark price updates at a fixed interval. This is the price on which all open positions are marked for liquidation.Please note that the product symbol is prepended with a "MARK:" to subscribe for mark price.  
You need to send the list of symbols for which you would like to subscribe to mark price channel. You can also subscribe to 
mark price updates for category of products by sending [category-names](25-schemas.md#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "perpetual_futures"]}`.  
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.  
You can also subscribe to a Options chain, by passing 'Asset-Expiry', e.g. `{"symbols": ["BTC-310524"] }` will subscribe to all BTC Options expirying on 31st May 2024.  
Please note that if you subscribe to mark price channel without specifying the symbols list, you will not receive any data.  
Publish interval: 2 secs.

> Mark Price Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "mark_price",
                "symbols": [
                    "MARK:C-BTC-69500-150426"
                ]
            }
        ]
    }
}
```

```json
// Mark Price Response
{
    "p": "2296.3486551", // mark price
    "sy": "MARK:C-BTC-69500-100426", // symbol
    "ts": 1775814170680883, // timestamp
    "type": "mark_price"
}
```

## candlesticks
This channel is available on the new public api websocket endpoint.

**candlesticks** channel provides last ohlc candle for given time resolution. Traded price candles and Mark Price candles data can be received by sending appropriate symbol string. "product_symbol" gives traded_price candles, and "MARK:product_symbol" gives mark_price candles.  
e.g. symbols: ["BTCUSD"] gives you Traded Price candlestick data for BTCUSD  
symbols: ["MARK:C-BTC-75000-310325"] gives you Mark Price candlestick data for C-BTC-75000-310325

Subscribe to **candlestick_${resolution}** channel for updates. 

List of supported resolutions
["1m","3m","5m","15m","30m","1h","2h","4h","6h","12h","1d","1w"]
 
You need to send the list of symbols for which you would like to subscribe to candlesticks channel. 
You can also subscribe to candlesticks updates for category of products by sending [category-names](25-schemas.md#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "perpetual_futures"]}`.
Please note that if you subscribe to candlesticks channel without specifying the symbols list, you will not receive any data.

>OHLC candles update sample

```json
//Sample Subscribe Request
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "candlestick_5m",        // "candlestick_" + resolution
                "symbols": ["BTCUSD", "C-BTC-75000-271224"]
            }
        ]
    }
}

Sample feed response

{
    "c": 71748.0, // close
    "h": 71751.5, // high
    "l": 71737.0, // low
    "o": 71737.0, // open
    "res": "1m",
    "sy": "BTCUSD", // symbol
    "ts": 1775814834503627, // timestamp
    "type": "candlestick_1m",
    "v": 2826.0 // volume not present in Mark Price candlestick
}
```

## spot_price
This channel is available on the new public api websocket endpoint.

**spot_price** channel provides a real time feed of the underlying index prices. Specifying symbols when subscribing to spot_price is necessary to receive updates. No updates are sent for symbol: ***"all"***

> Spot Price Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "spot_price",
                "symbols": [
                    ".DEUSDTUSD"
                ]
            }
        ]
    }
}
```

```json
// Spot Price Response
{
    "p": "1", // price
    "sy": ".DEUSDTUSD", // symbol
    "ts": 1775818505952018, // timestamp
    "type": "spot_price"
}
```

## spot_30mtwap_price

**spot_30mtwap_price** channel provides a real time feed of the 30 min twap of underlying index prices. 
This is the price used for settlement of options. Specifying symbols when subscribing to spot_30mtwap_price is necessary to receive updates. No updates are sent for symbol: ***"all"***

> Spot Price 30mtwap Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "spot_30mtwap_price",
                "symbols": [
                    ".DEXBTUSD"
                ]
            }
        ]
    }
}
```

```json
// Spot 30 minutes twap Price Response
{
    "symbol": ".DEXBTUSD",
    "price": "0.0014579",
    "type": "spot_30mtwap_price",
    "timestamp": 1561634049751430
}
```

## funding_rate
This channel is available on the new public api websocket endpoint.

**funding_rate** channel provides a real time feed of funding rates for perpetual contracts.

You need to send the list of symbols for which you would like to subscribe to funding rate channel. You can also subscribe to funding rate updates for category of products by sending [category-names](25-schemas.md#schemaproductcategories). For example: to receive updates for put options and futures, refer this: `{"symbols": ["put_options", "perpetual_futures"]}`.
If you would like to subscribe for all the listed contracts, pass: `{ "symbols": ["all"] }`.
Please note that if you subscribe to funding rate channel without specifying the symbols list, you will not receive any data.

> Funding Rate Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "funding_rate",
                "symbols": [
                    "BTCUSD"
                ]
            }
        ]
    }
}
```

```json
// Funding Rate Response
{
    "fi": 28800,
    "fr": 0.010000000000000002, // funding_rate
    "nfr": 1775836800000000, // next_funding_realization
    "sy": "BTCUSD", // symbol
    "ts": 1775817617666383, // timestamp
    "type": "funding_rate"
}
```

## product_updates
This channel provides updates when markets are disrupted and resumed. On opening, we conduct a single price auction and auction starting and finish events are also published on this channel. To subscribe, you dont need to pass the symbol list. This channel automatically subscribes to all markets by default.

>  Product Updates Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "product_updates"
            }
        ]
    }
}
```

```json
// Market Disruption Response
{
    "type":"product_updates",
    "event":"market_disruption",
    "product":{
        "id":17,
        "symbol":"NEOUSDQ",
        "trading_status":"disrupted_cancel_only",
    },
    "timestamp": 1561634049751430,
}

// Auction Started Response
{
    "type":"product_updates",
    "event":"start_auction",
    "product":{
        "id":17,
        "symbol":"NEOUSDQ",
        "trading_status":"disrupted_post_only",
    },
    "timestamp": 1561634049751430,
}

// Auction Finished Response
{
    "type":"product_updates",
    "event":"finish_auction",
    "product":{
        "id":17,
        "symbol":"NEOUSDQ",
        "trading_status":"operational",
    },
    "timestamp": 1561634049751430,
}
```
### Market Disruption
When markets are disrupted, orderbook enters into cancel only mode. You can refer to "trading_status" field in product info to determine this. In cancel only mode, you can only cancel your orders. No matching happens in this mode.

### Auction Started
When markets need to come up, we conduct a single price auction. In this case, orderbook enters into post only mode. In post only mode, you can post new orders, cancel exisiting orders, add more margin to open positions. No matching happens in this mode. It is possible to see an overlap between asks and bids during this time.

### Auction Finished
When auction finishes, markets enter into operational mode and trading continues as usual. 

You can read more about the single price auction [here](https://www.delta.exchange/blog/bootstrapping-liquidity-using-auctions/)

## system_status

**Note:** This channel is now available on the new [public channel websocket endpoint](30-websocket-feed.md#websocket-feed). It will be deprecated from the [private channel websocket endpoint](30-websocket-feed.md#websocket-feed) on 31st July 2026.

This is a public websocket channel that provides updates on system-wide status events such as scheduled maintenance, maintenance start and finish, degraded mode, and fallback operation. No symbols are required when subscribing to this channel. Below are the types of messages sent for more details:
> System status Sample

```json
//Subscribe
{
    "type": "subscribe",
    "payload": {
        "channels": [
            {
                "name": "system_status"
            }
        ]
    }
}
```

```json
// Maintenance Scheduled Response
{
    "type": "system_status",
    "status": "live",
    "event": "maintenance_scheduled",
    "maintenance_start_time": 1765259125000000, // estimated maintenance start time in microseconds
    "maintenance_announcement_time": 1764548092000000, // estimated maintenance announcement time in microseconds
    "maintenance_finish_time": 1765259428000000, // estimated finish time
    "timestamp": 1765239292000000
}

// Maintenance Started Response
{
    "type":"system_status",
    "status": "maintenance",
    "event":"maintenance_started",
    "maintenance_start_time": 1765259301000000, // estimated maintenance start time in microseconds
    "maintenance_announcement_time": 1764720892000000, // estimated maintenance announcement time in microseconds
    "maintenance_finish_time": 1765259450000000, // estimated finish time in microseconds.
    "timestamp": 1765259716000000
}

// Maintenance Cancelled Response
{
    "type":"system_status",
    "status": "api_fallback", // current status
    "event":"maintenance_cancelled",
    "maintenance_start_time": 1765259325000000, // estimated maintenance start time in microseconds
    "maintenance_announcement_time": 1764807292000000, // estimated maintenance announcement time in microseconds
    "maintenance_finish_time": 1765259526000000, // estimated finish time in microseconds.
    "timestamp": 1765259727000000
}

// Maintenance Finished Response
{
    "type":"system_status",
    "status": "live",
    "event":"maintenance_finished",
    "maintenance_start_time": 1765259338000000, // estimated maintenance start time in microseconds
    "maintenance_announcement_time": 1764634492000000, // estimated maintenance announcement time in microseconds
    "maintenance_finish_time": 1765259575000000, // estimated finish time in microseconds.
    "timestamp": 1765259744000000
}
```

snapshot → This event is sent as soon as you subscribe to the system_status channel. The data in this event contains the current system status details.

1. "event": "maintenance_scheduled" is sent when maintenance is scheduled, usually 6 to 24 hours before the actual maintenance. It includes the estimated start and finish times.  
2. "event": "maintenance_started" is sent when maintenance begins. It indicates service disruption and includes the estimated finish time. For unscheduled maintenance, this event may be sent directly without the prior maintenance_scheduled event.  
3. "event": "maintenance_finished" is sent when maintenance is complete. Usually, after this event, there is an auction period lasting around 5 to 10 minutes.  
4. "event": "maintenance_cancelled" is sent when upcoming scheduled maintenance has been cancelled.

Note: Maintenance start and finish times are approximate estimates. The actual start time is confirmed by the maintenance_started event, and the actual completion is confirmed by the maintenance_finished event.

These values describe the current state of the entire system.

The payload["status"] describe the current state of the entire system. Below are the possible values:

1. "live": The system is operating normally. All services (REST APIs, WebSocket, backend processes) are functioning as expected.  
2. "maintenance": The system is currently under maintenance. Some features or services may be temporarily unavailable or disrupted.  
3. "api_fallback": Our system might be facing some technical issues, but most core functions remain available. Mostly used by our internal system. You can treat this as "live" mode, and check with our support team.  
4. "degraded_mode": Our system might be facing some technical issues, but most core functions remain available. Mostly used by our internal system. You can treat this as "live" mode, and check with our support team.  

Changing status to between these three: ["api_fallback", "degraded_mode", "live"] is done by sending message with 

"event":  "app_status_update".

e.g. payload = %{type: "system_status", event: "app_status_update", status: "api_fallback", maintenance_announcement_time: time, maintenance_start_time: time, maintenance_finish_time: time, timestamp: current_time}

Note: The "app_status_update" messages will still contain correct maintenance related timestamps.

In addition to the event field, the status field reflects the overall system state, such as: live, maintenance, api_fallback, or degraded_mode.
All timestamps are in epoch microseconds.
