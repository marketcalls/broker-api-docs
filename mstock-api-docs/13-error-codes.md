# Errors

> Source: https://tradingapi.mstock.com/docs/v1/typeB/error-codes/
>
> Section: Type B

### Common Error Codes

| Error Code | Status Code | Description |
| --- | --- | --- |
| `IA403` | 403 | Preceded by a 403 status code, this indicates the expiry or invalidation of an API Key. |
| `IA401` | 401 | Preceded by a 401 status code, this indicated the missing, expiry or invalidation of JWT token. |
| `IA400` | 400 | Preceded by a 400 status code, Represents missing required fields, bad values for parameters etc. |
| `IA404` | 404 | Preceded by a 404 status code, Requested resource could not be found. |
| `MA{XXX}` | --- | Represent the error status code received from mStock's API. |
| `IA500` | 500 | Represents an Internal server error occured while processing the API request. This should only happen rarely. |
