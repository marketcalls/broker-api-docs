# HDFC Securities InvestRight Open API Documentation

Unofficial Markdown conversion of the official HDFC Securities InvestRight Open API developer
documentation.

> Source: https://developer.hdfcsec.com/ir-docs/docs/intro

InvestRight Open API is HDFC Securities' REST + WebSocket trading API. It covers the browser and
programmatic login flows, regular order placement/modification/cancellation, order book and trade
book, positions, holdings, funds and margins, LTP snapshots, a Protobuf-based streaming market
data feed, and a downloadable security master.

> **Not the same product as HDFC Sky.** HDFC Securities publishes two separate Open APIs on two
> separate hosts. This folder documents **InvestRight** (`developer.hdfcsec.com/ir-docs`); see
> [`../hdfcsky-api-docs/`](../hdfcsky-api-docs/README.md) for **HDFC Sky**
> (`developer.hdfcsky.com/sky-docs`). The two share a house style and some path names but differ in
> endpoints, field names and enum vocabulary — do not mix them.

## Contents

| # | Section | Source |
|---|---------|--------|
| 01 | [Introduction](01-introduction.md) | https://developer.hdfcsec.com/ir-docs/docs/intro |
| 02 | [API Response Structure](02-response-structure.md) | https://developer.hdfcsec.com/ir-docs/docs/response |
| 03 | [Error and Exception Handling](03-errors-and-exceptions.md) | https://developer.hdfcsec.com/ir-docs/docs/error_structure |
| 04 | [Fetch Access Token via Frontend](04-authentication-frontend.md) | https://developer.hdfcsec.com/ir-docs/docs/token_id_fe |
| 05 | [Fetch Access Token via API](05-authentication-api.md) | https://developer.hdfcsec.com/ir-docs/docs/category/fetch-access-token-via-api |
| 06 | [User Profile](06-user-profile.md) | https://developer.hdfcsec.com/ir-docs/docs/user_profile |
| 07 | [Place Order](07-place-order.md) | https://developer.hdfcsec.com/ir-docs/docs/place_order |
| 08 | [Modify Order](08-modify-order.md) | https://developer.hdfcsec.com/ir-docs/docs/modify_order |
| 09 | [Cancel Order](09-cancel-order.md) | https://developer.hdfcsec.com/ir-docs/docs/cancel_order |
| 10 | [Order Status - All Orders](10-order-book.md) | https://developer.hdfcsec.com/ir-docs/docs/order_status |
| 11 | [Single Order Status](11-single-order.md) | https://developer.hdfcsec.com/ir-docs/docs/single_order |
| 12 | [Trade Book - All Trades](12-trade-book.md) | https://developer.hdfcsec.com/ir-docs/docs/trade_book |
| 13 | [Single Trade](13-single-trade.md) | https://developer.hdfcsec.com/ir-docs/docs/trade_book_single_trading |
| 14 | [Overall Position](14-positions.md) | https://developer.hdfcsec.com/ir-docs/docs/overall_position |
| 15 | [Holdings / Portfolio](15-holdings.md) | https://developer.hdfcsec.com/ir-docs/docs/holdings |
| 16 | [Market Data - Fetch LTP](16-market-data-ltp.md) | https://developer.hdfcsec.com/ir-docs/docs/fetchltp |
| 17 | [Market Data - WebSocket](17-websocket.md) | https://developer.hdfcsec.com/ir-docs/docs/market_data_websocket |
| 18 | [Funds and Margins](18-funds-and-margins.md) | https://developer.hdfcsec.com/ir-docs/docs/funds_and_margins |
| 19 | [Security Master](19-security-master.md) | https://developer.hdfcsec.com/ir-docs/docs/security_master |
| — | [`GenericDTO3.proto`](GenericDTO3.proto) | https://developer.hdfcsec.com/ir-docs/assets/files/GenericDTO3-7527bc03756bb132bd39c0eefdae7d35.proto |

## Base URLs

| Purpose | URL |
|---------|-----|
| REST API | `https://developer.hdfcsec.com` |
| WebSocket (market data) | `wss://developer.hdfcsec.com/wsapi/v1/session` |
| Security Master CSV | `https://developer.hdfcsec.com/oapi/v1/security-master` |
| Documentation | `https://developer.hdfcsec.com/ir-docs/` |

All REST endpoints are on the `/oapi/v1/` prefix, except User Profile which is `/oapi/v3/`.
No UAT/sandbox host is documented.

