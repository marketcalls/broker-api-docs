# User Authentication and Profile

## Login Flow

1. Direct users to: `https://kite.zerodha.com/connect/login?v=3&api_key=xxx`
2. On successful login, system redirects to your registered URL with `request_token`
3. POST to `/session/token` with `api_key`, `request_token`, and `checksum`
4. Receive `access_token` for subsequent requests

### Checksum Generation

SHA-256 hash of: `api_key + request_token + api_secret`

## Token Exchange

**POST** `/session/token`

### Parameters

| Parameter | Description |
|-----------|-------------|
| api_key | Your API key |
| request_token | Token from login redirect |
| checksum | SHA-256(api_key + request_token + api_secret) |

### Response

- `access_token` - Authentication token (expires 6 AM next day)
- `user_id` - User identifier
- `exchanges` - NSE, NFO, BFO, CDS, BSE, MCX, BCD, MF
- `products` - CNC, NRML, MIS, BO, CO
- `order_types` - MARKET, LIMIT, SL, SL-M

## Request Authorization

All requests require the HTTP `Authorization` header:

```
Authorization: token api_key:access_token
```

## Endpoints

### Get Profile

**GET** `/user/profile`

Returns user information without tokens.

### Get Margins

**GET** `/user/margins` - All segments

**GET** `/user/margins/:segment` - Specific segment (equity/commodity)

Returns detailed fund allocation including available cash, margin utilization, and exposure metrics.

### Logout

**DELETE** `/session/token`

Invalidates the session, requiring fresh authentication.
