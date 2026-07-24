# Authentication

`apiKey` and `apiSecret` are used to generate an access token (`jKey`) that is used in all API calls to perform trading.

The access token generation process starts with an authentication flow in a web browser. You authorize the program using your client ID (UCC), trading password, and PAN/year of birth.

Whether your program runs on a GUI or a console, you always have to use a web browser to create an access token, which then allows you to use the API.

> The access token is valid for 24 hours, so you only need to generate it once per day. Access tokens are cleared between 5 AM and 6 AM — regenerate your access token after 6 AM.

Once you generate your access token, you can store it and bypass authentication for subsequent connections.

## Token Generation Steps

| Step | Description |
| --- | --- |
| 1 | Open the authorization URL `https://auth.flattrade.in/?app_key=APIKEY` in a browser, replacing `APIKEY` with the API key allocated to you. |
| 2 | Enter your Client ID (UCC), password, and PAN/DOB, then submit. |
| 3 | After successful authorization, the portal redirects to your registered Redirect URL with a `request_code`: `https://yourRedirectURL.com/?request_code=requestCodeValue`. The `request_code` is a one-time code valid for only a few minutes and must be exchanged for a token immediately. |
| 4 | Call `https://authapi.flattrade.in/trade/apitoken` with `POST` to validate the `request_code` and obtain the token. |
| 5 | You get a response with the token, which can be used in the appropriate endpoints. |

> The Redirect URL is pre-registered against each API Key. If you use different Redirect URLs for PROD and TESTING, register a separate API Key for each environment.
>
> The token is returned only if the request originates from the registered static IP for the API key.

## Step 4 — Exchange request_code for a Token

### Request

```
POST https://authapi.flattrade.in/trade/apitoken
Content-Type: application/json

{
  "api_key": "xcvvwegfhgh4454646",
  "request_code": "xxdfddfdfdsfdsf84okkdlfelfdfdfd345fsf",
  "api_secret": "sdfdsfsdfdsfXXXXXXX"
}
```

| Field | Description |
| --- | --- |
| `api_key` | The public API key |
| `request_code` | The one-time code obtained during the login flow. Lifetime is a few minutes; exchange it for a token immediately after obtaining it. |
| `api_secret` | SHA-256 hash of `(api_key + request_code + api_secret)` |

### Response

```json
{
  "token": "dsfdsf84okkdlfelfdfdfd3454545454ssdfsf",
  "client": "CCODE123",
  "status": "Ok",
  "emsg": ""
}
```

## Using the Token

Extract `token` from the response and use it as `jKey` in all subsequent REST API calls (sent as a form field, e.g. `jKey=<token>`) and as `accesstoken` when connecting to the WebSocket API.
