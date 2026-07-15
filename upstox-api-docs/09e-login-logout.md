# Logout API

## Overview

The Logout API endpoint allows developers to terminate a user's active session, invalidating the current access token. Users must re-authenticate to perform additional operations after logging out.

## Endpoint

**DELETE** `https://api.upstox.com/v2/logout`

## Request Headers

- `Content-Type: application/json`
- `Accept: application/json`
- `Authorization: Bearer {your_access_token}`

## cURL Example

```bash
curl --location --request DELETE 'https://api.upstox.com/v2/logout' \
  --header 'Content-Type: application/json' \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer {your_access_token}'
```

## Response

**Status Code:** 200

```json
{
  "status": "success",
  "data": true
}
```

| Field | Type | Description |
|-------|------|-------------|
| status | string | Indicates request outcome; typically returns `success` |
| data | boolean | Confirms whether the logout action succeeded |
