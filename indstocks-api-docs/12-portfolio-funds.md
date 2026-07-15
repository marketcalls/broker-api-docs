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

Retrieves current equity holdings from the Demat account.

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
      "security_id": "12345",
      "trading_symbol": "RELIANCE-EQ",
      "exchange_segment": "NSE_EQ",
      "isin": "INE002A01018",
      "quantity": 50,
      "average_price": 2200.00,
      "last_traded_price": 2505.10,
      "close_price": 2495.00,
      "market_value": 125255.00,
      "pnl_absolute": 15255.00,
      "pnl_percent": 13.87
    }
  ]
}
```

| Field | Description |
|-------|-------------|
| `security_id` | Instrument identifier |
| `trading_symbol` | Exchange trading symbol |
| `exchange_segment` | Segment (e.g., `NSE_EQ`) |
| `isin` | ISIN of the holding |
| `quantity` | Held quantity |
| `average_price` | Average buy price |
| `last_traded_price` | Current market price |
| `close_price` | Previous close |
| `market_value` | Current market value of the holding |
| `pnl_absolute` | Absolute profit / loss |
| `pnl_percent` | Percentage profit / loss |

---

## Get Positions

Retrieves open positions including intraday trades and F&O positions.

**Endpoint:** `GET /portfolio/positions`

### Query Parameters

| Parameter | Type | Required | Details |
|-----------|------|----------|---------|
| `segment` | string | ✅ | `derivative` or `equity` |
| `product` | string | ✅ | Derivatives: `margin` / `intraday`; Equity: `cnc` / `intraday` |

### Request

```bash
# Derivative positions
curl --location 'https://api.indstocks.com/portfolio/positions?segment=derivative&product=margin' \
--header 'Authorization: YOUR_ACCESS_TOKEN'

# Equity positions
curl --location 'https://api.indstocks.com/portfolio/positions?segment=equity&product=cnc' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
  "status": "success",
  "data": {
    "net_positions": [
      {
        "security_id": "67890",
        "trading_symbol": "NIFTY25MAYFUT",
        "exchange_segment": "NSE_FNO",
        "net_quantity": 100,
        "average_price": 18500.00,
        "last_traded_price": 18550.50,
        "market_value": 1855050.00,
        "pnl_absolute": 5050.00,
        "multiplier": 50,
        "position_type": "open"
      }
    ],
    "day_positions": []
  }
}
```

| Field | Description |
|-------|-------------|
| `net_positions` | Net (carry-forward + day) positions |
| `day_positions` | Positions opened during the current day |
| `net_quantity` | Net position quantity |
| `average_price` | Average entry price |
| `last_traded_price` | Current market price |
| `market_value` | Current market value |
| `pnl_absolute` | Absolute profit / loss |
| `multiplier` | Contract multiplier / lot size |
| `position_type` | Position state (e.g., `open`) |

---

## Get Funds

Returns fund utilization and availability. See
[Authentication & Users](04-authentication-users.md#get-funds) for the full response schema.

**Endpoint:** `GET /funds`

```bash
curl --location 'https://api.indstocks.com/funds' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```
