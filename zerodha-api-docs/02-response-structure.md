# Response Structure

All responses from the API server are JSON with content-type `application/json`.

## Successful Responses

HTTP 200 OK:

```json
{
    "status": "success",
    "data": {}
}
```

The `data` key houses the complete response payload.

## Failed Responses

HTTP 40x or 50x status codes:

```json
{
    "status": "error",
    "message": "Error message",
    "error_type": "GeneralException"
}
```

An optional `data` field may provide additional context.

## Data Type Standards

- JSON values: string, integer, float, boolean
- Timestamps: `yyyy-mm-dd hh:mm:ss` in IST (UTC+5:30)
- Dates: `yyyy-mm-dd` format

## Request Formats

- **GET/DELETE:** Query parameters
- **POST/PUT:** Form-encoded data (or JSON for margin endpoints)
