# Getting Started

> Source: https://api-docs.indstocks.com/getting-started/

This guide takes you from zero to your first authenticated API call in about 5 minutes.

## Prerequisites

- An **INDstocks account** — sign up at [indstocks.com](https://indstocks.com)
- Completed **KYC verification** (per SEBI requirements)
- **Funded account** if you plan to place live trades

## Step 1 — Generate Your Access Token

1. Log in to your INDstocks dashboard.
2. Go to the API section: `https://indstocks.com/app/api-trading`
3. Click **Generate Token** and copy your access token.

> ⚠️ Your access token is like a password — keep it secure. **Tokens expire after 24 hours**,
> after which you must generate a new one.

## Step 2 — Verify Authentication

Call `GET /user/profile` with your token to confirm it works.

```python
import requests
import os

access_token = os.getenv('INDSTOCKS_TOKEN')
base_url = 'https://api.indstocks.com'
headers = {
    'Authorization': access_token,
    'Content-Type': 'application/json'
}

response = requests.get(f'{base_url}/user/profile', headers=headers)
print(response.json())
```

A successful response returns your user profile (user ID, email, name, and onboarding flags).

## Step 3 — Fetch Market Data

Request real-time quotes using scrip codes (`SEGMENT_TOKEN` format):

```python
params = {'scrip-codes': 'NSE_2885,NSE_11536'}
response = requests.get(
    f'{base_url}/market/quotes/full',
    headers=headers,
    params=params
)
print(response.json())
```

## Step 4 — Place Your First Order

Use the `/order` endpoint with the required parameters — transaction type, exchange, segment,
security ID, quantity, order type, and product type. Set `algo_id` to `"99999"` for regular
NSE orders. See **[Order Management](09-order-management.md)** for the full parameter list.

## Step 5 — Check Order Status

Retrieve your order book to see all of the day's orders and their statuses:

```python
response = requests.get(f'{base_url}/order-book', headers=headers)
print(response.json())
```

## Next Steps

- Review the **[API Conventions](03-conventions.md)** for rate limits and formats.
- Explore **[Smart Orders (GTT)](10-smart-orders.md)** for automated stop-loss / target legs.
- Stream live prices with the **[WebSocket API](08-websockets.md)**.
