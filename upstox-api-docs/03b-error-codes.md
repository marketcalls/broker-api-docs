# Error Codes

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 400 | Your request parameters are incorrect |
| 401 | Your API key is wrong or missing |
| 403 | The requested resource is hidden for administrators only |
| 404 | The specified resource could not be found |
| 405 | You tried to access a resource with an invalid method |
| 406 | You requested a format that isn't JSON |
| 410 | The resource requested has been removed from our servers |
| 429 | You're requesting too many resources! Slow down! |
| 500 | We had a problem with our server. Please try again later |
| 503 | We're temporarily offline for maintenance |

## Application-Level Error Codes

| Code | Description |
|------|-------------|
| UDAPI10000 | Request not recognized or URL malformed |
| UDAPI100016 | Invalid Credentials |
| UDAPI10005 | Rate limit threshold exceeded |
| UDAPI100015 | Missing API version in header |
| UDAPI100050 | Compromised or invalid token |
| UDAPI100067 | Extended token lacks permissions for endpoint |
| UDAPI100036 | Malformed input parameters |
| UDAPI100038 | Malformed input parameters |
| UDAPI100073 | client_id is inactive; contact support |
| UDAPI100500 | Unexpected system failure; contact support |

Error codes specific to each API are detailed in the 4XX response section within their respective documentation.
