> Source: https://docs.arrow.trade/rest-api/market-data/

# WebSocket Market Data API

Real-time market data streaming with ultra-low latency for institutional-grade trading applications. Get live price feeds, market depth, and trading analytics through persistent WebSocket connections.

## Overview

The WebSocket Market Data API delivers professional-grade real-time market data with sub-second latency, making it essential for algorithmic trading, portfolio management platforms, and advanced trading applications requiring instant market updates.

### Key Features

  * **Ultra-Low Latency** : Sub-second market data updates with optimized binary protocols
  * **Multiple Data Modes** : Choose from LTP, LTPC, Quote, or Full market depth based on your needs
  * **Efficient Binary Protocol** : Compact data packets (13–249 bytes) for minimal bandwidth usage
  * **Real-Time Market Depth** : Complete order book with 5-level bid/ask data
  * **Cross-Exchange Support** : Unified data stream across NSE, BSE, NFO, BFO, and MCX
  * **Scalable Architecture** : Handle thousands of instrument subscriptions simultaneously

## Connection Setup

### WebSocket Endpoint

```
wss://ds.arrow.trade
```

### Authentication Parameters

Connect using your application credentials as query parameters:

#### JavaScript

BashJavascriptPython

```bash
# Test connection
websocat "wss://ds.arrow.trade?appID=<YOUR_APP_ID>&token=<YOUR_TOKEN>"
```

```javascript
const wsUrl = `wss://ds.arrow.trade?appID=${YOUR_APP_ID}&token=${YOUR_TOKEN}`;
const ws = new WebSocket(wsUrl);

ws.onopen = function(event) {
    console.log('WebSocket connected');
};

ws.onmessage = function(event) {
    // Handle binary market data
    const data = new Uint8Array(event.data);
    const marketData = parseMarketData(data);
};
```

```python
import websocket
import struct

ws_url = f"wss://ds.arrow.trade?appID={YOUR_APP_ID}&token={YOUR_TOKEN}"

def on_message(ws, message):
    # Parse binary market data
    market_data = parse_market_data(message)

def on_open(ws):
    print("WebSocket connected")

ws = websocket.WebSocketApp(ws_url,
                        on_message=on_message,
                        on_open=on_open)
