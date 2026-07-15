# API Overview — Endpoint Catalog

> Source: https://api-docs.indstocks.com/api-overview/

A complete catalog of INDstocks REST endpoints, grouped by category. All paths are relative to
the base URL `https://api.indstocks.com`.

## 1. User Management & Profile

| Endpoint | Method | Purpose | Docs |
|----------|--------|---------|------|
| `/user/profile` | GET | User profile and account details | [04](04-authentication-users.md) |
| `/funds` | GET | Available and utilized funds | [04](04-authentication-users.md) · [12](12-portfolio-funds.md) |

## 2. Market Data

| Endpoint | Method | Purpose | Docs |
|----------|--------|---------|------|
| `/market/instruments` | GET | Instrument master (CSV) | [05](05-instruments.md) |
| `/market/quotes/full` | GET | Real-time full market quotes | [06](06-market-quotes.md) |
| `/market/quotes/ltp` | GET | Last traded price only | [06](06-market-quotes.md) |
| `/market/quotes/mkt` | GET | Market depth / order book | [06](06-market-quotes.md) |
| `/market/historical/{interval}` | GET | Historical OHLCV candle data | [07](07-historical-data.md) |

## 3. Order Management

| Endpoint | Method | Purpose | Docs |
|----------|--------|---------|------|
| `/order` | POST | Place a new order | [09](09-order-management.md) |
| `/order/modify` | POST | Modify a pending order | [09](09-order-management.md) |
| `/order/cancel` | POST | Cancel an order | [09](09-order-management.md) |
| `/order` | GET | Get single order details | [09](09-order-management.md) |
| `/order-book` | GET | Daily order history | [09](09-order-management.md) |
| `/trades/{order_id}` | GET | Trades for a specific order | [09](09-order-management.md) |
| `/trade-book` | GET | Trade book for a segment | [09](09-order-management.md) |

## 4. Smart Orders (GTT)

| Endpoint | Method | Purpose | Docs |
|----------|--------|---------|------|
| `/smart/order` | POST | Multi-leg GTT / OCO order | [10](10-smart-orders.md) |
| `/smart/order/modify` | POST | Modify a smart order | [10](10-smart-orders.md) |
| `/smart/order/cancel` | POST | Cancel a smart order | [10](10-smart-orders.md) |

## 5. Portfolio & Risk

| Endpoint | Method | Purpose | Docs |
|----------|--------|---------|------|
| `/portfolio/holdings` | GET | Equity holdings in Demat account | [12](12-portfolio-funds.md) |
| `/portfolio/positions` | GET | Open positions (intraday & F&O) | [12](12-portfolio-funds.md) |
| `/margin` | GET | Margin calculation for orders | [11](11-margin-calculator.md) |

## 6. WebSocket Streaming

| Stream | URL | Docs |
|--------|-----|------|
| Price Feed | `wss://ws-prices.indstocks.com/api/v1/ws/prices` | [08](08-websockets.md) |
| Order Updates | `wss://ws-order-updates.indstocks.com/api/v1/ws/trades` | [08](08-websockets.md) |

## 7. Utility & System *(Coming Soon)*

| Endpoint | Method | Purpose | Docs |
|----------|--------|---------|------|
| `/option-chain` | GET | Option chain data | [13](13-utility.md) |
| `/option-chain-symbols` | GET | Available expiry dates | [13](13-utility.md) |
| `/greeks` | POST | Option greeks calculation | [13](13-utility.md) |
