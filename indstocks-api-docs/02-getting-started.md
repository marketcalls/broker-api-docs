# Getting Started

> Source: https://api-docs.indstocks.com/getting-started/

This guide takes you from zero to your first authenticated API call in about 5 minutes.

## Prerequisites

- An **INDstocks account** — sign up at [indstocks.com](https://indstocks.com)
- Completed **KYC verification** (per SEBI requirements)
- **Funded account** if you plan to place live trades

## Step 1 — Generate Your Access Token

1. Log in to your INDstocks dashboard.
2. Go to the API section: `https://indstocks.com/app/api-trading/access-tokens`
3. Click **Generate Token** and copy your access token.

The same page also offers **TOTP setup** and **Static IP** configuration.

> ⚠️ Your access token is like a password — keep it secure. Never commit it to version
> control. **Tokens expire after 24 hours**, after which you must generate a new one. Revoke
> immediately if compromised.

### Prefer a scriptable token?

Set up TOTP once on the website, then have your script mint its own token each day with
`POST /generate/token` — no browser login required. See
[Authentication & Users](04-authentication-users.md#method-2--totp-based-token-generation).

### Using an algo platform instead?

If you use Tradetron rather than writing code: log in at tradetron.tech, open the broker
integration settings, select **INDmoney** as your broker, paste your access token, and save.
Steps 2–5 below are only needed for the DIY path.

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

> ⚠️ **This places real orders with real money.** Start with small quantities to test your
> integration. There is no sandbox environment.

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
- Keep **[Glossary & Constants](16-glossary.md)** open for enum and prefix lookups.

## Common Troubleshooting

| Problem | Fix |
|---------|-----|
| Invalid token | Regenerate at the access-tokens dashboard |
| Insufficient margin | Check available funds via `/funds` |
| Wrong security ID | Re-download the [instruments master](05-instruments.md) and verify |
| Connection timeout | Check connectivity and that the endpoint path is correct |

See [Error Codes](14-errors.md) for the full error and RMS-rejection tables.

## Best Practices

Handle errors explicitly, respect rate limits, add exponential-backoff retries, log API
requests, test with minimal quantities, and keep tokens in environment variables rather than
hardcoding them.
