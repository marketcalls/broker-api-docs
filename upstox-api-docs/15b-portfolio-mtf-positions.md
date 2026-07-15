# Get MTF Positions API

## Overview

Retrieves current Margin Trade Funding (MTF) positions. MTF allows investors to buy securities by paying a fraction of the transaction value.

## Endpoint

**GET** `https://api.upstox.com/v3/portfolio/mtf-positions`

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| exchange | string | Exchange (NSE only for MTF) |
| multiplier | float | Quantity/lot size multiplier |
| value | float | Net position value |
| pnl | float | Profit and loss |
| product | string | Always "MTF" |
| instrument_token | string | Instrument identifier |
| average_price | float | Net position acquisition price |
| quantity | int32 | Remaining position quantity |
| last_price | float | Current market price |
| unrealised | float | Day PnL on open positions |
| realised | float | Day PnL on closed positions |
| trading_symbol | string | Instrument trading symbol |
