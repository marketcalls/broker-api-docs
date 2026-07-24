# Exceptions and Errors

> Source: https://developer.hdfcsky.com/sky-docs/docs/error_structure

When interacting with HDFC Sky Open API, it's crucial to understand how errors and exceptions are handled. This guide provides an overview of the structure of error responses and how to handle exceptions effectively.

## HTTP Status Codes

HDFC Sky Open API utilizes standard HTTP status codes to communicate the outcome of requests. Below are common status codes related to errors and exceptions:

- **400 Bad Request:** The request was invalid or malformed.
- **401 Unauthorized:** Authentication credentials are missing or incorrect.
- **403 Forbidden:** The server understood the request, but it refuses to authorize it.
- **404 Not Found:** The requested resource could not be found.
- **422 Unprocessable Entity:** The server understands the content type of the request entity, but it was unable to process the contained instructions.
- **5xx Server Errors:** An error occurred on the server side.
