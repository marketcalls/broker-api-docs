# Market Timings API

## Endpoint

**GET** `https://api.upstox.com/v2/market/timings/{date}`

## Path Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| date | Yes | string | YYYY-MM-DD format |

## Response

| Field | Type | Description |
|-------|------|-------------|
| exchange | string | Exchange identifier |
| start_time | number | Opening timestamp (ms) |
| end_time | number | Closing timestamp (ms) |

## Supported Exchanges

MCX, NSE, NFO, CDS, BSE, BCD, BFO

## Segment Close Times

Effective 3 August 2026 the derivatives segments close later than the cash segments. Read the per-segment `NORMAL_CLOSE` from the Exchange Status API rather than assuming a single 3:30 PM close.

| Segment | `NORMAL_CLOSE` (IST) |
|---------|----------------------|
| `NSE_EQ`, `BSE_EQ` | 3:30 PM |
| `NSE_FO`, `BSE_FO` | 3:40 PM |

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1088 | Invalid date format |
