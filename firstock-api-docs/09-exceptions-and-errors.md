# Exception & Errors

> Source: https://firstock.in/api/docs/exception-errors/

> This page provides a comprehensive look at how Firstock APIs handle exceptions and error responses—along with best practices for catching and resolving issues in your integration.

## Overview

Whenever a Firstock API call encounters an issue—such as missing parameters, invalid credentials, or unavailable resources—it returns a **failed** response instead of a traditional success object. This failed response includes crucial information you need to diagnose and fix the problem quickly, such as:

- A ***code*** or status code (often *"400"*, *"401"*, etc.).
- A descriptive ***name*** or label (like *"BADREQUEST"*).
- An ***error*** object containing specific details about which field or parameter caused the issue.

By systematically inspecting these fields, you can:

- Prompt your user to correct a missing or malformed input.
- Refresh or renew a session token (*jKey*) if it has expired.
- Log unexpected server or internal errors for deeper debugging.

## Common Error Response Structure

When the ***status***field is *"failed"*, the response typically contains the following keys:

| Field | Data Type | Description | Example |
|---|---|---|---|
| *status* | string | Indicates a failed request, typically set to *"failed"*. | *"failed"* |
| *code* | string or integer | Error or HTTP-like status code (*"400"*, *"401"*, *"404"*, *"429"*, etc.). | *"400"* |
| *name* | string | A short name or label describing the error (e.g., *"BAD_REQUEST"*, *"INVALID_JKEY"*). | *"MISSING_FIELD", "INVALID_USERID"* |
| *error* | object | An object holding more fine-grained details about the field or reason for failure. | See **Error Object** section below |

## Error Object Structure

The ***error***object often looks like this:

```
"error": {
  "field": "exchange",
  "message": "required field is empty or missing: exchange"
}
```

- ***field***: Specifies which parameter caused the error (like *"exchange"*, *"jKey"*, or *"tradingSymbol"*).
- ***message***: Explains the nature of the error, e.g., **“cannot be empty”**, **“is invalid”**, or **“expired token”**.

## Typical HTTP Error Codes

While Firstock APIs generally return a code field in the response JSON, it often maps closely to common HTTP status codes:

- **400 Bad Request**: The request was invalid, such as missing required parameters or using incorrect data types.
- **401 Unauthorized**: Authentication failed—often triggered by an invalid or expired *jKey* or missing credentials.
- **403 Forbidden**: The user is authenticated but not authorized to perform this action.
- **404 Not Found**: The resource or endpoint doesn’t exist (or the symbol/order was not found).
- **429 Too Many Requests**: The client has hit the **API rate limit**. You should slow down or implement a backoff strategy.
- **500 Internal Server Erro**r: A server-side issue occurred—possibly a temporary service glitch.
- **503 Service Unavailable**: The server is overloaded or down for maintenance; retry later.

You may see these codes in the *code* field, or an equivalent custom label (e.g., *"RATELIMITEXCEEDED"*).

## API Rate Limit

Firstock imposes **rate limits** to ensure fair usage and protect service stability. Common behaviors to expect:

- **HTTP 429 (Too Many Requests)**: Indicates you have exceeded the number of requests allowed within a certain time window.
- **Error Response**: Could include a **name** like **"RATE_LIMIT_EXCEEDED"** or **"TOO_MANY_REQUESTS"**.
- **Backoff Strategy**: Once you get a 429, stop sending requests for a short cooling period (e.g., a few seconds) before retrying.

**Best Practices for Rate Limit Handling:**

1. **Implement Throttling**: In your client or server code, track how many requests you’ve made in a window—pause or slow down if you’re nearing the limit.
2. **Handle 429 Errors Gracefully**: Provide a user-friendly message if you’re rate-limited—e.g., “We’re sending too many requests at once. Please try again in a moment.”

  3.**Batch Requests Where Possible**: Endpoints like “get multi quotes” can fetch multiple symbols in one call—reducing the total number of requests.

