# Error Codes

The API returns different errors depending on the nature of the data submitted and server processing. Some of the errors are technical while some are business validations.

## HTTP Status Codes

| Code | Meaning |
| --- | --- |
| **400** | Returned if some of the request parameters are incorrect or required headers are missing |
| **401** | Returned if your `api_session_key` is incorrect or the request is not from the registered IP |
| **404** | Returned when the requested URL is invalid |
| **500** | General error if there are any technical issues on the API server |

> The rest of the errors are returned in the API response with a JSON structure.
