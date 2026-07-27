# Nubra REST API LLM Builder

This file is a bundled, LLM-friendly Markdown export of the Nubra REST API documentation.

- Generated from the REST API documentation set
- Source set: docs/rest-api-v3/**
- Generated at: 2026-06-18 09:10:27 UTC
- Intended use: upload once to an LLM for backend integration, API client generation, workflow planning, and endpoint reasoning

## Notes

- YAML frontmatter has been removed from individual pages
- Embedded video iframes have been removed to reduce noise for LLM ingestion
- Page boundaries are preserved with Source markers

## Reading Hints For LLMs

- `LLM guidance` explains when to use the page, when not to use it, and which adjacent page is the better fit for a related workflow.
- `Implementation Notes` explain usage nuance, runtime behavior, or practical integration details that help code generation.
- `Important Rules` contain operational constraints, environment boundaries, identifier requirements, or safety-critical behavior that should be treated as hard guidance.
- When these sections overlap, prefer `Important Rules` as the stronger constraint signal.
---

Source: docs/rest-api-v3/index.md

<a id="page-index"></a>
<a id="page-index--rest-api-v3-payload-overview"></a>
## REST API V3 Payload Overview

<section class="version-hero">
  <div class="version-hero__eyebrow">
    UAT V3
    <span class="nav-new-badge">New</span>
  </div>
  <p><strong>Our new powerful OMS is coming soon, and as part of this transition we are providing UAT V3 access to help you test early and migrate with confidence.</strong> Use these REST API V3 pages to validate the newer trading payload structure and endpoint flow for your strategies and integrations.</p>
  <p>These pages are intended for UAT V3 validation. If you are not testing V3 yet, you can continue using the main REST API documentation. The current V2 OMS endpoints will be deprecated, so it is advised to start validating the UAT V3 endpoints as early as possible.</p>
</section>

Nubra's REST API provides a fast, secure, and scalable interface for developers building
trading systems, backend services, execution engines, or enterprise-grade market-data pipelines.
It exposes low-latency HTTP endpoints that allow complete programmatic access to Nubra's
trading infrastructure.

The REST API is designed for reliability, consistency, and performance - enabling you to
build anything from automated trading strategies to large-scale institutional systems.

---

<a id="page-index--whats-new-in-v3"></a>
## What's New In V3

This V3 track is intended for clients validating the upgraded UAT rollout.

Compared with the current public REST track, this documentation set focuses on:

- the newer V3 trading payload structure
- a cleaner and more unified OMS flow
- the UAT header contract aligned to `x-app-version: 0.4.5` or above
- updated request patterns for the upgraded UAT setup
- clearer onboarding guidance for teams validating the new UAT flow
- a transition path that still allows current users to remain on the existing public track until they are ready

---

<a id="page-index--majorly-updated-sections"></a>
## Majorly Updated Sections

If you are evaluating the V3 rollout, start with these pages first:

1. [Authentication](#page-authentication)
2. [Orders Overview](#page-trading-orders-orders)
3. [Place Order](#page-trading-orders-place-order)
4. [Place Multi Order](#page-trading-orders-place-basket-order)
5. [Place Strategy Order](#page-trading-orders-place-flexi-order)
6. [Get Order Margin](#page-trading-orders-get-margin)
7. [Realtime Order Updates](#page-trading-realtime-order-updates)

---

<a id="page-index--migration-quick-start"></a>
## Migration Quick Start

If you are currently using the public REST API track, use this order to start validating the upgraded UAT V3 flow:

1. Complete [Authentication](#page-authentication) against the upgraded UAT environment.
2. Use [Get Instruments](#page-get-instruments) to resolve the `ref_id` and exchange metadata needed by the V3 payloads.
3. Read [Orders Overview](#page-trading-orders-orders) to understand the V3 request model and intent-order flow.
4. Validate one primary placement flow using [Place Order](#page-trading-orders-place-order) or [Place Strategy Order](#page-trading-orders-place-flexi-order), depending on your integration.
5. Use [Get Order Margin](#page-trading-orders-get-margin) and [Realtime Order Updates](#page-trading-realtime-order-updates) to complete your UAT verification path.

---

<a id="page-index--key-features"></a>
## Key Features

- **REST-like resource-based endpoints** using standard HTTP verbs  
- **Low-latency order execution** for regular, CO, flexi, and basket orders  
- **Comprehensive market data access** including quotes, Greeks, and historical data  
- **Portfolio & account data** including positions, holdings, and available funds  
- **Secure MPIN-based authentication** for all critical operations  
- **Consistent JSON request/response format** for seamless integration  
- **Language-agnostic** - works with Python, JavaScript, Go, Rust, Java, C#, and more  

---

<a id="page-index--who-is-this-api-for"></a>
## Who Is This API For?

The REST API is ideal for:

- Backend and server-side systems  
- Execution engines and OMS/RMS infrastructure  
- Institutional and proprietary trading desks  
- Traders who prefer raw HTTP APIs over SDK abstractions  
- Developers integrating Nubra into multi-language codebases  

If you need maximum control, custom orchestration, or advanced system-to-system automation,
the REST API is the right tool.

---

<a id="page-index--authentication-model"></a>
## Authentication Model

All REST requests require:

1. **API Key (client_id)**  
2. **MPIN-based session (MPIN -> session token)**  

Once authenticated, you can generate session tokens and call any trading or market-data endpoint.

Authentication flow:

1. Login using user ID  
2. Submit MPIN securely  
3. Receive an encrypted session token  
4. Use the session token for all API requests in the `Authorization` header  

Detailed endpoints are available in the **Authentication** section.

---

<a id="page-index--market-data"></a>
## Market Data

Using the REST API, you can retrieve:

- Live market quotes  
- Greeks and option chain snapshots  
- Historical candles (OHLCV)  
- Order book data  
- Intraday and multi-day timeframes  

Market-data responses follow a consistent JSON structure designed for speed and easy parsing.

---

<a id="page-index--trading"></a>
## Trading

The REST API supports:

- Placing new orders (all varieties)  
- Modifying price/quantity  
- Cancelling pending orders  
- Basket and multi-leg execution  
- Fetching complete order book and trade book  

All trading operations are validated and protected with session-level security.

---

<a id="page-index--portfolio-funds"></a>
## Portfolio & Funds

REST endpoints also expose:

- Current positions  
- Holding breakup with average buy price  
- Fund availability  
- Margin details  
- P&L data  

These endpoints allow complete portfolio lifecycle management for both live and automated trading.

---

<a id="page-index--rate-limits-best-practices"></a>
## Rate Limits & Best Practices

To ensure stability and fair usage:

- All endpoints follow defined rate limits  
- Burst traffic is handled gracefully  
- Clients should cache non-live data where possible  
- Long-running strategies should refresh tokens proactively  

Details are documented alongside each endpoint group.

---

<a id="page-index--getting-started"></a>
## Getting Started

To begin using the REST API:

1. Generate API credentials  
2. Authenticate using your MPIN  
3. Create a session token  
4. Start making HTTP requests to trading or data endpoints  

Sample request/response payloads are included in each endpoint's documentation.

---

<a id="page-index--support"></a>
## Support

If you require help, guidance, or have questions about integration, feel free to contact:

**support@nubra.io**

Our team will be happy to assist you with API onboarding and usage.

---

Source: docs/rest-api-v3/authentication.md

<a id="page-authentication"></a>
<a id="page-authentication--authentication"></a>
## Authentication

<section class="version-hero">
  <div class="version-hero__eyebrow">
    REST API V3
    <span class="nav-new-badge">New</span>
  </div>
  <p>This authentication guide is for users validating the upgraded UAT REST setup and V3 payload flow.</p>
  <p>For now, expose and test only the UAT login flow in this V3 track. Production V3 URLs are intentionally omitted here. All authenticated examples below assume the current UAT header contract with <code>x-app-version: 0.4.5</code>.</p>
</section>

<a id="page-authentication--nubra-auth-flow"></a>
## Nubra Auth Flow

<a id="page-authentication--api-endpoints"></a>
### API Endpoints

| Environment | Base URL |
|-------------|----------|
| UAT | `https://uatapi.nubra.io` |

<a id="page-authentication--step-1-generate-temporary-token"></a>
### Step 1: Generate Temporary Token

Initiates the login flow and returns a `temp_token`. This token is required for the OTP request in the next step.

```text
Method: POST
Endpoint: /sendphoneotp
```

<a id="page-authentication--curl"></a>
#### cURL

```bash
curl --location 'https://uatapi.nubra.io/sendphoneotp' \
--header 'Content-Type: application/json' \
--data '{
  "phone": "0000000000",
  "skip_totp": false
}'
```

<a id="page-authentication--payload"></a>
#### Payload

```json
{
  "phone": "0000000000",
  "skip_totp": false
}
```

<a id="page-authentication--response"></a>
#### Response

```json
{
  "attempts_left": 4,
  "email": "xyz@gmail.com",
  "expiry": 30,
  "flow": "LOGIN",
  "message": "OTP sent",
  "next": "VERIFY_MOBILE",
  "phone": "0000000000",
  "temp_token": "eyJh...zd0"
}
```

> Save the `temp_token` from this response. This token must be passed in the `x-temp-token` header in Step 2. Also choose the `x-device-id` to be used for this login session, for example `12345mac` or `TS123`.

<a id="page-authentication--step-2-send-otp"></a>
### Step 2: Send OTP

Uses the `temp_token` from Step 1 to generate and send the OTP required for login.

```text
Method: POST
Endpoint: /sendphoneotp
```

<a id="page-authentication--curl"></a>
#### cURL

```bash
curl --location 'https://uatapi.nubra.io/sendphoneotp' \
--header 'x-temp-token: eyJh...zd0' \
--header 'Content-Type: application/json' \
--data '{
  "phone": "0000000000",
  "skip_totp": true
}'
```

<a id="page-authentication--headers"></a>
#### Headers

- `x-temp-token`: `temp_token` returned in Step 1

<a id="page-authentication--payload"></a>
#### Payload

```json
{
  "phone": "0000000000",
  "skip_totp": true
}
```

<a id="page-authentication--response"></a>
#### Response

```json
{
  "attempts_left": 4,
  "email": "xyz@gmail.com",
  "expiry": 30,
  "flow": "LOGIN",
  "message": "OTP sent",
  "next": "VERIFY_MOBILE",
  "phone": "0000000000",
  "temp_token": "eyJh...zd0"
}
```

> Save the new `temp_token` returned in this response. This updated token must be used during OTP verification in Step 3.

<a id="page-authentication--step-3-verify-otp"></a>
### Step 3: Verify OTP

Validates the OTP received on the registered mobile number. Use the latest `temp_token` and the same `x-device-id` selected for this login session.

```text
Method: POST
Endpoint: /verifyphoneotp
```

<a id="page-authentication--curl"></a>
#### cURL

```bash
curl --location 'https://uatapi.nubra.io/verifyphoneotp' \
--header 'x-temp-token: eyJh...zd0' \
--header 'x-device-id: TS123' \
--header 'Content-Type: application/json' \
--data '{
  "phone": "0000000000",
  "otp": "341874"
}'
```

<a id="page-authentication--headers"></a>
#### Headers

- `x-temp-token`: Latest `temp_token` returned by the previous step
- `x-device-id`: Device identifier selected for this login session, for example `TS123`

<a id="page-authentication--payload"></a>
#### Payload

```json
{
  "phone": "0000000000",
  "otp": "341874"
}
```

<a id="page-authentication--response"></a>
#### Response

```json
{
  "auth_token": "7a1171e6-790c-40fa-ae16-b71cfd19923f",
  "flow": "LOGIN",
  "message": "User Created Successfully",
  "next": "ENTER_MPIN"
}
```

> Save the `auth_token`. This token is used as the Bearer token in Step 4.

<a id="page-authentication--step-4-verify-pin"></a>
### Step 4: Verify PIN

Validates the user's MPIN and returns the final authenticated session.

```text
Method: POST
Endpoint: /verifypin
```

<a id="page-authentication--curl"></a>
#### cURL

```bash
curl --location 'https://uatapi.nubra.io/verifypin' \
--header 'x-device-id: TS123' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 7a1171e6-790c-40fa-ae16-b71cfd19923f' \
--data '{
  "pin": "1234"
}'
```

<a id="page-authentication--authorization"></a>
#### Authorization

- Type: Bearer Token
- Token: `auth_token` returned in Step 3

<a id="page-authentication--headers"></a>
#### Headers

- `x-device-id`: Same device ID used in Step 3
- `x-temp-token`: Do not include this header in this request

<a id="page-authentication--payload"></a>
#### Payload

```json
{
  "pin": "1234"
}
```

<a id="page-authentication--response"></a>
#### Response

```json
{
  "email": "xyz@gmail.com",
  "message": "Login Successful",
  "next": "DASHBOARD",
  "phone": "0000000000",
  "session_token": "eyJh...6Pno",
  "userId": 224
}
```

> The `session_token` returned in this response is the final login token. Use it as the Bearer token for authenticated REST APIs such as market data, trading, portfolio, and account endpoints.

<a id="page-authentication--authenticated-request-headers"></a>
### Authenticated Request Headers

For authenticated REST API calls in the UAT V3 track, send the same header set used by the current SDK:

- `Authorization: Bearer <session_token>`
- `x-device-id: <device_id>`
- `x-app-version: 0.4.5`
- `x-device-os: sdk`
- `Cookie: deviceId=<device_id>`

<a id="page-authentication--totp-authentication"></a>
## TOTP Authentication

The TOTP login flow is a secondary authentication method that can be enabled or disabled after a client has logged in.
Once logged in, the client receives a session token, which is used as a bearer token to initiate the TOTP login flow.

<a id="page-authentication--step-1-generate-totp-secret"></a>
### Step 1: Generate TOTP Secret

```text
Method: GET
Endpoint: /totp/generate-secret

```

<a id="page-authentication--curl"></a>
#### cURL

```bash
curl --location 'https://uatapi.nubra.io/totp/generate-secret' \
--header 'Authorization: Bearer {{session_token}}' \
--header 'x-device-id: {{device_id}}' \
--header 'x-app-version: 0.4.5' \
--header 'x-device-os: sdk' \
--header 'Cookie: deviceId={{device_id}}'
```

Headers

- `Authorization`: Bearer `session_token` (from first-time login)
- `x-device-id`: Your device ID (e.g., `TS123`)
- `x-app-version`: SDK/app version string used for the session, for example `0.4.5`
- `x-device-os`: Use `sdk`
- `Cookie`: `deviceId={{device_id}}`

<a id="page-authentication--response"></a>
#### Response

```json
{
  "data": {
    "secret_key": "BTZYQ6WQ3XSHXOWEMIZC5FTDKB6ODQJP",
    "qr_image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgAAAAIAAQMAAADOtka5AAAABlBMVEX///8AAABVwtN+R2mIrU++xzyRmap3jAAA4AlIkbD0EV8bHCc/0AsLCwsL5ErkJggg=="
  },
  "message": "Enable TOTP flow by verifying TOTP"
}
```

> This endpoint returns a **TOTP secret**.
> 

     The client must save this secret and add it to an Authenticator App (e.g., Google      Authenticator or any other preferred TOTP-compatible app).

---

<a id="page-authentication--step-2-enable-totp"></a>
### Step 2: Enable TOTP

```text
Method: POST
Endpoint: /totp/enable

```

<a id="page-authentication--curl"></a>
#### cURL

```bash
curl --location 'https://uatapi.nubra.io/totp/enable' \
--header 'Authorization: Bearer {{session_token}}' \
--header 'x-device-id: {{device_id}}' \
--header 'x-app-version: 0.4.5' \
--header 'x-device-os: sdk' \
--header 'Cookie: deviceId={{device_id}}' \
--header 'Content-Type: application/json' \
--data '{
  "mpin": "1234",
  "totp": "123456"
}'

```
<a id="page-authentication--payload"></a>
#### Payload

```json
{
  "mpin": "1234",
  "totp": "1234"
}
```

<a id="page-authentication--response"></a>
#### Response

```json
{
    "message": "TOTP verified successfully"
}

```

---

<a id="page-authentication--step-3-login-via-totp"></a>
### Step 3: Login via TOTP

```text
Method: POST
Endpoint: /totp/login

```

<a id="page-authentication--curl"></a>
#### cURL

```bash
curl --location 'https://uatapi.nubra.io/totp/login' \
--header 'x-device-id: {{device_id}}' \
--header 'x-app-version: 0.4.5' \
--header 'x-device-os: sdk' \
--header 'Cookie: deviceId={{device_id}}' \
--header 'Content-Type: application/json' \
--data '{
  "phone": "0000000000",
  "totp": 847851,
  "otp": ""
}'

```

<a id="page-authentication--payload"></a>
#### Payload
```json
{
  "phone": "0000000000",
  "totp": 307215,
  "otp": ""
}

```

<a id="page-authentication--response"></a>
#### Response

```json
{
    "auth_token": "40e10d2e-fe48-4651-becb-7a97261d63cc",
    "flow": "LOGIN",
    "message": "User Created Successfully",
    "next": "ENTER_MPIN"
}

```

---

<a id="page-authentication--step-4-verify-pin"></a>
### Step 4: Verify PIN

```text
Method: POST
Endpoint: /verifypin

```

<a id="page-authentication--curl"></a>
#### cURL

```bash
curl --location 'https://uatapi.nubra.io/verifypin' \
--header 'x-device-id: {{device_id}}' \
--header 'x-app-version: 0.4.5' \
--header 'x-device-os: sdk' \
--header 'Cookie: deviceId={{device_id}}' \
--header 'Authorization: Bearer 7a1171e6-790c-40fa-ae16-b71cfd19923f' \
--header 'Content-Type: application/json' \
--data '{
  "pin": "1234"
}'

```

<a id="page-authentication--payload"></a>
#### Payload

```json
{
  "pin": "1234"
}

```

<a id="page-authentication--response"></a>
#### Response

```json
{
    "email": "kavya@zanskar.xyz",
    "message": "Login Successful",
    "next": "DASHBOARD",
    "phone": "000000000",
    "session_token": "eyJhbGciOi...Dz5T5dMRgY",
    "userId": 35
}
```

> Use this session token for accessing all protected APIs.

---

<a id="page-authentication--disable-totp"></a>
#### Disable TOTP

```text
Method: POST
Endpoint: /totp/disable

```

<a id="page-authentication--curl"></a>
#### cURL

```bash
curl --location 'https://uatapi.nubra.io/totp/disable' \
--header 'Authorization: Bearer {{session_token}}' \
--header 'x-device-id: {{device_id}}' \
--header 'x-app-version: 0.4.5' \
--header 'x-device-os: sdk' \
--header 'Cookie: deviceId={{device_id}}' \
--header 'Content-Type: application/json' \
--data '{
  "mpin": "1234"
}'

```
<a id="page-authentication--payload"></a>
#### Payload

```json
{
  "mpin": "1234"
}
```

<a id="page-authentication--response"></a>
#### Response

```json
{
  "message": "Disabled TOTP successfully"
}
```

---

Source: docs/rest-api-v3/RateLimits.md

<a id="page-ratelimits"></a>
<a id="page-ratelimits--rate-limits-api-usage"></a>
## Rate Limits & API Usage

<section class="version-hero">
  <div class="version-hero__eyebrow">
    REST API V3
    <span class="nav-new-badge">New</span>
  </div>
  <p>These usage limits are the operating baseline for the upgraded UAT REST V3 validation track.</p>
  <p>Use this page while testing the newer V3 payload flow in the upgraded UAT environment.</p>
</section>

This page outlines the rate limits and usage guidelines for Nubra’s REST and WebSocket APIs. Adhering to these limits is crucial for stable, uninterrupted algorithmic trading.

---

<a id="page-ratelimits--api-rate-limits-summary"></a>
## API Rate Limits Summary

Nubra maintains separate limits for different API categories to ensure high-throughput trading and reliable market data streams.

| API Category | Limit | Notes |
| :--- | :--- | :--- |
| **Trading APIs (UAT)** | **100 operations/sec** | Higher OPS cap for testing and simulation purposes. |
| **Historical Data (REST)** | **60 requests/min** | Intended for backtesting and analysis workloads. |
| **Live Market Data (WebSocket)** | **Weight-based limits** | Subscription limits are governed by a weight-based tier system. |

---

<a id="page-ratelimits--trading-api-limits"></a>
## Trading API Limits

The core trading APIs (placing, modifying, and canceling orders) are optimized for low-latency execution and are subject to exchange-defined constraints.

- **UAT Environment Limit:** **100 ops/sec** for testing and dry runs.
- **Enforcement:** Limits are applied **per IP address**.
- **Note:** Treat the UAT limit as a validation baseline rather than a production throughput promise.

---

<a id="page-ratelimits--market-data-limits"></a>
## Market Data Limits

Market data access is governed by separate rules for REST and WebSocket APIs.

<a id="page-ratelimits--rest-historical-data"></a>
### REST (Historical Data)

- Limited to **60 requests per minute**.

<a id="page-ratelimits--websocket-live-market-data"></a>
### WebSocket (Live Market Data)

- WebSocket subscriptions are governed by a **weight-based tier system**.
- Each WebSocket stream type consumes a predefined number of **weight points**.
- The **free tier** provides a capped amount of total weight per session.
- Clients may subscribe to any combination of streams as long as the **total session weight remains within the allowed limit**.
- Subscription requests exceeding the allowed weight are **rejected with an error**.
- Clients must **unsubscribe from existing streams** to free up weight before adding new subscriptions.

For detailed stream weights and tier limits, refer to the **WebSocket Subscription Tiers & Weights** documentation.

---

---

Source: docs/rest-api-v3/errors_and_exceptions.md

<a id="page-errors_and_exceptions"></a>
<a id="page-errors_and_exceptions--errors-exceptions"></a>
## Errors & Exceptions

Nubra REST API V3 returns compact error payloads and a small set of important status codes.

This page documents the response shape that clients should handle in the current V3 flow.

---

<a id="page-errors_and_exceptions--error-response-format"></a>
## Error Response Format

The current REST V3 error shape is:

```json
{
  "error": "Description of the issue",
  "nubra_error_code": ""
}
```

<a id="page-errors_and_exceptions--fields"></a>
### Fields

| Field | Type | Description |
|-------|-------|-------------|
| **error** | string | Human-readable explanation of the failure. |
| **nubra_error_code** | string | Reserved for future use. Currently empty (`""`). |

---

<a id="page-errors_and_exceptions--http-status-codes"></a>
## HTTP Status Codes

<a id="page-errors_and_exceptions--400-bad-request"></a>
### 400 - Bad Request

The request is invalid or violates trading rules.

Typical causes include:

- missing required fields
- invalid or unsupported parameters
- wrong data types
- invalid instrument identifiers
- quantity or price rule violations
- malformed trigger, stop-loss, target, or basket payloads

Example:

```json
{
  "error": "Enter valid inputs to proceed.",
  "nubra_error_code": ""
}
```

<a id="page-errors_and_exceptions--440-authentication-session-failure"></a>
### 440 - Authentication / Session Failure

Some authenticated endpoints may return HTTP `440` when the session is expired, invalid, or no longer usable.

Clients should treat this as a re-authentication case rather than a retriable trading error.

<a id="page-errors_and_exceptions--500-internal-server-error"></a>
### 500 - Internal Server Error

An unexpected backend or OMS failure occurred.

Typical causes include:

- upstream OMS or internal service failure
- internal validation or routing failure
- unexpected backend exception

These errors are not caused by normal client input and should be logged and retried carefully.

---

<a id="page-errors_and_exceptions--recommended-client-handling"></a>
## Recommended Client Handling

<a id="page-errors_and_exceptions--for-http-400"></a>
### For HTTP 400

- validate request payloads before sending
- confirm enum values and field names
- confirm instrument IDs and price rules
- surface the `error` string directly in logs or client diagnostics

<a id="page-errors_and_exceptions--for-http-440"></a>
### For HTTP 440

- refresh or recreate the session
- repeat the request only after authentication succeeds again

<a id="page-errors_and_exceptions--for-http-500"></a>
### For HTTP 500

- retry after a short delay
- use exponential backoff for automated systems
- log request context and response body for debugging

---

Source: docs/rest-api-v3/get-instruments.md

<a id="page-get-instruments"></a>
<a id="page-get-instruments--get-instruments"></a>
## Get Instruments

<section class="version-hero">
  <div class="version-hero__eyebrow">
    REST API V3
    <span class="nav-new-badge">New</span>
  </div>
  <p>Use this instrument master page as the starting point for the upgraded UAT REST V3 flow.</p>
  <p>The returned <code>ref_id</code>, exchange metadata, and underlying fields here feed directly into the V3 order, market-data, and realtime payload examples in this hidden track.</p>
</section>

Retrieve instrument reference data for a specific date.

`exchange` can be `NSE`, `BSE`, or `MCX`. If you do not pass an exchange, use `NSE` as the default.

```jsx
Method:GET
Endpoint:refdata/refdata/{Date}?exchange=NSE
```

<a id="page-get-instruments--curl"></a>
### cURL
```bash
curl --location 'https://uatapi.nubra.io/refdata/refdata/2025-06-27?exchange=NSE' \
--header 'x-device-id: TS1234' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VJZCI6IlRTMTIzNCIsImV4cCI6MTc1MTA1Mjc2MSwibG9naW5fbW9kZSI6InVzZXIiLCJzZXNzaW9uSWQiOiI4N2QxZDE5YS0zZTkyLTQ4MWItYTQ3OC1mMDA5MTVmNjMyNWQiLCJzdWIiOiJhYmhpbmF2Nzk0N0BnbWFpbC5jb20iLCJ1c2VySWQiOjIyNH0.l60cnTEUspV1PXhM7LMdrLPPB6ZXBWkZvROEwpYLYdE'
```

<a id="page-get-instruments--parameters"></a>
### Parameters
- `date` (path parameter): The date for which to retrieve instrument data in YYYY-MM-DD format
- `exchange` (query parameter): Exchange code such as `NSE`, `BSE`, or `MCX`

<a id="page-get-instruments--headers"></a>
## Headers
- `x-device-id`: Device identifier
- `Authorization`: Bearer token for authentication

<a id="page-get-instruments--sample-response"></a>
## Sample Response

```json
{
    "exchange": "NSE",
    "is_trading_on": true,
    "message": "refdata",
    "refdata": [
        {
            "ref_id": 739119,
            "strike_price": 2990000,
            "option_type": "CE",
            "token": 35187,
            "stock_name": "NIFTY2570329900CE",
            "series": "__",
            "zanskar_name": "OPT_NIFTY_20250703_CE_2990000",
            "lot_size": 75,
            "asset": "NIFTY",
            "expiry": 20250703,
            "exchange": "NSE",
            "derivative_type": "OPT",
            "isin": "N/A         ",
            "asset_type": "INDEX_FO",
            "tick_size": 5,
            "underlying_prev_close": 2554900
        }
    ]
}
```

<a id="page-get-instruments--response-fields"></a>
## Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `is_trading_on` | boolean | Indicates if trading is active on the specified date |
| `message` | string | Response message |
| `refdata` | array | Array of instrument reference data |

<a id="page-get-instruments--instrument-object-fields"></a>
### Instrument Object Fields

| Field | Type | Description |
|-------|------|-------------|
| `ref_id` | integer | Unique reference ID for the instrument |
| `strike_price` | integer | Strike price for options |
| `option_type` | string | Option type (CE for Call, PE for Put) |
| `token` | integer | Token identifier |
| `stock_name` | string | Stock/instrument name |
| `series` | string | Series identifier |
| `zanskar_name` | string | Zanskar platform specific name |
| `lot_size` | integer | Lot size for the instrument |
| `asset` | string | Underlying asset name |
| `expiry` | integer | Expiry date in YYYYMMDD format |
| `exchange` | string | Exchange code such as `NSE`, `BSE`, or `MCX` |
| `derivative_type` | string | Type of derivative (OPT for options) |
| `isin` | string | ISIN code |
| `asset_type` | string | Asset type classification |
| `tick_size` | integer | Minimum price movement |
| `underlying_prev_close` | integer | Previous closing price of underlying asset |

<a id="page-get-instruments--notes"></a>
## Notes

- Use the returned `exchange` values to separate `NSE`, `BSE`, and `MCX` instrument masters.
- For derivative rows, the `asset` field is the underlying name to carry into option-chain snapshot or realtime option subscriptions.

---

Source: docs/rest-api-v3/market-data/bhavcopy.md

<a id="page-market-data-bhavcopy"></a>
<a id="page-market-data-bhavcopy--end-of-day-bhavcopy-reports"></a>
## End of Day Bhavcopy (Reports)

The End of Day Bhavcopy API provides official NSE end-of-day reports in CSV format.  
These reports are generated after market close and are commonly used for reconciliation, reporting, analytics, and historical storage.

```jsx
Method: GET
Endpoint: bhavcopy/nse/{date}?format=csv&type={type}
```

<a id="page-market-data-bhavcopy--curl"></a>
## cURL

```bash
curl --location --globoff \
'https://uatapi.nubra.io/bhavcopy/nse/{date}?format=csv&type={type}' \
--header 'x-device-id: TS123' \
--header 'Authorization: Bearer eyJh...6Pno'
```

<a id="page-market-data-bhavcopy--path-parameters"></a>
## Path Parameters

| **Parameter** | **Description** |
|---|---|
| `date` | Trading date in `YYYYMMDD` format (must be a completed trading day) |
| `type` | Type is `FO`,`OP`,`BhavcopyFO`,`BhavcopySec`,`BhavcopyCM`,`PD`,`PR`|

<a id="page-market-data-bhavcopy--query-parameters"></a>
## Query Parameters

| **Parameter** | **Description** |
|---|---|
| `format` | Response format. Supported value: `csv` and `json` |
| `type` | Bhavcopy / report type including date suffix (see supported types below) |

<a id="page-market-data-bhavcopy--supported-bhavcopy-report-types"></a>
## Supported Bhavcopy & Report Types

The `type` parameter must include the date in `YYYYMMDD` format and must match the `{date}` in the endpoint.

| **Type Format** | **Description** | **Example Output File** |
|---|---|---|
| `BhavcopyFO{yyyymmdd}` | NSE Futures & Options Bhavcopy | `BhavCopy_NSE_FO_0_0_0_20251016_F_0000.csv` |
| `BhavcopyCM{yyyymmdd}` | NSE Cash Market Bhavcopy | `BhavCopy_NSE_CM_0_0_0_20251016_F_0000.csv` |
| `BhavcopySec{yyyymmdd}` | Security-wise Bhavcopy | `sec_bhavdata_full_16102025.csv` |
| `FO{yyyymmdd}` | FO Daily Report | `fo161025.csv` |
| `OP{yyyymmdd}` | Options Report | `op161025.csv` |
| `PD{yyyymmdd}` | Price Data Report | `pd16102025.csv` |
| `PR{yyyymmdd}` | Price Range Report | `pr16102025.csv` |

> ⚠️ **Important**
> - `{date}` in the endpoint and `{yyyymmdd}` in `type` must be identical  
> - Requests for future dates or non-trading days will fail

<a id="page-market-data-bhavcopy--example-request"></a>
## Example Request

```bash
curl --location --globoff \
'https://uatapi.nubra.io/bhavcopy/nse/20251016?format=csv&type=BhavcopyFO20251016' \
--header 'x-device-id: TS123' \
--header 'Authorization: Bearer eyJh...6Pno'
```

<a id="page-market-data-bhavcopy--response"></a>
## Response

- **Content-Type:** `text/csv`
- **Response Body:** Raw CSV file

<a id="page-market-data-bhavcopy--response-behavior"></a>
## Response Behavior

| **Scenario** | **Behavior** |
|---|---|
| Valid trading date and type | CSV file returned |
| Bhavcopy not generated yet | HTTP 440 |
| Future or invalid date | HTTP 440 |
| Invalid or expired session | HTTP 440 |

<a id="page-market-data-bhavcopy--common-use-cases"></a>
## Common Use Cases

- End-of-day reconciliation
- Portfolio valuation and P&L
- Historical data ingestion
- Back-office reporting
- Dashboards and analytics pipelines

<a id="page-market-data-bhavcopy--notes-for-developers"></a>
## Notes for Developers

- Bhavcopies are generated after market close
- Availability varies by report type
- API returns raw CSV only
- Ensure session token is valid before requesting reports

---

Source: docs/rest-api-v3/market-data/current-price.md

<a id="page-market-data-current-price"></a>
<a id="page-market-data-current-price--current-price"></a>
## Current Price

This endpoint supports instruments from `NSE`, `BSE`, and `MCX`. If `exchange` is omitted, use `NSE` as the default.

The Current Price API provides the latest market price snapshot for a given instrument or index across supported exchanges.

```jsx
Method: GET
Endpoint: optionchains/{instrument}/price
```

<a id="page-market-data-current-price--example-curl-requests"></a>
## Example cURL Requests

=== "NSE"

    ```bash
    curl --location 'https://uatapi.nubra.io/optionchains/NIFTY/price' \
    --header 'x-device-id: TS123' \
    --header 'Authorization: Bearer eyJh...6Pno'
    ```

=== "BSE"

    ```bash
    curl --location 'https://uatapi.nubra.io/optionchains/SENSEX/price?exchange=BSE' \
    --header 'x-device-id: TS123' \
    --header 'Authorization: Bearer eyJh...6Pno'
    ```

=== "MCX"

    ```bash
    curl --location 'https://uatapi.nubra.io/optionchains/FUT_CRUDEOIL_20260618/price?exchange=MCX' \
    --header 'x-device-id: TS123' \
    --header 'Authorization: Bearer eyJh...6Pno'
    ```

---

<a id="page-market-data-current-price--path-parameters"></a>
## Path Parameters

| **Parameter** | **Type** | **Required** | **Description** |
|--------------|---------|-------------|-----------------|
| instrument | string | Yes | Trading symbol of the instrument or index (e.g. `NIFTY`, `RELIANCE`, `BANKNIFTY`) |

---

<a id="page-market-data-current-price--query-parameters"></a>
## Query Parameters

| **Parameter** | **Type** | **Required** | **Description** |
|--------------|---------|-------------|-----------------|
| exchange | string | No | Exchange for the instrument. Defaults to `NSE`. Supported values: `BSE`, `MCX` |

> ⚠️ When `exchange` is `NSE` or not provided, the default endpoint is used without query parameters.

---

<a id="page-market-data-current-price--example-endpoints"></a>
## Example Endpoints

- **NSE (default)**  
  ```
  optionchains/NIFTY/price
  ```

- **BSE**  
  ```
  optionchains/SENSEX/price?exchange=BSE
  ```

- **MCX**  
  ```
  optionchains/FUT_CRUDEOIL_20260618/price?exchange=MCX
  ```

---

<a id="page-market-data-current-price--response-structure"></a>
## Response Structure

```jsx
{
  "message": "current price",
  "exchange": "NSE",
  "price": 2575555,
  "prev_close": 2572755,
  "change": 0.10883275
}
```

---

<a id="page-market-data-current-price--response-attributes"></a>
## Response Attributes

| **Field** | **Description** |
|---------|-----------------|
| message | Description of the response |
| exchange | Exchange of the instrument |
| price | Latest traded price of the instrument (integer, exchange price units) |
| prev_close | Previous closing price of the instrument |
| change | Percentage change from previous close |

---

<a id="page-market-data-current-price--notes"></a>
## Notes

- Authentication via `Authorization` and `x-device-id` headers is mandatory.
- NSE is used by default when `exchange` is not specified.
- This API returns a **snapshot** of the current price.
- The response format is **uniform across all instruments and indices**.
- Price values are returned in **exchange-defined integer units**.
- Prices are subject to market availability and exchange rules.

---

Source: docs/rest-api-v3/market-data/market-quotes.md

<a id="page-market-data-market-quotes"></a>
<a id="page-market-data-market-quotes--market-quotes"></a>
## Market Quotes

This endpoint supports `ref_id` values resolved from the `NSE`, `BSE`, and `MCX` instrument masters.

The Market Quote API provides market quotes for specified instruments.

```jsx
Method: GET
Endpoint: orderbooks/{ref_id}?levels={levels}
```

<a id="page-market-data-market-quotes--example-curl-requests"></a>
## Example cURL Requests

Use a `ref_id` resolved from the matching exchange instruments master. The endpoint does not take an `exchange` query parameter; exchange context comes from the selected `ref_id`.

=== "NSE"

    ```bash
    curl --location --globoff 'https://uatapi.nubra.io/orderbooks/{nse_ref_id}?levels=5' \
    --header 'x-device-id: TS123' \
    --header 'Authorization: Bearer eyJh...6Pno'
    ```

=== "BSE"

    ```bash
    curl --location --globoff 'https://uatapi.nubra.io/orderbooks/{bse_ref_id}?levels=5' \
    --header 'x-device-id: TS123' \
    --header 'Authorization: Bearer eyJh...6Pno'
    ```

=== "MCX"

    ```bash
    curl --location --globoff 'https://uatapi.nubra.io/orderbooks/{mcx_ref_id}?levels=5' \
    --header 'x-device-id: TS123' \
    --header 'Authorization: Bearer eyJh...6Pno'
    ```

<a id="page-market-data-market-quotes--response-structure"></a>
### Response Structure

```jsx
{
  "orderBook": {
    "inst_id": 3045,
    "ref_id": 70115,
    "ts": 1749714670835214187,
    "bid": [
      { "p": 81065, "q": 142, "o": 3 }
    ],
    "ask": [
      { "p": 81080, "q": 79, "o": 2 }
    ],
    "ltp": 81080,
    "ltq": 9,
    "volume": 6565771
  }
}
```

<a id="page-market-data-market-quotes--response-attributes"></a>
### Response attributes

| **Fields** | **Description** |
| --- | --- |
| orderBook | OrderBook object containing the market quote data |
| orderBook.ref_id | Reference ID of the instrument |
| orderBook.timestamp | Timestamp of the quote in nanoseconds |
| orderBook.bid | List of BidAsk objects for bid orders, sorted by price in descending order |
| orderBook.bid[].price | Price of the bid order |
| orderBook.bid[].quantity | Quantity available at this bid price |
| orderBook.bid[].num_orders | Number of orders at this bid price |
| orderBook.ask | List of BidAsk objects for ask orders, sorted by price in ascending order |
| orderBook.ask[].price | Price of the ask order |
| orderBook.ask[].quantity | Quantity available at this ask price |
| orderBook.ask[].num_orders | Number of orders at this ask price |
| orderBook.last_traded_price | Last traded price |
| orderBook.last_traded_quantity | Last traded quantity |
| orderBook.volume | Total volume traded for the day |

---

Source: docs/rest-api-v3/market-data/historical-market-data.md

<a id="page-market-data-historical-market-data"></a>
<a id="page-market-data-historical-market-data--historical-market-data"></a>
## Historical Market Data

Historical market-data requests can be made for supported `NSE`, `BSE`, and `MCX` instruments.

Historical Data API provides the candle data(Open, High, Low, Close) with timestamps for a given time period, for the given scrips, for a specifed candle duration.

```jsx
Method: POST
Endpoint: charts/timeseries
```
<a id="page-market-data-historical-market-data--curl"></a>
### cURL
```bash
curl --location 'https://uatapi.nubra.io/charts/timeseries' \
--header 'x-device-id: TS123' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJh...6Pno' \
--data '{
   "query":[
      {
         "exchange":"NSE",
         "type":"STOCK",
         "values":[
            "ASIANPAINT"
         ],
         "fields":[
            "open",
            "high",
            "low",
            "close",
            "cumulative_volume"
         ],
         "startDate":"2025-02-12T03:45:00.000Z",
         "endDate":"2025-02-12T09:16:39.358Z",
         "interval":"1m",
         "intraDay":false,
         "realTime":false
      }
   ]
}
    '
```

**Payload**

```jsx
{
   "query":[
      {
         "exchange":"NSE",
         "type":"STOCK",
         "values":[
            "ASIANPAINT"
         ],
         "fields":[
            "open",
            "high",
            "low",
            "close",
            "cumulative_volume"
         ],
         "startDate":"2025-02-12T03:45:00.000Z",
         "endDate":"2025-02-12T09:16:39.358Z",
         "interval":"1m",
         "intraDay":false,
         "realTime":false
      }
   ]
}
```

<a id="page-market-data-historical-market-data--request-parameters"></a>
### Request Parameters

| **Fields** | **Data Type** | **Description** |
| --- | --- | --- |
| exchange | String | Exchange name (e.g., NSE, BSE, MCX) |
| type | String | "STOCK", "INDEX", "OPT", "FUT", or "CHAIN" |
| values | List[str] | One or more instrument symbols e.g. ["ASIANPAINT","NIFTY25JUL25000PE"] |
| fields | List[str]| One or more fields e.g.["open","high","low","close","tick_volume","cumulative_volume","cumulative_volume_premium","cumulative_oi","cumulative_call_oi","cumulative_put_oi","cumulative_fut_oi","l1bid","l1ask","theta","delta","gamma","vega","iv_bid","iv_ask","iv_mid","cumulative_volume_delta"] |
| startDate | str | Start date time format eg. "2025-04-19T11:01:57.000Z" |
| endDate | str | end date time format eg. "2025-04-24T06:13:57.000Z" |
| interval | str | Interval can be "1s", "1m", "2m", "3m", "5m", "15m", "30m", "1h", "1d", "1w", or "1mth" |
| intraDay | bool | If True startDate is current date |
| realTime | bool | To be declared |

Note:
Intervals less than 1 day → data for last 3 months
Intervals 1 day or more → data for up to 10 years (stocks)

**Response** 

```jsx
{
  "market_time": "2025-06-12T07:56:46.12844401Z",
  "message": "charts",
  "result": [
    {
      "exchange": "NSE",
      "type": "STOCK",
      "values": [
        {
          "ASIANPAINT": {
            "close": [
              { "ts": 1749699900000000000, "v": 225010 }
            ],
            "cumulative_volume": [
              { "ts": 1749699900000000000, "v": 1211686 }
            ],
            "open": [
              { "ts": 1749699900000000000, "v": 223900 }
            ]
        }
      ]
}
```

<a id="page-market-data-historical-market-data--response-attributes"></a>
## Response attributes

| **Fields** | **Description** |
| --- | --- |
| market_time | Current market time in ISO format |
| message | Response message type (e.g. "charts") |
| result | List of DataResult objects containing the historical data |
| result[].exchange | Exchange name (e.g. "NSE") |
| result[].type | Security type (e.g. "STOCK", "INDEX") |
| result[].values | List of dictionaries containing data for each symbol |
| result[].values[].{symbol} | SymbolData object containing OHLCV data for specific symbol |
| result[].values[].{symbol}.{field} | List of DataPoint objects for each requested field |
| result[].values[].{symbol}.{field}[].timestamp | Timestamp in nanoseconds |
| result[].values[].{symbol}.{field}[].value | Value for the field at given timestamp |

---

Source: docs/rest-api-v3/market-data/option-chain.md

<a id="page-market-data-option-chain"></a>
<a id="page-market-data-option-chain--option-chain"></a>
## Option Chain

Provides entire Option Chain of any Option Instrument. This includes OI, greeks, volume, top bid/ask and price data of all strikes of a particular underlying scrip.

Option-chain snapshot requests support underlyings from `NSE`, `BSE`, and `MCX` where option-chain data is available.

```jsx
Method: GET
Endpoint: optionchains/{instrument}?exchange=NSE&expiry={expiry}
```

<a id="page-market-data-option-chain--example-curl-requests"></a>
## Example cURL Requests

=== "NSE"

    ```bash
    curl --location --globoff 'https://uatapi.nubra.io/optionchains/NIFTY?exchange=NSE&expiry={expiry}' \
    --header 'x-device-id: TS123' \
    --header 'Authorization: Bearer eyJh...6Pno'
    ```

=== "BSE"

    ```bash
    curl --location --globoff 'https://uatapi.nubra.io/optionchains/SENSEX?exchange=BSE&expiry={expiry}' \
    --header 'x-device-id: TS123' \
    --header 'Authorization: Bearer eyJh...6Pno'
    ```

=== "MCX"

    ```bash
    curl --location --globoff 'https://uatapi.nubra.io/optionchains/CRUDEOIL?exchange=MCX&expiry={expiry}' \
    --header 'x-device-id: TS123' \
    --header 'Authorization: Bearer eyJh...6Pno'
    ```

<a id="page-market-data-option-chain--response-structure"></a>
### Response Structure

```jsx
{
  "chain": {
    "asset": "NIFTY",
    "exchange": "NSE",
    "expiry": "20250626",
    "ce": [
      {
        "ref_id": 3069,
        "inst_id": 62205,
        "ts": 1749715212000000000,
        "sp": 2265000,
        "ls": 75,
        "ltp": 0,
        "ltpchg": null,
        "iv": null,
        "delta": 0.9884471,
        "gamma": 6.654546e-05,
        "theta": -1.111143,
        "vega": 1.4857718,
        "oi": 2700,
        "volume": 0
      }
    ],
    "pe": [
      {
        "ref_id": 3089,
        "inst_id": 62309,
        "ts": 1749715212000000000,
        "sp": 2320000,
        "ls": 75,
        "ltp": 189255,
        "ltpchg": -6.4760823,
        "iv": null,
        "delta": 0.9808698,
        "gamma": 8.9285655e-05,
        "theta": -1.4506115,
        "vega": 2.2921157,
        "oi": 58125,
        "volume": 375
      }
    ],
    "atm": 2495000,
    "cp": 2496260,
    "all_expiries": [
      "20250612",
      "20250619",
      "20250626"
    ]
  },
  "message": "option chains"
}
```

<a id="page-market-data-option-chain--response-attributes"></a>
### Response Attributes

| **Fields** | **Description** |
| --- | --- |
| chain | OptionChain object containing the option chain data |
| chain.asset | Underlying asset symbol |
| chain.expiry | Expiry date of the options |
| chain.ce | List of Option objects for call options |
| chain.pe | List of Option objects for put options |
| chain.at_the_money_strike | At-the-money strike price |
| chain.current_price | Current price of underlying |
| chain.all_expiries | List of available expiry dates |
| chain.[ce/pe][].ref_id | Reference ID of the option |
| chain.[ce/pe][].timestamp | Timestamp in Epoch |
| chain.[ce/pe][].strike_price | Strike price |
| chain.[ce/pe][].lot_size | Lot size |
| chain.[ce/pe][].last_traded_price | Last traded price |
| chain.[ce/pe][].last_traded_price_change | Change in last traded price (percentage) |
| chain.[ce/pe][].iv | Implied volatility |
| chain.[ce/pe][].delta | Option delta |
| chain.[ce/pe][].gamma | Option gamma |
| chain.[ce/pe][].theta | Option theta |
| chain.[ce/pe][].vega | Option vega |
| chain.[ce/pe][].open_interest | Open interest |
| chain.[ce/pe][].volume | Trading volume |
| message | Response message | 

<a id="page-market-data-option-chain--notes"></a>
## Notes

- Use the underlying symbol, not the option trading symbol, when calling this endpoint.
- When deriving the underlying from the instruments master, use the `asset` field.
- Option-chain snapshots support eligible option underlyings from `NSE`, `BSE`, and `MCX`.

---

Source: docs/rest-api-v3/market-data/realtime-data.md

<a id="page-market-data-realtime-data"></a>
<a id="page-market-data-realtime-data--realtime-market-data-websocket"></a>
## Realtime Market Data (WebSocket)

This section documents Nubra's WebSocket streams for real-time market data in the REST API. Use these streams for low-latency updates on indexes, instruments, order books, option chains, and Greeks.

Realtime market-data subscriptions can be built for supported `NSE`, `BSE`, and `MCX` instruments, depending on the stream type and subscription key format.

```jsx
Method: WebSocket
Endpoint: /apibatch/ws
```

<a id="page-market-data-realtime-data--example-websocket-subscribe-messages"></a>
## Example WebSocket Subscribe Messages

WebSocket streams are subscription messages sent after connecting to `/apibatch/ws`. These examples show the NSE, BSE, and MCX variants for the main market-data stream types.

=== "Index Data"

    ```text
    batch_subscribe [token] index {"indexes":["NIFTY","HDFCBANK"]} NSE
    batch_subscribe [token] index {"indexes":["SENSEX"]} BSE
    batch_subscribe [token] index {"indexes":["FUT_CRUDEOIL_20260618"]} MCX
    ```

=== "OHLCV Data"

    ```text
    batch_subscribe [token] index_bucket {"indexes":["NIFTY"]} 5m NSE
    batch_subscribe [token] index_bucket {"indexes":["SENSEX"]} 5m BSE
    batch_subscribe [token] index_bucket {"indexes":["FUT_CRUDEOIL_20260618"]} 5m MCX
    ```

=== "Option Chain Data"

    ```text
    batch_subscribe [token] option [{"exchange":"NSE","asset":"NIFTY","expiry":"{expiry}"}]
    batch_subscribe [token] option [{"exchange":"BSE","asset":"SENSEX","expiry":"{expiry}"}]
    batch_subscribe [token] option [{"exchange":"MCX","asset":"CRUDEOIL","expiry":"{expiry}"}]
    ```

=== "Order Book And Greeks Data"

    ```text
    batch_subscribe [token] orderbook {"instruments":[{nse_ref_id},{bse_ref_id},{mcx_ref_id}]}
    batch_subscribe [token] greeks {"instruments":[{nse_option_ref_id},{bse_option_ref_id},{mcx_option_ref_id}]}
    ```

<a id="page-market-data-realtime-data--websocket-urls"></a>
## WebSocket URLs

| Environment | WebSocket URL |
|---|---|
| UAT | `wss://uatapi.nubra.io/apibatch/ws` |

<a id="page-market-data-realtime-data--available-websocket-streams"></a>
## Available WebSocket Streams

| Stream | Channel | Description |
|---|---|---|
| [Index Data](#1-index-data) | `index` | Live index and instrument ticks including LTP, volume, and percentage change. |
| [Index Bucket (OHLCV)](#2-index-bucket-ohlcv) | `index_bucket` | Time-bucketed OHLCV data for indexes and instruments. |
| [Order Book](#3-order-book) | `orderbook` | Market depth with bid/ask levels, LTP, LTQ, and volume. |
| [Greeks](#4-greeks) | `greeks` | Tick-level option Greeks for option instruments. |
| [Option Chain](#5-option-chain) | `option` | Full option chain updates by asset and expiry. |

---

<a id="page-market-data-realtime-data--websocket-stream-controls"></a>
## WebSocket Stream Controls

These commands modify stream behavior across channels.

| Feature | Command | Scope | Description |
|---|---|---|---|
| [Stream Interval](#stream-interval-control) | `socket_interval` | Per channel | Controls the update frequency of WebSocket streams. |
| [Post Market Data](#post-market-data) | `post_market` | Connection-level | Enables static post-market data for testing and validation after market hours. |
| [Order Book Depth](#order-book-depth-selective-levels) | `orderbook_depth` | Per connection | Controls the number of order-book levels streamed. |

---

<a id="page-market-data-realtime-data--message-envelope-genericdata"></a>
## Message Envelope (GenericData)

All WebSocket payloads are wrapped in a common envelope.

```proto
message GenericData {
  string key = 1;
  google.protobuf.Any data = 2;
}
```

- `key` identifies the message type.
- `data` contains one of the stream payloads defined below.

---

<a id="page-market-data-realtime-data--1-index-data"></a>
## 1. Index Data

**Channel:** `index`

<a id="page-market-data-realtime-data--subscribe-unsubscribe"></a>
### Subscribe / Unsubscribe

```
SUBSCRIBE:   batch_subscribe [token] index {"indexes":["BANKNIFTY","TCS","RELIANCE"]} NSE
UNSUBSCRIBE: batch_unsubscribe [token] index {"indexes":["BANKNIFTY","TCS","RELIANCE"]} NSE
```

Notes:
- `exchange` is sent at the message level, for example `NSE`, `BSE`, or `MCX`.
- Both index symbols and instrument symbols are sent in the `indexes` array.
- The response separates them into `indexes` and `instruments`.
- The JSON object must not contain spaces.

<a id="page-market-data-realtime-data--payload-proto"></a>
### Payload (Proto)

```proto
message BatchWebSocketIndexMessage {
  int64 timestamp = 1;
  repeated WebSocketMsgIndex indexes = 2;
  repeated WebSocketMsgIndex instruments = 3;
}

message WebSocketMsgIndex {
  string indexname = 1;
  int64 timestamp = 2;
  int64 index_value = 3;
  int64 high_index_value = 4;
  int64 low_index_value = 5;
  int64 volume = 6;
  float changepercent = 7;
  int64 tick_volume = 8;
  int64 prev_close = 9;
  string exchange = 10;
  int64 volume_oi = 11;
}
```

---

<a id="page-market-data-realtime-data--2-index-bucket-ohlcv"></a>
## 2. Index Bucket (OHLCV)

**Channel:** `index_bucket`

<a id="page-market-data-realtime-data--subscribe-unsubscribe"></a>
### Subscribe / Unsubscribe

```
SUBSCRIBE:   batch_subscribe [token] index_bucket {"indexes":["BANKNIFTY","TCS","RELIANCE"]} 2m NSE
UNSUBSCRIBE: batch_unsubscribe [token] index_bucket {"indexes":["BANKNIFTY","TCS","RELIANCE"]} 2m NSE
```

Notes:
- `interval` and `exchange` are sent at the message level.
- Both index symbols and instrument symbols are sent in the `indexes` array.
- The response separates them into `indexes` and `instruments`.
- The JSON object must not contain spaces.
- Interval values are returned in the payload as an `Interval` enum.

<a id="page-market-data-realtime-data--supported-intervals"></a>
### Supported Intervals

The server accepts the following interval strings in the subscribe command:

- `1s`, `5s`, `10s`, `30s`
- `1m`, `2m`, `3m`, `5m`, `10m`, `15m`, `30m`
- `1h`, `2h`, `4h`
- `1d`
- `1w`
- `1mt`
- `1yr`

> **Important:** Although the `Interval` enum includes values from `INTERVAL_INVALID = 0` through `INTERVAL_1_YEAR = 16`, the following enum values are currently not available for `index_bucket`:
- `INTERVAL_INVALID = 0`
- `INTERVAL_1_SECOND = 1`
- `INTERVAL_10_SECOND = 2`
- `INTERVAL_1_YEAR = 16`

<a id="page-market-data-realtime-data--payload-proto"></a>
### Payload (Proto)

```proto
message BatchWebSocketIndexBucketMessage {
  int64 timestamp = 1;
  repeated WebSocketMsgIndexBucket indexes = 2;
  repeated WebSocketMsgIndexBucket instruments = 3;
}

message WebSocketMsgIndexBucket {
  string indexname = 1;
  string exchange = 2;
  Interval interval = 3;
  int64 timestamp = 4;
  int64 open = 5;
  int64 high = 6;
  int64 low = 7;
  int64 close = 8;
  int64 bucket_volume = 9;
  int64 tick_volume = 10;
  int64 cumulative_volume = 11;
  int64 bucket_timestamp = 12;
}
```

<a id="page-market-data-realtime-data--interval-enum-proto"></a>
### Interval Enum (Proto)

```proto
enum Interval {
  INTERVAL_INVALID = 0;
  INTERVAL_1_SECOND = 1;
  INTERVAL_10_SECOND = 2;
  INTERVAL_1_MINUTE = 3;
  INTERVAL_2_MINUTE = 4;
  INTERVAL_3_MINUTE = 5;
  INTERVAL_5_MINUTE = 6;
  INTERVAL_10_MINUTE = 7;
  INTERVAL_15_MINUTE = 8;
  INTERVAL_30_MINUTE = 9;
  INTERVAL_1_HOUR = 10;
  INTERVAL_2_HOUR = 11;
  INTERVAL_4_HOUR = 12;
  INTERVAL_1_DAY = 13;
  INTERVAL_1_WEEK = 14;
  INTERVAL_1_MONTH = 15;
  INTERVAL_1_YEAR = 16;
  INTERVAL_5_SECOND = 17;
}
```

<a id="page-market-data-realtime-data--interval-mapping-subscribe-string-enum"></a>
### Interval Mapping (Subscribe String -> Enum)

Use these mappings to interpret `WebSocketMsgIndexBucket.interval`:

- `1m` -> `INTERVAL_1_MINUTE (3)`
- `2m` -> `INTERVAL_2_MINUTE (4)`
- `3m` -> `INTERVAL_3_MINUTE (5)`
- `5m` -> `INTERVAL_5_MINUTE (6)`
- `10m` -> `INTERVAL_10_MINUTE (7)`
- `15m` -> `INTERVAL_15_MINUTE (8)`
- `30m` -> `INTERVAL_30_MINUTE (9)`
- `1h` -> `INTERVAL_1_HOUR (10)`
- `2h` -> `INTERVAL_2_HOUR (11)`
- `4h` -> `INTERVAL_4_HOUR (12)`
- `1d` -> `INTERVAL_1_DAY (13)`
- `1w` -> `INTERVAL_1_WEEK (14)`
- `1mt` -> `INTERVAL_1_MONTH (15)`
- `5s` -> `INTERVAL_5_SECOND (17)`

> Note: Even if the subscribe command allows `1s`, `5s`, `10s`, `30s`, the payload enum set shown above does not include `30s` values.

---

<a id="page-market-data-realtime-data--3-order-book"></a>
## 3. Order Book

**Channel:** `orderbook`

Provides real-time market depth, LTP, LTQ, and traded volume for subscribed instruments.

<a id="page-market-data-realtime-data--subscribe-unsubscribe"></a>
### Subscribe / Unsubscribe

```
SUBSCRIBE:   batch_subscribe [token] orderbook {"instruments":[1120031,73009]}
UNSUBSCRIBE: batch_unsubscribe [token] orderbook {"instruments":[1120031,73009]}
```

By default, the order book stream sends up to 20 bid and ask levels per instrument.

<a id="page-market-data-realtime-data--order-book-depth-selective-levels"></a>
### Order Book Depth (Selective Levels)

Users can subscribe to a specific depth level from `1` to `20` instead of receiving all 20 levels.

```
MESSAGE: batch_subscribe [token] orderbook_depth 4
```

Notes:
- This setting applies to the `orderbook` channel.
- `orderbook_depth 4` streams the top 4 bid and ask levels only.
- If not specified, the default depth is `20`.

<a id="page-market-data-realtime-data--payload-proto"></a>
### Payload (Proto)

```proto
message BatchWebSocketOrderbookMessage {
  int64 timestamp = 1;
  repeated WebSocketMsgOrderBook instruments = 2;
}

message WebSocketMsgOrderBook {
  uint32 inst_id = 1;
  int64 timestamp = 2;
  repeated OrderBookLevel bids = 3;
  repeated OrderBookLevel asks = 4;
  int64 ltp = 5;
  int64 ltq = 6;
  int64 volume = 7;
  int64 ref_id = 8;
}

message OrderBookLevel {
  int64 price = 1;
  int64 quantity = 2;
  int64 orders = 3;
}
```

<a id="page-market-data-realtime-data--notes"></a>
### Notes

- The number of `bids` and `asks` entries depends on the subscribed order-book depth.
- `bids[0]` and `asks[0]` represent the best bid and best ask respectively.

---

<a id="page-market-data-realtime-data--4-greeks"></a>
## 4. Greeks

**Channel:** `greeks`

<a id="page-market-data-realtime-data--subscribe-unsubscribe"></a>
### Subscribe / Unsubscribe

```
SUBSCRIBE:   batch_subscribe [token] greeks {"instruments":[1120031,1120032]}
UNSUBSCRIBE: batch_unsubscribe [token] greeks {"instruments":[1120031,1120032]}
```

<a id="page-market-data-realtime-data--payload-proto"></a>
### Payload (Proto)

```proto
message BatchWebSocketGreeksMessage {
  int64 timestamp = 1;
  repeated WebSocketMsgOptionChainItem instruments = 2;
}

message WebSocketMsgOptionChainItem {
  int64 inst_id = 1;
  int64 ts = 2;
  int64 sp = 3;
  int32 ls = 4;
  int64 ltp = 5;
  float ltpchg = 6;
  float iv = 7;
  float delta = 8;
  float gamma = 9;
  float theta = 10;
  float vega = 11;
  int64 oi = 12;
  int64 volume = 13;
  int64 ref_id = 14;
  int64 prev_oi = 15;
  int64 price_pcp = 16;
}
```

---

<a id="page-market-data-realtime-data--5-option-chain"></a>
## 5. Option Chain

**Channel:** `option`

<a id="page-market-data-realtime-data--subscribe-unsubscribe"></a>
### Subscribe / Unsubscribe

```
SUBSCRIBE:   batch_subscribe [token] option [{"exchange":"NSE","asset":"RELIANCE","expiry":"20260224"},{"exchange":"BSE","asset":"SENSEX","expiry":"20260205"},{"exchange":"NSE","asset":"NIFTY","expiry":"20260203"}]
UNSUBSCRIBE: batch_unsubscribe [token] option [{"exchange":"NSE","asset":"RELIANCE","expiry":"20260224"},{"exchange":"BSE","asset":"SENSEX","expiry":"20260205"},{"exchange":"NSE","asset":"NIFTY","expiry":"20260203"}]
```

Notes:
- The JSON array must not contain spaces.
- Option chain updates are received in the older format: one packet per subscribed chain (not batched together).
- When deriving the underlying from the instruments master, use the `asset` field and pair it with the chosen `expiry`.

<a id="page-market-data-realtime-data--payload-proto"></a>
### Payload (Proto)

```proto
message WebSocketMsgOptionChainUpdate {
  string asset = 1;
  string expiry = 2;
  repeated WebSocketMsgOptionChainItem ce = 3;
  repeated WebSocketMsgOptionChainItem pe = 4;
  int64 atm = 5;
  int64 currentprice = 6;
  string exchange = 7;
}
```

---

<a id="page-market-data-realtime-data--stream-interval-control"></a>
## Stream Interval Control

Users can control the update frequency of WebSocket streams by subscribing to a stream interval.

<a id="page-market-data-realtime-data--set-stream-interval"></a>
### Set Stream Interval

```
MESSAGE: batch_subscribe [token] socket_interval option 1m
```

Notes:
- The stream interval applies to the specified channel, for example `option`, `index`, `orderbook`, `greeks`, or `index_bucket`.
- Interval settings are connection-level and affect subsequent subscriptions on that channel unless changed.
- If no interval is specified, the default behavior is tick-level streaming.

<a id="page-market-data-realtime-data--supported-stream-intervals"></a>
### Supported Stream Intervals

The following interval strings are supported:

- `1s`
- `5s`
- `10s`
- `30s`
- `1m`
- `5m`
- `10m`

<a id="page-market-data-realtime-data--subscription-limits-by-interval"></a>
### Subscription Limits by Interval

<a id="page-market-data-realtime-data--second-based-intervals-limited"></a>
#### Second-Based Intervals (Limited)

The following intervals have standard subscription limits:

- `1s`
- `5s`
- `10s`
- `30s`

Notes:
- These intervals are subject to per-connection and per-channel subscription limits.
- Recommended for latency-sensitive strategies requiring near real-time updates.

<a id="page-market-data-realtime-data--minute-based-intervals-unlimited"></a>
#### Minute-Based Intervals (Unlimited)

The following intervals currently have no subscription limits:

- `1m`
- `5m`
- `10m`

Notes:
- You can subscribe to any number of instruments when using these intervals.
- Ideal for strategies focused on candle-based logic, scans, or lower-frequency signals.
- Significantly reduces bandwidth and processing overhead compared to second-level streams.

<a id="page-market-data-realtime-data--example"></a>
### Example

Subscribe to the option chain stream with 1-minute updates:

```
MESSAGE: batch_subscribe [token] socket_interval option 1m
MESSAGE: batch_subscribe [token] option [{"exchange":"NSE","asset":"NIFTY","expiry":"20260203"}]
```

<a id="page-market-data-realtime-data--best-practices"></a>
### Best Practices

- Use second-based intervals only when necessary for execution or market-making strategies.
- Prefer minute-based intervals for monitoring, analytics, and signal generation.
- Combine `socket_interval` with features like order book depth control to further optimize performance.

---

<a id="page-market-data-realtime-data--post-market-data"></a>
## Post Market Data

Post-market data is available for testing and validation. This data represents an end-of-day static market snapshot and does not stream live updates.

<a id="page-market-data-realtime-data--enable-post-market-mode"></a>
### Enable Post Market Mode

```
MESSAGE: batch_subscribe [token] post_market true
```

Notes:
- When enabled, WebSocket streams return static post-market data instead of live ticks.
- Data remains unchanged for the duration of the session.
- This mode is intended for strategy testing, validation, and integration development.
- Post-market data is available only after the market has closed.

<a id="page-market-data-realtime-data--key-characteristics"></a>
### Key Characteristics

- Static data with no live updates
- Same payload structures as live streams
- Useful for non-market-hour testing and demos

<a id="page-market-data-realtime-data--example-workflow"></a>
### Example Workflow

Enable post-market mode and subscribe to an index stream:

```
MESSAGE: batch_subscribe [token] post_market true
MESSAGE: batch_subscribe [token] index {"indexes":["NIFTY","BANKNIFTY"]} NSE
```

<a id="page-market-data-realtime-data--notes"></a>
### Notes

- Post-market mode applies at the connection level.
- To resume live data, reconnect without enabling `post_market`.

---

Source: docs/rest-api-v3/trading/orders/orders.md

<a id="page-trading-orders-orders"></a>
<a id="page-trading-orders-orders--orders"></a>
## Orders

<section class="version-hero">
  <div class="version-hero__eyebrow">
    Trading API V3
    <span class="nav-new-badge">New</span>
  </div>
  <p>This is the REST V3 trading track for the upgraded UAT rollout.</p>
  <p>Use these pages when validating the newer V3 intent-order payload structure in the upgraded UAT environment.</p>
</section>

Use these pages for Trading API V3 REST order workflows. Trading API V3 uses intent orders for single orders, grouped multi-order requests, and strategy orders.

Authenticated REST requests in this V3 track should include `Authorization`, `x-device-id`, `x-app-version`, `x-device-os: sdk`, and `Cookie: deviceId=<device_id>`.

This section is intentionally aligned to the Python SDK V3 trading flow, but each page uses REST request and response payloads instead of SDK code. Use it when you want to validate or integrate the raw Trading API V3 request shape directly.

<a id="page-trading-orders-orders--basic-usage"></a>
## Basic Usage

Use this section as the entry point when deciding which Trading API V3 REST workflow page to follow.

<a id="page-trading-orders-orders--main-endpoints"></a>
## Main Endpoints

| Workflow | Endpoint |
| --- | --- |
| Place single order | `POST sentinel/orders/create` |
| Place multi order | `POST sentinel/orders/create` |
| Place strategy order | `POST sentinel/orders/create` |
| Modify order | `POST sentinel/orders/modify` |
| Modify multi order | `POST sentinel/orders/modify` |
| Cancel order | `POST sentinel/orders/cancel` |
| Get orders | `GET sentinel/orders` |
| Get order margin | `POST sentinel/orders/funds_required` |

<a id="page-trading-orders-orders--page-map"></a>
## Page Map

- [Place Single Order](#page-trading-orders-place-order)
- [Place Multi Order](#page-trading-orders-place-basket-order)
- [Place Strategy Order](#page-trading-orders-place-flexi-order)
- [Modify Order](#page-trading-orders-modify-order)
- [Modify Multi Order](#page-trading-orders-modify-multi-order)
- [Cancel Order](#page-trading-orders-cancel-order)
- [Get Orders](#page-trading-orders-get-order)
- [Get Order Margin](#page-trading-orders-get-margin)
- [Realtime Order Updates](#page-trading-realtime-order-updates)

<a id="page-trading-orders-orders--order-id-model"></a>
## Order ID Model

Trading API V3 uses `intentOrderId` as the order identifier for create responses, get-order retrieval, modify flows, cancel flows, and realtime updates.

For strategy orders:

- one strategy returns one strategy-level `intentOrderId`
- the same strategy response can also include `legs[]`
- modify and cancel flows still use the strategy-level `intentOrderId`

<a id="page-trading-orders-orders--trading-api-v3-field-groups"></a>
## Trading API V3 Field Groups

| Group | Common fields |
| --- | --- |
| Single order fields | `refId`, `qty`, `side`, `deliveryType`, `priceType`, `validityType`, `entryPrice` |
| Entry control fields | `entryConfig`, `entryConfig.triggers`, `entryConfig.entryTime` |
| Exit control fields | `exitConfig`, `stoplossParams`, `targetParams`, `exitTime` |
| Strategy fields | `isMultiLeg`, `legs`, `legs[].refId`, `legs[].unitQty` |
| Tracking fields | `stratTags`, `intentOrderId`, `timestamps`, `status` |

<a id="page-trading-orders-orders--major-areas-to-review"></a>
## Major Areas To Review

- [Place Single Order](#page-trading-orders-place-order): single-instrument payload families such as market, limit, AMO, trigger, iceberg, timed, and GTE
- [Place Multi Order](#page-trading-orders-place-basket-order): several independent single-order payloads in one request
- [Place Strategy Order](#page-trading-orders-place-flexi-order): one multi-leg strategy payload with shared top-level quantity and per-leg multipliers
- [Modify Order](#page-trading-orders-modify-order): single-order and strategy-order modify payloads using the V3 `orders[]` wrapper
- [Get Order Margin](#page-trading-orders-get-margin): pre-placement funds and charges using the same payload shape as placement

<a id="page-trading-orders-orders--trading-api-v3-enum-values"></a>
## Trading API V3 Enum Values

| Field | Typical values |
| --- | --- |
| `side` | `BUY`, `SELL` |
| `deliveryType` | `IDAY`, `CNC` |
| `priceType` | `LIMIT`, `MARKET` |
| `validityType` | `DAY`, `IOC`, `GTE` |
| `executionMode` | `ENTRY`, `ENTRY_AND_EXIT`, `EXIT` |

<a id="page-trading-orders-orders--important-rules"></a>
## Important Rules

!!! important-rules "Important Rules"
    - Trading API V3 order placement uses camel-case field names such as `refId`, `deliveryType`, `entryPrice`, and `isMultiLeg`.
    - Use `isMultiLeg: false` for single-instrument order items.
    - Use `isMultiLeg: true` with `legs[]` for one strategy order.
    - Multi-order placement groups independent single-order items; it does not create one leg-based strategy.
    - Strategy orders return one strategy-level `intentOrderId`.
    - Modify and cancel workflows use the same `intentOrderId` model for single orders, multi-order items, and strategy orders.
    - Review [Rate Limits & API Usage](#page-ratelimits) before automating order placement.

<a id="page-trading-orders-orders--what-to-read-next"></a>
## What To Read Next

- [Place Single Order](#page-trading-orders-place-order)
- [Place Multi Order](#page-trading-orders-place-basket-order)
- [Place Strategy Order](#page-trading-orders-place-flexi-order)
- [Modify Order](#page-trading-orders-modify-order)
- [Get Order Margin](#page-trading-orders-get-margin)

---

Source: docs/rest-api-v3/trading/orders/place-order.md

<a id="page-trading-orders-place-order"></a>
<a id="page-trading-orders-place-order--place-single-order"></a>
## Place Single Order

Use this page for one Trading API V3 single-instrument order through the REST API.

Trading API V3 uses the intent-order payload model. Even for one order, the request body is still sent inside an `orders` array with exactly one item.

Nubra Trading API V3 supports the same main single-order families documented in the Python SDK V3 track. In REST, the same workflows are expressed directly through the payload shape, including market, limit, AMO-style, trigger, iceberg, timed, and good-till patterns.

!!! note "Scope"
    Use this page only for one independent single-instrument order.

    A single order:

    - sets `refId`
    - sets `qty`
    - sets `side`
    - sets `deliveryType`
    - sets `isMultiLeg: false`
    - does not send `legs`

    For several independent orders in one request, use [Place Multi Order](#page-trading-orders-place-basket-order). For one strategy order made from legs, use [Place Strategy Order](#page-trading-orders-place-flexi-order).

<a id="page-trading-orders-place-order--endpoint"></a>
## Endpoint

```text
Method: POST
Endpoint: sentinel/orders/create
```

<a id="page-trading-orders-place-order--required-headers"></a>
## Required Headers

```text
Authorization: Bearer <session_token>
x-device-id: <device_id>
x-app-version: 0.4.5
x-device-os: sdk
Cookie: deviceId=<device_id>
Content-Type: application/json
```

All examples on this page assume the request is being sent to the UAT V3 REST flow with the headers above. Keep field names in camel case exactly as shown, such as `refId`, `deliveryType`, `validityType`, `entryPrice`, and `isMultiLeg`.

<a id="page-trading-orders-place-order--basic-usage"></a>
## Basic Usage

```bash
curl --location 'https://uatapi.nubra.io/sentinel/orders/create' \
--header 'Authorization: Bearer {{session_token}}' \
--header 'x-device-id: {{x_device_id}}' \
--header 'x-app-version: 0.4.5' \
--header 'x-device-os: sdk' \
--header 'Cookie: deviceId={{x_device_id}}' \
--header 'Content-Type: application/json' \
--data '{
  "orders": [
    {
      "refId": 72329,
      "qty": 1,
      "side": "BUY",
      "deliveryType": "IDAY",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "isMultiLeg": false,
      "executionMode": "ENTRY",
      "entryPrice": 127000,
      "stratTags": ["rest-api-v3", "basic-usage"]
    }
  ]
}'
```

Successful create requests return HTTP `201 Created` on this REST V3 flow.

<a id="page-trading-orders-place-order--example-order-patterns"></a>
## Example Order Patterns

- market order
- limit order
- AMO order
- trigger or stoploss order (price based entry or exit)
- iceberg order
- good-till order
- timed entry or exit order (time based entry or exit)

Use the tabs below as the main single-order families. The detailed sections later on this page expand the same payload families further.

=== "Market Order"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "MARKET",
          "validityType": "IOC",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "stratTags": ["rest-api-v3", "single-market"]
        }
      ]
    }
    ```

    Use this pattern when the order should execute as a market order. In the current REST flow, `MARKET` orders should use `validityType: "IOC"` and should not send `entryPrice`.

=== "Limit Order"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000,
          "stratTags": ["rest-api-v3", "single-limit"]
        }
      ]
    }
    ```

    Use this pattern for a standard single-instrument limit order.

=== "AMO Order"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000,
          "stratTags": ["rest-api-v3", "amo-limit"]
        }
      ]
    }
    ```

    Use this pattern for a standard limit order placed after market hours. Trading API V3 does not require a separate AMO payload field.

=== "Trigger / Stoploss"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY_AND_EXIT",
          "entryPrice": 127000,
          "entryConfig": {
            "triggers": {
              "ltp": {
                "atOrAbove": { "value": 127000 }
              }
            }
          },
          "exitConfig": {
            "stoplossParams": {
              "stoplossTriggerPrice": { "value": 126500 },
              "stoplossLimitPrice": { "value": 126400 }
            }
          },
          "stratTags": ["rest-api-v3", "trigger-stoploss"]
        }
      ]
    }
    ```

    Use this family when the entry is trigger-based, when the order carries a stoploss exit, or when both are required.

=== "Iceberg Order"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1000,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000,
          "icebergInfo": {
            "maxQtyPerLeg": 100
          },
          "stratTags": ["rest-api-v3", "iceberg"]
        }
      ]
    }
    ```

    Use this family when the order quantity should be sliced using `icebergInfo`.

=== "GTE Order"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "CNC",
          "priceType": "LIMIT",
          "validityType": "GTE",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "goodTillDate": "2026-10-31T15:10:00Z",
          "entryPrice": 127000,
          "stratTags": ["rest-api-v3", "gte"]
        }
      ]
    }
    ```

    Use this pattern for future-dated good-till orders. For this validated flow, future-dated `GTE` should be paired with `deliveryType: "CNC"`.

=== "Timed Entry / Exit"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000,
          "entryConfig": {
            "entryTime": "2026-06-17T09:20:00Z"
          },
          "exitConfig": {
            "exitTime": "2026-06-17T09:25:00Z"
          },
          "stratTags": ["rest-api-v3", "timed-entry-exit"]
        }
      ]
    }
    ```

    Use this family when the order should become active at a scheduled time, exit at a scheduled time, or both.
    Replace the sample `entryTime` and `exitTime` values before running the payload. They are illustrative placeholders and should be updated to valid times for your current trading session.

<a id="page-trading-orders-place-order--iceberg-orders"></a>
## Iceberg Orders

Use `icebergInfo` when a larger order should be split into smaller visible slices. Choose either `maxQtyPerLeg` or `numberOfLegs`; do not send both in the same order.

=== "Max Qty Per Leg"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1000,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000,
          "icebergInfo": {
            "maxQtyPerLeg": 100
          }
        }
      ]
    }
    ```

    Use this pattern when you want each visible iceberg slice to be capped at a fixed quantity.

=== "Number Of Legs"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1000,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000,
          "icebergInfo": {
            "numberOfLegs": 10
          }
        }
      ]
    }
    ```

    Use this pattern when you want Trading API V3 to split the total quantity across a fixed number of iceberg slices.

<a id="page-trading-orders-place-order--trigger-order-patterns"></a>
## Trigger Order Patterns

- trailing stop-loss exit
- trigger entry above the current price
- trigger entry below the current price
- trigger entry with stop-loss exit
- target-only exit
- stop-loss and target exit

=== "Trailing Stoploss"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY_AND_EXIT",
          "entryPrice": 127000,
          "exitConfig": {
            "stoplossParams": {
              "stoplossTriggerPrice": { "value": 126500 },
              "stoplossLimitPrice": { "value": 126400 },
              "stoplossTrailJump": 5
            }
          }
        }
      ]
    }
    ```

=== "Trigger Above"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000,
          "entryConfig": {
            "triggers": {
              "ltp": {
                "atOrAbove": { "value": 127000 }
              }
            }
          }
        }
      ]
    }
    ```

=== "Trigger Below"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000,
          "entryConfig": {
            "triggers": {
              "ltp": {
                "atOrBelow": { "value": 126900 }
              }
            }
          }
        }
      ]
    }
    ```

=== "Trigger With Stoploss"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY_AND_EXIT",
          "entryPrice": 127000,
          "entryConfig": {
            "triggers": {
              "ltp": {
                "atOrAbove": { "value": 127000 }
              }
            }
          },
          "exitConfig": {
            "stoplossParams": {
              "stoplossTriggerPrice": { "value": 126500 },
              "stoplossLimitPrice": { "value": 126400 }
            }
          }
        }
      ]
    }
    ```

=== "Target Only"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY_AND_EXIT",
          "entryPrice": 127000,
          "exitConfig": {
            "targetParams": {
              "targetProfitTriggerPrice": { "value": 127500 },
              "targetProfitLimitPrice": { "value": 127400 }
            }
          }
        }
      ]
    }
    ```

=== "Stoploss + Target"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY_AND_EXIT",
          "entryPrice": 127000,
          "exitConfig": {
            "stoplossParams": {
              "stoplossTriggerPrice": { "value": 126500 },
              "stoplossLimitPrice": { "value": 126400 }
            },
            "targetParams": {
              "targetProfitTriggerPrice": { "value": 127500 },
              "targetProfitLimitPrice": { "value": 127400 }
            }
          }
        }
      ]
    }
    ```

<a id="page-trading-orders-place-order--timed-entry-exit-patterns"></a>
## Timed Entry / Exit Patterns

- timed entry
- timed exit
- timed entry with timed exit

=== "Timed Entry"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000,
          "entryConfig": {
            "entryTime": "2026-06-17T09:20:00Z"
          }
        }
      ]
    }
    ```

=== "Timed Exit"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY_AND_EXIT",
          "entryPrice": 127000,
          "exitConfig": {
            "exitTime": "2026-06-17T09:25:00Z"
          }
        }
      ]
    }
    ```

=== "Timed Entry + Exit"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000,
          "entryConfig": {
            "entryTime": "2026-06-17T09:20:00Z"
          },
          "exitConfig": {
            "exitTime": "2026-06-17T09:25:00Z"
          }
        }
      ]
    }
    ```

<a id="page-trading-orders-place-order--gte-patterns"></a>
## GTE Patterns

Use `validityType: "GTE"` for good-till orders.

- good-till limit order
- good-till order with price-based entry trigger

=== "GTE Limit"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "CNC",
          "priceType": "LIMIT",
          "validityType": "GTE",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "goodTillDate": "2026-10-31T15:10:00Z",
          "entryPrice": 127000
        }
      ]
    }
    ```

=== "GTE With Trigger"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "CNC",
          "priceType": "LIMIT",
          "validityType": "GTE",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "goodTillDate": "2026-10-31T15:10:00Z",
          "entryPrice": 127000,
          "entryConfig": {
            "triggers": {
              "ltp": {
                "atOrAbove": { "value": 127000 }
              }
            }
          }
        }
      ]
    }
    ```

<a id="page-trading-orders-place-order--execution-modes"></a>
## Execution Modes

| Value | Use |
| --- | --- |
| `ENTRY` | Entry-only order without managed exit controls |
| `ENTRY_AND_EXIT` | Entry order with target, stop-loss, trailing stop-loss, timed exit, or a combination of these |
| `EXIT` | Exit-only modification or exit-only workflow where the order is meant to manage the exit leg or exit controls |

<a id="page-trading-orders-place-order--single-order-fields"></a>
## Single Order Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `orders` | array | Yes | Wrapper array. For this page, send exactly one order item |
| `orders[].refId` | int | Yes | Instrument reference id |
| `orders[].qty` | int | Yes | Order quantity |
| `orders[].side` | enum | Yes | `BUY` or `SELL` |
| `orders[].deliveryType` | enum | Yes | `IDAY` or `CNC` |
| `orders[].priceType` | enum | Yes | `LIMIT` or `MARKET` |
| `orders[].validityType` | enum | Yes | `DAY`, `IOC`, or `GTE` depending on the order family |
| `orders[].isMultiLeg` | boolean | Yes | Must be `false` for independent single orders |
| `orders[].executionMode` | enum | Yes | `ENTRY` or `ENTRY_AND_EXIT` depending on the payload |
| `orders[].entryPrice` | int | Conditional | Required for `LIMIT` orders. Omit for `MARKET` orders |
| `orders[].goodTillDate` | string | Conditional | Required for `GTE` orders |
| `orders[].entryConfig` | object | Conditional | Entry trigger or entry-time configuration |
| `orders[].exitConfig` | object | Conditional | Stoploss, target, exit-time, or other exit controls |
| `orders[].icebergInfo` | object | Conditional | Iceberg slicing configuration |
| `orders[].stratTags` | array | Optional | Client-defined tags for grouping and traceability |

<a id="page-trading-orders-place-order--order-condition-fields"></a>
## Order Condition Fields

| Field | Type | Description |
| --- | --- | --- |
| `entryConfig.triggers.ltp.atOrAbove.value` | int | Entry trigger above a price |
| `entryConfig.triggers.ltp.atOrBelow.value` | int | Entry trigger below a price |
| `entryConfig.entryTime` | string | Scheduled entry time in ISO format |
| `exitConfig.exitTime` | string | Scheduled exit time in ISO format |
| `exitConfig.stoplossParams.stoplossTriggerPrice.value` | int | Stop-loss trigger price |
| `exitConfig.stoplossParams.stoplossLimitPrice.value` | int | Stop-loss limit price |
| `exitConfig.stoplossParams.stoplossTrailJump` | int | Trailing stop-loss jump |
| `exitConfig.targetParams.targetProfitTriggerPrice.value` | int | Target trigger price |
| `exitConfig.targetParams.targetProfitLimitPrice.value` | int | Target limit price |

<a id="page-trading-orders-place-order--response-behaviour-notes"></a>
## Response Behaviour Notes

- successful create requests return HTTP `201 Created`
- good-till orders are returned under the `gtt` bucket in `GET sentinel/orders`
- the returned order object may normalize `executionMode`
- `goodTillDate` may need to be confirmed through `GET sentinel/orders` instead of relying only on the create-response echo
- `icebergInfo` may not be echoed back identically for every iceberg variant
- for target exits, keep `targetProfitTriggerPrice` greater than or equal to `targetProfitLimitPrice`

<a id="page-trading-orders-place-order--order-response-fields"></a>
## Order Response Fields

| Field | Meaning |
| --- | --- |
| `intentOrderId` | Trading API V3 order id used for modify, cancel, and tracking |
| `status` | Current order state such as `OPEN`, `CANCELLED`, or `GTE` |
| `intentOrderType` | Normalized response family such as `REGULAR`, `TRIGGER`, or `FLEXI` |
| `orderQty` | Final order quantity accepted for the item |
| `orderPrice` | Final normalized entry price |
| `ltp` | Market price snapshot attached to the response |
| `refData` | Instrument metadata returned alongside the order |
| `timestamps` | Lifecycle timestamps such as create and send-to-exchange times |

<a id="page-trading-orders-place-order--response-shape"></a>
## Response Shape

```json
{
  "message": "order creation request pushed successfully",
  "orders": [
    {
      "intentOrderId": 9946,
      "exchange": "NSE",
      "status": "OPEN",
      "isMulti": false,
      "legs": null,
      "refId": 72329,
      "refData": {
        "refId": 72329,
        "exchange": "NSE",
        "asset": "ICICIBANK",
        "stockName": "ICICIBANK",
        "displayName": "ICICIBANK",
        "lotSize": 1,
        "tickSize": 10
      },
      "filledQty": 0,
      "orderQty": 1,
      "deliveryType": "IDAY",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "executionMode": "ENTRY",
      "stratTags": ["rest-api-v3", "basic-usage"],
      "ltp": 133360,
      "orderPrice": 127000,
      "timestamps": {
        "intentCreatedAt": "2026-06-15T08:27:31.191134998Z",
        "sentToColoAt": "2026-06-15T08:27:31.19804133Z"
      },
      "intentOrderType": "REGULAR",
      "side": "BUY"
    }
  ]
}
```

<a id="page-trading-orders-place-order--important-rules"></a>
## Important Rules

- `MARKET` orders were accepted in validation when `entryPrice` was omitted and `validityType` was set to `IOC`.
- Future-dated `GTE` orders should use `deliveryType: "CNC"`. An intraday `GTE` order was rejected with the message: `Intraday orders cannot have an expiry beyond today. Use Delivery (CNC) instead.`
- Trigger-based and timed payloads are normalized in the response model. For example, a trigger plus stoploss request may come back with `intentOrderType: "TRIGGER"` and a normalized `exitConfig` array.
- Use hyphenated or plain tags in `stratTags`. Avoid underscores in tag names such as `abc_def`; prefer names such as `abc-def`.

<a id="page-trading-orders-place-order--what-to-read-next"></a>
## What To Read Next

- [Place Multi Order](#page-trading-orders-place-basket-order)
- [Place Strategy Order](#page-trading-orders-place-flexi-order)
- [Modify Order](#page-trading-orders-modify-order)
- [Get Orders](#page-trading-orders-get-order)

---

Source: docs/rest-api-v3/trading/orders/place-basket-order.md

<a id="page-trading-orders-place-basket-order"></a>
<a id="page-trading-orders-place-basket-order--place-multi-order"></a>
## Place Multi Order

Use this page to submit multiple independent Trading API V3 single-instrument orders in one REST request.

Each object inside `orders[]` is a full single-order payload. Multi-order create uses the same endpoint as single-order create; the difference is only that the `orders` array contains more than one independent item.

This page is the REST V3 equivalent of placing several single-order payloads together. It is not the strategy-order flow. If one order object needs `legs`, use [Place Strategy Order](#page-trading-orders-place-flexi-order) instead.

!!! note "Scope"
    Use this page for several independent order items.

    Every item:

    - has its own `refId`
    - has its own `qty`
    - has its own `side`
    - keeps `isMultiLeg: false`
    - does not send `legs`

    Do not use this page for one strategy made from FNO legs. For one leg-based strategy order, use [Place Strategy Order](#page-trading-orders-place-flexi-order).

<a id="page-trading-orders-place-basket-order--endpoint"></a>
## Endpoint

```text
Method: POST
Endpoint: sentinel/orders/create
```

<a id="page-trading-orders-place-basket-order--basic-usage"></a>
## Basic Usage

```json
{
  "orders": [
    {
      "refId": 72329,
      "qty": 1,
      "side": "BUY",
      "deliveryType": "IDAY",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "isMultiLeg": false,
      "executionMode": "ENTRY",
      "entryPrice": 127000,
      "stratTags": ["rest-api-v3", "multi-order-buy"]
    },
    {
      "refId": 72329,
      "qty": 1,
      "side": "SELL",
      "deliveryType": "IDAY",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "isMultiLeg": false,
      "executionMode": "ENTRY",
      "entryPrice": 140000,
      "stratTags": ["rest-api-v3", "multi-order-sell"]
    }
  ]
}
```

<a id="page-trading-orders-place-basket-order--example-order-patterns"></a>
## Example Order Patterns

- use one payload per order inside the list
- mix any supported single-place-order case inside the same multi-order request
- keep the order-specific fields inside each item
- set `isMultiLeg: false` and the correct `executionMode` inside each item
- add `entryConfig` or `exitConfig` only for the orders that require it
- keep each item aligned to the same single-order field rules documented on [Place Single Order](#page-trading-orders-place-order)

=== "Limit + Market"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000
        },
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "MARKET",
          "validityType": "IOC",
          "isMultiLeg": false,
          "executionMode": "ENTRY"
        }
      ]
    }
    ```

=== "Two Limit Orders"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000
        },
        {
          "refId": 72329,
          "qty": 1,
          "side": "SELL",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 140000
        }
      ]
    }
    ```

=== "Limit + Stoploss"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 127000
        },
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY_AND_EXIT",
          "entryPrice": 127000,
          "exitConfig": {
            "stoplossParams": {
              "stoplossTriggerPrice": { "value": 126500 },
              "stoplossLimitPrice": { "value": 126400 }
            }
          }
        }
      ]
    }
    ```

=== "GTE + Limit"

    ```json
    {
      "orders": [
        {
          "refId": 72329,
          "qty": 1,
          "side": "BUY",
          "deliveryType": "CNC",
          "priceType": "LIMIT",
          "validityType": "GTE",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "goodTillDate": "2026-10-31T15:10:00Z",
          "entryPrice": 127000
        },
        {
          "refId": 72329,
          "qty": 1,
          "side": "SELL",
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "isMultiLeg": false,
          "executionMode": "ENTRY",
          "entryPrice": 140000
        }
      ]
    }
    ```

<a id="page-trading-orders-place-basket-order--execution-modes"></a>
## Execution Modes

| Value | Use |
| --- | --- |
| `ENTRY` | Standard entry-only order item |
| `ENTRY_AND_EXIT` | Order item that also carries exit controls such as stop-loss, target, or timed exit |
| `EXIT` | Exit-only order-management workflow when the item is intended only to manage the exit side |

<a id="page-trading-orders-place-basket-order--list-item-fields"></a>
## List Item Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `orders[].refId` | int | Yes | Instrument reference id for the item |
| `orders[].qty` | int | Yes | Quantity for the item |
| `orders[].side` | enum | Yes | `BUY` or `SELL` |
| `orders[].deliveryType` | enum | Yes | `IDAY` or `CNC` |
| `orders[].priceType` | enum | Yes | `LIMIT` or `MARKET` |
| `orders[].validityType` | enum | Yes | `DAY`, `IOC`, or `GTE` |
| `orders[].isMultiLeg` | boolean | Yes | Must remain `false` for independent items |
| `orders[].executionMode` | enum | Yes | `ENTRY`, `ENTRY_AND_EXIT`, or `EXIT` depending on the item |
| `orders[].entryPrice` | int | Conditional | Required for limit-based items |
| `orders[].entryConfig` | object | Conditional | Entry trigger or timed-entry controls for that item |
| `orders[].exitConfig` | object | Conditional | Stop-loss, target, trailing, or timed-exit controls for that item |

<a id="page-trading-orders-place-basket-order--nested-condition-fields"></a>
## Nested Condition Fields

| Field | Type | Description |
| --- | --- | --- |
| `entryConfig.triggers.ltp.atOrAbove.value` | int | Entry trigger above a price |
| `entryConfig.triggers.ltp.atOrBelow.value` | int | Entry trigger below a price |
| `entryConfig.entryTime` | string | Timed entry in ISO format |
| `exitConfig.exitTime` | string | Timed exit in ISO format |
| `exitConfig.stoplossParams.*` | object | Stop-loss configuration |
| `exitConfig.targetParams.*` | object | Target configuration |

<a id="page-trading-orders-place-basket-order--response-fields"></a>
## Response Fields

| Field | Meaning |
| --- | --- |
| `orders[].intentOrderId` | Unique Trading API V3 order id for the item |
| `orders[].status` | Current state of the item |
| `orders[].orderQty` | Final accepted quantity for the item |
| `orders[].orderPrice` | Final normalized price for the item |
| `orders[].intentOrderType` | Normalized item family such as `REGULAR`, `TRIGGER`, or `FLEXI` |

<a id="page-trading-orders-place-basket-order--response-shape"></a>
## Response Shape

```json
{
  "message": "order creation request pushed successfully",
  "orders": [
    {
      "intentOrderId": 9957,
      "status": "OPEN",
      "isMulti": false,
      "refId": 72329,
      "orderQty": 1,
      "orderPrice": 127000,
      "side": "BUY"
    },
    {
      "intentOrderId": 9958,
      "status": "OPEN",
      "isMulti": false,
      "refId": 72329,
      "orderQty": 1,
      "orderPrice": 140000,
      "side": "SELL"
    }
  ]
}
```

<a id="page-trading-orders-place-basket-order--important-rules"></a>
## Important Rules

- Multi-order and single-order create share the same REST route.
- A multi-order request is only a batch of independent orders.
- Keep all order-specific fields inside the relevant item instead of at the top level.
- Keep `isMultiLeg: false` on every item in this page.
- For one strategy order with multiple legs, use [Place Strategy Order](#page-trading-orders-place-flexi-order).

<a id="page-trading-orders-place-basket-order--what-to-read-next"></a>
## What To Read Next

- [Place Single Order](#page-trading-orders-place-order)
- [Place Strategy Order](#page-trading-orders-place-flexi-order)
- [Modify Multi Order](#page-trading-orders-modify-multi-order)
- [Get Orders](#page-trading-orders-get-order)

---

Source: docs/rest-api-v3/trading/orders/place-flexi-order.md

<a id="page-trading-orders-place-flexi-order"></a>
<a id="page-trading-orders-place-flexi-order--place-strategy-order"></a>
## Place Strategy Order

Use this page to place one leg-based Trading API V3 FNO strategy order through the REST API.

A strategy order sets `isMultiLeg: true` and sends a non-empty `legs` list. The strategy is treated as one order object, with one strategy-level `intentOrderId` in the response.

Strategy orders help users build complex FNO strategies by grouping multiple option or future legs into one strategy order.

With basket-level execution, users can choose strategy-level entry and exit controls without breaking the strategy into separate independent orders. Price-based entry, time-based entry, target, stop-loss, trailing stop-loss, and GTE-style validity can all be expressed through the same REST strategy payload shape.

!!! note "Scope"
    Use this page for one strategy order composed from FNO legs.

    This shape:

    - sets `isMultiLeg: true`
    - omits top-level `refId`
    - sends `legs`
    - uses one top-level `qty` for the full strategy
    - uses `legs[].unitQty` for leg-level multipliers

!!! important "Price and quantity format"
    For strategy quantities, use `qty` as the common executable base quantity derived from the leg lot sizes, and use `legs[].unitQty` as the lot multiplier for each leg. If both legs trade in `65`-lot contracts, one strategy unit is usually `qty: 65` with `unitQty: 1` on each leg. To scale the full strategy to two strategy units, set `qty: 130`. To scale only one leg, keep the same base `qty` and adjust that leg's `unitQty`.

<a id="page-trading-orders-place-flexi-order--basic-usage"></a>
## Basic Usage

```json
{
  "orders": [
    {
      "isMultiLeg": true,
      "qty": 65,
      "side": "BUY",
      "deliveryType": "CNC",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "executionMode": "ENTRY",
      "entryPrice": 44935,
      "legs": [
        {
          "refId": 1497712,
          "unitQty": 1
        },
        {
          "refId": 1497713,
          "unitQty": 1
        }
      ],
      "stratTags": ["rest-api-v3", "basic-strategy-order"]
    }
  ]
}
```

<a id="page-trading-orders-place-flexi-order--example-strategy-payload-notes"></a>
## Example Strategy Payload Notes

- each leg is passed through `legs`
- strategy-level pricing and controls stay on the top-level order object
- option `refId` values should be resolved before placement
- set `isMultiLeg: true`, set strategy `side`, omit top-level `refId`, and set the correct `executionMode`
- use `qty` as the common executable base quantity for the strategy and `legs[].unitQty` as the signed lot multiplier for each leg
- strategy orders can combine `validityType: "GTE"`, `goodTillDate`, price and time entry, stop-loss, trailing stop-loss, and target in the same payload
- if you use `validityType: "GTE"`, do not add `exitConfig.exitTime`
- there is no separate top-level basket `multiplier` field in this strategy shape; scale the whole strategy through `qty`

<a id="page-trading-orders-place-flexi-order--multi-leg-behavior"></a>
## Multi-Leg Behavior

Strategy quantity uses two layers:

- `qty`: the common executable base quantity for the full strategy
- `legs[].unitQty`: the per-leg multiplier

For a one-lot NIFTY straddle:

- top-level `qty` is `65`
- each leg uses `unitQty: 1`
- each leg expands to `orderQty: 65` in the response

If you want to scale the whole strategy, increase the top-level base quantity appropriately and keep `unitQty` as the leg multiplier. If you want to scale only one leg, keep the same base quantity and change only that leg's `unitQty`.

<a id="page-trading-orders-place-flexi-order--execution-modes"></a>
## Execution Modes

| Value | Use |
| --- | --- |
| `ENTRY` | Entry-only strategy order |
| `ENTRY_AND_EXIT` | Strategy order with target, stop-loss, trailing stop-loss, timed exit, or a combination of these |
| `EXIT` | Exit-only strategy management workflow |

<a id="page-trading-orders-place-flexi-order--rest-payload-shape"></a>
## REST Payload Shape

```json
{
  "orders": [
    {
      "isMultiLeg": true,
      "qty": 65,
      "side": "BUY",
      "deliveryType": "CNC",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "executionMode": "ENTRY",
      "entryPrice": 44935,
      "legs": [
        { "refId": 1497712, "unitQty": 1 },
        { "refId": 1497713, "unitQty": 1 }
      ],
      "stratTags": ["rest-api-v3", "basic-strategy-order"]
    }
  ]
}
```

<a id="page-trading-orders-place-flexi-order--strategy-order-fields"></a>
## Strategy Order Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `orders[].isMultiLeg` | boolean | Yes | Must be `true` for strategy orders |
| `orders[].qty` | int | Yes | Common executable base quantity for the strategy |
| `orders[].side` | enum | Yes | Strategy direction |
| `orders[].deliveryType` | enum | Yes | `CNC` or `IDAY` |
| `orders[].priceType` | enum | Yes | `LIMIT` or `MARKET` |
| `orders[].validityType` | enum | Yes | `DAY` or `GTE` depending on the payload |
| `orders[].executionMode` | enum | Yes | `ENTRY`, `ENTRY_AND_EXIT`, or `EXIT` |
| `orders[].entryPrice` | int | Conditional | Strategy net entry price for limit-based strategies |
| `orders[].goodTillDate` | string | Conditional | Required for GTE strategy payloads |
| `orders[].legs` | array | Yes | Strategy leg definitions |
| `orders[].legs[].refId` | int | Yes | Instrument reference id for the leg |
| `orders[].legs[].unitQty` | int | Yes | Leg multiplier |

<a id="page-trading-orders-place-flexi-order--condition-fields"></a>
## Condition Fields

| Field | Type | Description |
| --- | --- | --- |
| `entryConfig.triggers.*` | object | Entry trigger controls |
| `entryConfig.entryTime` | string | Timed entry in ISO format |
| `exitConfig.stoplossParams.*` | object | Stop-loss controls |
| `exitConfig.targetParams.*` | object | Target controls |
| `exitConfig.exitTime` | string | Timed exit in ISO format |

<a id="page-trading-orders-place-flexi-order--response-fields"></a>
## Response Fields

| Field | Meaning |
| --- | --- |
| `intentOrderId` | Strategy-level Trading API V3 order id |
| `isMulti` | Indicates the returned order is a multi-leg strategy |
| `legs[].unitQty` | Multiplier used for each leg |
| `legs[].orderQty` | Expanded final quantity for the leg |
| `orderQty` | Final accepted top-level strategy quantity |
| `intentOrderType` | Normalized strategy response family |

<a id="page-trading-orders-place-flexi-order--response-shape"></a>
## Response Shape

```json
{
  "message": "order creation request pushed successfully",
  "orders": [
    {
      "intentOrderId": 9965,
      "exchange": "NSE",
      "status": "OPEN",
      "isMulti": true,
      "legs": [
        {
          "refId": 1497712,
          "unitQty": 1,
          "orderQty": 65,
          "filledQty": 0,
          "filledPrice": 0
        },
        {
          "refId": 1497713,
          "unitQty": 1,
          "orderQty": 65,
          "filledQty": 0,
          "filledPrice": 0
        }
      ],
      "filledQty": 0,
      "orderQty": 65,
      "deliveryType": "CNC",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "executionMode": "ENTRY",
      "stratTags": ["rest-api-v3", "basic-strategy-order"],
      "orderPrice": 44935,
      "intentOrderType": "REGULAR",
      "side": "BUY"
    }
  ]
}
```

<a id="page-trading-orders-place-flexi-order--important-rules"></a>
## Important Rules

- every leg must use a unique instrument
- all legs must belong to the same exchange
- choose `qty` as the common executable base quantity derived from the leg lot sizes
- use `unitQty` as the leg multiplier, not as the absolute lot size
- there is no separate basket-level multiplier field; scale the full strategy through `qty`
- keep the same `qty` and `unitQty` logic in both placement and margin-estimation payloads so the estimated strategy matches the placed strategy

<a id="page-trading-orders-place-flexi-order--what-to-read-next"></a>
## What To Read Next

- [Place Single Order](#page-trading-orders-place-order)
- [Modify Order](#page-trading-orders-modify-order)
- [Get Orders](#page-trading-orders-get-order)
- [Get Order Margin](#page-trading-orders-get-margin)

---

Source: docs/rest-api-v3/trading/orders/modify-order.md

<a id="page-trading-orders-modify-order"></a>
<a id="page-trading-orders-modify-order--modify-order"></a>
## Modify Order

Use this page to modify one existing Trading API V3 order ID through the REST API.

This same endpoint is used for:

- one single-instrument order
- one item originally placed inside a multi-order request
- one strategy order

For strategy orders created with `isMultiLeg: true`, use the strategy-level `intentOrderId` returned by placement. Do not use `basketId`, and do not resend `legs` or `isMultiLeg` in the modify payload.

<a id="page-trading-orders-modify-order--basic-usage"></a>
## Basic Usage

```json
{
  "orders": [
    {
      "orderId": 10003,
      "deliveryType": "CNC",
      "priceType": "LIMIT",
      "entryPrice": 1420,
      "validityType": "DAY",
      "executionMode": "ENTRY",
      "echoFields": "{\"omsType\":\"SINGLE\",\"orderType\":\"REGULAR\",\"displayName\":\"Custom Basket\"}"
    }
  ]
}
```

Use the payload as an order-level patch request. Send only the fields you want to change, but keep the field names and nesting exactly aligned to the create-order shape for the same order family.

<a id="page-trading-orders-modify-order--order-type-scope"></a>
## Order Type Scope

Use this page when modifying exactly one Trading API V3 `intentOrderId`.

The REST body still uses an `orders` array, but the array should contain exactly one modify item.

<a id="page-trading-orders-modify-order--example-modify-patterns"></a>
## Example Modify Patterns

- pass the target Trading API V3 order ID as `orderId`
- keep the request object scoped to the fields being changed
- use `entryConfig` for entry trigger or timed-entry changes
- use `exitConfig` for stop-loss, target, trailing stop-loss, or timed-exit changes
- for strategy orders, use `qty` as the updated common executable base quantity
- do not resend `legs` or `isMultiLeg` when modifying an already-created strategy order

=== "Price / Quantity"

    ```json
    {
      "orders": [
        {
          "orderId": 10003,
          "qty": 1,
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "entryPrice": 127500,
          "validityType": "DAY",
          "executionMode": "ENTRY"
        }
      ]
    }
    ```

=== "Entry Trigger"

    ```json
    {
      "orders": [
        {
          "orderId": 10003,
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "entryPrice": 127000,
          "validityType": "DAY",
          "executionMode": "ENTRY",
          "entryConfig": {
            "triggers": {
              "ltp": {
                "atOrAbove": { "value": 127000 }
              }
            }
          }
        }
      ]
    }
    ```

=== "Stoploss / Target"

    ```json
    {
      "orders": [
        {
          "orderId": 10003,
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "entryPrice": 127000,
          "validityType": "DAY",
          "executionMode": "ENTRY_AND_EXIT",
          "exitConfig": {
            "stoplossParams": {
              "stoplossTriggerPrice": { "value": 126500 },
              "stoplossLimitPrice": { "value": 126400 }
            },
            "targetParams": {
              "targetProfitTriggerPrice": { "value": 127500 },
              "targetProfitLimitPrice": { "value": 127400 }
            }
          }
        }
      ]
    }
    ```

=== "Trailing Stoploss"

    ```json
    {
      "orders": [
        {
          "orderId": 10003,
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "entryPrice": 127000,
          "validityType": "DAY",
          "executionMode": "ENTRY_AND_EXIT",
          "exitConfig": {
            "stoplossParams": {
              "stoplossTriggerPrice": { "value": 126500 },
              "stoplossLimitPrice": { "value": 126400 },
              "stoplossTrailJump": 5
            }
          }
        }
      ]
    }
    ```

=== "Strategy Order"

    ```json
    {
      "orders": [
        {
          "orderId": 10003,
          "qty": 65,
          "deliveryType": "CNC",
          "priceType": "LIMIT",
          "entryPrice": 44935,
          "validityType": "DAY",
          "executionMode": "ENTRY"
        }
      ]
    }
    ```

<a id="page-trading-orders-modify-order--timed-entry-exit"></a>
## Timed Entry / Exit

Use `entryConfig.entryTime` to adjust scheduled entry behavior and `exitConfig.exitTime` to adjust scheduled exit behavior.

```json
{
  "orders": [
    {
      "orderId": 10003,
      "deliveryType": "IDAY",
      "priceType": "LIMIT",
      "entryPrice": 127000,
      "validityType": "DAY",
      "executionMode": "ENTRY",
      "entryConfig": {
        "entryTime": "2026-06-17T09:20:00Z"
      },
      "exitConfig": {
        "exitTime": "2026-06-17T09:25:00Z"
      }
    }
  ]
}
```

<a id="page-trading-orders-modify-order--gte-modifications"></a>
## GTE Modifications

For good-till orders, keep `validityType: "GTE"` and send the new `goodTillDate`.

```json
{
  "orders": [
    {
      "orderId": 10003,
      "deliveryType": "CNC",
      "priceType": "LIMIT",
      "entryPrice": 127000,
      "validityType": "GTE",
      "goodTillDate": "2026-10-31T15:10:00Z",
      "executionMode": "ENTRY"
    }
  ]
}
```

<a id="page-trading-orders-modify-order--execution-modes"></a>
## Execution Modes

| Value | Use |
| --- | --- |
| `ENTRY` | Entry-only modify |
| `ENTRY_AND_EXIT` | Modify payload that also changes managed exits |
| `EXIT` | Exit-only modify flow |

<a id="page-trading-orders-modify-order--request-fields"></a>
## Request Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `orders` | array | Yes | Wrapper for one or more modify requests |
| `orders[].orderId` | int | Yes | Intent order id to modify |
| `orders[].qty` | int | Conditional | Updated quantity. For strategy orders, use the updated common executable base quantity |
| `orders[].deliveryType` | enum | Yes | Updated delivery type |
| `orders[].priceType` | enum | Yes | Updated price type |
| `orders[].entryPrice` | int | Conditional | Updated limit price |
| `orders[].validityType` | enum | Yes | Updated validity type |
| `orders[].executionMode` | enum | Yes | Updated execution mode |
| `orders[].goodTillDate` | string | Conditional | Updated expiry time for GTE orders |
| `orders[].entryConfig` | object | Conditional | Updated entry trigger or entry time |
| `orders[].exitConfig` | object | Conditional | Updated stop-loss, target, trailing, or exit time |
| `orders[].echoFields` | string | Optional | Client metadata echoed through the OMS flow |

<a id="page-trading-orders-modify-order--condition-fields"></a>
## Condition Fields

| Field | Type | Description |
| --- | --- | --- |
| `entryConfig.triggers.*` | object | Updated entry trigger controls |
| `entryConfig.entryTime` | string | Updated timed entry |
| `exitConfig.stoplossParams.*` | object | Updated stop-loss controls |
| `exitConfig.targetParams.*` | object | Updated target controls |
| `exitConfig.exitTime` | string | Updated timed exit |

<a id="page-trading-orders-modify-order--response-fields"></a>
## Response Fields

The modify endpoint returns an acknowledgement:

```json
{
  "message": "order modify request pushed successfully"
}
```

<a id="page-trading-orders-modify-order--important-rules"></a>
## Important Rules

- Treat the modify response as an acknowledgement only.
- A `200` response means the modify request was accepted by the backend, not that the exchange-side state has already changed.
- To confirm whether a modify actually took effect, call `GET sentinel/orders`, find the target `intentOrderId`, and compare `orderPrice`, `status`, and `timestamps.lastModifiedAt`.
- If the target order is already executed, cancelled, or still being processed by the exchange, the modify may be ignored or rejected even when the payload shape is otherwise correct.
- For target exits, keep `targetProfitTriggerPrice` greater than or equal to `targetProfitLimitPrice`.

<a id="page-trading-orders-modify-order--what-to-read-next"></a>
## What To Read Next

- [Modify Multi Order](#page-trading-orders-modify-multi-order)
- [Cancel Order](#page-trading-orders-cancel-order)
- [Get Orders](#page-trading-orders-get-order)

---

Source: docs/rest-api-v3/trading/orders/modify-multi-order.md

<a id="page-trading-orders-modify-multi-order"></a>
<a id="page-trading-orders-modify-multi-order--modify-multi-order"></a>
## Modify Multi Order

Use this page to modify multiple existing Trading API V3 order IDs in one REST request.

Group modifications for:

- multiple independent single-instrument orders
- multiple items that were originally placed through [Place Multi Order](#page-trading-orders-place-basket-order)
- multiple strategy orders
- a mixed list of single orders and strategy order IDs

Every item in `orders[]` carries its own `orderId` and only the fields being changed for that target order.

For strategy orders created with `isMultiLeg: true`, use the strategy-level `intentOrderId` as `orderId`. Do not use `basketId`, and do not resend `legs`, `isMultiLeg`, or `basketParams`.

<a id="page-trading-orders-modify-multi-order--endpoint"></a>
## Endpoint

```text
Method: POST
Endpoint: sentinel/orders/modify
```

<a id="page-trading-orders-modify-multi-order--basic-usage"></a>
## Basic Usage

```bash
curl --location 'https://uatapi.nubra.io/sentinel/orders/modify' \
--header 'x-device-id: {{x_device_id}}' \
--header 'x-app-version: 0.4.5' \
--header 'x-device-os: sdk' \
--header 'Cookie: deviceId={{x_device_id}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{session_token}}' \
--data '{
  "orders": [
    {
      "orderId": 987654,
      "qty": 1,
      "entryPrice": 24600,
      "deliveryType": "IDAY",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "executionMode": "ENTRY"
    },
    {
      "orderId": 987655,
      "entryPrice": 18000,
      "deliveryType": "IDAY",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "executionMode": "ENTRY"
    }
  ]
}'
```

<a id="page-trading-orders-modify-multi-order--order-type-scope"></a>
## Order Type Scope

| Existing order type | Which ID to use in each item | Notes |
| --- | --- | --- |
| Single order | `orderId: orders[i].intentOrderId` | Modify several independent single orders together. |
| Multi-order item | `orderId: orders[i].intentOrderId` | Each item from a multi-order placement has its own ID. |
| Strategy order | `orderId: strategy intentOrderId` | Each strategy order is one strategy-level order ID. |

<a id="page-trading-orders-modify-multi-order--example-modify-patterns"></a>
## Example Modify Patterns

=== "Two Limit Modifications"

    ```json
    {
      "orders": [
        {
          "orderId": 987654,
          "qty": 1,
          "entryPrice": 24600,
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "executionMode": "ENTRY"
        },
        {
          "orderId": 987655,
          "qty": 1,
          "entryPrice": 18000,
          "deliveryType": "IDAY",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "executionMode": "ENTRY"
        }
      ]
    }
    ```

=== "Entry + Exit Mix"

    ```json
    {
      "orders": [
        {
          "orderId": 987654,
          "entryPrice": 24600,
          "entryConfig": {
            "triggers": {
                "ltp": {
                    "atOrAbove": {"value": 24600}
                }
            }
          },
          "executionMode": "ENTRY"
        },
        {
          "orderId": 987655,
          "exitConfig": {
            "targetParams": {
              "targetProfitTriggerPrice": { "value": 18400 },
              "targetProfitLimitPrice": { "value": 18380 }
            }
          },
          "executionMode": "EXIT"
        }
      ]
    }
    ```

=== "Multiple Strategy Orders"

    ```json
    {
      "orders": [
        {
          "orderId": 987654,
          "qty": 130,
          "entryPrice": -36000,
          "deliveryType": "CNC",
          "priceType": "LIMIT",
          "validityType": "DAY",
          "executionMode": "ENTRY"
        },
        {
          "orderId": 987655,
          "exitConfig": {
            "targetParams": {
              "targetProfitTriggerPrice": { "value": -39000 },
              "targetProfitLimitPrice": { "value": -39100 }
            }
          },
          "executionMode": "EXIT"
        }
      ]
    }
    ```

    Use this pattern when several strategy orders need strategy-level updates. Each `orderId` is a strategy-level `intentOrderId`. For example, if one strategy unit uses base `qty: 65`, then `qty: 130` represents two strategy units.

=== "Mixed Single + Strategy Order"

    ```json
    {
      "orders": [
        {
          "orderId": 987654,
          "entryPrice": 24600,
          "executionMode": "ENTRY"
        },
        {
          "orderId": 987655,
          "qty": 130,
          "entryPrice": -36000,
          "executionMode": "ENTRY"
        }
      ]
    }
    ```

<a id="page-trading-orders-modify-multi-order--timed-and-gte-modifications"></a>
## Timed And GTE Modifications

Timed entry, timed exit, and GTE validity can also be grouped inside `orders[]`. Keep the execution mode aligned to the fields being changed in each item.

```json
{
  "orders": [
    {
      "orderId": 987654,
      "entryConfig": {
        "entryTime": "2026-10-30T09:20:00.000Z"
      },
      "exitConfig": {
        "exitTime": "2026-10-30T15:10:00.000Z"
      },
      "executionMode": "ENTRY_AND_EXIT"
    },
    {
      "orderId": 987655,
      "validityType": "GTE",
      "goodTillDate": "2026-10-30T15:20:00.000Z",
      "executionMode": "ENTRY"
    }
  ]
}
```

For futures and options, `goodTillDate` must not be beyond the contract expiry. For stocks, the date can be up to a maximum of one year.

<a id="page-trading-orders-modify-multi-order--execution-modes"></a>
## Execution Modes

Each item inside `orders[]` has its own `executionMode`.

| Item payload shape | `executionMode` | Meaning |
| --- | --- | --- |
| The item modifies `entryPrice` and/or `entryConfig`, and has no `exitConfig`. | `ENTRY` | Entry-only order modification. |
| The item has no entry fields and modifies only `exitConfig`. | `EXIT` | Exit-only order modification. |
| The item modifies entry fields and also modifies `exitConfig`. | `ENTRY_AND_EXIT` | Entry order with attached exit modifications. |

<a id="page-trading-orders-modify-multi-order--request-attributes"></a>
## Request Attributes

| Field | Type | Required | Allowed values / shape | Meaning |
| --- | --- | ---: | --- | --- |
| `orders` | `array` | yes | non-empty array | Modification items. |
| `orders[].orderId` | `int` | yes | Trading API V3 `intentOrderId` | Target Trading API V3 order ID for this item. |
| `orders[].refId` | `int` | no | instrument ref ID | Replacement instrument reference ID when supported. Do not use for strategy order modification. |
| `orders[].qty` | `int` | no | positive integer | Updated single-order quantity. For strategy orders, send the updated common executable base quantity. To scale the full strategy, multiply the base quantity here. |
| `orders[].side` | `string` | no | `BUY`, `SELL` | Updated side when supported. Do not use for strategy order modification. |
| `orders[].entryPrice` | `int` | no | price integer | Updated entry price, or net strategy price for strategy orders. |
| `orders[].goodTillDate` | `string` | no | date-time string | Updated GTE date/time. |
| `orders[].entryConfig` | `object` | no | timed entry or triggers | Updated entry conditions. |
| `orders[].exitConfig` | `object` | no | stop-loss, target, trailing stop, exit time | Updated exit conditions. |
| `orders[].deliveryType` | `string` | no | `IDAY`, `CNC` | Updated delivery type when supported by the order. |
| `orders[].priceType` | `string` | no | `LIMIT`, `MARKET` | Updated price type. |
| `orders[].validityType` | `string` | no | `DAY`, `IOC`, `GTE` | Updated validity. |
| `orders[].executionMode` | `string` | no | `ENTRY`, `EXIT`, `ENTRY_AND_EXIT` | Execution mode that matches this item's updated fields. |
| `orders[].icebergInfo` | `object` | no | `numberOfLegs` or `maxQtyPerLeg` | Updated iceberg slicing settings when supported. |
| `orders[].echoFields` | `string` | no | string | Metadata echoed back by Trading API V3. |

<a id="page-trading-orders-modify-multi-order--response-structure"></a>
## Response Structure

```json
{
  "message": "order modify request pushed successfully"
}
```

Fetch the latest order state with [Get Orders](#page-trading-orders-get-order) after modification when control flow depends on final order status, fill state, rejection reason, or strategy order leg state.

<a id="page-trading-orders-modify-multi-order--important-rules"></a>
## Important Rules

!!! important-rules "Important Rules"
    - Include `orderId` inside every item.
    - Send only the fields being changed for each target order.
    - Set `executionMode` per item based on that item's entry and exit fields.
    - Strategy order IDs can be modified in the same grouped request as single-order IDs.
    - For strategy orders, use the strategy-level `intentOrderId` as `orderId`; do not pass `basketId`.
    - For strategy-order quantity changes, update `qty` using the same base-quantity model used at placement time.
    - Do not send `legs`, `isMultiLeg`, or `basketParams` in modify requests.
    - Do not send top-level `refId` or top-level `side` when modifying a strategy order.
    - Use [Modify Order](#page-trading-orders-modify-order) when modifying only one Trading API V3 order ID.
    - Use [Get Orders](#page-trading-orders-get-order) to inspect current order state before and after modification.

<a id="page-trading-orders-modify-multi-order--what-to-read-next"></a>
## What To Read Next

1. [Modify Order](#page-trading-orders-modify-order)
2. [Place Multi Order](#page-trading-orders-place-basket-order)
3. [Place Strategy Order](#page-trading-orders-place-flexi-order)
4. [Get Orders](#page-trading-orders-get-order)
5. [Cancel Order](#page-trading-orders-cancel-order)

---

Source: docs/rest-api-v3/trading/orders/cancel-order.md

<a id="page-trading-orders-cancel-order"></a>
<a id="page-trading-orders-cancel-order--cancel-order"></a>
## Cancel Order

Use this page to cancel Trading API V3 orders through the REST API. The same cancel endpoint is used for full orders and selected exit triggers.

Use this same Trading API V3 cancel endpoint for:

- single orders
- independent multi-order items
- strategy orders

For Trading API V3 strategy orders created with `isMultiLeg: true`, the placement response contains one strategy-level `intentOrderId`. Use that same ID to cancel the full strategy order. Do not use `basketId`, and do not send `legs` or `isMultiLeg` in the cancel request.

!!! note "Scope"
    To cancel a full order, pass `{"orderId": intent_order_id}`. To cancel a selected exit trigger, pass `{"orderId": intent_order_id, "exitTriggerKind": "STOPLOSS"}` or the relevant trigger kind.

<a id="page-trading-orders-cancel-order--endpoint"></a>
## Endpoint

```text
Method: POST
Endpoint: sentinel/orders/cancel
```

<a id="page-trading-orders-cancel-order--basic-usage"></a>
## Basic Usage

```bash
curl --location 'https://uatapi.nubra.io/sentinel/orders/cancel' \
--header 'x-device-id: {{x_device_id}}' \
--header 'x-app-version: 0.4.5' \
--header 'x-device-os: sdk' \
--header 'Cookie: deviceId={{x_device_id}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{session_token}}' \
--data '{
  "orders": [
    {
      "orderId": 987654
    }
  ]
}'
```

Omitting `exitTriggerKind` cancels the full Trading API V3 order.

<a id="page-trading-orders-cancel-order--cancel-full-order-patterns"></a>
## Cancel Full Order Patterns

These examples all use the same Trading API V3 cancellation endpoint. The only difference is which `intentOrderId` values you pass.

=== "Single Order"

    ```json
    {
      "orders": [
        {
          "orderId": 987654
        }
      ]
    }
    ```

    Use this pattern when cancelling one independent single-instrument Trading API V3 order.

=== "Multi Order Items"

    ```json
    {
      "orders": [
        {
          "orderId": 987654
        },
        {
          "orderId": 987655
        }
      ]
    }
    ```

    Use this pattern when cancelling multiple independent orders that were placed together through [Place Multi Order](#page-trading-orders-place-basket-order). Each item has its own `intentOrderId`; cancel only the items that should be cancelled.

=== "Strategy Order"

    ```json
    {
      "orders": [
        {
          "orderId": 987654
        }
      ]
    }
    ```

    Use this pattern when cancelling one strategy order. The `orderId` is the `intentOrderId` returned by the `isMultiLeg: true` placement response.

<a id="page-trading-orders-cancel-order--cancel-exit-trigger-patterns"></a>
## Cancel Exit Trigger Patterns

Use `exitTriggerKind` when the order should remain active but a selected attached exit trigger should be cancelled.

=== "Cancel Stop-Loss Trigger"

    ```json
    {
      "orders": [
        {
          "orderId": 987654,
          "exitTriggerKind": "STOPLOSS"
        }
      ]
    }
    ```

    Use this pattern to cancel only the stop-loss exit trigger attached to the Trading API V3 order.

=== "Cancel Target Trigger"

    ```json
    {
      "orders": [
        {
          "orderId": 987654,
          "exitTriggerKind": "TARGET_PROFIT"
        }
      ]
    }
    ```

    Use this pattern to cancel only the target-profit exit trigger attached to the Trading API V3 order.

=== "Cancel Trailing Stop Trigger"

    ```json
    {
      "orders": [
        {
          "orderId": 987654,
          "exitTriggerKind": "TRAILING_STOP"
        }
      ]
    }
    ```

    Use this pattern to cancel only the trailing stop-loss exit trigger attached to the Trading API V3 order.

=== "Cancel Multiple Exit Triggers"

    ```json
    {
      "orders": [
        {
          "orderId": 987654,
          "exitTriggerKind": "STOPLOSS"
        },
        {
          "orderId": 987655,
          "exitTriggerKind": "TARGET_PROFIT"
        }
      ]
    }
    ```

    Use this pattern when cancelling selected exit triggers across multiple Trading API V3 orders.

<a id="page-trading-orders-cancel-order--request-attributes"></a>
## Request Attributes

| Field | Type | Required | Meaning |
| --- | --- | ---: | --- |
| `orders` | `array` | yes | Cancel request items. |
| `orders[].orderId` | `int` | yes | Trading API V3 `intentOrderId` returned by placement or order retrieval. |
| `orders[].exitTriggerKind` | `string` | no | `STOPLOSS`, `TARGET_PROFIT`, or `TRAILING_STOP`; omit to cancel the full order. |

<a id="page-trading-orders-cancel-order--order-id-sources"></a>
## Order ID Sources

| Order type | Which ID to cancel | Notes |
| --- | --- | --- |
| Single order | `orders[0].intentOrderId` | Returned by [Place Single Order](#page-trading-orders-place-order). |
| Multi order | each `orders[i].intentOrderId` | Returned by [Place Multi Order](#page-trading-orders-place-basket-order); each independent item has its own ID. |
| Strategy order | strategy `orders[0].intentOrderId` | One ID represents the full strategy. `legs[]` are details under the strategy and do not have cancel IDs. |

<a id="page-trading-orders-cancel-order--response-structure"></a>
## Response Structure

```json
{
  "message": "order cancellation request pushed successfully"
}
```

Treat cancellation as an acknowledgement and fetch current state with [Get Orders](#page-trading-orders-get-order) afterwards when control flow depends on final status.

<a id="page-trading-orders-cancel-order--important-rules"></a>
## Important Rules

!!! important-rules "Important Rules"
    - Pass IDs from the active environment.
    - Use Trading API V3 `intentOrderId` values for all cancellation flows.
    - Single, multi-order, and strategy order cancellation use the same Trading API V3 cancel endpoint.
    - For a strategy order, pass the strategy-level `intentOrderId`; do not pass `basketId`.
    - Cancellation is a request, not a guarantee that execution state can always be reversed.
    - Omit `exitTriggerKind` when the goal is to cancel the full order.
    - Pass `exitTriggerKind` only when cancelling a specific exit trigger.
    - Inspect latest state with [Get Orders](#page-trading-orders-get-order) when cancellation status matters.

<a id="page-trading-orders-cancel-order--what-to-read-next"></a>
## What To Read Next

1. [Get Orders](#page-trading-orders-get-order)
2. [Place Single Order](#page-trading-orders-place-order)
3. [Place Multi Order](#page-trading-orders-place-basket-order)
4. [Place Strategy Order](#page-trading-orders-place-flexi-order)

---

Source: docs/rest-api-v3/trading/orders/get-order.md

<a id="page-trading-orders-get-order"></a>
<a id="page-trading-orders-get-order--get-orders"></a>
## Get Orders

Use this page to fetch grouped Trading API V3 order snapshots through the REST API.

This is the main REST V3 retrieval page for single orders, multi-order items, and strategy orders. Use it as the operational verification endpoint after create, modify, or cancel requests.

Use the same retrieval endpoint for:

- single orders
- independent multi-order items
- strategy orders

For strategy orders created with `isMultiLeg: true`, Trading API V3 returns one strategy-level order with `isMulti: true` and a non-empty `legs` list.

<a id="page-trading-orders-get-order--endpoint"></a>
## Endpoint

```text
Method: GET
Endpoint: sentinel/orders
```

<a id="page-trading-orders-get-order--basic-usage"></a>
## Basic Usage

```bash
curl --location 'https://uatapi.nubra.io/sentinel/orders' \
--header 'Authorization: Bearer {{session_token}}' \
--header 'x-device-id: {{x_device_id}}' \
--header 'x-app-version: 0.4.5' \
--header 'x-device-os: sdk' \
--header 'Cookie: deviceId={{x_device_id}}'
```

<a id="page-trading-orders-get-order--response-shape"></a>
## Response Shape

```json
{
  "orders": {
    "open": [
      {
        "intentOrderId": 9979,
        "exchange": "NSE",
        "status": "OPEN",
        "orderPrice": 127000,
        "timestamps": {
          "intentCreatedAt": "2026-06-15T09:36:41.321238924Z",
          "sentToColoAt": "2026-06-15T09:36:41.329677462Z"
        },
        "intentOrderType": "REGULAR"
      }
    ],
    "cancelled": [
      {
        "intentOrderId": 9972,
        "exchange": "NSE",
        "status": "CANCELLED",
        "orderPrice": 127500,
        "timestamps": {
          "intentCreatedAt": "2026-06-15T09:26:31.228469923Z",
          "sentToColoAt": "2026-06-15T09:27:27.301932449Z",
          "cancelledAt": "2026-06-15T09:27:31.295763424Z",
          "lastModifiedAt": "2026-06-15T09:27:26.29550221Z",
          "lastUpdatedAt": "2026-06-15T09:27:31.295763424Z"
        },
        "intentOrderType": "REGULAR"
      }
    ],
    "executed": [],
    "rejected": [],
    "gtt": []
  }
}
```

<a id="page-trading-orders-get-order--response-notes"></a>
## Response Notes

- orders are grouped by status bucket instead of being returned as one flat list
- common buckets include `open`, `cancelled`, `executed`, `rejected`, and `gtt`
- each order object contains the normalized V3 order model
- strategy orders still appear as one strategy-level order row; inspect `isMulti`, `legs`, `orderQty`, and `intentOrderType` inside that grouped response
- use the `gtt` bucket when validating good-till orders returned by the API

<a id="page-trading-orders-get-order--recommended-usage"></a>
## Recommended Usage

Use `GET sentinel/orders` for:

- checking whether create requests were accepted
- verifying whether modify requests actually changed `orderPrice`
- inspecting `lastModifiedAt`, `cancelledAt`, and `lastUpdatedAt`
- locating a specific order by filtering on `intentOrderId` in the returned buckets
- checking whether a strategy order is still open as one grouped order or has progressed to later lifecycle states

<a id="page-trading-orders-get-order--important-note"></a>

---

Source: docs/rest-api-v3/trading/realtime-order-updates.md

<a id="page-trading-realtime-order-updates"></a>
<a id="page-trading-realtime-order-updates--realtime-order-updates"></a>
## Realtime Order Updates

Use the order-update WebSocket stream to receive realtime Trading API V3 order-state and trade-execution events.

For REST API integrations, connect directly to the WebSocket endpoint, authenticate with the same session token used for REST calls, and decode binary protobuf messages. Trading API V3 order events are sent as `NubraToClientIntentUpdate` messages.

The stream separates two practical event categories:

- non-fill intent-order events such as accepted, rejected, modified, cancelled, triggered, or trail-updated updates
- fill events where the V3 update contains `intentOrderResponse.tradeFill`

Use [Get Orders](#page-trading-orders-get-order) when you need a fetched snapshot instead of a live stream.

If the goal is debugging or operational validation, prefer logging the full decoded event object first and only then narrowing the fields you read in production logic.

<a id="page-trading-realtime-order-updates--websocket-endpoint"></a>
## WebSocket Endpoint

Use the UAT WebSocket URL for the current V3 rollout:

| Environment | WebSocket URL |
| --- | --- |
| UAT | `wss://uatapi.nubra.io/ws` |

<a id="page-trading-realtime-order-updates--rest-base-url"></a>
## REST Base URL

Use the UAT REST base URL for authentication and session management:

| Environment | REST base URL |
| --- | --- |
| UAT | `https://uatapi.nubra.io` |

<a id="page-trading-realtime-order-updates--authentication"></a>
## Authentication

Order updates are pushed only for authenticated sessions. Use the same session token as the REST API login flow.

After the WebSocket opens, send this text message:

```text
subscribe <session_token> notifications notification
```

If the WebSocket returns `Invalid Token`, re-authenticate and reconnect.

<a id="page-trading-realtime-order-updates--message-envelope"></a>
## Message Envelope

WebSocket binary payloads are protobuf `Any` messages. The server sends an outer `Any` whose `value` contains another `Any`.

For Trading API V3, the inner `Any.type_url` ends with:

```text
NubraToClientIntentUpdate
```

The inner `Any.value` is the corresponding `NubraToClientIntentUpdate` protobuf payload.

```proto
message Any {
  string type_url = 1;
  bytes value = 2;
}
```

<a id="page-trading-realtime-order-updates--payload-nubratoclientintentupdate-proto"></a>
## Payload: NubraToClientIntentUpdate Proto

The Trading API V3 order-update payload is `NubraToClientIntentUpdate`.

```proto
message NubraToClientIntentUpdate {
  IntentOrderResponse intent_order_response = 1;
  IntentOrderResponseType intent_order_response_type = 2;
  IntentOrderRequestType intent_order_requst_type = 3;
}

message IntentOrderResponse {
  int64 intent_order_id = 1;
  NubraIntentOrderStatus order_status = 2;
  IntentEntryConfig entry_config = 3;
  repeated IntentExitTrigger exit_triggers = 4;
  repeated IntentLeg legs = 5;
  int64 filled_at = 6;
  OrderDeliveryType delivery_type = 7;
  PriceType price_type = 8;
  ValidityType validity_type = 9;
  repeated string strat_tags = 10;
  bool is_admin = 11;
  string echo_fields = 12;
  int64 order_qty = 13;
  int64 filled_qty = 14;
  int64 expiry_time = 15;
  int64 ltp = 16;
  int64 order_price = 17;
  int64 filled_price = 18;
  TradeFill trade_fill = 19;
  ExecutionMode execution_mode = 20;
  NubraIntentTimestamps nubra_timestamps = 21;
  string position_id = 22;
  int64 entry_price = 23;
  IcebergInfo iceberg_info = 24;
  RefData refdata = 25;
  int64 ref_id = 26;
  int64 good_till_date = 27;
  bool is_multi = 28;
  OrderSide order_side = 29;
  IntentOrderType intent_order_type = 30;
  string rejection_msg = 31;
}
```

!!! note "Protocol field spelling"
    The proto field for request type is `intent_order_requst_type`; its default JSON name is `intentOrderRequstType`. Some SDK wrappers expose a normalized `intent_order_request_type` property, but direct REST WebSocket decoders should handle the raw protocol field name.

<a id="page-trading-realtime-order-updates--nested-messages-proto"></a>
## Nested Messages Proto

```proto
message TradeFill {
  int64 trade_qty = 1;
  int64 trade_price = 2;
  int64 ref_id = 3;
}

message IntentEntryConfig {
  repeated IntentEntryCondition conditions = 4;
  ConditionOperator condition_operator = 5;
  int64 entry_time = 6;
}

message IntentEntryCondition {
  ConditionKind kind = 1;
  int64 threshold = 2;
  IntentEntryTriggerStatus status = 3;
}

message ConditionKind {
  LTPConditionKind ltp_condition_kind = 1;
}

message IntentExitTrigger {
  IntentExitTriggerKind kind = 1;
  LTPConditionKind condition_kind = 2;
  int64 trigger_price = 3;
  int64 limit_price = 4;
  int64 trail_jump = 5;
  IntentExitTriggerStatus status = 6;
  int64 algo_trigger_price = 7;
  int64 algo_limit_price = 8;
  int64 exit_time = 9;
}

message IntentLeg {
  int64 ref_id = 1;
  int32 unit_qty = 2;
  int32 filled_qty = 3;
  int64 filled_price = 4;
  RefData refdata = 5;
  int32 order_qty = 6;
}

message NubraIntentTimestamps {
  int64 intent_created_at = 1;
  int64 sent_to_colo_at = 2;
  int64 filled_at = 3;
  int64 cancelled_at = 4;
  int64 last_modified_at = 5;
  int64 last_updated_at = 6;
}

message IcebergInfo {
  int32 number_of_legs = 1;
  int32 max_qty_per_leg = 2;
}

message RefData {
  int64 ref_id = 1;
  int64 zanskar_id = 2;
  string option_type = 3;
  int64 token = 4;
  string stock_name = 5;
  string series = 6;
  string zanskar_name = 7;
  int64 lot_size = 8;
  string asset = 9;
  string exchange = 10;
  string derivative_type = 11;
  string display_name = 12;
}
```

<a id="page-trading-realtime-order-updates--shared-enums-proto"></a>
## Shared Enums Proto

```proto
enum IntentOrderResponseType {
  INTENT_ORDER_RESPONSE_TYPE_INVALID = 0;
  INTENT_ORDER_RESPONSE_TYPE_ACCEPT = 1;
  INTENT_ORDER_RESPONSE_TYPE_REJECT = 2;
  INTENT_ORDER_RESPONSE_TYPE_FILLED = 3;
  INTENT_ORDER_RESPONSE_TYPE_ENTRY_TRIGGERED = 4;
  INTENT_ORDER_RESPONSE_TYPE_EXIT_SL_TRIGGERED = 5;
  INTENT_ORDER_RESPONSE_TYPE_EXIT_TP_TRIGGERED = 6;
  INTENT_ORDER_RESPONSE_TYPE_TRAIL_UPDATED = 7;
  INTENT_ORDER_RESPONSE_TYPE_EXECUTED = 8;
  INTENT_ORDER_RESPONSE_TYPE_UNSOLICITED_CANCEL = 9;
}

enum IntentOrderRequestType {
  INTENT_ORDER_REQUEST_TYPE_INVALID = 0;
  INTENT_ORDER_REQUEST_TYPE_NEW = 1;
  INTENT_ORDER_REQUEST_TYPE_MOD = 2;
  INTENT_ORDER_REQUEST_TYPE_CANCEL = 3;
}

enum NubraIntentOrderStatus {
  INTENT_ORDER_STATUS_INVALID = 0;
  INTENT_ORDER_STATUS_OPEN = 1;
  INTENT_ORDER_STATUS_EXECUTED = 2;
  INTENT_ORDER_STATUS_REJECTED = 3;
  INTENT_ORDER_STATUS_GTE = 4;
  INTENT_ORDER_STATUS_CANCELLED = 5;
  INTENT_ORDER_STATUS_EXPIRED = 6;
}

enum ExecutionMode {
  EXECUTION_MODE_INVALID = 0;
  EXECUTION_MODE_ENTRY = 1;
  EXECUTION_MODE_EXIT = 2;
  EXECUTION_MODE_ENTRY_AND_EXIT = 3;
}

enum IntentOrderType {
  INTENT_ORDER_TYPE_INVALID = 0;
  INTENT_ORDER_TYPE_REGULAR = 1;
  INTENT_ORDER_TYPE_TRIGGER = 2;
  INTENT_ORDER_TYPE_ICEBERG = 3;
  INTENT_ORDER_TYPE_FLEXI = 4;
}

enum IntentExitTriggerKind {
  INTENT_EXIT_TRIGGER_KIND_INVALID = 0;
  INTENT_EXIT_TRIGGER_KIND_STOPLOSS = 1;
  INTENT_EXIT_TRIGGER_KIND_TARGET_PROFIT = 2;
  INTENT_EXIT_TRIGGER_KIND_TRAILING_STOP = 3;
  INTENT_EXIT_TRIGGER_KIND_EXIT_TIME = 4;
}

enum IntentExitTriggerStatus {
  INTENT_EXIT_TRIGGER_STATUS_OPEN = 0;
  INTENT_EXIT_TRIGGER_STATUS_TRIGGERED = 1;
  INTENT_EXIT_TRIGGER_STATUS_FILLED = 2;
  INTENT_EXIT_TRIGGER_STATUS_CANCELLED = 3;
}

enum IntentEntryTriggerStatus {
  INTENT_ENTRY_TRIGGER_STATUS_OPEN = 0;
  INTENT_ENTRY_TRIGGER_STATUS_TRIGGERED = 1;
  INTENT_ENTRY_TRIGGER_STATUS_FILLED = 2;
  INTENT_ENTRY_TRIGGER_STATUS_CANCELLED = 3;
}

enum LTPConditionKind {
  LTP_CONDITION_KIND_INVALID = 0;
  LTP_CONDITION_KIND_ABOVE = 1;
  LTP_CONDITION_KIND_BELOW = 2;
  LTP_CONDITION_KIND_AT_OR_ABOVE = 3;
  LTP_CONDITION_KIND_AT_OR_BELOW = 4;
}

enum ConditionOperator {
  CONDITION_OPERATOR_INVALID = 0;
  CONDITION_OPERATOR_AND = 1;
  CONDITION_OPERATOR_OR = 2;
}

enum OrderSide {
  ORDER_SIDE_INVALID = 0;
  ORDER_SIDE_BUY = 1;
  ORDER_SIDE_SELL = 2;
}

enum OrderDeliveryType {
  ORDER_DELIVERY_TYPE_INVALID = 0;
  ORDER_DELIVERY_TYPE_CNC = 1;
  ORDER_DELIVERY_TYPE_IDAY = 2;
}

enum PriceType {
  PRICE_TYPE_INVALID = 0;
  PRICE_TYPE_LIMIT = 1;
  PRICE_TYPE_MARKET = 2;
}

enum ValidityType {
  VALIDITY_TYPE_INVALID = 0;
  VALIDITY_TYPE_DAY = 1;
  VALIDITY_TYPE_IOC = 2;
}
```

!!! note "Price type compatibility"
    The realtime protocol exposes `PRICE_TYPE_MARKET` because Trading API V3 supports market-capable flows too. Keep websocket decoding aligned with the same placement rules documented elsewhere in this V3 track, including `MARKET` with `IOC`.

<a id="page-trading-realtime-order-updates--v3-routing-logic"></a>
## V3 Routing Logic

After decoding `NubraToClientIntentUpdate`:

| Condition | Treat as | Meaning |
| --- | --- | --- |
| `intentOrderResponse.tradeFill` is present and has `tradeQty` | trade update | Fill event. |
| `intentOrderResponse.tradeFill` is absent | order update | Non-fill intent-order event. |

Use the embedded intent order response when the application needs the full order snapshot from the update.

In practice, many integrations start by printing the entire decoded `NubraToClientIntentUpdate` object and then progressively reading fields such as `intentOrderResponse.intentOrderId`, `intentOrderResponse.orderStatus`, `intentOrderResponse.tradeFill`, and `intentOrderResponse.legs`.

<a id="page-trading-realtime-order-updates--v3-wrapper-fields"></a>
## V3 Wrapper Fields

| Field | Type | Meaning |
| --- | --- | --- |
| `intentOrderResponse` | `IntentOrderResponse` | Full Trading API V3 order snapshot embedded in the update. |
| `intentOrderResponseType` | `string` | Update type such as accept, reject, fill, entry-triggered, exit-triggered, trail-updated, executed, or unsolicited cancel. |
| `intentOrderRequstType` | `string` | Request category such as new, modify, or cancel. This is the raw protocol JSON field spelling. |

<a id="page-trading-realtime-order-updates--intent-order-response-fields"></a>
## Intent Order Response Fields

| Field | Type | Meaning |
| --- | --- | --- |
| `intentOrderResponse.intentOrderId` | `int` | Trading API V3 order identifier. |
| `intentOrderResponse.orderStatus` | `string` | Current order status. |
| `intentOrderResponse.intentOrderType` | `string` | Intent order type. |
| `intentOrderResponse.isMulti` | `bool` | Whether the update is for a strategy order. |
| `intentOrderResponse.refId` | `int` | Single-leg reference ID when returned. |
| `intentOrderResponse.refdata` | `object` | Instrument metadata. |
| `intentOrderResponse.legs` | `array` | Strategy order leg details. |
| `intentOrderResponse.orderSide` | `string` | Strategy or order side when returned. |
| `intentOrderResponse.deliveryType` | `string` | Delivery type. |
| `intentOrderResponse.priceType` | `string` | Price type. |
| `intentOrderResponse.validityType` | `string` | Validity type. |
| `intentOrderResponse.goodTillDate` | `int` | Good-till date/time when returned. |
| `intentOrderResponse.executionMode` | `string` | Execution mode. |
| `intentOrderResponse.entryPrice` | `int` | Entry price. |
| `intentOrderResponse.orderPrice` | `int` | Order price. |
| `intentOrderResponse.ltp` | `int` | Latest traded price. |
| `intentOrderResponse.orderQty` | `int` | Order quantity. |
| `intentOrderResponse.filledQty` | `int` | Filled quantity. |
| `intentOrderResponse.filledPrice` | `int` | Filled price. |
| `intentOrderResponse.filledAt` | `int` | Fill timestamp. |
| `intentOrderResponse.expiryTime` | `int` | Expiry timestamp. |
| `intentOrderResponse.entryConfig` | `object` | Entry trigger or timed-entry state. |
| `intentOrderResponse.exitTriggers` | `array` | Stop-loss, target, trailing, or timed-exit trigger state. |
| `intentOrderResponse.icebergInfo` | `object` | Iceberg slicing fields when returned. |
| `intentOrderResponse.tradeFill` | `object` | Fill details when present. |
| `intentOrderResponse.nubraTimestamps` | `object` | Lifecycle timestamps. |
| `intentOrderResponse.positionId` | `string` | Linked position ID when available. |
| `intentOrderResponse.stratTags` | `string[]` | Strategy tags. |
| `intentOrderResponse.echoFields` | `string` | Echo metadata. |
| `intentOrderResponse.rejectionMsg` | `string` | Rejection reason when rejected. |

<a id="page-trading-realtime-order-updates--nested-fields"></a>
## Nested Fields

<a id="page-trading-realtime-order-updates--trade-fill"></a>
### Trade Fill

| Field | Meaning |
| --- | --- |
| `tradeFill.refId` | Filled instrument reference ID. |
| `tradeFill.tradeQty` | Filled trade quantity. |
| `tradeFill.tradePrice` | Filled trade price. |

<a id="page-trading-realtime-order-updates--entry-config"></a>
### Entry Config

| Field | Meaning |
| --- | --- |
| `entryConfig.entryTime` | Timed entry timestamp. |
| `entryConfig.conditionOperator` | Condition operator when multiple conditions are present. |
| `entryConfig.conditions[].kind.ltpConditionKind` | Entry LTP condition kind. |
| `entryConfig.conditions[].threshold` | Entry condition threshold. |
| `entryConfig.conditions[].status` | Entry condition status. |

<a id="page-trading-realtime-order-updates--exit-triggers"></a>
### Exit Triggers

| Field | Meaning |
| --- | --- |
| `exitTriggers[].kind` | Trigger kind such as stop-loss, target profit, trailing stop, or exit time. |
| `exitTriggers[].conditionKind` | Condition kind. |
| `exitTriggers[].triggerPrice` | Trigger price. |
| `exitTriggers[].limitPrice` | Limit price. |
| `exitTriggers[].trailJump` | Trailing stop jump. |
| `exitTriggers[].status` | Exit trigger status. |
| `exitTriggers[].algoTriggerPrice` | Algorithm trigger price when returned. |
| `exitTriggers[].algoLimitPrice` | Algorithm limit price when returned. |
| `exitTriggers[].exitTime` | Timed-exit timestamp. |

<a id="page-trading-realtime-order-updates--legs"></a>
### Legs

| Field | Meaning |
| --- | --- |
| `legs[].refId` | Leg reference ID. |
| `legs[].unitQty` | Signed leg quantity; positive values are buy legs and negative values are sell legs. |
| `legs[].orderQty` | Leg order quantity. |
| `legs[].filledQty` | Leg filled quantity. |
| `legs[].filledPrice` | Leg fill price. |
| `legs[].refdata` | Leg instrument metadata. |

<a id="page-trading-realtime-order-updates--lifecycle-timestamps"></a>
### Lifecycle Timestamps

| Field | Meaning |
| --- | --- |
| `nubraTimestamps.intentCreatedAt` | Intent order creation timestamp. |
| `nubraTimestamps.sentToColoAt` | Time sent to execution layer. |
| `nubraTimestamps.filledAt` | Fill timestamp. |
| `nubraTimestamps.cancelledAt` | Cancellation timestamp. |
| `nubraTimestamps.lastModifiedAt` | Last modification timestamp. |

<a id="page-trading-realtime-order-updates--v3-event-types"></a>
## V3 Event Types

| Field | Values |
| --- | --- |
| `intentOrderResponseType` | `INTENT_ORDER_RESPONSE_TYPE_ACCEPT`, `INTENT_ORDER_RESPONSE_TYPE_REJECT`, `INTENT_ORDER_RESPONSE_TYPE_FILLED`, `INTENT_ORDER_RESPONSE_TYPE_ENTRY_TRIGGERED`, `INTENT_ORDER_RESPONSE_TYPE_EXIT_SL_TRIGGERED`, `INTENT_ORDER_RESPONSE_TYPE_EXIT_TP_TRIGGERED`, `INTENT_ORDER_RESPONSE_TYPE_TRAIL_UPDATED`, `INTENT_ORDER_RESPONSE_TYPE_EXECUTED`, `INTENT_ORDER_RESPONSE_TYPE_UNSOLICITED_CANCEL` |
| `intentOrderRequstType` | `INTENT_ORDER_REQUEST_TYPE_NEW`, `INTENT_ORDER_REQUEST_TYPE_MOD`, `INTENT_ORDER_REQUEST_TYPE_CANCEL` |
| `orderStatus` | `INTENT_ORDER_STATUS_OPEN`, `INTENT_ORDER_STATUS_EXECUTED`, `INTENT_ORDER_STATUS_CANCELLED`, `INTENT_ORDER_STATUS_REJECTED`, `INTENT_ORDER_STATUS_GTE`, `INTENT_ORDER_STATUS_EXPIRED` |

<a id="page-trading-realtime-order-updates--example-json"></a>
## Example JSON

This is an example of the decoded message shape after protobuf decoding.

```json
{
  "intentOrderResponseType": "INTENT_ORDER_RESPONSE_TYPE_ACCEPT",
  "intentOrderRequstType": "INTENT_ORDER_REQUEST_TYPE_NEW",
  "intentOrderResponse": {
    "intentOrderId": 987654,
    "orderStatus": "INTENT_ORDER_STATUS_OPEN",
    "isMulti": false,
    "refId": 1842210,
    "deliveryType": "IDAY",
    "priceType": "LIMIT",
    "validityType": "DAY",
    "executionMode": "ENTRY",
    "entryPrice": 24600,
    "orderQty": 1,
    "filledQty": 0,
    "rejectionMsg": null
  }
}
```

<a id="page-trading-realtime-order-updates--important-rules"></a>
## Important Rules

!!! important-rules "Important Rules"
    - This is a realtime streaming feed, not a snapshot API.
    - Send `subscribe <session_token> notifications notification` after opening the WebSocket.
    - For Trading API V3, decode inner protobuf messages whose type URL ends with `NubraToClientIntentUpdate`.
    - Use `intentOrderResponse.tradeFill` to identify V3 fill events.
    - For strategy orders, inspect `intentOrderResponse.legs[]`; the strategy still has one `intentOrderId`.
    - Price fields such as `entryPrice`, `orderPrice`, `filledPrice`, `tradePrice`, and `ltp` are typically returned in exchange-native integer units such as paise for NSE instruments.
    - For first-pass validation, print the full decoded event object before reducing it to selected fields.
    - Keep the process alive with your own long-lived WebSocket loop.
    - Use [Get Orders](#page-trading-orders-get-order) when you need a fetched snapshot of current order state instead of a live stream.

<a id="page-trading-realtime-order-updates--what-to-read-next"></a>
## What To Read Next

1. [Get Orders](#page-trading-orders-get-order)
2. [Place Single Order](#page-trading-orders-place-order)
3. [Modify Order](#page-trading-orders-modify-order)
4. [Cancel Order](#page-trading-orders-cancel-order)

---

Source: docs/rest-api-v3/trading/orders/get-margin.md

<a id="page-trading-orders-get-margin"></a>
<a id="page-trading-orders-get-margin--get-order-margin"></a>
## Get Order Margin

Use this page to estimate Trading API V3 funds and margin requirements before placing an order.

Estimate funds before placing:

- one single-instrument order
- multiple independent single-instrument orders
- one strategy order

The request payload uses the same Trading API V3 order fields as:

- [Place Single Order](#page-trading-orders-place-order)
- [Place Multi Order](#page-trading-orders-place-basket-order)
- [Place Strategy Order](#page-trading-orders-place-flexi-order)

Add only the top-level `requestType` field for the margin-estimation call.

<a id="page-trading-orders-get-margin--endpoint"></a>
## Endpoint

```text
Method: POST
Endpoint: sentinel/orders/funds_required
```

<a id="page-trading-orders-get-margin--basic-usage"></a>
## Basic Usage

```bash
curl --location 'https://uatapi.nubra.io/sentinel/orders/funds_required' \
--header 'Authorization: Bearer {{session_token}}' \
--header 'x-device-id: {{x_device_id}}' \
--header 'x-app-version: 0.4.5' \
--header 'x-device-os: sdk' \
--header 'Cookie: deviceId={{x_device_id}}' \
--header 'Content-Type: application/json' \
--data '{
  "requestType": "NEW",
  "orders": [
    {
      "refId": 72329,
      "qty": 1,
      "side": "BUY",
      "deliveryType": "IDAY",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "isMultiLeg": false,
      "executionMode": "ENTRY",
      "entryPrice": 127000,
      "stratTags": ["rest-api-v3", "single-margin"]
    }
  ]
}'
```

<a id="page-trading-orders-get-margin--example-margin-patterns"></a>
## Example Margin Patterns

<a id="page-trading-orders-get-margin--single-order"></a>
### Single Order

```json
{
  "requestType": "NEW",
  "orders": [
    {
      "refId": 72329,
      "qty": 1,
      "side": "BUY",
      "deliveryType": "IDAY",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "isMultiLeg": false,
      "executionMode": "ENTRY",
      "entryPrice": 127000,
      "stratTags": ["rest-api-v3", "single-margin"]
    }
  ]
}
```

<a id="page-trading-orders-get-margin--strategy-order"></a>
### Strategy Order

Use the same base-quantity model as strategy placement. The top-level `qty` is the common executable base quantity, and each `legs[].unitQty` value is the per-leg multiplier.

```json
{
  "requestType": "NEW",
  "orders": [
    {
      "isMultiLeg": true,
      "qty": 65,
      "side": "BUY",
      "deliveryType": "CNC",
      "priceType": "LIMIT",
      "validityType": "DAY",
      "executionMode": "ENTRY",
      "entryPrice": 44935,
      "legs": [
        { "refId": 1497712, "unitQty": 1 },
        { "refId": 1497713, "unitQty": 1 }
      ],
      "stratTags": ["rest-api-v3", "strategy-margin"]
    }
  ]
}
```

This validated strategy-margin example corresponds to:

- nearest validated expiry: `20260616`
- strike: `23600`
- CE leg: `1497712`
- PE leg: `1497713`
- top-level strategy base quantity: `65`
- each leg multiplier: `1`
- net entry price used in validation: `44935`

<a id="page-trading-orders-get-margin--request-contract"></a>
## Request Contract

| Field | Type | Required | Meaning |
| --- | --- | --- | --- |
| `requestType` | string | Yes | Use `NEW` when estimating funds for a new order before placement |
| `orders` | array | Yes | Trading API V3 order payloads to estimate |
| `orders[].refId` | int | Conditional | Single-order instrument reference id. Omit for strategy orders |
| `orders[].qty` | int | Yes | Single-order quantity or the common executable base quantity for a strategy |
| `orders[].side` | string | Yes | `BUY` or `SELL` |
| `orders[].deliveryType` | string | Yes | `IDAY` or `CNC` |
| `orders[].priceType` | string | Yes | `LIMIT` or `MARKET` |
| `orders[].validityType` | string | Yes | `DAY`, `IOC`, or `GTE` |
| `orders[].isMultiLeg` | bool | Yes | `false` for independent orders, `true` for strategy orders |
| `orders[].executionMode` | string | Yes | `ENTRY`, `EXIT`, or `ENTRY_AND_EXIT` |
| `orders[].entryPrice` | int | Conditional | Entry price or strategy net entry price |
| `orders[].legs` | array | Conditional | Required for strategy-order margin checks |
| `orders[].legs[].refId` | int | Yes for leg | FNO instrument reference id |
| `orders[].legs[].unitQty` | int | Yes for leg | Leg multiplier |

<a id="page-trading-orders-get-margin--condition-fields"></a>
## Condition Fields

| Field | Type | Description |
| --- | --- | --- |
| `entryConfig.triggers.*` | object | Entry trigger controls |
| `entryConfig.entryTime` | string | Timed entry |
| `exitConfig.stoplossParams.*` | object | Stop-loss controls |
| `exitConfig.targetParams.*` | object | Target controls |
| `exitConfig.exitTime` | string | Timed exit |

<a id="page-trading-orders-get-margin--response-contract"></a>
## Response Contract

The margin response includes both funds and charge information.

Validated output in this track included:

- `totalFundsRequired: 13565`
- `marginInfo.totalMargin: 0`

That means the selected example produced a charges-only requirement in that validation run, not an additional blocked strategy margin component.

```json
{
  "code": 1,
  "marginInfo": {
    "totalMargin": 0,
    "message": null
  },
  "brokerageInfo": {
    "totalChargesFloat": 13565.63879385
  },
  "totalFundsRequired": 13565,
  "willDefaultBePlacedAsAmo": true,
  "willBeAutoSliced": false
}
```

<a id="page-trading-orders-get-margin--margininfo"></a>
### `marginInfo`

| Field | Meaning |
| --- | --- |
| `totalMargin` | Final margin component calculated by the engine |
| `message` | Optional engine message |

<a id="page-trading-orders-get-margin--brokerageinfo"></a>
### `brokerageInfo`

| Field | Meaning |
| --- | --- |
| `totalChargesFloat` | Total estimated charges as a float before rounding in the top-level response |

<a id="page-trading-orders-get-margin--important-rules"></a>
## Important Rules

- Margin estimation does not place an order. It only evaluates the payload and returns estimated funds and charges.
- For strategy orders, keep `qty` and `legs[].unitQty` aligned with the placement payload you intend to use.
- There is no separate basket-level multiplier field in the margin request. Scale the full strategy by changing the top-level base quantity.
- If you want to cross-check the example in the UI, validate the same CE and PE instruments, expiry, strike, side, and net entry price.

<a id="page-trading-orders-get-margin--what-to-read-next"></a>
## What To Read Next

- [Place Single Order](#page-trading-orders-place-order)
- [Place Strategy Order](#page-trading-orders-place-flexi-order)
- [Get Orders](#page-trading-orders-get-order)

---

Source: docs/rest-api-v3/trading/portfolio/holdings.md

<a id="page-trading-portfolio-holdings"></a>
<a id="page-trading-portfolio-holdings--holdings"></a>
## Holdings

Provides a detailed snapshot of all active holdings in the demat account, including invested value, current market value, day and overall PnL (both absolute and percentage), margin benefit, haircut, and pledge availability for each stock. Also includes client-level statistics such as total investment, net PnL, and daily PnL performance.

```jsx
Method: GET
Endpoint: sentinel/portfolio/holdings
```
<a id="page-trading-portfolio-holdings--curl"></a>
### cURL
```bash
curl --location 'https://uatapi.nubra.io/sentinel/portfolio/holdings' \
--header 'x-device-id: TS123' \
--header 'Authorization: Bearer eyJh...6Pno' \
```

**Response Structure**

```jsx
{
    "message": "holdings",
    "portfolio": {
        "client_code": "ZRL001",
        "holding_stats": {
            "invested_amount": 743039,
            "current_value": 763165,
            "total_pnl": 20126,
            "total_pnl_chg": 2.7086062,
            "day_pnl": -31795,
            "day_pnl_chg": -3.9995723
        },
        "holdings": [
            {
                "ref_id": 83414,
                "nubra_name": "STOCK_TVSMOTOR.NSECM",
                "displayName": "TVSMOTOR",
                "derivative_type": "STOCK",
                "strike_price": 0,
                "lot_size": 1,
                "exchange": "NSE",
                "asset": "TVSMOTOR",
                "symbol": "TVSMOTOR",
                "qty": 1,
                "pledged_qty": 0,
                "t1_qty": 0,
                "avg_price": 245292,
                "prev_close": 273790,
                "ltp": 246625,
                "ltp_chg": -9.921838,
                "invested_value": 245292,
                "current_value": 246625,
                "net_pnl": 1333,
                "net_pnl_chg": 0.54343396,
                "day_pnl": -27165,
                "haircut": 14.93,
                "margin_benefit": 209803
                "available_to_pledge":1
                "is_pledgeable": true,
                "supported_exchanges": {
                    "BSE": 847854,
                    "NSE": 73082}
            }
        ]
    }
}
```

**Response Attributes**

| **Fields** | **Description** |
| --- | --- |
| `message` | Response message |
| `portfolio.client_code` | Unique client code linked to the demat account |
| `portfolio.holding_stats.invested_amount` | Total capital invested across all holdings |
| `portfolio.holding_stats.current_value` | Current market value of all holdings |
| `portfolio.holding_stats.total_pnl` | Total profit or loss (absolute value) |
| `portfolio.holding_stats.total_pnl_chg` | Total profit or loss percentage |
| `portfolio.holding_stats.day_pnl` | Intraday mark-to-market profit or loss |
| `portfolio.holding_stats.day_pnl_chg` | Intraday profit or loss percentage |
| `portfolio.holdings[].ref_id` | Internal reference ID for the instrument |
| `portfolio.holdings[].nubra_name` | Full instrument name used in Nubra |
| `portfolio.holdings[].displayName` | Display name of the holding shown in UI |
| `portfolio.holdings[].derivative_type` | Type of instrument (e.g., FUT, OPT, EQ) |
| `portfolio.holdings[].strike_price` | Strike price (if applicable) |
| `portfolio.holdings[].lot_size` | Lot size of the instrument |
| `portfolio.holdings[].exchange` | Exchange where the instrument is listed (e.g., NSE, BSE) |
| `portfolio.holdings[].asset` | Asset class (Equity, Derivative, etc.) |
| `portfolio.holdings[].symbol` | Trading symbol of the holding |
| `portfolio.holdings[].quantity` | Total quantity currently held |
| `portfolio.holdings[].pledged_qty` | Quantity pledged as collateral |
| `portfolio.holdings[].t1_qty` | T+1 unsettled quantity |
| `portfolio.holdings[].avg_price` | Average acquisition price |
| `portfolio.holdings[].prev_close` | Previous closing price |
| `portfolio.holdings[].last_traded_price` | Most recent traded price |
| `portfolio.holdings[].last_traded_price_change` | % change in LTP from previous close |
| `portfolio.holdings[].invested_value` | Total invested value in this holding |
| `portfolio.holdings[].current_value` | Current market value of this holding |
| `portfolio.holdings[].net_pnl` | Net profit or loss for this holding |
| `portfolio.holdings[].net_pnl_chg` | Net profit/loss percentage |
| `portfolio.holdings[].day_pnl` | Intraday profit or loss |
| `portfolio.holdings[].haircut` | Haircut percentage applied to pledged value |
| `portfolio.holdings[].margin_benefit` | Margin benefit available from pledge |
| `portfolio.holdings[].available_to_pledge` | Quantity that can still be pledged |
| `portfolio.holdings[].is_pledgeable` | Available to pledge |

---

Source: docs/rest-api-v3/trading/portfolio/positions.md

<a id="page-trading-portfolio-positions"></a>
<a id="page-trading-portfolio-positions--positions"></a>
## Positions

Returns open and closed positions across stocks, futures, and options. Includes key details like symbol, quantity, average prices, last traded price, order side, and a comprehensive PnL breakdown — including realised, unrealised, and total PnL with percentage changes.

```jsx
Method: GET
Endpoint: sentinel/portfolio/positions
```

<a id="page-trading-portfolio-positions--curl"></a>
### cURL
```bash
curl --location 'https://uatapi.nubra.io/sentinel/portfolio/positions' \
--header 'x-device-id: TS123' \
--header 'Authorization: Bearer eyJh...6Pno' \
```

<a id="page-trading-portfolio-positions--response-structure"></a>
### Response Structure

```jsx
{
    "message": "positions",
    "portfolio": {
        "client_code": "XXXXXX",
        "position_stats": {
            "realised_pnl": 0,
            "unrealised_pnl": 0,
            "total_pnl": -75180,
            "total_pnl_chg": -35.191193
        },
        "stock_positions": [
            {
                "ref_id": 847854,
                "zanskar_name": "STOCK_YESBANK_EQ_A.BSECM",
                "display_name": "YESBANK",
                "derivative_type": "STOCK",
                "strike_price": 0,
                "lot_size": 1,
                "exchange": "BSE",
                "asset": "YESBANK",
                "symbol": "YESBANK",
                "product": "ORDER_DELIVERY_TYPE_CNC",
                "order_side": "BUY",
                "qty": 1,
                "ltp": 1853,
                "avg_price": 1868,
                "avg_buy_price": 1868,
                "avg_sell_price": 0,
                "pnl": -15,
                "pnl_chg": -0.8029979
            },
        ],
        "fut_positions": null,
        "opt_positions": null,
        "close_positions": [
            {
                "ref_id": 808198,
                "zanskar_name": "OPT_NIFTY_20250814_PE_2445000",
                "display_name": "NIFTY 14 Aug 24450 PE",
                "derivative_type": "OPT",
                "strike_price": 2445000,
                "lot_size": 75,
                "exchange": "NSE",
                "asset": "NIFTY",
                "symbol": "NIFTY2581424450PE",
                "product": "ORDER_DELIVERY_TYPE_IDAY",
                "order_side": "C",
                "qty": 225,
                "ltp": 15195,
                "avg_price": 12010,
                "avg_buy_price": 12473,
                "avg_sell_price": 12010,
                "pnl": -104175,
                "pnl_chg": 0
            }
        ]
    }
}
```

<a id="page-trading-portfolio-positions--response-attributes"></a>
### Response Attributes

| **Field** | **Description** |
| --- | --- |
| `message` | Response message |
| `portfolio.client_code` | Unique client code linked to the demat account |
| `portfolio.position_stats.realised_pnl` | Realised profit or loss |
| `portfolio.position_stats.unrealised_pnl` | Unrealised profit or loss |
| `portfolio.position_stats.total_pnl` | Total profit or loss (absolute value) |
| `portfolio.position_stats.total_pnl_chg` | Total profit or loss percentage |
| `portfolio.stock_positions[].ref_id` | Internal reference ID for the instrument |
| `portfolio.stock_positions[].zanskar_name` | Full instrument name used by Nubra |
| `portfolio.stock_positions[].display_name` | Display name of the position shown in UI |
| `portfolio.stock_positions[].derivative_type` | Type of instrument (e.g., FUT, OPT, EQ) |
| `portfolio.stock_positions[].strike_price` | Strike price (if applicable) |
| `portfolio.stock_positions[].lot_size` | Lot size of the instrument |
| `portfolio.stock_positions[].exchange` | Exchange where the instrument is listed (e.g., NSE, BSE) |
| `portfolio.stock_positions[].asset` | Asset class (Equity, Derivative, etc.) |
| `portfolio.stock_positions[].symbol` | Trading symbol of the position |
| `portfolio.stock_positions[].product` | Product type (CNC, MIS, etc.) |
| `portfolio.stock_positions[].order_side` | Buy or Sell side |
| `portfolio.stock_positions[].quantity` | Total quantity in position |
| `portfolio.stock_positions[].last_traded_price` | Most recent traded price |
| `portfolio.stock_positions[].avg_price` | Average price of the position |
| `portfolio.stock_positions[].avg_buy_price` | Average buy price |
| `portfolio.stock_positions[].avg_sell_price` | Average sell price |
| `portfolio.stock_positions[].pnl` | Profit or loss for this position |
| `portfolio.stock_positions[].pnl_chg` | Profit/loss percentage |

---

Source: docs/rest-api-v3/trading/portfolio/funds.md

<a id="page-trading-portfolio-funds"></a>
<a id="page-trading-portfolio-funds--funds"></a>
## Funds

Provides live cash and margin breakdown including blocked funds, margin used, collateral pledged and available balance.

```jsx
Method: GET
Endpoint: sentinel/portfolio/user_funds_and_margin
```
<a id="page-trading-portfolio-funds--curl"></a>
### cURL
```bash
curl --location 'https://uatapi.nubra.io/sentinel/portfolio/user_funds_and_margin' \
--header 'x-device-id: TS123' \
--header 'Authorization: Bearer eyJh...6Pno' \
```

<a id="page-trading-portfolio-funds--response-structure"></a>
### Response Structure

```jsx
{
    "message": "portfolio and funds values fetched successfully",
    "port_funds_and_margin": {
        "client_code": "XXXXX",
        "start_of_day_funds": 2888888,
        "pay_in_credit": 0,
        "pay_out_debit": 0,
        "net_derivative_prem_buy": 5612625,
        "net_derivative_prem_sell": 5538000,
        "net_derivative_prem": -74625,
        "cash_blocked_cnc_traded": 1868,
        "cash_blocked_cnc_open": 0,
        "cash_blocked_deriv_open": 0,
        "cash_cnc_traded_and_open": 1868,
        "mtm_deriv": -74625,
        "mtm_eq_iday_cnc": -555,
        "mtm_eq_delivery": -222027,
        "net_trading_amount": 28680916,
        "net_withdrawal_amount": 23115099,
        "total_payin_cash": 0,
        "start_of_day_collateral": 0,
        "iday_collateral_pledge": 0,
        "iday_collateral_pledge_sell": 0,
        "total_collateral": 0,
        "margin_used_deriv_traded": 0,
        "margin_block_deriv_open_order": 0,
        "margin_used_eq_iday": 27817,
        "margin_blocked_eq_iday_open": 0,
        "net_margin_available": 28653099,
        "total_margin_blocked": 27817,
        "derivative_margin_blocked": 0,
        "brokerage": 18788
    }
}
```

<a id="page-trading-portfolio-funds--response-attributes"></a>
### Response Attributes

| **Field** | **Description** |
| --- | --- |
| `message` | Response message |
| `portfolio.client_code` | Unique client code linked to the demat account |
| `portfolio.funds.available_balance` | Available cash balance for trading |
| `portfolio.funds.blocked_amount` | Amount blocked for pending orders |
| `portfolio.funds.margin_used` | Margin currently being used |
| `portfolio.funds.collateral_pledged` | Value of securities pledged as collateral |
| `portfolio.funds.total_balance` | Total account balance |
