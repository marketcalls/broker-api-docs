# Error Codes

> Source: https://api-docs.indstocks.com/errors/

## Error Response Format

All failed requests return a JSON body with this structure:

```json
{
  "status": "error",
  "message": "A human-readable error message providing details about the error.",
  "error_type": "TokenException"
}
```

> **Alternative shape.** The Instruments and Market Quotes endpoints return
> `{"message": "...", "success": false}` — with **no** `status` or `error_type` field. Handle
> both shapes when parsing errors.

## HTTP Status Code Conventions

| Range | Meaning |
|-------|---------|
| `2xx` | Request succeeded |
| `4xx` | Client-side error (malformed request, invalid auth, bad parameters) |
| `5xx` | Server-side error |

## General API Errors

| Error Type | HTTP Status | Description |
|------------|-------------|-------------|
| `InputException` | 400 Bad Request | The request is invalid — malformed JSON, missing parameters, or incorrect data types. |
| `TokenException` | 403 Forbidden (sometimes 401) | The provided access token is invalid, expired, or revoked. Re-authenticate. |
| `UserException` | 403 Forbidden | Authenticated user lacks permission — account status or missing segment activation. |
| `NotFoundException` | 404 Not Found | The requested endpoint or resource (e.g., a specific order ID) could not be found. |
| `MethodNotAllowedException` | 405 Method Not Allowed | Incorrect HTTP method used (e.g., GET instead of POST). |
| `DataException` | 400 Bad Request | Invalid parameters for market / historical data requests. |
| `NetworkException` | 503 Service Unavailable | Temporary issue reaching an upstream service (e.g., an exchange). Safe to retry. |
| `GeneralException` | 500 Internal Server Error | Unexpected server error. Report if persistent. |
| `ServiceUnavailableException` | 503 Service Unavailable | API down for maintenance or overloaded. |
| `GatewayTimeoutException` | 504 Gateway Timeout | Upstream service timeout. Safe to retry. |

## Rate Limiting

Exceeding a rate limit returns **`429 Too Many Requests`**. See
[API Conventions](03-conventions.md#rate-limits) for per-category limits.

## Token Generation Errors (TOTP)

Applies to the `POST /generate/token` endpoint only.

| Situation | Meaning | Action |
|-----------|---------|--------|
| Wrong MPIN | MPIN doesn't match the account | Fix the MPIN; not retryable as-is |
| Wrong / expired TOTP | Code mistyped, already used, or outside its validity window | Wait for the next code — **never retry the same code** |
| Throttled | Endpoint called more than once in 60 seconds | Reuse the existing token |
| Locked out | 5 wrong codes in 15 min (15-min lockout), or 3 lockouts in 1 hour (1-hour lockout) | Wait the full window; verify NTP sync |
| Clock drift | Server time mismatch against the TOTP window | Sync the host clock via NTP |
| TOTP disabled | Secret deleted from the dashboard | Re-run the dashboard TOTP setup |

See [Authentication & Users](04-authentication-users.md#method-2--totp-based-token-generation)
for the setup flow and limits.

## Order-Specific Errors

Order rejections typically return `OrderException` (400 Bad Request) with an RMS message:

| Message pattern | Meaning |
|-----------------|---------|
| `RMS: Margin exceeds ...` | Insufficient account margin |
| `RMS: Rule: Check ...` | A custom risk rule was triggered |
| `RMS: Blocked for ...` | Account / security blocked by RMS |
| `The instrument is not tradable.` | Security unavailable in the requested segment |
| `The quantity is not a multiple of the lot size.` | F&O order quantity must be a lot multiple |
| `The price is out of the circuit limit.` | Price exceeds the daily circuit bounds |
| `Order price must be a multiple of the tick size.` | Invalid price increment |
| `Market orders are blocked for this instrument.` | Use limit orders instead |
| `The order quantity exceeds the freeze limit.` | Exceeds the maximum single-order quantity |
| `Position could not be found.` | Order doesn't exist or is already completed |
| `The order is already pending...` | Order is awaiting exchange confirmation |

## Retry Guidance

**Safe to retry with backoff:** `NetworkException`, `GatewayTimeoutException`,
`ServiceUnavailableException`, other `5xx`, and `429`.

**Not retryable without fixing the request:** `InputException`, `TokenException`,
`UserException`, `NotFoundException`, `MethodNotAllowedException`, `DataException`.

- On `TokenException`, generate a fresh access token (dashboard or TOTP) and retry.
- On `429`, back off and add a client-side rate limiter.
- On `InputException` / `OrderException`, fix the request payload before retrying.

> ⚠️ **Never blindly retry order placement.** On a timeout or 5xx during `/order`, query the
> [Order Book](09-order-management.md#get-order-book) first to confirm the actual state —
> otherwise you risk duplicate orders.

## Quick Troubleshooting

| Situation | HTTP Code | Resolution |
|-----------|-----------|------------|
| All requests fail | 403 / 401 | Token empty, wrong, or expired — regenerate |
| Token stops working mid-day | 403 | Replaced or revoked by another process or the dashboard |
| `/generate/token` fails | — | Wrong MPIN/TOTP, 60-second throttle, lockout, or clock drift |
| A single request fails | 400 | Read `message` and validate against the endpoint docs |
| Failures only under load | 429 | Rate limit hit — implement backoff |
| Order rejected | 400 | Check the RMS message table above |
| Intermittent failures | 5xx | Transient — retry with backoff, reconcile via the Order Book |
