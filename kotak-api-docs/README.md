# Kotak Neo Trade API (v2) — Documentation

Unofficial Markdown conversion of the Kotak Securities Neo Trade API "Client documentation" (v2).

- **Source:** https://app.notion.com/p/Client-documentation-236da70d37e280b3a979fc7be7b003bc
- **Python SDK:** https://github.com/Kotak-Neo/kotak-neo-python
- **Postman collection:** https://bit.ly/3W4x7oO — also vendored in the SDK repo at `docs/postman/`
- **Migration guide (v1 → v2):** https://bit.ly/46nKKpg

*Last reconciled against the SDK repo on 2026-09-07 (SDK v3.0.6, HEAD `a365994`),
and against the Notion source's Order Report APIs page on 2026-09-08.*

> **The response field tables here are Kotak's own, and Kotak's own are partial.**
> Each Order Report table carries a vendor note pointing at a separate API glossary
> for the rest; a live trade object has roughly 50 keys against the 13 listed. A
> field missing from a table is not evidence the API does not return it.

## Contents

| # | File | Description |
| --- | --- | --- |
| 1 | [01-getting-started.md](01-getting-started.md) | 5-step quick start: prerequisites, auth, first order |
| 2 | [02-authentication.md](02-authentication.md) | TOTP login + MPIN validate, response fields, error codes |
| 3 | [03-static-ip-whitelisting.md](03-static-ip-whitelisting.md) | SEBI static IP requirement (effective 1 Apr 2026) |
| 4 | [04-market-data-instruments.md](04-market-data-instruments.md) | Scrip Master (instrument master) API + CSV column mapping |
| 5 | [05-market-data-quotes.md](05-market-data-quotes.md) | Quotes API, filters, index glossary |
| 6 | [06-trading-place-modify-cancel.md](06-trading-place-modify-cancel.md) | Place / Modify / Cancel order APIs |
| 7 | [07-portfolio-positions.md](07-portfolio-positions.md) | Positions API |
| 8 | [08-portfolio-holdings.md](08-portfolio-holdings.md) | Holdings API (+ v1→v2 field mapping) |
| 9 | [09-portfolio-limits.md](09-portfolio-limits.md) | Limits / funds API |
| 10 | [10-portfolio-margins.md](10-portfolio-margins.md) | Margin (check-margin) API |
| 11 | [11-order-reports.md](11-order-reports.md) | Order Book, Order History, Trade Book |
| 12 | [12-neo-websocket.md](12-neo-websocket.md) | Market-data WebSocket (HSM / HSI) |
| 13 | [13-order-position-streaming-websocket.md](13-order-position-streaming-websocket.md) | Order & Position streaming WebSocket |
| 14 | [14-troubleshooting-faqs-error-codes.md](14-troubleshooting-faqs-error-codes.md) | FAQs, error handling, error codes |
| 15 | [15-api-reference.md](15-api-reference.md) | cURL examples + downloadable references |
| 16 | [16-market-data-historical.md](16-market-data-historical.md) | Historical OHLCV candles (new, Sept 2026) |
| 17 | [17-market-data-expiries-option-chain.md](17-market-data-expiries-option-chain.md) | Expiry dates + option/futures chain (new, Sept 2026) |

## What changed in the September 2026 update

Kotak revised the Neo documentation and SDK between 2026-08-19 and 2026-09-06. The API-surface changes, all reflected above:

| Change | Where |
| --- | --- |
| Three new market-data endpoints: historical candles, expiries, option chain | [16](16-market-data-historical.md), [17](17-market-data-expiries-option-chain.md) |
| New optional order tag field `ig`, echoed back as `GuiOrdId` in the order and trade reports | [06](06-trading-place-modify-cancel.md), [11](11-order-reports.md) |
| Quotes limits documented for the first time: 50 instruments per call, 25 requests/second | [05](05-market-data-quotes.md) |
| WebSocket market-status and Closing Auction Session (CAS) message types | [12](12-neo-websocket.md) |
| Feed hosts now resolved per data centre from a config service; no data centre routes to the legacy HSM feed any more | [12](12-neo-websocket.md) |
| HSM deprecated: `HSWebSocket`/`HSIWebSocket` removed from the SDK in 2.2.0 with no replacement and no HSM fallback, though `mlhsm` still serves | [12](12-neo-websocket.md) |

The Positions, Holdings, Limits, Margin, Order Book, Order History and Trade Book endpoints were **not** changed — request and response shapes and the documented P&L formula all stand. The remainder of the update (structured logging, Jupyter support, a sync-integration guide) is internal to Kotak's Python SDK and does not affect anyone calling the REST API directly.

## Key concepts (quick reference)

**Login endpoints (fixed):**
- TOTP login: `POST https://mis.kotaksecurities.com/login/1.0/tradeApiLogin`
- MPIN validate: `POST https://mis.kotaksecurities.com/login/1.0/tradeApiValidate` → returns `baseUrl`, session token, session sid

**Token types:**
- **Access token** — from Neo app/web → More/Invest → TradeAPI → API Dashboard. Sent as plain string (no `Bearer`) in `Authorization` header for Login, Quotes, Scripmaster, and the three market-data APIs (historical candles, expiries, option chain). These authenticate on the access token **alone** — no TOTP/MPIN session, so no `Auth`/`Sid` headers.
- **View token / View sid** — returned by `tradeApiLogin` (TOTP step).
- **Session token (Trade token) / Session sid** — returned by `tradeApiValidate` (MPIN step). Used as `Auth` + `Sid` headers for all post-login APIs.
- **`neo-fin-key`** — static value `neotradeapi`; required on all APIs **except** Quotes, Scripmaster, and the three market-data APIs above.

**Rate limit:** 10 requests/second across APIs, but this is not uniform and the per-endpoint figure wins where one is documented:

- Quotes: 25 requests/second, and at most 50 instruments per call (see [05](05-market-data-quotes.md); measured, the instrument cap is lower still).
- Historical candles: no published limit. Measured 2026-09-21 at **1 request/second** sustained; 0.75 s between requests already draws HTTP 429, and no `Retry-After` header is sent. An earlier measurement on 2026-09-06 put it near 5/second, so this one is worth re-checking rather than assuming (see [16](16-market-data-historical.md)).

> Unofficial conversion for personal/educational reference. Always verify against Kotak's official documentation. Support: service.securities@kotak.com
