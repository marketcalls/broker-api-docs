# OHLC Quotes API (V2 - Deprecated)

## Endpoint

**GET** `https://api.upstox.com/v2/market-quote/ohlc`

## Query Parameters

| Parameter | Required | Type | Details |
|-----------|----------|------|---------|
| instrument_key | Yes | string | Comma-separated (max 500) |
| interval | Yes | string | `1d`, `I1` (1-minute), `I30` (30-minute) |

## Response

Returns per-instrument OHLC with last_price and instrument_token.

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1087 | Invalid symbol/instrument_key |
| UDAPI1028 | Unrecognized interval |
| UDAPI1027 | Missing interval |
| UDAPI100043 | Exceeds 500 instrument limit |
