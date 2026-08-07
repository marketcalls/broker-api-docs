# 5paisa Xstream API Documentation

Unofficial Markdown conversion of the official 5paisa Xstream (IIFL Securities) developer documentation.

> Source: https://xstream.5paisa.com/dev-docs

Xstream API is 5paisa's REST + WebSocket trading API. It covers OAuth login and access-token
generation, order placement / modification / cancellation, order and trade tracking, holdings,
net-wise positions and eDIS, funds and margin, snapshot and historical market data, and three
streaming feeds (market feed, option Greeks and 20-level market depth).

## Contents

| # | Section | Source |
|---|---------|--------|
| 01 | [Introduction](01-introduction.md) | https://xstream.5paisa.com/dev-docs |
| 02 | [Integration Flow](02-integration-flow.md) | https://xstream.5paisa.com/dev-docs/docFundamentals/integration-flow |
| 03 | [Scrip Master](03-scrip-master.md) | https://xstream.5paisa.com/dev-docs/docFundamentals/scrip-master |
| 04 | [Publisher JS](04-publisher-js.md) | https://xstream.5paisa.com/dev-docs/docFundamentals/publisher-js |
| 05 | [API Changelog](05-api-changelog.md) | https://xstream.5paisa.com/dev-docs/docFundamentals/api-changelog |
| 06 | [User Authentication System](06-user-authentication.md) | https://xstream.5paisa.com/dev-docs/user-authentication-system/oauth-login |
| 07 | [Order Management System](07-order-management.md) | https://xstream.5paisa.com/dev-docs/order-management-system/place-order |
| 08 | [Order Tracking System](08-order-tracking.md) | https://xstream.5paisa.com/dev-docs/order-tracking-system/order-book |
| 09 | [Market Data System - REST APIs](09-market-data-rest.md) | https://xstream.5paisa.com/dev-docs/market-data-system/market-feed |
| 10 | [Market Data System - WebSocket](10-market-data-websocket.md) | https://xstream.5paisa.com/dev-docs/market-data-system/web-socket |
| 11 | [Portfolio Management System](11-portfolio-management.md) | https://xstream.5paisa.com/dev-docs/portfolio-management-system/holdings |
| 12 | [Funds Management System](12-funds-management.md) | https://xstream.5paisa.com/dev-docs/funds-management-system/margin |

Each multi-page section carries a `> Source:` line per page, so every block of content can be traced
back to its original URL.

## Base URLs

| Purpose | URL |
|---------|-----|
| REST API (production) | `https://Openapi.5paisa.com` |
| Historical candles (V2) | `https://openapi.5paisa.com/V2` |
| OAuth login / eDIS authorisation | `https://dev-openapi.5paisa.com` |
| Market feed + order/trade confirmation WebSocket | `wss://openfeed.5paisa.com/feeds/api/chat` (also `aopenfeed`/`bopenfeed` — see below) |
| Option Greeks WebSocket | `wss://gateway.5paisa.com/openapi/greeks` |
| 20-level market depth WebSocket | `wss://gateway.5paisa.com/openapi/20depth` |
| Scrip master CSV | `https://Openapi.5paisa.com/VendorsAPI/Service1.svc/ScripMaster/segment/{segment}` |
| Developer dashboard (API keys) | `https://xstream.5paisa.com/dashboard` |
| Documentation | `https://xstream.5paisa.com/dev-docs` |

Most REST endpoints live under `/VendorsAPI/Service1.svc/`.

