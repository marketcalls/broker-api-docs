# Market Quotes

> Source: https://api-docs.indstocks.com/MarketQuote/

Real-time market quotes come in three flavors — a full snapshot, a lightweight LTP, and a
5-level market depth. All three accept the same `scrip-codes` parameter and require the
`Authorization` header.

## Instrument Format

Instruments are identified as `SEGMENT_TOKEN`, comma-separated for multiple instruments:

```
NSE_3045,NFO_51011
```

- `/market/quotes/full` and `/market/quotes/ltp`: up to **1,000 instruments** per request.
- `/market/quotes/mkt`: one or more instruments (no documented cap).

---

## Full Market Quote

Returns a comprehensive snapshot including OHLC, day change, volume, circuit limits, 52-week
range, and market depth.

**Endpoint:** `GET /market/quotes/full`

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `scrip-codes` | string | ✅ | Comma-separated `SEGMENT_TOKEN` identifiers |

### Request

```bash
curl --location 'https://api.indstocks.com/market/quotes/full?scrip-codes=NSE_3045' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
  "status": "success",
  "data": {
    "NSE_3045": {
      "live_price": 788.8,
      "day_change": -3.5,
      "day_change_percentage": -0.44,
      "day_low": 788.35,
      "day_high": 795.5,
      "day_open": 792.5,
      "prev_close": 792.3,
      "52week_high": 899,
      "52week_low": 680,
      "upper_circuit": 871.5,
      "lower_circuit": 713.1,
      "market_depth": { "aggregate": { }, "depth": [ ] },
      "volume": 3546732
    }
  }
}
```

The full quote embeds the same `market_depth` object documented under
[Market Depth](#market-depth) below.

---

## LTP Quote

A lightweight alternative to the full quote that returns only the last traded price.

**Endpoint:** `GET /market/quotes/ltp`

### Request

```bash
curl --location 'https://api.indstocks.com/market/quotes/ltp?scrip-codes=NSE_3045' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
  "status": "success",
  "data": {
    "NSE_3045": {
      "live_price": 792.5
    }
  }
}
```

---

## Market Depth

Retrieves 5-level market depth (bid/ask book) for one or more instruments.

**Endpoint:** `GET /market/quotes/mkt`

### Request

```bash
curl --location 'https://api.indstocks.com/market/quotes/mkt?scrip-codes=NSE_3045' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
  "status": "success",
  "data": {
    "NSE_3045": {
      "market_depth": {
        "aggregate": {
          "total_buy": "5,82,909",
          "total_sell": "11,01,938",
          "buy_percentage": 34.6,
          "sell_percentage": 65.4
        },
        "depth": [
          { "buy": { "quantity": "6.00", "price": "788.95" }, "sell": { "quantity": "21.00", "price": "789.00" } },
          { "buy": { "quantity": "756.00", "price": "788.70" }, "sell": { "quantity": "255.00", "price": "789.05" } },
          { "buy": { "quantity": "456.00", "price": "788.65" }, "sell": { "quantity": "264.00", "price": "789.10" } },
          { "buy": { "quantity": "2,318", "price": "788.60" }, "sell": { "quantity": "1,792", "price": "789.15" } },
          { "buy": { "quantity": "1,644", "price": "788.55" }, "sell": { "quantity": "1,328", "price": "789.20" } }
        ]
      }
    }
  }
}
```

| Field | Description |
|-------|-------------|
| `aggregate.total_buy` / `total_sell` | Total bid / ask quantity across the book |
| `aggregate.buy_percentage` / `sell_percentage` | Buy vs sell distribution |
| `depth[]` | Top 5 levels; each entry has a `buy` and a `sell` side with `quantity` and `price` |

> ⚠️ **Depth quantities and prices are strings, not numbers**, and are **locale-formatted with
> Indian-grouping commas** (`"5,82,909"`, `"2,318"`). Some values also carry decimals
> (`"6.00"`). Strip commas before parsing to a number. There is **no order-count field** per
> level.
