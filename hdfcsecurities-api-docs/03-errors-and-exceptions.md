# Error and Exception Handling

> Source: https://developer.hdfcsec.com/ir-docs/docs/error_structure

When interacting with InvestRight Open API, it's crucial to understand how errors and exceptions are handled. This guide provides an overview of the structure of error responses and how to handle exceptions effectively.

## HTTP Status Codes

InvestRight Open API utilizes standard HTTP status codes to communicate the outcome of requests. Below are common status codes related to errors and exceptions:

- **400 Bad Request:** The request was invalid or malformed.
- **401 Unauthorized:** Authentication credentials are missing or incorrect.
- **403 Forbidden:** The server understood the request, but it refuses to authorize it.
- **404 Not Found:** The requested resource could not be found.
- **422 Unprocessable Entity:** The server understands the content type of the request entity, but it was unable to process the contained instructions.
- **5xx Server Errors:** An error occurred on the server side.

## Order-level Rejection Reasons

The official documentation does not publish a rejection code table. Order-level failures surface
through the order book instead:

| Field | Meaning |
| --- | --- |
| `status` | Order status — a rejected order reports `Rejected` here |
| `status_message` | Rejection or RMS error reason |
| `status_message_raw` | Raw (unmapped) status message from the OMS |

See [Order Book](10-order-book.md) and [Single Order Status](11-single-order.md).

The `ErrorCode` enum shipped in the WebSocket Protobuf schema (`GenericDTO3.proto`) is the closest
thing to a published rejection-code list — it enumerates the OMS/RMS and exchange rejection codes
that can appear on the streamed `Order` message. See
[Market Data - WebSocket](17-websocket.md#appendix-genericdto-proto-schema).
