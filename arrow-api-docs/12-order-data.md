> Source: https://docs.arrow.trade/rest-api/order-data/

# WebSocket Order Updates API

Real-time order and trade updates with automatic reconnection for monitoring order status, executions, and trade confirmations.

## Overview

The WebSocket Order Updates API provides instant notifications for all order-related events including placements, modifications, cancellations, executions, and rejections. This persistent connection ensures you never miss critical trading events.

### Key Features

  * **Real-Time Order Updates** : Instant notifications for all order state changes
  * **Automatic Reconnection** : Built-in exponential backoff retry mechanism
  * **Heartbeat Monitoring** : Active connection health checks with configurable client-side intervals
  * **Session-Based Authentication** : Secure connection using session tokens
  * **Text-Based Protocol** : JSON messages for easy parsing and debugging

## Connection Setup

### WebSocket Endpoint

```
Production: wss://order-updates.arrow.trade
```

## Connection Events

The WebSocket client triggers various events to help you manage connection lifecycle:

Event | Description | When Triggered
---|---|---
`connect` | Connection established | WebSocket opens successfully
`disconnect` | Connection closed | WebSocket closes or errors
`reconnect` | Reconnection attempt | Automatic retry in progress
`noreconnect` | Reconnection exhausted | Max retry attempts reached
`error` | Connection error | WebSocket error occurs
`close` | Connection closed | WebSocket closes cleanly
`message` | Raw message received | Any message from server
`orderUpdate` | Order status changed | Order event received

## Connection Management

### Heartbeat Protocol

The connection maintains health through a client-side heartbeat mechanism. The Python SDK (`ConnectionConfig`) uses these defaults for all WebSocket streams (order, data, and HFT):

  * **Client Ping** : Sends `PONG` text every **3 seconds** (`ping_interval`)
  * **Read Timeout** : **5 seconds** without an incoming message closes the connection and triggers reconnection (`read_timeout`)
  * **Automatic Recovery** : Reconnects on timeout or connection loss when `enable_reconnect` is true

Custom clients should send periodic `PONG` messages and treat prolonged read silence as a stale connection.

### Reconnection Strategy

Built-in exponential backoff with configurable parameters. Python SDK defaults (`ConnectionConfig`):

Parameter | Default | Description
---|---|---
`enable_reconnect` | `true` | Enable automatic reconnection
`max_reconnect_attempts` | 300 | Maximum reconnection attempts
`immediate_reconnect_attempts` | 3 | First N attempts with no delay
`max_reconnect_delay` | 5 seconds | Maximum delay between attempts
`ping_interval` | 3 seconds | Interval for client `PONG` messages
`read_timeout` | 5 seconds | Idle read timeout before reconnect

**Backoff schedule (Python SDK):**

  * Attempts 1–3: immediate (0 second delay)
  * Attempt 4: 2 seconds (`2^1`, capped at 5)
  * Attempt 5: 4 seconds (`2^2`, capped at 5)
  * Attempt 6+: 5 seconds (capped at `max_reconnect_delay`)

## Order Update Messages

### Message Format

All order updates are JSON objects with the following structure:

```json
{
  "updateType": "ORDER_UPDATE",
  "userID": "AJ0001",
  "accountID": "AJ0001",
  "exchange": "NFO",
  "symbol": "NIFTY27JAN26C25300",
  "id": "26012301000023",
  "price": "0.05",
  "quantity": "65",
  "product": "M",
  "orderStatus": "PENDING",
  "reportType": "PendingNew",
  "transactionType": "B",
  "order": "LMT",
  "cumulativeFillQty": "0",
  "fillShares": "0",
  "averagePrice": "0",
  "exchangeOrderID": "0",
  "cancelQuantity": "0",
  "orderTriggerPrice": "0",
  "validity": "DAY",
  "pricePrecision": "2",
  "tickSize": "0.05",
  "lotSize": "65",
  "token": "58695",
  "orderTime": "2026-01-23T13:40:53",
  "orderSource": "WEB",
  "leavesQuantity": "65"
}
```

### Field Reference

