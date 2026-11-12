# NEO WebSocket (Market Data)

The Kotak Neo WebSocket ZIP (`Websocket (2).zip`, ~29.5 KiB) contains 4 major files:

1. `HSLib`
2. `Demo.html`
3. `Demo.js`
4. `Neo.js`

To start the WebSocket, make sure the position of these files is aligned as shown in the ZIP's example layout.

Open `demo.html` — it opens a web page in your browser to drive the connection.

## Establishing the Connection

To establish the connection the user passes 3 parameters:

- **Token** — final token (session token) received after running the login API
- **sid** — session sid received after running the login API
- **Data Center** — returned in the login API response (e.g. `E43`, `E41`, ...), passed as `'dataCenter': '123'`

> If you're using Postman for testing, `https://mis.kotaksecurities.com/login/1.0/tradeApiValidate` returns all 3 of the above values.

## Connect to Market Feed (HSM)

HSM is the stream that delivers market data. When you pass Session Token, SID and Data Center, you can connect with HSM — click **"Connect HSM"**.

### Subscribe Scrip

Provide the exchange identifier to start receiving feeds.

Format: `nse_cm|11536&`

One scrip input consists of the exchange name, a pipe separator (`|`), then the scrip identifier. To add another scrip in the same input, use an ampersand (`&`) separator.

### Subscribe Index

Provide the exchange identifier of indices to start receiving feeds.

Format: `nse_cm|Nifty 50&`

Same pipe + ampersand structure as scrips.

### Subscribe Depth

Format: `nse_cm|11536&`

One market-depth input consists of the exchange name, a pipe separator (`|`), then the scrip identifier. Add another with an ampersand (`&`) separator.

## Connect to Order Feed (HSI)

HSI is the stream that delivers order updates. Connect with HSI to view feeds of orders you have placed. The feeds reflect in the **Streaming Orders** column.

## Integrating market/order feed in code

By running Inspect on the `demo.html` file you can get the WebSocket string.

For in-depth detail of WebSocket functions, refer: <https://www.hypersync.in/hs_interactive_api_js/>

## Limits

- Total number of channels a user can use at a time: **16**
- Total number of scrips a user can subscribe to at a time: **200**

The two figures above apply to the legacy HSM/HSI browser stream described in this document. The newer async SFeed client has its own separate limit: at most **3000** input tokens may be subscribed at once, counted as a running total across all subscribe requests (touch line, option chain, index, depth and so on). A request that would push the running total past 3000 is rejected and nothing is sent. Do not confuse this figure with the 16-channel / 200-scrip legacy limits.

## Field Mapping in the WebSocket Response

| Field | Meaning |
| --- | --- |
| tk | Exchange Token |
| ts | Trading Symbol |
| e | Exchange |
| ltp | Last Traded Price |
| ltq | Last Traded Quantity |
| tbq | Total Buy Qty |
| tsq | Total Sell Qty |
| bp | Best Bid Price |
| bq | Best Bid Qty |
| sp | Best Ask Price |
| bs | Best Ask Qty |
| op | Open |
| h | High |
| lo | Low |
| c | Previous Close |
| cng | Change |
| nc | % Change |
| ap | Average Traded Price |
| to | Turnover |
| oi | Open Interest |
| ltt | Last Trade Time |
| fdtm | Feed Time |
| prec | Price Precision |
| lcl | Lower Circuit |
| ucl | Upper Circuit |
| yh | 52 Week High |
| yl | 52 Week Low |
| mul | Price/Contract Multiplier |
| name | Feed Type (sf) |

## Market Status and Closing Auction (SFeed client)

Everything above describes the legacy browser stream (`Websocket (2).zip`, HSLib / Demo.html / Demo.js / Neo.js) that connects to HSM for market data and HSI for order updates. The message types in this section belong to Kotak's newer async **SFeed** WebSocket client instead. They are not available on the legacy HSM stream, so do not assume an HSM subscription will deliver them.

These are two different wire protocols on two different hosts, not two clients over one feed:

| | HSM (legacy) | SFeed (current) |
| --- | --- | --- |
| Host | `wss://mlhsm.kotaksecurities.com` | `wss://sfeed.kotaksecurities.com/apifeed` |
| Byte order | Big-endian | Little-endian, packed (`#pragma pack(1)`) |
| Framing | Topic-based, 1-byte message type | 9-byte header, `uint16` message code, batched packets |
| Message codes | 1 to 10 (`CONNECTION`, `DATA`, `SUBSCRIBE`, ...), with response types 83/85 | 104, 105, 1109, 1117/1119, 6511, 6521, 7207, 7208 |

The two code spaces do not overlap in meaning and are not even the same width, so a decoder written for one cannot read the other. Code `104` is not a valid HSM message type.

### Which feed your data centre is routed to

Kotak resolves the feed host per data centre from a config service rather than from a fixed URL:

```
GET https://lapi.kotaksecurities.com/5config/config?appVersion=<v>&platform=api&environment=prod
```

The lookup is two-step. `{data_center}_broadcast_source` gives the source in use (`hs`, `sh` or `ks`), which then builds `{data_center}_{broadcast_source}_broadcast_endpoint` (market data) and `{data_center}_{broadcast_source}_interactive_endpoint` (order feed).

