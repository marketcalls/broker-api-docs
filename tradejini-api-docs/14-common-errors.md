# Common Errors

All error responses share the same JSON envelope — regardless of whether the error originates at the API gateway (nginx) or the application layer:

```json
{ "s": "error", "msg": "Description of what went wrong" }
```

## Quick Reference

| Status | Msg | Origin | Retryable |
| --- | --- | --- | --- |
| `400` | `Bad request` | Gateway | No — fix the request |
| `400` | `Input validation failed. Kindly check your input contains required fields for the request` | Application | No — fix the request |
| `400` | `Internal Error occurred. Kindly try again.` | Application | Yes |
| `401` | `Unauthorized` | Gateway / Application | No — re-authenticate |
| `403` | `Forbidden` | Gateway | No — check IP whitelist and app permissions |
| `404` | `Resource not found` | Gateway | No — check the endpoint path |
| `405` | `Method not allowed` | Gateway | No — check the HTTP method |
| `429` | `Too many requests` | Gateway | Yes — back off and retry |
| `500` | `Internal server error` | Application | Yes — retry with backoff |
| `502` | `Bad gateway` | Gateway | Yes — retry with backoff |
| `503` | `Service unavailable` | Gateway | Yes — retry after delay |
| `504` | `Gateway timedout` | Gateway | Yes — retry with backoff |

## HTTP 400 — Bad Request

A 400 can come from two sources with different `msg` values.

### Gateway-level 400

The request was structurally invalid and rejected by the API gateway before reaching the application (e.g. malformed URL, unparseable body, unsupported `Content-Type`).

```json
{ "s": "error", "msg": "Bad request" }
```

| Cause | Resolution |
| --- | --- |
| `Content-Type: application/json` sent on a POST/PUT endpoint | Use `Content-Type: application/x-www-form-urlencoded` |
| `Content-Type` header missing on a POST/PUT endpoint | Add `Content-Type: application/x-www-form-urlencoded` |
| Malformed request URL or unparseable query string | Check URL encoding; special characters in query values must be percent-encoded |

### Application-level 400

The request reached the application but failed field-level validation.

```json
{ "s": "error", "msg": "Input validation failed. Kindly check your input contains required fields for the request" }
```

```json
{ "s": "error", "msg": "Internal Error occurred. Kindly try again." }
```

| Scenario | Bad value | Correct value |
| --- | --- | --- |
| Wrong `side` value | `"b"`, `"BUY"` | `"buy"` or `"sell"` |
| Wrong `type` value | `"LIMIT"`, `"sl"` | `"limit"`, `"market"`, `"stoplimit"`, `"stopmarket"` |
| Wrong `product` value | `"CNC"`, `"cnc"` | `"delivery"`, `"intraday"`, `"normal"` |
| Wrong `validity` value | `"DAY"` | `"day"`, `"ioc"`, `"eos"`, `"gtc"` |
| `limitPrice` missing for limit order | Omitted | Required when `type` is `"limit"` or `"stoplimit"` |
| `trigPrice` missing for stop order | Omitted | Required when `type` is `"stoplimit"` or `"stopmarket"` |
| Missing `twoFaTyp` on Individual Token endpoint | Field omitted | Pass `twoFaTyp=otp` or `twoFaTyp=totp` |

## HTTP 401 — Unauthorized

The request could not be authenticated. A single `msg: "Unauthorized"` is returned for all causes — use the sub-scenarios below to diagnose.

```json
{ "s": "error", "msg": "Unauthorized" }
```

| Scenario | Cause | Resolution |
| --- | --- | --- |
| **Wrong credentials** | Incorrect `client_id`, `password`, or `twoFa` value on the auth endpoint | Verify your API key in the Apps section; regenerate your OTP/TOTP; confirm `twoFaTyp` matches the value type (`otp` or `totp`) |
| **Token expired** | Access tokens are valid for **24 hours** — after expiry all authenticated calls return 401 | Re-authenticate using the Individual Token or OAuth token endpoint to obtain a fresh `access_token` |
| **Authorization header missing** | No `Authorization` header sent with the request | Add `Authorization: Bearer <api_key>:<access_token>` |
| **Authorization header malformed** | Wrong format — e.g. `Bearer <token_only>` or missing `Bearer` prefix | Use the exact format `Authorization: Bearer <api_key>:<access_token>` |
| **Static IP not whitelisted** | Request originates from an IP not registered during app creation (Individual Apps only) | Add your IP to the whitelist in the Apps section |
| **TOTP/OTP expired or wrong** | The 6-digit code in `twoFa` is incorrect or has expired | Generate a fresh TOTP code; OTP codes expire after 30–60 seconds |

## HTTP 403 — Forbidden

The request was authenticated but the caller does not have permission to access the resource.

```json
{ "s": "error", "msg": "Forbidden" }
```

| Cause | Resolution |
| --- | --- |
| **Static IP not whitelisted** | The authenticated token is valid but the originating IP address is not on the app's whitelist |
| **App not authorised for endpoint** | Your app registration does not include permission for this endpoint or segment |
| **Accessing another user's resource** | Attempting to query data that does not belong to the authenticated account |

> A 403 differs from 401: 401 means the server could not identify who you are; 403 means the server knows who you are but is denying access.

## HTTP 404 — Resource Not Found

The requested endpoint path does not exist on the server.

```json
{ "s": "error", "msg": "Resource not found" }
```

| Cause | Resolution |
| --- | --- |
| Incorrect endpoint path | Check the path against the API reference; paths are case-sensitive |
| Missing path parameter | e.g. `/api/mkt-data/scrips/symbol-store/{scripGroup}` requires `scripGroup` to be filled in |
| Wrong base URL | All requests must go to `https://api.tradejini.com/v2` — requests to `developer.tradejini.com` will not resolve API paths |

