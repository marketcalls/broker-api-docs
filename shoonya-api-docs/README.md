# Shoonya API Documentation

Unofficial Markdown conversion of the official Shoonya (Finvasia) API documentation.

> Source: https://shoonya.com/api-documentation

Shoonya's trading API is powered by Finvasia's **Noren OMS**. It is a REST + WebSocket API
covering OAuth-style login and session management, user and account details, symbol search
and security info, quotes and option chain, order placement/modification/cancellation,
order and trade books, positions, holdings, margins, watch lists, price alerts, GTT orders,
and a streaming feed for touchline, market depth and order updates.

## Contents

| # | Section | Pages |
|---|---------|-------|
| 01 | [Introduction](01-introduction.md) | Overview, target audience, integration options |
| 02 | [Authentication](02-authentication.md) | How to get an API key, Login, Logout, Validate HS Token |
| 03 | [User & Account Management](03-user-and-account-management.md) | User Details, Client Details, Forgot Password, Change Password, Set Device Pin, Login With Device Pin |
| 04 | [Symbol & Instrument Data](04-symbol-and-instrument-data.md) | Search Scrips, Get Security Info |
| 05 | [Market Data](05-market-data.md) | Get Quotes, Get Option Chain |
| 06 | [Orders & Trading](06-orders-and-trading.md) | Place Order, Modify Order, Cancel Order, Product Conversion |
| 07 | [Order & Trade Information](07-order-and-trade-information.md) | Order Margin, Basket Margin, Order Book, Single Order History, Single Order Status, Trade Book, Positions Book |
| 08 | [Portfolio](08-portfolio.md) | Holdings, Limits |
| 09 | [Web Socket API](09-websocket-api.md) | Connect, Subscribe/Unsubscribe Touchline, Subscribe/Unsubscribe Depth, Subscribe/Unsubscribe Order Update |
| 10 | [Watch Lists](10-watch-lists.md) | Get WatchList Names, Get WatchList, Add Scrip, Delete Scrip |
| 11 | [Alerts](11-alerts.md) | Set Alert, Cancel Alert, Modify Alert, Get Pending Alert, Get Enabled Alert Types |
| 12 | [GTT Orders](12-gtt-orders.md) | Place GTT, Cancel GTT, Get Pending GTT, Get Enabled GTTs, Get Unsettled Trading Date |
| 13 | [Symbol Master](13-symbol-master.md) | Downloadable symbol files per exchange |
| 14 | [Exceptions & Errors](14-exceptions-and-errors.md) | Common HTTP error codes |
| 15 | [Python (SDK)](15-python-sdk.md) | Official Python SDK repository |

## Base URLs

| Purpose | URL |
|---------|-----|
| REST API endpoints | `/NorenWClientAPI/<Endpoint>` (see note below) |
| Host used in the official curl samples | `https://apitest.kambala.co.in` |
| WebSocket | `wss://api.shoonya.com/NorenWSAPI/` |
| Symbol master files | `https://api.shoonya.com/<EXCH>_symbols.txt.zip` |
| Trading site (login / API key) | `https://trade.shoonya.com/` |
| Documentation | `https://shoonya.com/api-documentation` |

The documentation states endpoint **paths** (`/NorenWClientAPI/PlaceOrder`) rather than a
production base URL; every curl sample points at the `apitest.kambala.co.in` test host. The
WebSocket page is the only one that names `api.shoonya.com` directly. Verify the production
host against your onboarding email before wiring anything up.

## Endpoint Catalog

All REST endpoints are **POST** with the payload sent as a form field named `jData`
(a JSON object), plus `jKey` (the session token) where applicable.

