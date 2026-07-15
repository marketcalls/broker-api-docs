# Upstox API Endpoints Quick Reference

## Base URLs
- **Standard API:** `https://api.upstox.com/v2/` or `https://api.upstox.com/v3/`
- **HFT API (Orders):** `https://api-hft.upstox.com/v2/` or `https://api-hft.upstox.com/v3/`

## Authentication
All endpoints require: `Authorization: Bearer {access_token}`

---

## Login & Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v2/login/authorization/dialog` | Initiate OAuth flow |
| POST | `/v2/login/authorization/token` | Exchange code for token |
| POST | `/v3/login/auth/token/request/{client_id}` | Request token via webhook |
| DELETE | `/v2/logout` | Logout / invalidate token |

## User

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v2/user/profile` | Get user profile |
| GET | `/v2/user/get-funds-and-margin` | Get funds and margin |

## Charges & Margins

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v2/charges/brokerage` | Calculate brokerage |
| POST | `/v2/charges/margin` | Calculate margin (max 20 instruments) |

## Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v3/order/place` | Place order (V3, current) |
| POST | `/v2/order/place` | Place order (V2, deprecated) |
| POST | `/v2/order/multi/place` | Place multi order (max 10) |
| PUT | `/v3/order/modify` | Modify order (V3) |
| PUT | `/v2/order/modify` | Modify order (V2, deprecated) |
| DELETE | `/v3/order/cancel` | Cancel order (V3) |
| DELETE | `/v2/order/cancel` | Cancel order (V2, deprecated) |
| DELETE | `/v2/order/multi/cancel` | Cancel multi order |
| POST | `/v2/order/positions/exit` | Exit all positions |
| GET | `/v2/order/details` | Get order details |
| GET | `/v2/order/history` | Get order history |
| GET | `/v2/order/retrieve-all` | Get order book |
| GET | `/v2/order/trades/get-trades-for-day` | Get trades for day |
| GET | `/v2/order/trades?order_id={id}` | Get order trades |

## GTT Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v3/order/gtt/place` | Place GTT order |
| PUT | `/v3/order/gtt/modify` | Modify GTT order |
| DELETE | `/v3/order/gtt/cancel` | Cancel GTT order |
| GET | `/v3/order/gtt` | Get GTT order details |

## Portfolio

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v2/portfolio/short-term-positions` | Get positions |
| GET | `/v3/portfolio/mtf-positions` | Get MTF positions |
| PUT | `/v2/portfolio/convert-position` | Convert position |
| GET | `/v2/portfolio/long-term-holdings` | Get holdings |

## Trade P&L

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v2/trade/profit-loss/metadata` | P&L report metadata |
| GET | `/v2/trade/profit-loss/data` | P&L report data |

## Historical Data

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v3/historical-candle/{key}/{unit}/{interval}/{to}/{from}` | Historical candle V3 |
| GET | `/v3/historical-candle/intraday/{key}/{unit}/{interval}` | Intraday candle V3 |
| GET | `/v2/historical-candle/{key}/{interval}/{to}/{from}` | Historical candle (deprecated) |
| GET | `/v2/historical-candle/intraday/{key}/{interval}` | Intraday candle (deprecated) |

## Market Quotes

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v2/market-quote/quotes` | Full market quotes (max 500) |
| GET | `/v3/market-quote/ohlc` | OHLC quotes V3 |
| GET | `/v3/market-quote/ltp` | LTP quotes V3 |
| GET | `/v3/market-quote/option-greek` | Option Greeks (max 50) |
| GET | `/v2/market-quote/ohlc` | OHLC quotes (deprecated) |
| GET | `/v2/market-quote/ltp` | LTP quotes (deprecated) |

## Market Information

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v2/market/holidays` | Market holidays |
| GET | `/v2/market/timings/{date}` | Market timings |
| GET | `/v2/market/status/{exchange}` | Exchange status |

## Option Chain

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v2/option/contract` | Option contracts |
| GET | `/v2/option/chain` | Put/Call option chain |

## Instruments

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v2/instruments/search` | Search instruments |

## Expired Instruments

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v2/expired-instruments/expiries` | Get expiries |
| GET | `/v2/expired-instruments/option/contract` | Expired option contracts |
| GET | `/v2/expired-instruments/future/contract` | Expired future contracts |
| GET | `/v2/expired-instruments/historical-candle/{key}/{interval}/{to}/{from}` | Expired candle data |

## WebSocket

| Type | Description |
|------|-------------|
| Market Data Feed V3 | Real-time price updates |
| Portfolio Stream Feed | Order and position updates |

## Exchanges Supported

NSE, BSE, NFO, MCX, CDS, BFO, BCD, NSCOM

## Products

| Code | Meaning |
|------|---------|
| I | Intraday |
| D | Delivery |
| CO | Cover Order |
| MTF | Margin Trade Funding |

## Order Types

| Code | Meaning |
|------|---------|
| MARKET | Market order |
| LIMIT | Limit order |
| SL | Stop-Loss Limit |
| SL-M | Stop-Loss Market |