Checked against the live prod config on 2026-09-07: every data centre (E201, E21, E22, E25, E41, E43) selects `sh`, and E210/E220/E410/E430 select `ks`. **None selects `hs`.**

The `hs` keys have also started disappearing from the config rather than merely going unused. The primary data centres (E21, E22, E25, E41, E43, E201) no longer carry an `_hs_broadcast_endpoint` key at all; they keep only `_hs_base_url` and `_hs_interactive_endpoint`. The surviving `_hs_broadcast_endpoint` entries pointing at `mlhsm.kotaksecurities.com` are limited to E210, E220, E410, E430 and the two legacy keys `adc` and `gdcd`.

### Status of the HSM feed

HSM is deprecated but not switched off. As of 2026-09-07:

- `mlhsm.kotaksecurities.com` still completes a WebSocket upgrade (HTTP 101), and its TLS certificate has been renewed to expire 11 Nov 2026. It resolves to Cloudflare (104.18.x), unlike `sfeed`/`cdtstream`, which sit on Kotak's own range (121.240.x).
- Kotak's Python SDK has no code path to it. `HSWebSocket`, `HSIWebSocket` and `NeoWebSocket` were **removed in SDK 2.2.0** and survive only as migration stubs that raise a "no direct replacement" error (`neo_api.py`, `docs/scripts/migrate_from_v2.py`). Searching SDK v3.0.6 for `mlhsm`, `hslib` or `hypersync` returns nothing.
- There is no HSM fallback. When the config lookup fails for any reason, `resolve_dynamic_urls()` leaves the URL unset and the caller falls back to the hardcoded `SFEED_WEBSOCKET_URL = "wss://sfeed.kotaksecurities.com/apifeed"` (`neo_api_client/utils/urls.py`).
- The removal was never announced. The v3.0.6 changelog does not mention HSM at all.

A client that still speaks HSM works today only because it hardcodes the host instead of consulting the config service. Expect no deprecation notice before it stops.

### The order feed is not affected

The HSM-to-SFeed migration covers market data only. Both sources resolve the order feed to the same host:

```
E21_hs_interactive_endpoint = e21.kotaksecurities.com/realtime
E21_sh_interactive_endpoint = https://e21.kotaksecurities.com/realtime
```

The SDK's own fallback derives the identical URL from `baseUrl` (`_to_realtime_url`), so an order-feed client needs no change.

### Closing auction session (CAS) change — message code 104

Message code `104` carries closing auction session reference-price and order-imbalance updates.

It is not a separate subscription. CAS change messages arrive on your existing scrip and depth subscriptions, interleaved with the normal touch-line and depth data.

| Field | Meaning |
| --- | --- |
| ref_price | Closing auction reference price, scaled by the per-exchange divider like every other price field |
| imbalance_qty | Order imbalance quantity |
| imbalance_qty_at_market | Order imbalance quantity at market |

These values are only meaningful during the CAS window. Outside that window the exchange still broadcasts the packet with all three fields set to zero; the SDK drops that case rather than delivering an empty message. A packet in which only some of the three fields are zero is still delivered.

### Market status

Market status reaches the client two ways:

- From touch-line-style subscriptions, as message codes `6511` and `6521`. These are header-only packets with no body.
- From a dedicated exchange subscription, as message code `105`, which carries a real body.

The dedicated subscription sends a single frame and takes no tokens at all:

```json
{"event": "subscribeExchange"}
```

The matching unsubscribe is:

```json
{"event": "unsubscribeExchange"}
```

Fields on a market status message:

| Field | Meaning |
| --- | --- |
| exchange_segment | Exchange segment the status applies to |
| status_code | Numeric market status code (see table below) |
| status | Status text |

There is no instrument token or trading symbol on this message type — the wire packet carries no token field.

For the header-only `6511` and `6521` cases there is no body to read, so the status code is synthesized as `1` and `2` respectively.

The raw status string on the wire is unreliable: the live feed sends an empty string for most codes other than `1`. Clients should therefore ignore the wire string and map `status_code` through a static table:

| Code | Constant | Status text |
| --- | --- | --- |
| 1 | BCAST_OPEN_MESSAGE | Market open |
| 2 | BCAST_CLOSE_MESSAGE | Market closed |
| 3 | BCAST_PREOPEN_SHUTDOWN_MSG | Pre-open session ending |
| 4 | BCAST_NORMAL_MKT_PREOPEN_ENDED | Pre-open ended, normal market open |
| 5 | BCAST_AUCTION_STATUS_CHANGE | Auction status changed |
| 6 | BCAST_CLOSING_START | Closing session started |
| 7 | BCAST_CLOSING_END | Closing session ended |
| 8 | BCAST_CTS_CLOSE_FOR_CAS | Continuous trading closed, closing auction starting soon |
| 9 | BCAST_REVISED_PRICE_BAND_COMPLETED | Closing auction price band set |
| 10 | BCAST_CAS_START | Closing auction (CAS) started |
| 11 | BCAST_MARKET_ORDER_RESTRICTED | Market orders restricted |
| 12 | BCAST_CAS_END | Closing auction (CAS) ended |

### Subscription limit

The SFeed client allows at most 3000 input tokens subscribed at once, as a running total across all subscribe requests (touch line, option chain, index, depth and so on). A request that would exceed the limit is rejected and sends nothing. This is separate from the legacy 16-channel / 200-scrip limits noted under "Limits" above.
