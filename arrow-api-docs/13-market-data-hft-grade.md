> Source: https://docs.arrow.trade/rest-api/hft-stream/

# Arrow HFT Datastream API

Real-time market data streaming via WebSocket with binary protocol for high-performance trading applications.

## Overview

The Arrow Dataserver API provides institutional-grade real-time market data streaming through persistent WebSocket connections. Built with a binary protocol for maximum efficiency, it supports Last Traded Price (LTP) and Full market depth data across NSE and BSE exchanges.

### Key Features

  * **Binary Protocol** : Optimized binary frames for minimal latency and bandwidth
  * **Zstd Compression** : Inbound market-data frames are zstd-compressed when `zstd=1` is set on the connection URL
  * **Dual Data Modes** : LTPC (compact) or Full (complete market depth)
  * **Flexible Symbol Formats** : Subscribe using symbol names or numeric IDs
  * **Cross-Exchange Coverage** : Unified data stream across NSE CM, NSE FO, BSE CM, and BSE FO
  * **Configurable Latency** : Adjust tick intervals upto 50ms (Super fast)
  * **Scalable Architecture** : Up to 1,024 subscribed symbols per connection; up to 512 symbols per subscription request

## Connection Setup

### WebSocket Endpoint

```
wss://socket.arrow.trade?appID=<APP_ID>&token=<TOKEN>&zstd=1
```

Mandatory from 8 July 2026

**Zstd compression becomes mandatory on 8 July 2026.** After that date, the HFT feed sends only zstd-compressed inbound frames. Clients that connect without `zstd=1` or that do not decompress payloads before parsing will not receive usable market data.

Upgrade to a current **pyarrow-client** release (which handles decompression automatically) or update any custom WebSocket client before the cutoff.

### Connection Parameters

Parameter | Value | Description
---|---|---
`appID` | `APP_ID` | Application identifier
`token` | `TOKEN` | Authentication token
`zstd` | `1` | Request zstd-compressed inbound frames (required from 8 July 2026)

### Establishing Connection

JavaScript

```javascript
const wsUrl = 'wss://socket.arrow.trade?appID=APP_ID&token=TOKEN&zstd=1';
const ws = new WebSocket(wsUrl);

ws.binaryType = 'arraybuffer';

ws.onopen = function(event) {
    console.log('Connected to Arrow Dataserver');
};

ws.onmessage = function(event) {
    const data = new Uint8Array(event.data);
    const marketData = parseMarketData(data);
    console.log(marketData);
};
```

Python

```python
import websocket
import struct
import zstandard as zstd

ws_url = "wss://socket.arrow.trade?appID=APP_ID&token=TOKEN&zstd=1"
zdec = zstd.ZstdDecompressor()

def on_message(ws, message):
    payload = zdec.decompress(bytes(message))
    market_data = parse_market_data(payload)
    print(market_data)

def on_open(ws):
    print("Connected to Arrow Dataserver")

ws = websocket.WebSocketApp(
    ws_url,
    on_message=on_message,
    on_open=on_open
)
ws.run_forever()
```

Bash

```bash
# Test connection using websocat
websocat "wss://socket.arrow.trade?appID=<APP_ID>&token=<TOKEN>&zstd=1"
```

## Subscription Management

### Request Format

All subscription requests are sent as JSON strings over the WebSocket connection.

Subscription limits

Each WebSocket connection supports a maximum of **1,024 subscribed symbols** in total. A single subscription request can include at most **512 symbols** (via `symbols` or `symIds`). To subscribe to the full 1,024-symbol allowance, send **two requests** with up to 512 symbols each—for example, one request with 512 symbols and a second request with the remaining 512.

```json
{
  "code": "string",
  "mode": "string",
  "symbols": ["string"],
  "latency": integer
}
```

### Request Fields

Field | Required | Type | Description
---|---|---|---
`code` | Yes | string | Action: `sub`/`s` (subscribe) or `unsub`/`u` (unsubscribe)
`mode` | Yes | string | Data mode: `ltpc`/`l` (compact) or `full`/`f` (complete)
`symbols` | Conditional | array | Symbol names (mutually exclusive with `symIds`)
`symIds` | Conditional | array | Symbol ID objects (mutually exclusive with `symbols`)
`latency` | No | integer | Tick interval in ms (upto 50, default: 1000)

