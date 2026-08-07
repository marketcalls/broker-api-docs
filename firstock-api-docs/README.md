# Firstock Developer API Documentation

Unofficial Markdown conversion of the official Firstock Developer API documentation.

> Source: https://firstock.in/api/docs/

Firstock's Developer API is a REST + WebSocket trading API. It covers login/session
generation, regular and after-market orders, basket orders, order/trade/position books,
holdings and limits, product conversion, brokerage and margin calculators, quotes and
multi-quotes, option chains (with and without Greeks), expiry and index lists, intraday and
EOD candles, and JSON-based streaming feeds for market data, order updates and position
updates.

## Contents

### Overview

| # | Section | Source |
|---|---------|--------|
| 01 | [Introduction](01-introduction.md) | https://firstock.in/api/docs/overview/ |
| 02 | [Versioning](02-versioning.md) | https://firstock.in/api/docs/versioning/ |
| 03 | [Key Generation](03-key-generation.md) | https://firstock.in/api/docs/key-generation/ |
| 04 | [Change Logs](04-change-logs.md) | https://firstock.in/api/docs/change-logs/ |

### Downloader API

| # | Section | Source |
|---|---------|--------|
| 05 | [Downloaders (symbol files)](05-downloaders.md) | https://firstock.in/api/docs/downloaders/ |
| 06 | [Library & SDK](06-library-and-sdk.md) | https://firstock.in/api/docs/library-sdk/ |
| 07 | [Data Types](07-data-types.md) | https://firstock.in/api/docs/data-types/ |
| 08 | [Request & Responses](08-request-and-responses.md) | https://firstock.in/api/docs/request-responses/ |
| 09 | [Exceptions & Errors](09-exceptions-and-errors.md) | https://firstock.in/api/docs/exception-errors/ |

### Login & Profile

| # | Section | Source |
|---|---------|--------|
| 10 | [Login](10-login.md) | https://firstock.in/api/docs/login/ |
| 11 | [Logout](11-logout.md) | https://firstock.in/api/docs/logout/ |
| 12 | [User Details](12-user-details.md) | https://firstock.in/api/docs/user-details/ |

### Orders & Reports

| # | Section | Source |
|---|---------|--------|
| 13 | [Place Order](13-place-order.md) | https://firstock.in/api/docs/place-order/ |
| 14 | [Order Margin](14-order-margin.md) | https://firstock.in/api/docs/order-margin/ |
| 15 | [Order Book](15-order-book.md) | https://firstock.in/api/docs/order-book/ |
| 16 | [Cancel Order](16-cancel-order.md) | https://firstock.in/api/docs/cancel-order/ |
| 17 | [Modify Order](17-modify-order.md) | https://firstock.in/api/docs/modify-order/ |
| 18 | [Single Order History](18-single-order-history.md) | https://firstock.in/api/docs/single-order-history/ |
| 19 | [Trade Book](19-trade-book.md) | https://firstock.in/api/docs/trade-book/ |
| 20 | [Position Book](20-position-book.md) | https://firstock.in/api/docs/position-book/ |
| 21 | [Product Conversion](21-product-conversion.md) | https://firstock.in/api/docs/product-conversion/ |
| 22 | [Holdings](22-holdings.md) | https://firstock.in/api/docs/holdings/ |
| 23 | [Limit](23-limit.md) | https://firstock.in/api/docs/limits/ |
| 24 | [Basket Margin](24-basket-margin.md) | https://firstock.in/api/docs/basket-margin-2/ |
| 25 | [Holding Details](25-holding-details.md) | https://firstock.in/api/docs/holding-details/ |
| 26 | [Place After Market Order (AMO)](26-place-after-market-order.md) | https://firstock.in/api/docs/place-after-market-order-amo/ |
| 27 | [Modify After Market Order (AMO)](27-modify-after-market-order.md) | https://firstock.in/api/docs/modify-after-market-order-amo/ |
| 28 | [Basket Orders](28-basket-orders.md) | https://firstock.in/api/docs/basket-orders/ |
| 29 | [Combined Holdings](29-combined-holdings.md) | https://firstock.in/api/docs/combined-holdings/ |

### Market Info