ws.run_forever()
```

## Subscription Management

### Message Format

All subscription messages follow this JSON structure:

```json
{
    "code": "SUBSCRIPTION_MODE",
    "mode": "DATA_MODE",
    "DATA_MODE": [array_of_tokens]
}
```

### Subscription Modes

Mode | Description | Use Case
---|---|---
`sub` | Subscribe to instruments | Start receiving data for specified tokens
`unsub` | Unsubscribe from instruments | Stop data feed for specified tokens

### Data Modes

Mode | Description | Packet Size | Update Frequency | Best For
---|---|---|---|---
`ltpc` | Last Traded Price + Previous Close | 17 bytes | Real-time | Basic price monitoring
`ltp` | Last Traded Price only | 13 bytes | Real-time | High-frequency price feeds
`quote` | Complete quote without depth | 93 bytes | Real-time | Comprehensive market view
`full` | Complete data with market depth | 249 bytes | Real-time | Order book analysis

## Subscription Examples

### Subscribe to Basic Price Data (LTPC)

```json
{
    "code": "sub",
    "mode": "ltpc",
    "ltpc": [26009, 26000, 256265]
}
```

### Subscribe to High-Frequency Price Feed (LTP)

```json
{
    "code": "sub",
    "mode": "ltp",
    "ltp": [26009, 26000]
}
```

### Subscribe to Complete Market Data (Quote)

```json
{
    "code": "sub",
    "mode": "quote",
    "quote": [26009, 26000, 256265]
}
```

### Subscribe to Full Market Depth

```json
{
    "code": "sub",
    "mode": "full",
    "full": [26009, 26000]
}
```

### Unsubscribe from Instruments

```json
{
    "code": "unsub",
    "mode": "ltpc",
    "ltpc": [26009]
}
```

## Binary Data Structures

All market data is received as binary packets for maximum efficiency. Parse using the appropriate structure based on your subscription mode.

### LTPC Mode (17 bytes)

Enhanced LTP data with previous day closing price for accurate P&L calculations.

Bytes | Field | Type | Description
---|---|---|---
0-4 | Token | `int32` | Unique instrument identifier
4-8 | LTP | `int32` | Last traded price (scaled)
8-9 | Net Change Indicator | `int8` | Direction: +1 (up), -1 (down), 0 (unchanged)
9-13 | Net Change | `int32` | Absolute price change from previous close
13-17 | Previous Close | `int32` | Previous trading session close price

> **Note:** LTPC mode includes previous day closing price, enabling accurate net change calculations based on closing price rather than settlement price.

### Complete Market Data Structure (Quote Mode - 93 bytes)

Comprehensive market data including OHLC, volume, and open interest.

Bytes | Field | Type | Description
---|---|---|---
0-4 | Token | `int32` | Instrument identifier
4-8 | LTP | `int32` | Last traded price
8-9 | Net Change Indicator | `int8` | Price direction
9-13 | Net Change | `int32` | Price change amount
13-17 | LTQ | `int32` | Last traded quantity
17-21 | Average Price | `int32` | Volume-weighted average price
21-29 | Total Buy Quantity | `int64` | Cumulative buy orders
29-37 | Total Sell Quantity | `int64` | Cumulative sell orders
37-41 | Open | `int32` | Session opening price
41-45 | High | `int32` | Session highest price
45-49 | Close | `int32` | Previous session close
49-53 | Low | `int32` | Session lowest price
53-61 | Volume | `int64` | Total traded volume
61-65 | LTT | `int32` | Last trade time (epoch)
65-69 | Exchange Time | `int32` | Exchange timestamp
69-77 | Open Interest | `int64` | Current open interest
77-85 | OI Day High | `int64` | Highest OI during session
85-93 | OI Day Low | `int64` | Lowest OI during session

Futures volume vs HFT (TBT) feed

This Data Stream uses exchange **bcast** data. For **futures (FO)** instruments, `volume` here can be **higher** than on the [HFT Data Stream](../hft-stream/#market-data-packets), which is built from **TBT** data and counts only trades on the subscribed instrument token. Bcast aggregates may include volume from the **spread order book** across related legs. Compare feeds only after accounting for this difference.

### Full Market Data Structure (249 bytes)

Complete market data with 5-level order book depth.

Bytes | Field | Type | Description
---|---|---|---
0-93 | Base Market Data | `bytes` | Same structure as Quote mode
93-97 | Lower Circuit | `int32` | Lower price limit
97-101 | Upper Circuit | `int32` | Upper price limit
101-109 | Reserved | `bytes` | Reserved (8 bytes)
109-249 | Market Depth | `bytes` | Order book data (5 bids + 5 asks)

## Market Depth Structure (Full Mode)

The market depth provides a complete 5-level order book with bid/ask prices, quantities, and order counts.

### Depth Layout (140 bytes total, starting at offset 109)

Each depth level contains 14 bytes: \- **Quantity** : 8 bytes (`int64`) \- **Price** : 4 bytes (`int32`) \- **Orders** : 2 bytes (`int16`)

Position | Level | Data | Structure
---|---|---|---
109-123 | Bid 1 | Best buy orders | Quantity (8) + Price (4) + Orders (2)
123-137 | Bid 2 | Second best buy | Quantity (8) + Price (4) + Orders (2)
137-151 | Bid 3 | Third best buy | Quantity (8) + Price (4) + Orders (2)
151-165 | Bid 4 | Fourth best buy | Quantity (8) + Price (4) + Orders (2)
165-179 | Bid 5 | Fifth best buy | Quantity (8) + Price (4) + Orders (2)
179-193 | Ask 1 | Best sell orders | Quantity (8) + Price (4) + Orders (2)
193-207 | Ask 2 | Second best sell | Quantity (8) + Price (4) + Orders (2)
207-221 | Ask 3 | Third best sell | Quantity (8) + Price (4) + Orders (2)
221-235 | Ask 4 | Fourth best sell | Quantity (8) + Price (4) + Orders (2)
235-249 | Ask 5 | Fifth best sell | Quantity (8) + Price (4) + Orders (2)

## Implementation Examples

### Complete WebSocket Client

#### JavaScript

JavascriptPython

```javascript
class MarketDataClient {
    constructor(appID, token) {
        this.wsUrl = `wss://ds.arrow.trade?appID=${appID}&token=${token}`;
        this.ws = null;
        this.subscribers = new Map();
    }

