# Option Greeks API

## Overview

Supplies option Greek data for designated instruments. Accommodates up to 50 instrument keys per request.

## Endpoint

**GET** `https://api.upstox.com/v3/market-quote/option-greek`

## Query Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| instrument_key | Yes | Comma-separated list (max 50) |

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| last_price | number | Most recent trade price |
| instrument_token | string | Instrument identifier |
| ltq | number | Last traded quantity |
| volume | number | Current day's trading volume |
| cp | number | Previous closing price |
| iv | number | Implied volatility |
| vega | number | Price sensitivity to volatility |
| gamma | number | Delta change rate |
| theta | number | Time decay rate |
| delta | number | Price sensitivity to underlying |
| oi | number | Open interest quantity |

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1009 | Missing instrument_key |
| UDAPI1011 | Invalid format |
| UDAPI1087 | Invalid instrument_key value |
| UDAPI100076 | Exceeds max instrument key limit (50) |
