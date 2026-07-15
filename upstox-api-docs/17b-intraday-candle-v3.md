# Intraday Candle Data V3 API

## Overview

Retrieves OHLC values for the current trading day with customizable time intervals.

## Endpoint

**GET** `https://api.upstox.com/v3/historical-candle/intraday/{instrument_key}/{unit}/{interval}`

## Path Parameters

| Name | Required | Type | Description |
|------|----------|------|-------------|
| instrument_key | Yes | string | Instrument identifier |
| unit | Yes | string | `minutes`, `hours`, or `days` |
| interval | Yes | string | 1-300 for minutes, 1-5 for hours, 1 for days |

## Response

Same candle array format as Historical Candle Data V3: [timestamp, open, high, low, close, volume, open_interest]

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1021 | Invalid instrument key format |
| UDAPI100011 | Unrecognized instrument key |
| UDAPI1146 | Invalid unit |
| UDAPI1147 | Invalid interval for unit |
