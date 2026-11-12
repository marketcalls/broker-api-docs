# Authentication

Two ways to obtain a session token — the direct server-to-server flow and the OAuth 2.1 authorization-code flow — plus the login-code helpers and logout.

## Generate Session Token

`POST /session/token`

The Generate Session Token API is the **direct** way for headless / server-to-server integrations to obtain a session token using your OAuth app's `apiKey` and `apiSecret` — without launching a browser-based OAuth login.

> **INFO** — Two ways to obtain a session token
>
> 1. **Direct (this page)** — `POST /session/token` with `apiKey` + `apiSecret`. Recommended for backend bots, scheduled jobs, and any flow where the user is not present in a browser.
> 2. **[OAuth 2.1 Authorization-Code Flow](#oauth-21-authorization-code-flow)** — your app redirects the end-user to the SAMCO consent page; the user authorises on SAMCO's domain; the browser is redirected back to your callback URL with a short-lived `code`, and your backend exchanges it at `POST /oauth/token` for an `access_token` (used as `x-session-token`). Recommended when you're building a third-party app that signs in **end-users** (you never see their password or the API secret).
>
> Both flows produce a session token that is sent as the `x-session-token` header on subsequent Trade API calls.

> **WARNING** — Pre-requisites
>
> - The OAuth app must be **Active** (created via the [Web Dashboard](03-dashboard.md#dashboard-user-manual)).
> - At least one **Static IP** must be registered for the app via the dashboard. Calls to order-related APIs are rejected from non-whitelisted IPs.

### Parameter

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `apiKey` | string | true | AES-encrypted API key of the app. |
| `apiSecret` | string | true | AES-encrypted API secret of the app. |

### Sample Request Body

```json
requestBody={
    "apiKey"    : "<AES_ENCRYPTED_API_KEY>",
    "apiSecret" : "<AES_ENCRYPTED_API_SECRET>"
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/session/token' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{"apiKey":"<AES_ENCRYPTED_API_KEY>","apiSecret":"<AES_ENCRYPTED_API_SECRET>"}'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    String requestBody = """
        {
          "apiKey": "<AES_ENCRYPTED_API_KEY>",
          "apiSecret": "<AES_ENCRYPTED_API_SECRET>"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/session/token"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(requestBody))
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };

  const requestBody = {
    apiKey: "<AES_ENCRYPTED_API_KEY>",
    apiSecret: "<AES_ENCRYPTED_API_SECRET>"
  };

  const response = await fetch('https://tradeapi.samco.in/session/token', {
    method: 'POST',
    headers,
    body: JSON.stringify(requestBody),
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

requestBody = {
  "apiKey": "<AES_ENCRYPTED_API_KEY>",
  "apiSecret": "<AES_ENCRYPTED_API_SECRET>"
}

r = requests.post('https://tradeapi.samco.in/session/token',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Response

**200**

```json
{
    "serverTime": "29/01/26 10:46:06",
    "msgId": "d5f083f3-1b04-4b97-9385-1e578fdfeb7a",
    "status": "Success",
    "statusMessage": "Session token generated successfully",
    "sessionToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "tokenId": "550e8400-e29b-41d4-a716-446655440000",
    "accountID": "DV99999",
    "accountName": "JOHN DOE",
    "exchangeList": ["NSE", "BSE", "NFO", "MCX"],
    "orderTypeList": ["L", "MKT", "SL", "SL-M"],
    "productList": ["MIS", "CNC", "NRML"],
    "srcIp": "203.0.113.10",
    "primaryIp": "203.0.113.10",
    "secondaryIp": "203.0.113.11"
}
```

**400 - Missing inputs**

```json
{
    "status": "Failure",
    "statusMessage": "apiKey and apiSecret are required"
}
```

**401 - Invalid key**

```json
{
    "status": "Failure",
    "statusMessage": "Invalid API key",
    "errorCode": "EOAUTH001"
}
```

**401 - Inactive app**

```json
{
    "status": "Failure",
    "statusMessage": "Invalid or inactive API key",
    "errorCode": "EOAUTH001"
}
```

**401 - Bad secret format**

```json
{
    "status": "Failure",
    "statusMessage": "Invalid API secret format",
    "errorCode": "EOAUTH008"
}
```

**401 - Invalid secret**

```json
{
    "status": "Failure",
    "statusMessage": "Invalid API secret",
    "errorCode": "EOAUTH008"
}
```

**403 - Not subscribed**

```json
{
    "status": "Failure",
    "statusMessage": "User not subscribed. Please subscribe to access trade API"
}
```

**403 - Blocked**

```json
{
    "status": "Failure",
    "statusMessage": "User account is blocked"
}
```

**401 - Trading session could not be started**

```json
{
    "status": "Failure",
    "statusMessage": "Unable to start your trading session. Please open the SAMCO mobile app, sign in once, and then retry."
}
```

> **WARNING** — "Unable to start your trading session" — what to do
>
> This response means your `apiKey` + `apiSecret` were accepted, but our trading backend could not establish a session for the underlying SAMCO trading account. The fastest fix is for the **account holder** to:
>
> 1. **Open the SAMCO mobile app** (or [Samco Web](https://www.samco.in)) and sign in once with their Client ID + password (and OTP).
> 2. If the password is rejected, complete a **password reset** from the mobile app's *Forgot Password* flow.
> 3. If the account shows as **blocked / dormant / under review**, the user must clear that status before any API session can be issued — reach out to [support@samco.in](mailto:support@samco.in) or call the SAMCO support desk to unblock / reactivate the account.
> 4. Once a mobile-app login succeeds, retry `POST /session/token` from your integration.
>
> This applies to both this **Direct** flow and the [**OAuth 2.1 Authorization-Code Flow**](#oauth-21-authorization-code-flow) — the underlying trading-account check is the same in both cases.

### Response Schema

Status Code **200**

| Name | Type | Description |
| --- | --- | --- |
| `serverTime` | string | The date and time when the server generated the response. |
| `msgId` | string | Unique identifier for the API response message. |
| `status` | string | `Success` on a valid login. |
| `statusMessage` | string | Human-readable message. |
| `sessionToken` | string | JWT session token — send as `x-session-token` on all subsequent Trade API calls. Expires at the next 08:00 IST. |
| `tokenId` | string | Server-side identifier for this session (used internally for revocation / audit). |
| `accountID` | string | Trading account / client ID. |
| `accountName` | string | Display name on the trading account. |
| `exchangeList` | array | Exchanges available to this account (`NSE`, `BSE`, `NFO`, `MCX`, …). |
| `orderTypeList` | array | Order types this account is permitted to place. |
| `productList` | array | Product types this account is permitted to trade (`MIS`, `CNC`, `NRML`). |
| `srcIp` | string | The source IP our server sees this request coming from. |
| `primaryIp` | string | The `PRIMARY` IP currently registered for this app (or default mapping). |
| `secondaryIp` | string | The `SECONDARY` IP currently registered for this app, if any. |

> **TIP** — Verify your IP at integration time
>
> Compare `srcIp` against `primaryIp` and `secondaryIp` immediately after login. If they don't match, order-related endpoints will reject this host with HTTP 403 and `statusMessage: "The IP is not the registered static IP"`. For ongoing diagnostics from any backend host (multi-pod deployments, fallback hosts), call [`GET /ip/whoami`](05-ip-diagnostics.md#who-am-i) instead.

> **TIP** — Token lifetime
>
> The `sessionToken` is valid **until 08:00 IST the next day**. After expiry, call this endpoint again with the same `apiKey` + `apiSecret` to obtain a fresh token.

### Error codes

The same `errorCode` scheme used by the OAuth endpoints applies here so a single error-handling block in your integration can cover both flows.

| `errorCode` | Meaning | Remediation |
| --- | --- | --- |
| `EOAUTH001` | The `apiKey` cannot be decrypted, or no active OAuth app exists for it. | Confirm you are sending the AES-encrypted value emailed at app creation, and that the app is in **Active** state. If the app was created in a different environment than the one being called (or after an `AES_KEY` rotation), regenerate the app in the target environment. |
| `EOAUTH008` | The `apiSecret` cannot be decrypted, or its hash does not match the secret stored for the app. | Re-fetch the secret from the dashboard's **API Keys → Reveal Secret** flow, or regenerate it. |
| `EOAUTH009` | Calling IP is not registered for this app (only enforced on order-related calls; not on this login). | Register the IP under **Static IPs** in the dashboard. |

---

## OAuth 2.1 Authorization-Code Flow

This is the recommended way for **third-party / partner applications** to obtain a session token on behalf of an end-user — **without** ever asking the user to share their API key, API secret, or trading-account password with your app.

The flow follows the standard **OAuth 2.1 authorization-code** grant (see [oauth.net/2.1](https://oauth.net/2.1/) for the spec). Your app hands the user off to a SAMCO-hosted consent page; the user authorises the request with the app's **API Secret**; SAMCO redirects the browser back to your **callback URL** with a short-lived **authorization code**; your backend then exchanges that code for an **`access_token`** (sent as the `x-session-token` header on Trade API calls) and a **`refresh_token`**.

> **INFO** — Two ways to obtain a session token
>
> - **This page** — OAuth 2.1 authorization-code flow. Recommended when your app authenticates **end-users** through a browser (web apps, mobile apps with a webview).
> - **[Direct (`POST /session/token`)](#generate-session-token)** — For your **own** apiKey + apiSecret, headless / server-to-server use.

> **TIP** — Looking for the SAMCO Web Dashboard?
>
> The SAMCO Web Dashboard (where account holders sign in to create OAuth apps and register static IPs) is documented in the **[Dashboard User Manual](03-dashboard.md#dashboard-user-manual)**. That dashboard is **separate** from the partner OAuth consent UI described on this page.

---

### Prerequisites

1. **Create an OAuth app** in the [Web Dashboard](03-dashboard.md#dashboard-user-manual) (under **[API Keys](03-dashboard.md#api-keys)**). When creating the app, register your **Redirect URL** — this is the callback your users will land on after a successful authorisation.
2. **Register static IPs** for the app (under **[Static IPs](03-dashboard.md#static-ips)**) if you intend to call `POST /oauth/token` from a backend server.

> **WARNING** — Redirect URL rules
>
> - Must be **HTTPS** (`http://127.0.0.1` is allowed for local testing).
> - The URL your app uses at authorize time must **match** the redirect URL registered for the app — including scheme, host, port, and path.
> - If you need to change it, edit the app in the dashboard (OTP required).

---

### The flow

```
 ┌──────────────┐                          ┌─────────────────────────┐
 │ Your App     │ 1. GET /oauth/authorize  │  Samco OAuth Consent UI │
 │              │ ───────────────────────► │  tradeapi.samco.in/app  │
 │              │                          │                         │
 │              │                          │  user enters API Secret │
 │              │                          │                         │
 │              │                          │  POST /oauth/authenticate
 │              │                          │  issues 10-min auth_code│
 │              │                          │  returns redirectTo JSON│
 │              │                          │                         │
 │              │ 2. browser navigates to  │                         │
 │              │    redirect_url?code=…   │                         │
 │              │    &state=…              │                         │
 │              │                          │                         │
 │              │ 3. authorization code    │                         │
 │              │    received — must be    │                         │
 │              │    exchanged within 10m  │                         │
 │              │                          │                         │
 │ Your backend │ 4. POST /oauth/token     │                         │
 │              │    grant_type=           │                         │
 │              │      authorization_code  │                         │
 │              │ ───────────────────────► │  exchange code for      │
 │              │                          │  access_token (24h) +   │
 │              │ 5. {access_token, …}     │  refresh_token (7d)     │
 │              │ ◄─────────────────────── │                         │
 │              │                          │                         │
 │              │ 6. API call with         │                         │
 │              │    x-session-token: …    │                         │
 └──────────────┘                          └─────────────────────────┘
```

#### Step 1 — Redirect the user to the SAMCO authorize page

From your app, send the user's browser to:

```
https://tradeapi.samco.in/app/oauth/authorize
    ?api_key=<AES_ENCRYPTED_API_KEY>
    &redirect_url=https://your-app.example.com/callback
    &state=<OPTIONAL_CSRF_TOKEN>
    &scopes=<COMMA_SEPARATED_SCOPES>   (optional; defaults to "all")
```

| Query param | Required | Description |
| --- | --- | --- |
| `api_key` | yes | AES-encrypted form of your OAuth app's API key (the value mailed to you when the app was created — paste as-is, do **not** decrypt). |
| `redirect_url` | yes | Your callback URL. Must exactly match the redirect URL registered for the app. |
| `state` | no | An opaque, unguessable value generated by your app. SAMCO echoes it back unchanged in the callback so you can defend against CSRF. |
| `scopes` | no | Comma-separated list of scopes you want to request. Must be a subset of the scopes registered on the app. Defaults to `all`. The consent page forwards this to the validation endpoint but does **not** render it to the end-user in the current build. |

Behind the scenes, the page calls `GET /oauth/authorize` to validate the `api_key` + `redirect_url` (+ `scopes`) against the registered OAuth app. On success the endpoint returns:

```json
{
  "status": "Success",
  "message": "Authorization request validated. Continue with POST /oauth/authenticate to complete login and consent.",
  "data": {
    "appName":     "<your app's display name>",
    "apiKey":      "<echoed api_key>",
    "redirectUrl": "<echoed redirect_url>",
    "state":       "<echoed state>",
    "scopes":      "<resolved scopes>",
    "clientUid":   "<owner client UID>",
    "nextAction":  "/oauth/authenticate"
  }
}
```

The consent UI uses `appName` to populate the heading. While validation is in flight the user sees a brief loading screen.

If the `api_key` or `redirect_url` does not match a registered app (or the app is inactive, or the scopes don't match), the consent UI behaviour splits:

- If the supplied `redirect_url` is a valid HTTP(S) URL, the browser is redirected back to it with `?error=invalid_request&errorMessage=...&state=...` (see step 3).
- Otherwise the consent UI displays the error inline and does **not** redirect.

#### Step 2 — User authorises on the SAMCO consent page

On successful validation, the user sees the authorisation card with your **app name** clearly displayed and a single input that asks for the **API Secret** of that app.

> **WARNING** — You paste the AES-encrypted API Secret — not the plaintext
>
> The value the consent page accepts is the **AES-encrypted** API Secret (~96 hex characters) that the dashboard delivered to you on app creation / secret regeneration. Plaintext secrets are rejected by `POST /oauth/authenticate`. If you no longer have the encrypted value, regenerate it from the **API Keys** page in the dashboard.

![SAMCO OAuth consent page showing the requesting app name and the encrypted API Secret input](https://docs-tradeapi.samco.in/assets/oauth/consent-page-initial.png)

*The consent page after `GET /oauth/authorize` validates your `api_key` and `redirect_url`.*

![Consent page with the encrypted API Secret pasted and the Authorize button in its "Authorizing…" submitting state](https://docs-tradeapi.samco.in/assets/oauth/consent-page-submitting.png)

*Submitting calls `POST /oauth/authenticate`. The button disables and shows "Authorizing…" until the server responds.*

Submitting the form calls `POST /oauth/authenticate` server-side, which runs the following checks **in this order**:

1. Decrypt and look up `api_key`; reject inactive / unknown apps (`EOAUTH001`).
2. Validate `redirect_url` matches the URL registered for the app (`EOAUTH002`).
3. Decrypt `api_secret` and verify its hash against the secret stored when the app was created (`EOAUTH008`).
4. Enforce the static IP allowlist if `CLIENT_IP_MAPPING` rows are registered for this app (`EOAUTH009`).
5. Validate the requested `scopes` are a subset of those registered on the app (`EOAUTH003`).
6. Generate a **10-minute, single-use `auth_code`** — `randomBytes(32).toString('base64url')` (~43 characters) — and persist it.
7. Return `{ status: "Success", data: { redirectTo: "<redirect_url>?code=<auth_code>&state=<state>" } }`.

The consent UI then navigates the browser to `redirectTo` on the client side. (Earlier builds of `/oauth/authenticate` returned an HTTP `302` directly; the current contract returns JSON with `data.redirectTo` so failures surface inline in the consent UI rather than landing on your callback.)

> **WARNING** — Treat the encrypted API Secret as a bearer credential
>
> Even though the value the user pastes is already encrypted (not plaintext), anyone who holds it can complete the OAuth flow for your app. Open the consent page only on a trusted machine, over HTTPS, and never paste the value into a shared session. The secret is never persisted client-side — it travels through the browser only on this single submission.

If the user cancels, or any of the checks above fails after the `redirect_url` itself has been validated, the browser is redirected to the callback URL with an `error=...&errorMessage=...` instead of a `code` (see step 3 error variant below).

#### Step 3 — Browser is redirected back to your callback URL

After a successful authorisation, the browser is redirected to:

```
https://your-app.example.com/callback
    ?code=<AUTHORIZATION_CODE>
    &state=<ECHOED_STATE>
```

![Browser address bar showing the redirect to https://your-app.example.com/callback?code=…&state=…](https://docs-tradeapi.samco.in/assets/oauth/callback-url-bar.png)

*What your callback URL looks like in the user's browser after a successful authorization.*

| Query param | Description |
| --- | --- |
| `code` | A single-use authorization code — base64url-encoded, ~43 characters, valid for **10 minutes**. Exchange it at `POST /oauth/token` immediately (step 4). |
| `state` | The same `state` value your app sent in step 1. **You must verify it matches** what you generated, then discard it (prevents CSRF replay). |

If the user cancelled, the redirect carries an `error` instead of a `code`:

```
https://your-app.example.com/callback
    ?error=access_denied
    &errorMessage=User+cancelled+the+login
    &state=<ECHOED_STATE>
```

If validation in step 1 failed (bad `api_key`, mismatched `redirect_url`, inactive app, invalid scopes) **and** the supplied `redirect_url` was itself a valid HTTP(S) URL, the consent UI redirects back with:

```
https://your-app.example.com/callback
    ?error=invalid_request
    &errorMessage=<server-provided+detail>
    &state=<ECHOED_STATE>
```

If the `redirect_url` was malformed, the consent UI shows the error inline and does **not** redirect.

> **TIP** — Authorization code received
>
> Your backend must exchange this `code` at [`POST /oauth/token`](#step-4--exchange-the-code-for-an-access_token) (with `grant_type=authorization_code`) **within 10 minutes** to obtain an `access_token`. Use that `access_token` as the `x-session-token` header on subsequent Trade API calls.

#### Step 4 — Exchange the code for an `access_token`

From your **backend** (not the browser), POST the code to `/oauth/token`:

```http
POST /oauth/token HTTP/1.1
Host: tradeapi.samco.in
Content-Type: application/json

{
  "grant_type" : "authorization_code",
  "code"       : "<AUTH_CODE_FROM_STEP_3>"
}
```

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/oauth/token' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "grant_type": "authorization_code",
    "code": "<AUTH_CODE_FROM_STEP_3>"
  }'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    HttpClient client = HttpClient.newHttpClient();

    String requestBody = "{\n" +
        "  \"grant_type\": \"authorization_code\",\n" +
        "  \"code\": \"<AUTH_CODE_FROM_STEP_3>\"\n" +
        "}";

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/oauth/token"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(requestBody))
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const response = await fetch('https://tradeapi.samco.in/oauth/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    body: JSON.stringify({
      grant_type: 'authorization_code',
      code: '<AUTH_CODE_FROM_STEP_3>',
    }),
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests

payload = {
  'grant_type': 'authorization_code',
  'code': '<AUTH_CODE_FROM_STEP_3>',
}

r = requests.post('https://tradeapi.samco.in/oauth/token',
  headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
  json=payload)

print(r.json())
```

> **INFO** — Why no `api_key` / `api_secret` here
>
> The `code` itself is the credential. It is unguessable, single-use, valid only for **10 minutes**, and bound server-side to the app that authorised it. Re-sending the app credentials at token-exchange time adds no security and is not required.

Response (200):

```json
{
  "status": "Success",
  "data": {
    "access_token"             : "eyJhbGciOi...",
    "token_type"               : "Bearer",
    "expires_in"               : 86400,
    "refresh_token"            : "k6Yc7…base64url…",
    "refresh_token_expires_in" : 604800,
    "session_id"               : "9c3f…hex…",
    "user_id"                  : "ABCD1234",
    "scopes"                   : "all",
    "accountID"                : "ABCD1234",
    "accountName"              : "Jane Doe",
    "exchangeList"             : ["NSE", "BSE", "NFO", "CDS", "MCX"],
    "orderTypeList"            : ["LIMIT", "MARKET", "SL", "SL-M"],
    "productList"              : ["CNC", "MIS", "NRML"],
    "srcIp"                    : "203.0.113.42",
    "primaryIp"                : "203.0.113.42",
    "secondaryIp"              : "203.0.113.43"
  }
}
```

| Field | Description |
| --- | --- |
| `access_token` | JWT. Send it as the `x-session-token` header on all subsequent Trade API calls. Valid for **24 hours** (`expires_in: 86400`). |
| `refresh_token` | Opaque base64url string. Use it to obtain a fresh `access_token` without re-prompting the user. Valid for **7 days** (`refresh_token_expires_in: 604800`). |
| `session_id` | Server-side identifier for the session (used for revocation / audit). |
| `user_id` | Trading-account `clientUid` — same value as `accountID`. |
| `accountID` / `accountName` | Trading account metadata for the authenticated user. |
| `exchangeList` / `orderTypeList` / `productList` | What the account is enabled for. |
| `srcIp` | The client IP this token was issued to. Subsequent Trade API calls should originate from this IP. |
| `primaryIp` / `secondaryIp` | Static IPs registered for the OAuth app — useful for verifying your allowlist setup matches what's on file. |

The auth code is **single-use** — replaying it sequentially returns `EOAUTH012` and revokes all tokens issued under the same `api_key` for the user as a security measure. See [Concurrent exchanges](#concurrent-token-exchange-in-progress-please-retry-eoauth030) below for the race-vs-replay distinction.

#### Step 5 — Use the access token

```http
GET /position/getPositions HTTP/1.1
Host: tradeapi.samco.in
Accept: application/json
x-session-token: <ACCESS_TOKEN_FROM_STEP_4>
```

#### Step 6 — Refresh the access token (optional)

When `access_token` is close to expiry (or has expired within the 7-day refresh window), call `/oauth/token` again with the refresh-token grant:

```http
POST /oauth/token HTTP/1.1
Host: tradeapi.samco.in
Content-Type: application/json

{
  "grant_type"   : "refresh_token",
  "refresh_token": "<REFRESH_TOKEN_FROM_STEP_4>"
}
```

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/oauth/token' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "grant_type": "refresh_token",
    "refresh_token": "<REFRESH_TOKEN_FROM_STEP_4>"
  }'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    HttpClient client = HttpClient.newHttpClient();

    String requestBody = "{\n" +
        "  \"grant_type\": \"refresh_token\",\n" +
        "  \"refresh_token\": \"<REFRESH_TOKEN_FROM_STEP_4>\"\n" +
        "}";

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/oauth/token"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(requestBody))
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const response = await fetch('https://tradeapi.samco.in/oauth/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    body: JSON.stringify({
      grant_type: 'refresh_token',
      refresh_token: '<REFRESH_TOKEN_FROM_STEP_4>',
    }),
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests

payload = {
  'grant_type': 'refresh_token',
  'refresh_token': '<REFRESH_TOKEN_FROM_STEP_4>',
}

r = requests.post('https://tradeapi.samco.in/oauth/token',
  headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
  json=payload)

print(r.json())
```

The response shape is identical to step 4 — a new `access_token` and a new `refresh_token` (rotation). The **old refresh_token is immediately marked inactive** as part of issuing the new one, so always persist the new pair and discard the previous values atomically.

#### Step 7 — Revoke a token (logout)

```http
POST /oauth/revoke HTTP/1.1
Host: tradeapi.samco.in
Content-Type: application/json

{
  "token"     : "<ACCESS_TOKEN_OR_REFRESH_TOKEN>",
  "token_type": "access_token"
}
```

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/oauth/revoke' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{
    "token": "<ACCESS_TOKEN_OR_REFRESH_TOKEN>",
    "token_type": "access_token"
  }'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    HttpClient client = HttpClient.newHttpClient();

    String requestBody = "{\n" +
        "  \"token\": \"<ACCESS_TOKEN_OR_REFRESH_TOKEN>\",\n" +
        "  \"token_type\": \"access_token\"\n" +
        "}";

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/oauth/revoke"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(requestBody))
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const response = await fetch('https://tradeapi.samco.in/oauth/revoke', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
    },
    body: JSON.stringify({
      token: '<ACCESS_TOKEN_OR_REFRESH_TOKEN>',
      token_type: 'access_token',
    }),
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests

payload = {
  'token': '<ACCESS_TOKEN_OR_REFRESH_TOKEN>',
  'token_type': 'access_token',
}

r = requests.post('https://tradeapi.samco.in/oauth/revoke',
  headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
  json=payload)

print(r.json())
```

Revoking either token invalidates the entire session. The endpoint is **idempotent** — calling it with an unknown / already-revoked token still returns `{ "status": "Success", "message": "Token revoked successfully" }`.

---

### Sample callback handler

The SAMCO Web Dashboard ships a built-in `/callback` landing page you can point your test OAuth app at while integrating — register `https://<dashboard-host>/callback` as your app's `redirect_url` and the dashboard will render the following after a successful authorisation:

![SAMCO dashboard built-in /callback landing page — header "OAuth Callback", green "Authorization code received" panel, code and state fields with Copy buttons, and Java/Node/Python tabbed backend snippets](https://docs-tradeapi.samco.in/assets/oauth/callback-landing-page.png)

The page contains, top-to-bottom:

- A header **OAuth Callback** with a placeholder description and a **Close** button (returns to login).
- A green status panel **Authorization code received** — verbatim copy: *"Your backend must exchange this `code` at `POST /oauth/token` (with `grant_type=authorization_code`) within 10 minutes to obtain an `access_token`. Use that `access_token` as the `x-session-token` header on subsequent Trade API calls."*
- The received **`code`** and **`state`** values, each with a **Copy** button.
- A **Backend code samples** panel with three tabs — **Java**, **Node.js**, **Python** — each pre-populated with the received `code` interpolated into a runnable two-step snippet: (1) `POST /oauth/token` to exchange the code, (2) call `GET /holding/getHolding` with the resulting `access_token` in the `x-session-token` header.
- A collapsible **All query parameters** block listing every query-string key/value that landed on the URL — useful for debugging the error variants.
- A footer reminder: *"For production, replace this URL with your own backend endpoint that securely exchanges the code for an access token."*

If the redirect carried an `error=...` instead of a `code=...`, the green panel is replaced with a red **Authorization failed** panel that prints the `error` code and `errorMessage`, and no code snippets are rendered.

**JavaScript / Express**

```js
// GET https://your-app.example.com/callback?code=...&state=...
app.get('/callback', async (req, res) => {
  const { code, state, error, errorMessage } = req.query;

  // 1. CSRF check
  if (state !== req.session.oauthState) {
    return res.status(400).send('Invalid state');
  }
  delete req.session.oauthState;

  // 2. Handle error
  if (error) {
    return res.status(401).send(`Login failed: ${errorMessage}`);
  }

  // 3. Exchange code for access_token (server-to-server)
  const tokenRes = await fetch('https://tradeapi.samco.in/oauth/token', {
    method:  'POST',
    headers: { 'Content-Type': 'application/json' },
    body:    JSON.stringify({
      grant_type: 'authorization_code',
      code,
    }),
  });
  const { status, data } = await tokenRes.json();
  if (status !== 'Success') return res.status(401).send('Token exchange failed');

  // 4. Persist for the user. Use access_token as x-session-token on Trade APIs.
  req.session.samco = {
    accessToken:  data.access_token,
    refreshToken: data.refresh_token,
    sessionId:    data.session_id,
  };
  res.redirect('/dashboard');
});
```

**Python / Flask**

```py
import os, requests
from flask import request, session, redirect, abort

@app.route('/callback')
def callback():
    if request.args.get('state') != session.pop('oauth_state', None):
        abort(400, 'Invalid state')

    if request.args.get('error'):
        return f"Login failed: {request.args.get('errorMessage')}", 401

    r = requests.post('https://tradeapi.samco.in/oauth/token', json={
        'grant_type': 'authorization_code',
        'code':       request.args['code'],
    }).json()
    if r.get('status') != 'Success':
        return 'Token exchange failed', 401

    d = r['data']
    session['samco_access_token']  = d['access_token']
    session['samco_refresh_token'] = d['refresh_token']
    session['samco_session_id']    = d['session_id']
    return redirect('/dashboard')
```

---

### Troubleshooting

#### `"Unauthorized - Invalid token. sessId missing."` on Trade API calls

You are sending something other than the `access_token` from step 4 as the `x-session-token` header. The `code` from the callback URL is **not** a session token — it must first be exchanged at `POST /oauth/token` (step 4). Use the `access_token` field of that response as `x-session-token`.

#### `"Authorization code already used. All tokens revoked for security."`

The `code` returned in step 3 is single-use. If you call `POST /oauth/token` twice with the same code (or your callback fires twice), SAMCO treats it as a replay and revokes every token previously issued under the same `api_key` for the user. Re-run the full flow from step 1.

#### `"Authorization code has expired"` (EOAUTH013)

`code` is valid for **10 minutes**. Make sure your callback exchanges it promptly; don't queue it for batch processing.

#### `"Concurrent token exchange in progress. Please retry."` (EOAUTH030)

You issued two parallel `POST /oauth/token` requests with the same `code` (often a runaway retry library, or the user double-clicking through your callback). The backend uses a compare-and-swap on the code's `used` flag — the winner gets tokens, the loser gets `EOAUTH030`. Wait briefly, then re-issue **once**; if the original request actually succeeded, the retry will now surface `EOAUTH012` ("already used") because the code has been claimed.

> **INFO** — Retrying `/oauth/token` safely
>
> - **Sequential** retries inside the 10-minute window are safe **as long as the previous attempt did not succeed**. A genuine transient infrastructure error (network blip, upstream 5xx before the code was claimed) leaves the code intact.
> - **Concurrent** retries can race and produce `EOAUTH030` — serialize them.
> - Any `EOAUTH012` response means the code was already redeemed and **all tokens issued under your `api_key` for that user have been revoked**. Re-run the full authorization flow from step 1.

#### `"Unable to start your trading session"` after entering the API Secret

OAuth credentials were accepted but our trading backend could not establish a session for the underlying SAMCO trading account that owns the OAuth app. The integrator (or the account holder) should:

1. **Open the SAMCO mobile app** (or [Samco Web](https://www.samco.in)) and sign in once with the SAMCO Client ID + password (and OTP).
2. If the password is rejected, complete a **password reset** from the mobile app's *Forgot Password* flow.
3. If the account shows as **blocked / dormant / under review**, contact [support@samco.in](mailto:support@samco.in) to unblock / reactivate.
4. Retry the OAuth login.

This is also surfaced by the direct [`POST /session/token`](#generate-session-token) endpoint with the same message body.

#### Error code reference

The error codes you'll realistically encounter at runtime, mapped to the step that emits them:

| Code | Emitted by | Meaning |
| --- | --- | --- |
| `EOAUTH001` | `/oauth/authorize`, `/authenticate` | Invalid or inactive `api_key` (decrypt failure or app not Active). |
| `EOAUTH002` | `/oauth/authorize`, `/authenticate` | `redirect_url` does not match the URL registered for the app. |
| `EOAUTH003` | `/oauth/authorize`, `/authenticate` | Requested `scopes` are not a subset of those registered on the app. |
| `EOAUTH008` | `/oauth/authenticate` | Invalid `api_secret` (decrypt failure or hash mismatch). |
| `EOAUTH009` | `/oauth/authenticate`, `/token` | Request originated from an IP not on the app's static-IP allowlist. |
| `EOAUTH010` | `/oauth/token` | `code` field missing on `authorization_code` grant. |
| `EOAUTH011` | `/oauth/token` | `code` not found in the auth-codes store. |
| `EOAUTH012` | `/oauth/token` | `code` was already used — **all tokens for this `api_key` revoked**. |
| `EOAUTH013` | `/oauth/token` | `code` expired (older than 10 minutes). |
| `EOAUTH015` | `/oauth/token` | `refresh_token` field missing on `refresh_token` grant. |
| `EOAUTH016` | `/oauth/token` | `refresh_token` not found or has been invalidated. |
| `EOAUTH017` | `/oauth/token` | `refresh_token` expired (older than 7 days). |
| `EOAUTH030` | `/oauth/token` | Concurrent exchange of the same `code` — see above. |
| `EOAUTH999` | `/oauth/token` | Trading backend could not establish a session for the underlying account (see "Unable to start your trading session" above). |

---

### Why this flow?

- **No credential sharing** — end-users never hand their SAMCO password or your app's API secret to a third-party UI.
- **Standard OAuth 2.1** — well-understood authorization-code grant with replay protection on the code.
- **SEBI compliant** — authorisation happens on SAMCO's domain with full audit trail.
- **Static-IP-friendly** — the token-exchange endpoint enforces the IPs registered for your OAuth app; calls from other IPs are rejected.
- **Long-lived sessions** — 24-hour `access_token` + 7-day rotating `refresh_token` keeps integrations stable without forcing daily re-consent.

> **TIP** — Need a backend-only flow?
>
> If your integration is purely server-to-server (no end-user browser involved), use [`POST /session/token`](#generate-session-token) directly with your own `apiKey` + `apiSecret`.

---

## Login Code

`GET /webSecretCode`

The Web Login Secret Code API provides a secure and efficient way to authenticate users without the need for traditional username and password credentials. This API allows users to request a One-Time Password (OTP) that can be used for logging into the web portal at [Samco](https://web.samco.in/login).

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/webSecretCode' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/webSecretCode"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .GET()
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-session-token': '<SESSION_TOKEN>',
  };

  const response = await fetch('https://tradeapi.samco.in/webSecretCode', {
    method: 'GET',
    headers,
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-session-token': '<SESSION_TOKEN>',
}

r = requests.get('https://tradeapi.samco.in/webSecretCode',
  headers=headers)

print(r.json())
```

### Sample Response

```json
{
    "serverTime": "15/10/24 09:16:36",
    "msgId": "40c5b113-0aa6-4399-b9e0-ab5e243ae683",
    "status": "Success",
    "statusMessage": "Secret code genererated successfully.",
    "data": {
        "timeRemainingInSeconds": 120,
        "OTP": "QOHG6854"
    }
}
```

### Response Schema

Status Code **200**

| Name | Type | Description |
| --- | --- | --- |
| `serverTime` | string | The date and time when the server generated the response. |
| `msgId` | string | A unique identifier for the API response message. Useful for tracking or debugging purposes. |
| `status` | string | The status of the API response. Possible values are 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `data` | Object | An object containing specific data related to the OTP request. |
| `timeRemainingInSeconds` | Integer | Specifies the remaining time (in seconds) for which the OTP is valid. This helps users understand how long they have to use the OTP before it expires. |
| `OTP` | string | The generated One-Time Password (OTP) that the user must enter to complete the login process. This code is unique and time-sensitive, ensuring secure access to the system. |

---

## Login Code Validation

`POST /webSecretCodeValidation`

This API validates the One-Time Password (OTP) provided by the user. Upon successful OTP verification, the API returns the user's account details, similar to the login API response. The account details typically include information such as the user’s account ID, session token, user profile, and other relevant data associated with the user’s login status.

### Parameter

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `otp` | string | true | The OTP entered by the user for validation. |

### Sample Request Body

```json
requestBody={
    "otp":"NUWL3586"
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/webSecretCodeValidation' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{"otp":"NUWL3586"}'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    String requestBody = """
        {
          "otp": "NUWL3586"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/webSecretCodeValidation"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(requestBody))
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  };

  const requestBody = {
    otp: "NUWL3586"
  };

  const response = await fetch('https://tradeapi.samco.in/webSecretCodeValidation', {
    method: 'POST',
    headers,
    body: JSON.stringify(requestBody),
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

requestBody = {
  "otp": "NUWL3586"
}

r = requests.post('https://tradeapi.samco.in/webSecretCodeValidation',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Response

**200**

```json
{
    "serverTime": "13/01/25 10:10:40",
    "status": "Success",
    "statusMessage": "Login session token generated successfully",
    "sessionToken": "f4b8ec1dcc1e9486f723cb5fcba16859",
    "accountID": "RM3XXXXX",
    "accountName": "MXXXXXAD AXXX",
    "exchangeList": [
        "BFO",
        "BSE",
        "CDS",
        "MCX",
        "NSE",
        "NFO"
    ],
    "orderTypeList": [
        "MKT",
        "L",
        "SL",
        "SL-M"
    ],
    "productList": [
        "MIS",
        "CNC",
        "NRML",
        "CO",
        "BO"
    ]
}
```

**400**

```JSON

{
    "serverTime": "13/01/25 15:00:29",
    "status": "Failure",
    "validationErrors": [
        "OTP expired. Please enter valid OTP."
    ]
}
```

### Response Schema

Status Code **200**

| Name | Type | Description |
| --- | --- | --- |
| `serverTime` | string | The date and time when the server generated the response. |
| `msgId` | string | A unique identifier for the API response message. Useful for tracking or debugging purposes. |
| `status` | string | The status of the API response. Possible values are 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `sessionToken` | string | A unique token generated for the session. Used for authenticating subsequent API requests and maintaining the user's session. Valid for 24 hours from generation. |
| `accountID` | string | A unique identifier for the user's account, used to reference the user's specific account within the system. |
| `accountName` | string | The name associated with the account, providing a human-readable reference for the account holder. |
| `exchangeList` | [string] | A list of exchanges that the user has access to or can trade on. |
| `orderTypeList` | [string] | A list of order types available for trading. |
| `productList` | [string] | A list of product types enabled for the user, including CNC (Cash and Carry), BO (Bracket Order), CO (Cover Order), NRML (Normal), MIS (Intraday). |

---

## User Logout

Logging out user from the application `DELETE /logout`

### Sample Code

**cURL**

```bash
curl -X DELETE 'https://tradeapi.samco.in/logout' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/logout"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .DELETE()
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-session-token': '<SESSION_TOKEN>',
  };

  const response = await fetch('https://tradeapi.samco.in/logout', {
    method: 'DELETE',
    headers,
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-session-token': '<SESSION_TOKEN>',
}

r = requests.delete('https://tradeapi.samco.in/logout',
  headers=headers)

print(r.json())
```

### Sample Response

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "status": "Success",
  "statusMessage": "Request successful"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at the server when the response is generated. |
| `msgId` | string | Unique identifier for each request. Quote this identifier to the support team if you face issues. |
| `status` | string | Response status. Indicates whether the request was successful (`Success`) or failed (`Failure`). |
| `statusMessage` | string | Status message providing additional details about the response or any errors encountered. |
