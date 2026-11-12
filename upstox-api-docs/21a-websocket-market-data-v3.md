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

## Closing Auction Session (CAS) Fields

Added 4 September 2026. The `full` and `full_d30` feeds carry live closing auction values, and `ltpc` carries the indicative equilibrium price wherever it appears in the feed (populated only while the pre-open or closing auction session is active).

| Field | Type | Description |
|-------|------|-------------|
| iep | number | Indicative Equilibrium Price - price at which the maximum number of shares can be matched from the current order book |
| ieq | string | Indicative Equilibrium Quantity - total shares that will execute at the IEP |
| iiqTotal | string | Total Indicative Imbalance Quantity - net unmatched buy or sell quantity at the IEP (can be negative) |
| iiqM | string | Market Indicative Imbalance Quantity - the portion of the unmatched total originating from unpriced market orders |
| rp | string | Reference Price - base price used to calculate price bands and circuit filters for the session |
| casEligible | boolean | Whether the instrument may participate in a Call Auction Session |
| ltpc.iep | number | Indicative equilibrium price on `LTPC`, present only while a pre-open or closing auction session is active |

Market status updates now also report each segment's current closing auction and pre-open session status (`preOpenSessionStatus`). See Exchange Status for the CAS phase values.
