# Get Expired Option Contracts API

## Endpoint

**GET** `https://api.upstox.com/v2/expired-instruments/option/contract`

## Query Parameters

| Parameter | Required | Type | Details |
|-----------|----------|------|---------|
| instrument_key | Yes | String | Underlying instrument identifier |
| expiry_date | Yes | String | YYYY-MM-DD format |

## Response Fields

name, segment, exchange, expiry, instrument_key, exchange_token, trading_symbol, tick_size, lot_size, instrument_type (CE/PE), freeze_quantity, underlying_key, underlying_type, strike_price, minimum_lot, weekly

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI100011 | Invalid instrument key |
| UDAPI1088 | Invalid date format |
| UDAPI1149 | Requires Upstox Plus plan |
