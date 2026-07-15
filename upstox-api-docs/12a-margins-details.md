# Margin Details API

## Overview

The Margin Details API retrieves margin requirements for instruments based on specified parameters. Maximum of 20 instruments allowed per request.

## Endpoint

**POST** `https://api.upstox.com/v2/charges/margin`

## Authentication

Requires Bearer token: `Authorization: Bearer {your_access_token}`

## Request Parameters

| Parameter | Required | Type | Details |
|-----------|----------|------|---------|
| `instrument_key` | Yes | String | Instrument identifier following regex patterns |
| `quantity` | Yes | Integer | Must be multiple of lot size, greater than zero |
| `transaction_type` | Yes | String | BUY or SELL |
| `product` | Yes | String | I, D, CO, or MTF |
| `price` | No | Float | Order placement price |

## Response Fields

| Field | Description |
|-------|-------------|
| span_margin | Upfront exchange-mandated derivative margin |
| exposure_margin | Based on exchange ELM percentages for FNO trades |
| equity_margin | Applicable for equity transactions |
| net_buy_premium | Option premium requirements |
| additional_margin | MCX commodity-specific margin |
| tender_margin | Applied as futures approach expiration |
| total_margin | Sum of all applicable margins |
| required_margin | Total needed for order execution |
| final_margin | Amount after margin benefits applied |

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI1054 | Invalid product |
| UDAPI1057 | Invalid transaction type |
| UDAPI1096 | Quantity must be greater than zero |
| UDAPI1097 | Quantity must be multiple of lot size |
| UDAPI1098 | Invalid instrument key format |
| UDAPI1099 | Invalid instrument key |
| UDAPI1102 | Exceeds 20-instrument limit |
| UDAPI1103 | Duplicate instruments in request |
