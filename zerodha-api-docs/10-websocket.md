# WebSocket Streaming

The most efficient way to receive real-time quotes across all exchanges during market hours.

## Key Specs

- Subscribe to **up to 3000 instruments** per connection
- **Up to 3 concurrent WebSocket connections** per API key
- Delivers quotes, text messages, alerts, and order updates
- Binary protocol for market data; JSON for postbacks

## Connection

**Endpoint:** `wss://ws.kite.trade?api_key=xxx&access_token=xxxx`

## Request Structure

JSON with two parameters: `a` (action) and `v` (value).

### Actions

| Action | Value | Purpose |
|--------|-------|---------|
| `subscribe` | `[instrument_token...]` | Subscribe to instruments |
| `unsubscribe` | `[instrument_token...]` | Unsubscribe |
| `mode` | `[mode, [instrument_token...]]` | Set streaming mode |

### Examples

```javascript
// Subscribe
ws.send(JSON.stringify({ a: "subscribe", v: [408065, 884737] }));

// Set mode to full
ws.send(JSON.stringify({ a: "mode", v: ["full", [408065]] }));
```

## Modes

| Mode | Description | Packet Size |
|------|-------------|-------------|
| `ltp` | Last traded price only | 8 bytes |
| `quote` | Quote without depth | 44 bytes |
| `full` | Complete with market depth | 184 bytes |

## Binary Market Data Structure

All prices in paise. Currency: divide by 10,000,000. Others: divide by 100.

### Quote Packet

| Bytes | Type | Field |
|-------|------|-------|
| 0-4 | int32 | instrument_token |
| 4-8 | int32 | Last traded price *(ltp ends here)* |
| 8-12 | int32 | Last traded quantity |
| 12-16 | int32 | Average traded price |
| 16-20 | int32 | Volume traded |
| 20-24 | int32 | Total buy quantity |
| 24-28 | int32 | Total sell quantity |
| 28-32 | int32 | Open |
| 32-36 | int32 | High |
| 36-40 | int32 | Low |
| 40-44 | int32 | Close *(quote ends here)* |
| 44-48 | int32 | Last traded timestamp |
| 48-52 | int32 | Open Interest |
| 52-56 | int32 | OI Day High |
| 56-60 | int32 | OI Day Low |
| 60-64 | int32 | Exchange timestamp |
| 64-184 | bytes | Market depth (5 bid + 5 ask) |

### Index Packet

| Bytes | Type | Field |
|-------|------|-------|
| 0-4 | int32 | Token |
| 4-8 | int32 | LTP |
| 8-12 | int32 | High |
| 12-16 | int32 | Low |
| 16-20 | int32 | Open |
| 20-24 | int32 | Close |
| 24-28 | int32 | Price change *(quote ends here)* |
| 28-32 | int32 | Exchange timestamp |

### Market Depth Entry (12 bytes each)

- `quantity` (int32) + `price` (int32) + `orders` (int16) + 2-byte padding
- 5 bid entries [64-124] + 5 ask entries [124-184]

## Text Messages (JSON)

```json
{
  "type": "order|error|message",
  "data": {}
}
```

| Type | Description |
|------|-------------|
| `order` | Order postback |
| `error` | Error string |
| `message` | Broker messages/alerts |

## Notes

- **Heartbeat:** 1-byte ping every few seconds on idle connections
- Always check message type: binary = market data, text = postbacks/updates
