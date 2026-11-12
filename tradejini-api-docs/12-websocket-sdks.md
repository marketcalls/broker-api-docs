# WebSocket SDKs

Tradejini provides official **WebSocket SDKs** for **real-time market data streaming** and **order-related events** such as **order updates, trade updates, and position updates.**

## Why SDK ?

Unlike standard broker WebSocket APIs that provide :

- Direct WebSocket connection.
- JSON payload-based streaming.

Tradejini WebSocket SDK provides :

- Optimized binary streaming for better performance
- Reduced network payload size
- Lower latency market updates
- Structured real-time market data responses
- Order, trade, and position event updates

Since market data is transmitted in binary format, direct parsing is not supported. The Tradejini SDK includes an inbuild parsing mechanism to automatically decode and convert binary market data into structured responses.

## Available SDKs

Choose your preferred SDK to start integrating Tradejini WebSocket Streaming.

| Platform | Description | Dependencies | Action |
| --- | --- | --- | --- |
| Java library | WebSocket SDK for Java applications | Java 11+ | Download Now |
| Typescript library | WebSocket SDK for TypeScript applications | Node.js > 14 | Download Now |
| Python library | WebSocket SDK for Python applications | Python 3 | Download Now |
| Csharp library | WebSocket SDK for C# applications | .NET 4.6.2 | Download Now |
| Csharp Net6 library | WebSocket SDK for C# .NET 6 applications | .NET 6 | Download Now |

## SDK Installation

1. Download the SDK and follow the SDK-specific integration instructions provided in the respective README file.
2. Generate the `access_token` using the Authorization APIs. Refer to the **Authorization Flow** section for details.
3. Initialize the WebSocket connection using the SDK.
4. Subscribe to required instruments/token to receive **real-time market data, Greeks, and OHLC updates.**
5. Subscribe to events to receive **order, trade and position updates.**

## Integration

### 1. Authorization

The stream authenticates with a single **`authToken`**, which is your API key and access token joined with a colon:

```
authToken = "<APIkey>:<accessToken>"
```

