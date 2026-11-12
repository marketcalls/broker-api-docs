<!-- Source: https://vortex.rupeezy.in/docs/2.2/authentication/ -->

# Authentication

## SSO Authentication

```mermaid
sequenceDiagram
    participant Developer App
    participant User
    participant Flow Web
    participant Api Server
    Note over Developer App : login Url is https://flow.rupeezy.in?applicationId=<application_id>
    Developer App->>+User: Generate login URL and give to user.

    User->>+Flow Web: Browse to the login url created by the developer app
    Note over Flow Web: User authentication process
    Flow Web->>+Developer App: Redirect to callback URL with 'auth' parameter
    Developer App->>+Api Server: Call Create session api with auth parameter and x-api-key
    Api Server->>+Developer App: Server returns with Access Tokens
```

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `BROWSER URL` | https://flow.rupeezy.in?applicationId=<`YOUR application_id`> | Begin authentication flow | NA |
| `POST` | [/user/session](#create-session-object) | Create session | 1/sec |

**STEP 1:**  Navigate to https://flow.rupeezy.in?applicationId=<`YOUR application_id`>

This step should open a login screen for your user. Only the user whitelisted while creating the application will be able to login. All others will be shown an error. Once the user verifies himself, he will be asked to give consent to the application. Upon receiving consent, the user will be redirected to the `Callback URL` registered with the application

**STEP 2:**  The callbak url will be appended with a `auth` query parameter. Grab the `auth` parameter for the next step.

**STEP 3:**  Call the create session API to get access token

### Create Session Object

```
{
    "checksum": <checksum>, 
    "applicationId": <YOUR application_id>, 
    "token": <auth token>
}
```

| key | description |
| --- | --- |
| `checksum` | SHA-256 hash of string "application_id"+"auth_token"+"x-api-key" |
| `applicationId` | Contains `application_id` |
| `token` | Contains `auth` param received in STEP 2 |

### Create Session Response

```
{
    "status": "success",
    "data": {
        "access_token": "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAi.......",
        "user_name": "JOHN DOE",
        "login_time": "2023-Mar-29 13:10:50",
        "email": "JOHN.DOE@GMAIL.COM",
        "mobile": "9999999999",
        "exchanges": [
            "NSE_EQ",
            "NSE_FO",
            "MCX_FO",
            "NSE_CUR"
        ],
        "product_types": [
            "INTRADAY",
            "DELIVERY",
            "MTF"
        ],
        "others": {
            "userCode": "NXAAE",
            "POA": 2
        },
        "user_id": "XX9999",
        "tradingActive": true
    }
}
```

The `access_token` received in the above response should be used in Authorization header for all the subsequent apis. The format is:

```
Authorization: Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAi.......
```

## Authentication with TOTP (Depricating Soon)

| method | endpoint | use case | Rate Limit |
| --- | --- | --- | --- |
| `POST` | [{{base_url}}/user/login](#login-object) | Create session | 1/sec |
| `DELETE` | [{{base_url}}/user/session](#logout) | Logout Session | 1/sec |

### Login Header

```
x-api-key: <Your x-api Key>
```

### Login Object

```
{
    "client_code": "DEMOUSER", 
    "password": "DEMOPASS",
    "totp": "412312",
    "application_id": "dev_1234"
}
```

### Login Response

[Click Here](#create-session-response)

### Logout

```
Endpoint: {{base_url}}/user/session
```
