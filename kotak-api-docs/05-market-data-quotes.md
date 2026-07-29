# Market Data — Quotes

## 1. Introduction

The Quotes API retrieves live and last-traded market data for one or more instruments (including stocks, ETFs, and indices) from supported exchanges. It supports advanced filters to fetch specific market values including depth, OHLC, circuit limits, and more.

## 2. API Endpoint

```
GET <Base URL>/script-details/1.0/quotes/neosymbol/<query>[,<query>][/<filter_name>]
```

Replace `<Base URL>` with the relevant Kotak environment base URL provided in the response from the `/tradeApiValidate` API.

Key points about endpoint structure:

- `<query>` is formatted as `<exchange_segment>|<instrument>`.
- Multiple queries are separated by commas, e.g. `nse_cm|Nifty 50,bse_cm|SENSEX`.
- Instrument (except indices): use `pSymbol` from the instrument/scrip master file.
- Indices: use the exact case-sensitive name (e.g. `Nifty 50`, `BANKEX`). See the full list at the bottom.

Expected values for `exchange_segment` (string):

- `nse_cm` (NSE Cash)
- `bse_cm` (BSE Cash)
- `nse_fo` (NSE F&O)
- `bse_fo` (BSE F&O)
- `cde_fo` (CDS F&O)

## 3. Headers

| Name | Type | Description |
| --- | --- | --- |
| Authorization | string | Token provided in your NEO API dashboard — use plain token |
| Content-Type | string | `application/json` |

## 4. Request

```bash
curl --location --request GET '<Base URL>/script-details/1.0/quotes/neosymbol/nse_cm|Nifty 50,nse_cm|Nifty Bank/all' \
--header 'Content-Type: application/json' \
--header 'Authorization: xxxxx-your-api-token-xxxx'
```

### Filter Options

After all queries, you may append a filter with `/filter_name`. Allowed values (8 total, including default `all`):

- `all` (default, returns all fields)
- `52W` (52-week high/low)
- `scrip_details` (scrip basics)
- `circuit_limits` (circuit limits)
- `ohlc` (Open, High, Low, Close)
- `oi` (open interest, if applicable)
- `depth` (order book, top 5 each side)
- `ltp` (last traded price)

## 5. Response

Example Success Response:

```json
[
  {
    "exchange_token": "SENSEX",
    "display_symbol": "SENSEX-IN",
    "exchange": "bse_cm",
    "lstup_time": "1757915078",
    "ltp": "81809.3400",
    "last_traded_quantity": "0",
    "total_buy": "0",
    "total_sell": "0",
    "last_volume": "0",
    "change": "-95.3600",
    "per_change": "-0.1200",
    "year_high": "0",
    "year_low": "0",
    "ohlc": {
      "open": "81925.5100",
      "high": "81998.5100",
      "low": "81779.8200",
      "close": "81904.7000"
    },
    "depth": {
      "buy": [
        {"price": "0", "quantity": "0", "orders": "0"}
      ],
      "sell": [
        {"price": "0", "quantity": "0", "orders": "0"}
      ]
    }
  }
]
```

### Response Field Mapping

| Field | Type | Description |
| --- | --- | --- |
| exchange_token | string | Instrument token or index name |
| display_symbol | string | UI display symbol |
| exchange | string | Exchange segment (e.g. nse_cm, bse_cm, ...) |
| lstup_time | string | Last update time (Unix timestamp) |
| ltp | string | Last traded price |
| last_traded_quantity | string | Last traded quantity |
| total_buy | string | Top bid quantity |
| total_sell | string | Top offer quantity |
| last_volume | string | Most recent trade volume |
| change | string | Net price change from previous close |
| per_change | string | Percent price change |
| year_high | string | 52-week high |
| year_low | string | 52-week low |
| ohlc | object | Object: open, high, low, close prices |
| depth | object | Top 5 bid/ask levels (arrays `buy` & `sell`) |

