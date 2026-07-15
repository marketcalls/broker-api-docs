# Get Expired Historical Candle Data API

## Endpoint

**GET** `https://api.upstox.com/v2/expired-instruments/historical-candle/{expired_instrument_key}/{interval}/{to_date}/{from_date}`

## Path Parameters

| Parameter | Required | Type | Details |
|-----------|----------|------|---------|
| expired_instrument_key | Yes | string | Instrument key + expiry date combined |
| interval | Yes | string | `1minute`, `3minute`, `5minute`, `15minute`, `30minute`, `day` |
| to_date | Yes | string | End date (YYYY-MM-DD) |
| from_date | Yes | string | Start date (YYYY-MM-DD) |

## Response

Same candle array format: [timestamp, open, high, low, close, volume, open_interest]

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1021 | Invalid instrument key format |
| UDAPI1020 | Invalid interval |
| UDAPI1022 | Missing to_date |
| UDAPI100011 | Invalid expired instrument key |
| UDAPI1088 | Invalid date format |
| UDAPI1149 | Requires Upstox Plus subscription |
