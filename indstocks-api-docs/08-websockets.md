# WebSocket Streaming

> Source: https://api-docs.indstocks.com/Websockets/

INDstocks provides two WebSocket streams — one for live prices and one for order updates.

## Endpoints

| Stream | URL |
|--------|-----|
| Price Feed | `wss://ws-prices.indstocks.com/api/v1/ws/prices` |
| Order Updates | `wss://ws-order-updates.indstocks.com/api/v1/ws/trades` |

## Authentication

Send the access token in the `Authorization` header during the WebSocket handshake:

```
Authorization: YOUR_ACCESS_TOKEN
```

## Limits

- Up to **3** WebSocket connections per user.
- Up to **3,000** instruments subscribed per connection.

## Instrument Format

Instruments use `SEGMENT:TOKEN` notation (note the **colon**, unlike the REST `_` separator):

| Type | Prefix | Example |
|------|--------|---------|
| NSE Equity | `NSE:` | `NSE:2885` |
| BSE Equity | `BSE:` | `BSE:500325` |
| NSE Derivatives | `NFO:` | `NFO:51011` |
| BSE Derivatives | `BFO:` | `BFO:12345` |
| NSE Index | `NIDX:` | `NIDX:26000` |
| BSE Index | `BIDX:` | `BIDX:1` |

---

## Price Feed

Connect to `wss://ws-prices.indstocks.com/api/v1/ws/prices`, then send a subscribe message.

### Subscribe — LTP Mode

```json
{
  "action": "subscribe",
  "mode": "ltp",
  "instruments": ["NSE:2885"]
}
```

### Subscribe — Quote Mode

```json
{
  "action": "subscribe",
  "mode": "quote",
  "instruments": ["NSE:2885"]
}
```

### LTP Update (streamed)

```json
{
  "mode": "ltp",
  "instrument": "2885",
  "timestamp": 1750138351089,
  "data": {
    "ltp": 1426
  }
}
```

| `mode` | Payload |
|--------|---------|
| `ltp` | Last traded price only |
| `quote` | Fuller snapshot (OHLC, volume, change, etc.) |

To stop receiving data, send an `"action": "unsubscribe"` message with the same `mode` and
`instruments`.

> The docs show a payload example only for `ltp` mode. The `quote` mode payload (OHLC, volume,
> change, etc.) is not documented — inspect a live frame to confirm its field names.

### Heartbeats

The server may send periodic heartbeat messages to keep the connection alive. Clients should
handle these, typically by ignoring them. No heartbeat interval or client-ping requirement is
specified in the official docs.

---

## Order Updates

Connect to `wss://ws-order-updates.indstocks.com/api/v1/ws/trades` and subscribe to your
order stream.

### Subscribe

```json
{
  "action": "subscribe",
  "mode": "order_update"
}
```

> ⚠️ The mode is **`order_update`** — singular. The order-updates feed accepts only
> `"action": "subscribe"`; there is no unsubscribe action documented for it.

### Order Update (streamed)

```json
{
  "type": "order",
  "order_id": "INDM20250512ABC123",
  "order_status": "PARTIALLY_EXECUTED",
  "filled_quantity": 5,
  "remaining_quantity": 5,
  "average_price": 2500.40,
  "timestamp": 1678886530456
}
```

| Field | Description |
|-------|-------------|
| `type` | Message type (e.g., `order`) |
| `order_id` | Affected order identifier |
| `order_status` | Current status (see [Order Management](09-order-management.md) status values) |
| `filled_quantity` | Quantity executed so far |
| `remaining_quantity` | Quantity still pending |
| `average_price` | Average fill price |
| `timestamp` | Event time, Unix epoch milliseconds |
