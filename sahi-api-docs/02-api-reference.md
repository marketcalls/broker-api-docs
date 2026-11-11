> Source: https://docs.sahi.com/llms-full.txt (Sahi APIs - Contracts v1), fetched 2026-11-11.

<!-- source: https://docs.sahi.com/api/v1/reference/ -->

# Sahi APIs — Contracts (v1)

## Introduction

The Sahi APIs let you build your own tools on your Sahi account: read the
market, place and manage your orders, and keep track of your positions, holdings
and funds.

> New here? Start with the [Quick start](/quick-start/) in the Get started
> section. It takes you from a new API key to your first order in five steps,
> with the Python SDK or cURL.

The REST endpoints are HTTPS with JSON bodies, and there are two WebSocket
streams for anything live. Any HTTP client will do, and order updates arrive as
JSON; if you would rather not write the HTTP yourself, the
[Python SDK](/sdk/python/) wraps every endpoint here. The tick stream is the
exception: its frames are protobuf, so you compile the schema published with
[the tick stream](/api/v1/reference/market-data/#wss-v1streammarketdata--tick-stream)
for your language before you can decode them, or let the SDK decode them for you.

The endpoints fall into two families:

- **[Data APIs](#data-apis)** read the market. Prices, depth, history and the
  live tick stream, all read-only.
- **[Trade APIs](#trade-apis)** act on your account: place and manage orders,
  and read back your positions, holdings, funds and profile.

Every request carries a Bearer access token, and one token covers every scope it
was granted — market data included. You mint it yourself from an API key you
create in your Sahi account; the key's scopes are fixed at creation and are
listed under
[Create an API key](/api/v1/reference/authentication/#create-an-api-key).

### Data APIs

Quotes, candles and ticks, plus the instrument file they are addressed through.
One scope covers all of it, `marketdata.read`, and none of it is IP-checked.

Instruments are named by `instrument_id` — the integer `id` from the scrip
master. Look it up once at start of day and reuse it for every quote, candle and
subscription.

- [Market data](https://docs.sahi.com/api/v1/reference/market-data/): Last traded price, full quotes with depth, historical candles, and the live tick stream.
- [Scrip master](https://docs.sahi.com/api/v1/reference/scrip-master/): The daily instrument file every request maps its symbols through.

The tick stream is one of the two WebSocket connections, and the simpler one:
every tick is a full snapshot for its instrument, so the newest value wins and
there is nothing to reconcile. What both sockets share — authentication, ping
and pong, close codes — is under
[WebSocket connections](#websocket-connections).

### Trade APIs

Anything that acts on your account, and everything that reports back on it.
Each area has its own scope — `orders.write`, `orders.read`, `positions.read`,
`holdings.read`, `funds.read`, `profile.read` — so a key can be granted exactly
what your own tool does and no more.

Orders name instruments by `exchange_segment` + `symbol` rather than by
`instrument_id`, and placing, modifying or cancelling one must come from a
[registered static IP](/api/v1/reference/authentication/#register-your-static-ip).
Reads are not IP-checked.

Order updates stream over the other WebSocket. That one *does* need care on
connect: a socket that drops replays nothing, so follow
[Stream + Snapshot](/api/v1/reference/orders/#stream--snapshot) to bootstrap
without losing events.

- [Orders](https://docs.sahi.com/api/v1/reference/orders/): Place, modify and cancel orders, read the order book and the trades behind each order, and follow live order updates.
- [Portfolio](https://docs.sahi.com/api/v1/reference/portfolio/): Your open positions and demat holdings.
- [Funds](https://docs.sahi.com/api/v1/reference/funds/): Your available balances per order kind, and the margin an order would need before you place it.
- [Account](https://docs.sahi.com/api/v1/reference/account/): Your identity and account status.

### How to work through this

1. **[Quick start](/quick-start/)**, if you are new. Five steps from a new API
   key to a first order, with the Python SDK or cURL.
2. **[Authentication](/api/v1/reference/authentication/)**. Create an API key,
   register the static IP you place orders from, and exchange the key for a
   token. Nothing below works without one.
3. **Conventions**, further down this page. The rules that hold for every
   endpoint — money in paise, quantities in units, timestamps in milliseconds,
   identifiers as strings. Reading them once saves debugging later.
4. **[Scrip master](/api/v1/reference/scrip-master/)**. Download the daily
   instrument file and map the symbols you care about. Orders address instruments
   by `exchange_segment` and `symbol`; market data addresses them by
   `instrument_id`, and both come from this file.
5. **The endpoints you need**, from the two groups above. Each page lists its
   endpoints with every field, and shows the request and response beside them.

### Getting help

The endpoint pages are generated from the same contract our own services are
built against, so if something here disagrees with what the API does, that is a
bug worth reporting. Write to
[developers@sahi.com](mailto:developers@sahi.com).

## Conventions

- Base path: `/v1`. Versioning is URL-prefixed.
- All bodies are JSON; field names are `snake_case`.
- Authentication: `Authorization: Bearer <access_token>` on every request. See
  [Authentication](/api/v1/reference/authentication/) for how to mint one.
- Requests that place, modify, or cancel an order must arrive from a
  [registered static IP](/api/v1/reference/authentication/#register-your-static-ip).
  One that does not is refused with `403 IP_NOT_ALLOWED`, whatever the token
  permits. Read-only endpoints and the WebSocket streams are not IP-checked.
- Timestamps are integer milliseconds since Unix epoch (UTC).
- Money values are integer **paise**, in requests as well as responses. Example: `2499.55` INR is sent and returned as `249955`. A decimal such as `2499.55` is refused with `422 VALIDATION_FAILED`.
- A successful request returns a `2xx` status, and not always `200`: [place order](/api/v1/reference/orders/#post-v1orders--place-order) returns `201 Created` and [cancel order](/api/v1/reference/orders/#delete-v1ordersorder_id--cancel-order) returns `204 No Content` with an empty body. Treat any `2xx` as success. Each endpoint shows its success status under its route.
- Quantity is integer units, not lots. Example: 1 NIFTY lot of 65 contracts is `qty: 65`.
- Instrument identifier:
  - **Order APIs** use `exchange_segment` + `symbol` pair.
  - **Market Data APIs** use `instrument_id` — the integer value of the `id` column from the scrip-master CSV. Look it up once at start of day and use it for every market-data and WebSocket call.
  - `instrument_id` is Sahi's own key, not the exchange token: RELIANCE is `12027`, while `2885` is its NSE token and returns `null`.
- All identifiers (`order_id`, `exchange_order_id`, `user_id`) are opaque JSON **strings**, even when the value looks numeric. Do not parse them as integers — Sahi-issued order IDs can exceed JavaScript's safe-integer range. `instrument_id` is the exception: it's a JSON **integer**.

### Exchange segment

| Value | Market | Available on |
|---|---|---|
| `NSE` | NSE Cash | Order APIs + Market Data |
| `NFO` | NSE Futures & Options | Order APIs + Market Data |
| `BSE` | BSE Cash | Order APIs + Market Data |
| `BFO` | BSE Futures & Options | Order APIs + Market Data |

### Enum values

| Field | Values |
|---|---|
| `txn_type` | `B` (buy), `S` (sell) |
| `order_type` | `LMT`, `MKT`, `SL-LMT`, `SL-MKT` |
| `product` | `C`, `I`, `M`, `F` — see [Product](#product) |
| `validity` | `DAY`, `IOC` |
| `variant` | `REGULAR` (default), `AMO` — see [After-market orders](/api/v1/reference/orders/#after-market-orders) |
| `status` | See [Order status](#order-status) |

### Product

`product` says how a position is held. Each value is valid only on some segments. Any other pair of `product` and `exchange_segment` is refused with `400 VALIDATION_FAILED`, and nothing is placed.

| Value | Meaning | Valid on |
|---|---|---|
| `C` | Delivery. Shares you buy go to your demat account. | `NSE`, `BSE` |
| `I` | Intraday. The position is for the same trading day only. | `NSE`, `BSE`, `NFO`, `BFO` |
| `M` | Carry-forward (normal). The F&O position stays open from day to day until you close it or the contract expires. | `NFO`, `BFO` |
| `F` | Margin trading facility (MTF). | `NSE` |

### Error envelope

Every non-2xx response uses this shape:

```json
{
  "code": "VALIDATION_FAILED",
  "message": "trigger_price is required for SL-LMT orders"
}
```

`code` is a stable enum. The values used across these pages: `INVALID_ORDER_STATE`, `ORDER_NOT_FOUND`, `VALIDATION_FAILED`, `FORBIDDEN`, `NOT_FOUND`. `UNAUTHORIZED` (`401`) and [`RATE_LIMITED`](#rate-limits) (`429`) can come back from any endpoint, `IP_NOT_ALLOWED` (`403`) from the order-write endpoints, and `NOT_FOUND` (`404`) from an unknown route — or from `GET /v1/funds`, `POST /v1/margins/order`, `POST /v1/margins/basket` and `GET /v1/profile` when the account behind the token is not yet set up for trading. `UNDER_MAINTENANCE` (`503`) comes back from `POST /v1/margins/order` and `POST /v1/margins/basket` during the daily 04:45–07:00 IST maintenance window.

### Rate limits

Each endpoint carries its own request budget for your user, over up to three windows. A call over budget is refused with `429` and the standard envelope —

```json
{
  "code": "RATE_LIMITED",
  "message": "rate limit exceeded"
}
```

— carrying a `Retry-After` header in whole seconds. Wait that long: it is what the window that tripped has left to run, so an immediate retry only earns another `429`.

| Endpoint | Per second | Per minute | Per day |
|---|---|---|---|
| `POST /v1/orders`, `PUT /v1/orders/{order_id}`, `DELETE /v1/orders/{order_id}` | 10 | 250 | 10,000 |
| `GET /v1/orders`, `GET /v1/orders/{order_id}`, `GET /v1/orders/{order_id}/trades` | 5 | 250 | 10,000 |
| `GET /v1/positions` | 5 | 250 | 10,000 |
| `GET /v1/holdings` | 5 | 250 | 10,000 |
| `GET /v1/funds` | 1 | — | — |
| `POST /v1/margins/order`, `POST /v1/margins/basket` | 5 | 250 | 10,000 |
| `GET /v1/profile` | 1 | — | — |
| `GET /v1/marketdata/ltp` | 1 | — | — |
| `GET /v1/marketdata/quotes` | 1 | — | — |
| `GET /v1/marketdata/candles` | 2 | 250 | 100,000 |
| `GET /v1/marketdata/optionchain` | 2 | 120 | 20,000 |
| `GET /v1/marketdata/optionchain/expiries` | 5 | 250 | 10,000 |
| `WSS /v1/stream/orders` | 5 | 250 | 10,000 |
| `WSS /v1/stream/marketdata` | 5 | 250 | 10,000 |

- **Every row is its own counter.** Rows that share numbers do not share a budget: polling the order book never eats into your market-data allowance. The exceptions are the rows that list several endpoints, and they are charged together: place, modify and cancel are one surface onto the exchange, the three order reads are one view of the same book, and the two margin checks are one calculator.
- **`—` means that window is not enforced** for the endpoint; only the ceilings shown apply.
- **Windows are charged finest first, and a refusal stops there.** A call the per-second ceiling rejects never spends minute or day quota, so a burst cannot drain a daily budget in rejections alone.
- **The day window rolls from your first request in it**, not from midnight or the start of the trading day.
- **The WebSocket rows charge the upgrade request, not the frames.** Once a socket is open, what flows over it is uncounted; a reconnect loop is counted.

Batch before you back off. `ltp` and `quotes` take up to 100 `instrument_id`s per request, so one call a second is a whole watchlist a second — the ceiling bites only if you loop an instrument at a time. Anything you follow continuously belongs on [the tick stream](/api/v1/reference/market-data/#wss-v1streammarketdata--tick-stream) rather than in a polling loop, which is also why the streams are budgeted for reconnects rather than for traffic.

**Concurrent connections.** Each stream allows **5** open at once — per account for [order updates](/api/v1/reference/orders/#wss-v1streamorders--order-updates), per token for [the tick stream](/api/v1/reference/market-data/#wss-v1streammarketdata--tick-stream) — and refuses the next with close code `4429`.

If a strategy genuinely needs more than a row allows, write to [developers@sahi.com](mailto:developers@sahi.com) rather than sharding across keys to work around it.

### WebSocket connections

Two streams, each documented with the resource it carries: [order updates](/api/v1/reference/orders/#wss-v1streamorders--order-updates) is JSON-framed text, and [the tick stream](/api/v1/reference/market-data/#wss-v1streammarketdata--tick-stream) is protobuf-framed binary. Four rules hold for both.

- **Authentication** is the same Bearer JWT as REST, sent in the upgrade request's `Authorization` header. There is no in-band login frame.
- **On token expiry** the server closes with **`4401`**. Mint a fresh token and reconnect; a socket is never extended past its token's `exp`.
- **Connection health.** The server pings every **30 seconds** and expects a pong within **15 seconds**. If none arrives it closes with **`4408`**. Most WebSocket libraries answer pings for you; if you work with raw frames, send the pong yourself.
- **Nothing is replayed** for the time a socket was down, and no connection state survives a reconnect. What that costs you differs by stream, so the recovery step lives with each: order updates re-run [Stream + Snapshot](/api/v1/reference/orders/#stream--snapshot), and the tick stream re-sends its subscriptions.

---

## Orders

### POST /v1/orders — Place order

**Scope:** `orders.write`

To learn what an order would block before you send it, post the same body to [Order margin](/api/v1/reference/funds/#post-v1marginsorder--order-margin).

#### Request

| Field | Type | Required | Notes |
|---|---|---|---|
| `exchange_segment` | string | yes | `NSE` \| `NFO` \| `BSE` \| `BFO`. |
| `symbol` | string | yes | The scrip master's `symbol` column (e.g. `RELIANCE`, `NIFTY29DEC26C24500`, `SENSEX26NOVFUT`). Look it up rather than building it: NFO and BFO contracts follow different exchange formats. |
| `txn_type` | string | yes | `B` \| `S`. |
| `qty` | integer | yes | Total quantity in units. Must not exceed the instrument's freeze quantity — see [Freeze quantity](#freeze-quantity). |
| `order_type` | string | yes | `LMT` \| `MKT` \| `SL-LMT` \| `SL-MKT`. |
| `product` | string | yes | `C` delivery \| `I` intraday \| `M` carry-forward F&O \| `F` MTF. Each is valid only on some segments — see [Product](#product). A wrong pair is refused with `400 VALIDATION_FAILED`. |
| `validity` | string | yes | `DAY` \| `IOC`. |
| `price` | integer | yes | Integer **paise**, not rupees: ₹119.65 is `11965`. A decimal is refused with `422 VALIDATION_FAILED`. Use `0` for `MKT` / `SL-MKT`. Must be a multiple of tick size for `LMT` / `SL-LMT`. |
| `trigger_price` | integer | conditional | Integer paise, as `price`. Required for `SL-LMT` / `SL-MKT`. |
| `disclosed_qty` | integer | no | Disclosed quantity. |
| `market_protection` | number | no | `MKT` / `SL-MKT` only: `-1` applies auto protection, or a custom percentage (`0.01`–`100`, e.g. `2` = 2%). Omitted means auto protection. `0` is rejected. Ignored for `LMT` / `SL-LMT`. See [Market protection](#market-protection). |
| `variant` | string | no | `REGULAR` (default) \| `AMO`. `AMO` queues an after-market order for the next trading session — `LMT` / `SL-LMT` only. See [After-market orders](#after-market-orders). |

#### Example

```http
POST /v1/orders
Authorization: Bearer eyJhbGciOiJFUzI1NiIs...
Content-Type: application/json
```
```json
{
  "exchange_segment": "NSE",
  "symbol": "RELIANCE",
  "txn_type": "B",
  "qty": 10,
  "order_type": "LMT",
  "product": "I",
  "validity": "DAY",
  "price": 249950
}
```

#### Response — `201 Created`

```json
{
  "order_ids": ["26101900133912345678"]
}
```

| Field | Type | Notes |
|---|---|---|
| `order_ids` | string[] | Always a list, and it may hold more than one entry — read it as a list rather than taking a single id out of it. |

The body is an acknowledgement; the full order state is observed via `GET /v1/orders` and live on the order-updates stream. Synchronous rejection returns a non-2xx error with `code` set per the error enum.

#### Market protection

Every `MKT` / `SL-MKT` order is placed with market protection: it is converted, once, into a limit order before it reaches the exchange (a SEBI retail-algo requirement — no unprotected market order is accepted).

- **`MKT`** becomes `LMT` priced at LTP plus or minus protection% (buy above, sell below), clamped to the day's price band and snapped to tick size.
- **`SL-MKT`** becomes `SL-LMT` priced at `trigger_price` plus or minus protection% (no market-data dependency).
- **`market_protection: -1`** (or omitting the field) applies auto protection, tiered by reference price — equity & futures: below ₹100 → 2%, ₹100–500 → 1%, above ₹500 → 0.5%; options: below ₹10 → 5%, ₹10–100 → 3%, ₹100–500 → 2%, above ₹500 → 1%.
- **`market_protection: 0`** is rejected; custom values must be between `0.01` and `100`.
- A `MKT` order for an instrument with no traded price (no LTP) is rejected with `422`.

The conversion is **one-shot**: the resulting order *is* a plain `LMT` / `SL-LMT` — `GET /v1/orders` shows the converted order type and the computed price, and later modifications follow plain limit-order semantics (modifying only `trigger_price` on a converted stop order keeps the existing limit price). To re-anchor protection at the current price, send `order_type: "MKT"` / `"SL-MKT"` (optionally with `market_protection`) in a modify.

#### After-market orders

A `REGULAR` order is refused while the market is closed (`422 VALIDATION_FAILED`; the message carries the next opening time). To place an order for the next session, send it with `variant: "AMO"`: Sahi accepts it, holds it, and releases it to the exchange when the next trading session opens. Use it while the market is closed.

- **`LMT` / `SL-LMT` only.** An AMO with `order_type` `MKT` / `SL-MKT` is rejected with `400`: the only price it could be protected at is the previous session's, not the one it will trade at. Price the order yourself.
- **Not for expired contracts.** An AMO on a contract past its expiry is rejected with `422`.
- **It shows as `Open` with `placed_at: null`** in `GET /v1/orders` and on the order-updates stream until the exchange takes it at open; from then on it is an ordinary order and `placed_at` is set. Read an `Open` order with `placed_at` `null` as one that has not reached the exchange yet.
- **Modify and cancel work while it waits**, through the usual endpoints. A cancelled AMO shows as `Cancelled`. It cannot be modified to `MKT` / `SL-MKT` (`400`), and `variant` itself is not modifiable.
- **Everything else is as for a regular order**: `product`, `validity`, `disclosed_qty` and the rate-limit budget are unchanged, and [`POST /v1/margins/order`](/api/v1/reference/funds/#post-v1marginsorder--order-margin) takes the same body.

#### Freeze quantity

Exchanges cap how much quantity one order may carry — the contract's **freeze quantity** (the `freeze_quantity` column in the scrip master, in units). A `qty` above it is rejected with `400 VALIDATION_FAILED`:

```json
{ "code": "VALIDATION_FAILED", "message": "qty must not exceed the exchange freeze quantity of 1800 for this instrument" }
```

- **One request is one order.** Sahi does not slice an oversized order into freeze-sized child orders for you, because each slice would be its own order with its own `order_id` and a single request cannot return a manageable order. Split the quantity yourself and send one request per slice.
- **The cap is the freeze quantity exactly.** A `qty` *equal* to it is accepted; only a larger one is refused.
- **Instruments with no cap are not restricted.** The scrip master's `freeze_quantity` is a per-order regulatory ceiling and carries `0` where none applies; `0` (or an absent value) means the quantity is unrestricted here.
- **Modify is capped the same way**, whenever the request carries a `qty`. A modify that leaves `qty` alone is never refused by this rule, even on an order that is somehow already above the cap.
- **Margin is not capped.** [`POST /v1/margins/order`](/api/v1/reference/funds/#post-v1marginsorder--order-margin) and [`POST /v1/margins/basket`](/api/v1/reference/funds/#post-v1marginsbasket--basket-margin) will quote a quantity larger than the freeze quantity, so you can size a position before deciding how to slice it.

---

### PUT /v1/orders/{order_id} — Modify order

**Scope:** `orders.write`

Only orders in modifiable states (`Open`, `OpenPartial`) can be modified — including an [after-market order](#after-market-orders) still waiting for the next session (`Open`, `placed_at` `null`).

#### Request

Provide only the fields being changed; at least one is required.

| Field | Type | Required | Notes |
|---|---|---|---|
| `qty` | integer | no | New total quantity. Must not exceed the instrument's freeze quantity — see [Freeze quantity](#freeze-quantity). |
| `price` | integer | no | Integer paise, not rupees, as on place order. |
| `order_type` | string | no | `LMT` \| `MKT` \| `SL-LMT` \| `SL-MKT`. An after-market order cannot be switched to `MKT` / `SL-MKT` (`400`). |
| `validity` | string | no | `DAY` \| `IOC`. |
| `trigger_price` | integer | no | Integer paise, as `price`. |
| `disclosed_qty` | integer | no | |
| `market_protection` | number | no | Applies when the merged modify targets `MKT` / `SL-MKT` (which re-runs the one-shot conversion — see [Market protection](#market-protection)); ignored otherwise, and not a modification by itself. |

#### Response — `200 OK`

```json
{
  "order_id": "26101900133912345678"
}
```

| Field | Type | Notes |
|---|---|---|
| `order_id` | string | The modified order, echoed back. |

`INVALID_ORDER_STATE` if the order is no longer modifiable. `ORDER_NOT_FOUND` if the `order_id` doesn't belong to the authenticated `sub`.

---

### DELETE /v1/orders/{order_id} — Cancel order

**Scope:** `orders.write`

Cancellable states: `Open`, `OpenPartial`.

#### Response — `204 No Content`

`INVALID_ORDER_STATE` if the order is already terminal. `ORDER_NOT_FOUND` if the order doesn't belong to the caller.

---

### GET /v1/orders — Order book (today)

**Scope:** `orders.read`

Returns every order on your account for the current trading day, in any status. Single-shot; no pagination.

One exception, and it is a fault on our side rather than a state you can reach: an order whose symbol is
missing from the day's scrip master is left out of `orders`. The scrip master always carries the instrument
for an order accepted today, so a gap means our instrument table is stale, and we log it. Reconcile against
[the order-updates stream](#wss-v1streamorders--order-updates), which reports the order either way.

#### Response — `200 OK`

```json
{
  "orders": [
    {
      "order_id": "26101900133912345678",
      "exchange_order_id": "1300000123456789",
      "exchange_segment": "NSE",
      "symbol": "RELIANCE",
      "txn_type": "B",
      "order_type": "LMT",
      "product": "I",
      "validity": "DAY",
      "qty": 10,
      "disclosed_qty": 0,
      "filled_qty": 4,
      "price": 250000,
      "trigger_price": 0,
      "avg_price": 249975,
      "status": "OpenPartial",
      "rejection_reason": null,
      "created_at": 1747798201123,
      "placed_at": 1747798201456,
      "completed_at": null,
      "cancelled_at": null,
      "rejected_at": null,
      "last_modified_at": 1747798202789
    }
  ]
}
```

`orders` holds one object per order. Its fields:

| Field | Type | Notes |
|---|---|---|
| `order_id` | string | Sahi's id for the order — the key you modify, cancel and reconcile by. |
| `exchange_order_id` | string | The exchange's id for the same order. |
| `exchange_segment` | string | `NSE` \| `NFO` \| `BSE` \| `BFO`. |
| `symbol` | string | The scrip master's `symbol` column — the same value `POST /v1/orders` takes. |
| `txn_type` | string | `B` \| `S`. |
| `order_type` | string | `LMT` \| `MKT` \| `SL-LMT` \| `SL-MKT`. |
| `product` | string | `C` \| `I` \| `M` \| `F` — see [Product](#product). |
| `validity` | string | `DAY` \| `IOC`. |
| `qty` | integer | Total quantity, units. |
| `disclosed_qty` | integer | Disclosed quantity. |
| `filled_qty` | integer | Units filled so far. |
| `price` | integer | Limit price, paise. |
| `trigger_price` | integer | Paise. `0` when the order carries no trigger. |
| `avg_price` | integer | Average fill price so far, paise. |
| `status` | string | See [Order status](#order-status). |
| `rejection_reason` | string \| null | Set when `status` is `Rejected`; `null` otherwise. |
| `created_at` through `last_modified_at` | integer \| null | Epoch ms. Each of the six timestamps is defined under [Timestamps](#timestamps). |

#### Order status

| Value | Meaning |
|---|---|
| `Open` | Working, no fills yet: at the exchange (`placed_at` set), or an [after-market order](#after-market-orders) waiting for the next session (`placed_at` `null`). |
| `OpenPartial` | Partially filled, remainder open at exchange. |
| `PartialFilled` | Partially filled, remainder cancelled / IOC unfilled. |
| `Completed` | Fully filled. |
| `Cancelled` | Cancelled by you, EOD expiry, or system. |
| `Rejected` | Rejected by Sahi risk or the exchange (`rejection_reason` set). |

#### Timestamps

All timestamps are integer epoch milliseconds. Each terminal-state timestamp is `null` until the order reaches that state.

| Field | Meaning |
|---|---|
| `created_at` | Time Sahi accepted the order request and passed risk checks. Always set. |
| `placed_at` | Time the order was placed on the exchange. |
| `completed_at` | Set when the order transitions to `Completed`. |
| `cancelled_at` | Set when the order transitions to `Cancelled`. |
| `rejected_at` | Set when the order transitions to `Rejected`. |
| `last_modified_at` | Wall-clock of the most recent change to any field on the order. Use this for ordering when reconciling the REST snapshot against the order-updates stream. |

---

### GET /v1/orders/{order_id} — Order details

**Scope:** `orders.read`

Returns one order of yours by `order_id`, for the current trading day. Use it
to follow an order you have just placed or modified without pulling the whole
book and filtering it.

#### Response — `200 OK`

```json
{
  "order_id": "26101900133912345678",
  "exchange_order_id": "1300000123456789",
  "exchange_segment": "NSE",
  "symbol": "RELIANCE",
  "txn_type": "B",
  "order_type": "LMT",
  "product": "I",
  "validity": "DAY",
  "qty": 10,
  "disclosed_qty": 0,
  "filled_qty": 4,
  "price": 250000,
  "trigger_price": 0,
  "avg_price": 249975,
  "status": "OpenPartial",
  "rejection_reason": null,
  "created_at": 1747798201123,
  "placed_at": 1747798201456,
  "completed_at": null,
  "cancelled_at": null,
  "rejected_at": null,
  "last_modified_at": 1747798202789
}
```

The body is the order object itself, not a wrapper: the same fields, with the
same meanings, as an element of the `orders` array in
[GET /v1/orders](#get-v1orders--order-book-today) — including
[Order status](#order-status) and [Timestamps](#timestamps), so whatever type
you already parse the order book's entries with parses this response too.

Polling this endpoint is not a substitute for
[the order-updates stream](#wss-v1streamorders--order-updates). Reach for it
when you hold a handful of `order_id`s and want the current state of one of
them; anything you follow continuously belongs on the socket.

`ORDER_NOT_FOUND` if the order isn't on today's book, or doesn't belong to the
caller. `VALIDATION_FAILED` if `order_id` isn't a well-formed Sahi order id.
`INTERNAL` if the order's symbol is missing from the day's scrip master — the
same stale-instrument fault that drops a row from
[the order book](#get-v1orders--order-book-today).

---

### GET /v1/orders/{order_id}/trades — Trades for an order

**Scope:** `orders.read`

Returns the individual fills that make up one of your orders, for the current
trading day. A single order fills in one or more trades, each at its own price —
this is where you see them separately rather than collapsed into the order
book's `filled_qty` and `avg_price`.

Single-shot; no pagination. Fills are ordered oldest first.

#### Response — `200 OK`

```json
{
  "trades": [
    {
      "exchange_trade_id": "80123456",
      "order_id": "26101900133912345678",
      "exchange_order_id": "1300000123456789",
      "exchange_segment": "NSE",
      "symbol": "RELIANCE",
      "txn_type": "B",
      "product": "I",
      "qty": 2,
      "price": 249950,
      "traded_at": 1747798201789
    },
    {
      "exchange_trade_id": "80123481",
      "order_id": "26101900133912345678",
      "exchange_order_id": "1300000123456789",
      "exchange_segment": "NSE",
      "symbol": "RELIANCE",
      "txn_type": "B",
      "product": "I",
      "qty": 2,
      "price": 250000,
      "traded_at": 1747798202104
    }
  ]
}
```

`trades` holds one object per fill. Its fields:

| Field | Type | Notes |
|---|---|---|
| `exchange_trade_id` | string | The exchange's id for this fill; unique within the order. |
| `order_id` | string | The order the fill belongs to — the id you asked for. |
| `exchange_order_id` | string \| null | The exchange's id for that order, as in the order book. |
| `exchange_segment` | string | `NSE` \| `NFO` \| `BSE` \| `BFO`. |
| `symbol` | string | The scrip master's `symbol` column — the same value `POST /v1/orders` takes. |
| `txn_type` | string | `B` \| `S`. |
| `product` | string | `C` \| `I` \| `M` \| `F` — see [Product](#product). |
| `qty` | integer | Units filled by *this* trade — not a running total. |
| `price` | integer | Price this trade filled at, paise. |
| `traded_at` | integer | Epoch ms. The exchange's match time for the fill. |

The fills above are the same order shown under
[GET /v1/orders](#get-v1orders--order-book-today): `2 + 2` units make its
`filled_qty` of `4`, and the quantity-weighted average of `249950` and `250000`
is its `avg_price` of `249975`.

Reconcile that way rather than assuming the two are written together. The order
book's totals and this list reach Sahi as separate messages from the exchange,
so a request made in the middle of a fill can briefly see one ahead of the
other. They converge once the order stops filling.

An order that never reached the exchange — one still `AwaitingTrigger`, or
rejected by Sahi risk before placement — has no fills, and returns
`{"trades": []}` rather than an error.

`ORDER_NOT_FOUND` if the order isn't on today's book, or doesn't belong to the
caller.

---

### WSS /v1/stream/orders — Order updates

**Scope:** `orders.read`

Scoped to your account: each connection only receives updates for the JWT's `sub`. No subscribe message — the server starts pushing as soon as the connection is open.

#### Server → client messages

Each frame is a JSON order object identical in shape to a single element of `GET /v1/orders` — the fields are tabulated [there](#get-v1orders--order-book-today).

```json
{
  "order_id": "26101900133912345678",
  "exchange_order_id": "1300000123456789",
  "exchange_segment": "NSE",
  "symbol": "RELIANCE",
  "txn_type": "B",
  "order_type": "LMT",
  "product": "I",
  "validity": "DAY",
  "qty": 10,
  "disclosed_qty": 0,
  "filled_qty": 10,
  "price": 250000,
  "trigger_price": 0,
  "avg_price": 249975,
  "status": "Completed",
  "rejection_reason": null,
  "created_at": 1747798201123,
  "placed_at": 1747798201456,
  "completed_at": 1747798205890,
  "cancelled_at": null,
  "rejected_at": null,
  "last_modified_at": 1747798205890
}
```

#### Stream + Snapshot

Delivery favours freshness over exactly-once. An order update may arrive **more than once** — the stream can replay recent events after a restart on our side — and nothing is replayed for the time the socket was down. Bootstrap in this order rather than trusting the socket alone:

1. Open the WebSocket and wait for the connection to be accepted.
2. *Then* fetch `GET /v1/orders`.
3. Keep the stream frames that arrive before the snapshot does. Do not discard them.
4. Reconcile per `order_id`, keeping the higher `last_modified_at`.

Every reconnect repeats the sequence, `4408` and `4409` included. Duplicates are absorbed by step 4 rather than needing to be prevented.

#### Close codes

| Code | Meaning |
|---|---|
| `1000` | Normal closure (client-initiated). |
| `4401` | Auth expired — token reached `exp`. Mint a fresh token and reconnect. |
| `4403` | Forbidden — token lacks required scope. In practice an under-scoped (or otherwise invalid) token is rejected at the HTTP upgrade handshake with `403`, before the WebSocket is established; this close code is reserved for scope failures detected after the upgrade. |
| `4408` | Ping timeout — no pong received within 15s of the server ping. |
| `4409` | Dropped — the client fell too far behind (slow consumer); reconnect and re-sync via `GET /v1/orders`. |
| `4429` | Per-account concurrent-connection limit exceeded — [5 open connections](/#rate-limits). |

---

## Portfolio

### GET /v1/positions — Positions

**Scope:** `positions.read`

Returns net positions across all products.

#### Response — `200 OK`

```json
{
  "positions": [
    {
      "exchange_segment": "NSE",
      "symbol": "RELIANCE",
      "instrument_id": 12027,
      "product": "I",
      "day_buy_qty": 10,
      "day_buy_amt": 2499750,
      "day_buy_avg_price": 249975,
      "day_sell_qty": 0,
      "day_sell_amt": 0,
      "day_sell_avg_price": 0,
      "open_buy_qty": 10,
      "open_buy_amt": 2499750,
      "open_buy_avg_price": 249975,
      "open_sell_qty": 0,
      "open_sell_amt": 0,
      "open_sell_avg_price": 0,
      "cf_buy_qty": 0,
      "cf_buy_amt": 0,
      "cf_buy_avg_price": 0,
      "cf_sell_qty": 0,
      "cf_sell_amt": 0,
      "cf_sell_avg_price": 0,
      "net_qty": 10,
      "net_avg_price": 249975,
      "total_buy_qty": 10,
      "total_buy_amt": 2499750,
      "total_buy_avg_price": 249975,
      "total_sell_qty": 0,
      "total_sell_amt": 0,
      "total_sell_avg_price": 0,
      "realised_pnl": 0,
      "last_modified_at": 1747798205890
    }
  ]
}
```

`positions` holds one object per position. Every `*_qty` is integer units; every `*_amt` and `*_avg_price` is integer paise. The buy/sell groups come in triples — quantity, amount, quantity-weighted average price — and a side with no quantity has all three at `0`.

| Field | Type | Notes |
|---|---|---|
| `exchange_segment` | string | `NSE` \| `NFO` \| `BSE` \| `BFO`. |
| `symbol` | string | The scrip master's `symbol` column — the same value `POST /v1/orders` takes. |
| `instrument_id` | integer | Scrip-master `id`. Use with the Market Data APIs. |
| `product` | string | `C` \| `I` \| `M` \| `F` — see [Product](#product). |
| `day_buy_qty`, `day_buy_amt`, `day_buy_avg_price` | integer | Buys executed today. |
| `day_sell_qty`, `day_sell_amt`, `day_sell_avg_price` | integer | Sells executed today. |
| `cf_buy_qty`, `cf_buy_amt`, `cf_buy_avg_price` | integer | The position carried forward from previous days, when it came in long. |
| `cf_sell_qty`, `cf_sell_amt`, `cf_sell_avg_price` | integer | The carried-forward position, when it came in short. |
| `open_buy_qty`, `open_buy_amt`, `open_buy_avg_price` | integer | The current net open position, when net long: the absolute net quantity at `net_avg_price`. |
| `open_sell_qty`, `open_sell_amt`, `open_sell_avg_price` | integer | The current net open position, when net short. |
| `net_qty` | integer | Signed: positive for long, negative for short. Carried-forward plus today's net. |
| `net_avg_price` | integer | Paise. Weighted across the carried-forward position and today's net when they point the same way; otherwise the larger side's average. |
| `total_buy_qty`, `total_buy_amt`, `total_buy_avg_price` | integer | Carried-forward plus today's buys. |
| `total_sell_qty`, `total_sell_amt`, `total_sell_avg_price` | integer | Carried-forward plus today's sells. |
| `realised_pnl` | integer | Realised P&L, paise. |
| `last_modified_at` | integer | Epoch ms of the last change to this position. |

---

### GET /v1/holdings — Holdings

**Scope:** `holdings.read`

Your demat holdings, one entry per ISIN. Today's
delivery-product activity is folded in: `net_qty` adjusts the holding for
today's delivery buys/sells, and the nested `position` object carries the day's
delivery totals for the same ISIN. Returns an empty array when you hold
nothing. An ISIN first bought for delivery today appears with zero settled
quantities (`t1_qty`, `dp_qty`, `holding_qty` all `0`) and today's buys in
`net_qty`/`position`.

#### Response — `200 OK`

```json
{
  "holdings": [
    {
      "isin": "INE002A01018",
      "instrument_ids": [12027, 725069],
      "t1_qty": 0,
      "dp_qty": 10,
      "holding_qty": 10,
      "holding_avg_price": 245050,
      "authorised_qty": 10,
      "net_qty": 15,
      "net_avg_price": 245100,
      "position": {
        "net_qty": 5,
        "net_avg_price": 245200,
        "buy_qty": 5,
        "buy_avg_price": 245200,
        "sell_qty": 0,
        "sell_avg_price": 0
      },
      "last_modified_at": 1747798205890
    }
  ]
}
```

| Field | Type | Notes |
|---|---|---|
| `isin` | string | The holding key. Matches the `isin` column of the scrip master. |
| `instrument_ids` | integer[] | Scrip-master `id` of every listing of this ISIN (e.g. NSE + BSE), ascending. Use with the Market Data APIs. |
| `t1_qty` | integer | Units bought but not yet settled into demat (T+1). |
| `dp_qty` | integer | Units settled in the demat account. |
| `holding_qty` | integer | `t1_qty + dp_qty`. |
| `holding_avg_price` | integer | Paise. Quantity-weighted average of the T1 and demat average prices; `0` when `holding_qty` is `0`. |
| `authorised_qty` | integer | Units EDIS-authorised for sale in the current trading session (or the next one when the market is closed). Delivery sells beyond this are rejected. |
| `net_qty` | integer | `holding_qty` adjusted for today's delivery buys/sells. |
| `net_avg_price` | integer | Paise. Re-weighted with today's delivery buys when today's delivery net is positive; otherwise equals `holding_avg_price`. |
| `position` | object | Today's delivery-product activity for the same ISIN, summed across exchanges. `position.net_qty` is signed (negative when today's delivery sells exceed buys); `*_avg_price` are paise. |
| `last_modified_at` | integer | Epoch ms of the last delivery trade today; `0` when there is none. |

No valuation/LTP fields are included — fetch prices via
[`GET /v1/marketdata/ltp`](#get-v1marketdataltp--last-traded-price) with the
returned `instrument_ids`.

---

## Account

### GET /v1/profile — Your profile

**Scope:** `profile.read`

Your identity and account status. Read it once at start of day rather than per request; it does not change during a session.

#### Response — `200 OK`

```json
{
  "user_id": "AB1234",
  "name": "Jane Doe"
}
```

| Field | Type | Notes |
|---|---|---|
| `user_id` | string | Your user id — the same identity the token was approved for. Opaque string. |
| `name` | string | Your name, as held on the account. |

`404 NOT_FOUND` if no profile exists for the account behind the token.

---

## Funds

### GET /v1/funds — Available balances

**Scope:** `funds.read`

What your account can fund right now, and the components behind it. Reflects the live balance on your trading account.

There is no single "available balance" to report. The OMS holds one risk snapshot per account, but funds an order from a different formula depending on what the order is: pledge collateral is spendable against an intraday position and not against a delivery buy, and option premium received is spendable only in the exchange group it was received in. So `available` carries one figure per order kind, and `balance`, `utilised` and `option_premium` carry the components those figures are built from.

Size an order against the figure for the order you are about to place. [`POST /v1/margins/order`](#post-v1marginsorder--order-margin) picks the same branch for you, for one specific order.

#### Response — `200 OK`

```json
{
  "available": {
    "stocks_delivery": 10500000,
    "intraday_and_fno_selling": 11500000,
    "options_buying": {
      "equity_fno": 11000000,
      "mcx": 10500000,
      "ncom": 10500000
    }
  },
  "balance": {
    "opening_balance": 10000000,
    "payin": 500000,
    "payout": 0,
    "collateral": 2000000,
    "delivery_sell_credit": 0
  },
  "utilised": {
    "span": 800000,
    "exposure": 200000,
    "delivery_margin": 0,
    "intraday_margin": 0,
    "delivery_buy": 0,
    "charges": 12500,
    "mtm_loss": 0
  },
  "option_premium": {
    "paid": 0,
    "received": 500000,
    "by_pool": {
      "equity_fno": -500000,
      "mcx": 0,
      "ncom": 0
    }
  }
}
```

Every figure is integer paise. The account above holds ₹1,05,000 of cash, ₹20,000 of pledge collateral, ₹10,000 of margin blocked on an F&O position, and has received ₹5,000 of equity option premium — which is why its four balances differ.

**`available`** — the balance the OMS will check an order of that kind against. Can be **negative** when the account is in debit.

| Field | Type | Notes |
|---|---|---|
| `stocks_delivery` | integer | Paise. For delivery orders (`product: "C"`). Pledge collateral is **not** spendable here. |
| `intraday_and_fno_selling` | integer | Paise. For everything that is neither a delivery order nor an option buy — stocks intraday, futures, option selling. Pledge collateral **is** spendable here. |
| `options_buying` | object | Paise per premium pool, see below. |

**`available.options_buying`** — RMS keeps option premium in three pools that must not cross-fund. Premium received is spending power only inside its own pool; in the other pools it may offset charges, but nothing more. Size an option buy against the pool its `exchange_segment` belongs to — using another pool's figure over-orders, and the OMS rejects the order.

| Pool | `exchange_segment` | Notes |
|---|---|---|
| `equity_fno` | `NFO`, `BFO` | Equity and index options. |
| `mcx` | `MCX` | MCX commodity options. |
| `ncom` | `NCOM` | NSE commodity options. |

All three are always present. A figure for a segment the account is not activated for is not tradable.

**`balance`** — the money in the account, before anything is blocked against it.

| Field | Type | Notes |
|---|---|---|
| `opening_balance` | integer | Paise. Cash carried into the trading day. |
| `payin` | integer | Paise. Funds added today. |
| `payout` | integer | Paise, positive. Funds withdrawn today. |
| `collateral` | integer | Paise. Margin available from pledged holdings. |
| `delivery_sell_credit` | integer | Paise, positive. Credit from today's delivery sells. |

**`utilised`** — what is blocked against that money.

| Field | Type | Notes |
|---|---|---|
| `span` | integer | Paise. SPAN margin on derivative positions. |
| `exposure` | integer | Paise. Exposure margin on derivative positions. |
| `delivery_margin` | integer | Paise. Physical-delivery margin, levied near expiry on physically settled contracts. |
| `intraday_margin` | integer | Paise. Margin blocked by today's intraday positions. |
| `delivery_buy` | integer | Paise. Cash blocked by today's delivery buys. |
| `charges` | integer | Paise. Brokerage and regulatory charges accrued today — the OMS reports them as one figure. |
| `mtm_loss` | integer | Paise, positive. Today's net mark-to-market loss (realised + unrealised); `0` when the account is in profit. Only a net loss blocks funds. |

**`option_premium`** — premium held today. `paid` and `received` are the account-level **net**, so at most one of them is non-zero; the per-pool figures are in `by_pool`.

| Field | Type | Notes |
|---|---|---|
| `paid` | integer | Paise, positive. Net premium paid across all pools. `0` whenever the account received more premium than it paid overall — including when it did pay premium in one of the pools. |
| `received` | integer | Paise, positive. Net premium received across all pools. |
| `by_pool` | object | Paise per pool, **signed**: positive is net premium paid in that pool, negative is net premium received. Keys are `equity_fno`, `mcx`, `ncom`, as under `available.options_buying`. |

Premium actually paid is the sum of the **positive** `by_pool` entries, not `paid` — and it is deducted from every option-buying pool, wherever it was paid. An account that received ₹4,000 of premium on equity F&O and ₹5,000 on NCOM while paying ₹2,000 on MCX reports `paid: 0` and `received: 700000` — the ₹9,000 received net of the ₹2,000 paid — and all three figures under `available.options_buying` are ₹2,000 lower for that MCX premium. Reconcile a pool balance against `by_pool`; `paid` and `received` are what the delivery and intraday balances use, where only the net matters.

#### How the balances are computed

The four figures under `available` are exact functions of the other three blocks, so any of them can be reconciled field by field. Writing

```
base     = balance.opening_balance + balance.payin - balance.payout
           - utilised.delivery_buy + balance.delivery_sell_credit
accrued  = utilised.charges + utilised.mtm_loss
blocked  = utilised.span + utilised.exposure + utilised.delivery_margin
           + utilised.intraday_margin
```

the delivery and intraday figures are

```
stocks_delivery =
    base - option_premium.paid
         - max(max(accrued - option_premium.received, 0) + blocked - balance.collateral, 0)

intraday_and_fno_selling =
    base + balance.collateral - option_premium.paid
         - max(accrued - option_premium.received, 0) - blocked
```

Collateral is the difference between them: in the delivery formula it can only offset the margin block (and never turns into spendable cash, hence the outer `max(…, 0)`), while in the intraday formula it is added outright.

Each option-buying pool uses its own premium, and only the *other* pools' received premium against charges:

```
received(p)   = max(-option_premium.by_pool[p], 0)
paid_total    = Σ over all three pools of max(option_premium.by_pool[p], 0)
others(p)     = Σ over the two pools other than p of received(that pool)

options_buying[p] =
    base + received(p) - paid_total
         - max(max(accrued - others(p), 0) + blocked - balance.collateral, 0)
```

Premium paid is deducted from every pool wherever it was paid; premium received is added back only in the pool that received it.

`404 NOT_FOUND` if the account behind the token has no trading account yet.

---

### POST /v1/margins/order — Order margin

**Scope:** `funds.read`

What an order would cost before you place it: the margin the OMS would block for it, and the balance you have to fund it. Nothing is placed, and the call is not IP-checked.

The body is the one you would send to [`POST /v1/orders`](/api/v1/reference/orders/#post-v1orders--place-order), so one order object serves both calls. It is validated the same way, and a `MKT` / `SL-MKT` order is quoted at the protected limit price it would be placed at (see [Market protection](/api/v1/reference/orders/#market-protection)) — the figure is for the order as it would actually reach the exchange, not for an unprotected fill at LTP. Fields that do not affect margin (`validity`, `disclosed_qty`, `variant`) are accepted and checked for shape, but do not change the answer. One rule from place order is deliberately not applied: `qty` is **not** capped at the instrument's [freeze quantity](/api/v1/reference/orders/#freeze-quantity), so you can quote a full position before slicing it into placeable orders.

#### Request

| Field | Type | Required | Notes |
|---|---|---|---|
| `exchange_segment` | string | yes | `NSE` \| `NFO` \| `BSE` \| `BFO`. |
| `symbol` | string | yes | The scrip master's `symbol` column (e.g. `RELIANCE`, `NIFTY29DEC26C24500`, `SENSEX26NOVFUT`). Look it up rather than building it: NFO and BFO contracts follow different exchange formats. |
| `txn_type` | string | yes | `B` \| `S`. |
| `qty` | integer | yes | Total quantity in units. |
| `order_type` | string | yes | `LMT` \| `MKT` \| `SL-LMT` \| `SL-MKT`. |
| `product` | string | yes | `C` delivery \| `I` intraday \| `M` carry-forward F&O \| `F` MTF. Each is valid only on some segments — see [Product](#product). A wrong pair is refused with `400 VALIDATION_FAILED`. |
| `validity` | string | yes | `DAY` \| `IOC`. Required for parity with place order; does not affect margin. |
| `price` | integer | yes | Integer **paise**, not rupees: ₹119.65 is `11965`. A decimal is refused with `422 VALIDATION_FAILED`. Use `0` for `MKT` / `SL-MKT`. Must be a multiple of tick size for `LMT` / `SL-LMT`. |
| `trigger_price` | integer | conditional | Integer paise, as `price`. Required for `SL-LMT` / `SL-MKT`. |
| `disclosed_qty` | integer | no | Accepted; does not affect margin. |
| `market_protection` | number | no | As on place order: sets the protected price a `MKT` / `SL-MKT` order is quoted at. Ignored for `LMT` / `SL-LMT`. |
| `variant` | string | no | `REGULAR` (default) \| `AMO`. Validated as on place order (a `MKT` / `SL-MKT` AMO is rejected); does not affect margin. |

#### Example

```http
POST /v1/margins/order
Authorization: Bearer eyJhbGciOiJFUzI1NiIs...
Content-Type: application/json
```
```json
{
  "exchange_segment": "NFO",
  "symbol": "NIFTY29DEC26C24500",
  "txn_type": "S",
  "qty": 65,
  "order_type": "LMT",
  "product": "M",
  "validity": "DAY",
  "price": 12550
}
```

#### Response — `200 OK`

```json
{
  "required_margin": 13245000,
  "available_margin": 25000000
}
```

| Field | Type | Notes |
|---|---|---|
| `required_margin` | integer | Paise. The margin the OMS would block for this order right now — the same figure a placement is checked against. |
| `available_margin` | integer | Paise. The balance available to fund this order, computed the way the OMS funds this kind of order (delivery, option buy, or intraday / F&O) — the same branch [`GET /v1/funds`](#get-v1funds--available-balances) reports under `available`, picked for this order's segment and product. |

The order is affordable when `available_margin` is at least `required_margin`. Both figures are a snapshot: prices, positions and other open orders move them, and a placement is checked afresh by the OMS, so a passing margin check does not guarantee acceptance.

An unknown `symbol` for the `exchange_segment` is refused with `422 VALIDATION_FAILED`; malformed fields with `400 VALIDATION_FAILED`, exactly as on place order. `404 NOT_FOUND` if the account behind the token has no trading account yet — the same answer `GET /v1/funds` gives. Between 04:45 and 07:00 IST, while the OMS runs its beginning-of-day processing, the request is refused with `503 UNDER_MAINTENANCE`; retry after 07:00.

---

### POST /v1/margins/basket — Basket margin

**Scope:** `funds.read`

What a basket of orders would cost together. The answer is for the basket as a whole: the OMS nets the legs against each other and against your existing positions, so a hedged basket needs less than the sum of its legs' individual [Order margin](#post-v1marginsorder--order-margin) figures — the difference is the margin benefit. Nothing is placed, and the call is not IP-checked.

Each leg is the exact [`POST /v1/orders`](/api/v1/reference/orders/#post-v1orders--place-order) body, treated exactly as on the single-order check: validated the same way, with `MKT` / `SL-MKT` legs quoted at their protected limit prices. One call costs one unit of the margin budget whatever the leg count, and up to 10 legs are accepted.

#### Request

| Field | Type | Required | Notes |
|---|---|---|---|
| `legs` | object[] | yes | 1 to 10 orders, each the exact [`POST /v1/orders`](/api/v1/reference/orders/#post-v1orders--place-order) body, validated as on [`POST /v1/margins/order`](#post-v1marginsorder--order-margin). One bad leg refuses the whole request, and the error message names the leg by its zero-based index. |

#### Example

```http
POST /v1/margins/basket
Authorization: Bearer eyJhbGciOiJFUzI1NiIs...
Content-Type: application/json
```
```json
{
  "legs": [
    {
      "exchange_segment": "NFO",
      "symbol": "NIFTY29DEC26C25000",
      "txn_type": "B",
      "qty": 65,
      "order_type": "LMT",
      "product": "M",
      "validity": "DAY",
      "price": 4200
    },
    {
      "exchange_segment": "NFO",
      "symbol": "NIFTY29DEC26C24500",
      "txn_type": "S",
      "qty": 65,
      "order_type": "LMT",
      "product": "M",
      "validity": "DAY",
      "price": 12550
    }
  ]
}
```

#### Response — `200 OK`

```json
{
  "required_margin": 8460000,
  "available_margin": 25000000
}
```

| Field | Type | Notes |
|---|---|---|
| `required_margin` | integer | Paise. The margin the OMS would block for the basket as a whole, right now — legs netted against each other and your existing positions. |
| `available_margin` | integer | Paise. As on [`POST /v1/margins/order`](#post-v1marginsorder--order-margin): the balance available to fund these orders, computed the way the OMS funds them. |

When every leg draws on the same margin pool, the basket is affordable when `available_margin` is at least `required_margin`. For a basket that mixes pools (say an equity delivery leg alongside a commodity option), `available_margin` is still quoted from a single pool, so that comparison can overstate what the account can fund across all the legs. Both figures are a snapshot, and a placement is checked afresh by the OMS — a passing check does not guarantee acceptance.

For a basket where every leg buys options, the figures are the OMS quote as-is: the OMS nets option premium received into `required_margin` while also counting it in `available_margin`, so the quoted requirement can understate what the placement will actually block.

Errors are as on [`POST /v1/margins/order`](#post-v1marginsorder--order-margin): an unknown `symbol` is `422 VALIDATION_FAILED`, malformed fields are `400 VALIDATION_FAILED` (naming the leg), `404 NOT_FOUND` means the account behind the token has no trading account yet, and `503 UNDER_MAINTENANCE` is the 04:45–07:00 IST maintenance window. Two refusals are this endpoint's own: an empty `legs` array is `400 VALIDATION_FAILED`, and a basket over the 10-leg cap is `422 VALIDATION_FAILED` — the same code an unknown symbol gets, so tell them apart by the message, which names the cap.

---

## Market data

### GET /v1/marketdata/ltp — Last traded price

**Scope:** `marketdata.read`

Single or bulk.

#### Request

| Param | Type | Required | Notes |
|---|---|---|---|
| `i` | integer | yes | An `instrument_id` from the scrip master. Repeat the parameter once per instrument, up to 100 per request. |

#### Example

```http
GET /v1/marketdata/ltp?i=12027&i=11886&i=466828
Authorization: Bearer eyJhbGciOiJFUzI1NiIs...
```

#### Response — `200 OK`

The `data` object is keyed by `instrument_id` (string form because JSON object keys are always strings; the value originated as an integer).

```json
{
  "data": {
    "12027": {
      "last_trade_price": 251000,
      "last_trade_time": 1747798260123
    },
    "11886": {
      "last_trade_price": 412540,
      "last_trade_time": 1747798260110
    },
    "466828": {
      "last_trade_price": 15275,
      "last_trade_time": 1747798260087
    }
  }
}
```

Each per-instrument value:

| Field | Type | Notes |
|---|---|---|
| `last_trade_price` | integer | Paise. |
| `last_trade_time` | integer \| null | Epoch milliseconds. `null` for non-tradable instruments (e.g. indices). |

Instruments that don't exist are returned as `"data": { "5073182": null }`; the request as a whole still returns `200`. Validation failures (non-integer `i`, > 100 entries) return `400` with `VALIDATION_FAILED`.

---

### GET /v1/marketdata/quotes — Full quote with market depth

**Scope:** `marketdata.read`

Single or bulk. Returns the REST equivalent of the tick stream's `depth_tick` — price, volume, DPR band, open interest, and market depth.

`exchange_segment` / `instrument_type` (present on WS ticks) are not repeated here — both are static attributes of the instrument, available from the scrip master the `instrument_id` came from.

#### Request

| Param | Type | Required | Notes |
|---|---|---|---|
| `i` | integer | yes | An `instrument_id` from the scrip master. Repeat the parameter once per instrument, up to 100 per request — the same shape as `/v1/marketdata/ltp`. |

#### Example

```http
GET /v1/marketdata/quotes?i=12027&i=5073182
Authorization: Bearer eyJhbGciOiJFUzI1NiIs...
```

#### Response — `200 OK`

The `data` object is keyed by `instrument_id` (string form because JSON object keys are always strings; the value originated as an integer).

```json
{
  "data": {
    "12027": {
      "last_trade_price": 251000,
      "last_trade_time": 1747798260123,
      "volume_today": 12450,
      "dpr_upper": 276100,
      "dpr_lower": 225900,
      "prev_open_interest": null,
      "open_interest": null,
      "best_buys": [
        { "price": 250950, "qty": 100, "num_orders": 3 },
        { "price": 250900, "qty": 250, "num_orders": 7 }
      ],
      "best_sells": [
        { "price": 251050, "qty": 80, "num_orders": 2 }
      ]
    },
    "5073182": null
  }
}
```

Each per-instrument value:

| Field | Type | Notes |
|---|---|---|
| `last_trade_price` | integer | Paise. |
| `last_trade_time` | integer \| null | Epoch milliseconds. `null` for non-tradable instruments (e.g. indices). |
| `volume_today` | integer | Cumulative traded volume today. `0` for non-tradable instruments. |
| `dpr_upper`, `dpr_lower` | integer | Daily price range (circuit limit) bounds, paise. |
| `prev_open_interest`, `open_interest` | integer \| null | Open interest. `null` for non-derivative instruments; always present on derivatives, where `0` is a real value meaning zero open interest — not "unknown". |
| `best_buys`, `best_sells` | object[] | Order-book levels, best price first — only price levels holding orders are included, up to 5 or 20 per side depending on the instrument's feed type. Empty when no order book exists: before pre-market opens, immediately after the start-of-day reset, and on instruments with no resting orders. Levels are never zero-padded. |
| `best_buys[].price` | integer | Bid/ask price at the level, paise. |
| `best_buys[].qty` | integer | Total quantity resting at the level. |
| `best_buys[].num_orders` | integer | Number of orders at the level. |

Instruments that don't exist are returned as `null` (as `5073182` above); the request as a whole still returns `200`. Validation failures (non-integer `i`, > 100 entries) return `400` with `VALIDATION_FAILED`.

---

### GET /v1/marketdata/candles — Historical OHLC

**Scope:** `marketdata.read`

One instrument per request. Supported `size` values: `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `1d`. Labels are case-sensitive — `1M` is **not** one minute and is rejected.

#### Request

| Param | Type | Required | Notes |
|---|---|---|---|
| `instrument_id` | integer | yes | Scrip-master ID. |
| `size` | string | yes | One of `1m`, `3m`, `5m`, `15m`, `30m`, `1h`, `1d`. |
| `from` | integer | yes | Window start, epoch milliseconds, inclusive. |
| `to` | integer | yes | Window end, epoch milliseconds, inclusive. Must satisfy `to >= from`. |
| `include_partial` | boolean | no | Default `false`. When `true` and the market is open, the in-progress candle for the current window is appended as the last entry. |
| `oi` | boolean | no | Default `false`. When `true`, each candle carries open interest as a 7th array element (see below). |

#### Example

```http
GET /v1/marketdata/candles?instrument_id=12027&size=1m&from=1747798200000&to=1747820100000
Authorization: Bearer eyJhbGciOiJFUzI1NiIs...
```

#### Response — `200 OK`

```json
{
  "instrument_id": 12027,
  "size": "1m",
  "candles": [
    [1747798200000, 250000, 250125, 249850, 249975, 12450],
    [1747798260000, 249975, 250050, 249900, 250000, 8120]
  ],
  "has_more": false
}
```

Each candle is a fixed-length array. By default it has 6 elements — `[timestamp, open, high, low, close, volume]`. When the request sets `oi=true`, a 7th element (`open_interest`) is appended to every candle. The width is determined solely by the request flag, so every candle in a given response has the same length.

| Index | Field | Present | Notes |
|---|---|---|---|
| 0 | `timestamp` | always | Candle open-time, integer epoch milliseconds, aligned to the window (e.g. for `1m`: 09:15:00 IST, 09:16:00 IST, and so on). |
| 1–4 | `open`, `high`, `low`, `close` | always | Integer paise. |
| 5 | `volume` | always | Quantity traded in the window, in units. `0` for windows with no trades — in that case `open`, `high`, `low` and `close` all repeat the previous window's `close`. |
| 6 | `open_interest` | only when `oi=true` | Integer open interest; `0` for non-derivative instruments. May carry forward across zero-volume windows for derivatives. |

With `oi=true` each candle is a 7-element array; the appended element is the integer open interest (`0` for non-derivative instruments). For example, a futures instrument:

```json
"candles": [
  [1747820040000, 1840000, 1841500, 1839000, 1840500, 5120, 34500],
  [1747820100000, 1840500, 1842000, 1840000, 1841750, 4880, 34620]
]
```

Candles are returned in ascending order of `timestamp` (index 0). The series covers every window in `[from, to]` — windows with no trades are included with a `0` volume (index 5) so you do not have to interpolate missing buckets.

A response holds at most **2500 candles** per request. When the requested range covers more windows than that, the response carries the **most recent 2500** and the older part of the range is omitted — the series is clipped at its *start*, not its end. `has_more` is `true` exactly when that happened.

To walk a longer history, page **backward**: set `to` to the first returned `timestamp - 1` and re-fetch, repeating until `has_more` is `false`. Advancing `from` does not page — the returned series already ends at `to`.

An unknown `instrument_id` returns `200` with an empty `candles` array. Validation failures (unsupported `size`, inverted range, non-integer parameters) return `400` with `VALIDATION_FAILED`.

---

### GET /v1/marketdata/optionchain/expiries — Option expiries

**Scope:** `marketdata.read`

The expiry dates an [option chain](#get-v1marketdataoptionchain--option-chain) can be requested for: the unexpired expiries the underlying has listed option contracts on within the scrip master's horizon — 93 days ahead on NSE, 63 on BSE, 123 on MCX and NCOM — nearest first. Longer-dated contracts the exchange lists are not in the scrip master and are not served here. An expiry stays listed through its own expiry day until the F&O session closes.

#### Request

| Param | Type | Required | Notes |
|---|---|---|---|
| `underlying_id` | integer | yes | The **underlying's** `instrument_id` from the scrip master — the index or stock, not a derivative. |

#### Example

```http
GET /v1/marketdata/optionchain/expiries?underlying_id=10854
Authorization: Bearer eyJhbGciOiJFUzI1NiIs...
```

#### Response — `200 OK`

```json
{
  "expiries": ["2026-10-27", "2026-11-03", "2026-12-29"]
}
```

Expiries are calendar dates in IST, `YYYY-MM-DD` — the one place a date is not an epoch-millisecond timestamp, because an expiry is a trading day, not an instant. An `underlying_id` with no listed options returns `200` with an empty array. A missing or non-integer `underlying_id` returns `400` with `VALIDATION_FAILED`.

---

### GET /v1/marketdata/optionchain — Option chain

**Scope:** `marketdata.read`

The full option chain for one underlying and expiry: every strike with its call and put leg — price, open interest, volume, top of book, implied volatility and greeks — in one request.

Quote fields are live feed snapshots. Implied volatility and greeks come from Sahi's market-analytics service — the same numbers the Sahi app's option chain shows — and are `null` for the chains it does not track.

#### Request

| Param | Type | Required | Notes |
|---|---|---|---|
| `underlying_id` | integer | yes | The **underlying's** `instrument_id` from the scrip master. |
| `expiry` | string | no | `YYYY-MM-DD`, one of the [expiries endpoint](#get-v1marketdataoptionchainexpiries--option-expiries)'s values. Omitted, the nearest unexpired expiry is used. |

#### Example

```http
GET /v1/marketdata/optionchain?underlying_id=10854&expiry=2026-12-29
Authorization: Bearer eyJhbGciOiJFUzI1NiIs...
```

#### Response — `200 OK`

```json
{
  "underlying_id": 10854,
  "expiry": "2026-12-29",
  "last_price": 2564280,
  "strikes": [
    {
      "strike": 2500000,
      "ce": {
        "instrument_id": 466828,
        "last_trade_price": 43078,
        "last_trade_time": 1758790260123,
        "average_price": 42150,
        "volume_today": 1245600,
        "open_interest": 2354200,
        "prev_open_interest": 2100800,
        "prev_close_price": 41260,
        "top_bid_price": 43050,
        "top_bid_qty": 650,
        "top_ask_price": 43100,
        "top_ask_qty": 520,
        "implied_volatility": 12.34,
        "greeks": {
          "delta": 0.5706,
          "gamma": 0.00044,
          "theta": -6.04,
          "vega": 28.38
        }
      },
      "pe": null
    }
  ]
}
```

Top level:

| Field | Type | Notes |
|---|---|---|
| `underlying_id` | integer | Echoes the request. |
| `expiry` | string | The resolved expiry, `YYYY-MM-DD` (IST) — useful when the request omitted it. |
| `last_price` | integer \| null | The underlying's last-traded price, paise. `null` when no snapshot exists for it. |
| `strikes` | object[] | One row per strike, ascending by strike price. |

Each strike row:

| Field | Type | Notes |
|---|---|---|
| `strike` | integer | Strike price, paise. |
| `ce`, `pe` | object \| null | The call / put leg. `null` when no such contract is listed at this strike or the feed has no snapshot for it yet. |

Each leg:

| Field | Type | Notes |
|---|---|---|
| `instrument_id` | integer | The option contract — tradable via the [order APIs](/api/v1/reference/orders/) as-is. |
| `last_trade_price` | integer | Paise. |
| `last_trade_time` | integer \| null | Epoch milliseconds. `null` before the contract's first trade. |
| `average_price` | integer | Day's average traded price, paise. |
| `volume_today` | integer | Cumulative traded volume today. |
| `open_interest`, `prev_open_interest` | integer \| null | Current / previous-day open interest. |
| `prev_close_price` | integer | Previous session's close, paise. |
| `top_bid_price`, `top_bid_qty` | integer \| null | Best bid and the quantity resting at it, paise. `null` when the bid book is empty. |
| `top_ask_price`, `top_ask_qty` | integer \| null | Best ask and the quantity resting at it. `null` when the ask book is empty. |
| `implied_volatility` | number \| null | Percent (e.g. `12.34` = 12.34%). `null` when the analytics service does not track this chain, or has not solved this leg — a leg with no premium yet, for instance. |
| `greeks` | object \| null | Present when `implied_volatility` is. |
| `greeks.delta` | number | Price change per 1.0 move of the underlying. Calls in `[0, 1]`, puts in `[-1, 0]`. |
| `greeks.gamma` | number | Delta change per 1.0 move of the underlying. |
| `greeks.theta` | number | Price change per **day** of time decay, in the premium's units (paise-denominated rupee terms match `last_trade_price / 100`). |
| `greeks.vega` | number | Price change per **1%** move in implied volatility. |

There is no `previous_volume` field — the live feed does not carry the prior session's volume. Derive it from the [candles endpoint](#get-v1marketdatacandles--historical-ohlc) (`size=1d`) if you need it.

An `expiry` that isn't a listed, unexpired expiry for the underlying — or an `underlying_id` with no listed options — returns `400` with `VALIDATION_FAILED`. Malformed parameters (non-integer `underlying_id`, an `expiry` not in `YYYY-MM-DD` form) return `400` with `VALIDATION_FAILED`. A chain the analytics service does not track still returns `200`, with `implied_volatility` and `greeks` null on every leg; the feed or the analytics service being unreachable returns `500` with `INTERNAL`.

---

### WSS /v1/stream/marketdata — Tick stream

**Scope:** `marketdata.read`

Three modes select the field subset sent on the wire.

Subscription state is **connection-local** and is not persisted across disconnects. After any reconnect (`4401`, `4408`, or otherwise) the client must re-send its `Subscribe` messages — the server starts a new connection with an empty subscription set.

There is nothing to reconcile on this stream. Every tick is a complete snapshot for its instrument at the currently-effective mode, so the newest one you hold is the answer and a duplicate costs nothing — no REST snapshot, no per-key merge. After a reconnect the next tick per instrument brings the value back up to date; if you need one before that tick arrives, read it once from [`GET /v1/marketdata/ltp`](#get-v1marketdataltp--last-traded-price) or [`GET /v1/marketdata/quotes`](#get-v1marketdataquotes--full-quote-with-market-depth).

#### Wire format

Binary WebSocket frames. Each frame carries exactly one `ClientMessage` (client → server) or `ServerMessage` (server → client), serialised as protobuf wire format.

#### Schema

```proto
syntax = "proto3";

package sahi.direct.marketdata.v1;

// Enums

enum ExchangeSegment {
  EXCHANGE_SEGMENT_INVALID = 0;
  EXCHANGE_SEGMENT_NSE = 1;
  EXCHANGE_SEGMENT_BSE = 2;
  EXCHANGE_SEGMENT_NFO = 3;
  EXCHANGE_SEGMENT_BFO = 4;
}

enum InstrumentType {
  INSTRUMENT_TYPE_INVALID = 0;
  INSTRUMENT_TYPE_INDEX = 1;
  INSTRUMENT_TYPE_STOCK = 2;
  INSTRUMENT_TYPE_ETF = 3;
  INSTRUMENT_TYPE_INDEX_FUT = 4;
  INSTRUMENT_TYPE_INDEX_OPT_CE = 5;
  INSTRUMENT_TYPE_INDEX_OPT_PE = 6;
  INSTRUMENT_TYPE_STOCK_FUT = 7;
  INSTRUMENT_TYPE_STOCK_OPT_CE = 8;
  INSTRUMENT_TYPE_STOCK_OPT_PE = 9;
}

enum Mode {
  MODE_INVALID = 0;
  MODE_LTP = 1;
  MODE_QUOTE = 2;
  MODE_DEPTH = 3;
}

// Client -> server

message ClientMessage {
  oneof payload {
    Subscribe   subscribe   = 1;
    Unsubscribe unsubscribe = 2;
    ModeChange  mode_change = 3;
  }
}

message Subscribe {
  Mode mode = 1;
  repeated int64 instrument_ids = 2;
}

message Unsubscribe {
  repeated int64 instrument_ids = 1;
}

message ModeChange {
  Mode mode = 1;
  repeated int64 instrument_ids = 2;
}

// Server -> client

message ServerMessage {
  oneof payload {
    Ack         ack        = 1;
    LtpTick     ltp_tick   = 2;
    QuoteTick   quote_tick = 3;
    DepthTick   depth_tick = 4;
    StreamError error      = 5;
  }
}

message Ack {
  enum Action {
    ACTION_INVALID = 0;
    ACTION_SUBSCRIBE = 1;
    ACTION_UNSUBSCRIBE = 2;
    ACTION_MODE_CHANGE = 3;
  }
  Action action = 1;
  repeated int64 instrument_ids = 2;
}

message StreamError {
  string code = 1;
  string message = 2;
}

message LtpTick {
  int64 instrument_id = 1;
  ExchangeSegment exchange_segment = 2;
  InstrumentType instrument_type = 3;
  int64 last_trade_price = 4;          // paise
  optional int64 last_trade_time = 5;  // epoch ms; absent for indices
}

message QuoteTick {
  int64 instrument_id = 1;
  ExchangeSegment exchange_segment = 2;
  InstrumentType instrument_type = 3;
  int64 last_trade_price = 4;
  optional int64 last_trade_time = 5;
  int64 volume_today = 6;
  int64 dpr_upper = 7;
  int64 dpr_lower = 8;
  optional int64 prev_open_interest = 9;  // derivative-only
  optional int64 open_interest = 10;      // derivative-only
}

message DepthTick {
  int64 instrument_id = 1;
  ExchangeSegment exchange_segment = 2;
  InstrumentType instrument_type = 3;
  int64 last_trade_price = 4;
  optional int64 last_trade_time = 5;
  int64 volume_today = 6;
  int64 dpr_upper = 7;
  int64 dpr_lower = 8;
  optional int64 prev_open_interest = 9;
  optional int64 open_interest = 10;
  // Only levels holding orders; up to 5 or 20 per side depending on the
  // instrument's feed type (L2 vs L3). Never zero-padded.
  repeated DepthLevel best_buys = 11;
  repeated DepthLevel best_sells = 12;
}

message DepthLevel {
  int64 price = 1;       // paise
  int64 qty = 2;
  int64 num_orders = 3;
}
```

#### Enums

| Proto enum | Values (prefix stripped) |
|---|---|
| `ExchangeSegment` | `NSE`, `BSE`, `NFO`, `BFO` |
| `InstrumentType` | `INDEX`, `STOCK`, `ETF`, `INDEX_FUT`, `INDEX_OPT_CE`, `INDEX_OPT_PE`, `STOCK_FUT`, `STOCK_OPT_CE`, `STOCK_OPT_PE` |
| `Mode` | `LTP`, `QUOTE`, `DEPTH` |

Each value in the schema above is prefixed with its enum name (e.g. `EXCHANGE_SEGMENT_NSE`); the table strips the prefix for readability.

#### Client → server (`ClientMessage` oneof)

| Variant | Fields | Meaning |
|---|---|---|
| `subscribe` | `mode`, `instrument_ids` | Add `instrument_ids` at the given `mode`. Idempotent. |
| `unsubscribe` | `instrument_ids` | Remove `instrument_ids` from the connection. |
| `mode_change` | `mode`, `instrument_ids` | Change mode for already-subscribed `instrument_ids`. |

#### Server → client (`ServerMessage` oneof)

| Variant | Meaning |
|---|---|
| `ack` | Server accepted a `subscribe` / `unsubscribe` / `mode_change`. Echoes the action and accepted `instrument_ids`. |
| `ltp_tick` / `quote_tick` / `depth_tick` | A snapshot for one instrument at the currently-effective mode. |
| `error` | Non-fatal error (e.g. unknown `instrument_id`, mode change on an unsubscribed id). Carries `code` and `message`; the connection stays open. |

Every tick variant carries the same identity fields (`instrument_id`, `exchange_segment`, `instrument_type`, `last_trade_price`, `last_trade_time`). Higher modes add more.

| Variant | Mode | Additional fields beyond the identity set |
|---|---|---|
| `LtpTick` | `LTP` | *(none)* |
| `QuoteTick` | `QUOTE` | `volume_today`, `dpr_upper`, `dpr_lower`, `prev_open_interest`, `open_interest` |
| `DepthTick` | `DEPTH` | `QuoteTick` fields **plus** repeated `best_buys` and `best_sells`. Each `DepthLevel` array carries only price levels holding orders, up to 5 or 20 depending on the instrument's feed type (L2 vs L3) — never zero-padded. |

#### Field semantics

Price fields (`last_trade_price`, `dpr_upper`, `dpr_lower`, `DepthLevel.price`) are integer **paise**. Quantities (`volume_today`, `prev_open_interest`, `open_interest`, `DepthLevel.qty`, `DepthLevel.num_orders`) are integer counts. `last_trade_time` is integer epoch milliseconds.

`last_trade_time` is absent (proto3 `optional`, no value) for non-tradable instruments (indices). `prev_open_interest` and `open_interest` are absent for non-derivative instruments. `volume_today` is `0` before the first trade of the day and after the start-of-day reset, then accumulates through the session.

`dpr_upper` and `dpr_lower` are the exchange-imposed **Daily Price Range** bounds (also called circuit limits) in paise — the upper and lower price band within which the exchange will accept orders for this instrument on the current trading day. Orders priced outside this band are rejected by the exchange.

#### Per-connection limits

- Maximum subscribed `instrument_ids` per connection: `1000` by default, configurable per account.
- Maximum concurrent connections per token: `5`. The next is refused with close code `4429`; see [Rate limits](/#rate-limits).
- Mode changes are per-`instrument_id`; a connection can hold a mix of modes simultaneously.

#### Close codes

| Code | Meaning |
|---|---|
| `1000` | Normal closure. |
| `4401` | Auth expired. |
| `4403` | Forbidden — token lacks `marketdata.read`. In practice an under-scoped (or otherwise invalid) token is rejected at the HTTP upgrade handshake with `403`, before the WebSocket is established; this close code is reserved for scope failures detected after the upgrade. |
| `4408` | Ping timeout — no pong received within 15s of the server ping. |
| `4429` | Per-token concurrent-connection limit exceeded — [5 open connections](/#rate-limits). |

## Scrip master

Master reference for every tradable and quotable instrument. Download the CSV at start of day and pass its `id` column as `instrument_id` for every market-data call (`/v1/marketdata/ltp`, `/v1/marketdata/quotes`, `/v1/marketdata/candles`, `WSS /v1/stream/marketdata`) and as the `instrument_id` returned in positions.

- **Format:** CSV, UTF-8, RFC 4180 (fields containing `,`, `"`, or newlines are double-quoted). Header row included. One instrument per row.
- **Refresh:** rebuilt once per trading day before the pre-open phase (around 06:00 IST). The file is immutable for the day; new listings or status changes flow on the next day's file.
- **URL:** [`https://assets.sahi.com/external/instruments.csv`](https://assets.sahi.com/external/instruments.csv)

### Columns

The header row is, verbatim:

```
id,isin,symbol,company_name,series,underlying_symbol,exchange,segment,token,instrument_type,option_type,expiry_date,strike_price,lot_size,tick_size,freeze_quantity,price_precision,price_multiplier
```

Read columns by header name, not position.

| Column | Type | Notes |
|---|---|---|
| `id` | int | Primary key — pass as `instrument_id` in all Market Data API calls; matches the `instrument_id` returned in positions. Stable across trading days for the same instrument. |
| `isin` | string | 12-character ISIN. Empty for derivatives and indices. |
| `symbol` | string | The symbol `POST /v1/orders` takes and the order book returns: the exchange trading symbol, with the `-EQ` series suffix dropped on NSE cash (`RELIANCE`, `3IINFOLTD-BE`, `NIFTY27OCT26C25000`). Empty for indices, which are not tradable. |
| `company_name` | string | Display name. Empty for NSE, BSE and NCOM derivatives. |
| `series` | string | Cash-equity series (`EQ`, `BE`, `A`, `B`, and so on). Empty for derivatives and indices. |
| `underlying_symbol` | string | Underlying symbol for derivatives; empty otherwise. |
| `exchange` | string | Listing exchange: `NSE`, `BSE`, `MCX` or `NCOM`. Derivatives carry the listing exchange here, so an NSE option has `exchange=NSE`; use `segment` for orders. |
| `segment` | string | The `exchange_segment` Order APIs take with `symbol`: `NSE`, `NFO`, `BSE` or `BFO`. Commodity rows carry `MCX` or `NCOM`. |
| `token` | int | Exchange-assigned numeric token. Not accepted by these APIs — always reference an instrument by `id`. |
| `instrument_type` | string | `STK`, `ETF`, `IDX`, `FUTSTK`, `FUTIDX`, `OPTSTK`, `OPTIDX` on NSE and BSE; `FUTBAS`, `FUTBLN`, `FUTENR`, `OPTFUT`, `UNDCOM` on MCX and NCOM. See [Field mappings](#field-mappings) for the proto `InstrumentType` used on the tick stream. |
| `option_type` | string | `CE` (call) or `PE` (put). Empty for non-options. |
| `expiry_date` | string | `DD-MM-YYYY` for derivatives; empty otherwise. |
| `strike_price` | decimal | Strike price in **rupees** (decimal). `0.00` for non-options, except NSE futures, which carry `-0.01`. |
| `lot_size` | int | Tradable lot size; order quantity must be a multiple of it. Usually `1` for cash equities, but some carry larger lots, such as `25000` for privately placed InvITs; `0` for indices. |
| `tick_size` | decimal | Minimum price increment in **rupees** (decimal). |
| `freeze_quantity` | int | Per-order regulatory quantity ceiling, in units; `0` if not applicable. |
| `price_precision` | int | Decimal places in a quoted price: `2` for every tradable instrument, `0` for indices. |
| `price_multiplier` | decimal | Contract value = price × quantity × `price_multiplier`. `1` for NSE and BSE instruments; commodity contracts carry their own (`100` for MCX GOLD, `0.1` for GOLDM), fractional for some. `0` for indices. |

### Field mappings

**Marketdata WS `InstrumentType`** is derived from CSV `instrument_type` + `option_type` for NSE and BSE rows:

| CSV `instrument_type` | CSV `option_type` | proto `InstrumentType` |
|---|---|---|
| `STK` | — | `STOCK` |
| `ETF` | — | `ETF` |
| `IDX` | — | `INDEX` |
| `FUTSTK` | — | `STOCK_FUT` |
| `FUTIDX` | — | `INDEX_FUT` |
| `OPTSTK` | `CE` | `STOCK_OPT_CE` |
| `OPTSTK` | `PE` | `STOCK_OPT_PE` |
| `OPTIDX` | `CE` | `INDEX_OPT_CE` |
| `OPTIDX` | `PE` | `INDEX_OPT_PE` |

### Sample records

```csv
id,isin,symbol,company_name,series,underlying_symbol,exchange,segment,token,instrument_type,option_type,expiry_date,strike_price,lot_size,tick_size,freeze_quantity,price_precision,price_multiplier
10854,,,Nifty 50,,,NSE,NSE,26000,IDX,,,0.00,0,0.00,0,0,0
12027,INE002A01018,RELIANCE,Reliance Industries,EQ,,NSE,NSE,2885,STK,,,0.00,1,0.10,0,2,1
10914,INE748C01038,3IINFOLTD-BE,3i Infotech,BE,,NSE,NSE,6240,STK,,,0.00,1,0.01,0,2,1
725069,INE002A01018,RELIANCE,Reliance Industries,A,,BSE,BSE,500325,STK,,,0.00,1,0.05,0,2,1
1914891,,NIFTY27OCT26C25000,,,NIFTY,NSE,NFO,51440,OPTIDX,CE,27-10-2026,25000.00,65,0.05,3510,2,1
1914890,,NIFTY27OCT26P25000,,,NIFTY,NSE,NFO,51441,OPTIDX,PE,27-10-2026,25000.00,65,0.05,3510,2,1
1963491,,RELIANCE23NOV26F,,,RELIANCE,NSE,NFO,61697,FUTSTK,,23-11-2026,-0.01,500,0.10,20000,2,1
2027645,,ALUMINI29JAN27,ALUMINI,,ALUMINI,MCX,MCX,587169,FUTBAS,,29-01-2027,0.00,1,0.05,150,2,1000
```

---
