# Exceptions & Errors

> Source: https://shoonya.com/api-documentation (Exceptions & Errors)

## Common HTTP error codes

| Code | Error Description |
|---|---|
| 400 | Missing or bad request parameters or values |
| 403 | Session expired or invalidate. Must relogin |
| 404 | Request resource was not found |
| 405 | Request method (GET, POST etc.) is not allowed on the requested endpoint |
| 410 | The requested resource is gone permanently |
| 429 | Too many requests to the API (rate limiting) |
| 500 | Something unexpected went wrong |
| 502 | The backend OMS is down and the API is unable to communicate with it |
| 503 | Service unavailable; the API is down |
| 503 | Gateway timeout; the API is unreachable |
