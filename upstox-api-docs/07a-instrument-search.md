# Instrument Search API

## Overview

Search instruments by name, symbol, or contract specifications across multiple exchanges and segments with pagination and filtering.

## Endpoint

**GET** `https://api.upstox.com/v2/instruments/search`

## Query Parameters

| Parameter | Type | Required | Details |
|-----------|------|----------|---------|
| query | string | Yes | Free text search, max 50 characters |
| exchanges | string | No | `ALL`, `NSE`, `BSE`, `MCX` (default: ALL) |
| segments | string | No | `ALL`, `EQ`, `FO`, `CURR`, `COMM`, `INDEX`, `OPT`, `FUT` |
| instrument_types | string | No | `CE`, `PE`, `A`, `X`, etc. |
| expiry | string | No | Keywords (`current_week`, `next_month`) or `yyyy-MM-dd` |
| atm_offset | integer | No | Distance from ATM strike (0=ATM, positive=above, negative=below) |
| page_number | integer | No | Starts from 1 (default: 1) |
| records | integer | No | Per-page limit (default: 10, max: 30) |

## Response Fields by Type

**Equity (EQ):** name, segment, exchange, ISIN, instrument_key, exchange_token, trading_symbol, short_name, tick_size, lot_size, instrument_type, freeze_quantity, qty_multiplier, security_type

**Futures/Options:** Adds expiry, weekly flag, underlying_key, underlying_type, underlying_symbol, strike_price, minimum_lot

**Indices:** name, segment, exchange, instrument_key, exchange_token, trading_symbol, instrument_type

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1169 | Empty query |
| UDAPI1170 | Query exceeds 50 characters |
| UDAPI1171 | Invalid exchange values |
| UDAPI1172 | Invalid segment values |
| UDAPI1173 | Records exceed 30 limit |
| UDAPI1174 | Invalid page number |
| UDAPI1175 | Invalid expiry format |

## cURL Example

```bash
curl 'https://api.upstox.com/v2/instruments/search?query=RELIANCE&exchanges=NSE&segments=FO&instrument_types=CE,PE&expiry=current_month&atm_offset=0&page_number=1&records=20' \
  --header 'Authorization: Bearer {your_access_token}'
```
