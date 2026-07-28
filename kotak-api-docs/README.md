# Kotak Neo Trade API (v2) — Documentation

Unofficial Markdown conversion of the Kotak Securities Neo Trade API "Client documentation" (v2).

- **Source:** https://app.notion.com/p/Client-documentation-236da70d37e280b3a979fc7be7b003bc
- **Python SDK:** https://github.com/Kotak-Neo/Kotak-neo-api-v2
- **Postman collection:** https://bit.ly/3W4x7oO
- **Migration guide (v1 → v2):** https://bit.ly/46nKKpg

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

## Key concepts (quick reference)

**Login endpoints (fixed):**
- TOTP login: `POST https://mis.kotaksecurities.com/login/1.0/tradeApiLogin`
- MPIN validate: `POST https://mis.kotaksecurities.com/login/1.0/tradeApiValidate` → returns `baseUrl`, session token, session sid

**Token types:**
- **Access token** — from Neo app/web → More/Invest → TradeAPI → API Dashboard. Sent as plain string (no `Bearer`) in `Authorization` header for Login, Quotes, and Scripmaster APIs.
- **View token / View sid** — returned by `tradeApiLogin` (TOTP step).
- **Session token (Trade token) / Session sid** — returned by `tradeApiValidate` (MPIN step). Used as `Auth` + `Sid` headers for all post-login APIs.
- **`neo-fin-key`** — static value `neotradeapi`; required on all APIs **except** Quotes and Scripmaster.

**Rate limit:** 10 requests/second across APIs.

> Unofficial conversion for personal/educational reference. Always verify against Kotak's official documentation. Support: service.securities@kotak.com
