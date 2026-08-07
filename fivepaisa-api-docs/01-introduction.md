# Introduction

> Source: https://xstream.5paisa.com/dev-docs

Xstream API is 5paisa's (IIFL Securities') REST + WebSocket trading API. It covers OAuth login and
access-token generation, order placement / modification / cancellation, order and trade tracking,
holdings and positions, funds and margin, snapshot and historical market data, and three separate
streaming feeds (market feed, option Greeks, 20-level depth).

## Overview

Our platform offers a flexible and extensible framework designed to help you build and automate
innovative digital journeys. It combines powerful APIs, real-time communication, and modular plugins
to support a wide range of use cases — from customer engagement to backend process automation.

Features:

- **REST APIs:** A rich set of endpoints to access and control core functionalities. Easily
  integrate with external systems and manage resources programmatically.
- **WebSocket Support:** Real-time, bi-directional communication for event-driven workflows, live
  updates, and interactive user experiences.
- **Scalable & Secure:** Built for performance and reliability with enterprise-grade security
  standards and support for scalable deployments.

## Documentation Map

| Group | Pages |
|---|---|
| Doc Fundamentals | [Integration Flow](02-integration-flow.md), [Scrip Master](03-scrip-master.md), [Publisher JS](04-publisher-js.md), [API Changelog](05-api-changelog.md) |
| User Authentication | [OAuth Login, Access Token](06-user-authentication.md) |
| Order Management | [Place / Modify / Cancel Order](07-order-management.md) |
| Order Tracking | [Order Book, Order Status, Trade Book, Trade Confirmation WebSocket](08-order-tracking.md) |
| Market Data (REST) | [Market Feed, Market Snapshot, Market Depth, Historical Candles](09-market-data-rest.md) |
| Market Data (WebSocket) | [Market Feed socket, Option Greeks, 20-Market Depth](10-market-data-websocket.md) |
| Portfolio Management | [Holdings, Net-wise Position, EDIS](11-portfolio-management.md) |
| Funds Management | [Margin, Multi Order Margin](12-funds-management.md) |

## Hosts

| Purpose | Host |
|---|---|
| REST API (production) | `https://Openapi.5paisa.com` |
| Historical candles (V2) | `https://openapi.5paisa.com/V2` |
| OAuth login / EDIS authorisation | `https://dev-openapi.5paisa.com` |
| Market feed + order/trade confirmation WebSocket | `wss://openfeed.5paisa.com/feeds/api/chat` |
| Option Greeks WebSocket | `wss://gateway.5paisa.com/openapi/greeks` |
| 20-level market depth WebSocket | `wss://gateway.5paisa.com/openapi/20depth` |
| Scrip master (CSV) | `https://Openapi.5paisa.com/VendorsAPI/Service1.svc/ScripMaster/segment/{segment}` |
| Publisher JS plugin | `https://tradechart.5paisa.com/plugin/plugin.js` |
| Developer dashboard (API keys) | `https://xstream.5paisa.com/dashboard` |

Most REST endpoints live under `/VendorsAPI/Service1.svc/`. A few pages still show the legacy
`https://dataservice.iifl.in/openapi/prod/...` host in code samples; the conversion preserves them
verbatim.

## Endpoint Catalog

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/WebVendorLogin/VLogin/Index` | OAuth login redirect (returns `RequestToken`) |
| POST | `/VendorsAPI/Service1.svc/GetAccessToken` | Exchange `RequestToken` for an access token |
| POST | `/VendorsAPI/Service1.svc/V1/PlaceOrderRequest` | Place order |
| POST | `/VendorsAPI/Service1.svc/V1/ModifyOrderRequest` | Modify order |
| POST | `/VendorsAPI/Service1.svc/V1/CancelOrderRequest` | Cancel order |
| POST | `/VendorsAPI/Service1.svc/V3/OrderBook` | Order book (a V4 variant appears in samples) |
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
| GET | `/V2/historical/{Exch}/{ExchType}/{ScripCode}/{interval}` | Historical candles |
| GET | `/VendorsAPI/Service1.svc/ScripMaster/segment/{segment}` | Scrip master CSV |
| WS | `wss://openfeed.5paisa.com/feeds/api/chat?Value1={access_token}\|{clientcode}` | Market feed + order/trade confirmations |
| WS | `wss://gateway.5paisa.com/openapi/greeks?access_token={access_token}` | Option Greeks stream |
| WS | `wss://gateway.5paisa.com/openapi/20depth?access_token={access_token}` | 20-level depth stream |

The CMS tags every API page as `POST`; historical candles and the scrip master are actually `GET`
requests, as their own cURL samples show.

## Quick Facts

- **Protocol:** REST with JSON request/response bodies; every request body is `{"head": {...}, "body": {...}}`
  and every response is `{"head": {...}, "body": {...}}`.
- **Authentication:** `Authorization: bearer <access_token>` header, plus your AppKey in the request
  `head.key`. The access token is valid for the day and expires at 11:59 PM.
- **Login:** OAuth web redirect gives a `RequestToken` (valid 60 min), which is exchanged for an
  access token together with `UserId` and `EncryKey`.
- **Exchanges:** `N` = NSE, `B` = BSE, `M` = MCX. **Exchange types:** `C` = Cash, `D` = Derivatives,
  `U` = Currency.
- **Instruments** are identified either by `ScripCode` (integer, from the scrip master) or by
  `ScripData` (symbol string, e.g. `RELIANCE_EQ`, `BANKNIFTY 24 Nov 2022 CE 41600.00_20221124_CE_41600`).
- **Order sides:** `B` = Buy, `S` = Sell. Intraday vs delivery is a boolean (`IsIntraday`), and
  after-market orders use `AHPlaced: "Y"`.
- **Algo ID:** SEBI algo-trading rules require a 5paisa-issued `AlgoID` on algorithmic orders;
  non-algo users pass `0` or `null`.
- **Timestamps** in responses use the .NET format `/Date(1658255400000+0530)/`.
- **Official SDKs:** [Python](https://github.com/OpenApi-5p/py5paisa),
  [C#](https://github.com/OpenApi-5p/5pdotnet_new), [Node.js](https://github.com/OpenApi-5p/5paisa-js),
  [Java](https://github.com/OpenApi-5p/5paisa-java) — all under
  [github.com/OpenApi-5p](https://github.com/OpenApi-5p).

## Support

- Developer community: https://help.indiainfoline.com/portal/en/community/iifl-help/algorithmic-trading
- Support: cs@iifl.com
- Changelog: [API Changelog](05-api-changelog.md)