## Endpoint Catalog

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/WebVendorLogin/VLogin/Index` | OAuth login redirect (returns `RequestToken`) |
| POST | `/VendorsAPI/Service1.svc/GetAccessToken` | Exchange `RequestToken` for an access token |
| POST | `/VendorsAPI/Service1.svc/V1/PlaceOrderRequest` | Place order |
| POST | `/VendorsAPI/Service1.svc/V1/ModifyOrderRequest` | Modify order |
| POST | `/VendorsAPI/Service1.svc/V1/CancelOrderRequest` | Cancel order |
| POST | `/VendorsAPI/Service1.svc/V3/OrderBook` | Order book |
| POST | `/VendorsAPI/Service1.svc/V3/OrderStatus` | Order status |
| POST | `/VendorsAPI/Service1.svc/V1/TradeBook` | Trade book |
| POST | `/VendorsAPI/Service1.svc/V3/Holding` | Holdings |
| POST | `/VendorsAPI/Service1.svc/V2/NetPositionNetWise` | Net-wise positions |
| POST | `/WebVendorLogin/EDISAuthorization/Authorization` | eDIS holding authorisation |
| POST | `/VendorsAPI/Service1.svc/V4/Margin` | Funds / margin |
| POST | `/VendorsAPI/Service1.svc/MultiOrderMargin` | Multi-order margin |
| POST | `/VendorsAPI/Service1.svc/V1/MarketFeed` | Market feed (LTP / OHLC snapshot) |
| POST | `/VendorsAPI/Service1.svc/MarketSnapshot` | Market snapshot (quotes, OI, 52-week high/low) |
| POST | `/VendorsAPI/Service1.svc/V2/MarketDepth` | Market depth snapshot |
| GET | `/V2/historical/{Exch}/{ExchType}/{ScripCode}/{Interval}` | Historical candles |
| GET | `/VendorsAPI/Service1.svc/ScripMaster/segment/{segment}` | Scrip master CSV |
| WS | `/feeds/api/chat?Value1={access_token}\|{clientcode}` | Market feed + order/trade confirmations |
| WS | `/openapi/greeks?access_token={access_token}` | Option Greeks stream |
| WS | `/openapi/20depth?access_token={access_token}` | 20-level depth stream |

## Quick Facts

- **Protocol:** REST with JSON bodies. Every request is `{"head": {...}, "body": {...}}` and every
  response comes back as `{"head": {...}, "body": {...}}`.
- **Authentication:** `Authorization: bearer <access_token>` header plus your AppKey in `head.key`.
  The access token is valid for the day and expires at 11:59 PM.
- **Login:** the OAuth web redirect returns a `RequestToken` (valid 60 minutes) which is exchanged
  for an access token together with `UserId` and `EncryKey`.
- **Exchanges:** `N` = NSE, `B` = BSE, `M` = MCX (and `n` = NCDEX for historical candles).
  **Exchange types:** `C` = Cash, `D` = Derivatives, `U` = Currency.
- **Instruments** are addressed either by `ScripCode` (integer from the scrip master) or by
  `ScripData` (symbol string, e.g. `RELIANCE_EQ`, `BANKNIFTY 24 Nov 2022 CE 41600.00_20221124_CE_41600`).
- **Order sides:** `B` = Buy, `S` = Sell. Intraday vs delivery is the boolean `IsIntraday`;
  after-market orders set `AHPlaced: "Y"`.
- **Algo ID:** SEBI algo-trading rules require a 5paisa-issued `AlgoID` on algorithmic orders;
  non-algo users pass `0` or `null`.
- **Timestamps** in responses use the .NET format `/Date(1658255400000+0530)/`.
- **WebSocket methods:** `MarketFeedV3`, `MarketDepthService`, `GetScripInfoForFuture` (open
  interest) and `OrderTradeConfirmations` — each subscribed/unsubscribed over the single feed
  connection. Option Greeks and 20-level depth are separate sockets on `gateway.5paisa.com`.
- **Order updates are host-sharded.** Decode the access-token JWT and read `RedirectServer`:
  `C` → `wss://openfeed.5paisa.com/feeds`, `A` → `wss://aopenfeed.5paisa.com/feeds`,
  `B` → `wss://bopenfeed.5paisa.com/feeds`. Connecting to the wrong host silently drops order
  updates; market data works on any of them.
- **Official SDKs** live at [github.com/OpenApi-5p](https://github.com/OpenApi-5p):
  [Python](https://github.com/OpenApi-5p/py5paisa), [C#](https://github.com/OpenApi-5p/5pdotnet_new),
  [Node.js](https://github.com/OpenApi-5p/5paisa-js), [Java](https://github.com/OpenApi-5p/5paisa-java).

## Notes

- The docs portal tags every API page as `POST`; historical candles and the scrip master are in fact
  `GET` requests, as their own cURL samples show.
- Hosts are inconsistent in the official docs — OAuth login and eDIS point at `dev-openapi.5paisa.com`,
  some samples still reference the legacy `dataservice.iifl.in/openapi/prod` host, and the market feed
  connection URL appears as both `https://` and `wss://`. The conversion preserves them verbatim.
- The sidebar links a "Customer Login" page (`/user-authentication-system/login`) that returns 404 on
  the live site; OAuth is the only documented login flow, so there is no page for it here.
- A couple of sample JSON failure responses are truncated in the source CMS (they end mid-object);
  those are reproduced as-is.
- Example tokens, client codes, order IDs and account values are the illustrative values from the
  official docs — they are not live credentials or real data.

## Disclaimer

This is an unofficial Markdown conversion maintained for personal/educational reference. The official
5paisa documentation at https://xstream.5paisa.com/dev-docs is the authoritative source — always
verify against it. Trademarks and content belong to 5paisa / IIFL Securities.
