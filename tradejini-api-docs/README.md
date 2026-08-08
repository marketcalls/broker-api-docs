# Tradejini (CubePlus API v2) Documentation

> **Unofficial Markdown conversion** of the Tradejini developer documentation, sourced from the official developer portal:
> <https://developer.tradejini.com/docs>

The Tradejini REST API (CubePlus) is a set of HTTP APIs covering order management, advanced order types (BO/CO/GTT/OCO), account and funds information, scrip master data, historical chart data, and real-time WebSocket streaming via official SDKs.

## Base URLs

| Purpose | Base URL |
| --- | --- |
| REST API | `https://api.tradejini.com/v2` |
| Developer portal / Apps | <https://developer.tradejini.com/developer-portal> |
| CubePlus web app (2FA / TOTP setup) | <https://cubeplus.tradejini.com/> |

Endpoint paths in these documents are relative to the REST base URL — e.g. `GET /api/oms/orders` means `GET https://api.tradejini.com/v2/api/oms/orders`.

## Table of Contents

| # | Document | Description |
| --- | --- | --- |
| 01 | [Introduction](01-introduction.md) | Overview, base URL, getting started, documentation map |
| 02 | [API Basics](02-api-basics.md) | Auth header format, request/response envelope, symbol IDs, order field codes, static IP requirement |
| 03 | [App Creation](03-app-creation.md) | Registering Individual and User Based apps to obtain API credentials |
| 04 | [Authorization Flow](04-authorization-flow.md) | Step-by-step auth walkthroughs for each app type |
| 05 | [Authorization APIs](05-authorization.md) | Individual Token, Authorize, Access Token, Order Connect |
| 06 | [Account](06-account.md) | User details and logout |
| 07 | [Symbol Details](07-symbol-details.md) | Scrip master groups and scrip master data (`symId` lookup) |
| 08 | [Funds](08-funds.md) | Limits — available margin and cash balances |
| 09 | [Orders](09-orders.md) | Place/modify/cancel orders, order book, history, trades, positions, holdings, margin |
| 10 | [Advance Orders](10-advance-orders.md) | Bracket, Cover, GTT, and OCO order types |
| 11 | [Chart Data](11-chart-data.md) | Historical interval (OHLCV) candle data |
| 12 | [WebSocket SDKs](12-websocket-sdks.md) | Binary streaming SDKs, subscriptions, market data fields, order events |
| 13 | [Rate Limits](13-rate-limits.md) | REST, WebSocket, and session limits |
| 14 | [Common Errors](14-common-errors.md) | HTTP status codes, causes, and resolutions |
| 15 | [Market Hours](15-market-hours.md) | Session timings by exchange and segment |
| 16 | [FAQ](16-faq.md) | Frequently asked questions |

## Notes

- Authenticate every protected request with `Authorization: Bearer <api_key>:<access_token>`.
  The Individual Token endpoint is the exception — it takes `Authorization: Bearer <api_key>` only.
- Access tokens are valid for **24 hours**; a fresh login is required each trading day.
- `GET`/`DELETE` requests take query parameters. `POST`/`PUT` requests use
  `Content-Type: application/x-www-form-urlencoded` (a few endpoints use `application/json`).
- All JSON responses use the envelope `{"s": "ok"|"error"|"no-data", "d": ..., "msg": ...}`.
- Instruments are identified by a `symId` string (e.g. `EQT_RELIANCE_EQ_NSE`) — look them up with the
  [Scrip Master Data](07-symbol-details.md) endpoint.
- **Individual Apps require a whitelisted static IP** — requests from other IPs return `401 Unauthorized`.
- Market data streaming is binary and is consumed through the official WebSocket SDKs, not raw JSON.
