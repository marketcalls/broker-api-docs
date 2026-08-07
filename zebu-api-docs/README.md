# Zebu (MYNT) API Documentation

Unofficial Markdown conversion of the official Zebu MYNT API documentation.

> Source: https://zebumyntapi.web.app/

Zebu's trading API is a **Noren OMS** implementation (same family as Shoonya, Flattrade and
TradeSmart), so the field vocabulary — `jData` payloads, `uid` / `actid` / `exch` / `tsym`,
`prd` / `prctyp` / `trantype`, `stat` + `emsg` responses — matches the other Noren brokers.

The site publishes **two parallel API flavours**, and they are not interchangeable:

| | Base API | OAuth API |
|---|---|---|
| Path prefix | `/NorenWClientTP/` | `/NorenWClientAPI/` |
| Auth | `QuickAuth` login → `jKey` session token sent with every request | OAuth 2.0 authorization code → `Authorization: Bearer <access_token>` |
| Credentials | API key generated in MYNT (valid for a chosen number of months) | Client ID + Secret Key, with Redirect URL and IP whitelisting |
| Docs | [`01`](01-base-introduction.md) – [`06`](06-base-websocket.md) | [`07`](07-oauth-introduction.md) – [`16`](16-oauth-masters.md) |

The OAuth section is the newer of the two and is the one to build against for new integrations.

## Contents

| # | Section | Pages |
|---|---------|-------|
| 01 | [Base — Introduction](01-base-introduction.md) | Base URL, generating an API key from MYNT web |
| 02 | [Base — Users](02-base-users.md) | Login (`QuickAuth`), Client Details, Limits, Logout, error message list |
| 03 | [Base — Order](03-base-order.md) | Place / Modify / Cancel Order, Order Book, Single Order History, Trade Book, GTT orders |
| 04 | [Base — Portfolio](04-base-portfolio.md) | Holdings, Positions Book, Product Conversion, Close position, Close Partially |
| 05 | [Base — Market Quotes](05-base-market-quotes.md) | Quotes, Historical candle data (TPSeries, EOD), Master Files, Index List, Option Chain, Linked Scrips |
| 06 | [Base — WebSocket](06-base-websocket.md) | Connect, Subscribe/Unsubscribe Touchline, Depth and Order Update |
| 07 | [OAuth — Introduction](07-oauth-introduction.md) | Overview, key features, base URLs, obtaining API credentials, OAuth flow |
| 08 | [OAuth — Authentication](08-oauth-authentication.md) | Login redirect, authorization code, `GenAcsTok`, Bearer usage, `RefreshToken` |
| 09 | [OAuth — Users](09-oauth-users.md) | Client Details, Logout |
| 10 | [OAuth — Limits](10-oauth-limits.md) | Margins, collateral, P&L, brokerage and turnover limits |
| 11 | [OAuth — Order](11-oauth-order.md) | Place / Modify / Cancel Order, Order Book, Order history, Trade Book |
| 12 | [OAuth — GTT Order](12-oauth-gtt-order.md) | Place / Modify / Cancel GTT, Pending GTTs, Enabled GTTs |
| 13 | [OAuth — Portfolio](13-oauth-portfolio.md) | Holdings, Positions Book, Product Conversion |
| 14 | [OAuth — Market Quotes](14-oauth-market-quotes.md) | Quotes, Index List, Option Chain, Linked Scrips, TPSeries, EOD Chart Data |
| 15 | [OAuth — Web Socket](15-oauth-websocket.md) | Connect, Subscribe/Unsubscribe Touchline, Depth and Order Update |
| 16 | [OAuth — Masters](16-oauth-masters.md) | Symbol master file downloads, file format, usage guidelines |

## Base URLs

| Purpose | URL |
|---------|-----|
| Production | `https://go.mynt.in` |
| Sandbox / UAT | `https://uat.mynt.in` |
| OAuth login redirect | `https://go.mynt.in/OAuthlogin/authorize/oauth?client_id=<CLIENT_ID>` |
| Close position (Base only) | `https://be.mynt.in/close_position` |
| Symbol master files | `https://go.mynt.in/<EXCH>_symbols.txt.zip` |
| Documentation | `https://zebumyntapi.web.app/` |

Note that `close_position` / `close_partially` sit on a **different host** (`be.mynt.in`) from
every other endpoint.

## Authentication

### OAuth 2.0 (recommended)

1. Generate a Client ID and Secret Key in MYNT (Profile → Client ID → API Key), setting a
   Redirect URL and a mandatory primary IP address.
2. Send the user to `GET /OAuthlogin/authorize/oauth?client_id=<CLIENT_ID>`.
3. After login, MYNT redirects to your Redirect URL with `?code=<AUTHORIZATION_CODE>`.
4. `POST /NorenWClientAPI/GenAcsTok` with `jData={"code": "...", "checksum": "..."}` where
   the checksum is `SHA256(client_id + secret_key + code)` — the three values concatenated
   with no separator.
