# Option Contracts API

## Endpoint

**GET** `https://api.upstox.com/v2/option/contract`

## Query Parameters

| Parameter | Required | Type | Details |
|-----------|----------|------|---------|
| instrument_key | Yes | String | Underlying symbol (e.g., `NSE_INDEX|Nifty 50`) |
| expiry_date | No | String | Filter by expiry (YYYY-MM-DD) |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| name | string | Option name |
| segment | string | NSE_FO, BSE_FO, MCX_FO, etc. |
| exchange | string | NSE, BSE, MCX |
| expiry | string | Expiry date (YYYY-MM-DD) |
| instrument_key | string | Unique identifier |
| exchange_token | string | Exchange-specific token |
| trading_symbol | string | e.g., "NIFTY 19650 CE 15 FEB 24" |
| tick_size | number | Minimum price movement |
| lot_size | number | Lot size |
| instrument_type | string | CE or PE |
| freeze_quantity | number | Max frozen quantity |
| underlying_key | string | Parent asset identifier |
| underlying_type | string | COM, INDEX, EQUITY, CUR, IRD |
| underlying_symbol | string | Parent asset symbol |
| strike_price | number | Strike price |
| minimum_lot | number | Minimum lot requirement |
| weekly | boolean | Weekly options indicator |

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI100011 | Invalid instrument key |
| UDAPI1088 | Invalid date format |
