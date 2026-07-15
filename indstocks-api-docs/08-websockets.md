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

```
NSE:2885    NFO:51011    NIDX:26000
```

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

---

## Order Updates

Connect to `wss://ws-order-updates.indstocks.com/api/v1/ws/trades` and subscribe to your
order stream.

### Subscribe

```json
{
  "action": "subscribe",
  "mode": "order_updates"
}
```

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
