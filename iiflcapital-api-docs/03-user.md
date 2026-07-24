# User

Four endpoints covering login, logout, account details, and trading margins/limits.

| Method | Endpoint | Processing Mode | Action |
| --- | --- | --- | --- |
| POST | `/getusersession` | Single | Generates the access token used to authenticate API calls |
| GET | `/profile` | Single | Retrieves the client's account details and personal information |
| GET | `/limits` | Single | Returns the user's available trading limits and margins |
| POST | `/profile/logout` | Single | Terminates the user's active session |

## Login Flow

To log in, a client needs:

- **Trading account credentials** — Email/Phone/ClientId/PAN and password (resettable on the web login page)
- **OTP or TOTP** — for two-factor authentication
- **App Key and App Secret** — specific to the application being used (obtained from your Relationship Manager / Point of Contact)

### Daily Login Steps

1. **Redirect to the login endpoint**:

   ```
   https://markets.iiflcapital.com/?v=1&appkey=xxx&redirecturl=abc
   ```

   Replace `xxx` with the application's `appKey`. An optional `redirecturl` parameter can be passed if you need to redirect users dynamically after login; otherwise they're redirected to the default URL registered with the application.

2. The client enters their trading account credentials (username, password, OTP/TOTP) on the login portal.
3. On success, the client is redirected to the app's registered redirect URL with `authCode` and `clientId` appended as query parameters. If no redirect URL was registered, an IIFL page displays the `authCode` instead.
4. **Generate the access token**: SHA-256-encrypt `clientId + authCode + appSecret` and pass it as `checkSum` to [Get User Session](#get-user-session) to obtain the access token.
5. Use the resulting `userSession` as a Bearer token in the `Authorization` header of every subsequent API request.

> A fresh login (and token) is required every trading day.

## Get User Session

`POST /getusersession`

### Request

```json
{ "checkSum": "bec46c08a04f7c8f1ea355b85d0f32e9250d83ffe42a147400fc4d0bdb9aee2b" }
```

| Field | Description |
| --- | --- |
| `checkSum`* | SHA-256 of `clientId + authCode + apiSecret` concatenated |

### Response

```json
{ "status": "Ok", "userSession": "eyJhbGciOi*******bx844uFwWA" }
```

| Field | Description |
| --- | --- |
| `status` | `Ok` or `Not_Ok` |
| `userSession` | JWT representing the authenticated session — use as the Bearer token for all subsequent calls |

---

## Profile

`GET /profile`

**Headers:** `Authorization: Bearer <userSession>`

### Response

```json
{
  "status": "Ok",
  "message": "Success",
  "result": {
    "clientId": "3******4",
    "clientName": "Ishan Arora",
    "isTotpEnabled": "Y",
    "isPoaProvided": "Y",
    "accountStatus": "Na",
    "exchanges": ["BSECURR", "BSEEQ", "BSEFO", "NSECURR", "NSEEQ", "NSEFO"],
    "products": ["NORMAL", "INTRADAY", "DELIVERY", "BNPL"],
    "orderComplexity": ["REGULAR", "AMO", "BO", "CO"],
    "email": "is**********@gmail.com",
    "phoneNumber": "8********4"
  }
}
```

| Field | Description |
| --- | --- |
| `clientId` | Unique client identifier |
| `clientName` | Client's registered name |
| `isTotpEnabled` | `Y`/`N` — whether TOTP-based 2FA is enabled |
| `isPoaProvided` | `Y`/`N` — whether Power of Attorney has been provided |
| `accountStatus` | Current account status |
| `exchanges` | Exchanges the client is authorized to trade on |
| `products` | Trading products enabled for the client |
| `orderComplexity` | Order complexities the client can use |

---

## Limits

> Trading limits are pooled across segments for Indian resident clients. For NRI clients, Equity and F&O limits are tracked separately, so `/limits`, `/limits/fno`, and `/limits/equity` return the same values for resident clients but differ for NRI clients.

| Method | Endpoint | Processing Mode | Action |
| --- | --- | --- | --- |
| GET | `/limits` | Single | Overall limits for residents; F&O segment limits for NRIs |
| GET | `/limits/fno` | Single | Overall limits for residents; F&O segment limits for NRIs |
| GET | `/limits/equity` | Single | Overall limits for residents; Equity segment limits for NRIs |

**Headers:** `Authorization: Bearer <userSession>`

### Response

```json
{
  "status": "Ok",
  "message": "Success",
  "result": {
    "tradingLimit": 19990000,
    "openingCashLimit": 0,
    "intradayPayin": 20000000,
    "collateralMargin": 0,
    "creditForSell": 0,
    "adhocMargin": 0,
    "utilizedMargin": 0,
    "blockedForPayout": 10000,
    "utilizedSpanMargin": 0,
    "utilizedExposureMargin": 0
  }
}
```

| Field | Description |
| --- | --- |
| `tradingLimit` | Maximum funds available for trading |
| `openingCashLimit` | Cash balance at the start of the trading day |
| `intradayPayin` | Funds added during the day for intraday trades |
| `collateralMargin` | Margin available from pledged securities |
| `creditForSell` | Credit for securities sold but not yet settled |
| `adhocMargin` | Additional margin provided by the broker |
| `utilizedMargin` | Total margin used for open positions and orders |
| `blockedForPayout` | Amount blocked for payout requests |
| `utilizedSpanMargin` | Margin used for SPAN requirements on derivatives |
| `utilizedExposureMargin` | Margin used for derivative exposure requirements |

---

## Logout

`POST /profile/logout`

**Headers:** `Authorization: Bearer <userSession>`

### Response

```json
{
  "status": "Ok",
  "message": "Success",
  "result": { "status": "Success", "message": "Success" }
}
```
