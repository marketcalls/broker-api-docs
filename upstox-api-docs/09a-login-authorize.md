# Authorize API

## Overview

The authorization endpoint initiates a login flow that redirects users to Upstox's authentication page. Upon a successful user login, the user is then redirected to the specified `redirect_uri` with an authorization code.

## Endpoint

**GET** `https://api.upstox.com/v2/login/authorization/dialog`

## Query Parameters

| Parameter | Required | Type | Purpose |
|-----------|----------|------|---------|
| `client_id` | Yes | string | API key from app registration |
| `redirect_uri` | Yes | string | Post-authentication redirect URL (must match registered URI) |
| `state` | No | string | Optional parameter returned after authentication for state continuity |
| `response_type` | Yes | string | Must always be `code` |

## Response Format

**Success (HTTP 302):**

```
https://<redirect_uri>?code=mk404x&state=XX56849
```

| Element | Purpose |
|---------|---------|
| `code` | Required for generating access tokens via Get Token API |
| `state` | Returned if included in initial request |

## Error Handling

**Error Code:** UDAPI100068
- Message: Indicates invalid `client_id` or `redirect_uri` parameters

## Next Steps

The authorization code obtained here should be used with the Get Token API to acquire an access token for subsequent API requests.