### Data Modes

Mode | Shorthand | Packet Size | Description | Best For
---|---|---|---|---
`ltpc` | `l` | 40 bytes | Last Traded Price Compact | Basic price monitoring, high-frequency feeds
`full` | `f` | 196 bytes | Complete market data with depth | Order book analysis, full market view

## Symbol Naming Conventions

### Symbol Format Overview

Segment | Pattern | Example
---|---|---
NSE Cash Market | `NSE.<UNDERLYING>-<SERIES>` | `NSE.SBIN-EQ`
NSE Futures | `<UNDERLYING><DD><MON><YY>F` | `BANKNIFTY30DEC25F`
NSE Options | `<UNDERLYING><DD><MON><YY><C\|P><STRIKE>` | `NYKAA30DEC25C232.5`
BSE Cash Market | `BSE.<UNDERLYING>` | `BSE.SBIN`
BSE Futures | `<ASSET_TYPE><DD><MON><YY>F` | `SENSEX01JAN26F`
BSE Options | `<ASSET_TYPE><DD><MON><YY><C\|P><STRIKE>` | `SENSEX01JAN26C74900`

### NSE Cash Market (NSECM)

**Format** : `NSE.<UNDERLYING>-<SERIES>`

```
NSE.SBIN-EQ     → State Bank of India, Equity series
NSE.RELIANCE-EQ → Reliance Industries, Equity series
NSE.TCS-EQ      → Tata Consultancy Services, Equity series
```

### NSE Futures & Options (NSEFO)

**Options Format** : `<UNDERLYING><DD><MON><YY><C|P><STRIKE>`

  * `C` = Call Option
  * `P` = Put Option
  * Strike prices are in rupees (drop trailing `.0` for whole numbers)

```
NYKAA30DEC25C232.5  → NYKAA Call, 30-Dec-2025 expiry, Strike ₹232.50
NYKAA30DEC25P360    → NYKAA Put, 30-Dec-2025 expiry, Strike ₹360
NIFTY25JAN25C24000  → NIFTY Call, 25-Jan-2025 expiry, Strike ₹24,000
```

**Futures Format** : `<UNDERLYING><DD><MON><YY>F`

```
BANKNIFTY30DEC25F   → Bank Nifty Future, 30-Dec-2025 expiry
NIFTY25JAN25F       → Nifty Future, 25-Jan-2025 expiry
```

### BSE Cash Market (BSECM)

**Format** : `BSE.<UNDERLYING>`

```
BSE.SBIN      → State Bank of India
BSE.RELIANCE  → Reliance Industries
BSE.HDFC      → HDFC Bank
```

### BSE Futures & Options (BSEFO)

**Options Format** : `<ASSET_TYPE><DD><MON><YY><C|P><STRIKE>`

```
SENSEX01JAN26C74900 → SENSEX Call, 01-Jan-2026 expiry, Strike ₹74,900
SENSEX01JAN26P74000 → SENSEX Put, 01-Jan-2026 expiry, Strike ₹74,000
```

**Futures Format** : `<ASSET_TYPE><DD><MON><YY>F`

```
SENSEX01JAN26F → SENSEX Future, 01-Jan-2026 expiry
```

## Subscription Examples

### Subscribe Using Symbol Names

```json
{
  "code": "sub",
  "mode": "full",
  "symbols": ["NSE.SBIN-EQ", "BSE.RELIANCE"],
  "latency": 200
}
```

### Subscribe Using Symbol IDs

```json
{
  "code": "sub",
  "mode": "full",
  "symIds": [
    {
      "exch_seg": 1,
      "ids": [5042, 4449, 91]
    },
    {
      "exch_seg": 2,
      "ids": [100, 200]
    }
  ]
}
```

### Subscribe to LTPC Mode

```json
{
  "code": "sub",
  "mode": "ltpc",
  "symbols": ["NSE.SBIN-EQ", "NSE.RELIANCE-EQ"],
  "latency": 100
}
```

