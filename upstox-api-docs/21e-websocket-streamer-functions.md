# Streamer Functions (SDK)

## MarketDataStreamerV3

### Subscription Modes

- `ltpc` - Last trade price and close
- `full` - Trade prices, D5 depth, candlestick charts
- `option_greeks` - Options Greek calculations
- `full_d30` - Full + 30 market level quotes

### Core Functions

| Function | Purpose |
|----------|---------|
| `constructor(apiClient, instrumentKeys, mode)` | Initialize streamer |
| `connect()` | Establish WebSocket connection |
| `subscribe(instrumentKeys, mode)` | Add instruments |
| `unsubscribe(instrumentKeys)` | Remove instruments |
| `changeMode(instrumentKeys, mode)` | Modify mode |
| `disconnect()` | Close connection |
| `auto_reconnect(enable, interval, retryCount)` | Configure reconnection |

### Events

- `open` - Connection established
- `close` - Connection terminated
- `message` - Data update received
- `error` - Error occurred
- `reconnecting` - Reconnection attempt
- `autoReconnectStopped` - Retries exhausted

## PortfolioDataStreamer

### Constructor Flags

- `order_update` - Real-time order changes (default: enabled)
- `position_update` - Position modifications
- `holding_update` - Holding changes
- `gtt_update` - GTT order triggers

### Core Functions

| Function | Purpose |
|----------|---------|
| `constructor(apiClient, [update flags])` | Initialize |
| `connect()` | Establish connection |
| `disconnect()` | Close connection |
| `auto_reconnect(enable, interval, retryCount)` | Configure reconnection |

SDK support: Python, Node.js, Java, PHP
