# API Basics

This page covers the fundamental conventions that apply to every endpoint in the Tradejini Rest API.

## Base URL

All API requests must be sent to:

```
https://api.tradejini.com/v2
```

Endpoint paths in this documentation are shown relative to this base URL.
For example, `GET /api/oms/orders` means:

```
GET https://api.tradejini.com/v2/api/oms/orders
```

## Authentication

All protected endpoints require an `Authorization` header in the following format:

```
Authorization: Bearer <api_key>:<access_token>
```

| Part | Description |
| --- | --- |
| `<api_key>` | Your app's alphanumeric API key from the [Apps](https://developer.tradejini.com/developer-portal) section |
| `<access_token>` | The token returned by the authentication endpoint. Valid for **24 hours**. |

The Individual Token endpoint (`POST /api-gw/oauth/individual-token-v2`) uses a different format — it only requires the API key, since it is the endpoint that generates the access token:

```
Authorization: Bearer <api_key>
```

See the [Authorization Flow](https://developer.tradejini.com/docs/authorization-flow/individual-apps) section for step-by-step instructions.

## Request Format

| HTTP Method | Content-Type | Body format |
| --- | --- | --- |
| `GET` | — | Query parameters only |
| `DELETE` | — | Query parameters only |
| `POST` | `application/x-www-form-urlencoded` | Form-encoded key=value pairs |
| `PUT` | `application/x-www-form-urlencoded` | Form-encoded key=value pairs |

**Example POST request:**

```bash
curl -X POST https://api.tradejini.com/v2/api/oms/place-order \
  -H "Authorization: Bearer xK9mP2qRtZ:eyJhbGciOiJSUzI1NiJ9..." \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "symId=EQT_RELIANCE_EQ_NSE&qty=10&side=buy&type=limit&product=delivery&limitPrice=2440&validity=day"
```

## Response Format

All JSON responses follow a consistent envelope structure:

```json
{
  "s": "ok",
  "d": { ... }
}
```

| Field | Type | Values | Description |
| --- | --- | --- | --- |
| `s` | string | `"ok"`, `"error"`, `"no-data"` | Response status |
| `d` | any | object, array, or string | Response payload. Present only when `s` is `"ok"`. |
| `msg` | string | — | Present on `"error"` and `"no-data"` responses instead of `d`. |

**Success response (object payload):**

```json
{ "s": "ok", "d": { "orderId": "210115000000001", "msg": "Order Placed Successfully" } }
```

**Success response (array payload):**

```json
{ "s": "ok", "d": [ { "symId": "EQT_RELIANCE_EQ_NSE", "qty": 10 } ] }
```

**No-data response:**

```json
{ "s": "no-data", "msg": "no-data" }
```

**Error response:**

```json
{ "s": "error", "msg": "Input validation failed. Kindly check your input contains required fields for the request" }
```

## Symbol IDs

Instruments are identified by a `symId` string. The format encodes the asset class, symbol, series, and exchange:

```
EQT_RELIANCE_EQ_NSE      → Reliance Industries equity on NSE
FUT_NIFTY_FUT_NFO_25APR2024  → NIFTY April 2024 futures
OPT_NIFTY_CE_NFO_25APR2024_22000  → NIFTY April 2024 22000 CE options
```

Use the [Scrip Master Data](https://developer.tradejini.com/docs/symbol-details/getSymbolDetails) endpoint to look up valid `symId` values.

## Order Field Codes

Many order fields use abbreviated codes. The full value set is accepted in requests and returned in responses.

| Field | Accepted values | Meaning |
| --- | --- | --- |
| `side` | `buy`, `sell` | Order direction |
| `type` | `limit`, `market`, `stoplimit`, `stopmarket` | Order price type |
| `product` | `delivery`, `intraday`, `normal`, `cover`, `bracket` | Product / margin type |
| `validity` | `day`, `ioc`, `eos`, `gtc` | Order validity — Day, Immediate-or-Cancel, End-of-Session (BSE only), Good-Till-Cancelled |
| `status` | `open`, `completed`, `rejected`, `cancelled` | Order status in order book |
| `legType` | `main`, `stoploss`, `target` | Leg type for bracket/cover orders |

## Static IP Requirement

For **Individual App** registrations, all API requests must originate from a **whitelisted static IP address**. This is enforced at the gateway level. Requests from non-whitelisted IPs return `401 Unauthorized` with no further detail.

Ensure you have a static IP from your ISP, a cloud provider (AWS/GCP/Azure), or a VPS before going live. You register the IP during [App Creation](https://developer.tradejini.com/docs/app-creation/individual-apps).

## Pagination

The Tradejini Rest API does not use cursor-based or offset pagination. All list endpoints return the full result set for the authenticated user's session in a single response.
