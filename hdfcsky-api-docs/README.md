# HDFC Sky Open API Documentation

Unofficial Markdown conversion of the official HDFC Sky Open API developer documentation.

> Source: https://developer.hdfcsky.com/sky-docs/docs/intro

HDFC Sky Open API is HDFC Securities' REST + WebSocket trading API. It covers login/token
generation, regular and AMO orders, bracket and cover orders, GTT, basket orders, order book
and trade book, funds, portfolio (positions, holdings, eDIS), brokerage and margin calculators,
historical candles, LTP snapshots, and a Protobuf-based streaming market data feed.

## Contents

| # | Section | Source |
|---|---------|--------|
| 01 | [Introduction](01-introduction.md) | https://developer.hdfcsky.com/sky-docs/docs/intro |
| 02 | [Response Data Structure](02-response-structure.md) | https://developer.hdfcsky.com/sky-docs/docs/response |
| 03 | [Exceptions and Errors](03-errors-and-exceptions.md) | https://developer.hdfcsky.com/sky-docs/docs/error_structure |
| 04 | [Fetch Access Token via Frontend](04-authentication-frontend.md) | https://developer.hdfcsky.com/sky-docs/docs/token_id_fe |
| 05 | [Fetch Access Token via API](05-authentication-api.md) | https://developer.hdfcsky.com/sky-docs/docs/category/fetch-access-token-via-api |
| 06 | [Regular Orders](06-regular-orders.md) | https://developer.hdfcsky.com/sky-docs/docs/category/regular-orders |
| 07 | [Conditional Orders (BO / CO)](07-conditional-orders.md) | https://developer.hdfcsky.com/sky-docs/docs/category/conditonal-orders |
| 08 | [Order Book](08-order-book.md) | https://developer.hdfcsky.com/sky-docs/docs/category/order-book |
| 09 | [GTT Orders](09-gtt-orders.md) | https://developer.hdfcsky.com/sky-docs/docs/category/gtt-orders |
| 10 | [Basket Orders](10-basket-orders.md) | https://developer.hdfcsky.com/sky-docs/docs/category/basket-orders |
| 11 | [Funds](11-funds.md) | https://developer.hdfcsky.com/sky-docs/docs/category/funds |
| 12 | [Portfolio](12-portfolio.md) | https://developer.hdfcsky.com/sky-docs/docs/category/portfolio |
| 13 | [Brokerage](13-brokerage.md) | https://developer.hdfcsky.com/sky-docs/docs/brokerage/calculateBrokerage |
| 14 | [Margin Calculator](14-margin-calculator.md) | https://developer.hdfcsky.com/sky-docs/docs/margin_calculator |
| 15 | [Chart Data](15-chart-data.md) | https://developer.hdfcsky.com/sky-docs/docs/fetchCandles |
| 16 | [Market Data - LTP](16-market-data-ltp.md) | https://developer.hdfcsky.com/sky-docs/docs/fetchltp |
| 17 | [Market Data - WebSocket](17-websocket.md) | https://developer.hdfcsky.com/sky-docs/docs/websocket |
| 18 | [PNL Data](18-pnl-data.md) | https://developer.hdfcsky.com/sky-docs/docs/PNL_Data |
| 19 | [Profile](19-profile.md) | https://developer.hdfcsky.com/sky-docs/docs/profile/ |
| 20 | [Rejection Codes](20-rejection-codes.md) | https://developer.hdfcsky.com/sky-docs/docs/rejection_code |
| 21 | [Security Master](21-security-master.md) | https://developer.hdfcsky.com/sky-docs/docs/security_master |

## Base URLs

| Purpose | URL |
|---------|-----|
| REST API (production) | `https://developer.hdfcsky.com` |
| REST API (UAT) | `https://uat-developer.hdfcsky.com` |
| WebSocket (UAT, as documented) | `ws://uat-developer.hdfcsky.com/wsapi/v1/session` |
| Security Master CSV | `https://hdfcsky.com/api/v1/contract/Compact?info=download` |
| Documentation | `https://developer.hdfcsky.com/sky-docs/` |

Most endpoints are under the `/oapi/v1/` prefix (funds also has a `/oapi/v2/` variant, and
chart data lives under `/oapi/charts-api/charts/v1/`).

