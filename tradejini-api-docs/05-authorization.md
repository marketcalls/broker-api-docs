# Authorization APIs

Endpoint reference for the authentication APIs. Access tokens are valid for **24 hours**.

## Individual Token service

`POST /api-gw/oauth/individual-token-v2`

Authentication endpoint for **individual app** registrations. Use this flow when your app authenticates only your own Tradejini account — no browser redirect required.

Submit your account password and a 2FA value to receive an access token valid for **24 hours**.

**Prerequisite:** [Create an app](https://developer.tradejini.com/developer-portal) in the Apps Section to obtain your alphanumeric API key. Pass it as `Bearer <api_key>` in the `Authorization` header of this request.

**2FA types:**
- `otp` — One-time password sent via SMS/email. Generate it from the [CubePlus web app](https://cubeplus.tradejini.com/) under the 2FA page.
- `totp` — Time-based OTP from an authenticator app (e.g. Google Authenticator, Authy). Set up via Settings → Security → scan the QR code in the [CubePlus web app](https://cubeplus.tradejini.com/).

**Token expiry:** Tokens expire after 24 hours. An expired token returns `401 Unauthorized` — re-call this endpoint with fresh credentials.

**Rate limit:** 3 requests/second per IP.

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Your app API key in the following format: Bearer `<api_key>` The `api_key` is the alphanumeric key from your app registration in the Apps Section. This endpoint exchanges it for an `access_token`. Example: `Bearer <api Key>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `password` | `string` | Yes | Enter your login password here. Example: `6789` |
| `twoFa` | `string` | Yes | To get the OTP for your client code, login into the web app [here](https://cubeplus.tradejini.com/) and in the 2FA page, click 'Having trouble with AppCode/TOTP' to see 'Send SMS / Email OTP' option to generate OTP. For Time based OTP, login [here](https://cubeplus.tradejini.com/) and set up the Authenticator app to generate time based OTP by scanning the QR code provided under the Settings section. Example: `123456` |
| `twoFaTyp` | `string` | Yes | Enter the type of TwoFactorAuthorization based on your twoFa field input. Values: `otp`, `totp`; Example: `totp` |

### Example Request

```bash
curl -X POST "https://example.com/api-gw/oauth/individual-token-v2" \
  -H "Authorization: Bearer <api Key>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'password=yourpassword&twoFa=123456&twoFaTyp=totp'
```

### Responses

#### 200 OK

Success response with access token

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `access_token` | `string` | The access token to include in the `Authorization` header of all subsequent API requests. Format: `Bearer <api_key>:<access_token>`. Example: `eyJhbGciOiJSUzI1NiJ9...` |
| `token_type` | `string` | Token type. Always `"bearer"`. Example: `bearer` |
| `expires_in` | `integer (int32)` | Token lifetime in seconds. Typically `86400` (24 hours). After expiry the API returns `401 Unauthorized` — re-authenticate to get a new token. Example: `86400` |
| `scope` | `string` | OAuth scope granted to the token. Example: `general` |

**Example**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 86400,
  "scope": "general"
}
```

#### 400 Bad Request

Bad Request — missing `password`, `twoFa`, or `twoFaTyp`

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message describing which field failed validation or why the request was rejected. Values: `Internal Error occurred. Kindly try again.`, `Input validation failed. Kindly check your input contains required fields for the request` |

**Example**

```json
{
  "s": "error",
  "msg": "Input validation failed. Kindly check your input contains required fields for the request"
}
```

#### 401 Unauthorized

Unauthorized — wrong `client_id`, password, or 2FA value. Ensure `twoFaTyp` matches the value type passed in `twoFa` (`otp` or `totp`).

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. Values: `Unauthorized` |

**Example**

```json
{
  "s": "error",
  "msg": "Unauthorized"
}
```

#### 429 Too Many Requests

Too Many Requests — OTP rate limit exceeded (3 req/sec per IP)

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message indicating the rate limit was exceeded. |

**Example**

```json
{
  "s": "error",
  "msg": "Too many requests"
}
```

#### 500 Internal Server Error

Internal Server Error — retry with backoff

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. |

**Example**

```json
{
  "s": "error",
  "msg": "Internal server error"
}
```

---

## Authorize

`GET /api-gw/oauth/authorize`

First step of the OAuth 2.0 authorization flow for **third-party app** registrations. Redirects the user's browser to the Tradejini login page. After the user logs in, their browser is redirected to your `redirect_uri` with an authorization `code` in the query string. Pass that code to `POST /api-gw/oauth/token` to obtain an access token.

**Use this flow when:** your app authenticates on behalf of multiple Tradejini user accounts.

**Prerequisite:** [Create an app](https://developer.tradejini.com/developer-portal) in the Apps Section to obtain your `client_id` (API key) and `client_secret`.

**Note:** This endpoint performs a browser redirect and cannot be tested directly in this playground. See the authentication curl examples in the API overview.

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `client_id` | `string` | Yes | Your app's alphanumeric API key from the [Apps Section](https://developer.tradejini.com/developer-portal) app registration page. If the value does not match the registered app, authorization will be denied. |
| `redirect_uri` | `string` | Yes | The callback URL registered in your app on the [Apps Section](https://developer.tradejini.com/developer-portal). Must match exactly — if it does not, authorization will be denied. |
| `response_type` | `string` | Yes | As per oAuth specification this value should be __"code"__. Values: `code` |
| `scope` | `string` | Yes | This field value should be __"general"__. Values: `general` |
| `state` | `string` | Yes | A literal string that will be return in the final redirection callback. |

### Example Request

```bash
curl -X GET "https://example.com/api-gw/oauth/authorize?client_id=string&redirect_uri=string&response_type=code&scope=general&state=string"
```

### Responses

#### 302

Redirect to login page or redirect url with code.

#### 400 Bad Request

Bad inputs

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. Values: `Unauthorized` |

**Example**

```json
{
  "s": "error",
  "msg": "Unauthorized"
}
```

#### 401 Unauthorized

Unauthorized — wrong `client_id`, password, or 2FA value. Verify credentials and ensure `twoFaTyp` matches the 2FA value type.

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. Values: `Unauthorized` |

**Example**

```json
{
  "s": "error",
  "msg": "Unauthorized"
}
```

---

## Access token

`POST /api-gw/oauth/token`

Exchange the authorization code received from the OAuth redirect callback for an access token.

**Token lifetime:** The returned access token is valid for **24 hours**. After expiry, the token is silently rejected with a `401 Unauthorized`. Re-authenticate by repeating the full authorization flow.

**Re-authentication flow:** `GET /api-gw/oauth/authorize` → user login → redirect with code → `POST /api-gw/oauth/token`.

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | This field value will be same as code received in the final redirection callback. |
| `client_id` | `string` | Yes | Your app's alphanumeric API key from the [Apps Section](https://developer.tradejini.com/developer-portal) app registration page. Must match the key used in Step 1 (`/authorize`). If it does not match, access token generation will fail. |
| `redirect_uri` | `string` | Yes | This field value should be the redirect url mentioned in the registered app. If the value is improper access token will not be generated. |
| `client_secret` | `string` | Yes | Your app's API secret, obtained from the [Apps Section](https://developer.tradejini.com/developer-portal) app registration page. If the value does not match, access token generation will fail. |
| `grant_type` | `string` | Yes | As per oAuth specification this value should be __"authorization_code"__. Values: `authorization_code` |

### Example Request

```bash
curl -X POST "https://example.com/api-gw/oauth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'code=abc123def456&client_id=xK9mP2qRtZ&client_secret=sG7nL4wVyQ&redirect_uri=https%3A%2F%2Fyourapp.com%2Fcallback&grant_type=authorization_code'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `access_token` | `string` | The access token to include in the `Authorization` header of all subsequent API requests. Format: `Bearer <api_key>:<access_token>`. Example: `eyJhbGciOiJSUzI1NiJ9...` |
| `token_type` | `string` | Token type. Always `"bearer"`. Example: `bearer` |
| `expires_in` | `integer (int32)` | Token lifetime in seconds. Typically `86400` (24 hours). After expiry the API returns `401 Unauthorized` — re-authenticate to get a new token. Example: `86400` |
| `scope` | `string` | OAuth scope granted to the token. Example: `general` |

**Example**

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 86400,
  "scope": "general"
}
```

#### 400 Bad Request

Bad Request — missing or invalid `code` or `redirect_uri`

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message describing which field failed validation or why the request was rejected. Values: `Internal Error occurred. Kindly try again.`, `Input validation failed. Kindly check your input contains required fields for the request` |

**Example**

```json
{
  "s": "error",
  "msg": "Input validation failed. Kindly check your input contains required fields for the request"
}
```

#### 401 Unauthorized

Unauthorized — invalid or expired authorization code

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. Values: `Unauthorized` |

**Example**

```json
{
  "s": "error",
  "msg": "Unauthorized"
}
```

#### 429 Too Many Requests

Too Many Requests — rate limit exceeded (100 req/sec per API key)

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message indicating the rate limit was exceeded. |

**Example**

```json
{
  "s": "error",
  "msg": "Too many requests"
}
```

#### 500 Internal Server Error

Internal Server Error — retry with backoff

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. |

**Example**

```json
{
  "s": "error",
  "msg": "Internal server error"
}
```

---

## Order Connect [Offsite Orders]

`GET /api-gw/oauth/order-connect`

Authorize to place orders and get oAuth Code to the redirect url at once.

**Note:** This API cannot be tested from this API document since it gets redirected.

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `client_id` | `string` | Yes | Your app's alphanumeric API key from the [Apps Section](https://developer.tradejini.com/developer-portal) app registration page. If the value does not match the registered app, authorization will be denied. Example: `<api key>` |
| `redirect_uri` | `string` | Yes | The callback URL registered in your app on the [Apps Section](https://developer.tradejini.com/developer-portal). Must match exactly — if it does not, authorization will be denied. Example: `http:/myapp.in/` |
| `response_type` | `string` | Yes | As per oAuth specification this value should be __"code"__. Values: `code` |
| `scope` | `string` | Yes | This field value should be __"general"__. Values: `general` |
| `state` | `string` | Yes | A literal string that will be return in the final redirection callback. Example: `` |
| `params` | `string` | Yes | This field value should be the params required to place orders in json array format and get oAuth Code. **Note:** Each array value should match any of examples provided. Else your authorization will fail. Example: ```json [{"exch":"NSE","symbol":"ACC","series":"EQ","inst":"EQT","qty":10,"side":"buy","type":"limit","product":"intraday","limitPrice":2700.55,"validity":"day"},{"exch":"NFO","symbol":"NIFTY","expiry":"2022-11-24","inst":"FUTIDX","qty":2000,"side":"sell","type":"market","product":"intraday","limitPrice":0,"validity":"ioc","discQty":500},{"exch":"NFO","symbol":"BANKNIFTY","expiry":"2022-11-24","optType":"PE","inst":"OPTIDX","strike":"34000","qty":1500,"side":"buy","type":"market","product":"delivery","limitPrice":0,"validity":"day","mktProt":5}] ``` For equity symbol instrument must be `EQT`. Example: `` |

### Example Request

```bash
curl -X GET "https://example.com/api-gw/oauth/order-connect?client_id=%3Capi+key%3E&redirect_uri=http%3A%2Fmyapp.in%2F&response_type=code&scope=general&state=&params="
```

### Responses

#### 302

Redirect to login page or redirect url with code.

#### 400 Bad Request

Bad order params

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message describing which field failed validation or why the request was rejected. Values: `Internal Error occurred. Kindly try again.`, `Input validation failed. Kindly check your input contains required fields for the request` |

**Example**

```json
{
  "s": "error",
  "msg": "Input validation failed. Kindly check your input contains required fields for the request"
}
```

#### 401 Unauthorized

Unauthorized — wrong `client_id`, password, or 2FA value. Verify credentials and ensure `twoFaTyp` matches the 2FA value type.

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. Values: `Unauthorized` |

**Example**

```json
{
  "s": "error",
  "msg": "Unauthorized"
}
```
