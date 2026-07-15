# Get Positions API

## Overview

Retrieves current positions for a user. Positions remain until sold or reach their standard three-month expiration date.

## Endpoint

**GET** `https://api.upstox.com/v2/portfolio/short-term-positions`

## Request Headers

```
Content-Type: application/json
Accept: application/json
Authorization: Bearer {your_access_token}
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| exchange | string | NSE, BSE, NFO, MCX, CDS |
| multiplier | float | Quantity/lot size multiplier |
| value | float | Net position value |
| pnl | float | Profit and loss |
| product | string | I (Intraday), D (Delivery), CO (Cover Order) |
| quantity | int32 | Remaining quantity |
| last_price | float | Current market price |
| unrealised | float | Day PnL on open positions |
| realised | float | Day PnL on closed positions |

## Python Example

```python
import requests
url = 'https://api.upstox.com/v2/portfolio/short-term-positions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {your_access_token}'
}
response = requests.get(url, headers=headers)
print(response.json())
```
