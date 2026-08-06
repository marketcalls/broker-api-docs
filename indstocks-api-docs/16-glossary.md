# Glossary & Constants

> Source: https://api-docs.indstocks.com/glossary/

A single-page reference for every enum, prefix, and identifier format used across the API.

## Order ID Prefixes

| Prefix | Meaning | Usage |
|--------|---------|-------|
| `EQ-` | Equity order | Standard and smart-order parent orders in the `EQUITY` segment |
| `DRV-` | Derivative order | Standard and smart-order parent orders in the `DERIVATIVE` segment |
| `GTT-` | Good Till Triggered | Smart-order child legs, and parents when the limit price exceeds the circuit range |

## Core Request Enums

### Transaction & Exchange

| Field | Values |
|-------|--------|
| `txn_type` | `BUY`, `SELL` |
| `exchange` | `NSE`, `BSE` |

### Segment & Product

> ⚠️ **Casing differs by endpoint family.** Order and other REST endpoints take **uppercase**;
> portfolio queries take **lowercase**.

| Context | `segment` | `product` |
|---------|-----------|-----------|
| Orders / REST | `EQUITY`, `DERIVATIVE` | `CNC`, `INTRADAY`, `MARGIN` |
| Portfolio queries | `equity`, `derivative` | `cnc`, `intraday`, `margin` |

### Order Parameters

| Field | Values |
|-------|--------|
| `order_type` (standard) | `LIMIT`, `MARKET` |
| `order_type` (smart orders) | `LIMIT`, `MARKET`, `TRIGGER` |
| `validity` (standard) | `DAY`, `IOC` |
| `validity` (smart orders) | `DAY` only |
| `algo_id` | `99999` (NSE), `9999999999999999` (BSE) |
| `source` (instruments master) | `equity`, `fno`, `index` |

## Instrument Code Formats

| Context | Format | Example |
|---------|--------|---------|
| REST query | `SEGMENT_TOKEN` (underscore) | `NSE_3045`, `NFO_51011` |
| WebSocket | `SEGMENT:TOKEN` (colon) | `NSE:2885`, `NFO:51011` |

### WebSocket Prefixes

| Prefix | Meaning |
|--------|---------|
| `NSE:` | NSE Equity |
| `BSE:` | BSE Equity |
| `NFO:` | NSE Derivatives (F&O) |
| `BFO:` | BSE Derivatives (F&O) |
| `NIDX:` | NSE Index |
| `BIDX:` | BSE Index |

## Order Status Values

`QUEUED`, `O-PENDING`, `SL-PENDING`, `PROCESSING`, `ABORTED`, `INITIATED`, `SUCCESS`,
`CANCELLED`, `MODIFIED`, `PENDING`, `EXPIRED`, `FAILED`, `PARTIALLY FILLED`,
`PARTIALLY FILLED - CANCELLED`, `PARTIALLY FILLED - EXPIRED`

See [Order Management](09-order-management.md#order-status-values).

## WebSocket Message Fields

| Field | Values | Feed |
|-------|--------|------|
| `action` | `subscribe`, `unsubscribe` | Price Feed |
| `action` | `subscribe` | Order Updates Feed |
| `mode` | `ltp`, `quote` | Price Feed |
| `mode` | `order_update` | Order Updates Feed |

## TOTP Authentication

| Field | Meaning |
|-------|---------|
| `mpin` | Account MPIN |
| `totp` | 6-digit code from the authenticator app |
| `x-api-key` | Client ID — a **header**, distinct from the access token |

| Limit | Value |
|-------|-------|
| Token generation rate | 1 per 60 seconds |
| Lockout threshold | 5 incorrect codes in 15 minutes |
| Setup window | 5 minutes |
| Access token validity | 24 hours |
| Concurrent tokens | 1 — a new token invalidates the previous one |

See [Authentication & Users](04-authentication-users.md).
