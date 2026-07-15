# Exceptions and Errors

## Exception Types

| Exception | Description |
|-----------|-------------|
| **TokenException** | Session expired or invalidated (HTTP 403). Requires re-authentication. |
| **UserException** | Account-related failures |
| **OrderException** | Order placement failures or data retrieval issues |
| **InputException** | Missing required fields or invalid parameter values |
| **MarginException** | Insufficient funds for order execution |
| **HoldingException** | Insufficient holdings for sell orders |
| **NetworkException** | API unable to communicate with OMS |
| **DataException** | Internal system error; API cannot process OMS response |
| **GeneralException** | Unclassified errors (rare) |

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 400 | Missing or bad request parameters or values |
| 403 | Session expired; re-authentication required |
| 404 | Resource not found |
| 405 | HTTP method not allowed |
| 410 | Resource permanently removed |
| 429 | Rate limit exceeded |
| 500 | Unexpected server error |
| 502 | Backend OMS unavailable |
| 503 | API service down |
| 504 | Gateway timeout |

## Rate Limits

| Endpoint | Limit |
|----------|-------|
| Quote | 1 request/second |
| Historical candle | 3 requests/second |
| Order placement | 10 requests/second |
| All other endpoints | 10 requests/second |

**Additional restrictions:**
- 400 orders/minute maximum
- 5,000 orders/day per user/API key
- 25 order modifications maximum before cancellation required
