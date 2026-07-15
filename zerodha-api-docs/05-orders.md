# Orders API

## Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/orders/:variety` | Place order |
| PUT | `/orders/:variety/:order_id` | Modify pending order |
| DELETE | `/orders/:variety/:order_id` | Cancel pending order |
| GET | `/orders` | Retrieve all daily orders |
| GET | `/orders/:order_id` | Retrieve order history |
| GET | `/trades` | Retrieve all daily trades |
| GET | `/orders/:order_id/trades` | Retrieve order's trades |

## Order Varieties

| Variety | Description |
|---------|-------------|
| `regular` | Standard orders |
| `amo` | After Market Orders |
| `co` | Cover Orders |
| `iceberg` | Iceberg Orders |
| `auction` | Auction Orders |

## Order Types

| Type | Description |
|------|-------------|
| `MARKET` | Execute at market price |
| `LIMIT` | Execute at specified price |
| `SL` | Stop Loss order |
| `SL-M` | Stop Loss Market order |

## Product Types

| Product | Description |
|---------|-------------|
| `CNC` | Cash & Carry (equity delivery) |
| `NRML` | Normal (futures/options) |
| `MIS` | Margin Intraday Squareoff |
| `MTF` | Margin Trading Facility |

## Order Validity

| Validity | Description |
|----------|-------------|
| `DAY` | Valid for trading day |
| `IOC` | Immediate or Cancel |
| `TTL` | Time-to-Live (specify minutes via `validity_ttl`) |

## Place Order - Parameters

### Required

| Parameter | Description |
|-----------|-------------|
| `tradingsymbol` | Instrument identifier |
| `exchange` | NSE, BSE, NFO, CDS, BCD, MCX |
| `transaction_type` | BUY or SELL |
| `order_type` | MARKET, LIMIT, SL, SL-M |
| `quantity` | Units to trade |
| `product` | Margin product type |
| `price` | Required for LIMIT orders |
| `trigger_price` | For SL/SL-M orders |
| `validity` | Order validity period |

### Optional

| Parameter | Description |
|-----------|-------------|
| `disclosed_quantity` | Public quantity on exchange |
| `validity_ttl` | Minutes for TTL validity |
| `iceberg_legs` | Number of legs (2-50) |
| `iceberg_quantity` | Quantity per leg |
| `auction_number` | Auction identifier |
| `market_protection` | 0 (none), 1-100 (%), -1 (auto) |
| `autoslice` | true/false for auto-slicing |
| `tag` | Alphanumeric identifier (max 20 chars) |

## Market Protection

Limits price deviation for MARKET and SL-M orders:
- `0` - No protection (default)
- `1-100` - Custom percentage threshold
- `-1` - Automatic system protection

## Order Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `order_id` | string | Unique identifier |
| `exchange_order_id` | string | Exchange identifier |
| `status` | string | OPEN, COMPLETE, REJECTED, CANCELLED |
| `filled_quantity` | int | Executed units |
| `pending_quantity` | int | Awaiting execution |
| `average_price` | float | Execution price |
| `order_timestamp` | string | Placement time |
| `exchange_timestamp` | string | Exchange registration time |

## Order Statuses (Transient)

- `PUT ORDER REQ RECEIVED` - Backend acknowledgment
- `VALIDATION PENDING` - RMS validation
- `OPEN PENDING` - Awaiting exchange registration
- `MODIFY VALIDATION PENDING` - Modification validation
- `MODIFY PENDING` - Modification registration
- `TRIGGER PENDING` - Awaiting trigger execution
- `CANCEL PENDING` - Cancellation pending

## Auto Slicing

When `autoslice=true`, orders exceeding freeze limits automatically split into max 50 slices. Each slice receives unique `order_id` with parent relationship tags.

## Trade Fields

| Field | Type | Description |
|-------|------|-------------|
| `trade_id` | string | Exchange identifier |
| `order_id` | string | Associated order |
| `average_price` | float | Fill price |
| `quantity` | int | Filled amount |
| `fill_timestamp` | string | Execution timestamp |
