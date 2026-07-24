# Market Data Stream

The Bridge Package exposes 8 binary streaming event types. Each event has a fixed length and fixed byte layout, documented per event below. Connection and subscription use the same Bridge Package flow as [Order and Trade Updates](06-order-and-trade-updates.md#connecting-and-subscribing-python-sdk-example) — connect to `bridge.iiflcapital.com:8883` with your `userSession` token, then subscribe.

> Up to 6000 event subscriptions are allowed per client, with a maximum of 1024 subscription requests sent in a single call.

| Event | Setter Property | Length (bytes) | Description |
| --- | --- | --- | --- |
| Market Feed | `on_feed_data_received` | 188 | Prices, volumes, and market depth for equities, F&O, and indices |
| Open Interest | `on_open_interest_data_received` | 16 | Current, day-high, and day-low open interest for F&O contracts |
| Market Status | `on_market_status_data_received` | 2 | Opening/closing events across the normal market's sessions |
| Upper Circuit | `on_upper_circuit_data_received` | 12 | Fired when a security hits its daily upper price band |
| Lower Circuit | `on_lower_circuit_data_received` | 12 | Fired when a security hits its daily lower price band |
| LPP | `on_lpp_data_received` | 12 | Limit order price range updates for F&O contracts |
| 52 Week High | `on_high_52_week_data_received` | 12 | Fired when an instrument hits a new 52-week high |
| 52 Week Low | `on_low_52_week_data_received` | 12 | Fired when an instrument hits a new 52-week low |

Subscribe using `<exchange>/<instrumentId>` topics (all lowercase), e.g.:

```python
req = '{"subscriptionList": ["nseeq/2885","nsefo/35005"]}'
connection_object.subscribe_feed(req)
connection_object.on_feed_data_received = market_feed_handler
```

See the [Binary Decoding Guide](11-binary-decoding-guide.md) for how to turn a raw event payload into readable values.

## Market Feed

Topic template: `<exchange>/<instrumentId>` (e.g. `nseeq/2885`, `nsefo/35005`, `bseeq/999901` for an index — depth/volume are 0 for indices).

| Field | Type | Bytes | Description |
| --- | --- | --- | --- |
| `ltp` | Int32 | 0-3 | Last traded price |
| `lastTradedQuantity` | UInt32 | 4-7 | Quantity of the last trade |
| `tradedVolume` | UInt32 | 8-11 | Total traded volume |
| `high` / `low` | Int32 | 12-15 / 16-19 | Session high / low |
| `open` / `close` | Int32 | 20-23 / 24-27 | Session open / previous close |
| `averageTradedPrice` | Int32 | 28-31 | Average traded price for the session |
| `reserved` | UInt16 | 32-33 | Reserved for future use |
| `bestBidQuantity` / `bestBidPrice` | UInt32 / Int32 | 34-37 / 38-41 | Best buy quantity / price |
| `bestAskQuantity` / `bestAskPrice` | UInt32 / Int32 | 42-45 / 46-49 | Best sell quantity / price |
| `totalBidQuantity` / `totalAskQuantity` | UInt32 | 50-53 / 54-57 | Total buy / sell quantity |
| `priceDivisor` | Int32 | 58-61 | Divide raw prices by this to get the decimal price |
| `lastTradedTime` | Int32 | 62-65 | Timestamp of the last trade |
| `marketDepth` | Int16[120] | 66-185 | 5 bid + 5 ask depth levels — see below |

### Market Depth Levels (bytes 66-185)

Each of the 5 bid and 5 ask levels repeats the same 12-byte layout (`quantity`, `price`, `orders`, then 2 ignored bytes):

| Level | Bid quantity/price/orders bytes | Ask quantity/price/orders bytes |
| --- | --- | --- |
| 1 | 66-75 | 126-135 |
| 2 | 78-87 | 138-147 |
| 3 | 90-99 | 150-159 |
| 4 | 102-111 | 162-171 |
| 5 | 114-123 | 174-183 |

Bytes 184-187 are ignored/padding.

---

## Open Interest Stream

Topic template: `<exchange>/<instrumentId>` (e.g. `nsefo/35005`).

| Field | Type | Bytes | Description |
| --- | --- | --- | --- |
| `openInterest` | Int32 | 0-3 | Outstanding derivative contracts |
| `dayHighOi` | Int32 | 4-7 | Day's highest OI |
| `dayLowOi` | Int32 | 8-11 | Day's lowest OI |
| `previousOi` | Int32 | 12-15 | Previous session's OI |

---

## Market Status

Topic template: `<exchange>` (e.g. `nseeq`).

| Field | Type | Bytes | Description |
| --- | --- | --- | --- |
| `MarketStatusCode` | Int16 | 0-1 | Exchange status code — see below |

| Code | Status |
| --- | --- |
| 0 | Pre-Open Started |
| 1 | Pre-Open Closed |
| 2 | Market Opened |
| 3 | Call Auction Started |
| 4 | Call Auction Closed |
| 5 | Auction Market Started |
| 6 | Auction Market Closed |
| 7 | Market Closed |
| 8 | Closing Session Opened |
| 9 | Closing Session Closed |
| 10 | Halt |

---

## Upper Circuit Change

Topic template: `<exchange>` (e.g. `nseeq`).

| Field | Type | Bytes | Description |
| --- | --- | --- | --- |
| `instrumentId` | UInt32 | 0-3 | Instrument identifier |
| `upperCircuit` | UInt32 | 4-7 | Upper daily price range limit reached |
| `priceDivisor` | Int32 | 8-11 | Divide `upperCircuit` by this to get the decimal price |

---

## Lower Circuit Change

Topic template: `<exchange>` (e.g. `nseeq`).

| Field | Type | Bytes | Description |
| --- | --- | --- | --- |
| `instrumentId` | UInt32 | 0-3 | Instrument identifier |
| `lowerCircuit` | UInt32 | 4-7 | Lower daily price range limit reached |
| `priceDivisor` | Int32 | 8-11 | Divide `lowerCircuit` by this to get the decimal price |

---

## Limit Price Protection (LPP) Change

Topic template: `<exchange>/<instrumentId>` (e.g. `nsefo/35005`).

| Field | Type | Bytes | Description |
| --- | --- | --- | --- |
| `lppHigh` | UInt32 | 0-3 | Updated high execution band for limit orders |
| `lppLow` | UInt32 | 4-7 | Updated low execution band for limit orders |
| `priceDivisor` | Int32 | 8-11 | Divide `lppHigh`/`lppLow` by this to get the decimal price |

---

## 52 Week High Change

Topic template: `<exchange>` (e.g. `nseeq`).

| Field | Type | Bytes | Description |
| --- | --- | --- | --- |
| `instrumentId` | UInt32 | 0-3 | Instrument identifier |
| `52WeekHigh` | UInt32 | 4-7 | Updated 52-week high price |
| `priceDivisor` | Int32 | 8-11 | Divide `52WeekHigh` by this to get the decimal price |

---

## 52 Week Low Change

Topic template: `<exchange>` (e.g. `nseeq`).

| Field | Type | Bytes | Description |
| --- | --- | --- | --- |
| `instrumentId` | UInt32 | 0-3 | Instrument identifier |
| `52WeekLow` | UInt32 | 4-7 | Updated 52-week low price |
| `priceDivisor` | Int32 | 8-11 | Divide `52WeekLow` by this to get the decimal price |