### Unsubscribe from Symbols

```json
{
  "code": "unsub",
  "mode": "full",
  "symbols": ["NSE.SBIN-EQ"]
}
```

### Using Shorthand Codes

```json
{
  "code": "s",
  "mode": "l",
  "symbols": ["NSE.SBIN-EQ"],
  "l": 500
}
```

## Exchange Segments

Value | Segment | Description
---|---|---
0 | NSE_CM | NSE Cash Market
1 | NSE_FO | NSE Futures & Options
2 | BSE_CM | BSE Cash Market
3 | BSE_FO | BSE Futures & Options

## Inbound compression (zstd)

When `zstd=1` is present on the connection URL, **inbound** WebSocket binary messages are zstd-compressed. Outbound subscription commands remain plain JSON strings.

**Client flow**

  1. Connect with `zstd=1` in the query string.
  2. On each binary `message` event, **decompress** the raw bytes with a zstd decoder.
  3. Parse one or more binary frames from the decompressed buffer (frames may be concatenated in a single message).

**Frame detection**

Frame type | Size (bytes) | Size field | Packet type offset
---|---|---|---
Response | 540 | uint32 at offset 0 | byte 4 (`99`)
LTP | 40 | int16 at offset 0 | byte 2 (`1`)
Full | 196 | int16 at offset 0 | byte 2 (`2`)

Inspect response frames first (540-byte layout differs from LTP/full). After identifying frame length `n`, consume `payload[0:n]` and continue with any remaining bytes.

**Python** — `pip install zstandard`, then `ZstdDecompressor().decompress(raw_bytes)`.

