# Get Expired Future Contracts API

## Endpoint

**GET** `https://api.upstox.com/v2/expired-instruments/future/contract`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| instrument_key | Yes | String | Underlying instrument key |
| expiry_date | Yes | String | YYYY-MM-DD format |

## Response Fields

name, segment, exchange, expiry, instrument_key, exchange_token, trading_symbol, tick_size, lot_size, instrument_type (FUT), freeze_quantity, underlying_key, underlying_type, underlying_symbol, minimum_lot

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI100011 | Invalid instrument key |
| UDAPI1088 | Invalid date format |
| UDAPI1149 | Requires Upstox Plus plan |
