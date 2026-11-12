# Verify OTP

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Authentication/Profile

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/login/v5/verifyotp |
| Test URL | https://openapi.motilaloswaluat.com/rest/login/v5/verifyotp |
| Request | JSON |
| Response | JSON |

## Request JSON

| Field | Type | Mandatory | Description |
| --- | --- | --- | --- |
| otp | Number(6) | Y | 6 digit Code sent to your mobile/mail |

## Sample Request (Body)

```json
{
“otp”: 6 digit Code sent to your mobile/ mail
}
```

## Sample Response

```json
{
“status": "SUCCESS",
"message": "OTP VERFIED SUCCESSFULLY",
"errorcode": ""
}
```
