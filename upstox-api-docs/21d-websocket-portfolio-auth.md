# Get Portfolio Stream Feed Authorized URL

## Overview

Retrieves the WebSocket connection URI for real-time portfolio updates.

## Request Headers

| Parameter | Required | Format |
|-----------|----------|--------|
| Authorization | Yes | `Bearer access_token` |
| Accept | Yes | `application/json` |

## Query Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| update_types | No | Comma-separated: `order`, `gtt_order`, `position`, `holding` |

## Response (200)

```json
{
  "status": "success",
  "data": {
    "authorized_redirect_uri": "wss://xyz.upstox.com/upstox-developer-api/order-updates/feed?requestId=...&code=..."
  }
}
```

**Note:** The `code` parameter is single-use. The camelCase field `authorizedRedirectUri` is deprecated.
