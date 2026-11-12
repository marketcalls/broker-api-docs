# Login through API

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction
>
> Section: Authentication/Profile

Authentication token will be expired at every day morning 6 a.m. due to exchange compliance.

This API authenticates the user and creates a session for the user in the Host System. The session is identified by an alphanumeric login key in the response.

| Method | POST |
| --- | --- |
| Production URL | https://openapi.motilaloswal.com/rest/login/v7/authdirectapi |
| Test URL | https://openapi.motilaloswaluat.com/rest/login/v7/authdirectapi |
| Request | JSON |
| Response | JSON |

Ex . Password = abc and APIKey = 123

SHA-256(Password + APIKey) = SHA-256(abc123)

## Sample Request (Body)

TOTP

```json
{
"userid":"AA017",
"password" :"23812bd4c1f3e980d86a16260b307d4a38dd6079577c9e9a22e9ccb75fcd59eb",
"2FA":"18/10/1988",
"totp": "Authenticator 6 digit Code"
}
```

OTP

```json
{
"userid":"AA017",
"password" :"23812bd4c1f3e980d86a16260b307d4a38dd6079577c9e9a22e9ccb75fcd59eb",
"2FA":"18/10/1988"
}
```

Note -

TOTP – Send the 6 digit OTP on login using any Authenticator App.

OR

OTP – do not pass the otp parameter or pass it as blank..

## Sample Response

```json
{
"status": "SUCCESS",
"message": "Return Auth Token SUCCESS",
"errorcode": "",
"AuthToken": "774aac4a0a8846cc865d7df05c095b13_M",
"isAuthTokenVerified": "TRUE"
}
```

The AuthToken returned in response is Authorization Token used in header of each API.
