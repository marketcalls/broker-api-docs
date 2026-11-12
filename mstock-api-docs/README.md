# mStock Trading API Documentation (Type B)

Unofficial Markdown conversion of the official mStock (Mirae Asset Capital Markets) Trading API v1
documentation.

> Source: https://tradingapi.mstock.com/docs/v1/Introduction/

The mStock Trading API is a REST-style HTTP API covering authentication (password + OTP or TOTP),
order management (place / modify / cancel / cancel-all), order book, trade book and trade history,
portfolio holdings, net positions and position conversion, order margin calculation, baskets,
market quotes and the instrument scrip master, historical and intraday candles, option chain,
top gainers/losers, plus a binary market-data WebSocket feed.

The upstream docs publish two parallel API variants, **Type A** (`/openapi/typea/...`) and
**Type B** (`/openapi/typeb/...`). **Only Type B is covered here**, since that is the variant
OpenAlgo supports. Shared pages (Introduction, Partners Onboarding, Annexure) are included as-is.

## Endpoints

| Base | URL |
| --- | --- |
| Interactive (REST) | `https://api.mstock.trade` |
| Broadcasting (WebSocket) | `wss://ws.mstock.trade` |

All Type B REST paths are rooted at `https://api.mstock.trade/openapi/typeb/`.

## Contents

| # | Section | Group | Covers |
|---|---------|-------|--------|
| 01 | [Introduction](01-introduction.md) | Getting started | Root endpoints, rate limits, API key & access-token validity, common request headers, BOD/EOD timings |
| 02 | [User Details and Authentication](02-user-and-authentication.md) | Type B | Login flow, `connect/login`, `session/token`, `session/verifytotp`, `user/fundsummary`, `logout` |
| 03 | [Orders](03-orders.md) | Type B | `orders/regular` (place), `orders/regular/{OrderID}` (modify), cancel, `orders/cancelall`, `orders`, `tradebook`, `trades`, `order/details` |
| 04 | [Portfolio](04-portfolio.md) | Type B | `portfolio/holdings` |
| 05 | [Position](05-position.md) | Type B | `portfolio/positions`, `portfolio/convertposition` |
| 06 | [Calculate Order Margin](06-calculate-order-margin.md) | Type B | `margins/orders` |
| 07 | [Basket APIs](07-basket.md) | Type B | `CreateBasket`, `FetchBasket`, `RenameBasket`, `DeleteBasket`, `CalculateBasket` |
| 08 | [Market Quotes and Instruments](08-market-quotes-and-instruments.md) | Type B | `instruments/quote` (OHLC), `instruments/OpenAPIScripMaster` |
| 09 | [Historical Data](09-historical-data.md) | Type B | `instruments/historical` |
| 10 | [Intraday Chart Data](10-intraday-chart-data.md) | Type B | `instruments/intraday` |
| 11 | [Option Chain APIs](11-option-chain.md) | Type B | `getoptionchainmaster/{exch}`, `GetOptionChain/{exch}/{expiry}/{token}` |
| 12 | [Top Gainers / Losers](12-gainers-losers.md) | Type B | Top gainers / losers API |
| 13 | [Exceptions and Error Types](13-error-codes.md) | Type B | `IA400` / `IA401` / `IA403` / `IA404` / `IA500` / `MA{XXX}` error codes |
| 14 | [Market Data (WebSocket)](14-market-data-websocket.md) | Type B | `wss://ws.mstock.trade` — auth, subscribe/unsubscribe, modes, binary quote (379 bytes) and market-depth (200 bytes) packet layouts |
| 15 | [Partners Onboarding](15-partners-onboarding.md) | Partners Onboarding | Third-party platform login redirect flow, encrypted user payload handling, decryption |
| 16 | [Annexure](16-annexure.md) | Reference | Exchange index token tables (BSE / NSE) |

## Authentication summary

1. Generate an API key at [trade.mstock.com](https://trade.mstock.com).
2. `POST /openapi/typeb/connect/login` with client code + password → OTP is sent to the registered mobile.
3. `POST /openapi/typeb/session/token` with the OTP → returns `jwtToken` (access token) and `refreshToken`.
   With TOTP enabled, use `POST /openapi/typeb/session/verifytotp` instead.
4. Send on every subsequent call:
   - `X-Mirae-Version: 1`
   - `Authorization: token <api_key>:<jwtToken>`
   - `X-PrivateKey: <api_key>`

Access tokens expire within 12 hours or at end of day, whichever comes first, so they must be
regenerated daily.

## Known quirks in the upstream docs

These are reproduced verbatim rather than silently corrected — verify against the code samples on
each page, which use the correct paths:

- In the `02-user-and-authentication.md` "User APIs" summary table, the verify-TOTP row lists
  `.../openapi/typeb/openapi/typeb/session/verifytotp` (segment duplicated). The correct path is
  `/openapi/typeb/session/verifytotp`.
- In the `08-market-quotes-and-instruments.md` summary table, the OHLC row lists
  `.../openapi/typeb/typeb/instruments/quote` (segment duplicated). The correct path is
  `/openapi/typeb/instruments/quote`.
- "Option Chain Master" in `11-option-chain.md` is marked *coming soon* upstream.

## Disclaimer

Unofficial Markdown conversion maintained for personal/educational reference. The official mStock
documentation at https://tradingapi.mstock.com/docs/ is the authoritative source — always verify
against it. Trademarks and content belong to mStock / Mirae Asset Capital Markets.
