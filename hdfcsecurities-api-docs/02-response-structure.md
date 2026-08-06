# API Response Structure

> Source: https://developer.hdfcsec.com/ir-docs/docs/response

When you make requests to InvestRight Open API endpoints, you'll receive responses in a structured format. Below is an overview of the typical structure of API responses:

## HTTP Status Codes

InvestRight Open API uses standard HTTP status codes to indicate the success or failure of a request. Here are some common status codes you may encounter:

- **200 OK:** The request was successful.
- **400 Bad Request:** The request was invalid or malformed.
- **401 Unauthorized:** Authentication is required to access the resource.
- **404 Not Found:** The requested resource could not be found.
- **5xx Server Errors:** An error occurred on the server side.

## Observed Body Envelope

The official page documents only status codes. In practice every trading endpoint in this
documentation returns one of the following two envelopes:

```js
{
    "status": "success",
    "data": { ... }        // object or array, endpoint dependent
}
```

The LTP endpoint (see [Market Data - LTP](16-market-data-ltp.md)) uses a different envelope:

```js
{
    "data": [ ... ],
    "meta": {
        "statusCode": "OK",
        "statusMsg": "OK"
    }
}
```
