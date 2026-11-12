# Delta Exchange API Documentation

Unofficial Markdown conversion of the official Delta Exchange API documentation.

> Source: https://docs.delta.exchange/#introduction

Delta Exchange is a crypto derivatives exchange. Its v2 API is a REST + WebSocket trading API
covering public market data (assets, indices, products, tickers, option chain, orderbook, public
trades, OHLC candles, settlement prices), order management (regular, bracket, batch and stop
orders), positions, trade history, wallets and sub-account transfers, market maker protection,
account preferences, a heartbeat-driven deadman switch, and real-time public/private WebSocket
channels.

## Contents

| # | Section | Source |
|---|---------|--------|
| 01 | [Introduction](01-introduction.md) | https://docs.delta.exchange/#introduction |
| 02 | [General Information](02-general-information.md) | https://docs.delta.exchange/#general-information |
| 03 | [Authentication](03-authentication.md) | https://docs.delta.exchange/#authentication |
| 04 | [Rate Limits](04-rate-limits.md) | https://docs.delta.exchange/#rate-limits |
| 05 | [System Status](05-system-status.md) | https://docs.delta.exchange/#system-status |
| 06 | [Types](06-types.md) | https://docs.delta.exchange/#types |
| 07 | [Response Formats](07-response-formats.md) | https://docs.delta.exchange/#response-formats |
| 08 | [MCP Server](08-mcp-server.md) | https://docs.delta.exchange/#mcp-server |
| 09 | [Rest API Overview](09-rest-api-overview.md) | https://docs.delta.exchange/#ApiSection |
| 10 | [Assets](10-assets.md) | https://docs.delta.exchange/#delta-exchange-api-v2-assets |
| 11 | [Indices](11-indices.md) | https://docs.delta.exchange/#delta-exchange-api-v2-indices |
| 12 | [Products](12-products.md) | https://docs.delta.exchange/#delta-exchange-api-v2-products |
| 13 | [Orders](13-orders.md) | https://docs.delta.exchange/#delta-exchange-api-v2-orders |
| 14 | [Positions](14-positions.md) | https://docs.delta.exchange/#delta-exchange-api-v2-positions |
| 15 | [Trade History](15-trade-history.md) | https://docs.delta.exchange/#delta-exchange-api-v2-tradehistory |
| 16 | [Orderbook](16-orderbook.md) | https://docs.delta.exchange/#delta-exchange-api-v2-orderbook |
| 17 | [Trades](17-trades.md) | https://docs.delta.exchange/#delta-exchange-api-v2-trades |
| 18 | [Wallet](18-wallet.md) | https://docs.delta.exchange/#delta-exchange-api-v2-wallet |
| 19 | [Stats](19-stats.md) | https://docs.delta.exchange/#delta-exchange-api-v2-stats |
| 20 | [MMP (Market Maker Protection)](20-mmp.md) | https://docs.delta.exchange/#delta-exchange-api-v2-mmp |
| 21 | [Account](21-account.md) | https://docs.delta.exchange/#delta-exchange-api-v2-account |
| 22 | [Heartbeat Management](22-heartbeat-management.md) | https://docs.delta.exchange/#delta-exchange-api-v2-heartbeat-management |
| 23 | [Settlement Prices](23-settlement-prices.md) | https://docs.delta.exchange/#delta-exchange-api-v2-settlement-prices |
| 24 | [Historical OHLC Candles / Sparklines](24-historical-ohlc-candles.md) | https://docs.delta.exchange/#delta-exchange-api-v2-historical-ohlc-candles-sparklines |
| 25 | [Schemas](25-schemas.md) | https://docs.delta.exchange/#schemas |
| 26 | [Deadman Switch](26-deadman-switch.md) | https://docs.delta.exchange/#deadman-switch |
| 27 | [Place Order Errors](27-place-order-errors.md) | https://docs.delta.exchange/#place-order-errors |
| 28 | [Errors](28-errors.md) | https://docs.delta.exchange/#errors |
| 29 | [Rest Clients](29-rest-clients.md) | https://docs.delta.exchange/#rest-clients |
| 30 | [Websocket Feed](30-websocket-feed.md) | https://docs.delta.exchange/#websocket-feed |
| 31 | [Websocket Public Channels](31-websocket-public-channels.md) | https://docs.delta.exchange/#public-channels |
| 32 | [Websocket Private Channels](32-websocket-private-channels.md) | https://docs.delta.exchange/#private-channels-2 |
| 33 | [Changelog](33-changelog.md) | https://docs.delta.exchange/#changelog |
| 34 | [Security](34-security.md) | https://docs.delta.exchange/#security |

