# Introduction

Overview of the Samco Trade API — setup flow, supported runtimes, base URLs, and the master contract file.

## Overview

Samco Trade API lets you integrate trading, market data, and account management into your own applications. This page describes the recommended setup flow using the current APIs.

---

### Quick Start

#### Step 1 — Create an OAuth App (One-Time Setup)

All API access starts with an **OAuth App**. Log in to the [Web Dashboard](https://tradeapi.samco.in/app/login) using your Samco Client ID and create an app to obtain:

- **API Key** — delivered to your registered email address.
- **API Secret** — shown **once** in the dashboard; copy it immediately and store it securely.

> Detailed steps: [Web Dashboard Guide](03-dashboard.md#dashboard-user-manual)

#### Step 2 — Register a Static IP (One-Time Setup)

Register the IP address(es) your server will call from under **Static IPs** in the dashboard. Requests from unregistered IPs are rejected by order-related APIs.

> Detailed steps: [Web Dashboard Guide — Static IPs](03-dashboard.md#static-ips)

#### Step 3 — Obtain a Session Token

Choose the flow that fits your integration:

| Flow | When to use | How |
| --- | --- | --- |
| **Direct** (`POST /session/token`) | Backend / server-to-server — your own `apiKey` + `apiSecret`, no browser involved | [Generate Session Token](04-authentication.md#generate-session-token) |
| **OAuth 2.1** (authorization-code) | Third-party apps authenticating end-users through a browser | [OAuth 2.1 Authorization-Code Flow](04-authentication.md#oauth-21-authorization-code-flow) |

The session token is a **JWT** returned by both flows. Send it as the `x-session-token` header on all subsequent API calls. It is valid until **08:00 IST the next day**.

#### Step 4 — Call the APIs

With a valid `x-session-token` you can call:

- [Orders](08-orders.md#place-order), [Order Book](08-orders.md#order-book), [Trade Book](11-portfolio.md#trade-book)
- [Positions](11-portfolio.md#user-positions), [Holdings](11-portfolio.md#user-holdings), [User Limit](06-account-and-limits.md#user-limits)
- [Quote](07-market-data.md#get-quote), [Option Chain](07-market-data.md#option-chain), [Future Chain](07-market-data.md#future-chain)
- [GTT Orders](09-gtt-orders.md#gtt), [Basket Orders](10-basket-orders.md#introducing-the-new-basket-order-api-feature)
- [Intraday](12-candle-data.md#intraday-candle-data) & [Historical Candle Data](12-candle-data.md#historical-candle-data)
- [Streaming Market Data](13-streaming-data.md#streaming-market-data)
- [Personal Index](06-account-and-limits.md#personal-index), [Market Depth](07-market-data.md#market-depth), [Contract Analyser](07-market-data.md#contract-analyser), [Span Margin](08-orders.md#span-margin)
- [Trade View Analytics](14-analytics.md#analytics-summary-api)

---

### Supported Client Runtimes

Samco tests the v3.2 code samples against the following runtime floors. Older versions may work but are not supported.

| Language | Minimum Version | Library Used |
| --- | --- | --- |
| cURL | Any modern shell (`bash` / `zsh`) | — (single-quote JSON bodies) |
| Java | JDK 17 LTS+ | Built-in `java.net.http.HttpClient` (REST) and `java.net.http.WebSocket` (streaming) |
| Node.js | Node 22 LTS+ | Built-in `fetch` (REST); `ws` package for streaming |
| Python | Python 3.8+ | `requests` (REST); `websocket-client` (streaming) |

---

### Token Lifetime

> **INFO** — Session token expiry
>
> All session tokens — regardless of how they were obtained — expire at **08:00 IST the next calendar day**. Refresh by calling `POST /session/token` again or by repeating the OAuth Login flow.

---

### Deprecated APIs

The following APIs from the legacy flow are **deprecated**. They continue to work during a transition period but will be removed in a future release. Migrate to the current equivalents listed above.

| Deprecated API | Replacement |
| --- | --- |
| `POST /login` | Not required with the new session token flow |
| `POST /login2FA/generateOTP` | OTP is handled by the Web Dashboard |
| `POST /login2FA/generateSecretApiKey` | API Secret is generated in the Web Dashboard |
| `POST /login2FA/generateAccessToken` | [`POST /session/token`](04-authentication.md#generate-session-token) |
| `POST /ip/ipRegistration` | [Web Dashboard — Static IPs](03-dashboard.md#static-ips) |
| `POST /ip/ipUpdate` | [Web Dashboard — Static IPs](03-dashboard.md#static-ips) |
