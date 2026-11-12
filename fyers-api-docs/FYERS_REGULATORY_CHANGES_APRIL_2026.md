# FYERS — SEBI Retail Algo Trading Regulatory Changes (April 2026)

**Source:** <https://myapi.fyers.in/mandatory-regulatory-changes> (spec title:
"Regulatory Changes (April 2026)"). Captured 2026-08-31.

> **Fetching note.** `myapi.fyers.in` is a React SPA with client-side routing — a
> direct fetch of `/mandatory-regulatory-changes` or `/docsv3` returns a genuine
> HTTP 404. The rendered content comes from two Redocly OpenAPI specs referenced by
> the SPA bundle, which are the authoritative machine-readable sources:
> - `https://myapi.fyers.in/static/media/v3.1.32a8eeba1fba866d1201.yaml` → regulatory changes
>   (still the same file on 2026-09-29, so this page has not changed since capture)
> - `https://myapi.fyers.in/static/media/v3.41fe6ac3325b670b7549.yaml` → `/docsv3`
>   (replaced `v3.e760f0a0a1029ff225e0.yaml` with the 06 Sep 2026 docs release; the old
>   file is still served but stale). `regenerate_fyers_api_v3.py` in this folder reads
>   the bundle and picks up the current name by itself.
>
> The hashed filenames change on redeploy; re-extract them from the SPA bundle if
> these 404.

`FYERS_API_v3.md` links to this page four times (Rate Limits, App Creation,
Authentication & Login Flow, Order Placement Guide) but does not reproduce its
content. This file fills that gap.

## Timeline

| Date | Event |
| --- | --- |
| 31 March 2026 | Parallel-running period ends |
| **1 April 2026** | SEBI retail-algo framework enforced |
| 1 April 2026 | Refresh-token flow discontinued |

## API classification

The framework splits the API surface in two, and the obligations differ sharply.

**Transactional** — Single Order, Multi Order, Multi-Leg Order, Exit Positions,
Modify Order, Cancel Order, Smart Orders.

**Non-Transactional** — **Market data**, Orderbook, Positions, Holdings, Reports.

## Static IP whitelisting — order placement only

> "Order placement will be allowed only from whitelisted static IP addresses linked
> to the App ID."

This gate applies to **transactional** APIs. Market data and the other
non-transactional endpoints are exempt:

> "Existing App IDs will continue to function for data and non-transactional APIs only."

**Implication for OpenAlgo:** the market-data WebSocket (HSM) is unaffected by static
IP requirements. A streaming failure is never explained by IP whitelisting — see
`FYERS_HSM_MARKET_DATA_WEBSOCKET.md` for the real failure modes.

## Authentication — refresh tokens discontinued

> "The refresh token flow has been discontinued. A daily 2FA login is mandatory for
> API access. Access tokens will be valid only as per the updated authentication
> cycle."

`FYERS_API_v3.md` (*Authentication & Login Flow*) carries the matching note: *"Refresh token will be
discontinued from 1st April. When we validate the auth code to generate the access
token, a refresh token is also sent in the response. The refresh token has a validity
of 15 days."*

**Implication for OpenAlgo:** any flow calling `POST /api/v3/validate-refresh-token`
is dead. Tokens must come from the daily 2FA auth-code exchange.

Note the failure mode: a token minted through the retired refresh flow can still
decode as a structurally valid JWT — correct segments, an `hsm_key` claim, a future
`exp` — while being dead server-side. Local validity checks cannot detect this;
only a server round-trip can.

## Other deprecations recorded in `FYERS_API_v3.md`

- **`cmd` attribute** in the Quotes API response — deprecated
  ([notice](https://fyers.in/notice-board/action-required-cmd-field-in-api-to-be-deprecated.html)).
- **`slNo`** in the Positions response — deprecated (was used for sorting).
- **CO/BO orders** — deprecated per the 02 Aug 2026 changelog entry, alongside
  SL/TP position management.
- **EDIS/DDPI** — "As per new regulations, clients are required to authorise sell
  transactions" (no deadline stated).

## What did *not* change

Verified 2026-08-31 while diagnosing a WebSocket outage:

- **No change to the market-data socket.** The endpoint
  `wss://socket.fyers.in/hsm/v1-5/prod` and the request-type-1 auth frame are
  byte-for-byte identical between `fyers-apiv3` 3.1.7 (Mar 2025) and 3.1.16
  (Aug 2026). The only diff in `data_ws.py` across that window is four state-dict
  resets added to the reconnect/close paths.
- **No appId-hash, DPI, or new query-param/header requirement** on the data socket.
- **No vendor/source registration requirement** — the auth frame's source field is
  unvalidated.
- The changelog through 06 Sep 2026 contains **no** HSM endpoint or handshake change.
  The last socket-related entries are 22 Aug 2025 (reconnection logic) and
  23 Jun 2025 (NSE equity on TBT). The 30 Sep 2026 WebSocket-authentication notice
  is covered in `FYERS_HSM_MARKET_DATA_WEBSOCKET.md`, *Change history*.

## Host inconsistencies worth knowing

Most v3 endpoints are on `https://api-t1.fyers.in/api/v3/`, but Span Margin and all
EDIS endpoints still point at `https://api.fyers.in/api/v2/`. Async order docs note
`https://api-y1.fyers.in` may appear in other environments.