## Base URLs

| Purpose | URL |
|---------|-----|
| REST API (production, India) | `https://api.india.delta.exchange` |
| REST API (testnet / demo account) | `https://cdn-ind.testnet.deltaex.org` |
| WebSocket private channels (production) | `wss://socket.india.delta.exchange` |
| WebSocket public channels (production) | `wss://public-socket.india.delta.exchange` |
| WebSocket private channels (testnet) | `wss://socket-ind.testnet.deltaex.org` |
| WebSocket public channels (testnet) | `wss://socket-ind-pub.testnet.deltaex.org` |
| MCP server docs (`uvx delta-exchange-mcp`, local stdio) | `https://mcp.delta.exchange/docs` |
| OpenAPI spec | `https://docs.delta.exchange/api/swagger_v2.json` |
| Documentation | `https://docs.delta.exchange/` |

All REST endpoints are under the `/v2/` prefix — the paths in the endpoint catalog below are
relative to it (e.g. `POST /orders` is `https://api.india.delta.exchange/v2/orders`).

## Endpoint Catalog

| Method | Path | Purpose | Section |
|--------|------|---------|---------|
| GET | `/assets` | List all assets | [Assets](10-assets.md) |
| GET | `/indices` | List indices | [Indices](11-indices.md) |
| GET | `/products` | List products (contracts) | [Products](12-products.md) |
| GET | `/products/{symbol}` | Product by symbol | [Products](12-products.md) |
| GET | `/tickers` | Tickers for all products | [Products](12-products.md) |
| GET | `/tickers/{symbol}` | Ticker for one product | [Products](12-products.md) |
| GET | `/tickers?contract_types=call_options,put_options&...` | Option chain | [Products](12-products.md) |
| POST | `/orders` | Place order | [Orders](13-orders.md) |
| PUT | `/orders` | Edit order | [Orders](13-orders.md) |
| DELETE | `/orders` | Cancel order | [Orders](13-orders.md) |
| GET | `/orders` | Get active orders | [Orders](13-orders.md) |
| POST | `/orders/bracket` | Place bracket order | [Orders](13-orders.md) |
| PUT | `/orders/bracket` | Edit bracket order | [Orders](13-orders.md) |
| DELETE | `/orders/all` | Cancel all open orders | [Orders](13-orders.md) |
| POST | `/orders/batch` | Create batch orders | [Orders](13-orders.md) |
| PUT | `/orders/batch` | Edit batch orders | [Orders](13-orders.md) |
| DELETE | `/orders/batch` | Delete batch orders | [Orders](13-orders.md) |
| GET | `/orders/{order_id}` | Get order by id | [Orders](13-orders.md) |
| GET | `/orders/client_order_id/{client_oid}` | Get order by client order id | [Orders](13-orders.md) |
| POST | `/products/{product_id}/orders/leverage` | Change order leverage | [Orders](13-orders.md) |
| GET | `/products/{product_id}/orders/leverage` | Get order leverage | [Orders](13-orders.md) |
| GET | `/positions/margined` | Get margined positions | [Positions](14-positions.md) |
| GET | `/positions` | Get position | [Positions](14-positions.md) |
| PUT | `/positions/auto_topup` | Auto topup | [Positions](14-positions.md) |
| POST | `/positions/change_margin` | Add / remove position margin | [Positions](14-positions.md) |
| POST | `/positions/close_all` | Close all positions | [Positions](14-positions.md) |
| GET | `/orders/history` | Order history (cancelled and closed) | [Trade History](15-trade-history.md) |
| GET | `/fills` | User fills by filters | [Trade History](15-trade-history.md) |
| GET | `/fills/history/download/csv` | Download fills history | [Trade History](15-trade-history.md) |
| GET | `/l2orderbook/{symbol}` | L2 orderbook | [Orderbook](16-orderbook.md) |
| GET | `/trades/{symbol}` | Public trades | [Trades](17-trades.md) |
| GET | `/wallet/balances` | Wallet balances | [Wallet](18-wallet.md) |
| GET | `/wallet/transactions` | Wallet transactions | [Wallet](18-wallet.md) |
| GET | `/wallet/transactions/download` | Download wallet transactions | [Wallet](18-wallet.md) |
| POST | `/wallets/sub_account_balance_transfer` | Request asset transfer | [Wallet](18-wallet.md) |
| GET | `/wallets/sub_accounts_transfer_history` | Sub-account transfer history | [Wallet](18-wallet.md) |
| GET | `/stats` | Volume stats | [Stats](19-stats.md) |
| PUT | `/users/update_mmp` | Update MMP config | [MMP](20-mmp.md) |
| PUT | `/users/reset_mmp` | Reset MMP | [MMP](20-mmp.md) |
| GET | `/users/trading_preferences` | Get trading preferences | [Account](21-account.md) |
| PUT | `/users/trading_preferences` | Update trading preferences | [Account](21-account.md) |
| GET | `/sub_accounts` | Get sub-accounts | [Account](21-account.md) |
| GET | `/profile` | Get user | [Account](21-account.md) |
| PUT | `/users/margin_mode` | Change margin mode | [Account](21-account.md) |
| GET | `/rate_limits/quota` | Current rate limit quota | [Account](21-account.md) |
| POST | `/heartbeat/create` | Create heartbeat | [Heartbeat Management](22-heartbeat-management.md) |
| POST | `/heartbeat` | Send heartbeat acknowledgment | [Heartbeat Management](22-heartbeat-management.md) |
| GET | `/heartbeat` | Get heartbeats | [Heartbeat Management](22-heartbeat-management.md) |
| GET | `/products/?states=expired` | Product settlement prices | [Settlement Prices](23-settlement-prices.md) |
| GET | `/history/candles` | Historical OHLC candles | [Historical OHLC](24-historical-ohlc-candles.md) |
| GET | `/history/sparklines` | Product history sparklines | [Historical OHLC](24-historical-ohlc-candles.md) |