| # | Section | Source |
|---|---------|--------|
| 30 | [Brokerage Calculator](30-brokerage-calculator.md) | https://firstock.in/api/docs/brokerage-calculator/ |
| 31 | [Get Security Info](31-get-security-info.md) | https://firstock.in/api/docs/get-security-info/ |
| 32 | [Get Quote](32-get-quote.md) | https://firstock.in/api/docs/get-quote/ |
| 33 | [Get Quote LTP](33-get-quote-ltp.md) | https://firstock.in/api/docs/get-quote-ltp/ |
| 34 | [Get Multi Quote](34-get-multi-quote.md) | https://firstock.in/api/docs/get-multi-quote/ |
| 35 | [Get Multi Quote LTP](35-get-multi-quote-ltp.md) | https://firstock.in/api/docs/get-multi-quote-ltp/ |
| 36 | [Index List](36-index-list.md) | https://firstock.in/api/docs/index-list/ |
| 37 | [Get Expiry](37-get-expiry.md) | https://firstock.in/api/docs/get-expiry/ |
| 38 | [Option Chain](38-option-chain.md) | https://firstock.in/api/docs/option-chain/ |
| 39 | [Search Scrips](39-search-scrips.md) | https://firstock.in/api/docs/search-scrips/ |
| 40 | [Time Price Regular Interval](40-time-price-regular-interval.md) | https://firstock.in/api/docs/time-price-regular-interval/ |
| 41 | [Time Price Day Interval](41-time-price-day-interval.md) | https://firstock.in/api/docs/time-price-day-interval/ |
| 42 | [Option Chain with Greeks](42-option-chain-with-greeks.md) | https://firstock.in/api/docs/option-chain-with-greeks/ |

### WebSocket

| # | Section | Source |
|---|---------|--------|
| 43 | [Getting Started V2](43-websocket-getting-started-v2.md) | https://firstock.in/api/docs/getting-started-v2/ |
| 44 | [Subscribe Feed V2](44-websocket-subscribe-feed-v2.md) | https://firstock.in/api/docs/subscribe-feed-v2/ |
| 45 | [Order Update Feed V2](45-websocket-order-update-feed-v2.md) | https://firstock.in/api/docs/order-update-feed-v/ |
| 46 | [Position Update Feed V2](46-websocket-position-update-feed-v2.md) | https://firstock.in/api/docs/position-update-feed-v2/ |
| 47 | [WebSocket Tester V2](47-websocket-tester-v2.md) | https://firstock.in/api/docs/websocket-tester-v2/ |
| 48 | [Getting Started (Deprecated)](48-websocket-getting-started-deprecated.md) | https://firstock.in/api/docs/getting-started-3/ |
| 49 | [Subscribe Feed (Deprecated)](49-websocket-subscribe-feed-deprecated.md) | https://firstock.in/api/docs/subscribe-feed-3/ |
| 50 | [Order Update Feed (Deprecated)](50-websocket-order-update-feed-deprecated.md) | https://firstock.in/api/docs/order-update-feed/ |
| 51 | [Position Update Feed (Deprecated)](51-websocket-position-update-feed-deprecated.md) | https://firstock.in/api/docs/position-update-feed/ |

## Base URLs

| Purpose | URL |
|---------|-----|
| REST API | `https://api.firstock.in/V1/` |
| WebSocket (V2, current) | `wss://socket.firstock.in/V2/ws` |
| WebSocket (deprecated) | `wss://socket.firstock.in/ws` |
| API key / vendor code portal | `https://firstock.in/api/` |
| Documentation | `https://firstock.in/api/docs/` |

## Endpoint Catalog

Every REST endpoint is a **POST** with a JSON body; there are no path or query parameters.
`userId` and `jKey` travel in the body, not in headers.

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/V1/login` | Login, returns `susertoken` (used as `jKey`) |
| POST | `/V1/logout` | Invalidate the session |
| POST | `/V1/userDetails` | User profile, enabled exchanges and products |
| POST | `/V1/placeOrder` | Place a regular order |
| POST | `/V1/modifyOrder` | Modify an open order |
| POST | `/V1/cancelOrder` | Cancel an open order |
| POST | `/V1/placeAfterMarketOrder` | Place an AMO |
| POST | `/V1/modifyAfterMarketOrder` | Modify an AMO |
| POST | `/V1/basketOrder` | Place multiple order legs in one request |
| POST | `/V1/orderBook` | Order book |
| POST | `/V1/singleOrderHistory` | Order history for one order number |
| POST | `/V1/tradeBook` | Trade book |
| POST | `/V1/positionBook` | Net positions |
| POST | `/V1/productConversion` | Convert a position's product type |
| POST | `/V1/holdings` | Holdings |
| POST | `/V1/holdingsDetails` | Holding details |
| POST | `/V1/combinedHoldings` | Combined equity + mutual fund holdings |
| POST | `/V1/limit` | Funds / limits |
| POST | `/V1/orderMargin` | Margin required for a single order |
| POST | `/V1/basketMargin` | Margin required for a basket of orders |
| POST | `/V1/brokerageCalculator` | Brokerage and charges estimate |
| POST | `/V1/securityInfo` | Instrument / contract details |
| POST | `/V1/searchScrips` | Symbol search |
| POST | `/V1/indexList` | Index names and tokens |
| POST | `/V1/getExpiry` | Expiry dates for a derivative underlying |
| POST | `/V1/optionChain` | Option chain |
| POST | `/V1/optionChainGreeks` | Option chain with Greeks |
| POST | `/V1/getQuote` | Full quote with market depth |
| POST | `/V1/getQuote/ltp` | LTP-only quote |
| POST | `/V1/getMultiQuotes` | Full quotes for multiple instruments |
| POST | `/V1/getMultiQuotes/ltp` | LTP-only quotes for multiple instruments |
| POST | `/V1/timePriceSeries` | Historical candles (intraday `1mi`/`2mi`/… and daily `1d`) |
| GET | `/V1/symbols/NSE` | NSE equity symbol file |
| GET | `/V1/symbols/BSE` | BSE equity symbol file |
| GET | `/V1/symbols/NFO` | NSE F&O symbol file |
| GET | `/V1/symbols/BFO` | BSE F&O symbol file |
| GET | `/V1/symbols/Indices` | Index derivatives symbol file |

## Quick Facts

- **Protocol:** REST with JSON request/response bodies (all endpoints are POST); streaming
  over WebSocket with plain JSON messages — no binary or Protobuf framing.
- **Authentication:** `POST /V1/login` with `userId`, SHA-256 hashed `password`, `TOTP`,
  `vendorCode` and `apiKey`. The returned `susertoken` is passed as `jKey` in the body of
  every subsequent request. Only header required is `Content-Type: application/json`.
- **API keys** are generated from the portal at `https://firstock.in/api/` and **expire after
  365 days**. Up to **two IP addresses** may be whitelisted per account (SEBI requirement,
  mandatory from 1 April 2026).
