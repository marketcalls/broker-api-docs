# Kite Connect 3 API Endpoints Quick Reference

## Base URL

`https://api.kite.trade`

## Authentication

All requests: `Authorization: token api_key:access_token`
Version header: `X-Kite-Version: 3`

---

## Session / User

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/session/token` | Exchange request_token for access_token |
| DELETE | `/session/token` | Logout |
| GET | `/user/profile` | User profile |
| GET | `/user/margins` | All margins |
| GET | `/user/margins/:segment` | Segment margins (equity/commodity) |

## Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/orders/:variety` | Place order |
| PUT | `/orders/:variety/:order_id` | Modify order |
| DELETE | `/orders/:variety/:order_id` | Cancel order |
| GET | `/orders` | All orders for day |
| GET | `/orders/:order_id` | Order history |
| GET | `/trades` | All trades for day |
| GET | `/orders/:order_id/trades` | Trades for order |

## GTT

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/gtt/triggers` | Create GTT |
| GET | `/gtt/triggers` | List all GTTs |
| GET | `/gtt/triggers/:id` | Get GTT details |
| PUT | `/gtt/triggers/:id` | Modify GTT |
| DELETE | `/gtt/triggers/:id` | Delete GTT |

## Alerts

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/alerts` | Create alert |
| GET | `/alerts` | List alerts |
| GET | `/alerts/{uuid}` | Get alert |
| PUT | `/alerts/{uuid}` | Modify alert |
| DELETE | `/alerts?uuid={uuid}` | Delete alert(s) |

## Portfolio

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/portfolio/holdings` | Holdings |
| GET | `/portfolio/positions` | Positions |
| PUT | `/portfolio/positions` | Convert position |
| GET | `/portfolio/holdings/auctions` | Auctions |
| POST | `/portfolio/holdings/authorise` | CDSL authorisation |

## Market Data

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/instruments` | All instruments (CSV) |
| GET | `/instruments/:exchange` | Exchange instruments (CSV) |
| GET | `/quote?i=EXCHANGE:SYMBOL` | Full quotes (max 500) |
| GET | `/quote/ohlc?i=EXCHANGE:SYMBOL` | OHLC (max 1000) |
| GET | `/quote/ltp?i=EXCHANGE:SYMBOL` | LTP (max 1000) |

## Historical

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/instruments/historical/:token/:interval` | Candle data |

## Mutual Funds

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/mf/orders` | MF orders (7 days) |
| GET | `/mf/orders/:order_id` | Specific MF order |
| GET | `/mf/sips/` | Active SIPs |
| GET | `/mf/holdings` | MF holdings |
| GET | `/mf/instruments` | MF instrument list (CSV) |

## Margins & Charges

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/margins/orders` | Order margins |
| POST | `/margins/basket` | Basket/spread margins |
| POST | `/charges/orders` | Virtual contract note |

## WebSocket

**Endpoint:** `wss://ws.kite.trade?api_key=xxx&access_token=xxx`

- Up to 3000 instruments per connection
- Up to 3 concurrent connections per API key
- Modes: `ltp` (8B), `quote` (44B), `full` (184B)

## Exchanges

NSE, BSE, NFO, CDS, BCD, MCX, MF

## Products

| Code | Description |
|------|-------------|
| CNC | Cash & Carry (delivery) |
| NRML | Normal (F&O) |
| MIS | Margin Intraday |
| MTF | Margin Trading Facility |

## Order Types

MARKET, LIMIT, SL, SL-M

## Varieties

regular, amo, co, iceberg, auction

## Rate Limits

| Endpoint | Limit |
|----------|-------|
| Quote | 1/sec |
| Historical | 3/sec |
| Orders | 10/sec |
| Others | 10/sec |
| Orders/minute | 400 |
| Orders/day | 5,000 |
