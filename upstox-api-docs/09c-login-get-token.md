# Get Token API

## Overview

The Get Token API enables developers to exchange an authorization code for an access token while retrieving the user's profile information simultaneously.

## Token Validity

The `access_token` obtained through this API has a specific validity period that lasts until **3:30 AM** the following day, regardless of the time it was generated. The authorization code itself is single-use only.

## Endpoint

**POST** `https://api.upstox.com/v2/login/authorization/token`

## Request Headers

- `accept: application/json`
- `Content-Type: application/x-www-form-urlencoded`

## Request Parameters

| Parameter | Required | Type | Details |
|-----------|----------|------|---------|
| code | Yes | string | Unique parameter from successful Authorize API authentication |
| client_id | Yes | string | API key from app generation |
| client_secret | Yes | string | API secret from app generation (confidential) |
| redirect_uri | Yes | string | URL provided during app setup |
| grant_type | Yes | string | Must be `authorization_code` |

## cURL Example

```bash
curl -X 'POST' 'https://api.upstox.com/v2/login/authorization/token' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'code=<Auth-Code>&client_id=<API-Key>&client_secret=<API-Secret>&redirect_uri=<Redirect-URI>&grant_type=authorization_code'
```

## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| email | string | User's email address |
| exchanges | string[] | Enabled exchanges (NSE, NFO, BSE, CDS, BFO, BCD) |
| products | string[] | Product types (I, D, CO, MTF) |
| broker | string | Broker ID |
| user_id | string | Unique user identifier (UCC) |
| user_name | string | User's name |
| order_types | string[] | Enabled order types (MARKET, LIMIT, SL, SL-M) |
| user_type | string | User role (individual for retail) |
| poa | boolean | Power of attorney authorization status |
| is_active | boolean | Account active status |
| access_token | string | Authentication token for API requests |
| extended_token | string | Token for prolonged read-only access |

## Error Codes

| Code | Description |
|------|-------------|
| UDAPI100069 | Invalid client credentials |
| UDAPI100070 | Invalid redirect_uri |
| UDAPI100057 | Invalid authorization code |
