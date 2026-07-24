# Flattrade Pi API Documentation

> **Unofficial Markdown conversion** of the Flattrade **Pi** trading API documentation, sourced from the official documentation portal:
> <https://pi.flattrade.in/docs>

Pi is a collection of REST APIs that provides the required capabilities to build a modern stock market investment and trading platform — execute orders in real time (equities, commodities, currency), stream live market data over WebSockets, and more. Pi is part of the same Noren API family as Aliceblue (ANT) and Definedge (INTEGRATE), so the request/response shape (`jData`/`jKey`, `tsym`, `prd`, `trantype`, ...) will look familiar if you've integrated with those.

## Base URLs

| Purpose | Base URL |
| --- | --- |
| REST API | `https://piconnect.flattrade.in/PiConnectAPI` |
| WebSocket (market data / order / position updates) | `wss://piconnect.flattrade.in/PiConnectWSAPI/` |
| Login — Authorize | `https://auth.flattrade.in/?app_key=APIKEY` |
| Login — Token Exchange | `https://authapi.flattrade.in/trade/apitoken` |

> The REST and WebSocket base URLs changed recently (`PiConnectTP` → `PiConnectAPI`, `PiConnectWSTp` → `PiConnectWSAPI`). See [Change Log](15-changelog.md).

## Table of Contents

| # | Document | Description |
| --- | --- | --- |
| 01 | [Introduction](01-introduction.md) | API overview, app registration, Postman collection, MCP server |
| 02 | [Authentication](02-authentication.md) | Browser login flow and access token (`jKey`) generation |
| 03 | [Orders and Trades](03-orders.md) | Place/modify/cancel/exit orders, margins, order/trade/position books, product conversion |
| 04 | [GTT & OCO Orders](04-gtt-oco-orders.md) | Good-Till-Triggered and One-Cancels-Other conditional orders |
| 05 | [Holdings and Limits](05-holdings-and-limits.md) | Portfolio holdings and account fund limits |
| 06 | [Market Info](06-market-info.md) | Index list, top lists, charts (intraday & EOD), option chain, option greeks, span calculator |
| 07 | [Alerts](07-alerts.md) | Price alert set/modify/cancel |
| 08 | [Funds](08-funds.md) | Payout requests, payin/payout reports |
| 09 | [WebSocket API](09-websocket.md) | Touchline, market depth, order update, and position update streaming |
| 10 | [User Details](10-user-details.md) | Enabled exchanges, products, and price types for the logged-in user |
| 11 | [Scrips](11-scrips.md) | Symbol search and quotes |
| 12 | [Postback / Webhook](12-postback-webhook.md) | Real-time order update webhook payload |
| 13 | [Scrip Master](13-scrip-master.md) | Daily contract master file downloads per exchange segment |
| 14 | [Rate Limits](14-rate-limits.md) | Order API and general API rate limits |
| 15 | [Change Log](15-changelog.md) | Breaking API/WebSocket endpoint and payload changes |

## Notes

- All REST endpoints are `POST` requests with a form-encoded body of `jData` (a JSON payload) and `jKey` (the access token from [Authentication](02-authentication.md)).
- Field names and JSON keys are case-sensitive.
- Fields marked `*` in the parameter tables are mandatory.
