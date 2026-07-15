# Authentication & Users

> Source: https://api-docs.indstocks.com/Users/

## Obtaining an Access Token

Individual traders obtain an access token by logging in at
[web.indstocks.com](https://indstocks.com) → **API / API Trading** section →
**Generate Token**. Tokens are valid for **24 hours**.

Every authenticated request must include the token in the `Authorization` header:

```
Authorization: YOUR_ACCESS_TOKEN
```

---

## Get User Profile

Retrieves the authenticated user's account information. Also useful as a lightweight way to
verify that a token is still valid.

**Endpoint:** `GET /user/profile`

### Request

```bash
curl --location 'https://api.indstocks.com/user/profile' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
  "status": "success",
  "data": {
    "user_id": "1234567",
    "email": "john.doe@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "demat_id": "",
    "is_nse_onboarded": true,
    "is_bse_onboarded": true,
    "is_nse_fno_onboarded": true,
    "is_bse_fno_onboarded": true
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `user_id` | string | Unique user identifier |
| `email` | string | Registered email address |
| `first_name` / `last_name` | string | Account holder name |
| `demat_id` | string | Demat account identifier |
| `is_nse_onboarded` | boolean | Whether NSE equity trading is enabled |
| `is_bse_onboarded` | boolean | Whether BSE equity trading is enabled |
| `is_nse_fno_onboarded` | boolean | Whether NSE F&O trading is enabled |
| `is_bse_fno_onboarded` | boolean | Whether BSE F&O trading is enabled |

---

## Get Funds

Returns fund utilization and availability details for the account.

**Endpoint:** `GET /funds`

### Request

```bash
curl --location 'https://api.indstocks.com/funds' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
  "status": "success",
  "data": {
    "sod_balance": 4996.47,
    "pledge_received": 0,
    "pledge_remained": 0,
    "detailed_avl_balance": {
      "option_sell": 2980.40,
      "future": 2980.40,
      "option_buy": 4449.65,
      "eq_mis": 2980.40,
      "eq_cnc": 2980.40,
      "eq_mtf": 2980.40
    },
    "withdrawal_balance": 2983.47,
    "funds_added": 0,
    "funds_withdrawn": 0,
    "realized_pnl": -751.92,
    "unrealized_pnl": 62.15
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `sod_balance` | number | Start-of-day balance |
| `pledge_received` / `pledge_remained` | number | Pledged collateral values |
| `detailed_avl_balance` | object | Available balance broken down per product/segment |
| `withdrawal_balance` | number | Amount available for withdrawal |
| `funds_added` / `funds_withdrawn` | number | Funds added/withdrawn during the day |
| `realized_pnl` | number | Realized profit / loss |
| `unrealized_pnl` | number | Mark-to-market profit / loss on open positions |

> The same funds data is available via the `/funds` endpoint referenced in
> [Portfolio & Funds](12-portfolio-funds.md).