| Path | Purpose |
|------|---------|
| `/NorenWClientAPI/GenAcsTok` | Login — exchange `code` + `checksum` for `susertoken` |
| `/NorenWClientAPI/Logout` | End the session |
| `/NorenWClientAPI/ValidateHsToken` | Validate a token (server-side only) |
| `/NorenWClientAPI/UserDetails` | User profile, enabled exchanges (`exarr`) and products (`prarr`) |
| `/NorenWClientAPI/ClientDetails` | Client details |
| `/NorenWClientAPI/ForgotPassword` | Forgot password |
| `/NorenWClientAPI/Changepwd` | Change password |
| `/NorenWClientAPI/SetPin` | Set device PIN |
| `/NorenWClientAPI/PinAuth` | Login with device PIN |
| `/NorenWClientAPI/SearchScrip` | Symbol search |
| `/NorenWClientAPI/GetSecurityInfo` | Contract / security info |
| `/NorenWClientAPI/GetQuotes` | Full quote snapshot |
| `/NorenWClientAPI/GetOptionChain` | Option chain |
| `/NorenWClientAPI/PlaceOrder` | Place an order |
| `/NorenWClientAPI/ModifyOrder` | Modify an order |
| `/NorenWClientAPI/CancelOrder` | Cancel an order |
| `/NorenWClientAPI/ProductConversion` | Convert product type on a position |
| `/NorenWClientAPI/GetOrderMargin` | Margin for a single order |
| `/NorenWClientAPI/GetBasketMargin` | Margin for a basket of orders |
| `/NorenWClientAPI/OrderBook` | Order book |
| `/NorenWClientAPI/SingleOrdHist` | Order history for one order |
| `/NorenWClientAPI/SingleOrdStatus` | Status of one order |
| `/NorenWClientAPI/TradeBook` | Trade book |
| `/NorenWClientAPI/PositionBook` | Positions book |
| `/NorenWClientAPI/Holdings` | Holdings |
| `/NorenWClientAPI/MWList` | Watch list names |
| `/NorenWClientAPI/MarketWatch` | Watch list contents |
| `/NorenWClientAPI/AddMultiScripsToMW` | Add scrips to a watch list |
| `/NorenWClientAPI/DeleteMultiMWScrips` | Remove scrips from a watch list |
| `/NorenWClientAPI/SetAlert` | Create a price alert |
| `/NorenWClientAPI/ModifyAlert` | Modify an alert |
| `/NorenWClientAPI/CancelAlert` | Cancel an alert |
| `/NorenWClientAPI/PlaceGTTOrder` | Place a GTT order |
| `/NorenWClientAPI/CancelGTTOrder` | Cancel a GTT order |
| `/NorenWClientAPI/GetPendingGTTOrder` | Pending GTT orders |
| `/NorenWClientAPI/GetEnabledGTTs` | Enabled GTT types |
| `/NorenWClientAPI/GetUnSttledTradingDate` | Unsettled trading date |
| `wss://api.shoonya.com/NorenWSAPI/` | WebSocket connect (`t: "a"`) |
| `/NorenWSTP` | Path quoted on the Subscribe Order Update page |

## Quick Facts

- **Protocol:** REST over POST; the request body is `jData=<json>` (and `jKey=<token>` for
  authenticated calls). Streaming is plain-JSON WebSocket messages keyed by a `t` field:
  `a` connect, `t` touchline, `d` depth, `o` order update, `u` unsubscribe touchline, and
  `ud` for unsubscribe depth *and* unsubscribe order update; acknowledgements and feeds come
  back as `ak`, `tk`/`tf`, `dk`/`df`, `ok`/`om`, `uk`, `udk`, `uok`.
- **Login:** OAuth-style. You receive a `code` on the redirect, then POST it to `GenAcsTok`
  with `checksum` = SHA-256 of `appkey + secretkey + code` concatenated without spaces. The
  response carries `susertoken`, which becomes `jKey` / `usertoken` everywhere else.
  API key and secret are generated from the profile section of `trade.shoonya.com`.
- **Exchanges:** NSE, NFO, BSE, BFO, MCX, CDS, NCX, BCD — the allowed set per user comes back
  in `exarr` from User Details.
- **Products:** `C`, `M`, `I`, `B`, `H` (from `prarr`). **Transaction type:** `B` / `S`.
  **Price types:** `LMT`, `MKT`, `SL-LMT`, `SL-MKT`, `DS`, plus `2L` / `3L` for two- and
  three-leg orders. **Retention:** `DAY`, `EOS`, `IOC`.
- **Instruments** are identified by `exch` + `tsym` (trading symbol) in REST calls and by
  `EXCH|token` (e.g. `NSE|22#BSE|508123`) in WebSocket subscriptions. Symbols containing
  special characters (`M&M`) must be URL-encoded.
- **Symbol master** files are per-exchange zipped text files under `api.shoonya.com`, listed
  in [13-symbol-master.md](13-symbol-master.md).
- **Errors:** standard HTTP codes plus a JSON body with `stat: "Not_Ok"` and `emsg`.
  `403` means the session expired and you must re-login; `429` is rate limiting.
- **Python SDK:** https://github.com/Shoonya-API-OAuth-Python/Shoonya_API_OAuth

## Notes

- **Three sidebar entries on the live site render the wrong page.** `Limits` (Portfolio)
  renders the *Get WatchList Names* page, `Get Pending Alert` renders *Get Pending GTT Order*,
  and `Get Enabled Alert Types` renders *Get Enabled GTTs* — the nav entries point at the same
  component. These are reproduced as published, each with an inline conversion note. There is
  no separate documentation for Limits, pending alerts, or alert types, even though the Order
  Margin page's calculation notes reference a `/Limits` API.
- The *Get WatchList Names* page's "Sample Success Response" is garbled in the official docs
  (table headings leak into the JSON sample). It is reproduced verbatim.
- Section landing entries in the sidebar (e.g. clicking "Market Data" itself) have no page of
  their own on the live site, so this conversion has one file per section with the individual
  API pages as `##` headings inside it.
- The source is a client-rendered Next.js application with no per-page URLs, so section links
  in this README point at the single documentation URL.
- Example tokens, order numbers, client IDs and account values in the samples are illustrative
  values copied from the official docs — they are not live credentials or real data.
