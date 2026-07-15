# Margin Calculation

All margin endpoints require `Content-Type: application/json` and JSON POST format.

## Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/margins/orders` | Per-order margins with positions |
| POST | `/margins/basket` | Spread order margins |
| POST | `/charges/orders` | Order-wise charges breakdown |

## Order Margins

**POST** `/margins/orders`

### Request Parameters

| Parameter | Description |
|-----------|-------------|
| exchange | Exchange name |
| tradingsymbol | Instrument symbol |
| transaction_type | BUY or SELL |
| variety | regular, amo, co |
| product | CNC, MIS, NRML |
| order_type | MARKET, LIMIT, etc. |
| quantity | Order quantity |
| price | Limit price (0 for market) |
| trigger_price | SL/CO trigger |

### Response Fields

- `span`, `exposure`, `option_premium`, `additional`, `bo`, `cash`, `var` - margin components
- `pnl` - realised and unrealised P&L
- `leverage` - allowed margin leverage
- `charges` - detailed cost breakdown
- `total` - total margin block

### Charges Breakdown

| Field | Description |
|-------|-------------|
| transaction_tax | Exchange transaction tax |
| exchange_turnover_charge | Daily turnover charge |
| sebi_turnover_charge | SEBI regulatory charge |
| brokerage | Trading brokerage |
| stamp_duty | Government stamp duty |
| gst | GST (IGST/CGST/SGST) |
| total | Sum of all charges |

**Query:** `mode=compact` returns only total margins.

## Basket Margins

**POST** `/margins/basket`

Query params: `consider_positions` (boolean), `mode` (`compact`)

Returns: `initial` margins, `final` margins (after spread benefit), per-order details, and charges.

## Virtual Contract Note

**POST** `/charges/orders`

Detailed charges for executed orders. Requires `average_price` (non-zero).