**OHLC Object**

| Field | Type | Description |
| --- | --- | --- |
| open | string | Day's open price |
| high | string | Day's high price |
| low | string | Day's low price |
| close | string | Previous close price |

**Depth Object**

| Field | Type | Description |
| --- | --- | --- |
| price | string | Price level |
| quantity | string | Quantity at level |
| orders | string | Order count at level |

Example Error Response:

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid instrument/code",
  "stCode": 1009
}
```

| Field | Type | Description |
| --- | --- | --- |
| stat | string | "Not_Ok" for errors |
| emsg | string | Error message |
| stCode | int | Error code |

## 6. Notes

- All fields are returned as strings.
- When using indices, pass the correct case-sensitive index name.
- For stocks/ETFs, use `pSymbol` from the instrument/scrip master.
- Multi-instrument queries are comma-separated.
- Valid exchange segments: `nse_cm`, `bse_cm`, `nse_fo`, `bse_fo`, `cde_fo` (must be passed as string).
- By default (`/all` or blank) returns all quote data; filters allow more targeted queries.

## 7. Glossary: Index search values

### NSE (`nse_cm`)

```
NIFTY AlphaLowVol, Nifty Commodities, Nifty Consumption, Nifty Div Opps 50,
Nifty Energy, Nifty Infra, Nifty Media, Nifty Metal, Nifty MNC,
Nifty Serv Sector, NIFTY SMLCAP 100, Nifty100 Liq 15, NIFTY LARGEMID250,
NIFTY MIDSML 400, Nifty FinSrv25 50, NIFTY100 EQL Wgt, NIFTY100 LowVol30,
NIFTY500 MULTICAP, NIFTY Alpha 50, NIFTY CONSR DURBL, NIFTY HEALTHCARE,
Nifty GrowSect 15, Nifty200Momentm30, Nifty Mid Liq 15, Nifty Pvt Bank,
NIFTY OIL AND GAS, Nifty 100, Nifty 200, Nifty Auto, Nifty FMCG,
NIFTY MIDCAP 100, Nifty Next 50, Nifty Pharma, Nifty PSU Bank,
NIFTY100 Qualty30, NIFTY MIDCAP 150, NIFTY200 QUALTY30, NIFTY SMLCAP 250,
NIFTY SMLCAP 50, Nifty Realty, Nifty 500, Nifty 50, Nifty IT, Nifty Bank,
Nifty Midcap 50, INDIA VIX, Nifty PSE, Nifty Fin Service, Nifty CPSE,
NIFTY MID SELECT, NIFTY MICROCAP250
```

### BSE (`bse_cm`)

```
SNSX50, SENSEX, BANKEX, BSE100, BSE200, BSE500, BSE CG, BSE CD, BSEPSU,
TECK, AUTO, OILGAS, DOL30, DOL100, DOL200, REALTY, POWER, BSEIPO, SMEIPO,
INFRA, CPSE, MIDCAP, SMLCAP, BSEFMC, BSE HC, BSE IT, MFG, ALLCAP, COMDTY,
CONDIS, ENERGY, FINSER, INDSTR, LRGCAP, MIDSEL, SMLSEL, TELCOM, UTILS,
SNXT50, BHRT22, ESG100, MID150, SML250, LMI250, MSL400, BSEDSI, BSEEVI,
BSELVI, BSEMOI, BSEQUI, DFRGRI, LCTMCI, BSEPBI, BSESER, SNXN30, SNSX60,
SS6535, POWENE, 200EQW, INTECO, CAPINS, FOCIT, PRECON, FOCMID, BBGEFS,
SENEQW, SELIPO, PSUBNK, INSLDR, BS1000, NXT500, BSM250, NXT250, 1000EQ,
IND150, BSE5S, BN5TIP, BSLMIP, BSHOIP, BS5TIP, BDISB, BSEBIP, BSREIT, BSMSIP
```
