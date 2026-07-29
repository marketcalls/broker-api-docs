# Request & Responses

> Source: https://firstock.in/api/docs/request-responses/

> This page provides a detailed overview of Firstock’s API response format, referencing the common fields you’ll see across multiple endpoints—whether the request succeeds or fails.

## Overview

When you call a Firstock API endpoint, you’ll receive a JSON response that typically contains:

- A ***status*** field, indicating *success* or *failed*.
- A ***message*** field, providing a short description of the outcome.
- An optional **code** field—often a string or number resembling HTTP status codes (e.g., *"400"*, *"401"*, *"429"*).
- A ***data*** field (on success) or an ***error*** object (on failure).

With this standardized approach, you can quickly determine if the request was successful, handle any returned data, or parse an error object to diagnose issues.

## Common Code Response

| Code | Name (If Present) | HTTP Equivalent | Meaning / Typical Causes | Resolution |
|---|---|---|---|---|
| **200** | N/A (Success) | **200 OK** | - Indicates a successful request. - Request processed without errors. | - No action needed aside from handling the data in data field. |
| **400** | *BAD_REQUEST*, *MISSING_FIELD* | **400 Bad Request** | - Missing or malformed fields in the request. - Invalid JSON or parameter values. | - Check which field caused the error in *error.field*. - Supply valid data or correct the missing fields. |
| **401** | *INVALID_JKEY*, *UNAUTHORIZED* | **401 Unauthorized** | - *jKey* (session token) is invalid or expired. - Missing user credentials. | - Re-authenticate the user. - Prompt login or refresh tokens. |
| **403** | FORBIDDEN | **403 Forbidden** | - User lacks permission for this operation. - Credential is valid, but privileges are insufficient. | - Verify user privileges. - Contact support if user needs access. |
| **404** | *RESOURCE_ NOT_FOUND* | **404 Not Found** | - The endpoint, symbol, or order does not exist. - Possibly a misspelled path or parameter. | - Confirm correct endpoint or resource. - Check the *tradingSymbol* or order number. |
| **429** | *RATE_LIMIT _EXCEEDED* | **429 Too Many Requests** | - Client has exceeded the allowed number of requests in a given time window. | - Implement client-side throttling. - Wait before retrying (backoff strategy). |
| **500** | *INTERNAL_ SERVER_ERROR* | **500 Internal Server Error** | - Unexpected server issue. - Temporary glitch or unhandled exception on the server side. | - Retry after a brief delay. - If persistent, contact Firstock support. |
| **503** | *SERVICE_ UNAVAILABLE* | **503 Service Unavailable** | - The service is down or overloaded. - Scheduled maintenance or server overload. | - Try again after a short wait. - Look for maintenance announcements from Firstock. |

## Success Responses

When an API call is **successful**, you’ll see a minimal set of fields confirming the outcome and providing the requested data.

```json
{
  "status": "success",
  "message": "Operation successful",
  "data": {
    // The payload, varying by endpoint
  }
}
```

## Fields in a Success Response

| Field | Data Type | Description | Example |
|---|---|---|---|
| *status* | string | Always *"success"* for a successful request. | *"success"* |
| *message* | string | A short description or confirmation of the operation’s outcome. | *"Login successful"* |
| *data* | object or array | The primary response payload, whose structure varies by endpoint. | e.g., user profile, quote data, etc. |

->Some endpoints may return additional top-level fields (like *"code"*) even on success, but commonly you’ll see *status*, *message*, and *data*.

## Failure (Error) Responses

If an API call fails due to invalid input, expired tokens, or any other issue, the response includes:

- ***status*** set to *"failed"*.
- An optional ***code*** resembling HTTP status codes (e.g., *"400"*, *"401"*, *"429"*).
- A name or short label describing the error category.
- An ***error*** object detailing which field or parameter caused the failure.

**For a deep dive into parsing and handling errors, see the** Exception & Error Handling **page**.

## Fields in an Error Response

```json
{
  "status": "failed",
  "code": "400",
  "name": "BAD_REQUEST",
  "error": {
    "field": "exchange",
    "message": "required field is empty or missing: exchange"
  }
}
```

| Field | Data Type | Description | Example |
|---|---|---|---|
| *status* | string | Typically *"failed"* when the request cannot be processed. | *"failed"* |
| *code* | string or integer | Numeric or string code resembling HTTP status codes (*"400"*, *"401"*, *"404"*, *"429"*, etc.). | *"400"* |
| *name* | string | Short label describing the error type (e.g., *"BAD_REQUEST"*, *"INVALID_JKEY"*). | *"MISSING_FIELD", "RATE_LIMIT_EXCEEDED"* |
| *error* | object | Object describing which field triggered the error and a clarifying message. | See **Error Object** below |

**Error Object**

```
"error": {
  "field": "tradingSymbol",
  "message": "Trading Symbol is required"
}
```

- ***field***: Indicates which parameter or resource caused the error (e.g., *"tradingSymbol"*, *"jKey"*).
- ***message***: Explains the nature of the error—e.g., “cannot be empty,” “is invalid,” “expired token,” or “API rate limit exceeded.”

## Best Practices & Recommendations

1. **Check** ***status***

  - Always verify if status is *"success"* or *"failed"* before processing data.
2. **Use** ***data*** **Correctly**

  - If *status* = *"success"*, parse *data* for the payload (e.g., quotes, user info, order details).
3. **Inspect** ***error*** **Fields**

  - If *status* = *"failed"*, parse *error.field* and *error.message* to pinpoint the cause.
4. **Respect Rate Limits**

  - If you encounter *code* = *"429"*, reduce requests or adopt a backoff to avoid spamming the server.
5. **Maintain Authentication**

  - *code* = *"401"* or a name like *"INVALIDJKEY"* means your session token (*jKey*) is expired or invalid—prompt re-login or refresh the token.
6. **Provide User Feedback**

  - Display descriptive error messages. For example, if *field* = *"password"*, show “Your password cannot be empty.”
7. **Logging & Monitoring**

  - Capture all failed responses in logs for debugging or analytics. Patterns in errors (e.g., repeated missing fields) can highlight UI or user flow issues.

## Conclusion

A consistent **response format**—covering both **success** and **failure** cases—ensures you can seamlessly integrate Firstock’s APIs into your application. By following these guidelines:

- You’ll handle **success** responses by parsing *data*.
- You’ll manage **failed** responses by inspecting *status*, *code*, *name*, and especially the *error* object.
- You’ll respect **API rate limits** and maintain **valid session tokens**, resulting in a more stable, user-friendly trading experience.

For further information, refer to the Exception & Error Handling page for a deeper look into error parsing or consult Firstock’s official documentation for advanced usage.
