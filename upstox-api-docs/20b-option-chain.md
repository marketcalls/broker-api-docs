# Put/Call Option Chain API

## Overview

Retrieves option chain data for an underlying symbol on a specific expiry date. **Not available for MCX Exchange.**

## Endpoint

**GET** `https://api.upstox.com/v2/option/chain`

## Query Parameters

| Parameter | Required | Type | Description |
|-----------|----------|------|-------------|
| instrument_key | Yes | string | Underlying symbol identifier |
| expiry_date | Yes | string | YYYY-MM-DD format |

## Response Contains

- Expiry date
- Put-Call Ratio (PCR)
- Strike price
- Underlying asset details (key and spot price)
- Call options data (market data and Greeks)
- Put options data (market data and Greeks)

### Market Data Fields

- Last Traded Price (LTP)
- Close price
- Volume and Open Interest
- Bid/Ask prices and quantities
- Previous Open Interest

### Option Greeks (per contract)

| Greek | Description |
|-------|-------------|
| Vega | Volatility impact |
| Theta | Time decay |
| Gamma | Delta change rate |
| Delta | Directional sensitivity |
| IV | Implied volatility |
| POP | Probability of profit |

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI100011 | Invalid instrument key |
| UDAPI1088 | Invalid expiry_date format |
