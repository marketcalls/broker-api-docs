# Access Token Request API

## Overview

The Access Token Request API enables secure, user-driven approval workflows for token generation. This mechanism facilitates secure communication by triggering a user-driven approval process.

## Request Flow

1. **Initiating the Request** - API invocation generates an access token request and notifies the user
2. **User Notification** - Alerts sent via in-app prompts and WhatsApp
3. **User Action** - User approves (token sent to webhook) or rejects (process terminated)

## Endpoint

**POST** `https://api.upstox.com/v3/login/auth/token/request/{client_id}`

### Required Parameters

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `client_id` | string | Path | API key from app generation |
| `client_secret` | string | Body | API secret (confidential) |

## Response Structure

**Success (200):**

```json
{
  "status": "success",
  "data": {
    "authorization_expiry": "1732226400000",
    "notifier_url": "https://initiator-webhook-endpoint"
  }
}
```

**Key Fields:**
- `authorization_expiry` - Token request validity (expires at 3:30 AM next day)
- `notifier_url` - Webhook endpoint for token delivery

## Webhook Payload

Upon user approval, the API sends to the configured notifier URL:

```json
{
  "client_id": "string",
  "user_id": "string",
  "access_token": "string",
  "token_type": "Bearer",
  "expires_at": "string",
  "issued_at": "string",
  "message_type": "access_token"
}
```

## Error Codes

| Code | Meaning |
|------|---------|
| UDAPI100069 | Invalid credentials (client_id/secret) |
| UDAPI1123 | Notifier URL not configured |
| UDAPI1124 | Non-individual user type |
| UDAPI1155 | App under review or rejected |
| UDAPI1157 | App expired |

## Authorization Expiry Window

Requests expire at 3:30 AM the following day unless approved earlier. Example: A request at 8:00 PM Tuesday expires at 3:30 AM Wednesday.
