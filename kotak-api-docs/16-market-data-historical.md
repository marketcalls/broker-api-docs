# Market Data — Historical Candles

> Added to the Neo API in September 2026 (SDK v3.0.6). Not present in the original v2 client documentation.

## 1. Introduction

The Historical Data API returns OHLCV candles for a single instrument over a date range. It is the endpoint behind the SDK's `historical_data()` function.

Like Quotes and Scrip Master, this endpoint authenticates on the **access token alone** — no TOTP/MPIN session is required, so no `Auth`/`Sid`/`neo-fin-key` headers.

## 2. API Endpoint

```
GET <Base URL>/market-data/1.0/historical/details
```

Replace `<Base URL>` with the base URL returned by `/tradeApiValidate`.

## 3. Headers

| Name | Type | Description |
| --- | --- | --- |
| Authorization | string | Access token from the NEO API dashboard — plain token, no `Bearer` |

## 4. Query Parameters

Note that the wire parameter names are lower-case and unseparated (`fromdate`, `todate`) even though the SDK's Python keyword arguments are snake_case (`from_date`, `to_date`).

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| neosymbol | string | Yes | `<exchange_segment>\|<instrument_token>`, e.g. `nse_cm\|1333`. The token is `pSymbol` from the scrip master. |
| interval | string | Yes | One of `1min`, `3min`, `5min`, `10min`, `15min`, `30min`, `60min`, `D` (daily), `W` (weekly). |
| fromdate | string | Yes | Start date, `YYYY-MM-DD`. |
| todate | string | Yes | End date, `YYYY-MM-DD`. May be the current date. |

### Supported segments

Historical data is served for `nse_cm`, `bse_cm`, `nse_fo` and `bse_fo` only. It is **not** available for `mcx_fo` or `nse_com`. `cde_fo` is undocumented and untested.

### Date range limits

Enforced by the backend, not by the client. A range wider than the limit for its interval is rejected outright — it is not truncated — so a longer pull has to be split into chunks and stitched back together.

| Interval | Max days per request |
| --- | --- |
| `1min`, `3min`, `5min` | 30 |
| `10min`, `15min` | 60 |
| `30min`, `60min` | 90 |
| `D`, `W` | 180 |

### Rate limit

Kotak publishes no rate limit for this endpoint, so the figure below is measured, and it has moved once already — re-measure before trusting it.

**Current guidance: pace at 1 request/second.** Measured against the live endpoint on 2026-09-21:

| Gap between requests | Result |
| --- | --- |
| 0.25 s | 5/10 succeeded |
| 0.5 s | 6/10 succeeded |
| 0.75 s | 11/12 succeeded |
| 1.0 s | 20/20 succeeded over 23 s |

A single request after an idle period succeeds, and a quotes call immediately before one does not disturb it, so this is the historical endpoint's own sustained ceiling rather than a burst allowance or a budget shared with quotes.

The earlier measurement on 2026-09-06 — 12 back-to-back requests giving 5 successes then HTTP 429, with a 0.5 s gap sustaining 10/10, suggesting roughly 4/second — no longer holds. Kotak appears to have tightened the endpoint in the interim.

Pacing at the ceiling costs no wall clock: at 4/second roughly half the requests returned 429, and each cost a backoff plus a wasted round trip, so a chunk averaged about a second either way.

No `Retry-After` header is sent on a 429, so back off exponentially.

## 5. Request

```bash
curl --location --request GET \
  '<Base URL>/market-data/1.0/historical/details?neosymbol=nse_cm|1333&interval=10min&fromdate=2026-08-20&todate=2026-09-01' \
  --header 'Authorization: xxxxx-your-neo-token-xxxx'
```

## 6. Response

```json
{
  "status": "success",
  "interval": "1min",
  "data": {
    "candles": [
      ["2026-08-20T09:15:00+0530", 12009.9, 12019.35, 12001.25, 12001.5, 163275, 13667775],
      ["2026-08-20T09:16:00+0530", 12001, 12003, 11998.25, 12001, 105750, 13667775]
    ]
  }
}
```

Each entry in `candles` is a **fixed-order positional row, not an object**. This is the key difference from the legacy parallel-array response shape:

```
[timestamp, open, high, low, close, volume, oi]
```

| Position | Field | Notes |
| --- | --- | --- |
| 0 | timestamp | ISO 8601, carrying the `+0530` offset |
| 1 | open | |
| 2 | high | |
| 3 | low | |
| 4 | close | |
| 5 | volume | |
| 6 | oi | **Not populated in phase one.** Planned for a later phase; a row may arrive short. Do not rely on it being present or non-null. |

### Empty ranges

A range holding no candles — a weekend, a holiday, or today before the open — comes back as an HTTP **400 fault**, not as an empty success. It has to be told apart from a real failure by the fault text. Two observed live:

- `No data found` — for a weekend or holiday
- `Data not available ... Market has not yet opened` — for today before the open

`Invalid neosymbol` is a genuine error and must not be treated as an empty range.

### Error Codes

| Code | Description |
| --- | --- |
| 200 | Success |
| 400 | Invalid or missing input parameters — unsupported `interval`, a date range exceeding that interval's limit, or an empty range (see above) |
| 403 | Invalid session, please re-login |
| 429 | Too many requests: API rate limited |
| 500 | Server error: unexpected system error |

## 7. Notes

- The `|` in `neosymbol` is taken literally and does not need percent-encoding.
- The historical endpoint matches instrument names **case-sensitively** and does not always agree with the Quotes endpoint. INDIAVIX answers to `India VIX` for quotes but only to `INDIA VIX` here, so an index lookup should try the token first and fall back across name variants.
- Daily and weekly candles are dates rather than instants. Parse the `+0530` offset to get the true epoch for intraday bars.
