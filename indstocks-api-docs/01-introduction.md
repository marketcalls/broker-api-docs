# Introduction

> Source: https://api-docs.indstocks.com/introduction/

The INDstocks API is a RESTful platform for building trading and investment applications. It
provides deep integration into the INDstocks trading platform, allowing you to execute orders
in real time, manage your portfolio, access live market data, and much more.

## API Design

- **Resource-based URLs** — predictable, resource-oriented endpoint paths.
- **JSON everywhere** — request bodies and responses are JSON-encoded.
- **Standard HTTP status codes** — `2xx` for success, `4xx` for client errors, `5xx` for
  server errors.

## What You Can Do

| Category | Capabilities |
|----------|--------------|
| **Market Data** | Instruments master, real-time quotes (full / LTP / depth), historical OHLCV candles, WebSocket streaming |
| **Trading & Orders** | Place / modify / cancel orders, order book, trade book, Smart Orders (GTT) with OCO and multi-leg support |
| **Portfolio & Risk** | Holdings, positions, funds, margin calculation |
| **Utilities** | Option chain, expiries, greeks *(coming soon)*, error codes |

## Base URL

```
https://api.indstocks.com
```

## Suggested Reading Path

1. **[Getting Started](02-getting-started.md)** — generate a token and make your first call
2. **[API Conventions](03-conventions.md)** — headers, formats, rate limits
3. **[Authentication & Users](04-authentication-users.md)** — verify your token, or automate
   token generation with TOTP
4. **[Order Management](09-order-management.md)** — place your first order
5. **[Glossary & Constants](16-glossary.md)** — enum, prefix, and identifier reference

Algorithmic traders should also review **[Smart Orders (GTT)](10-smart-orders.md)** for
stop-loss / target automation.

## Platform Highlights

- Multi-leg GTT strategies with OCO (One-Cancels-Other) support
- Real-time market data streaming across all asset classes
- Multi-exchange connectivity (NSE, BSE)
- Flat ₹5 brokerage, no API subscription fees