    connect() {
        return new Promise((resolve, reject) => {
            this.ws = new WebSocket(this.wsUrl);

            this.ws.onopen = () => {
                console.log('WebSocket connected');
                resolve();
            };

            this.ws.onmessage = (event) => {
                this.handleMessage(event.data);
            };

            this.ws.onerror = (error) => {
                console.error('WebSocket error:', error);
                reject(error);
            };

            this.ws.onclose = () => {
                console.log('WebSocket disconnected');
                this.reconnect();
            };
        });
    }

    subscribe(mode, tokens, callback) {
        const message = {
            code: 'sub',
            mode: mode,
            [mode]: tokens
        };

        this.ws.send(JSON.stringify(message));

        tokens.forEach(token => {
            this.subscribers.set(token, callback);
        });
    }

    handleMessage(data) {
        const buffer = new Uint8Array(data);
        const marketData = this.parseMarketData(buffer);

        const callback = this.subscribers.get(marketData.token);
        if (callback) {
            callback(marketData);
        }
    }

    parseMarketData(buffer) {
        if (buffer.length === 17) {
            return this.parseLTPC(buffer);
        } else if (buffer.length === 13) {
            return this.parseLTP(buffer);
        } else if (buffer.length === 93) {
            return this.parseQuote(buffer);
        } else if (buffer.length === 249) {
            return this.parseFull(buffer);
        }
    }

    parseLTPC(data) {
        const tick = {};
        tick.token = this.bigEndianToInt(data.slice(0, 4));
        tick.ltp = this.bigEndianToInt(data.slice(4, 8));
        tick.close = this.bigEndianToInt(data.slice(13, 17));
        tick.netChange = Math.round(
            (((tick.ltp - tick.close) / tick.close) * 100 + Number.EPSILON) * 100
        ) / 100 || 0;

        if (tick.ltp > tick.close) {
            tick.changeFlag = 43; // ascii code for +
        } else if (tick.ltp < tick.close) {
            tick.changeFlag = 45; // ascii code for -
        } else {
            tick.changeFlag = 32; // no change
        }

        return tick;
    }

    parseQuote(data) {
        const tick = this.parseLTPC(data);

        tick.ltq = this.bigEndianToInt(data.slice(13, 17));
        tick.avgPrice = this.bigEndianToInt(data.slice(17, 21));
        tick.totalBuyQuantity = this.bigEndianToInt(data.slice(21, 29));
        tick.totalSellQuantity = this.bigEndianToInt(data.slice(29, 37));
        tick.open = this.bigEndianToInt(data.slice(37, 41));
        tick.high = this.bigEndianToInt(data.slice(41, 45));
        tick.close = this.bigEndianToInt(data.slice(45, 49));
        tick.low = this.bigEndianToInt(data.slice(49, 53));
        tick.volume = this.bigEndianToInt(data.slice(53, 61));
        tick.ltt = this.bigEndianToInt(data.slice(61, 65));
        tick.time = this.bigEndianToInt(data.slice(65, 69));
        tick.oi = this.bigEndianToInt(data.slice(69, 77));
        tick.oiDayHigh = this.bigEndianToInt(data.slice(77, 85));
        tick.oiDayLow = this.bigEndianToInt(data.slice(85, 93));

        // Recalculate net change with correct close price
        tick.netChange = Math.round(
            (((tick.ltp - tick.close) / tick.close) * 100 + Number.EPSILON) * 100
        ) / 100 || 0;

        if (tick.ltp > tick.close) {
            tick.changeFlag = 43; // ascii code for +
        } else if (tick.ltp < tick.close) {
            tick.changeFlag = 45; // ascii code for -
        } else {
            tick.changeFlag = 32; // no change
        }

        return tick;
    }

