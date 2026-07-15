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
| `TokenException` | 403 Forbidden | The provided access token is invalid, expired, or revoked. Re-authenticate. |
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

## Handling Guidance

- On `TokenException`, generate a fresh access token and retry.
- On `NetworkException`, `GatewayTimeoutException`, or `ServiceUnavailableException`, retry
  with backoff — these are transient.
- On `429`, back off and respect the rate limits.
- On `InputException` / `OrderException`, fix the request payload before retrying.
