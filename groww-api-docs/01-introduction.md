# Introduction

> Source: https://groww.in/trade-api/docs/curl

The Groww Trading API provides REST endpoints for trading and account data, including orders, portfolio information, and market data. Groww's cURL documentation describes equity (CASH) and derivatives (FNO) support; MCX commodities trading is not currently supported.

## Prerequisites

- A Groww account.
- An active Trading API subscription.
- An access token generated using one of the authentication flows in [02-authentication.md](02-authentication.md).

## Base URL and headers

The documented API host is `https://api.groww.in`. The documentation shows these headers for API requests:

| Header | Value |
|---|---|
| `Authorization` | `Bearer {ACCESS_TOKEN}` |
| `Accept` | `application/json` |
| `X-API-VERSION` | `1.0` |

POST requests that send JSON also include `Content-Type: application/json`. The docs state that all headers are mandatory.

## Request conventions

- GET request parameters are supplied in the URL as query parameters or path parameters.
- POST request parameters are sent as a JSON request body.
- Responses are JSON.

Example GET request from the documentation:

```bash
curl -X GET 'https://api.groww.in/v1/order/detail/{groww_order_id}?segment=CASH' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

## Response structure

Successful requests use `status: "SUCCESS"` and include the requested data in `payload`:

```json
{
  "status": "SUCCESS",
  "payload": {
    "symbolIsin": "INE002A01018",
    "productWisePositions": {}
  }
}
```

Failed requests (documented as HTTP 40x or 50x responses) use `status: "FAILURE"` and include an `error` object:

```json
{
  "status": "FAILURE",
  "error": {
    "code": "GA001",
    "message": "Bad request",
    "metadata": null
  }
}
```

## Error codes

| Code | Documented message |
|---|---|
| `GA000` | Internal error occurred |
| `GA001` | Bad request |
| `GA003` | Unable to serve request currently |
| `GA004` | Requested entity does not exist |
| `GA005` | User not authorised to perform this operation |
| `GA006` | Cannot process this request |
| `GA007` | Duplicate order reference id |

## Rate limits

Limits are applied by API type. APIs in the same type share the limit, so exhausting a limit on one API can rate-limit the other APIs in that type until the window resets.

| Type | APIs named by Groww | Requests/second | Requests/minute |
|---|---|---:|---:|
| Authentication | Generate access token | 5 | 30 |
| Orders | Create, modify, cancel order | 10 | 250 |
| Live Data | Market quote, LTP, OHLC | 10 | 300 |
| Non Trading | Order status/list, trade list, positions, holdings, margin | 20 | 500 |

The `/v1/token/api/access` endpoint is additionally limited to 150 requests per 24 hours.

## Common documented values

Groww's [Annexures](https://groww.in/trade-api/docs/curl/annexures) lists the API's fixed values. Frequently used values include:

| Field | Values documented |
|---|---|
| Exchange | `BSE`, `NSE` |
| Segment | `CASH`, `FNO` |
| Order type | `LIMIT`, `MARKET`, `SL`, `SL_M` |
| Product | `CNC`, `MIS`, `NRML` |
| Transaction type | `BUY`, `SELL` |
| Validity | `DAY` |
| Instrument type | `EQ`, `IDX`, `FUT`, `CE`, `PE` |

The Annexures page also documents order status, after-market order status, and candle intervals.

## Official sources

- [Groww cURL API documentation](https://groww.in/trade-api/docs/curl)
- [Groww API Annexures](https://groww.in/trade-api/docs/curl/annexures)
