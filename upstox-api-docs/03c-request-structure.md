# Request Structure

## Overview

The standard template for Upstox API calls.

## Request Format

```bash
curl -X [API_METHOD] \
    'https://api.upstox.com/v2/[API_ENDPOINT]' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer [YOUR_ACCESS_TOKEN]' \
    [CONTENT_TYPE_HEADER] \
    [REQUEST_PAYLOAD]
```

## Key Components

### Required Elements
- **HTTP Method:** GET, POST, PUT, DELETE
- **API Endpoint:** Specific resource paths like `/user/profile` or `/order/place`
- **Access Token:** Personal access token for authentication
- **Base URL:** `https://api.upstox.com/v2/` (or `/v3/` for newer endpoints)

### Conditional Headers
- For JSON payloads: `Content-Type: application/json`
- For form-encoded data: `Content-Type: application/x-www-form-urlencoded`
- Omit content type when not sending a body

### Response Format
All endpoints return `application/json`

## Important
All API requests must be encoded using Standard URL Encoding to handle special characters and non-ASCII content properly.
