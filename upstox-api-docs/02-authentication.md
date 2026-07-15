# Authentication

Upstox implements standard OAuth 2.0 for customer authentication and login. All authentication occurs through upstox.com exclusively for security compliance.

## Authentication Flow

### Step 1: Initiate Login

Direct users to the authorization dialog at:

```
https://api.upstox.com/v2/login/authorization/dialog
```

**Required Parameters:**

| Parameter | Purpose |
|-----------|---------|
| `client_id` | Your API key from app registration |
| `redirect_uri` | Post-authentication redirect URL (must match registered URL) |
| `response_type` | Must always be `code` |
| `state` | Optional parameter for state continuity |

**Example URL:**

```
https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id=615b1297-d443-3b39-ba19-1927fbcdddc7&redirect_uri=https%3A%2F%2Fwww.trading.tech%2Flogin%2Fupstox-v2&state=RnJpIERlYyAxNiAyMDIyIDE1OjU4OjUxIEdNVCswNTMwIChJbmRpYSBTdGFuZGFyZCBUaW1lKQ%3D%3D
```

### Step 2: Receive Authorization Code

Upon successful login, users are redirected with:

```
https://<redirect_uri>?code=mk404x&state=XX56849
```

The `code` parameter is single-use and required for token generation.

### Step 3: Generate Access Token

Make a server-to-server POST request to:

```
https://api.upstox.com/v2/login/authorization/token
```

**Required Parameters:**

| Parameter | Description |
|-----------|-------------|
| `code` | Authorization code from Step 2 |
| `client_id` | Your API key |
| `client_secret` | Your API secret (confidential) |
| `redirect_uri` | Registered redirect URL |
| `grant_type` | Must be `authorization_code` |

**cURL Example:**

```bash
curl -X 'POST' 'https://api.upstox.com/v2/login/authorization/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'code=<Auth-Code>&client_id=<API-Key>&client_secret=<API-Secret>&redirect_uri=<Redirect-URI>&grant_type=authorization_code'
```

## Alternative Token Generation Methods

### Semi-Automated Approach

Apps can trigger authentication requests requiring manual approval:

1. Initiate auth request via Access Token Request API
2. User approves via mobile notification or developer dashboard
3. Token delivered to configured notifier URL
4. App stores token for subsequent use

### Manual Generation

For small utilities or occasional use:

1. Visit [Upstox Developer Apps](https://account.upstox.com/developer/apps)
2. Click app and select **Generate**
3. Copy and implement the token

## Extended Token Feature

Upstox supports extended tokens for long-term read-only access, valid for one year or until account revocation (whichever occurs first).

**Supported APIs:**

- Get Positions
- Get Holdings
- Get Order Details
- Get Order History
- Get Order Book

Extended tokens require enrollment through support for multi-client applications.

## Key Notes

- OAuth terminology: `client_id` = API Key; `client_secret` = API Secret
- Avoid using `.php` extensions in redirect URLs due to security filtering
- TOTP (Time-based One-Time Password) available as enhanced 2FA alternative
- Authorization codes expire after single use, regardless of token generation success
