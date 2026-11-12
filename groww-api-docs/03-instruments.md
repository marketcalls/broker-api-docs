# Instruments

> Source: https://groww.in/trade-api/docs/curl/instruments

Groww publishes instrument data as a CSV containing instruments in the CASH and FNO segments. The data identifies securities for use with Groww API operations. The documentation says prices in the instrument data are in rupees.

## Download

The documented CSV URL is:

```text
https://growwapi-assets.groww.in/instruments/instrument.csv
```

Download it with cURL:

```bash
curl -X GET 'https://growwapi-assets.groww.in/instruments/instrument.csv' -o instrument.csv
```

The file contains CASH equity stocks and indices (NSE, BSE) and FNO equity futures and options (NSE, BSE).

## CSV columns

| Column | Type in docs | Description |
|---|---|---|
| `exchange` | string | Exchange where the instrument is traded |
| `exchange_token` | string | Unique token assigned to the instrument by the exchange |
| `trading_symbol` | string | Trading symbol used to place orders |
| `groww_symbol` | string | Symbol Groww uses to identify the instrument |
| `name` | string | Instrument name |
| `instrument_type` | string | Instrument type; see [Annexures](https://groww.in/trade-api/docs/curl/annexures) |
| `segment` | string | Instrument segment, such as CASH or FNO |
| `series` | string | Instrument series, for example EQ, A, or B |
| `isin` | string | International Securities Identification Number |
| `underlying_symbol` | string | Derivative underlying symbol; empty for stocks and indices |
| `underlying_exchange_token` | string | Exchange token of the underlying asset |
| `expiry_date` | string | Derivative expiry date |
| `strike_price` | integer | Option strike price |
| `lot_size` | integer | Minimum lot size for the instrument |
| `tick_size` | decimal | Minimum price movement |
| `freeze_quantity` | integer | Quantity frozen for trading |
| `is_reserved` | boolean | Whether the instrument is reserved for trading |
| `buy_allowed` | boolean | Whether buying is allowed |
| `sell_allowed` | boolean | Whether selling is allowed |

## Instrument segments

| Segment | Instruments described by Groww |
|---|---|
| `CASH` | Equity stocks and indices (NSE, BSE) |
| `FNO` | Equity futures and options (NSE, BSE) |

## Price units

Groww explicitly states that all prices in the instrument CSV are in rupees.

## Official sources

- [Groww Instruments documentation](https://groww.in/trade-api/docs/curl/instruments)
- [Instrument CSV](https://growwapi-assets.groww.in/instruments/instrument.csv)
- [Groww API Annexures](https://groww.in/trade-api/docs/curl/annexures)
