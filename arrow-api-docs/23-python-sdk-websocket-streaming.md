> Source: https://docs.arrow.trade/python-sdk/websocket-streaming/

# WebSocket Streaming

The PyArrow SDK provides real-time WebSocket streaming: the **Order Stream** (JSON updates), the **Data Stream** (token-based ticks), and the **HFT Data Stream** (symbol- or token-based binary protocol). All sockets share automatic reconnection, heartbeat/read timeouts, and thread-based event delivery.

## Overview

`ArrowStreams` exposes three WebSocket connections:

Stream | Endpoint | Purpose | Events
---|---|---|---
**Order Stream** | `wss://order-updates.arrow.trade` | Order and position updates | `on_order_update` (JSON)
**Data Stream** | `wss://ds.arrow.trade` | Standard market data (token-based, binary ticks) | `on_ticks` (`MarketTick`)
**HFT Data Stream** | `wss://socket.arrow.trade` | Low-latency market data (symbol or token IDs, zstd-compressed binary protocol) | `on_ltp_tick`, `on_full_tick`, `on_response`

## Quick Start

```python
from pyarrow_client import ArrowStreams, DataMode

# Initialize streams
streams = ArrowStreams(
    appID="your_app_id",
    token="your_access_token",
    debug=True  # Enable debug logging
)

# Define event handlers
def on_order_update(order):
    print(f"Order Update: {order['id']} - {order['orderStatus']}")

def on_tick(tick):
    print(f"Token: {tick.token} | LTP: ₹{tick.ltp} | Change: {tick.net_change}%")

def on_connect():
    print("✓ Connected to market data stream")

def on_disconnect():
    print("✗ Disconnected from stream")

# Attach handlers
streams.order_stream.on_order_update = on_order_update
streams.data_stream.on_ticks = on_tick
streams.data_stream.on_connect = on_connect
streams.data_stream.on_disconnect = on_disconnect

# connect_all() connects order, data, and HFT streams
streams.connect_all()

# Subscribe to market data (Data Stream — integer tokens)
tokens = [3045, 1594]  # RELIANCE, INFY
streams.subscribe_market_data(DataMode.QUOTE, tokens)

# Keep connection alive
import time
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    streams.disconnect_all()
```

## Order Stream

The **Order Stream** (`OrderStream`) uses `wss://order-updates.arrow.trade?appID=<appID>&token=<token>`. Incoming messages are **JSON text**. The SDK parses each message and calls **`on_order_update`** when the object contains an **`id`** field (order identifier).

```python
streams.order_stream.on_order_update = lambda o: print(o["id"], o.get("orderStatus"))

streams.connect_order_stream()
```

Updates typically include fields such as `orderStatus`, `symbol`, `quantity`, `price`, `transactionType`, `averagePrice`, and `rejectReason`. Use the REST **orders** documentation for the full payload shape.

## Data Stream

The **Data Stream** (`DataStream`) uses integer **instrument tokens** and a **big-endian** binary tick format (aligned with the JS client). Subscribe with `DataMode` and `subscribe_market_data` / `unsubscribe_market_data`.

### LTP Mode (13 bytes)

Last traded price only.

```python
streams.subscribe_market_data(DataMode.LTP, [3045, 1594])

def on_tick(tick):
    print(f"Token: {tick.token} | LTP: {tick.ltp} | mode: {tick.mode}")  # mode == 'ltp'
```

Field | Description
---|---
`token` | Instrument token
`ltp` | Last traded price
`mode` | `"ltp"`

### LTPC Mode (17 bytes)

Minimal data for price tracking.

```python
from pyarrow_client import DataMode

# Subscribe to LTPC mode
streams.subscribe_market_data(DataMode.LTPC, [3045, 1594])

def on_tick(tick):
    print(f"Token: {tick.token}")
    print(f"LTP: ₹{tick.ltp}")
    print(f"Close: ₹{tick.close}")
    print(f"Net Change: {tick.net_change}%")
    print(f"Change Flag: {tick.change_flag}")  # 43(+), 45(-), 32(no change)
```

