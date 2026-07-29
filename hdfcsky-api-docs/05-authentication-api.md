# Fetch Access Token via API

The full non-interactive login flow: obtain a token ID, log in, validate the 2FA code and PIN, authorise the application, and exchange the request token for an access token.

## Contents

- [Token ID](#token-id)
- [Login](#login)
- [Validate 2FA Code](#validate-2fa-code)
- [Resend 2FA Code](#resend-2fa-code)
- [Validate 2FA Code](#validate-2fa-code)
- [Authorize](#authorize)
- [Access Token](#access-token)

---

## Token ID

> Source: https://developer.hdfcsky.com/sky-docs/docs/fetch_access_token_via_api/token_id

### Description

This endpoint is used to fetch Token ID for authentication with the HDFC Sky Open API.

### API Endpoint:

```js
Method: GET
`https://developer.hdfcsky.com/oapi/v1/login?api_key=api_key`
```

### Request Configuration:

- **Method:** GET
- **Headers:**
  - `User-Agent`: User-Agent header is required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for authentication.

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/login?api_key=api_key' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

### Response:

```js
{
 "tokenId":"71de27013f81441a9cc3f311ad8720a9"
}
```

---

## Login

> Source: https://developer.hdfcsky.com/sky-docs/docs/fetch_access_token_via_api/validate

### Description

This endpoint is used to validate username and password for authentication with the HDFC Sky Open API.

### Login Flow using OpenAPI

This document outlines the login flow for your application using OpenAPI.

![Example banner](https://developer.hdfcsky.com/sky-docs/assets/images/login_flow-e32996588d20f4cc0ea7480cc2dfa5a5.png)

### API Endpoint:

```js
Method: POST
`https://developer.hdfcsky.com/oapi/v1/login-channel/validate?api_key=api_key&token_id=token_id`
```

### Request Configuration:

- **Method:** POST
- **Headers:**
  - `User-Agent`: User-Agent header is required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for authentication.
  - `token_id`: The Token ID used for authentication.
- **Data:**
  - `username`: Username

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/login-channel/validate?api_key=api_key&token_id=token_id' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"<username>"
}'
```

### Response:

```js
{
  "name": "USER",
  "recaptcha": false,
  "loginId": "TESTUSER123",
  "twofa": {},
  "message": "Please enter otp sent on mobile ******1234 and email ID TEST******@GMAIL.COM.",
  "twoFAEnabled": true
}
```

---

## Validate 2FA Code

> Source: https://developer.hdfcsky.com/sky-docs/docs/fetch_access_token_via_api/OTP

### Description

This endpoint is used to validate 2FA Code for authentication with the HDFC Sky Open API.

### API Endpoint:

```js
Method: PUT
`https://uat-developer.hdfcsky.com/oapi/v1/otp/validate?api_key=api_key&token_id=token_id`
```

### Request Configuration:

- **Method:** PUT
- **Headers:**
  - `User-Agent`: User-Agent header is required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for authentication.
  - `token_id`: The Token ID used for authentication.
- **Data:**
  - `otp`: OTP Entered by user

### Request Curl:

```js
curl --location --request PUT 'https://uat-developer.hdfcsky.com/oapi/v1/otp/validate?api_key=api_key&token_id=token_id' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json' \
--data-raw '{"otp":"1134"}'
```

### Response:

```js
{
  "name": "USER",
  "recaptcha": false,
  "loginId": "TESTUSER123",
  "twofa": {
    "questions": [
      {
        "question": "Please enter your pin"
      }
    ]
  },
  "message": "",
  "twoFAEnabled": true
}
```

---

## Resend 2FA Code

> Source: https://developer.hdfcsky.com/sky-docs/docs/fetch_access_token_via_api/resend2fa

### Description

This endpoint is used to resend the OTP for authentication with the HDFC Sky Open API.

### API Endpoint:

```js
Method: POST
`https://developer.hdfcsky.com/oapi/v1/twofa/resend?api_key=api_key&token_id=token_id`
```

### Request Configuration:

- **Method:** POST
- **Headers:**
  - `User-Agent`: User-Agent header is required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for authentication.
  - `token_id`: The Token ID used for authentication. This endpoint is used to validate username and password for authentication with the HDFC Sky API.

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/twofa/resend?api_key=api_key&token_id=token_id' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

---

## Validate 2FA Code

> Source: https://developer.hdfcsky.com/sky-docs/docs/fetch_access_token_via_api/2FA

### Description

This endpoint is used to validate Pin for authentication with the HDFC Sky Open API.

### API Endpoint:

```js
Method: POST
`https://developer.hdfcsky.com/oapi/v1/twofa/validate?api_key=api_key&token_id=token_id`
```

### Request Configuration:

- **Method:** POST
- **Headers:**
  - `User-Agent`: User-Agent header is required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for authentication.
  - `token_id`: The Token ID used for authentication.
- **Data:**
  - `answer`: Security Pin Entered by user

### Request Curl:

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/twofa/validate?api_key=api_key&token_id=token_id' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json' \
--data-raw '{"answer":"1134"}'
```

### Response:

```js
{
  "requestToken": "2fde50dba25c46f581b9ea83041123b9473394134",
  "termsAndConditions": {
    "version": 1,
    "content": [
      {
        "header": "P&L1",
        "body": "Terms and conditions agreed"
      }
    ]
  },
  "callbackUrl": "https://test123.com",
  "authorised": true
}
```

---

## Authorize

> Source: https://developer.hdfcsky.com/sky-docs/docs/fetch_access_token_via_api/authorize

### Description

This endpoint is used to Authorize user choice to accept terms and condition and provide the user with Request Token with the HDFC Sky Open API.

### API Endpoint:

```js
Method: GET
`https://developer.hdfcsky.com/oapi/v1/authorise?api_key=api_key&token_id=token_id&consent=consent&request_token=request_token`
```

### Request Configuration:

- **Method:** GET
- **Headers:**
  - `User-Agent`: User-Agent header is required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for authentication.
  - `token_id`: The Token ID used for authentication.
  - `consent`: It can be either be True or False
  - `request_token`: We will get this after we have validated the Two FA Code.

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/authorise?api_key=api_key&token_id=token_id&consent=consent&request_token=request_token' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json'
```

### Response

```js
{
  "callbackUrl": "https://google.com",
  "requestToken": "a1561247f2184c119a24e1daee0d495c"
}
```

---

## Access Token

> Source: https://developer.hdfcsky.com/sky-docs/docs/fetch_access_token_via_api/access_token

### Description

This endpoint is used get the access token after the user sends the request token with the HDFC Sky Open API.

### API Endpoint:

```js
Method: POST
`https://developer.hdfcsky.com/oapi/v1/access-token?api_key=api_key&request_token=request_token`
```

### Request Configuration:

- **Method:** POST
- **Headers:**
  - `User-Agent`: User-Agent header is set required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for fetching.
  - `request_token`: We will get this after we have Authorized the application.
- **Data:**
  - `api_secret`: The API Secret used for authentication.

### Request Curl

```js
curl --location 'https://developer.hdfcsky.com/oapi/v1/access-token?api_key=api_key&request_token=request_token' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '{
    "apiSecret": "<api_secret>",
}'
```

### Response:

```js
{
    accessToken: "eyJhasdGciasdaiJsdM4NCJ9.eyJzdWIiOiJTMDE5MDAwNyIsImV4cCI6MTcyMjk1ODk5NywibWVyY2hhbasdasdQiOiJTa3kgSW5zdasdFPcHRpb25zIiwibWVyY2hhbnRfYXBpX2tleSI6ImY3MDBlZDkzNWMwNzRlYWI4M2YxNzdkODIzODlasdasAIiwiaWF0IjoxNzIyOTMwMTk3fQ.bRuORQ9VXczQJWiOBXtTF2TK5aTkfnlod17pFadyorb8BQWXRiRMhVuezZ7w-Zn7123"
}

```