## HTTP 405 — Method Not Allowed

The endpoint exists but does not support the HTTP method used in the request.

```json
{ "s": "error", "msg": "Method not allowed" }
```

| Cause | Resolution |
| --- | --- |
| Using `POST` on a `GET`-only endpoint | Check the method column in the API reference for the endpoint |
| Using `GET` on a `POST`/`PUT` endpoint | Use the correct HTTP method |
| Using `DELETE` without the required query parameters | Ensure required query parameters (e.g. `orderId`) are included |

## HTTP 415 — Unsupported Media Type

The request body's `Content-Type` is not accepted by the endpoint. This error is returned by the application layer before nginx for incorrectly typed POST/PUT requests.

| Cause | Resolution |
| --- | --- |
| `Content-Type: application/json` sent on a POST/PUT endpoint | Change to `Content-Type: application/x-www-form-urlencoded` |
| `Content-Type` header missing on a POST/PUT endpoint | Add `Content-Type: application/x-www-form-urlencoded` |

> `GET` and `DELETE` endpoints use only query parameters and do not require a `Content-Type` header.

## HTTP 429 — Too Many Requests

The request was rejected by the rate-limiter. See [Rate Limits](https://developer.tradejini.com/docs/rate-limits) for the full limits table.

```json
{ "s": "error", "msg": "Too many requests" }
```

| Zone | Applies to | Limit | Scope |
| --- | --- | --- | --- |
| OTP limit | `POST /api-gw/oauth/individual-token-v2` | 3 req/sec | Per IP address |
| API key limit | OAuth token exchange and API-key-only endpoints | 100 req/sec | Per `api_key` |
| Data fetch limit | Market data and account data endpoints | 100 req/sec | Per auth token |
| Place Order limit | `POST /api/oms/place-order` | 10 req/sec | Per auth token |
| General API limit | All other authenticated endpoints | 10 req/sec and 400 req/min | Per auth token |

**Resolution:** Implement exponential backoff — wait 1s, then 2s, then 4s between retries. Do not retry immediately on 429.

## HTTP 500 — Internal Server Error

An unexpected error occurred inside the application. The request was valid but could not be processed.

```json
{ "s": "error", "msg": "Internal server error" }
```

| Cause | Resolution |
| --- | --- |
| Transient application fault | Retry with exponential backoff (1s → 2s → 4s) |
| Dependency failure (database, downstream service) | Retry after a short delay; check [Tradejini status](https://cubeplus.tradejini.com/) |
| Persistent 500 on a specific endpoint | Contact [Tradejini support](https://cubeplus.tradejini.com/faq) with the full request details and timestamp |

## HTTP 502 — Bad Gateway

The API gateway received an invalid response from the upstream application server. The application may be restarting or temporarily unreachable.

```json
{ "s": "error", "msg": "Bad gateway" }
```

| Cause | Resolution |
| --- | --- |
| Upstream server restarting or crashing | Retry with exponential backoff; typically resolves within seconds |
| Deployment in progress | Wait 30–60 seconds and retry |
| Persistent 502 | Check [Tradejini status](https://cubeplus.tradejini.com/) |

## HTTP 503 — Service Unavailable

The server is temporarily unable to handle the request, usually due to maintenance or overload.

```json
{ "s": "error", "msg": "Service unavailable" }
```

| Cause | Resolution |
| --- | --- |
| Scheduled maintenance | Check [Tradejini status](https://cubeplus.tradejini.com/) for maintenance windows |
| Server overload | Retry with exponential backoff and reduced request frequency |
| Market hours startup | Some services start shortly before market open; retry after a short delay |

## HTTP 504 — Gateway Timeout

The API gateway did not receive a response from the upstream server within the allowed time.

```json
{ "s": "error", "msg": "Gateway timedout" }
```

| Cause | Resolution |
| --- | --- |
| Upstream server took too long to respond | Retry the request; consider whether the operation may have partially succeeded (e.g. check the order book after a 504 on place-order before retrying) |
| Network congestion between gateway and application | Retry with backoff |
| Request processing unusually slow | For order operations, always verify state via `GET /api/oms/orders` or `GET /api/oms/history` before assuming failure |

> **Important for order operations:** A 504 on `POST /api/oms/place-order` does **not** confirm that the order was rejected. The order may have been placed before the timeout. Always check `GET /api/oms/orders` before retrying a place-order call to avoid duplicate orders.

## Common Integration Mistakes

| Symptom | Most likely cause |
| --- | --- |
| Every request returns `401` | Token expired — re-authenticate; or static IP not whitelisted |
| Auth returns `401` despite correct password | Wrong `twoFaTyp` — use `totp` for authenticator app, `otp` for SMS/email |
| Auth returns `403` | Static IP not whitelisted — register your IP in the Apps section |
| Request returns `404` | Wrong base URL (`developer.tradejini.com` vs `api.tradejini.com/v2`) or wrong path |
| POST returns `400 Bad request` | Missing or wrong `Content-Type: application/x-www-form-urlencoded` |
| POST returns `400` with validation message | Missing required field or wrong enum value — check the endpoint's Request Body section |
| Successful auth but all subsequent calls return `401` | Authorization header format wrong — must be `Bearer <api_key>:<access_token>` (two parts separated by colon) |
| Works locally, fails in production | Static IP not whitelisted — register your production server IP |
| `429` on auth endpoint only | OTP rate limit is IP-based (3 req/sec) and separate from the general per-token limits |
| `504` after placing an order | Do **not** retry immediately — check `GET /api/oms/orders` first to avoid duplicate orders |
| `s: "no-data"` instead of an array | No records exist for the session (e.g. no open orders today) — this is a normal empty-state response, not an error |
