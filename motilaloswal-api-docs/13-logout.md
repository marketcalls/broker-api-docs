# Logout

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Authentication/Profile

This API closes the current session in the HOST system.

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/login/v5/logout |
| Test URL | https://openapi.motilaloswaluat.com/rest/login/v5/logout |
| Request | None |
| Response | JSON |

## Sample Request (Body)

```json
{
“userid":"AA017” //in case of dealer else not required
}
```

## Sample Response

```json
{
"status": "SUCCESS",
"message": "LOGOUT SUCCESSFULL",
"errorcode": ""
}
```