Field | Description
---|---
`token` | Instrument token
`ltp` | Last traded price
`close` | Previous close
`net_change` | % change
`change_flag` | Direction indicator

### Quote Mode (93 bytes)

Detailed quotes with OHLCV and OI data.

```python
# Subscribe to Quote mode
streams.subscribe_market_data(DataMode.QUOTE, [3045])

def on_tick(tick):
    print(f"Token: {tick.token}")
    print(f"LTP: ₹{tick.ltp} | Volume: {tick.volume}")
    print(f"Open: {tick.open} | High: {tick.high} | Low: {tick.low} | Close: {tick.close}")
    print(f"OI: {tick.oi} | OI High: {tick.oi_day_high} | OI Low: {tick.oi_day_low}")
    print(f"Buy Qty: {tick.total_buy_quantity} | Sell Qty: {tick.total_sell_quantity}")
    print(f"LTQ: {tick.ltq} | Avg Price: {tick.avg_price}")
    print(f"LTT: {tick.ltt} | Time: {tick.time}")
```

Field | Description
---|---
All LTPC fields | +
`open`, `high`, `low` | OHLC prices
`volume` | Traded volume
`oi`, `oi_day_high`, `oi_day_low` | Open Interest
`ltq` | Last traded quantity
`avg_price` | Average traded price
`total_buy_quantity` | Total buy quantity
`total_sell_quantity` | Total sell quantity
`ltt` | Last trade time
`time` | Timestamp

### Full Mode (249 bytes)

Complete market depth with 5 levels of bids/asks.

```python
# Subscribe to Full mode
streams.subscribe_market_data(DataMode.FULL, [3045])

def on_tick(tick):
    print(f"Token: {tick.token} | LTP: ₹{tick.ltp}")
    print(f"Upper Limit: ₹{tick.upper_limit} | Lower Limit: ₹{tick.lower_limit}")

    # Market Depth - Bids
    print("\n--- BID DEPTH ---")
    for i, bid in enumerate(tick.bids):
        print(f"Level {i+1}: {bid['quantity']:>8} @ ₹{bid['price']:>10.2f} ({bid['orders']} orders)")

    # Market Depth - Asks
    print("\n--- ASK DEPTH ---")
    for i, ask in enumerate(tick.asks):
        print(f"Level {i+1}: {ask['quantity']:>8} @ ₹{ask['price']:>10.2f} ({ask['orders']} orders)")
```

Field | Description
---|---
All Quote fields | +
`upper_limit` | Upper circuit limit
`lower_limit` | Lower circuit limit
`bids` | List of 5 bid levels
`asks` | List of 5 ask levels

### Subscribe to market data

```python
# Subscribe tokens to a specific mode
tokens = [3045, 1594, 5533]  # RELIANCE, INFY, SBIN
streams.subscribe_market_data(DataMode.QUOTE, tokens)

# Subscribe with different modes
streams.subscribe_market_data(DataMode.LTPC, [3045])   # Light data
streams.subscribe_market_data(DataMode.FULL, [1594])   # Full depth
```

### Unsubscribe from market data

```python
# Unsubscribe specific tokens from a mode
streams.unsubscribe_market_data(DataMode.QUOTE, [3045])

# Unsubscribe all
streams.unsubscribe_market_data(DataMode.LTPC, [3045, 1594, 5533])
```

### `MarketTick` object

The **Data Stream** delivers `MarketTick` instances (dataclass). Numeric fields are populated depending on mode; unused fields may be `0` or empty lists.

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class MarketTick:
    token: int
    ltp: float = 0.0
    mode: str = ""                    # "ltp" | "ltpc" | "quote" | "full"
    open: float = 0.0
    high: float = 0.0
    low: float = 0.0
    close: float = 0.0
    volume: int = 0
    net_change: float = 0.0
    change_flag: int = 32             # 43 '+', 45 '-', 32 flat
    ltq: int = 0
    avg_price: float = 0.0
    total_buy_quantity: int = 0
    total_sell_quantity: int = 0
    ltt: int = 0
    time: int = 0
    oi: int = 0
    oi_day_high: int = 0
    oi_day_low: int = 0
    upper_limit: float = 0.0
    lower_limit: float = 0.0
    bids: List[dict] = field(default_factory=list)   # keys: price, quantity, orders
    asks: List[dict] = field(default_factory=list)
