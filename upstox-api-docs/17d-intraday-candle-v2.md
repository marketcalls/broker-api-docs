# Intraday Candle Data API (V2 - Deprecated)

## Endpoint

**GET** `https://api.upstox.com/v2/historical-candle/intraday/{instrument_key}/{interval}`

## Parameters

| Parameter | Required | Type | Details |
|-----------|----------|------|---------|
| instrument_key | Yes | String | Instrument identifier |
| interval | Yes | String | `1minute` or `30minute` |

## Response

Same candle array format: [timestamp, open, high, low, close, volume, open_interest]
