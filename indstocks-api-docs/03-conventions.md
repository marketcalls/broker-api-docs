# API Conventions

> Source: https://api-docs.indstocks.com/conventions/

## Base URL

```
https://api.indstocks.com
```

## Data Format

- All request and response bodies are **JSON**.
- **Timestamps** are Unix epoch **milliseconds** in the **IST** timezone (unless a response
  explicitly returns an ISO-8601 string with a `+05:30` offset).

## HTTP Methods

| Method | Usage |
|--------|-------|
| `GET`  | Retrieve resources (quotes, orders, holdings, etc.) |
| `POST` | Create or act on resources (place / modify / cancel orders) |

## Authentication

Protected endpoints require your access token in the `Authorization` header. The token is sent
**raw**, without a `Bearer ` prefix:

```
Authorization: YOUR_ACCESS_TOKEN
```

For `POST` requests, also send:

```
Content-Type: application/json
```

## Standard Response Envelope

Successful responses share a common envelope:

```json
{
  "status": "success",
  "data": { }
}
```

Errors use:

```json
{
  "status": "error",
  "message": "A human-readable error message.",
  "error_code": "INVALID_INPUT"
}
```

See **[Error Codes](14-errors.md)** for the full list.

## Rate Limits

| Category | Per Second | Per Minute | Per Day | Notes |
|----------|-----------|------------|---------|-------|
| Order APIs | 10 | — | — | Max 25 modifications per order |
| Data APIs | 5 | — | 100,000 | Instruments, historical data |
| Quote APIs | 5 | — | 100,000 | Full / LTP / market depth quotes |
| Non-Trading APIs | 15 | — | 100,000 | Profile, Funds, Order History, etc. |
| Token Generation | — | **1** | — | `/generate/token` (TOTP) — 1 per 60 seconds |
| WebSocket Connections | — | — | — | Up to **3** connections per user |
| WebSocket Subscriptions | — | — | — | Up to **3,000** instruments per connection |

Exceeding a limit returns **`429 Too Many Requests`**.

> `/generate/token` has additional lockout rules on top of the throttle — see
> [Authentication & Users](04-authentication-users.md#rate-limits--lockouts).

## Instrument Identifiers

Most market-data endpoints identify instruments using a `SEGMENT_TOKEN` (REST) or
`SEGMENT:TOKEN` (WebSocket) convention, for example:

- `NSE_3045` / `NSE:2885` — NSE equity
- `NFO_51011` / `NFO:51011` — NSE F&O
- `NIDX:26000` — NSE index

The numeric token is the `SECURITY_ID` from the [Instruments Master](05-instruments.md) file.
