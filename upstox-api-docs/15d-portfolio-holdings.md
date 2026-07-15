# Get Holdings API

## Overview

Retrieves long-term holdings from a user's DEMAT account. Holdings remain without a predetermined time limit.

## Endpoint

**GET** `https://api.upstox.com/v2/portfolio/long-term-holdings`

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| isin | string | Standard ISIN code |
| quantity | int32 | Total holding quantity |
| trading_symbol | string | Trading symbol |
| last_price | float | Last traded price |
| close_price | float | Previous closing price |
| pnl | float | Profit/Loss amount |
| average_price | float | Acquisition price |
| product | string | Product type (I/D/CO/MTF) |
| collateral_quantity | int32 | RMS-marked collateral |
| haircut | float | Haircut percentage |
| exchange | string | Exchange identifier |

## Python Example

```python
import requests
url = 'https://api.upstox.com/v2/portfolio/long-term-holdings'
headers = {
    'Authorization': 'Bearer {your_access_token}',
    'Accept': 'application/json'
}
response = requests.get(url, headers=headers)
print(response.json())
```
