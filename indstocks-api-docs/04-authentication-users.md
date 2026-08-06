# Authentication & Users

> Source: https://api-docs.indstocks.com/Users/

There are **two** ways to obtain an access token: the web dashboard, and a scriptable
**TOTP** flow via `POST /generate/token`.

Every authenticated request must include the token in the `Authorization` header (raw, no
`Bearer ` prefix):

```
Authorization: YOUR_ACCESS_TOKEN
```

---

## Method 1 — Dashboard Token Generation

1. Log in at [indstocks.com](https://indstocks.com).
2. Go to `https://indstocks.com/app/api-trading/access-tokens`.
3. Click **Generate Token** and copy it.

Tokens are valid for **24 hours**.

---

## Method 2 — TOTP-Based Token Generation

Lets a script mint its own access token each day without a browser login.

### One-Time Setup (web only)

1. Log in to indstocks.com and open the **access-tokens** page.
2. Click **Setup TOTP** and link an authenticator app.
3. Scan the QR code, or enter the key manually.
4. Submit a confirmation code from the app **within 5 minutes**.
5. Record your static **Client ID** — it becomes the `x-api-key` for this endpoint.

> ⚠️ The TOTP secret is displayed **only once** and cannot be recovered. There is no API to
> configure TOTP — setup is web-only. If you lose the authenticator, disable TOTP on the
> website and re-enroll to get a fresh secret.

### Generate Token

**Endpoint:** `POST /generate/token`

This endpoint does **not** use the `Authorization` header. It authenticates with `x-api-key`
(your Client ID) plus MPIN and TOTP.

#### Request Headers

| Header | Value |
|--------|-------|
| `x-api-key` | Your static Client ID (from TOTP setup) |
| `Content-Type` | `application/json` |

#### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `mpin` | string | ✅ | Your account MPIN |
| `totp` | string | ✅ | Current 6-digit code from your authenticator app |

```bash
curl --location 'https://api.indstocks.com/generate/token' \
--header 'x-api-key: YOUR_API_KEY' \
--header 'Content-Type: application/json' \
--data '{
    "mpin": "YOUR_MPIN",
    "totp": "123456"
}'
```

#### Response

> ⚠️ The response field is named **`token`**, *not* `access_token`. Use its value in the
> `Authorization` header of subsequent requests.

### Token Lifecycle

- Only **one** TOTP-generated token is live at a time — each new generation **invalidates the
  previous one**.
- Tokens remain valid for **24 hours** unless replaced, revoked, or TOTP is disabled.
- Recommended: generate **once per session** and reuse the token for the rest of the day.

### Rate Limits & Lockouts

| Rule | Limit |
|------|-------|
| Minimum gap between generations | 1 token per **60 seconds** |
| Failed attempts before lockout | **5** wrong TOTP codes |
| Lockout duration | **15 minutes** |
| Repeated lockouts | **3** lockouts within 1 hour → **1-hour** lockout |

> Clock drift on your server is the most common cause of "wrong TOTP" failures — keep the host
> synced via NTP. Never retry the same TOTP code; wait for the next one.
> See [Error Codes](14-errors.md#token-generation-errors-totp) for the failure table.

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
    "is_bse_fno_onboarded": true,
    "ucc": "1ABCDE2N7X",
    "is_ddpi_active": true
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
| `ucc` | string | Unique Client Code assigned by the exchange |
| `is_ddpi_active` | boolean | Whether DDPI (Demat Debit and Pledge Instruction) is enabled |

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
      "comm_option_buy": 2980.40,
      "eq_mis": 2980.40,
      "eq_cnc": 2980.40,
      "eq_mtf": 2980.40
    },
    "withdrawal_balance": 2983.47,
    "funds_added": 0,
    "funds_withdrawn": 0,
    "realized_pnl": -751.92,
    "unrealized_pnl": 62.15,
    "brokerage": 0,
    "eq_charges": 0,
    "fno_charges": 0
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `sod_balance` | number | Start-of-day balance |
| `pledge_received` / `pledge_remained` | number | Pledged collateral values |
| `detailed_avl_balance` | object | Available balance broken down per product/segment |
| `detailed_avl_balance.comm_option_buy` | number | Available balance for commodity option buying |
| `withdrawal_balance` | number | Amount available for withdrawal |
| `funds_added` / `funds_withdrawn` | number | Funds added/withdrawn during the day |
| `realized_pnl` | number | Realized profit / loss |
| `unrealized_pnl` | number | Mark-to-market profit / loss on open positions |
| `brokerage` | number | Brokerage accrued for the day |
| `eq_charges` | number | Equity segment charges for the day |
| `fno_charges` | number | F&O segment charges for the day |

> The same funds data is available via the `/funds` endpoint referenced in
> [Portfolio & Funds](12-portfolio-funds.md).
