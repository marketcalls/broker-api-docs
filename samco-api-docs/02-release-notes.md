# Release Notes

What changed in the current release of the Samco Trade API.

## Trade API v3.2.0 — Release Notes

*Released: 08 June 2026*

Samco Trade API **v3.2.0** is now available. In this release, authentication moves away from User ID + Password to **API Key + API Secret** credentials — you can issue up to **5 key/secret pairs per account** and use them with `POST /session/token`. The release also adds a standards-based **OAuth 2.1 Authorization-Code flow** and a self-service **Web Dashboard** to create OAuth apps, manage your API Key / API Secret, register Static IPs, and verify your request IP (also available programmatically via `GET /ip/whoami`). The legacy 4-step login (`/login` → OTP → secret key → access token) continues to work but is now deprecated. New integrations should migrate to the v3.2 endpoints below.

> **TIP** — Highlights
>
> - **Generate Session Token (Direct)** — authentication using your **API Key + API Secret** via `POST /session/token`.
> - **OAuth 2.1 Authorization-Code Flow** — browser-based login at `https://tradeapi.samco.in/app/oauth/authorize`.
> - **Samco Trade API Web Dashboard** — create OAuth apps, manage API Key / API Secret, register Static IPs, and verify the request IP your integration is sending (also available programmatically via `GET /ip/whoami` — helpful while configuring Static IP allow-lists).
> - **Refreshed documentation with ready-to-run code samples** — every v3.2 endpoint now ships side-by-side examples in **cURL**, **Node.js**, **Java**, and **Python**, covering both direct execution and the matching official SDKs.

### What's New

| Feature | Endpoint / Page | Documentation |
| --- | --- | --- |
| Generate Session Token (Direct) | `POST /session/token` | [Session Token](04-authentication.md#generate-session-token) |
| OAuth 2.1 Authorization-Code Flow | `https://tradeapi.samco.in/app/oauth/authorize` | [OAuth 2.1 Flow](04-authentication.md#oauth-21-authorization-code-flow) |
| Web Dashboard — Documentation | [`https://docs-tradeapi.samco.in/dashboard/user-manual.html`](03-dashboard.md#dashboard-user-manual) | [Dashboard User Manual](03-dashboard.md#dashboard-user-manual) |
| Web Dashboard — Login | [`https://tradeapi.samco.in/app/login`](https://tradeapi.samco.in/app/login) | [Dashboard User Manual](03-dashboard.md#dashboard-user-manual) |
| Web Dashboard — API Keys | [`https://tradeapi.samco.in/app/api-keys`](https://tradeapi.samco.in/app/api-keys) | [API Keys](03-dashboard.md#api-keys) |
| Web Dashboard — Static IPs | [`https://tradeapi.samco.in/app/static-ips`](https://tradeapi.samco.in/app/static-ips) | [Static IPs](03-dashboard.md#static-ips) |
| IP Diagnostics — Who Am I | `GET /ip/whoami` | [Who Am I](05-ip-diagnostics.md#who-am-i) |

### Improvements

- **Code samples for every endpoint in four languages.** Every endpoint in the v3.2 reference now ships side-by-side examples in **cURL**, **Node.js**, **Java**, and **Python** — each one showing both the direct HTTP call and the equivalent idiomatic usage through the matching official SDK, so you can pick whichever fits your integration.
- **Runnable sample client in every official SDK.** The Java, Node.js, and Python SDKs each ship a complete sample client that walks through authenticating, calling the REST endpoints, and subscribing to the streaming quote / market-data feeds — clone, set credentials, and run.
- **`/webSecretCodeValidation` now returns Source-IP fields.** The legacy auth-validation endpoint now includes `srcIp`, `primaryIp`, and `secondaryIp` in its response so clients can confirm the source IP the API saw.
- **IP fields default to empty string instead of `null`.** Clients should treat `""` as "not set".

### Supported Client Runtimes

Samco tests the v3.2 code samples against the following runtime floors. Older versions may work but are not supported.

| Language | Minimum Version | Library Used |
| --- | --- | --- |
| cURL | Any modern shell (`bash` / `zsh`) | — (single-quote JSON bodies) |
| Java | JDK 17 LTS+ | Built-in `java.net.http.HttpClient` (REST) and `java.net.http.WebSocket` (streaming) |
| Node.js | Node 22 LTS+ | Built-in `fetch` (REST); `ws` package for streaming |
| Python | Python 3.8+ | `requests` (REST); `websocket-client` (streaming) |

### Deprecated APIs

These endpoints still work but will be removed in a future major release. Migrate at your earliest convenience.

| API Name | Request URL |
| --- | --- |
| Login | `/login` |
| Generate OTP | `/otp/generateOtp` |
| Generate Secret Key | `/otp/secretKeyGenerator` |
| Generate Access Token | `/accessToken/token` |
| IP Register | `/ip/ipRegistration` |
| IP Update | `/ip/ipUpdate` |

> **WARNING** — Note
>
> Generate Access Token API is used to generate the access token required for the legacy login flow. New integrations should use [`/session/token`](04-authentication.md#generate-session-token) or [OAuth 2.1](04-authentication.md#oauth-21-authorization-code-flow) instead.

### Migration Guide

1. **Replace the 4-step legacy login** (`/login` → OTP → secret key → access token) with either:

   - [`POST /session/token`](04-authentication.md#generate-session-token) for direct, programmatic authentication, **or**
   - [OAuth 2.1 Authorization-Code Flow](04-authentication.md#oauth-21-authorization-code-flow) for browser-based delegated authentication.
2. **Move Static IP management** off the password-based `/ip/ipRegistration` & `/ip/ipUpdate` endpoints to the [Web Dashboard](03-dashboard.md#static-ips).
3. **Update IP-field parsing** — treat `""` (empty string) instead of `null` as "IP not set" in responses from `/oauth/token` and `/webSecretCodeValidation`.

### Documentation & Support

- [Overview](01-introduction.md#overview) — full v3.2 documentation index.
- [Raise a support ticket](https://www.samco.in/support/ticket)
- [Write on the forum](https://forum.samco.in/tag/trade_api)
- Email: [apisupport@samco.in](mailto:apisupport@samco.in)