**JavaScript / Node.js** — use a zstd library such as [`fzstd`](https://www.npmjs.com/package/fzstd) and decompress before parsing frames.

The official **pyarrow-client** SDK enables compression and decompression automatically in `HFTDataStream`; custom clients must implement the steps above.

## Binary Response Format

### Response Packet Structure (540 bytes)

After each subscription request, the server sends a binary acknowledgment packet.

Offset | Size | Type | Field | Description
---|---|---|---|---
0 | 4 | uint32 | size | Total packet size
4 | 1 | uint8 | pktType | 99 (PKT_TYPE_RESPONSE)
5 | 1 | uint8 | exchSeg | 0 (not used)
6 | 16 | char[] | error_code | Error code string (null-terminated)
22 | 512 | char[] | error_msg | Error message (null-terminated)
534 | 1 | uint8 | request_type | 0=subscribe, 1=unsubscribe
535 | 1 | uint8 | mode | 0=ltpc, 1=full
536 | 2 | uint16 | success_count | Number of successful symbols
538 | 2 | uint16 | error_count | Number of failed symbols

### Error Codes

Code | Description
---|---
`SUCCESS` | All symbols processed successfully
`E_PARTIAL` | Some symbols failed
`E_ALL_INVALID` | All symbols failed
`E_INVALID_JSON` | Malformed JSON request
`E_MISSING_FIELD` | Required field missing
`E_INVALID_PARAM` | Invalid parameter value
`E_PARSE_ERROR` | General parsing error

## Market Data Packets

Futures volume vs other data feeds

When subscribing to **futures (FO)** instruments, the `volume` field on this feed is often **lower** than on other Arrow market data streams or third-party sources.

The HFT stream is built from exchange **TBT (Tick-by-Tick)** data. Volume counts only trades executed on **that specific instrument token**.

The standard [Data Stream](../market-data/) and most broadcast-based feeds use **bcast** data, where aggregated futures volume can include activity attributed to the **spread order book** across related legs—not just the single contract you subscribed to.

Do not compare HFT futures volume directly against bcast-based feeds without accounting for this difference.

### LTP Packet (LTPC Mode - 40 bytes)

Compact price data for high-frequency monitoring.

Offset | Size | Type | Field | Description
---|---|---|---|---
0 | 2 | int16 | size | Packet size (40)
2 | 1 | uint8 | pktType | 1 (PKT_TYPE_LTP)
3 | 1 | uint8 | exchSeg | Exchange segment
4 | 4 | int32 | symId | Symbol/Token ID
8 | 4 | int32 | ltp | Last traded price (paise)
12 | 4 | int32 | vwap | Volume-weighted average price
16 | 8 | int64 | volume | Traded volume (units)
24 | 8 | uint64 | ltt | Last traded time (seconds)
32 | 4 | uint32 | atv | Ask traded volume
36 | 4 | uint32 | btv | Buy traded volume

### Full Packet (Full Mode - 196 bytes)

Complete market data with 5-level order book depth.

Offset | Size | Type | Field | Description
---|---|---|---|---
0 | 2 | int16 | size | Packet size (196)
2 | 1 | uint8 | pktType | 2 (PKT_TYPE_FULL)
3 | 1 | uint8 | exchSeg | Exchange segment
4 | 4 | int32 | token | Symbol/Token ID
8 | 4 | int32 | ltp | Last traded price
12 | 4 | int32 | ltq | Last traded quantity
16 | 4 | int32 | vwap | Volume-weighted average price
20 | 4 | int32 | open | Open price
24 | 4 | int32 | high | High price
28 | 4 | int32 | close | Close price
32 | 4 | int32 | low | Low price
36 | 4 | int32 | ltt | Last traded time (seconds)
40 | 4 | int32 | dpr_l | Day price range low
44 | 4 | int32 | dpr_h | Day price range high
48 | 8 | int64 | tbq | Total buy quantity
56 | 8 | int64 | tsq | Total sell quantity
64 | 8 | int64 | volume | Total volume
72 | 20 | int32[5] | bid_px | Best 5 bid prices
92 | 20 | int32[5] | ask_px | Best 5 ask prices
112 | 20 | int32[5] | bid_size | Best 5 bid quantities
132 | 20 | int32[5] | ask_size | Best 5 ask quantities
152 | 10 | uint16[5] | bid_ord | Bid order counts (levels 1-5)
162 | 10 | uint16[5] | ask_ord | Ask order counts (levels 1-5)
172 | 8 | uint64 | oi | Open interest
180 | 8 | uint64 | ts | Server timestamp (epoch ns)
188 | 4 | uint32 | atv | Ask traded volume
192 | 4 | uint32 | btv | Buy traded volume

## Implementation Examples

### Complete WebSocket Client

JavaScript

```javascript
class ArrowDataserverClient {
    constructor() {
        this.wsUrl = 'wss://socket.arrow.trade?appID=APP_ID&token=TOKEN&zstd=1';
        this.ws = null;
        this.callbacks = new Map();
    }

    connect() {
        return new Promise((resolve, reject) => {
            this.ws = new WebSocket(this.wsUrl);
            this.ws.binaryType = 'arraybuffer';

            this.ws.onopen = () => {
                console.log('Connected to Arrow Dataserver');
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
                console.log('Disconnected from Arrow Dataserver');
                this.reconnect();
            };
        });
    }

    subscribe(mode, symbols, latency, callback) {
        const message = {
            code: 'sub',
            mode: mode,
            symbols: symbols,
            latency: latency || 1000
        };
        this.ws.send(JSON.stringify(message));
        symbols.forEach(sym => this.callbacks.set(sym, callback));
    }

    subscribeByIds(mode, symIds, latency, callback) {
        const message = {
            code: 'sub',
            mode: mode,
            symIds: symIds,
            latency: latency || 1000
        };
        this.ws.send(JSON.stringify(message));
    }

    unsubscribe(mode, symbols) {
        const message = {
            code: 'unsub',
            mode: mode,
            symbols: symbols
        };
        this.ws.send(JSON.stringify(message));
        symbols.forEach(sym => this.callbacks.delete(sym));
    }

    handleMessage(data) {
        // Decompress with your zstd library (e.g. fzstd in Node.js)
        const payload = fzstd.decompress(new Uint8Array(data));
        this.dispatchPayload(payload);
    }

    dispatchPayload(payload) {
        let offset = 0;
        while (offset < payload.length) {
            const view = new DataView(payload.buffer, payload.byteOffset + offset, payload.length - offset);
            const frame = this.nextFrame(view);
            if (!frame) break;
            if (frame.type === 'ltp') {
                this.notifyCallbacks(this.parseLTP(frame.bytes));
            } else if (frame.type === 'full') {
                this.notifyCallbacks(this.parseFull(frame.bytes));
            } else if (frame.type === 'response') {
                console.log('Subscription response:', this.parseResponse(frame.bytes));
            }
            offset += frame.size;
        }
    }

    nextFrame(view) {
        if (view.byteLength >= 540 &&
            view.getUint32(0, true) === 540 &&
            view.getUint8(4) === 99) {
            return { type: 'response', size: 540, bytes: new Uint8Array(view.buffer, view.byteOffset, 540) };
        }
        if (view.byteLength >= 40) {
            const size = view.getInt16(0, true);
            if (size === 40 && view.getUint8(2) === 1) {
                return { type: 'ltp', size: 40, bytes: new Uint8Array(view.buffer, view.byteOffset, 40) };
            }
        }
        if (view.byteLength >= 196) {
            const size = view.getInt16(0, true);
            if (size === 196 && view.getUint8(2) === 2) {
                return { type: 'full', size: 196, bytes: new Uint8Array(view.buffer, view.byteOffset, 196) };
            }
        }
        return null;
    }

    parseLTP(data) {
        const buffer = new DataView(data.buffer, data.byteOffset, data.byteLength);
        return {
            pktType: buffer.getUint8(2),
            exchSeg: buffer.getUint8(3),
            symId: buffer.getInt32(4, true),
            ltp: buffer.getInt32(8, true) / 100,
            vwap: buffer.getInt32(12, true) / 100,
            volume: Number(buffer.getBigInt64(16, true)),
            ltt: Number(buffer.getBigUint64(24, true)),
            atv: buffer.getUint32(32, true),
            btv: buffer.getUint32(36, true)
        };
    }

    parseFull(data) {
        const buffer = new DataView(data.buffer, data.byteOffset, data.byteLength);
        const tick = {
            pktType: buffer.getUint8(2),
            exchSeg: buffer.getUint8(3),
            token: buffer.getInt32(4, true),
            ltp: buffer.getInt32(8, true) / 100,
            ltq: buffer.getInt32(12, true),
            vwap: buffer.getInt32(16, true) / 100,
            open: buffer.getInt32(20, true) / 100,
            high: buffer.getInt32(24, true) / 100,
            close: buffer.getInt32(28, true) / 100,
            low: buffer.getInt32(32, true) / 100,
            ltt: buffer.getInt32(36, true),
            dprLow: buffer.getInt32(40, true) / 100,
            dprHigh: buffer.getInt32(44, true) / 100,
            tbq: Number(buffer.getBigInt64(48, true)),
            tsq: Number(buffer.getBigInt64(56, true)),
            volume: Number(buffer.getBigInt64(64, true)),
            bidPrices: [],
            askPrices: [],
            bidSizes: [],
            askSizes: [],
            bidOrders: [],
            askOrders: [],
            oi: Number(buffer.getBigUint64(172, true)),
            timestamp: Number(buffer.getBigUint64(180, true)),
            atv: buffer.getUint32(188, true),
            btv: buffer.getUint32(192, true)
        };

        // Parse 5-level depth
        for (let i = 0; i < 5; i++) {
            tick.bidPrices.push(buffer.getInt32(72 + i * 4, true) / 100);
            tick.askPrices.push(buffer.getInt32(92 + i * 4, true) / 100);
            tick.bidSizes.push(buffer.getInt32(112 + i * 4, true));
            tick.askSizes.push(buffer.getInt32(132 + i * 4, true));
            tick.bidOrders.push(buffer.getUint16(152 + i * 2, true));
            tick.askOrders.push(buffer.getUint16(162 + i * 2, true));
        }

        return tick;
    }

    parseResponse(data) {
        const buffer = new DataView(data.buffer, data.byteOffset, data.byteLength);
        const decoder = new TextDecoder();
        const errorCodeBytes = new Uint8Array(buffer.buffer, buffer.byteOffset + 6, 16);
        const errorMsgBytes = new Uint8Array(buffer.buffer, buffer.byteOffset + 22, 512);

        return {
            size: buffer.getUint32(0, true),
            pktType: buffer.getUint8(4),
            errorCode: decoder.decode(errorCodeBytes).replace(/\0/g, ''),
            errorMsg: decoder.decode(errorMsgBytes).replace(/\0/g, ''),
            requestType: buffer.getUint8(534) === 0 ? 'subscribe' : 'unsubscribe',
            mode: buffer.getUint8(535) === 0 ? 'ltpc' : 'full',
            successCount: buffer.getUint16(536, true),
            errorCount: buffer.getUint16(538, true)
        };
    }

    notifyCallbacks(tick) {
        this.callbacks.forEach((callback) => {
            callback(tick);
        });
    }

    reconnect() {
        setTimeout(() => {
            console.log('Reconnecting...');
            this.connect();
        }, 5000);
    }
}

// Usage
const client = new ArrowDataserverClient();

await client.connect();

client.subscribe('full', ['NSE.SBIN-EQ', 'NSE.RELIANCE-EQ'], 200, (tick) => {
    console.log(`Token: ${tick.token}, LTP: ₹${tick.ltp}, Volume: ${tick.volume}`);
});
```

Python

```python
import websocket
import json
import struct
import zstandard as zstd
from threading import Thread

class ArrowDataserverClient:
    def __init__(self):
        self.ws_url = "wss://socket.arrow.trade?appID=APP_ID&token=TOKEN&zstd=1"
        self.ws = None
        self.callbacks = {}
        self.zdec = zstd.ZstdDecompressor()

    def connect(self):
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

    def on_open(self, ws):
        print("Connected to Arrow Dataserver")

    def on_error(self, ws, error):
        print(f"WebSocket error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("Disconnected from Arrow Dataserver")

    def subscribe(self, mode, symbols, latency=1000, callback=None):
        message = {
            'code': 'sub',
            'mode': mode,
            'symbols': symbols,
            'latency': latency
        }
        self.ws.send(json.dumps(message))
        if callback:
            for sym in symbols:
                self.callbacks[sym] = callback

    def subscribe_by_ids(self, mode, sym_ids, latency=1000):
        message = {
            'code': 'sub',
            'mode': mode,
            'symIds': sym_ids,
            'latency': latency
        }
        self.ws.send(json.dumps(message))

    def unsubscribe(self, mode, symbols):
        message = {
            'code': 'unsub',
            'mode': mode,
            'symbols': symbols
        }
        self.ws.send(json.dumps(message))

    def on_message(self, ws, message):
        payload = self.zdec.decompress(bytes(message))
        self.dispatch_payload(payload)

    def dispatch_payload(self, payload):
        while payload:
            frame, payload = self.next_frame(payload)
            if frame is None:
                break
            if frame['type'] == 'ltp':
                tick = self.parse_ltp(frame['data'])
                self.notify_callbacks(tick)
            elif frame['type'] == 'full':
                tick = self.parse_full(frame['data'])
                self.notify_callbacks(tick)
            elif frame['type'] == 'response':
                response = self.parse_response(frame['data'])
                print(f"Subscription response: {response}")

    def next_frame(self, payload):
        if len(payload) >= 540:
            size = struct.unpack('<I', payload[0:4])[0]
            if size == 540 and payload[4] == 99:
                return {'type': 'response', 'data': payload[:540]}, payload[540:]
        if len(payload) >= 40:
            size = struct.unpack('<h', payload[0:2])[0]
            if size == 40 and payload[2] == 1:
                return {'type': 'ltp', 'data': payload[:40]}, payload[40:]
        if len(payload) >= 196:
            size = struct.unpack('<h', payload[0:2])[0]
            if size == 196 and payload[2] == 2:
                return {'type': 'full', 'data': payload[:196]}, payload[196:]
        return None, b''

    def parse_ltp(self, data):
        return {
            'pkt_type': struct.unpack('<B', data[2:3])[0],
            'exch_seg': struct.unpack('<B', data[3:4])[0],
            'sym_id': struct.unpack('<i', data[4:8])[0],
            'ltp': struct.unpack('<i', data[8:12])[0] / 100,
            'vwap': struct.unpack('<i', data[12:16])[0] / 100,
            'volume': struct.unpack('<q', data[16:24])[0],
            'ltt': struct.unpack('<Q', data[24:32])[0],
            'atv': struct.unpack('<I', data[32:36])[0],
            'btv': struct.unpack('<I', data[36:40])[0]
        }

    def parse_full(self, data):
        tick = {
            'pkt_type': struct.unpack('<B', data[2:3])[0],
            'exch_seg': struct.unpack('<B', data[3:4])[0],
            'token': struct.unpack('<i', data[4:8])[0],
            'ltp': struct.unpack('<i', data[8:12])[0] / 100,
            'ltq': struct.unpack('<i', data[12:16])[0],
            'vwap': struct.unpack('<i', data[16:20])[0] / 100,
            'open': struct.unpack('<i', data[20:24])[0] / 100,
            'high': struct.unpack('<i', data[24:28])[0] / 100,
            'close': struct.unpack('<i', data[28:32])[0] / 100,
            'low': struct.unpack('<i', data[32:36])[0] / 100,
            'ltt': struct.unpack('<i', data[36:40])[0],
            'dpr_low': struct.unpack('<i', data[40:44])[0] / 100,
            'dpr_high': struct.unpack('<i', data[44:48])[0] / 100,
            'tbq': struct.unpack('<q', data[48:56])[0],
            'tsq': struct.unpack('<q', data[56:64])[0],
            'volume': struct.unpack('<q', data[64:72])[0],
            'bid_prices': [],
            'ask_prices': [],
            'bid_sizes': [],
            'ask_sizes': [],
            'bid_orders': [],
            'ask_orders': [],
            'oi': struct.unpack('<Q', data[172:180])[0],
            'timestamp': struct.unpack('<Q', data[180:188])[0],
            'atv': struct.unpack('<I', data[188:192])[0],
            'btv': struct.unpack('<I', data[192:196])[0]
        }

        # Parse 5-level depth
        for i in range(5):
            tick['bid_prices'].append(struct.unpack('<i', data[72 + i*4:76 + i*4])[0] / 100)
            tick['ask_prices'].append(struct.unpack('<i', data[92 + i*4:96 + i*4])[0] / 100)
            tick['bid_sizes'].append(struct.unpack('<i', data[112 + i*4:116 + i*4])[0])
            tick['ask_sizes'].append(struct.unpack('<i', data[132 + i*4:136 + i*4])[0])
            tick['bid_orders'].append(struct.unpack('<H', data[152 + i*2:154 + i*2])[0])
            tick['ask_orders'].append(struct.unpack('<H', data[162 + i*2:164 + i*2])[0])

        return tick

    def parse_response(self, data):
        error_code = data[6:22].decode('utf-8').rstrip('\x00')
        error_msg = data[22:534].decode('utf-8').rstrip('\x00')

        return {
            'size': struct.unpack('<I', data[0:4])[0],
            'pkt_type': struct.unpack('<B', data[4:5])[0],
            'error_code': error_code,
            'error_msg': error_msg,
            'request_type': 'subscribe' if data[534] == 0 else 'unsubscribe',
            'mode': 'ltpc' if data[535] == 0 else 'full',
            'success_count': struct.unpack('<H', data[536:538])[0],
            'error_count': struct.unpack('<H', data[538:540])[0]
        }

    def notify_callbacks(self, tick):
        for callback in self.callbacks.values():
            callback(tick)

# Usage
client = ArrowDataserverClient()
client.connect()

def price_handler(tick):
    print(f"Token: {tick['token']}, LTP: ₹{tick['ltp']}, Volume: {tick['volume']}")

import time
time.sleep(1)  # Wait for connection

client.subscribe('full', ['NSE.SBIN-EQ', 'NSE.RELIANCE-EQ'], 200, price_handler)

# Keep running
while True:
    time.sleep(1)
```

## Error Handling and Reconnection

### Connection Management

```javascript
class ReconnectingClient {
    constructor() {
        this.reconnectInterval = 5000;
        this.maxReconnectAttempts = 10;
        this.reconnectAttempts = 0;
        this.subscriptions = [];
    }

    connect() {
        this.ws = new WebSocket('wss://socket.arrow.trade?appID=APP_ID&token=TOKEN&zstd=1');
        this.ws.binaryType = 'arraybuffer';

        this.ws.onopen = () => {
            this.reconnectAttempts = 0;
            this.resubscribeAll();
        };

        this.ws.onclose = () => {
            if (this.reconnectAttempts < this.maxReconnectAttempts) {
                const delay = this.reconnectInterval * Math.pow(2, this.reconnectAttempts);
                setTimeout(() => {
                    this.reconnectAttempts++;
                    this.connect();
                }, delay);
            }
        };
    }

    resubscribeAll() {
        this.subscriptions.forEach(sub => {
            this.ws.send(JSON.stringify(sub));
        });
    }
}
```

### Common Error Scenarios

Error | Cause | Solution
---|---|---
`E_INVALID_JSON` | Malformed JSON request | Validate JSON before sending
`E_MISSING_FIELD` | Required field missing | Include all required fields
`E_INVALID_PARAM` | Invalid parameter value | Check parameter constraints
`E_ALL_INVALID` | All symbols invalid | Verify symbol name formats
`E_PARTIAL` | Some symbols failed | Check error_msg for details
Connection timeout | Network issues | Implement reconnection with backoff

## Rate Limits and Constraints

Constraint | Limit
---|---
Requests per second | 100 per connection
Maximum symbols per connection | 1,024
Maximum symbols per subscription request | 512
Maximum request size | 16 KB
Latency range | 50ms - 60,000ms

## Data Type Notes

Type | Description
---|---
Prices | All prices are in paise (1 rupee = 100 paise)
Timestamps | Nanoseconds since Unix epoch
Byte order | Little-endian for all multi-byte integers

## Best Practices

### Subscription Management

  * **Batch subscriptions** : Subscribe to multiple symbols in a single request to reduce overhead
  * **Mode selection** : Use `ltpc` for minimal data when you only need last traded prices; use `full` for market depth and complete price information
  * **Symbol validation** : Verify symbol names/IDs before sending requests
  * **Latency tuning** : Adjust latency based on your application needs (lower for real-time, higher for reduced bandwidth)

### Error Handling

  * **Connection errors** : Reconnect with exponential backoff
  * **Invalid symbols** : Check the `error_msg` field for specific invalid symbols
  * **Subscription limits** : Split large requests into smaller batches
  * **Parse errors** : Validate JSON format before sending

### Performance Optimization

  * **Memory management** : Parse and process data efficiently to prevent memory leaks
  * **Binary parsing** : Use optimized binary parsers for high-frequency data
  * **Buffer handling** : Implement proper buffer management for binary data streams
  * **Connection pooling** : Reuse connections where possible

## Market Data Applications

### Real-Time Price Monitoring

```javascript
function formatTick(tick) {
    const change = ((tick.ltp - tick.close) / tick.close * 100).toFixed(2);
    const direction = tick.ltp >= tick.close ? '▲' : '▼';
    return `${tick.token}: ₹${tick.ltp} ${direction} ${change}%`;
}
```

### Order Book Analysis

```javascript
function analyzeOrderBook(tick) {
    const bestBid = tick.bidPrices[0];
    const bestAsk = tick.askPrices[0];
    const spread = bestAsk - bestBid;
    const spreadPercent = (spread / bestBid * 100).toFixed(4);

    const totalBidDepth = tick.bidSizes.reduce((a, b) => a + b, 0);
    const totalAskDepth = tick.askSizes.reduce((a, b) => a + b, 0);

    return {
        spread: spread,
        spreadPercent: spreadPercent,
        bidDepth: totalBidDepth,
        askDepth: totalAskDepth,
        imbalance: (totalBidDepth - totalAskDepth) / (totalBidDepth + totalAskDepth)
    };
}
```

### Volume Analysis

```javascript
function analyzeVolume(tick) {
    return {
        totalVolume: tick.volume,
        buyVolume: tick.btv,
        sellVolume: tick.atv,
        buyRatio: (tick.btv / (tick.btv + tick.atv) * 100).toFixed(2),
        vwap: tick.vwap
    };
}
```