Field | Type | Description | Example
---|---|---|---
`updateType` | string | Message type (always "ORDER_UPDATE") | `"ORDER_UPDATE"`
`userID` | string | User identifier | `"AJ0001"`
`accountID` | string | Trading account identifier | `"AJ0001"`
`exchange` | string | Exchange code | `"NFO"`, `"NSE"`, `"BSE"`
`symbol` | string | Trading symbol | `"NIFTY27JAN26C25300"`
`id` | string | Unique order identifier | `"26012301000023"`
`price` | string | Order price | `"0.05"`
`quantity` | string | Order quantity | `"65"`
`product` | string | Product type | `"M"` (Margin), `"C"` (Cash)
`orderStatus` | string | Current order status | See Order Status table
`reportType` | string | Type of update report | See Report Types table
`transactionType` | string | Buy or Sell | `"B"` (Buy), `"S"` (Sell)
`order` | string | Order type | `"LMT"`, `"MKT"`, `"SL"`, `"SL-M"`
`cumulativeFillQty` | string | Total filled quantity | `"0"`
`fillShares` | string | Shares filled in this update | `"0"`
`averagePrice` | string | Average execution price | `"0"`
`exchangeOrderID` | string | Exchange-assigned order ID | `"0"`
`cancelQuantity` | string | Cancelled quantity | `"0"`
`orderTriggerPrice` | string | Trigger price for stop orders | `"0"`
`validity` | string | Order validity | `"DAY"`, `"IOC"`
`pricePrecision` | string | Decimal precision for price | `"2"`
`tickSize` | string | Minimum price increment | `"0.05"`
`lotSize` | string | Trading lot size | `"65"`
`token` | string | Instrument token | `"58695"`
`orderTime` | string | Order timestamp (ISO format) | `"2026-01-23T13:40:53"`
`orderSource` | string | Order entry source | `"WEB"`, `"API"`, `"MOBILE"`
`leavesQuantity` | string | Remaining unfilled quantity | `"65"`

### Report Types

The `reportType` field indicates the type of order update:

Report Type | Description | Example Scenario
---|---|---
`PendingNew` | Order submitted, awaiting exchange | New order placed
`New` | Order accepted by exchange | Order becomes active
`Replaced` | Order modified successfully | Price or quantity changed
`Canceled` | Order cancelled | User cancellation
`Rejected` | Order rejected by exchange | Insufficient funds
`PartiallyFilled` | Partial execution | Some quantity filled
`Filled` | Complete execution | Order fully filled
`Expired` | Order expired | End of trading day
`Triggered` | Stop order triggered | Stop price reached

### Order Status Values

Status | Description | Terminal State
---|---|---
`PENDING` | Order submitted, awaiting exchange | No
`OPEN` | Active order in market | No
`COMPLETE` | Fully executed | Yes
`CANCELLED` | Cancelled by user/system | Yes
`REJECTED` | Rejected by exchange | Yes
`TRIGGER_PENDING` | Stop order waiting for trigger | No
`AFTER_MARKET_ORDER_REQ_RECEIVED` | AMO order queued | No

### Order Type Codes

Code | Full Name | Description
---|---|---
`LMT` | Limit | Order at specified price or better
`MKT` | Market | Market type; plain `MKT` is disabled by default on the place-order API—use `mpp: true` for market-style routing (Upper Limit / DPR by instrument)
`SL` | Stop Loss | Stop order with limit price
`SL-M` | Stop Loss Market | Stop order at market price

### Transaction Type Codes

Code | Full Name
---|---
`B` | Buy
`S` | Sell

### Product Type Codes

Code | Full Name | Description
---|---|---
`M` | Margin | Intraday trading
`C` | Cash | Delivery trading
`I` | Intraday | Intraday trading

## Troubleshooting

Issue | Cause | Solution
---|---|---
**Connection Fails** | Invalid appID/token | Verify credentials are current and valid
**Frequent Disconnects** | Network instability | Check network quality, increase timeout
**Missing Updates** | Connection dropped | Fetch order status via REST API on reconnect
**Duplicate Updates** | Network retry | Deduplicate using order ID + timestamp
**High CPU Usage** | Too many handlers | Optimize callback functions, batch updates
**Memory Leaks** | Handlers not cleaned | Remove handlers when components unmount
**Wrong Field Names** | Using old documentation | Use `id` instead of `orderId`, `symbol` instead of `tradingSymbol`
**String vs Number** | Field type mismatch | Parse string fields to numbers: `parseInt()`, `parseFloat()`
