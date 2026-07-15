# Instruments Master

> Source: https://api-docs.indstocks.com/instruments/

The Instruments Master is the reference list of all tradable instruments. Every other
endpoint identifies an instrument by the `SECURITY_ID` (token) found in this file. It is
returned as a **CSV file**, not JSON.

## Get Instruments

**Endpoint:** `GET /market/instruments`

### Query Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `source` | string | ✅ | Market segment: `equity`, `fno`, or `index` |

### Authentication

Requires the `Authorization` header with your access token.

### Request

```bash
curl --location 'https://api.indstocks.com/market/instruments?source=fno' \
--header 'Authorization: YOUR_ACCESS_TOKEN' \
--output instruments.csv
```

> The response is a CSV stream — use `--output` (or your HTTP client's file-download
> equivalent) to save it directly to disk.

### CSV Columns

| Column | Description |
|--------|-------------|
| `EXCH` | Exchange identifier (NSE, BSE) |
| `SEGMENT` | Market segment (`E` = Equity, `FNO`) |
| `SECURITY_ID` | Unique instrument identifier (the token used across the API) |
| `INSTRUMENT_NAME` | Instrument type (e.g., `EQUITY`, `FUTCUR`) |
| `EXPIRY_CODE` | Numeric expiry code; `0` for non-derivatives |
| `TRADING_SYMBOL` | Exchange trading symbol |
| `LOT_UNITS` | F&O contract lot size |
| `CUSTOM_SYMBOL` | Human-friendly descriptive symbol |
| `EXPIRY_DATE` | Derivative expiry date |
| `STRIKE_PRICE` | Options strike price |
| `OPTION_TYPE` | `CE` (Call) or `PE` (Put) |
| `TICK_SIZE` | Minimum price movement |
| `EXPIRY_FLAG` | Expiry type indicator (e.g., `M` = monthly) |
| `SEM_EXCH_INSTRUMENT_TYPE` | Exchange-defined instrument type |
| `SERIES` | Series code (e.g., `EQ`) |
| `SYMBOL_NAME` | Base symbol name |

### `source` Values

| Value | Returns |
|-------|---------|
| `equity` | Cash / equity instruments |
| `fno` | Futures & options contracts |
| `index` | Index instruments |

> **Tip:** Download the relevant instruments file periodically (contracts change on expiry)
> and build a local lookup from `TRADING_SYMBOL` / `CUSTOM_SYMBOL` → `SECURITY_ID`.
