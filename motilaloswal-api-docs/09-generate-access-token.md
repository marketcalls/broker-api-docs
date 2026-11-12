# Generate Access Token

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Authentication/Profile

This API generates an access token for client after validating the provided API key, authorization token & API secret key. This access token will be used for all API calls.

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/login/v1/getaccesstoken |
| Test URL | https://openapi.motilaloswaluat.com/rest/login/v1/getaccesstoken |
| Response | JSON |

## Sample Response

```json
{
"status": "SUCCESS",
"message": "",
"errorcode": "",
"accesstoken": "774aac4a0a8846cc865d7df05c095b13_M"
}
```

**Note: The Access Token API does not require a request body, only common headers are used.** The access token returned in response is Access Token used in header of each API.
