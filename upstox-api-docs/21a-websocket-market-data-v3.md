# Market Data Feed V3 (WebSocket)

## Overview

Real-time market updates through WebSocket connections using Protobuf encoding. Provides improved stability, performance, and reliability.

## Connection Details

- **Protocol:** `wss:` (secure WebSocket)
- **Message Format:** Binary (Protobuf encoded, not text)
- **Authentication:** Bearer token
- **Header:** `Accept: */*`

## Connection & Subscription Limits

### Standard Users

| Limit Type | Category | Individual | Combined |
|-----------|----------|-----------|----------|
| Connection | N/A | 2 per user | -- |
| LTPC | Subscription | 5000 keys | 2000 keys |
| Option Greeks | Subscription | 3000 keys | 2000 keys |
| Full | Subscription | 2000 keys | 1500 keys |

### Upstox Plus Users

| Limit Type | Category | Individual | Combined |
|-----------|----------|-----------|----------|
| Connection | N/A | 5 per user | -- |
| Full D30 | Subscription | 50 keys | 1500 keys |

## Request Structure

```json
{
  "guid": "13syxu852ztodyqncwt0",
  "method": "sub",
  "data": {
    "mode": "full",
    "instrumentKeys": ["NSE_INDEX|Nifty Bank"]
  }
}
```

### Method Values

- `sub` - Subscribe (default mode: ltpc)
- `change_mode` - Modify subscription mode
- `unsub` - Unsubscribe

### Mode Values

- `ltpc` - Latest trading price and close price only
- `option_greeks` - Option Greeks data
- `full` - LTPC + 5 market levels + metadata + Greeks
- `full_d30` - LTPC + 30 market levels + metadata + Greeks (Plus only)

## Response Flow

1. **First Tick:** Market status (segment conditions)
2. **Second Tick:** Market data snapshot
3. **Subsequent Ticks:** Live real-time updates

### Market Status Message

```json
{
  "type": "market_info",
  "currentTs": "1732775008661",
  "marketInfo": {
    "segmentStatus": {
      "NSE_COM": "NORMAL_OPEN",
      "NSE_FO": "NORMAL_OPEN"
    }
  }
}
```

### LTPC Feed Sample

```json
{
  "type": "live_feed",
  "feeds": {
    "NSE_FO|45450": {
      "ltpc": {
        "ltp": 219.3,
        "ltt": "1740729552723",
        "ltq": "75",
        "cp": 494.05
      }
    }
  },
  "currentTs": "1740729566039"
}
```

### Full Feed Fields

- `ltpc` - Price data
- `marketLevel` - Up to 5 bid/ask levels
- `optionGreeks` - Delta, theta, gamma, vega, rho
- `marketOHLC` - OHLC candles
- `atp` - Average traded price
- `vtt` - Volume traded today
- `oi` - Open interest
- `iv` - Implied volatility
- `tbq/tsq` - Total buy/sell quantities

## Heartbeat

Server sends periodic `ping` frames automatically. Standard WebSocket libraries respond with `pong`.

## Protobuf Decoding

Messages require decoding using the `MarketDataFeed.proto` file provided by Upstox.