| Endpoint | Rate-Limit |
|---|---|
| Quote | 3 req/second |
| Historical Candle | 3 req/second |
| All other endpoints | 10 req/second |
| Order Placement | 10 req/second |

**Note:** Quote API rate limit has been reduced from 4 req/sec to 1 req/sec

## Typical Error Cases

Here are some of the most common error scenarios across multiple Firstock APIs:

1. **Missing or Invalid Field**

  - **Cause**: A required parameter is omitted or set to an invalid value.
  - **Example**:

```json
{
  "status": "failed",
  "code": "400",
  "name": "BAD_REQUEST",
  "error": {
    "field": "tradingSymbol",
    "message": "Trading Symbol is required"
  }
}
```

1. **Expired** **or** **Invalid** **Session** **Token** (***jKey***)

  - **Cause**: The *jKey* or *susertoken* was not included, or it’s expired.
  - **Example**:

```json
{
  "status": "failed",
  "code": "401",
  "name": "INVALID_JKEY",
  "error": {
    "field": "jKey",
    "message": "jKey parameter is invalid"
  }
}
```

- Resolution: Prompt the user to re-login or refresh their token.

1. **Unauthorised Access**

  - **Cause**: The *jKey* or *susertoken* was not included, or it’s expired.
  - **Example**:Code *403* or a custom label like *"FORBIDDEN"*.
2. **Resource Not Found**

  - **Cause:** The symbol, order, or resource doesn’t exist or was spelled incorrectly.
  - **Example**:

```json
{
  "status": "failed",
  "code": "404",
  "name": "RESOURCE_NOT_FOUND",
  "error": {
    "field": "orderNumber",
    "message": "order not found or invalid"
  }
}
```

1. **Internal Server Error**

  - **Cause**: An unexpected issue on the server side (e.g., database down, unexpected bug).
  - **Resolution**:Retry the request later, and/or contact Firstock support if the problem persists.

## Best Practices for Handling Errors

1. **Check status**

  - Always inspect if *status* is *"success"* or *"failed"* before proceeding with your logic.
2. **Parse the error Object**

  - Identify which field caused the issue (*error.field*) and display or log (*error.message*) so users or developers know how to fix it.
3. **Maintain Session Tokens**

  - If you receive an error related to *"INVALIDJKEY"* or *"INVALIDUSERID"*, prompt a re-login or refresh your token.
  - Implement graceful handling for session expiration in your client app.
4. **Log & Monitor**

  - Capture error responses in logs or analytics to spot patterns—like repeated missing fields or consistent invalid tokens.
5. **User Feedback**

  - Provide clear messaging to end users. For instance, if *field* = *"password"* and *message* = *"Password cannot be empty"*, you can highlight that input field.
6. **Retry Logic**

  - For transient errors (e.g., server timeouts or internal errors), consider retrying after a short delay. Avoid infinite loops by capping retries.

## Example Integration Flow

Imagine you're placing order via the **Place Order API:**

- **User Submits** an order.
- **Check Response:**

  - If *status* = *"success"*, process the data (e.g., *orderNumber*).
  - If *status* = *"failed"*, parse *error.field* and *error.message* to correct the request or re-prompt the user.
- **Token Issues:**

  - If the error name is *"INVALIDJKEY"*, refresh or request new login credentials.

## Conclusion

Understanding and handling errors consistently is critical for building a smooth, user-friendly trading application. The **Firstock** APIs use a **common error structure** across all endpoints, making it simpler for developers to:

- Identify problematic fields or parameters.
- Address authentication or session timeouts quickly.
- Provide detailed feedback to end-users, ensuring they can correct their input or re-authenticate as needed.

By following the **Best Practices** outlined above—logging errors, retrying where appropriate, and always parsing the *error*object thoroughly—you’ll create a more reliable and robust integration with the Firstock platform.
