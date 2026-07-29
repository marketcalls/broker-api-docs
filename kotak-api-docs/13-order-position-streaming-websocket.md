# Order & Position Streaming API (WebSocket)

## 1. Introduction

The Order & Position Streaming API provides real-time streaming updates for:

- Order lifecycle events (new, validation, open, complete, rejected, etc.)
- Live position updates

The API uses a secure WebSocket (`wss://`) connection and pushes updates instantly whenever state changes occur in the trading system. This eliminates the need for polling and ensures low-latency state synchronization.

## 2. WebSocket Endpoint

```
wss://<baseurl>/realtime
```

Replace `<baseurl>` with the value returned from the `/tradeApiValidate` API.

Example:

```
wss://e21.kotaksecurities.com/realtime
```

## 3. Authentication & Connection Flow

### Step 1: Open WebSocket Connection

```js
const ws = new WebSocket(`wss://${baseurl}/realtime`);
```

### Step 2: Send Connection Payload (MANDATORY)

Immediately after `onopen`, send the authentication string:

```
{type:cn,Authorization:<token>,Sid:<sid>,src:WEB}
```

| Key field | type | description |
| --- | --- | --- |
| Sid | string | session sid generated on login (`/tradeApiValidate`) |
| Auth | string | session token generated on login (`/tradeApiValidate`) |

> **Important:** This is NOT JSON. Do NOT use `JSON.stringify`. It must be sent as a single raw string.

```js
ws.onopen = () => {
  const payload = `{type:cn,Authorization:${token},Sid:${sid},src:WEB}`;
  ws.send(payload);
};
```

## 4. Connection Acknowledgement

On successful authentication, the server responds:

```json
{
  "ak": "ok",
  "type": "cn",
  "task": "cn",
  "msg": "connected"
}
```

| Field | Description |
| --- | --- |
| ak | Acknowledgement status |
| type | Connection type |
| task | Task type |
| msg | Connection status |

## 5. Streaming Message Types

The WebSocket sends two primary message types: `order` and `position`.

## 6. Order Updates (`type: "order"`)

Each order update reflects a state change in the order lifecycle.

Example Order Message:

```json
{
  "type": "order",
  "data": {
    "nOrdNo": "260216000308219",
    "ordSt": "complete",
    "avgPrc": "35.88",
    "qty": 1,
    "fldQty": 1,
    "unFldSz": 0,
    "sym": "ITBEES",
    "trnsTp": "B",
    "prcTp": "MKT",
    "prod": "NRML",
    "exSeg": "nse_cm",
    "ordDtTm": "16-Feb-2026 12:29:31",
    "exOrdId": "1100000049435826"
  }
}
```

### Order Lifecycle (observed from stream)

Example sequence:

1. `put order req received`
2. `validation pending`
3. `open pending`
4. `open`
5. `complete`

Other possible states: `rejected`, `cancelled`, `modified`.

### Order Field Mapping

| Field | Type | Description |
| --- | --- | --- |
| nOrdNo | string | Internal order number |
| exOrdId | string | Exchange order ID |
| ordSt | string | Order status |
| avgPrc | string | Average traded price |
| qty | number | Total order quantity |
| fldQty | number | Filled quantity |
| unFldSz | number | Remaining quantity |
| trnsTp | string | Transaction type (B = Buy, S = Sell) |
| prcTp | string | Price type (MKT, LMT, etc.) |
| prod | string | Product type (NRML, MIS, etc.) |
| exSeg | string | Exchange segment |
| sym | string | Trading symbol |
| trdSym | string | Trading symbol with series |
| tok | string | Exchange token |
| ordDtTm | string | Order date/time |
| updRecvTm | number | Update receive timestamp (nanoseconds) |
| boeSec | number | Exchange broadcast time (epoch seconds) |
| exCfmTm | string | Exchange confirmation time |

## 7. Position Updates (`type: "position"`)

Position updates are pushed whenever there is a new trade execution, position quantity change, or buy/sell adjustment.

Example Position Message:

```json
{
  "type": "position",
  "data": {
    "actId": "XP6M4",
    "sym": "ITBEES",
    "exSeg": "nse_cm",
    "prod": "NRML",
    "flBuyQty": "1",
    "flSellQty": "0",
    "buyAmt": "35.88",
    "sellAmt": "0.00",
    "posFlg": "true",
    "hsUpTm": "2026/02/16 12:29:31"
  }
}
```

### Position Field Mapping

| Field | Type | Description |
| --- | --- | --- |
| actId | string | Account ID |
| sym | string | Symbol |
| exSeg | string | Exchange segment |
| prod | string | Product type |
| flBuyQty | string | Filled buy quantity |
| flSellQty | string | Filled sell quantity |
| buyAmt | string | Total buy amount |
| sellAmt | string | Total sell amount |
| posFlg | string | Position active flag |
| sqrFlg | string | Square-off allowed flag |
| lotSz | string | Lot size |
| multiplier | string | Contract multiplier |
| hsUpTm | string | Update timestamp |

## 8. Message Handling Example

```js
ws.onmessage = (event) => {
  const message = JSON.parse(event.data);

  if (message.type === "order") {
    console.log("Order Update:", message.data);
  }

  if (message.type === "position") {
    console.log("Position Update:", message.data);
  }
};
```

## 9. Important Notes

- WebSocket authentication must be sent as a raw string (non-JSON).
- Token and Sid must be valid.
- Token expiry will terminate the connection.
- Reconnection logic should be implemented at the client level.
- All numeric financial fields are returned as strings unless otherwise specified.
- Multiple order updates are sent for a single order as it moves through lifecycle stages.

## 10. Recommended Production Handling

- Implement auto-reconnect with exponential backoff.
- Detect duplicate order events using `nOrdNo` + `updRecvTm`.
- Maintain an in-memory order state machine.
- Persist only terminal states (`complete`, `rejected`, `cancelled`).
- Track latency: `updRecvTm - boeSec`.
