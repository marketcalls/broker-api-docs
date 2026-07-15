# Historical Candle Data API (V2 - Deprecated)

## Endpoint

**GET** `https://api.upstox.com/v2/historical-candle/{instrument_key}/{interval}/{to_date}/{from_date}`

## Data Availability

| Interval | Historical Depth |
|----------|-----------------|
| 1minute | Last month |
| 30minute | Past year |
| day | Past year |
| week | Previous ten years |
| month | Last ten years |

## Path Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| instrument_key | Yes | string | Instrument identifier |
| interval | Yes | string | `1minute`, `30minute`, `day`, `week`, `month` |
| to_date | Yes | string | End date (YYYY-MM-DD) |
| from_date | No | string | Start date (YYYY-MM-DD) |

## Response

Same candle array format: [timestamp, open, high, low, close, volume, open_interest]