- **Exchanges:** NSE, BSE, NFO, BFO.
- **Products:** `C` (Cash & Carry / delivery), `I` (Intraday), `M` (documented in
  [07-data-types.md](07-data-types.md) only as "Market", context-dependent).
  **Price types:** `MKT`, `LMT`, `SL-LMT`, `SL-MKT`. **Retention:** `DAY`, `IOC`.
  **Transaction type:** `B` (Buy) / `S` (Sell).
- **Instruments** are identified by `tradingSymbol` (e.g. `IDEA-EQ`, `NIFTY06MAR25C22500`)
  in REST calls, and by `EXCHANGE:token` (e.g. `NSE:26000`, `BSE:500470`) in the WebSocket
  feed. Symbols with special characters must be URL-encoded (`L&TFH-EQ` → `L%26TFH-EQ`).
- **Market protection** (`mkt_protection`) is mandatory and must be > 0 for `MKT` and
  `SL-MKT` orders — the order is converted to `LMT`/`SL-LMT` at a price derived from the
  best bid/ask adjusted by that percentage.
- **Order slicing:** orders above the exchange freeze quantity are auto-sliced into up to
  10 sub-orders placed in parallel; the response then returns an array of order numbers.
- **Rate limits:** 3 req/sec for quotes, 3 req/sec for historical candles, 10 req/sec for
  order placement and all other endpoints (see [09-exceptions-and-errors.md](09-exceptions-and-errors.md);
  note the page also carries a conflicting remark that quote limits dropped to 1 req/sec).
- **WebSocket:** connect with `userId`, `jKey` and `source=developer-api` as query
  parameters. The server sends `Ping` frames and expects a `Pong` within 10 seconds or it
  drops the connection. Three feeds are available: market data (subscribe), order updates,
  and position updates.
- **Official SDKs:** Python (`firstock`), Node.js (`firstock`) and Go
  (`github.com/the-firstock/firstock-developer-sdk-golang`); every endpoint page carries
  curl, Python, Node.js and Go samples.

## Notes

- Firstock ships **two WebSocket generations**. V2 (`/V2/ws`) is current and returns a
  unified JSON object per instrument; the deprecated V1 (`/ws`) pages are kept here
  (files 48–51) because the older format is still described in the official docs.
- Both "Time Price Regular Interval" and "Time Price Day Interval" hit the same
  `/V1/timePriceSeries` endpoint — they differ only in the `interval` field
  (`1mi`, `2mi`, `5mi`, … vs `1d`).
- The AMO pages document `/V1/placeAfterMarketOrder` and `/V1/modifyAfterMarketOrder`, but
  some curl samples on those pages still use the older `/V1/placeAMO` and `/V1/modifyAMO`
  paths; both are preserved verbatim.
- [47-websocket-tester-v2.md](47-websocket-tester-v2.md) is an interactive browser tool
  rather than reference content, so the converted page is almost empty by nature.
- Symbol master files are downloadable CSV-style endpoints under `/V1/symbols/…`; only the
  links are reproduced, not the file contents.
- Example tokens, session keys, order numbers, client IDs and account values in the samples
  are illustrative values copied from the official docs — they are not live credentials or
  real data.
