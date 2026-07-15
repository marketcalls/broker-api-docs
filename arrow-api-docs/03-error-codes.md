> Source: https://docs.arrow.trade/rest-api/error-codes/

# Error Codes

Error codes are standardized identifiers that help developers quickly understand and handle different types of failures in API requests. When an API call fails, the system returns a structured error response containing both an HTTP status code and a specific error code to provide precise information about what went wrong.

## Understanding Error Responses

Every error response follows this format:

**Error Response Structure**

```json
{
    "status": "error",
    "message": "Human-readable error description",
    "errorCode": "STANDARD_ERROR_CODE"
}
```

The error code serves multiple purposes:

  * **Programmatic Handling** \- Allows your application to respond differently to different error types
  * **Debugging** \- Helps developers quickly identify the root cause of issues
  * **User Experience** \- Enables appropriate user-facing error messages
  * **Monitoring** \- Facilitates error tracking and system health monitoring

## Complete Error Code Reference

### Client Errors (4xx)

These errors occur due to issues with the client request - invalid parameters, authentication problems, or malformed requests.

HTTP Status | Error Code | Error Message | Description | Common Causes
---|---|---|---|---
`400` | `BAD_REQUEST_ERROR` | BadRequestError | Missing or invalid request parameters or values | • Missing required fields
• Invalid data format
• Malformed JSON
• Invalid parameter values
`401` | `UNAUTHORIZED` | UnAuthorized | Your session has expired. You must relogin to access the resource | • Expired authentication token
• Missing API key
• Invalid credentials
• Session timeout
`403` | `FORBIDDEN` | Forbidden | You don't have permission to access this resource | • Insufficient user privileges
• Resource access restrictions
• Account limitations
`404` | `NOT_FOUND_ERROR` | NotFoundError | The requested resource could not be found | • Invalid endpoint URL
• Resource has been deleted
• Incorrect resource ID
`405` | `METHOD_NOT_ALLOWED` | Forbidden | The requested HTTP method is not allowed for this endpoint | • Using GET instead of POST
• Using POST on read-only endpoint
• Incorrect HTTP verb
`429` | `TOO_MANY_REQUESTS` | TooManyRequests | Rate limit exceeded - too many requests in a given time period | • Exceeding API rate limits
• Burst request patterns
• Multiple concurrent connections

### Server Errors (5xx)

These errors indicate problems on the server side that are typically outside of the client's control.

HTTP Status | Error Code | Error Message | Description | Resolution
---|---|---|---|---
`500` | `INTERNAL_ERROR` | InternalError | An unexpected error occurred on the server | • Retry the request after a delay
• Contact support if persistent
• Check system status page
`502` | `OMS_ERROR` | OMSError | The Order Management System (OMS) is down or unreachable | • Retry after a few minutes
• Check OMS system status
• Use alternative endpoints if available

## Error Code Categories

### Authentication & Authorization

  * `UNAUTHORIZED` \- Session or credential issues
  * `FORBIDDEN` \- Permission and access control issues

### Request Validation

  * `BAD_REQUEST_ERROR` \- Invalid request format or parameters
  * `NOT_FOUND_ERROR` \- Resource doesn't exist
  * `METHOD_NOT_ALLOWED` \- Incorrect HTTP method

### Rate Limiting

  * `TOO_MANY_REQUESTS` \- API usage limits exceeded

### System Issues

  * `INTERNAL_ERROR` \- General server problems
  * `OMS_ERROR` \- Specific service unavailability

## Troubleshooting Guide

### Common Solutions by Error Type

#### `BAD_REQUEST_ERROR`

  1. **Validate request payload** \- Ensure all required fields are present
  2. **Check data formats** \- Verify dates, numbers, and other formatted fields
  3. **Review API documentation** \- Confirm parameter names and types
  4. **Test with minimal payload** \- Start with basic required fields only

#### `UNAUTHORIZED`

  1. **Check authentication token** \- Verify token is valid and not expired
  2. **Refresh session** \- Re-authenticate if session has timed out
  3. **Verify API key** \- Ensure API key is correctly configured
  4. **Check token format** \- Confirm proper Bearer token format

#### `TOO_MANY_REQUESTS`

  1. **Review rate limits** \- Check your current usage against limits
  2. **Implement request queuing** \- Space out API calls appropriately
  3. **Use bulk operations** \- Combine multiple operations where possible
  4. **Consider caching** \- Reduce redundant API calls

#### `INTERNAL_ERROR` / `OMS_ERROR`

  1. **Retry the request** \- Often temporary issues resolve quickly
  2. **Check system status** \- Verify if there are known service issues
  3. **Contact support** \- Report persistent errors with request details
  4. **Implement fallback logic** \- Use cached data or alternative workflows

Pro Tips

  * Always log the full error context, not just the error message
  * Set up alerts for error rate spikes or new error types
  * Monitor error patterns to identify systemic issues
  * Include request IDs in logs for easier debugging