    parseFull(data) {
        const tick = this.parseQuote(data);

        tick.lowerLimit = this.bigEndianToInt(data.slice(93, 97));
        tick.upperLimit = this.bigEndianToInt(data.slice(97, 101));

        const bids = [];
        const asks = [];

        const depthOffset = 109;

        for (let i = 0; i < 10; i++) {
            const offset = depthOffset + i * 14;
            const quantity = this.bigEndianToInt(data.slice(offset, offset + 8));
            const price = this.bigEndianToInt(data.slice(offset + 8, offset + 12));
            const orders = this.bigEndianToInt(data.slice(offset + 12, offset + 14));

            if (i >= 5) {
                asks.push({ price, quantity, orders });
            } else {
                bids.push({ price, quantity, orders });
            }
        }

        tick.bids = bids;
        tick.asks = asks;

        return tick;
    }

    bigEndianToInt(buffer) {
        let result = 0;
        for (let i = 0; i < buffer.length; i++) {
            result = (result << 8) | buffer[i];
        }
        return result;
    }
}

// Usage
const client = new MarketDataClient('your_app_id', 'your_token');
await client.connect();

client.subscribe('ltpc', [26009, 26000], (data) => {
    console.log(`${data.token}: LTP=${data.ltp}, Change=${data.netChange}%`);
});
```

```python
import websocket
import json
import struct
from threading import Thread

class MarketDataClient:
    def __init__(self, app_id, token):
        self.ws_url = f"wss://ds.arrow.trade?appID={app_id}&token={token}"
        self.ws = None
        self.subscribers = {}

    def connect(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            self.ws_url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )

        wst = Thread(target=self.ws.run_forever)
        wst.daemon = True
        wst.start()

    def subscribe(self, mode, tokens, callback):
        message = {
            'code': 'sub',
            'mode': mode,
            mode: tokens
        }

        self.ws.send(json.dumps(message))

        for token in tokens:
            self.subscribers[token] = callback

    def on_message(self, ws, message):
        market_data = self.parse_market_data(message)

        callback = self.subscribers.get(market_data['token'])
        if callback:
            callback(market_data)

    def parse_market_data(self, data):
        if len(data) == 17:
            return self.parse_ltpc(data)
        elif len(data) == 13:
            return self.parse_ltp(data)
        elif len(data) == 93:
            return self.parse_quote(data)
        elif len(data) == 249:
            return self.parse_full(data)

    def parse_ltpc(self, data):
        tick = {}
        tick['token'] = struct.unpack('>I', data[0:4])[0]
        tick['ltp'] = struct.unpack('>I', data[4:8])[0]
        tick['close'] = struct.unpack('>I', data[13:17])[0]

        if tick['close'] != 0:
            tick['net_change'] = round(
                (((tick['ltp'] - tick['close']) / tick['close']) * 100), 2
            )
        else:
            tick['net_change'] = 0

        return tick

    def parse_quote(self, data):
        tick = self.parse_ltpc(data)

        tick['ltq'] = struct.unpack('>I', data[13:17])[0]
        tick['avg_price'] = struct.unpack('>I', data[17:21])[0]
        tick['total_buy_quantity'] = struct.unpack('>Q', data[21:29])[0]
        tick['total_sell_quantity'] = struct.unpack('>Q', data[29:37])[0]
        tick['open'] = struct.unpack('>I', data[37:41])[0]
        tick['high'] = struct.unpack('>I', data[41:45])[0]
        tick['close'] = struct.unpack('>I', data[45:49])[0]
        tick['low'] = struct.unpack('>I', data[49:53])[0]
        tick['volume'] = struct.unpack('>Q', data[53:61])[0]
        tick['ltt'] = struct.unpack('>I', data[61:65])[0]
        tick['time'] = struct.unpack('>I', data[65:69])[0]
        tick['oi'] = struct.unpack('>Q', data[69:77])[0]
        tick['oi_day_high'] = struct.unpack('>Q', data[77:85])[0]
        tick['oi_day_low'] = struct.unpack('>Q', data[85:93])[0]

        # Recalculate net change with correct close price
        if tick['close'] != 0:
            tick['net_change'] = round(
                (((tick['ltp'] - tick['close']) / tick['close']) * 100), 2
            )
        else:
            tick['net_change'] = 0

        return tick

    def parse_full(self, data):
        tick = self.parse_quote(data)

        tick['lower_limit'] = struct.unpack('>I', data[93:97])[0]
        tick['upper_limit'] = struct.unpack('>I', data[97:101])[0]

        bids = []
        asks = []

        depth_offset = 109

        for i in range(10):
            offset = depth_offset + i * 14
            quantity = struct.unpack('>Q', data[offset:offset+8])[0]
            price = struct.unpack('>I', data[offset+8:offset+12])[0]
            orders = struct.unpack('>H', data[offset+12:offset+14])[0]

            if i >= 5:
                asks.append({'price': price, 'quantity': quantity, 'orders': orders})
            else:
                bids.append({'price': price, 'quantity': quantity, 'orders': orders})

        tick['bids'] = bids
        tick['asks'] = asks

        return tick

