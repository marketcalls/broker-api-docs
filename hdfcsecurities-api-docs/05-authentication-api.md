# Fetch Access Token via API

> Source: https://developer.hdfcsec.com/ir-docs/docs/category/fetch-access-token-via-api

The fully programmatic login flow: obtain a token ID, log in with username/password, validate the
2FA code, authorise the application, and exchange the request token for an access token.

## Contents

- [Token ID](#token-id)
- [Login](#login)
- [Validate 2FA Code](#validate-2fa-code)
- [Resend 2FA Code](#resend-2fa-code)
- [Authorize](#authorize)
- [Access Token](#access-token)

## Flow Summary

| Step | Method | Endpoint | Produces |
| --- | --- | --- | --- |
| 1 | GET | `/oapi/v1/login?api_key=` | `tokenId` |
| 2 | POST | `/oapi/v1/login/validate?api_key=&token_id=` | `loginId`, 2FA question list |
| 3 | POST | `/oapi/v1/twofa/validate?api_key=&token_id=` | `requestToken`, T&C, `authorised` flag |
| 3a | GET | `/oapi/v1/twofa/resend?api_key=&token_id=` | resends the OTP |
| 4 | GET | `/oapi/v1/authorise?api_key=&token_id=&consent=&request_token=` | `callbackUrl`, `requestToken` |
| 5 | POST | `/oapi/v1/access-token?api_key=&request_token=` | `accessToken` |

---

## Token ID

> Source: https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/token_id

### Description

This endpoint is used to fetch Token ID for authentication with the InvestRight Open API.

### API Endpoint:

```js
Method: GET
`https://developer.hdfcsec.com/oapi/v1/login?api_key=<api_key>`
```

### Request Configuration:

- **Method:** GET
- **Headers:**
  - `User-Agent`: User-Agent header is required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for authentication.

### Request Curl

```js
curl --location 'https://developer.hdfcsec.com/oapi/v1/login?api_key=api_key' \
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

> Source: https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/validate

### Description

This endpoint is used to validate username and password for authentication with the InvestRight Open API.

### Login Flow using OpenAPI

This document outlines the login flow for your application using OpenAPI.

![Login flow](https://developer.hdfcsec.com/ir-docs/assets/images/login_flow-abd57a6b49c6b767bc84040ae554b13f.png)

### API Endpoint:

```js
Method: POST
`https://developer.hdfcsec.com/oapi/v1/login/validate?api_key=<api_key>&token_id=<token_id>`
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
  - `password`: Password

### Request Curl

```js
curl --location 'https://developer.hdfcsec.com/oapi/v1/login/validate?api_key=api_key&token_id=token_id' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json' \
--data-raw '{"username":"<username>","password":"<password>"}'
```

### Response:

```js
{
    "recaptcha": false,
    "loginId": "3170270",
    "twofa": {
        "questions": [
            {
                "question": "Please enter OTP received on registered Email/Mobile"
            }
        ]
    },
    "twoFAEnabled": true
}
```

---

## Validate 2FA Code

> Source: https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/2FA

### Description

This endpoint is used to validate 2FA Code for authentication with the InvestRight Open API.

### API Endpoint:

```js
Method: POST
`https://developer.hdfcsec.com/oapi/v1/twofa/validate?api_key=<api_key>&token_id=<token_id>`
```

### Request Configuration:

- **Method:** POST
- **Headers:**
  - `User-Agent`: User-Agent header is required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for authentication.
  - `token_id`: The Token ID used for authentication.
- **Data:**
  - `answer`: OTP Code or answer

### Request Curl:

```js
curl --location 'https://developer.hdfcsec.com/oapi/v1/twofa/validate?api_key=api_key&token_id=token_id' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json' \
--data-raw '{"answer":"113402"}'
```

### Response:

```js
{
  "requestToken": "a1561247f2184c123a24e1daee0d495c",
  "termsAndConditions": {
    "version": 1,
    "content": [
        {
            "header": "P&L1",
            "body": "Terms and Conditions Agreed"
        }
    ]
},
  "authorised": false
}
```

---

## Resend 2FA Code

> Source: https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/resend2fa

### Description

This endpoint is used to resend the OTP for authentication with the InvestRight Open API.

### API Endpoint:

```js
Method: GET
`https://developer.hdfcsec.com/oapi/v1/twofa/resend?api_key=<api_key>&token_id=<token_id>`
```

### Request Configuration:

- **Method:** GET
- **Headers:**
  - `User-Agent`: User-Agent header is required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for authentication.
  - `token_id`: The Token ID used for authentication.

### Request Curl

```js
curl --location 'https://developer.hdfcsec.com/oapi/v1/twofa/resend?api_key=api_key&token_id=token_id' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
```

---

## Authorize

> Source: https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/authorize

### Description

This endpoint is used to Authorize user choice to accept terms and condition and provide the user with Request Token with the InvestRight Open API.

### API Endpoint:

```js
Method: GET
`https://developer.hdfcsec.com/oapi/v1/authorise?api_key=<api_key>&token_id=<token_id>&consent=<consent>&request_token=<request_token>`
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
curl --location 'https://developer.hdfcsec.com/oapi/v1/authorise?api_key=api_key&token_id=token_id&consent=consent&request_token=request_token' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--header 'Content-Type: application/json'
```

### Response

```js
{
  "callbackUrl": "https://xyzmerchant.com",
  "requestToken": "a1561247f2184c119a24e1daee0d495c"
}
```

---

## Access Token

> Source: https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/access_token

### Description

This endpoint is used get the access token after the user sends the request token with the InvestRight Open API.

### API Endpoint:

```js
Method: POST
`https://developer.hdfcsec.com/oapi/v1/access-token?api_key=<api_key>&request_token=<request_token>`
```

### Request Configuration:

- **Method:** POST
- **Headers:**
  - `User-Agent`: User-Agent header is set required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for fetching.
  - `request_token`: We will get this after we have Authorized the application.
- **Data:**
  - `api_secret`: The API Secret used for authentication

### Request Curl

```js
curl --location 'https://developer.hdfcsec.com/oapi/v1/access-token?api_key=api_key&request_token=request_token' \
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

The `accessToken` is a JWT. Its payload carries `sub` (the trading account / client code), `exp`,
`iat`, `merchant`, and `merchant_api_key`. Pass it on every subsequent call as the bare
`Authorization` header value — there is no `Bearer ` prefix.
