# Response Formats

> Source: https://docs.delta.exchange/#response-formats

To ensure that you are effectively using the api, we encourage you to go through this section. 

1. All responses coming from the server, either from rest api or socket rpc calls will have the following success and error formats.
2. All timestamps reported in the apis will be in microseconds
3. All big decimal values are sent as string

```json
// The new format supports sending meta data alongside response body. 
// Success format
{
  "success": true,
  "result": {},         // response body
  "meta": {
    "after": "...",       // cursor for pagination, is returned in meta
    "before": null,
  },
}

// Error Format
{
  "success": false,
  "error": {
    "code": "insufficient_margin",             // error code
    "context": {                              // error context
      "additional_margin_required": "0.121"
    }
  }
}
```