## Quick Facts

- **Protocol:** REST with JSON request/response bodies; real-time data over WebSocket (JSON frames,
  no binary/protobuf).
- **Authentication:** HMAC-SHA256. The signature is computed over
  `method + timestamp + path + query_string + payload` and sent in the `api-key`, `timestamp`
  and `signature` headers. A `User-Agent` header is mandatory. See
  [Authentication](03-authentication.md).
- **Timestamp skew:** the `timestamp` header is a Unix timestamp in **seconds**, and requests
  are rejected with `SignatureExpired` if it is more than 5 seconds old on arrival.
- **Keys are environment-bound:** production keys work only against
  `api.india.delta.exchange`, demo-account keys only against `cdn-ind.testnet.deltaex.org`.
  `api.delta.exchange` is Delta Global and is a different deployment.
- **Instrument identity:** contracts are addressed by numeric `product_id` **or** `symbol`.
  Orders and orderbook APIs expect `product_id`. Symbol formats:
  `BTCUSD` (perpetual), `C-BTC-90000-310125` / `P-BTC-38100-230124` (options),
  `MARK:BTCUSD` (mark price), `.DEXBTUSD` (index).
- **Numbers:** big decimals (prices, amounts) are returned as strings to preserve precision;
  integers (`product_id`, contract size, impact size) are unquoted.
- **Timestamps** are ISO 8601 with microseconds unless otherwise specified — several payloads
  use Unix microseconds instead (e.g. an order's `created_at`).
- **Rate limits:** weighted quota of 10,000 units per fixed 5-minute window (per IP when
  unauthenticated, per user ID when authenticated); `429` with an `X-RATE-LIMIT-RESET` header on
  breach. A separate matching-engine limit of 500 operations/second/product applies on top.
- **Pagination** is cursor based (`after` / `before` / `page_size`) on products, orders, order
  history, fills and wallet transactions.
- **WebSocket limits:** 150 connections per IP per 5 minutes; a connection with no activity in
  the first 60 seconds is dropped.
- **Public vs private WebSocket endpoints are separate hosts.** Several channels
  (`mark_price`, `candlesticks`, `spot_price`, `funding_rate`, `system_status`, `ob_l1`, `ob_l2`,
  `ob_updates`, `ticker`, `trades`) have moved to the public endpoint; their legacy counterparts
  on the private endpoint are scheduled for removal on **31st July 2026** — see
  [Changelog](33-changelog.md).
- **Deadman switch:** heartbeat-based auto-cancel, configured via the Heartbeat Management
  endpoints. See [Deadman Switch](26-deadman-switch.md).
- **Data centers:** AWS Tokyo.

## Notes

- These docs describe the **Delta Exchange India** deployment (`api.india.delta.exchange`), which
  is what the official documentation site now publishes.
- The v1 API is deprecated and is not part of this conversion; the official docs link to it
  separately on GitHub.
- Code samples are reproduced as published, in Python, cURL (shell) and Ruby.
- API keys, signatures, order ids and account values in the samples are illustrative placeholders
  copied from the official docs — they are not live credentials or real data.
- One anchor in the upstream docs (`#trading-notitifications`) points at a target that does not
  exist; it is preserved as a link back to the live documentation site.
