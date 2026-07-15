# Utility APIs

> Source: https://api-docs.indstocks.com/utility/

Utility endpoints for options analytics.

> ⚠️ **Coming Soon** — All three endpoints below are marked "Coming Soon" in the official
> documentation and may not be live yet.

## Endpoints Overview

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/option-chain` | Option chain for an instrument and expiry |
| GET | `/option-chain-symbols` | Available expiry dates for an index/symbol |
| POST | `/greeks` | Calculate option greeks (IV, delta, gamma, theta, vega) |

---

## Option Chain

**Endpoint:** `GET /option-chain`

Retrieves the option chain for a specific instrument and expiry.

### Query Parameters

| Parameter | Description |
|-----------|-------------|
| `token` | Instrument (index) identifier |
| `count` | Number of strikes per side (ITM/OTM) |
| `expiry` | Expiry date in `DD-MMM-YYYY` format |

---

## Get Expiries

**Endpoint:** `GET /option-chain-symbols`

Lists the available expiry dates for an option symbol.

### Query Parameters

| Parameter | Description |
|-----------|-------------|
| `token` | Index identifier |

**Response:** an array of expiry dates in chronological order.

---

## Greeks Calculation

**Endpoint:** `POST /greeks`

Calculates option greeks for one or more instruments.

### Request Body

| Parameter | Description |
|-----------|-------------|
| `tokens` | Array of instrument tokens |

### Response

Returns calculated greek values per token:

| Greek | Description |
|-------|-------------|
| `IV` | Implied Volatility, expressed as a decimal (e.g., `0.16` = 16%) |
| `delta` | Rate of change vs. underlying (−1 to 1) |
| `gamma` | Rate of change of delta (small positive value) |
| `theta` | Time decay (typically negative for bought options) |
| `vega` | Sensitivity to volatility (typically positive) |
