<!-- Source: https://vortex.rupeezy.in/docs/2.2/usage/ -->

# Api Usage

### Root Endpoint

```
https://vortex-api.rupeezy.in/v2
```

### Required Headers

| Header Name | Value |
| --- | --- |
| `x-api-key` | Api key received after registration. Required for all apis. |
| `Authorization` | Bearer Access token received after exchanging auth token. e.g.: "Bearer exjy........". Required for all apis except login apis. |

### Rate Limits

Rate limits for individual endpoints are mentioned along with the endpoint. On top of that, there is a hard limit of 50,000 API requests per day.

### Common Error Codes

| HTTP Status | Meaning |
| --- | --- |
| `401` | Either x-api-key or Authorization header have incorrect values, or you are not allowed to access the particular endpoint |
| `404` | Invalid endpoint |
| `429` | Rate limit has been crossed for that particular endpoint |
| `5xx` | Internal server error |