## Endpoint Catalog

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/oapi/v1/login` | Fetch token ID (start of the API login flow) |
| POST | `/oapi/v1/login-channel/validate` | Validate username / start login |
| PUT | `/oapi/v1/otp/validate` | Validate 2FA code |
| POST | `/oapi/v1/twofa/resend` | Resend 2FA code |
| POST | `/oapi/v1/twofa/validate` | Validate PIN |
| GET | `/oapi/v1/authorise` | Authorise the app, get request token |
| POST | `/oapi/v1/access-token` | Exchange request token for access token |
| POST / PUT | `/oapi/v1/orders` | Place / modify regular and AMO orders |
| DELETE | `/oapi/v1/orders/<oms_order_id>` | Delete regular / AMO order |
| GET | `/oapi/v1/orders` | Order book (pending / completed) |
| GET | `/oapi/v1/order/<oms_order_id>/history` | Order history |
| GET | `/oapi/v1/trades` | Trade book |
| POST / PUT | `/oapi/v1/orders/kart` | Place / modify Bracket and Cover orders |
| DELETE | `/oapi/v1/orders/kart/<oms_order_id>` | Exit BO / CO order |
| POST / PUT | `/oapi/v1/event/gtt` | Place / modify GTT order |
| GET | `/oapi/v1/event/gtt/<client_id>` | Fetch GTT orders |
| DELETE | `/oapi/v1/event/gtt/<client_id>/<id>` | Cancel GTT order |
| POST / PUT / DELETE | `/oapi/v1/basket` | Create / rename / delete basket |
| POST / PUT / DELETE | `/oapi/v1/basket/order` | Fetch, add, edit and delete basket instruments |
| POST | `/oapi/v1/orders/kart` | Execute basket order |
| GET | `/oapi/v1/funds/view` | Funds V1 |
| GET | `/oapi/v2/funds/view` | Funds V2 |
| GET | `/oapi/v1/positions` | Positions (daywise / netwise) |
| PUT | `/oapi/v1/position/convert` | Convert positions |
| GET | `/oapi/v1/holdings` | Demat holdings |
| POST | `/oapi/v1/edis/instrument_details` | eDIS holding authorisation |
| GET | `/oapi/v1/brokerage/calculate` | Brokerage calculator |
| POST | `/oapi/v1/margin` | Margin calculator |
| POST | `/oapi/v1/reports/pnl` | PNL data |
| GET | `/oapi/v1/user/trading_info` | User profile |
| PUT | `/oapi/v1/fetch-ltp` | LTP snapshot |
| GET | `/oapi/charts-api/charts/v1/fetch-candle` | Historical candles |

## Quick Facts

- **Protocol:** REST with JSON request/response bodies; streaming market data over WebSocket
  using Protobuf (`GenericDTO` proto file linked from the WebSocket page).
- **Authentication:** `Authorization: <access_token>` header (no `Bearer ` prefix), plus an
  `api_key` query parameter on most calls.
- **`User-Agent` header is mandatory** on essentially every request.
- **Exchanges:** NSE, BSE, NFO, BFO, CDS/NCD, MCX.
- **Products:** CNC, MIS, NRML. **Order types:** LIMIT, MARKET, SL, SLM. **Validity:** DAY, IOC.
- **Instruments** are identified by `instrument_token` from the Security Master CSV; the
  WebSocket feed uses prefixed script IDs such as `NSE_<token>`, `NFO_<token>`, `BSE_INDEX_<token>`.
- **WebSocket limits:** up to 300 instruments per connection, up to 3 simultaneous connections
  per API key.
- **Two login paths:** browser redirect flow (Fetch Access Token via Frontend) or the fully
  programmatic flow (Fetch Access Token via API).

## Notes

- Some documented URLs point at the UAT host (`uat-developer.hdfcsky.com`) while others use the
  production host (`developer.hdfcsky.com`); the official docs are inconsistent here and the
  conversion preserves them verbatim.
- Rejection codes and the Security Master are distributed as downloadable CSVs, not as inline
  tables — the download links are preserved in the respective pages.
- Example tokens, client IDs, order IDs and account values in the samples are illustrative
  values copied from the official docs — they are not live credentials or real data.