## Endpoint Catalog

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/oapi/v1/login` | Fetch token ID (start of both login flows) |
| POST | `/oapi/v1/login/validate` | Validate username / password |
| POST | `/oapi/v1/twofa/validate` | Validate 2FA code, get request token |
| GET | `/oapi/v1/twofa/resend` | Resend 2FA code |
| GET | `/oapi/v1/authorise` | Accept T&C, get request token |
| POST | `/oapi/v1/access-token` | Exchange request token for access token |
| POST | `/oapi/v3/user/profile` | User profile |
| POST | `/oapi/v1/orders/regular` | Place order |
| PUT | `/oapi/v1/orders/regular/<order_id>` | Modify order |
| DELETE | `/oapi/v1/orders/regular/<order_id>` | Cancel order |
| GET | `/oapi/v1/orders` | Order book (all orders for the day) |
| GET | `/oapi/v1/orders/<order_id>` | Single order status |
| GET | `/oapi/v1/trades` | Trade book (all trades for the day) |
| GET | `/oapi/v1/orders/<order_id>/trades` | Trades for one order |
| GET | `/oapi/v1/portfolio/cumulative-positions` | Overall positions |
| GET | `/oapi/v1/portfolio/holdings` | Demat holdings |
| GET | `/oapi/v1/user/margins` | Funds and margins |
| PUT | `/oapi/v1/fetch-ltp` | LTP snapshot (batch) |
| GET | `/oapi/v1/security-master` | Security master CSV (unauthenticated) |

## Quick Facts

- **Protocol:** REST with JSON request/response bodies; streaming market data over WebSocket using
  Protobuf (`GenericDTO`).
- **Authentication:** `Authorization: <access_token>` header (a JWT, **no** `Bearer ` prefix),
  plus an `api_key` query parameter on every call.
- **`User-Agent` header is mandatory** on essentially every request.
- **Exchanges:** NSE, BSE, MCX.
- **Instrument segments (orders):** EQUITY, OPTIDX, OPTSTK, FUTIDX, FUTSTK, OPTCUR, FUTCUR.
- **Products:** DELIVERY, OVERNIGHT, INTRADAY, MTF, COLL-SELL, ENCASH (profile also reports COVER).
- **Order types:** MARKET, LIMIT, SL, SL-M. **Validity:** DAY, IOC, GTD. AMO via the `amo` boolean.
- **Instruments** are identified by `security_id` from the Security Master for orders, and by the
  numeric `exch_security_id` for LTP and WebSocket. The feed uses prefixed script IDs such as
  `NSE_<token>`, `NFO_<token>`, `BSE_INDEX_<token>`, `MCX_<token>`.
- **WebSocket limits:** up to 1500 instruments per connection, up to 3 simultaneous connections
  per API key.
- **Two login paths:** browser redirect flow ([Fetch Access Token via Frontend](04-authentication-frontend.md))
  or the fully programmatic flow ([Fetch Access Token via API](05-authentication-api.md)).

## Not Documented

The official documentation has no pages for: bracket / cover / GTT / basket orders, position
conversion, historical candles or charts, brokerage or margin calculators, P&L reports, rate
limits, order-update streaming subscription details, or a rejection-code table. The `Order` /
`Trade` Protobuf messages and the `ErrorCode` enum in `GenericDTO3.proto` are the only published
reference for OMS/RMS rejection codes.

## Notes

- **Key casing is inconsistent across endpoints.** [Trade Book](12-trade-book.md) returns
  `snake_case`; [Single Trade](13-single-trade.md) returns `camelCase` for the same data.
  [Funds and Margins](18-funds-and-margins.md) mixes both within a single response. Each page
  documents the specific mismatch.
- **Request and response vocabularies differ.** Orders are placed with `option_type` `CE`/`PE`,
  `expiry_date` `YYYYMMDD` and `transaction_type` `Buy`; the order book returns `Call`/`Put`,
  `30 APR 2024` and `Buy`/`Sell`. The Protobuf enums use a third vocabulary again (`SLM`, `NRML`,
  `CNC`, `MIS`).
- Several official pages contain internal contradictions — documented endpoint path vs. curl
  sample, glossary field names vs. actual response keys, malformed JSON in samples. These are
  preserved verbatim with a callout rather than silently corrected; where a JSON sample would not
  parse at all, the fix is applied and flagged.
- Code fences in the official docs are all tagged `js` regardless of content (curl, JSON, plain
  text). That tagging is preserved in the converted pages so the text stays byte-comparable with
  the source.
- The [Security Master](19-security-master.md) page adds a CSV schema section derived from
  downloading the live file — clearly marked, since the official page documents nothing beyond the
  download link.
- Example tokens, client IDs, order IDs and account values in the samples are illustrative values
  copied from the official docs — they are not live credentials or real data. The username and
  password in the official Login sample have been replaced with placeholders.
