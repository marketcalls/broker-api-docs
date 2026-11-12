# Backtesting

## Overview

Backtesting evaluates a trading strategy against past market data before you risk real capital. With Upstox APIs you can assemble everything a backtest needs — the correct instrument identifiers and historical OHLC candles for both equities and derivatives, including contracts that have already expired.

This guide ties together three building blocks:

| Step | API | Purpose |
| --- | --- | --- |
| Resolve instruments | [Instrument Search](https://upstox.com/developer/api-documentation/instrument-search) | Find the `instrument_key` and `trading_symbol` for an underlying, stock, or contract. |
| Discover expired contracts | [Get Expiries](https://upstox.com/developer/api-documentation/get-expiries) , [Get Expired Option Contracts](https://upstox.com/developer/api-documentation/get-expired-option-contracts) , [Get Expired Future Contracts](https://upstox.com/developer/api-documentation/get-expired-future-contracts) | List past expiry dates and the contracts that settled on them. |
| Fetch OHLC candles | [Historical Candle Data V3](https://upstox.com/developer/api-documentation/v3/get-historical-candle-data) , [Get Expired Historical Candle Data](https://upstox.com/developer/api-documentation/get-expired-historical-candle-data) | Retrieve open, high, low, close, volume, and open interest for active or expired instruments. |

The [Expired Instruments APIs](https://upstox.com/developer/api-documentation/expired-instruments) — Get Expiries, Get Expired Option/Future Contracts, and Get Expired Historical Candle Data — are available on the **Upstox Plus** plan. Instrument Search and Historical Candle Data V3 are available on all plans. See the [Help Center](https://upstox.com/help-center/my-account/plus-pack) for Plus details.

## Understanding instrument identifiers

Every backtest starts by resolving the instrument you want to test. Upstox uses three identifiers:

| Identifier | Example | Where it comes from |
| --- | --- | --- |
| `instrument_key` | `NSE_INDEX\|Nifty 50` , `NSE_EQ\|INE002A01018` , `NSE_FO\|53806` | Uniquely identifies an active instrument across all APIs. Returned by [Instrument Search](https://upstox.com/developer/api-documentation/instrument-search) . |
| `trading_symbol` | `Nifty 50` , `RELIANCE` , `RELIANCE FUT 30 MAR 26` | Human-readable symbol for display and lookup. Returned alongside `instrument_key` . |
| `expired_instrument_key` | `NSE_FO\|53806\|24-04-2025` | Identifies a contract that has already expired. Returned by [Get Expired Option Contracts](https://upstox.com/developer/api-documentation/get-expired-option-contracts) and [Get Expired Future Contracts](https://upstox.com/developer/api-documentation/get-expired-future-contracts) . |

Use [Instrument Search](https://upstox.com/developer/api-documentation/instrument-search) to convert a name or symbol into the exact `instrument_key` you need. For example, to find the underlying key for Reliance:

```bash
curl --location 'https://api.upstox.com/v2/instruments/search?query=RELIANCE&exchanges=NSE&segments=EQ&records=5' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {your_access_token}'
```

The response includes `instrument_key` ( `NSE_EQ|INE002A01018` ) and `trading_symbol` ( `RELIANCE` ), which you carry into the next step. See the [Instrument Search](https://upstox.com/developer/api-documentation/instrument-search#search-tips) page for reliable query patterns and filters.

## Backtest equities (cash segment)

For active equities and indices, resolve the key and pull candles directly — no expiry handling is needed.

### Step 1 — Resolve the instrument key

Search for the stock and read its `instrument_key` from the response:

```bash
curl --location 'https://api.upstox.com/v2/instruments/search?query=RELIANCE&exchanges=NSE&segments=EQ&records=5' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {your_access_token}'
```

### Step 2 — Fetch historical candles

Pass the key (URL-encoded) to [Historical Candle Data V3](https://upstox.com/developer/api-documentation/v3/get-historical-candle-data) with a `unit` , `interval` , and date range:

```bash
curl --location 'https://api.upstox.com/v3/historical-candle/NSE_EQ%7CINE002A01018/days/1/2025-03-04/2025-01-01' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {your_access_token}'
```

Historical Candle Data V3 supports `minutes` , `hours` , `days` , `weeks` , and `months` units, with daily data available from January 2000 and intraday from January 2022. Review the availability table on the [Historical Candle Data V3](https://upstox.com/developer/api-documentation/v3/get-historical-candle-data) page for the exact limits per unit.

## Backtest F&O (expired contracts)

Derivatives contracts expire, so a realistic F&O backtest needs the exact contract that traded during your test window. The flow adds two steps to discover expired contracts before fetching candles.

### Step 1 — Resolve the underlying instrument key

Find the `instrument_key` for the underlying index or stock. For an index:

```bash
curl --location 'https://api.upstox.com/v2/instruments/search?query=NIFTY&exchanges=NSE&segments=INDEX&records=5' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {your_access_token}'
```

This returns `NSE_INDEX|Nifty 50` for the Nifty 50 index. For stock derivatives, search the equity segment (as in the cash example) to get the underlying key such as `NSE_EQ|INE002A01018` .

### Step 2 — List available expiries

Pass the underlying key to [Get Expiries](https://upstox.com/developer/api-documentation/get-expiries) to retrieve every past expiry date for that underlying:

```bash
curl --location 'https://api.upstox.com/v2/expired-instruments/expiries?instrument_key=NSE_INDEX%7CNifty%2050' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {your_access_token}'
```

The response is a list of dates in `YYYY-MM-DD` format. Pick the expiry that covers your backtest window.

### Step 3 — Get the expired contracts

Use the underlying key and a chosen `expiry_date` to list the contracts that settled on that date. For options, call [Get Expired Option Contracts](https://upstox.com/developer/api-documentation/get-expired-option-contracts) :

```bash
curl --location 'https://api.upstox.com/v2/expired-instruments/option/contract?instrument_key=NSE_INDEX%7CNifty%2050&expiry_date=2025-04-24' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {your_access_token}'
```

For futures, call [Get Expired Future Contracts](https://upstox.com/developer/api-documentation/get-expired-future-contracts) with the same parameters. Each item in the response includes an `expired_instrument_key` (for example, `NSE_FO|53806|24-04-2025` ), along with the strike price, option type, and trading symbol. Select the contract you want to test and copy its `expired_instrument_key` .

### Step 4 — Fetch expired historical candles

Pass the `expired_instrument_key` (URL-encoded), an `interval` , and a date range to [Get Expired Historical Candle Data](https://upstox.com/developer/api-documentation/get-expired-historical-candle-data) :

```bash
curl --location 'https://api.upstox.com/v2/expired-instruments/historical-candle/NSE_FO%7C53806%7C24-04-2025/day/2025-04-24/2025-03-24' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {your_access_token}'
```

Each candle is an array of `[timestamp, open, high, low, close, volume, open_interest]` . Open interest is populated for derivatives, which lets you factor liquidity and positioning into your F&O backtests. See [Get Expired Historical Candle Data](https://upstox.com/developer/api-documentation/get-expired-historical-candle-data) for the supported intervals and per-interval history limits.

## Response format

All candle endpoints return the same OHLC array structure, so your backtesting engine can parse active and expired data with one code path:

```json
{
  "status": "success",
  "data": {
    "candles": [
      [
        "2025-04-24T00:00:00+05:30",
        125.35,
        126.8,
        122.1,
        123.45,
        1542678,
        184632
      ]
    ]
  }
}
```

| Index | Field | Description |
| --- | --- | --- |
| 0 | Timestamp | Start time of the candle. |
| 1 | Open | Opening price for the timeframe. |
| 2 | High | Highest traded price. |
| 3 | Low | Lowest traded price. |
| 4 | Close | Closing price for the timeframe. |
| 5 | Volume | Total quantity traded. |
| 6 | Open Interest | Outstanding derivative contracts ( `0` for cash instruments). |

## Best practices

- **Resolve keys once, then cache them.** Instrument and expiry lists change slowly. Store the keys you resolve so a long backtest does not re-query them on every run.
- **Respect interval history limits.** Finer intervals (such as `1minute` ) cover shorter windows than daily or weekly candles. Split long backtests into chunks that fit each interval's limit, and page through date ranges.
- **Handle rate limits.** Backtests can generate many requests. Follow the [rate limiting](https://upstox.com/developer/api-documentation/rate-limiting) guidelines and add retry/backoff logic. A
