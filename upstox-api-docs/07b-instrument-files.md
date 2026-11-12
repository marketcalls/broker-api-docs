# Instrument Files

## Overview

Upstox provides instrument files containing trading data across multiple asset classes and exchanges. Use `instrument_key` for unique identification. JSON format is recommended over deprecated CSV.

## BOD (Beginning of Day) Instruments - JSON

| Exchange | URL |
|----------|-----|
| Complete | `https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz` |
| NSE | `https://assets.upstox.com/market-quote/instruments/exchange/NSE.json.gz` |
| BSE | `https://assets.upstox.com/market-quote/instruments/exchange/BSE.json.gz` |
| MCX | `https://assets.upstox.com/market-quote/instruments/exchange/MCX.json.gz` |

## Specialized Instrument Lists

| Type | URL |
|------|-----|
| Suspended | `https://assets.upstox.com/market-quote/instruments/exchange/suspended-instrument.json.gz` |
| MTF | `https://assets.upstox.com/market-quote/instruments/exchange/MTF.json.gz` |
| MIS (NSE) | `https://assets.upstox.com/market-quote/instruments/exchange/NSE_MIS.json.gz` |
| MIS (BSE) | `https://assets.upstox.com/market-quote/instruments/exchange/BSE_MIS.json.gz` |
| Global | `https://assets.upstox.com/market-quote/instruments/exchange/global.json.gz` |

### Global Instruments

Added 11 May 2026. Provides instrument keys for global indices and economic indicators, usable with the existing market quote and historical candle APIs.

| Segment | Description | Examples |
|---------|-------------|----------|
| `GLOBAL_INDEX` | Global stock market indices | GIFT NIFTY, DOW JONES, S&P, FTSE 100, HANG SENG, DAX, NIKKEI 225, US Tech 100, CAC 40, US 30 |
| `GLOBAL_INDICATOR` | Economic and commodity indicators | USD INR, Oil (Brent), Oil (WTI) |

Fields: `segment`, `name`, `exchange` (always `GLOBAL`), `country`, `latency` (`20 Seconds`, `120 Seconds`, `900 Seconds`), `instrument_key` (`<segment>|<trading_symbol>`), `trading_symbol`, `start_time`, `end_time`, `week_days`, `weekly`, `mtf_enabled`.

## JSON Object Structure

### Equity (EQ) Fields
`segment`, `name`, `exchange`, `isin`, `instrument_type`, `instrument_key`, `lot_size`, `freeze_quantity`, `exchange_token`, `tick_size`, `trading_symbol`, `short_name`, `security_type`

`cas_eligible` (boolean, added 3 August 2026) marks securities that participate in the exchange Closing Auction Session. Read it dynamically rather than hardcoding a static list.

### Futures Fields
`weekly`, `segment`, `name`, `exchange`, `expiry`, `instrument_type`, `underlying_symbol`, `instrument_key`, `lot_size`, `freeze_quantity`, `exchange_token`, `minimum_lot`, `underlying_key`, `tick_size`, `underlying_type`, `trading_symbol`

### Options Fields
All futures fields plus `strike_price`

### Index Fields
`segment`, `name`, `exchange`, `instrument_type`, `instrument_key`, `exchange_token`, `trading_symbol`

## Update Schedule

Files refresh daily around 6 AM and selectively during trading hours. BOD instruments exclude delisted stocks and expired contracts.

## Key Recommendations

- Use `instrument_key` for unique identification (remains unique per instrument)
- Use JSON format over CSV (better structure, future scalability)
