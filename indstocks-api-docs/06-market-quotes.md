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

- Up to **1,000 instruments** per request.

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
      "volume": 3546732
    }
  }
}
```

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

Returns the top 5 buy and sell levels (price, quantity, and order count per level) for each
requested instrument.
