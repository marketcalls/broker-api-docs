# Get Market Data Feed Authorized URL V3

## Overview

Provides a WebSocket connection URI for receiving real-time market data updates. Alternative method to acquire the `wss://` URL.

## Endpoint

**GET** (requires Bearer token in Authorization header)

## Request Headers

| Parameter | Required | Type | Purpose |
|-----------|----------|------|---------|
| Authorization | Yes | String | `Bearer access_token` |
| Accept | Yes | String | `application/json` |

## Response (200)

```json
{
  "status": "success",
  "data": {
    "authorized_redirect_uri": "wss://xyz.upstox.com/market-data-feeder/v3/upstox-developer-api/feeds?requestId=...&code=..."
  }
}
```

**Note:** The embedded `code` parameter is single-use only.