```

HFT ticks are **not** `MarketTick`; use the dict fields described in [HFT tick and response shapes](#hft-tick-and-response-shapes).

## HFT Data Stream

The **HFT Data Stream** (`HFTDataStream`) connects to `wss://socket.arrow.trade?appID=<appID>&token=<token>&zstd=1`. Inbound market-data frames are **zstd-compressed** on the wire; the SDK decompresses them automatically before parsing. Outbound subscribe/unsubscribe commands remain **JSON** (`code`: `sub` / `unsub`).

Mandatory from 8 July 2026

**Zstd compression becomes mandatory on 8 July 2026.** After that date, the HFT feed sends only compressed inbound frames. Clients that do not decompress payloads will not receive usable ticks.

Use a current **pyarrow-client** release (which handles this in `HFTDataStream`) or follow the [HFT REST/WebSocket protocol](../../rest-api/hft-stream/#inbound-compression-zstd) if you maintain a custom client.

### Protocol summary

Topic | Detail
---|---
Inbound compression | Zstd (`zstd=1` on the connection URL; SDK handles decompression)
Multi-byte integers | Little-endian
Prices | Paise (1 rupee = 100 paise)
Packet framing | Response frames: uint32 size at offset 0, type at byte 4. LTP/full frames: int16 size at offset 0, type at byte 2. Multiple frames may appear in one decompressed message.

**Packet types**

Type | Value | Size (bytes) | Handler callback
---|---|---|---
LTP | `1` (`PKT_TYPE_LTP`) | 40 | `on_ltp_tick`
Full depth | `2` (`PKT_TYPE_FULL`) | 196 | `on_full_tick`
Server response | `99` (`PKT_TYPE_RESPONSE`) | 540 | `on_response`

**Exchange segments** (`HFTDataStream` constants)

Constant | Value | Segment
---|---|---
`EXCH_NSE_CM` | `0` | NSE cash
`EXCH_NSE_FO` | `1` | NSE F&O
`EXCH_BSE_CM` | `2` | BSE cash
`EXCH_BSE_FO` | `3` | BSE F&O

**Symbol string formats** (when subscribing with names instead of token IDs)

Segment | Example format
---|---
NSE CM | `NSE.<UNDERLYING>-<SERIES>` — e.g. `NSE.SBIN-EQ`
NSE FO options | Underlying + expiry + **C** or **P** \+ strike — e.g. `NYKAA30DEC25C232.5`
NSE FO futures | Underlying + expiry + **F** — e.g. `BANKNIFTY30DEC25F`
BSE CM | `BSE.<UNDERLYING>` — e.g. `BSE.SBIN`
BSE FO options | Asset type + expiry + **C** or **P** \+ strike — e.g. `SENSEX01JAN26C74900`
BSE FO futures | `<ASSET_TYPE><DD><MON><YY>F` — e.g. `SENSEX01JAN26F`

**Limits**

  * Up to **100 requests per second** per connection
  * Up to **512 symbols** per subscription request
  * Up to **1024 subscribed symbols** per connection
  * Max request size **16 KB**

**Product note:** LTP-style streaming is available for **NSE FO** and **NSE CM** ; full depth for other segments as supported by the service.

### Connect and subscribe

```python
from pyarrow_client import ArrowStreams, HFTDataStream

streams = ArrowStreams(appID="your_app_id", token="your_token", debug=True)

streams.hft_data_stream.on_ltp_tick = lambda t: print("LTP:", t)
streams.hft_data_stream.on_full_tick = lambda t: print("Full:", t)
streams.hft_data_stream.on_response = lambda r: print("Response:", r)

streams.connect_hft_data_stream()

# Mode: 'ltpc' or 'l' (LTP), 'full' or 'f' (depth)
# latency: milliseconds between ticks (50–60000, default 1000)
streams.subscribe_hft_data(
    "ltpc",
    ["NSE.SBIN-EQ", "BSE.RELIANCE"],
    latency=100,
)

# Integer token IDs (default segment NSE_CM / 0 in the wire message)
streams.subscribe_hft_data("full", [5042, 4449], latency=200)
```

**Explicit exchange segments** (token IDs per segment):

```python
streams.hft_data_stream.subscribe_by_segment(
    "full",
    {
        HFTDataStream.EXCH_NSE_FO: [5042, 4449, 91],
        HFTDataStream.EXCH_BSE_CM: [100, 200],
    },
    latency=100,
)
```

### Unsubscribe

```python
streams.unsubscribe_hft_data("ltpc", ["NSE.SBIN-EQ"])

streams.hft_data_stream.unsubscribe_by_segment(
    "full",
    {HFTDataStream.EXCH_NSE_FO: [5042]},
)
```

Mixed types (strings and ints in one list) are **not** supported for a single subscribe/unsubscribe call.

Futures volume vs other data feeds

For **futures (FO)** symbols, HFT tick `volume` is often **lower** than on the standard Data Stream or other bcast-based sources. The HFT feed uses **TBT** data (volume for that instrument token only); bcast feeds can include **spread order book** volume in the aggregate. See [Futures volume vs other data feeds](../../rest-api/hft-stream/#market-data-packets) in the HFT protocol docs.

### HFT tick and response shapes

Callbacks receive **plain dicts** (parsed binary).

**LTP packet (`on_ltp_tick`)** — fields include: `size`, `pkt_type`, `exch_seg`, `token`, `ltp`, `vwap`, `volume`, `ltt`, `atv`, `btv` (see SDK `_parse_ltp_packet` for offsets; prices in paise).

**Full packet (`on_full_tick`)** — includes OHLC, `ltq`, `vwap`, `ltt`, day range `dpr_l` / `dpr_h`, `tbq`, `tsq`, `volume`, five levels of `bid_px`, `ask_px`, `bid_size`, `ask_size`, `bid_ord`, `ask_ord`, `oi`, server `ts`, `atv`, `btv`.

**Response packet (`on_response`)** — subscribe/unsubscribe acknowledgement: `error_code`, `error_msg`, `request_type` / `request_type_str`, `mode` / `mode_str`, `success_count`, `error_count`. Typical `error_code` values include: `SUCCESS`, `E_PARTIAL`, `E_ALL_INVALID`, `E_INVALID_JSON`, `E_MISSING_FIELD`, `E_INVALID_PARAM`, `E_PARSE_ERROR`.

### Resubscription

Like `DataStream`, `HFTDataStream` **resubscribes** from its local subscription map after `on_open` (modes `ltpc` and `full`).

## Connection Management

### Connect Streams

```python
# Connect all three streams (order, data, HFT)
streams.connect_all()

# Or connect individually
streams.connect_order_stream()
streams.connect_data_stream()
streams.connect_hft_data_stream()
```

### Disconnect Streams

```python
# Disconnect from all streams
streams.disconnect_all()

# Check connection status
status = streams.get_status()
print(f"Order Stream: {status['order_stream']}")
print(f"Data Stream: {status['data_stream']}")
print(f"HFT Data Stream: {status['hft_data_stream']}")
```

### Connection Status

```python
status = streams.get_status()

# Returns (values are SocketStatus string values, e.g. 'connected', 'connecting', 'disconnected'):
# {
#     'order_stream': 'connected',
#     'data_stream': 'connected',
#     'hft_data_stream': 'connected',
# }
```

### `ConnectionConfig` (shared)

`ArrowStreams(appID=..., token=..., debug=...)` builds a `ConnectionConfig` used by all streams. Notable fields (defaults in the SDK): `enable_reconnect`, `max_reconnect_attempts` (300), `max_reconnect_delay` (5 seconds), `immediate_reconnect_attempts` (3), `read_timeout` (5 seconds), `ping_interval` (3 seconds). The socket layer sends periodic `PONG` text on a timer and closes the connection if incoming data stalls beyond `read_timeout`. See the [REST order-updates guide](../../rest-api/order-data/) for the full heartbeat and reconnection schedule.

## Event Handlers

### Order Stream Events

```python
# Order update received
def on_order_update(order):
    """Handle order status updates."""
    print(f"Order: {order['id']}")
    print(f"Status: {order['orderStatus']}")
    print(f"Symbol: {order['symbol']}")
    print(f"Qty: {order['quantity']} @ {order['price']}")

# Attach handler
streams.order_stream.on_order_update = on_order_update
```

### Data Stream Events

```python
# Market tick received
def on_ticks(tick):
    """Handle incoming market data."""
    print(f"Tick: {tick.token} @ {tick.ltp}")

# Connection established
def on_connect():
    """Called when connection is established."""
    print("Connected!")
    # Re-subscribe after reconnection
    streams.subscribe_market_data(DataMode.QUOTE, [3045])

# Connection lost
def on_disconnect():
    """Called when connection is lost."""
    print("Disconnected!")

# Error occurred
def on_error(error):
    """Handle connection errors."""
    print(f"Error: {error}")

# Connection closed
def on_close(close_status_code, close_msg):
    """Called when connection is closed."""
    print(f"Closed: {close_status_code} - {close_msg}")

# Reconnection attempt
def on_reconnect(attempt, delay):
    """Called during reconnection attempts."""
    print(f"Reconnecting... Attempt {attempt}, waiting {delay}s")

# Max reconnection attempts reached
def on_no_reconnect():
    """Called when max reconnection attempts reached."""
    print("Max reconnection attempts reached!")

# Attach handlers
streams.data_stream.on_ticks = on_ticks
streams.data_stream.on_connect = on_connect
streams.data_stream.on_disconnect = on_disconnect
streams.data_stream.on_error = on_error
streams.data_stream.on_close = on_close
streams.data_stream.on_reconnect = on_reconnect
streams.data_stream.on_no_reconnect = on_no_reconnect
```

### HFT Data Stream Events

```python
def on_ltp_tick(tick):
    """Binary LTP packet decoded to dict (40-byte payload)."""
    print(tick["token"], tick["ltp"])

def on_full_tick(tick):
    """Binary full-depth packet (196 bytes)."""
    print(tick["token"], tick["bid_px"], tick["ask_px"])

def on_response(resp):
    """Server response to sub/unsub (540 bytes)."""
    print(resp["error_code"], resp["success_count"], resp["error_count"])

streams.hft_data_stream.on_ltp_tick = on_ltp_tick
streams.hft_data_stream.on_full_tick = on_full_tick
streams.hft_data_stream.on_response = on_response

# BaseSocket handlers also apply: on_connect, on_disconnect, on_error, on_close,
# on_reconnect, on_no_reconnect
```

## Example: Order Monitor

```python
from pyarrow_client import ArrowClient, ArrowStreams

def order_monitor(app_id, token):
    """Monitor real-time order updates."""

    streams = ArrowStreams(appID=app_id, token=token, debug=False)

    def on_order_update(order):
        status = order.get('orderStatus', 'UNKNOWN')
        symbol = order.get('symbol', 'N/A')
        order_id = order.get('id', 'N/A')
        txn = "BUY" if order.get('transactionType') == 'B' else "SELL"
        qty = order.get('quantity', 0)
        price = order.get('price', 0)

        # Status emoji
        emoji = {
            'PENDING': '⏳',
            'OPEN': '📖',
            'COMPLETE': '✅',
            'CANCELLED': '❌',
            'REJECTED': '🚫'
        }.get(status, '❓')

        print(f"\n{emoji} ORDER UPDATE")
        print(f"   ID: {order_id}")
        print(f"   {txn} {qty} x {symbol} @ ₹{price}")
        print(f"   Status: {status}")

        if status == 'REJECTED':
            print(f"   Reason: {order.get('rejectReason', 'N/A')}")

        if status == 'COMPLETE':
            print(f"   Avg Price: ₹{order.get('averagePrice', 'N/A')}")

    streams.order_stream.on_order_update = on_order_update

    print("Starting order monitor...")
    streams.connect_order_stream()

    try:
        while True:
            import time
            time.sleep(1)
    except KeyboardInterrupt:
        streams.disconnect_all()

# Usage
order_monitor("your_app_id", "your_token")
```

## Complete Example: Live Dashboard

```python
from pyarrow_client import ArrowClient, ArrowStreams, DataMode
import time
from datetime import datetime

class LiveDashboard:
    def __init__(self, app_id, token):
        self.streams = ArrowStreams(appID=app_id, token=token, debug=False)
        self.prices = {}
        self.setup_handlers()

    def setup_handlers(self):
        self.streams.order_stream.on_order_update = self.on_order
        self.streams.data_stream.on_ticks = self.on_tick
        self.streams.data_stream.on_connect = self.on_connect
        self.streams.data_stream.on_disconnect = self.on_disconnect
        self.streams.data_stream.on_error = self.on_error

    def on_tick(self, tick):
        """Process incoming market data."""
        self.prices[tick.token] = {
            'ltp': tick.ltp,
            'change': tick.net_change,
            'volume': tick.volume,
            'time': datetime.now()
        }
        self.display()

    def on_connect(self):
        print("\n✓ Connected to Arrow Market Data Stream")
        print("=" * 60)

    def on_disconnect(self):
        print("\n✗ Disconnected from stream")

    def on_error(self, error):
        print(f"\n⚠ Error: {error}")

    def on_order(self, order):
        print(f"\n📋 Order Update: {order['symbol']} - {order['orderStatus']}")

    def display(self):
        """Display live prices."""
        # Clear screen (optional)
        # print("\033[2J\033[H")  # Uncomment to clear terminal

        print(f"\n{'Token':<10} {'LTP':>12} {'Change':>10} {'Volume':>15}")
        print("-" * 50)

        for token, data in self.prices.items():
            change_str = f"{data['change']:+.2f}%"
            color = "📈" if data['change'] > 0 else "📉" if data['change'] < 0 else "➡️"
            print(f"{token:<10} ₹{data['ltp']:>10.2f} {change_str:>10} {data['volume']:>15,} {color}")

    def start(self, tokens):
        """Start the dashboard."""
        # connect_all() opens order, data, and HFT sockets; use connect_data_stream /
        # connect_order_stream only if you do not need HFT.
        self.streams.connect_all()
        time.sleep(1)  # Wait for connection

        self.streams.subscribe_market_data(DataMode.QUOTE, tokens)
        print(f"Subscribed to {len(tokens)} tokens")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\nShutting down...")
            self.streams.disconnect_all()

# Usage
if __name__ == "__main__":
    # Initialize client and authenticate
    client = ArrowClient(app_id="your_app_id")
    client.auto_login(
        user_id="your_user_id",
        password="your_password",
        app_secret="your_app_secret",
        totp_secret="your_totp_secret"
    )

    # Start dashboard
    dashboard = LiveDashboard(
        app_id="your_app_id",
        token=client.get_token()
    )

    # Subscribe to tokens
    watchlist = [3045, 1594, 5533, 2885, 3499]  # RELIANCE, INFY, SBIN, ICICIBANK, HDFCBANK
    dashboard.start(watchlist)
```

## Best Practices

Performance Tips

  * **Order Stream:** use `connect_order_stream()` alone when you only need fills and status updates
  * **Data Stream:** use `DataMode.LTP` or `DataMode.LTPC` for large watchlists when you only need price; use `DataMode.QUOTE` for OHLCV; use `DataMode.FULL` only when you need depth
  * **HFT Data Stream:** tune `latency` (ms) to balance rate vs CPU; respect 100 req/s, 512 symbols per subscription request, and 1024 symbols per connection
  * Unsubscribe from instruments you no longer need on each stream you use

Connection Handling

  * Always implement `on_connect` to re-subscribe after reconnection
  * Handle `on_error` and `on_disconnect` for graceful degradation
  * Use `on_reconnect` to track reconnection attempts
  * Set `debug=True` during development for detailed logging

Thread Safety

  * Event handlers are called from WebSocket threads
  * Use thread-safe data structures when sharing state
  * Avoid blocking operations in event handlers
