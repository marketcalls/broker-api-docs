# Portfolio API

## Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/portfolio/holdings` | Long-term equity holdings |
| GET | `/portfolio/positions` | Short-term positions |
| PUT | `/portfolio/positions` | Convert position product |
| GET | `/portfolio/holdings/auctions` | Active auctions |
| POST | `/portfolio/holdings/authorise` | Initiate CDSL authorisation |

## Holdings

Equity delivery stocks in user's DEMAT account. Remain indefinitely until sold.

### Key Response Fields

| Field | Type | Description |
|-------|------|-------------|
| tradingsymbol | string | Trading symbol |
| exchange | string | Exchange |
| isin | string | ISIN code |
| quantity | int | Total quantity |
| t1_quantity | int | T+1 quantity |
| average_price | float | Acquisition price |
| last_price | float | Current price |
| close_price | float | Previous close |
| pnl | float | Profit/Loss |
| day_change | float | Day change value |
| day_change_percentage | float | Day change % |
| collateral_quantity | int | Pledged quantity |
| collateral_type | string | Collateral type |
| authorised_quantity | int | CDSL authorised qty |

## Positions

Short-to-medium-term derivatives and intraday equity. Returns `net` (current) and `day` (daily snapshot) sets.

### Key Response Fields

| Field | Type | Description |
|-------|------|-------------|
| tradingsymbol | string | Symbol |
| exchange | string | Exchange |
| product | string | CNC, NRML, MIS |
| quantity | int | Net quantity |
| overnight_quantity | int | Carried forward |
| buy_quantity | int | Total bought |
| sell_quantity | int | Total sold |
| average_price | float | Net average price |
| last_price | float | Current price |
| pnl | float | Net P&L |
| m2m | float | Mark to market |
| unrealised | float | Unrealised P&L |
| realised | float | Realised P&L |
| multiplier | int | Lot multiplier |

## Position Conversion

**PUT** `/portfolio/positions`

| Parameter | Description |
|-----------|-------------|
| tradingsymbol | Instrument symbol |
| exchange | Exchange |
| transaction_type | BUY or SELL |
| position_type | `overnight` or `day` |
| quantity | Quantity to convert |
| old_product | Current product |
| new_product | Target product |

## Holdings Authorisation

**POST** `/portfolio/holdings/authorise`

Returns `request_id` for redirect to:
`https://kite.zerodha.com/connect/portfolio/authorise/holdings/:api_key/:request_id`

Authorisations valid for single trading session (until 5:30 PM).

## Exiting

No special API calls. Place opposite BUY/SELL orders with matching product types.
