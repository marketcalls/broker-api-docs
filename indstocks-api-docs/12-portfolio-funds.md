# Portfolio & Funds

> Source: https://api-docs.indstocks.com/portfolio_funds/

Retrieve equity holdings, open positions, and available funds.

## Endpoints Overview

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/portfolio/holdings` | Equity holdings in the Demat account |
| GET | `/portfolio/positions` | Open intraday and F&O positions |
| GET | `/funds` | Available and utilized funds |

---

## Get Holdings

Retrieves the user's current equity holdings (stocks held in their Demat account).

**Endpoint:** `GET /portfolio/holdings`

### Request

```bash
curl --location 'https://api.indstocks.com/portfolio/holdings' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
    "status": "success",
    "data": [
        {
            "security_id": "18520",
            "symbol": "CUPID",
            "isin": "INE509F01029",
            "total_qty": 1,
            "used_qty": 0,
            "avg_price": 217.3,
            "t1_qty": 1,
            "t1_avg_price": 217.3,
            "dp_qty": 0,
            "dp_avg_price": 0
        }
    ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `security_id` | string | The unique identifier for the instrument |
| `symbol` | string | The trading symbol for the instrument |
| `isin` | string | The ISIN of the instrument |
| `total_qty` | number | Total quantity held (T1 + DP holdings) |
| `used_qty` | number | Quantity currently pledged, sold, or otherwise blocked |
| `avg_price` | number | Average buy price across `total_qty` |
| `t1_qty` | number | Quantity settled T1 (not yet moved to the Demat/DP account) |
| `t1_avg_price` | number | Average price for the `t1_qty` portion |
| `dp_qty` | number | Quantity already settled into the Demat (DP) account |
| `dp_avg_price` | number | Average price for the `dp_qty` portion |

> Holdings do **not** include live price or P&L fields. Fetch the current price separately via
> [Market Quotes](06-market-quotes.md) using `security_id`.

---

## Get Positions

Retrieves open positions including intraday trades and F&O positions.

**Endpoint:** `GET /portfolio/positions`

### Query Parameters

| Parameter | Type | Required | Details |
|-----------|------|----------|---------|
| `segment` | string | ✅ | `derivative` or `equity` (lowercase) |
| `product` | string | ✅ | Derivatives: `margin` / `intraday`; Equity: `cnc` / `intraday` (lowercase) |

> Note the casing: portfolio queries take **lowercase** `segment` / `product`, whereas order
> endpoints take **uppercase**. See [Glossary & Constants](16-glossary.md#core-request-enums).

### Request

```bash
# Derivative positions
curl --location 'https://api.indstocks.com/portfolio/positions?segment=derivative&product=margin' \
--header 'Authorization: YOUR_ACCESS_TOKEN'

# Equity positions
curl --location 'https://api.indstocks.com/portfolio/positions?segment=equity&product=cnc' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response — Derivative

```json
{
    "status": "success",
    "data": [
        {
            "position_id": "535654528",
            "security_id": "823580",
            "symbol": "SENSEX",
            "segment": "DERIVATIVE",
            "product": "MARGIN",
            "exchange": "",
            "drv_instrument": "OPTIDX",
            "drv_expiry_date": "07/16/2026 14:00",
            "drv_option_type": "CE",
            "drv_strike_price": 82000,
            "net_qty": 0,
            "avg_price": 1.2,
            "buy_qty": 20,
            "buy_avg": 1.25,
            "sell_qty": 20,
            "sell_avg": 1.2,
            "realized_profit": -1.0,
            "day_buy_qty": null,
            "day_buy_val": null,
            "day_sell_qty": null,
            "day_sell_val": null,
            "cf_buy_qty": null,
            "cf_buy_val": null,
            "cf_sell_qty": null,
            "cf_sell_val": null
        }
    ]
}
```

### Response — Equity

```json
{
    "status": "success",
    "data": [
        {
            "position_id": "86016462",
            "security_id": "1521",
            "symbol": "INDIAGLYCO",
            "segment": "EQUITY",
            "product": "INTRADAY",
            "exchange": "NSE",
            "isin": "INE560A01023",
            "drv_instrument": "",
            "net_qty": 0,
            "avg_price": 1146.85,
            "buy_qty": 1,
            "buy_avg": 1149.4,
            "sell_qty": 1,
            "sell_avg": 1146.85,
            "realized_profit": -2.55,
            "day_buy_qty": 1,
            "day_buy_val": 1149.4,
            "day_sell_qty": 1,
            "day_sell_val": 1146.85,
            "cf_buy_qty": null,
            "cf_buy_val": null,
            "cf_sell_qty": null,
            "cf_sell_val": null
        }
    ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `position_id` | string | Unique identifier for this position |
| `security_id` | string | The unique identifier for the instrument |
| `symbol` | string | The trading symbol for the instrument |
| `segment` | string | `EQUITY` or `DERIVATIVE` |
| `product` | string | `MARGIN`, `INTRADAY`, or `CNC`, matching the `product` query parameter |
| `exchange` | string | `NSE` / `BSE`. **May be empty** for some derivative index positions |
| `isin` | string | ISIN of the instrument (equity positions only) |
| `drv_instrument` | string | Derivative instrument type (e.g. `OPTIDX`, `FUTSTK`). Empty for equity |
| `drv_expiry_date` | string | Expiry date/time for derivative contracts (e.g. `07/16/2026 14:00`) |
| `drv_option_type` | string | `CE` or `PE` for options. Absent for futures/equity |
| `drv_strike_price` | number | Strike price for options. Absent for futures/equity |
| `net_qty` | number | Net open quantity (buy − sell) |
| `avg_price` | number | Average price of the net open quantity |
| `buy_qty` / `buy_avg` | number | Total bought quantity and its average price |
| `sell_qty` / `sell_avg` | number | Total sold quantity and its average price |
| `realized_profit` | number | Realized P&L for this position so far today |
| `day_buy_qty` / `day_buy_val` | number \| null | Same-day buy quantity/value. `null` where not applicable |
| `day_sell_qty` / `day_sell_val` | number \| null | Same-day sell quantity/value. `null` where not applicable |
| `cf_buy_qty` / `cf_buy_val` | number \| null | Carried-forward buy quantity/value. `null` where not applicable |
| `cf_sell_qty` / `cf_sell_val` | number \| null | Carried-forward sell quantity/value. `null` where not applicable |

> `data` is a **flat array** of positions — there is no `net_positions` / `day_positions`
> grouping. Day vs carry-forward is expressed by the `day_*` and `cf_*` fields on each row,
> which are `null` (not `0`) when they don't apply.

> Positions carry no live price or unrealized-P&L field. Only `realized_profit` is returned;
> compute MTM yourself from `avg_price`, `net_qty`, and a quote.

---

## Get Funds

Returns fund utilization and availability. See
[Authentication & Users](04-authentication-users.md#get-funds) for the full response schema.

**Endpoint:** `GET /funds`

```bash
curl --location 'https://api.indstocks.com/funds' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```