| Component | How to obtain it |
| --- | --- |
| **APIkey** | Register at the [Apps](https://developer.tradejini.com/developer-portal). Once registered, create an application under your account to generate the API key. |
| **accessToken** | Returned in the response of the **access-token service** or the **individual token service**. Refer to the [Authorization](https://developer.tradejini.com/docs/authorization/updatedIndividualToken) *Authorization Flow* section for details. |

Pass the `authToken` to the SDK's `connect` method. There is no separate login call on the stream — the token authenticates the WebSocket connection itself. If you already have the API key and access token handy, form the `authToken` directly and subscribe for prices; otherwise generate them from Authorization section.

#### Expired or invalid tokens

If the `authToken` is expired or invalid, the server closes the connection and your connection callback receives close code **`4001`**:

```json
{"s": "closed", "code": 4001, "reason": "Unauthorized Access"}
```

When this occurs, generate a fresh access token via the Authorization APIs, rebuild the `authToken`, and connect again.

**Note:** Reconnecting with the same expired token will fail with the same `4001` close code. Always refresh the token first.

### 2. Building Stream Symbols

Every price subscription requires a **stream symbol** in the format:

```
<exchangeToken>_<exchangeName>
```

Both parts come from the **ScripMaster Data API** response:

| Component | Source |
| --- | --- |
| `exchangeToken` | The `excToken` field |
| `exchangeName` | The **last segment** of the `id` field, split on underscore (`_`) |

#### Example: ACC on NSE

The ScripMaster entry for ACC returns:

- `excToken` = `22`
- `id` = `EQT_ACC_EQ_NSE` (format: `INSTRUMENT_SYMBOL_SERIES_EXCHANGE`)

Splitting the `id` on `_` gives the exchange `NSE`, so the stream symbol is:

```
22_NSE
```

#### Tip

Parsing the `id` field
Each ScripMaster group declares its own `id` format (via `idFormat` in the ScripMaster Groups API). Split the `id` on `_` according to that format to extract the exchange, base symbol, expiry, option type, strike price, and other components.

### 3. Subscriptions & Unsubscriptions

How to subscribe to and unsubscribe from feeds, and — critically — how the SDK's **replacement semantics** and **unsubscribe scoping** behave. All subscription calls require an active connection (`{"s": "connected"}` received on `connect_cb`) and stream symbols built as described

##### Feed Types

| Method | Provides |
| --- | --- |
| `subscribeL1` | Sends a level 1 request and provides data apart from market depth |
| `subscribeL1SnapShot` | Sends a level 1 snapshot request and provides snapshot data (a last-tick with all fields, delivered only once) apart from market depth |
| `subscribeL2` | Sends a level 2 request and provides data for market depth |
| `subscribeL2SnapShot` | Sends a level 2 request and provides snapshot data for market depth |
| `subscribeGreeks` | Sends an option greeks request and provides option greeks data |
| `subscribeGreeksSnapShot` | Sends an option greeks request and provides option greeks snapshot data |
| `subscribeOHLC` | Sends an OHLC request with a symbol list and interval, and provides OHLC, volume, and time for the particular minute |
| `subscribeEvents` | Sends a request for an events subscription and provides data when a subscribed event is triggered (e.g. change in order status, change in positions) |

TypeScript and C# SDKs only; requires `loadSymbolStore` enabled at client construction. Obtain the underlying ID from the ScripMaster column tagged **`undId`**, and the expiry from the scrip `id` .

Supported OHLC intervals: **`1M`**, **`5M`**, **`30M`** (reported in the `type` field of OHLC messages).

**Note** : Snapshot vs. streaming
Snapshot variants deliver the **last tick with all fields exactly once** — use them to seed application state (e.g. populating a watchlist on startup) without holding a continuous subscription.

### 4. Subscription Replacement Semantics

A subscription request **replaces** the previous symbol list for that feed — it does not append to it. The server keeps only the most recent list.

**Example (from the SDK):**

```
subscribeL1([A, B, C, D])   →  A, B, C, D streaming
subscribeL1([E, F])         →  only E, F streaming
                               A, B, C, D are unsubscribed
```

**Note**: Always send the complete list
To add symbol `E` while keeping `A–D`, send `subscribeL1([A, B, C, D, E])`. Maintain the authoritative symbol list per feed in your application state and send it whole on every change — and replay it after every reconnect, since subscriptions are not documented to survive reconnection.

### 5. Unsubscription

Each `unsubscribe*` method cancels the corresponding subscription made earlier. Two scoping rules require special care:

**Note**: Calling `unsubscribeL1` unsubscribes **all** L1 subscriptions .

**Note:** `unsubscribeOHLC` is scoped per interval
`unsubscribeOHLC` removes only the OHLC subscriptions for the **particular interval** you specify. Subscriptions on other intervals (e.g. `5M` when you unsubscribe `1M`) are persisted.

#### Managing Multiple Subscriptions

- **Feed types are independent.** L1, L2, greeks, per-interval and OHLC events can all be active simultaneously — they multiplex over the single connection.
- **Within a feed type, the last request wins** (replacement semantics above).
- **Your application is the source of truth.** Keep the intended symbol list per feed in your own state; the SDK does not restore subscriptions after reconnect.

### 6. Market Data Reference

Fields delivered to **`stream_cb`** for L1, L2, greeks and OHLC subscriptions (binary payloads are decoded by the SDK automatically). Which fields appear depends on the subscription type and instrument.

##### Connection Status ( connect_cb )

```json
{"s": "connected"}
{"s": "error",  "reason": "<error message>"}
{"s": "closed", "code": <close code>, "reason": "<close message>"}
```

Close code **`4001`** = "Unauthorized Access" (expired/invalid `authToken`).

### 7. Market Data Fields

| Field | Description | Field | Description |
| --- | --- | --- | --- |
| `symbol` | Subscribed symbol (token + segment, e.g. `22_NSE`) | `ltq` | Last traded quantity |
| `exchSeg` | Exchange segment | `vol` | Volume traded today |
| `token` | Exchange token | `ttv` | Total traded value |
| `precision` | Decimal precision | `totBuyQty` | Total buy quantity |
| `marketStatus` | Market status for the exchange | `totSellQty` | Total sell quantity |
| `ltp` | Last traded price | `bidPrice` | Bid price |
| `open` | Day's open | `askPrice` | Ask price |
| `high` | Day's high | `qty` | Bid/ask quantity |
| `low` | Day's low | `no` | Bid/ask orders |
| `close` | Day's previous close | `OI` | Open interest |
| `dayClose` | Current day's close | `OIChngPer` | OI change % |
| `chng` | Change | `prevOI` | Previous OI |
| `chngPer` | Change % | `dayHighOI` | Intraday high OI |
| `atp` | Average traded price | `dayLowOI` | Intraday low OI |
| `vwap` | Volume-weighted average price | `spotPrice` | Underlying spot price (derivatives) |
| `yHigh` | 52-week high | `iv` | Implied volatility |
| `yLow` | 52-week low | `highiv` / `lowiv` | Day high / low IV |
| `ucl` | Upper circuit limit | `itm` | In-the-money probability |
| `lcl` | Lower circuit limit | `delta` `gamma` `theta` `rho` `vega` | Option greeks |
| `ltt` | Last traded time | `undId` / `expiry` |  |
| `time` | Candle time (OHLC) | `type` | Candle type: `1M`, `5M`, `30M` |
| `minuteOi` | Chart minute OI |  |  |

## Order Events

In addition to market data, the WebSocket SDK delivers real-time **account activity** — order updates, position updates, and trade updates — over the same connection. Subscribe with **`subscribeEvents`**; each triggered event is delivered to your **`stream_cb`** as a structured message. Cancel with **`unsubscribeEvents`**.

### Available Event Types

| Event (`evntType`) | Triggered when |
| --- | --- |
| **`orders`** | There is **any change in orders** — placement, modification, cancellation, rejection, status transitions |
| **`positions`** | There is **any change in positions** |
| **`trades`** | Trades are **executed successfully** |

Route incoming event messages by the **`evntType`** field to distinguish them from market data ticks and from each other.

### Event Field Reference

| Field | Description |
| --- | --- |
| `evntType` | Event type identifier: `orders`, `positions`, or `trades` |
| `type` | Order type |
| `trdSym` | Trading symbol |
| `exch` | Exchange segment |
| `qty` | Quantity |
| `product` | Product ID |
| `price` | Price of the order — **context-dependent**, see below |
| `side` | Order action |
| `status` | Order status |
| `orderId` | Exchange order ID |
| `orderTime` | Time the order was placed |
| `actStatus` | Status of an order **modification or cancellation** request — see below |
| `msg` | Order message |
| `reason` | Rejection reason |

##### price semantics

The meaning of the `price` field depends on the event type:

| Event type | `price` means |
| --- | --- |
| `orders` | **Order price** — the price at which the order was placed |
| `trades` | **Fill price** — the price at which the trade executed |

##### actStatus — modification/cancellation request status

`actStatus` reports the lifecycle of a **modify or cancel request** placed against an order, independently of the order's own `status`:

| Value | Meaning |
| --- | --- |
| `open` | The modification/cancellation request is open |
| `closed` | The request is closed |
| `completed` | The request completed |
| `rejected` | The request was rejected |

#### Handling Guidance

- **Subscribe once per session.** `subscribeEvents` requires no symbol list; call it after `{"s": "connected"}` and re-issue it after every reconnect, like all subscriptions.
- **Use `orderId` to correlate.** Track order lifecycles by exchange order ID across successive `orders` events; `trades` events for the same order carry fills against it.
- **Read `reason` on rejections.** When `status` indicates rejection, `reason` carries the rejection message; `msg` carries the general order message.
- **Keep the handler fast.** Events share `stream_cb` with all market data — an unhandled exception or blocking work in your event handling disrupts every feed.
- **Unsubscribing is isolated.** `unsubscribeEvents` affects only the events subscription; market data feeds are untouched

**Note**: Per-event payload examples and any additional position-specific fields are not documented in the SDK README. The field list above applies to event messages generally, with the `orders`/`trades` distinctions noted.
