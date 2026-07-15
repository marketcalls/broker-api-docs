# Mutual Funds API

Manage SIPs for funds on Zerodha's Coin platform. Purchases delivered to buyer's DEMAT account. Built on BSE STARMF platform.

**Limitation:** Dividend reinvestment not supported.

## Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/mf/orders` | All orders (last 7 days) |
| GET | `/mf/orders/:order_id` | Specific order (no age limit) |
| GET | `/mf/sips/` | All active SIPs |
| GET | `/mf/holdings` | MF holdings in DEMAT |
| GET | `/mf/instruments` | Master list of funds (gzipped CSV) |

## Order Fields

| Field | Description |
|-------|-------------|
| order_id | Unique identifier |
| status | COMPLETE, REJECTED, CANCELLED, OPEN |
| fund | Fund name |
| amount | Investment amount |
| tradingsymbol | Fund's ISIN |
| purchase_type | FRESH or ADDITIONAL |
| variety | regular, sip, amc_sip |

## SIP Fields

| Field | Description |
|-------|-------------|
| sip_id | Unique SIP identifier |
| status | ACTIVE, PAUSED, CANCELLED |
| frequency | Monthly, weekly, quarterly |
| instalment_amount | Investment per cycle |
| instalments | Total planned (-1 = indefinite) |
| pending_instalments | Remaining |
| next_instalment | Next execution date |
| step_up | % increase schedule |

## Holdings Fields

| Field | Description |
|-------|-------------|
| folio | AMC folio number |
| quantity | Units held |
| average_price | Cost basis NAV |
| last_price | Current NAV |
| pnl | Net P&L |

## Instrument CSV Columns

tradingsymbol (ISIN), amc, name, purchase_allowed, redemption_allowed, minimum_purchase_amount, purchase_amount_multiplier, dividend_type, scheme_type, plan, settlement_type, last_price, last_price_date
