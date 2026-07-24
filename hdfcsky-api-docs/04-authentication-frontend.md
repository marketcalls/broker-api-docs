# Fetch Access Token via Frontend

> Source: https://developer.hdfcsky.com/sky-docs/docs/token_id_fe

## Description

```js
Login using below URL:
`https://uat-developer.hdfcsky.com/oapi/v1/login?api_key=api_key`
```

- User enters the URL mentioned above with API Key which redirects to the login page of HDFC Securities.
- Authenticate with user login credentials to generate request token followed by 2FA and accepting the terms and condition.
- After authorization the user is redirected back to the merchant's portal with a Request Token.
- The Merchant then passes the Request Token, API Key and API Secret to fetch the Access Token.

## Request Configuration:

- **Method:** POST
- **Headers:**
  - `User-Agent`: User-Agent header is set required indicating the client application making the request.
- **Params:**
  - `api_key`: The API key used for fetching.
  - `request_token`: We will get this after we have Authorized the application.
- **Data:**
  - `api_secret`: The API Secret used for authentication.

## Request Curl

```js
curl --location 'https://uat-developer.hdfcsky.com/oapi/v1/access-token?api_key=api_key&request_token=request_token' \
--header 'Content-Type: application/json' \
--header 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
--data '{
    "apiSecret": "<api_secret>",
}'
```
