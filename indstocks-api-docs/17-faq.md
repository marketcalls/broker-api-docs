# FAQ

> Source: https://api-docs.indstocks.com/faq/

Condensed from the official FAQ. Where the FAQ and the endpoint pages disagree, the endpoint
pages win — see the **Caveats** section at the bottom.

## General

**Who can use INDstocks APIs?** Individual traders, algo traders, fintech developers,
institutional and quant traders with completed KYC. The API is free to access with no
subscription fees — you pay ₹5 flat brokerage per order.

**What API categories exist?** User Management & Authentication, Market Data, Order
Management, Smart Orders (GTT), Portfolio & Risk, WebSocket Streaming, and Utility APIs.

**Can I integrate with an existing platform?** Yes — either connect via an algo platform such
as Tradetron using an access token, or build directly against the REST API.

**Is there a minimum investment?** No minimum to access the APIs; you only need enough funds
for the trades you place.

## Getting Started

**Prerequisites:** an INDstocks account, completed KYC, funds for live trading, and basic
programming knowledge.

**Is there a sandbox?** **No.** There is no test environment — INDstocks recommends starting
with small quantities in the live environment.

## Authentication & Security

**How long is a token valid?** 24 hours; then generate a new one.

**Can I generate a token from a script?** Yes — set up TOTP once on the website, then call
`POST /generate/token` with your Client ID, MPIN, and current TOTP code. Only the newest token
stays valid. See [Authentication & Users](04-authentication-users.md).

**I'm locked out of TOTP generation.** Five wrong codes in 15 minutes triggers a 15-minute
lockout. Check server clock sync via NTP — clock drift is the most common cause. Existing
access tokens stay valid until their 24-hour expiry.

**I lost my authenticator phone.** The TOTP secret is shown only once. Disable TOTP through
your website account, then re-enroll for a fresh secret and QR code.

**My token is compromised.** Revoke it from the dashboard, generate a new one, update your
application, and review account activity. Report security issues to security@indstocks.com.

## Pricing

API access is free — no subscription, usage, or hidden charges. Brokerage is ₹5 per order
regardless of size. Rate limits vary by category; see
[API Conventions](03-conventions.md#rate-limits). Contact support for higher institutional
limits.

## Trading & Orders

**Why is my order rejected?** Insufficient margin, price outside circuit limits or off
tick-size, quantity not a lot-size multiple, market closed, or the instrument blocked by RMS.
See [Error Codes](14-errors.md#order-specific-errors).

**Can I place orders outside market hours?** Yes — they are queued for execution at market
open.

**How do I modify or cancel?** `POST /order/modify` with `order_id`, `qty`, `limit_price`;
`POST /order/cancel` with `order_id`.

## Market Data

**How much history is available?** 10+ years for all instruments, across 1-minute, 5-minute,
15-minute, 1-hour, and daily candles.

**REST vs WebSocket?** REST for occasional on-demand snapshots; WebSocket for continuous
low-latency streaming and high-frequency strategies.

## WebSockets

**Why does my connection drop?** Missing heartbeats (send a ping roughly every 30 seconds),
network issues (implement auto-reconnect), exceeding 3,000 instruments per connection, or
invalid authentication.

**I'm not receiving updates.** Confirm the `open` event fired, authentication succeeded, the
subscribe message is well-formed with correctly prefixed symbols, listeners are attached, and
heartbeats are being sent.

## Smart Orders (GTT)

**What are they?** Advanced conditional orders that execute automatically when their
conditions are met — single trigger, OCO (One Cancels Other), and multi-leg strategies.

**How long do they last?** Up to **365 days**, or until the trigger fires, you cancel, or the
instrument expires.

## SDKs & Integration

Official Python, JavaScript/Node.js, and Java SDKs are **in progress** — not yet released.
Until then use the REST API directly; every endpoint page carries Python, JavaScript, and cURL
examples (Java and C# "coming soon").

## Versioning

Semantic versioning; current stable version is **v1**. INDstocks states a 12-month deprecation
notice before breaking changes and a 2-year backwards-compatibility guarantee. An
`API-Version: v1` header may optionally be sent.

## Support

- Technical support: **api-support@indstocks.com**
- Security issues: **security@indstocks.com**
- Docs: https://api-docs.indstocks.com
- Developer community: coming soon

---

## Caveats

The FAQ is written loosely and contradicts the endpoint reference in several places. Trust the
endpoint pages:

| FAQ claim | Reality per the endpoint docs |
|-----------|-------------------------------|
| "Order types supported: MARKET, LIMIT, STOP_LOSS, STOP_LOSS_MARKET, GTT" | `/order` accepts only `LIMIT` and `MARKET`, and MARKET is converted to LIMIT. Stop-loss is available only through [Smart Orders](10-smart-orders.md). |
| "Send ping every 30 seconds" | The WebSocket page documents only *server*-sent heartbeats and specifies no client ping interval. |
| Symbol example `'NSE:RELIANCE'` | WebSocket instruments are `SEGMENT:TOKEN` with a **numeric** token, e.g. `NSE:2885` — not a name. |
| "Utility APIs (option chains, Greeks)" listed as available | [Utility](13-utility.md) endpoints are still marked **Coming Soon**. |
