# INDstocks Trading API Documentation

Unofficial Markdown conversion of the official INDstocks Trading API documentation.

> Source: https://api-docs.indstocks.com/

INDstocks is a RESTful trading platform that lets you place and manage orders in real time,
stream live market data, access historical candles, track your portfolio, and calculate
margins — with flat ₹5 brokerage and no API subscription fees.

## Contents

| # | Section | Source |
|---|---------|--------|
| 01 | [Introduction](01-introduction.md) | https://api-docs.indstocks.com/introduction/ |
| 02 | [Getting Started](02-getting-started.md) | https://api-docs.indstocks.com/getting-started/ |
| 03 | [API Conventions](03-conventions.md) | https://api-docs.indstocks.com/conventions/ |
| 04 | [Authentication & Users](04-authentication-users.md) | https://api-docs.indstocks.com/Users/ |
| 05 | [Instruments Master](05-instruments.md) | https://api-docs.indstocks.com/instruments/ |
| 06 | [Market Quotes](06-market-quotes.md) | https://api-docs.indstocks.com/MarketQuote/ |
| 07 | [Historical Data](07-historical-data.md) | https://api-docs.indstocks.com/historicalData/ |
| 08 | [WebSocket Streaming](08-websockets.md) | https://api-docs.indstocks.com/Websockets/ |
| 09 | [Order Management](09-order-management.md) | https://api-docs.indstocks.com/normal_orders/ |
| 10 | [Smart Orders (GTT)](10-smart-orders.md) | https://api-docs.indstocks.com/smart_orders/ |
| 11 | [Margin Calculator](11-margin-calculator.md) | https://api-docs.indstocks.com/margin_calculation/ |
| 12 | [Portfolio & Funds](12-portfolio-funds.md) | https://api-docs.indstocks.com/portfolio_funds/ |
| 13 | [Utility APIs](13-utility.md) | https://api-docs.indstocks.com/utility/ |
| 14 | [Error Codes](14-errors.md) | https://api-docs.indstocks.com/errors/ |
| 15 | [API Overview (Endpoint Catalog)](15-api-overview.md) | https://api-docs.indstocks.com/api-overview/ |

## Base URLs

| Purpose | URL |
|---------|-----|
| REST API | `https://api.indstocks.com` |
| Price Feed WebSocket | `wss://ws-prices.indstocks.com/api/v1/ws/prices` |
| Order Updates WebSocket | `wss://ws-order-updates.indstocks.com/api/v1/ws/trades` |
| Documentation | `https://api-docs.indstocks.com` |

## Quick Facts

- **Protocol:** REST with JSON request/response bodies
- **Authentication:** Access token in the `Authorization` header
- **Exchanges:** NSE, BSE
- **Segments:** Equity, Derivatives (Futures & Options)
- **Timestamps:** Unix epoch **milliseconds**, IST timezone
- **Token validity:** Access tokens expire after **24 hours**

## Notes

- The BASE URL, endpoint paths, and payload JSON keys are **case-sensitive**. Use the exact
  format shown in the docs.
- The `Authorization` header takes the raw access token **without** a `Bearer ` prefix, i.e.
  `Authorization: YOUR_ACCESS_TOKEN`.
- Example tokens, order IDs, and account values in the response samples are illustrative
  values copied from the official docs — they are not live credentials or real data.
- Utility endpoints (Option Chain, Expiries, Greeks) are marked **"Coming Soon"** in the
  official docs and may not be live yet.
