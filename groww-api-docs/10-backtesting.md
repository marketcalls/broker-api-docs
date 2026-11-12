# Source: https://groww.in/trade-api/docs/curl/backtesting

# Backtesting Data

Backtesting APIs currently support `CASH` and `FNO`. Historical equity, index, and FNO data is available from 2020, according to Groww's documentation.

## Groww Symbol Format

The Groww symbol uniquely identifies an instrument. Stocks and indices use exchange and trading symbol (for example `NSE-WIPRO`). Futures add expiry and `FUT` (for example `NSE-NIFTY-30Sep25-FUT`). Options add expiry, strike, and option type (for example `NSE-NIFTY-30Sep25-24650-CE`). The instruments CSV/API provides Groww symbols.

## Get Expiries

`GET https://api.groww.in/v1/historical/expiries`

Required query parameters: `exchange`, `underlying_symbol`; optional `year` (2020 through current year) and `month` (1–12). If omitted, year defaults to current year and all year's expiries are returned.

```bash
curl -G 'https://api.groww.in/v1/historical/expiries' \
  --data-urlencode 'exchange=NSE' --data-urlencode 'underlying_symbol=NIFTY' \
  --data-urlencode 'year=2024' --data-urlencode 'month=1' \
  -H 'Accept: application/json' -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

Response: `payload.expiries`, an array of dates in `YYYY-MM-DD` format.

## Get Contracts

`GET https://api.groww.in/v1/historical/contracts`

Required query parameters: `exchange`, `underlying_symbol` (1–20 characters), and `expiry_date` (`YYYY-MM-DD`). Returns available derivative Groww symbols for that expiry.

```bash
curl -G 'https://api.groww.in/v1/historical/contracts' \
  --data-urlencode 'exchange=NSE' --data-urlencode 'underlying_symbol=NIFTY' \
  --data-urlencode 'expiry_date=2025-01-25' \
  -H 'Accept: application/json' -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

Response: `payload.contracts`, an array of contract Groww symbols.

## Get Historical Candle Data

`GET https://api.groww.in/v1/historical/candles`

Fetches historical OHLC candles; volume is available for tradable equities/FNO and open interest for FNO.

Required query parameters: `exchange`, `segment`, `groww_symbol`, `start_time`, `end_time`, and `candle_interval`. Times accept `yyyy-MM-dd HH:mm:ss` or epoch seconds. Intervals are listed in [Annexures](12-annexures.md#candle-interval).

```bash
curl -G 'https://api.groww.in/v1/historical/candles' \
  --data-urlencode 'exchange=NSE' --data-urlencode 'segment=CASH' \
  --data-urlencode 'groww_symbol=NSE-WIPRO' \
  --data-urlencode 'start_time=2025-09-24 10:56:00' \
  --data-urlencode 'end_time=2025-09-24 15:21:00' \
  --data-urlencode 'candle_interval=5minute' \
  -H 'Accept: application/json' -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

Each `payload.candles` row contains timestamp (`yyyy-MM-dd HH:mm:ss`), open, high, low, close, volume, and open interest (null for non-FNO instruments). All prices are rupees. Response also includes `closing_price`, `start_time`, `end_time`, and `interval_in_minutes`.

FNO workflow: request expiries, choose an expiry, request contracts for the underlying and expiry, then request candles using the selected contract's Groww symbol and `segment=FNO`.
