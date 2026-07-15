# Authentication

Login uses 2 Factor Authentication (2FA) and is performed in two steps. After successful login you receive an `api_session_key` that must be passed in the `Authorization` header of every subsequent API call, and a `susertoken` used for the WebSocket connection.

To get values for `api_token` and `api_secret`, go to the **Account** section of MyAccount (<https://myaccount.definedgesecurities.com>) and click on the **"API Config"** button at the top.

> Your API credentials get reset when you change/reset your login password.

---

## User Login — Step 1

| Particular | Details |
| --- | --- |
| API Name | User login - Step one |
| URL | `https://signin.definedgesecurities.com/auth/realms/debroking/dsbpkc/login/{{api_token}}` |
| Method | GET |
| Produces | application/json |

### Description

This step triggers an OTP that is sent to your registered mobile number and email id.

### Request Header

| Header | Value |
| --- | --- |
| api_secret | Actual value of `api_secret` key |

### GET Request

```
GET https://signin.definedgesecurities.com/auth/realms/debroking/dsbpkc/login/{{api_token}}
-H "api_secret: Actual value of api_secret key"
```

### Response Message Format

```json
{
  "otp_token": "...",
  "message": "OTP is sent to mobile XXXX and registered email id."
}
```

---

## User Login — Step 2

| Particular | Details |
| --- | --- |
| API Name | User login - Step two |
| URL | `https://signin.definedgesecurities.com/auth/realms/debroking/dsbpkc/token` |
| Method | POST |
| Produces | application/json |

### Description

This API performs the second step of login for 2 Factor Authentication and returns the API key.

- You need to retain the **API key** received in the response to use it for all API calls.
- Also retain **susertoken** for the WebSocket connection.

### Request Header

NA

### API Key

Extract `api_session_key` and use it in all subsequent API calls by passing it in the request header:

```
Authorization: <api_session_key>
```

### WebSocket Key

Extract `susertoken` from the response and use it while making the WebSocket connection.

### Request Message Format

```json
{
  "otp_token": "{{otp_token}}",
  "otp": "{{otp_code}}"
}
```

### Response Message Format

```json
{
  "request_time": "13:26:42 03-02-2023",
  "actid": "YOUR UCC",
  "uname": "test user10",
  "prarr": [ ... ],
  "stat": "Ok",
  "susertoken": "YOUR WEBSOCKET KEY",
  "email": "YOUR EMAIL",
  "uid": "YOUR UCC",
  "brnchid": "HO",
  "orarr": [ ... ],
  "exarr": [],
  "brkname": "DEFINEDGE",
  "lastaccesstime": "1675411002",
  "api_session_key": "YOUR API KEY"
}
```

### Response Fields (key items)

| Field | Description |
| --- | --- |
| `api_session_key` | API key to pass in the `Authorization` header for all trading API calls |
| `susertoken` | User session token used for the WebSocket connection |
| `actid` / `uid` | Your Unique Client Code (UCC) / Account ID |
| `uname` | User name |
| `email` | Registered email |
| `stat` | `Ok` on success |