5. Send `Authorization: Bearer <access_token>` on every subsequent request.
6. `POST /NorenWClientAPI/RefreshToken` with `jData={"refresh_token": "..."}` when the access
   token expires.

### Base (API key)

`POST /NorenWClientTP/QuickAuth` with `jData` containing `uid`, `pwd` (SHA-256 of the
password), `factor2` (DOB `DD-MM-YYYY` or PAN), `vc`, `appkey` (SHA-256 of `uid|app_key`),
`imei`, `apkversion` and `source`. The returned `susertoken` is then sent as `jKey` alongside
`jData` on every call.

## Endpoint Catalog

All REST endpoints are **POST**, with the payload sent as a `text/plain` body of the form
`jData=<json>` (plus `&jKey=<token>` on the Base API). Swap `/NorenWClientAPI/` for
`/NorenWClientTP/` to move between the OAuth and Base flavours.

| Path | Purpose |
|------|---------|
| `/OAuthlogin/authorize/oauth` | OAuth login redirect (GET) |
| `/NorenWClientAPI/GenAcsTok` | Exchange authorization `code` + `checksum` for an access token |
| `/NorenWClientAPI/RefreshToken` | Refresh an expired access token |
| `/NorenWClientTP/QuickAuth` | Base API login |
| `/NorenWClientAPI/ClientDetails` | Client / account details |
| `/NorenWClientAPI/Logout` | End the session |
| `/NorenWClientAPI/Limits` | Margins, collateral, P&L, brokerage, turnover limits |
| `/NorenWClientAPI/PlaceOrder` | Place an order |
| `/NorenWClientAPI/ModifyOrder` | Modify an order |
| `/NorenWClientAPI/CancelOrder` | Cancel an order |
| `/NorenWClientAPI/OrderBook` | All orders for the day |
| `/NorenWClientAPI/SingleOrdHist` | History of a single order |
| `/NorenWClientAPI/TradeBook` | All executed trades |
| `/NorenWClientAPI/PlaceGTTOrder` | Place a GTT order |
| `/NorenWClientAPI/ModifyGTTOrder` | Modify a GTT order |
| `/NorenWClientAPI/CancelGTTOrder` | Cancel a GTT order |
| `/NorenWClientAPI/GetPendingGTTOrder` | Pending GTT orders |
| `/NorenWClientAPI/GetEnabledGTTs` | GTT order types enabled for the account |
| `/NorenWClientAPI/Holdings` | Holdings |
| `/NorenWClientAPI/PositionBook` | Positions book |
| `/NorenWClientAPI/ProductConversion` | Convert product type on a position |
| `/NorenWClientAPI/GetQuotes` | Full quote snapshot |
| `/NorenWClientAPI/GetIndexList` | Index list for an exchange |
| `/NorenWClientAPI/GetOptionChain` | Option chain |
| `/NorenWClientAPI/GetLinkedScrips` | Linked / related scrips |
| `/NorenWClientAPI/TPSeries` | Intraday time-price (candle) series |
| `/NorenWClientAPI/EODChartData` | End-of-day chart data |
| `https://be.mynt.in/close_position` | Close a position fully or partially (Base API only) |

## Symbol Master Files

| Exchange | File |
|----------|------|
| NSE Cash | `https://go.mynt.in/NSE_symbols.txt.zip` |
| BSE Cash | `https://go.mynt.in/BSE_symbols.txt.zip` |
| NSE F&O | `https://go.mynt.in/NFO_symbols.txt.zip` |
| BSE F&O | `https://go.mynt.in/BFO_symbols.txt.zip` |
| NSE Currency | `https://go.mynt.in/CDS_symbols.txt.zip` |
| MCX Commodity | `https://go.mynt.in/MCX_symbols.txt.zip` |

## Gaps in the official documentation

Recorded here because these are properties of the source, not of the conversion:

- **The WebSocket URL is never published.** Both WebSocket pages document the connect
  handshake and every subscribe/unsubscribe message, but neither states the `wss://` host to
  connect to. Other Noren brokers use `wss://<host>/NorenWSTP/`; confirm with Zebu before use.
- **"OHLC Quotes" and "LTP Quotes" are empty headings** on the Base Market Quotes page — the
  bodies exist in the page source but are commented out, so they are not part of the published
  documentation and are not reproduced here.
- Several pages leave the "Possible value" column blank for most fields, including for
  mandatory ones.
- The OAuth pages write the host as `https://{{Base URL}}` in some endpoint tables and as
  `https://go.mynt.in` in others.

## Conversion notes

- One Markdown file per documentation page, numbered in site navigation order.
- Multi-language example tabs (cURL / Python / JavaScript / C# / Java / Go) are flattened to
  bold labels followed by fenced code blocks, preserving all languages.
- Screenshots are linked to their original URLs on the documentation site rather than vendored.
- HTML comments in the source (draft and disabled sections) are omitted.
- Every page was checked to have the same heading, table and code-block count as its source.