# Usage
client = MarketDataClient('your_app_id', 'your_token')
client.connect()

def price_handler(data):
    print(f"{data['token']}: LTP={data['ltp']}, Change={data['net_change']}%")

client.subscribe('ltpc', [26009, 26000], price_handler)
```

## Error Handling and Reconnection

### Connection Management

```javascript
class ReconnectingWebSocket {
    constructor(url) {
        this.url = url;
        this.reconnectInterval = 5000;
        this.maxReconnectAttempts = 10;
        this.reconnectAttempts = 0;
    }

    connect() {
        this.ws = new WebSocket(this.url);

        this.ws.onopen = () => {
            this.reconnectAttempts = 0;
            this.resubscribeAll();
        };

        this.ws.onclose = () => {
            if (this.reconnectAttempts < this.maxReconnectAttempts) {
                setTimeout(() => {
                    this.reconnectAttempts++;
                    this.connect();
                }, this.reconnectInterval);
            }
        };
    }
}
```

### Common Error Scenarios

Error | Cause | Solution
---|---|---
**Connection Failed** | Invalid credentials | Verify `appID` and `token`
**Authentication Error** | Expired token | Refresh authentication token
**Data Corruption** | Network issues | Implement data validation
**Rate Limiting** | Too many subscriptions | Throttle subscription requests

## Performance Optimization

### Best Practices

**Subscription Management** \- **Batch Subscriptions** : Subscribe to multiple instruments in single requests \- **Mode Selection** : Use the minimal data mode required for your use case \- **Selective Unsubscription** : Remove unused subscriptions to reduce bandwidth \- **Connection Pooling** : Reuse connections across multiple data feeds

**Resource Management** \- **Memory Usage** : Parse and process data efficiently to prevent memory leaks
\- **CPU Optimization** : Use optimized binary parsers for high-frequency data \- **Network Bandwidth** : Monitor data throughput, especially with Full mode subscriptions \- **Buffer Management** : Implement proper buffer handling for binary data streams

## Market Data Applications

### Real-Time Portfolio Monitoring

```javascript
// Track P&L in real-time
function trackPortfolioValue(positions, marketData) {
    const currentValue = positions.reduce((total, position) => {
        const ltp = marketData[position.token]?.ltp || 0;
        const positionValue = position.quantity * ltp;
        return total + positionValue;
    }, 0);

    return currentValue;
}
```

### Order Book Analysis

```javascript
// Calculate bid-ask spread and depth
function analyzeOrderBook(depth) {
    const bestBid = depth.bids[0];
    const bestAsk = depth.asks[0];

    return {
        spread: bestAsk.price - bestBid.price,
        spreadPercent: ((bestAsk.price - bestBid.price) / bestBid.price) * 100,
        bidDepth: depth.bids.reduce((sum, level) => sum + level.quantity, 0),
        askDepth: depth.asks.reduce((sum, level) => sum + level.quantity, 0)
    };
}
```

### Alert Systems

```javascript
// Price movement alerts
function createPriceAlert(token, threshold, callback) {
    return (marketData) => {
        if (marketData.token === token) {
            const changePercent = (marketData.netChange / marketData.previousClose) * 100;
            if (Math.abs(changePercent) >= threshold) {
                callback({
                    token: token,
                    change: changePercent,
                    ltp: marketData.ltp
                });
            }
        }
    };
}
```
