# Market Data — Expiries and Option Chain

> Added to the Neo API in September 2026 (SDK v3.0.6). Not present in the original v2 client documentation.

Two related endpoints: one lists the available expiry dates for an underlying, the other returns the option or futures chain for one of them. Both authenticate on the **access token alone** — no TOTP/MPIN session, so no `Auth`/`Sid`/`neo-fin-key` headers.

---

## Part A — Expiries

### 1. API Endpoint

```
GET <Base URL>/market-data/1.0/watchlist/expiries
```

### 2. Headers

| Name | Type | Description |
| --- | --- | --- |
| Authorization | string | Access token from the NEO API dashboard — plain token, no `Bearer` |

### 3. Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| exchange | string | Yes | Exchange segment: `nse_fo`, `bse_fo` or `mcx_fo` |
| underlying | string | Yes | Underlying name, e.g. `RELIANCE`, `NIFTY`. Matches `pSymbolName` in the scrip master. |
| instrument_type | string | No | `option` (default) or `fut` |

### 4. Request

```bash
curl --location --request GET \
  '<Base URL>/market-data/1.0/watchlist/expiries?exchange=nse_fo&underlying=RELIANCE' \
  --header 'Authorization: xxxxx-your-neo-token-xxxx'
```

### 5. Response

```json
{
  "exchange": "nse_fo",
  "underlying": "RELIANCE",
  "expiries": [
    "2026-06-25",
    "2026-06-30",
    "2026-07-31"
  ]
}
```

`expiries` is a flat array of ISO `YYYY-MM-DD` strings, sorted ascending. Pass one of them straight through as the option chain's `expiry` parameter.

---

## Part B — Option Chain

Returns the calls/puts chain, or the futures chain, for an underlying, with per-strike quote and open-interest data.

### 1. API Endpoint

```
GET <Base URL>/market-data/1.0/watchlist/option-chain
```

### 2. Headers

Same as Expiries above.

### 3. Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| exchange | string | Yes | Exchange segment: `nse_fo`, `bse_fo` or `mcx_fo` |
| underlying | string | Yes | Underlying name, e.g. `RELIANCE`, `NIFTY`. Matches `pSymbolName` in the scrip master. |
| expiry | string | No | ISO expiry date (`YYYY-MM-DD`) from the Expiries endpoint. Defaults to the nearest expiry when omitted. |
| instrument_type | string | No | `option` (default) or `fut` |
| count | int | No | Number of strikes. Default 40, giving 80 instruments (40 calls + 40 puts). Must be a multiple of 10. |

With `instrument_type=fut` and no `expiry`, the response's `fut[]` array carries every available futures contract; with a specific `expiry` it carries only that one.

### 4. Response — option chain

```json
{
  "data": {
    "common_data": {
      "mktLot": "65",
      "multiplier": "1",
      "unlSymbol": "NIFTY",
      "exSeg": "nse_fo",
      "expiryDt": "2026-06-23"
    },
    "call": [
      {
        "instrument": {
          "neoSymbol": "nse_fo|71472",
          "symbol": "NIFTY26JUN22250CE",
          "optionType": "CE",
          "strikePrice": "22250",
          "moneyness": "ATM"
        },
        "quote": {
          "ltp": "166.7500",
          "open": "89.8000",
          "high": "214.0000",
          "low": "77.1000",
          "prevClose": "99.7000",
          "close": null,
          "volume": 225431505
        },
        "openInterest": {
          "current": 10715645,
          "previous": 13647630,
          "change": -2931985,
          "changePct": -21.48
        }
      }
    ],
    "put": []
  }
}
```

- `openInterest.change` / `changePct` are computed server-side from current vs. previous OI, so every caller sees the same value.
- `close` stays `null` intraday and is populated at settlement. `prevClose` is stable for the whole session, so a day-change calculation needs no time-of-day logic.

### 5. Response — futures chain (`instrument_type=fut`)

The futures rows use a different, abbreviated field naming than the option rows — `inst`/`o`/`h`/`l`/`c`/`pc`/`vol` and `oi.cur`/`prev`/`chg`/`chgPct`, rather than `instrument`/`open`/`high`/... and `openInterest.current`/... Do not assume one parser covers both.

```json
{
  "data": {
    "common_data": {
      "mktLot": "65",
      "multiplier": "1",
      "unlSymbol": "NIFTY",
      "exSeg": "nse_fo",
      "expiryDt": null
    },
    "call": [],
    "put": [],
    "fut": [
      {
        "inst": {
          "neoSymbol": "nse_fo|53001",
          "symbol": "NIFTY26JULFUT",
          "expiryDt": "31-JUL-2026"
        },
        "quote": {
          "ltp": "24485.20",
          "o": "24455.00",
          "h": "24512.00",
          "l": "24428.00",
          "c": "24485.20",
          "pc": "24322.10",
          "vol": "9852340"
        },
        "oi": {
          "cur": "13930930",
          "prev": "13801200",
          "chg": "129730",
          "chgPct": "0.94"
        }
      }
    ]
  }
}
```

---

## Error Codes (both endpoints)

| Code | Description |
| --- | --- |
| 200 | Success |
| 400 | Invalid or missing input parameters (for the option chain, e.g. `count` not a multiple of 10) |
| 403 | Invalid session, please re-login |
| 429 | Too many requests: API rate limited |
| 500 | Server error: unexpected system error |
