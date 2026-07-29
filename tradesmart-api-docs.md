# TradeSmart Trading API

Unofficial Markdown conversion of the TradeSmart Trading API documentation (Noren v2).

> Converted from a TradeSmart API documentation HTML export. API credentials are created at
> https://web.tradesmartonline.in/api ; the REST base URL is
> `https://v2api.tradesmartonline.in/NorenWClientAPIv2/`.

## Contents

**Getting started**

- [Introduction](#introduction)
- [Quick start](#quick-start)
- [Generate Access Token](#generate-access-token)

**Account**

- [User Details](#user-details)
- [Holdings](#holdings)
- [Limits](#limits)

**Instruments & market data**

- [Search Script](#search-script)
- [Security Info](#security-info)
- [Get Quotes](#get-quotes)
- [Option Chain](#option-chain)
- [Historical Data](#historical-data)
- [Time Price Data](#time-price-data)

**Orders**

- [Place Order](#place-order)
- [Order Margin](#order-margin)
- [Modify Order](#modify-order)
- [Cancel Order](#cancel-order)
- [Exit SNO Order](#exit-sno-order)

**Order & trade book**

- [Order Book](#order-book)
- [Single Order History](#single-order-history)
- [Trade Book](#trade-book)
- [Position Book](#position-book)

**Streaming & reference**

- [Suggested integration flow](#suggested-integration-flow)
- [WebSocket streaming](#websocket-streaming)
- [Reference](#reference)

---

## Introduction

The TradeSmart Trading API is a set of REST-like HTTP endpoints plus a streaming WebSocket that let you build complete algo and third-party trading platforms. You can authenticate, fetch market data, place and manage orders, and stream live quotes, order updates and positions.

All REST endpoints use `POST` with a raw `text/plain` body of the form `jData={...}`. Authenticated endpoints additionally send `Authorization: Bearer <access_token>`. Responses are JSON; success is indicated by `stat: Ok`.

### Base URLs

| Purpose | URL |
|---|---|
| REST API | `https://v2api.tradesmartonline.in/NorenWClientAPIv2/` |
| WebSocket | `wss://v2api.tradesmartonline.in/NorenWSAPI/` |

### Session lifetime

An access token is valid for one trading day. The user logs in again the next trading day to generate a fresh token.

---

## Quick start

From zero to your first authenticated request.

### Steps

1. Create API credentials at `https://web.tradesmartonline.in/api`.
2. Enter the app name, static IP and redirect URL.
3. Complete the login flow and receive a `code` on the redirect URL.
4. Build `checksum = SHA-256(api_key + secret_key + code)`.
5. Call `POST /GenAcsTok` to receive an `access_token`.
6. Send REST requests with body `jData={...}` and header `Authorization: Bearer <access_token>` where required.

---

## Generate Access Token

Exchange the login code and checksum for an access token. No bearer token is required for this call.

`POST` `/GenAcsTok` — No auth

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "code": "",
  "checksum": ""
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `code` | `""` | Authorization code received on the redirect URL after a successful login. |
| `checksum` | `""` | SHA-256 of api_key + secret_key + code. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/GenAcsTok" \
  -H "Content-Type: text/plain" \
  --data-raw 'jData={
  "code": "",
  "checksum": ""
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## User Details

Fetch profile and account details for the logged-in user.

`POST` `/UserDetails` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/UserDetails" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Holdings

Retrieve holdings bought or sold in previous trading sessions. T1 and delivered quantities are included.

`POST` `/Holdings` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "prd": "C"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |
| `prd` | `C` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/Holdings" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "prd": "C"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Limits

Fetch available funds, used margin and other limit details for the account.

`POST` `/Limits` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/Limits" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Search Script

Search for instruments by name or symbol and resolve their tokens.

`POST` `/SearchScrip` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "stext": "TCS"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `stext` | `TCS` | Search text. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/SearchScrip" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "stext": "TCS"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Security Info

Get contract / security details for a token on an exchange.

`POST` `/GetSecurityInfo` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "token": "TCS-EQ",
  "exch": "NSE"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `token` | `TCS-EQ` | Contract token. |
| `exch` | `NSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/GetSecurityInfo" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "token": "TCS-EQ",
  "exch": "NSE"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Get Quotes

Fetch a full market quote snapshot for a single instrument.

`POST` `/GetQuotes` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "token": "TCS-EQ",
  "exch": "NSE"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `token` | `TCS-EQ` | Contract token. |
| `exch` | `NSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/GetQuotes" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "token": "TCS-EQ",
  "exch": "NSE"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Option Chain

Return a window of option strikes around a chosen middle strike.

`POST` `/GetOptionChain` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "token": "TCS-EQ",
  "strprc": "2276",
  "cnt": "10"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `token` | `TCS-EQ` | Contract token. |
| `strprc` | `2276` | Middle strike price for the option-chain window. |
| `cnt` | `10` | Number of strikes on each side of the middle strike. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/GetOptionChain" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "token": "TCS-EQ",
  "strprc": "2276",
  "cnt": "10"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Historical Data

End-of-day historical candle data for a symbol over a date range.

`POST` `/EODChartData` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "sym": "BSE:SBIN",
  "from": "1690934400",
  "to": "1691107200"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `sym` | `BSE:SBIN` | Symbol in exchange:symbol format. |
| `from` | `1690934400` | From time / date in Unix epoch seconds. |
| `to` | `1691107200` | To time / date in Unix epoch seconds. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/EODChartData" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "sym": "BSE:SBIN",
  "from": "1690934400",
  "to": "1691107200"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Time Price Data

Intraday time-price series (candles) for a token at a chosen interval.

`POST` `/TPSeries` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "exch": "BSE",
  "token": "INFY",
  "st": "1750357800",
  "et": "1750674066",
  "intrv": "1"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `exch` | `BSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |
| `token` | `INFY` | Contract token. |
| `st` | `1750357800` | Start time in Unix epoch seconds. |
| `et` | `1750674066` | End time in Unix epoch seconds. |
| `intrv` | `1` | Candle interval in minutes. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/TPSeries" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "exch": "BSE",
  "token": "INFY",
  "st": "1750357800",
  "et": "1750674066",
  "intrv": "1"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Place Order

Place equity and derivative orders. The same endpoint serves limit, stop-loss, cover and bracket orders. The variant is decided by `prctyp` and `prd`.

`POST` `/PlaceOrder` — Bearer token

### Request body

Pick an order type below. Each tab shows the exact `jData` payload, its parameters and a ready-to-run request.

#### LMT

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1584.5",
  "dscqty": "0",
  "prd": "C",
  "trantype": "B",
  "prctyp": "LMT",
  "ret": "DAY",
  "ordersource": "API"
}
```

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |
| `exch` | `NSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |
| `tsym` | `INFY-EQ` | Trading symbol of the contract. URL-encode special characters where applicable. |
| `qty` | `1` | Order quantity. |
| `prc` | `1584.5` | Order price. Use 0 for market orders. |
| `dscqty` | `0` | Disclosed quantity. |
| `prd` | `C` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |
| `trantype` | `B` | Transaction type. B = Buy, S = Sell. |
| `prctyp` | `LMT` | Price type. One of LMT, MKT, SL-LMT or SL-MKT. |
| `ret` | `DAY` | Retention / validity. One of DAY, IOC or EOS. |
| `ordersource` | `API` | Order source. Use API. |

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/PlaceOrder" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1584.5",
  "dscqty": "0",
  "prd": "C",
  "trantype": "B",
  "prctyp": "LMT",
  "ret": "DAY",
  "ordersource": "API"
}'
```

#### SL-LMT

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1589.20",
  "trgprc": "1588.70",
  "dscqty": "0",
  "prd": "C",
  "trantype": "B",
  "prctyp": "SL-LMT",
  "ret": "DAY",
  "ordersource": "API"
}
```

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |
| `exch` | `NSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |
| `tsym` | `INFY-EQ` | Trading symbol of the contract. URL-encode special characters where applicable. |
| `qty` | `1` | Order quantity. |
| `prc` | `1589.20` | Order price. Use 0 for market orders. |
| `trgprc` | `1588.70` | Trigger price for SL, SL-M or SL-LMT orders. |
| `dscqty` | `0` | Disclosed quantity. |
| `prd` | `C` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |
| `trantype` | `B` | Transaction type. B = Buy, S = Sell. |
| `prctyp` | `SL-LMT` | Price type. One of LMT, MKT, SL-LMT or SL-MKT. |
| `ret` | `DAY` | Retention / validity. One of DAY, IOC or EOS. |
| `ordersource` | `API` | Order source. Use API. |

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/PlaceOrder" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1589.20",
  "trgprc": "1588.70",
  "dscqty": "0",
  "prd": "C",
  "trantype": "B",
  "prctyp": "SL-LMT",
  "ret": "DAY",
  "ordersource": "API"
}'
```

#### Cover LMT

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1587.1",
  "prd": "H",
  "trantype": "B",
  "prctyp": "LMT",
  "ret": "DAY",
  "blprc": "2",
  "ordersource": "API"
}
```

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |
| `exch` | `NSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |
| `tsym` | `INFY-EQ` | Trading symbol of the contract. URL-encode special characters where applicable. |
| `qty` | `1` | Order quantity. |
| `prc` | `1587.1` | Order price. Use 0 for market orders. |
| `prd` | `H` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |
| `trantype` | `B` | Transaction type. B = Buy, S = Sell. |
| `prctyp` | `LMT` | Price type. One of LMT, MKT, SL-LMT or SL-MKT. |
| `ret` | `DAY` | Retention / validity. One of DAY, IOC or EOS. |
| `blprc` | `2` | Book loss / stop-loss differential for a cover or bracket order. |
| `ordersource` | `API` | Order source. Use API. |

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/PlaceOrder" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1587.1",
  "prd": "H",
  "trantype": "B",
  "prctyp": "LMT",
  "ret": "DAY",
  "blprc": "2",
  "ordersource": "API"
}'
```

#### Cover MKT

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "mkt_protection": "5",
  "prc": "0",
  "prd": "H",
  "trantype": "B",
  "prctyp": "MKT",
  "ret": "DAY",
  "blprc": "2",
  "ordersource": "API"
}
```

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |
| `exch` | `NSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |
| `tsym` | `INFY-EQ` | Trading symbol of the contract. URL-encode special characters where applicable. |
| `qty` | `1` | Order quantity. |
| `mkt_protection` | `5` | Market protection percentage for market orders. |
| `prc` | `0` | Order price. Use 0 for market orders. |
| `prd` | `H` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |
| `trantype` | `B` | Transaction type. B = Buy, S = Sell. |
| `prctyp` | `MKT` | Price type. One of LMT, MKT, SL-LMT or SL-MKT. |
| `ret` | `DAY` | Retention / validity. One of DAY, IOC or EOS. |
| `blprc` | `2` | Book loss / stop-loss differential for a cover or bracket order. |
| `ordersource` | `API` | Order source. Use API. |

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/PlaceOrder" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "mkt_protection": "5",
  "prc": "0",
  "prd": "H",
  "trantype": "B",
  "prctyp": "MKT",
  "ret": "DAY",
  "blprc": "2",
  "ordersource": "API"
}'
```

#### Cover SL-LMT

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1585.50",
  "trgprc": "1583.80",
  "prd": "H",
  "trantype": "B",
  "prctyp": "SL-LMT",
  "ret": "DAY",
  "blprc": "2",
  "ordersource": "API"
}
```

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |
| `exch` | `NSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |
| `tsym` | `INFY-EQ` | Trading symbol of the contract. URL-encode special characters where applicable. |
| `qty` | `1` | Order quantity. |
| `prc` | `1585.50` | Order price. Use 0 for market orders. |
| `trgprc` | `1583.80` | Trigger price for SL, SL-M or SL-LMT orders. |
| `prd` | `H` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |
| `trantype` | `B` | Transaction type. B = Buy, S = Sell. |
| `prctyp` | `SL-LMT` | Price type. One of LMT, MKT, SL-LMT or SL-MKT. |
| `ret` | `DAY` | Retention / validity. One of DAY, IOC or EOS. |
| `blprc` | `2` | Book loss / stop-loss differential for a cover or bracket order. |
| `ordersource` | `API` | Order source. Use API. |

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/PlaceOrder" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1585.50",
  "trgprc": "1583.80",
  "prd": "H",
  "trantype": "B",
  "prctyp": "SL-LMT",
  "ret": "DAY",
  "blprc": "2",
  "ordersource": "API"
}'
```

#### Bracket LMT

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1583.80",
  "prd": "B",
  "trantype": "B",
  "prctyp": "LMT",
  "ret": "DAY",
  "blprc": "2.00",
  "bpprc": "2",
  "trailprc": "1",
  "ordersource": "API"
}
```

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |
| `exch` | `NSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |
| `tsym` | `INFY-EQ` | Trading symbol of the contract. URL-encode special characters where applicable. |
| `qty` | `1` | Order quantity. |
| `prc` | `1583.80` | Order price. Use 0 for market orders. |
| `prd` | `B` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |
| `trantype` | `B` | Transaction type. B = Buy, S = Sell. |
| `prctyp` | `LMT` | Price type. One of LMT, MKT, SL-LMT or SL-MKT. |
| `ret` | `DAY` | Retention / validity. One of DAY, IOC or EOS. |
| `blprc` | `2.00` | Book loss / stop-loss differential for a cover or bracket order. |
| `bpprc` | `2` | Book profit / target differential for a bracket order. |
| `trailprc` | `1` | Trailing stop-loss differential for a cover or bracket order. |
| `ordersource` | `API` | Order source. Use API. |

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/PlaceOrder" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1583.80",
  "prd": "B",
  "trantype": "B",
  "prctyp": "LMT",
  "ret": "DAY",
  "blprc": "2.00",
  "bpprc": "2",
  "trailprc": "1",
  "ordersource": "API"
}'
```

#### Bracket MKT

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "mkt_protection": "5",
  "prc": "0",
  "prd": "B",
  "trantype": "B",
  "prctyp": "MKT",
  "ret": "DAY",
  "blprc": "2.00",
  "bpprc": "2",
  "trailprc": "1",
  "ordersource": "API"
}
```

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |
| `exch` | `NSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |
| `tsym` | `INFY-EQ` | Trading symbol of the contract. URL-encode special characters where applicable. |
| `qty` | `1` | Order quantity. |
| `mkt_protection` | `5` | Market protection percentage for market orders. |
| `prc` | `0` | Order price. Use 0 for market orders. |
| `prd` | `B` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |
| `trantype` | `B` | Transaction type. B = Buy, S = Sell. |
| `prctyp` | `MKT` | Price type. One of LMT, MKT, SL-LMT or SL-MKT. |
| `ret` | `DAY` | Retention / validity. One of DAY, IOC or EOS. |
| `blprc` | `2.00` | Book loss / stop-loss differential for a cover or bracket order. |
| `bpprc` | `2` | Book profit / target differential for a bracket order. |
| `trailprc` | `1` | Trailing stop-loss differential for a cover or bracket order. |
| `ordersource` | `API` | Order source. Use API. |

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/PlaceOrder" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "mkt_protection": "5",
  "prc": "0",
  "prd": "B",
  "trantype": "B",
  "prctyp": "MKT",
  "ret": "DAY",
  "blprc": "2.00",
  "bpprc": "2",
  "trailprc": "1",
  "ordersource": "API"
}'
```

#### Bracket SL-LMT

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1584.00",
  "trgprc": "1584.00",
  "prd": "B",
  "trantype": "B",
  "prctyp": "SL-LMT",
  "ret": "DAY",
  "blprc": "2.00",
  "bpprc": "2",
  "trailprc": "1",
  "ordersource": "API"
}
```

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |
| `exch` | `NSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |
| `tsym` | `INFY-EQ` | Trading symbol of the contract. URL-encode special characters where applicable. |
| `qty` | `1` | Order quantity. |
| `prc` | `1584.00` | Order price. Use 0 for market orders. |
| `trgprc` | `1584.00` | Trigger price for SL, SL-M or SL-LMT orders. |
| `prd` | `B` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |
| `trantype` | `B` | Transaction type. B = Buy, S = Sell. |
| `prctyp` | `SL-LMT` | Price type. One of LMT, MKT, SL-LMT or SL-MKT. |
| `ret` | `DAY` | Retention / validity. One of DAY, IOC or EOS. |
| `blprc` | `2.00` | Book loss / stop-loss differential for a cover or bracket order. |
| `bpprc` | `2` | Book profit / target differential for a bracket order. |
| `trailprc` | `1` | Trailing stop-loss differential for a cover or bracket order. |
| `ordersource` | `API` | Order source. Use API. |

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/PlaceOrder" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1584.00",
  "trgprc": "1584.00",
  "prd": "B",
  "trantype": "B",
  "prctyp": "SL-LMT",
  "ret": "DAY",
  "blprc": "2.00",
  "bpprc": "2",
  "trailprc": "1",
  "ordersource": "API"
}'
```

### Response

A successful response carries `stat: Ok` and a `norenordno` once the OMS accepts the order. A rejection carries `stat: Not_Ok` and an `emsg`.

---

## Order Margin

Calculate the margin required for an order before placing it.

`POST` `/GetOrderMargin` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "BSE",
  "tsym": "INFY",
  "qty": "1",
  "prc": "1598",
  "prd": "C",
  "trantype": "B",
  "prctyp": "LMT",
  "rorgqty": "0",
  "rorgprc": "0"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |
| `exch` | `BSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |
| `tsym` | `INFY` | Trading symbol of the contract. URL-encode special characters where applicable. |
| `qty` | `1` | Order quantity. |
| `prc` | `1598` | Order price. Use 0 for market orders. |
| `prd` | `C` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |
| `trantype` | `B` | Transaction type. B = Buy, S = Sell. |
| `prctyp` | `LMT` | Price type. One of LMT, MKT, SL-LMT or SL-MKT. |
| `rorgqty` | `0` | Original order quantity, used in the margin-modification context. |
| `rorgprc` | `0` | Original order price, used in the margin-modification context. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/GetOrderMargin" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "exch": "BSE",
  "tsym": "INFY",
  "qty": "1",
  "prc": "1598",
  "prd": "C",
  "trantype": "B",
  "prctyp": "LMT",
  "rorgqty": "0",
  "rorgprc": "0"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Modify Order

Modify the price, quantity or type of a pending order.

`POST` `/ModifyOrder` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "norenordno": "1234",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1584.5",
  "dscqty": "0",
  "prd": "C",
  "trantype": "B",
  "prctyp": "LMT",
  "ret": "DAY",
  "ordersource": "API"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |
| `norenordno` | `1234` | Noren order number returned by the OMS. |
| `exch` | `NSE` | Exchange code. One of NSE, BSE, NFO, BFO or MCX. |
| `tsym` | `INFY-EQ` | Trading symbol of the contract. URL-encode special characters where applicable. |
| `qty` | `1` | Order quantity. |
| `prc` | `1584.5` | Order price. Use 0 for market orders. |
| `dscqty` | `0` | Disclosed quantity. |
| `prd` | `C` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |
| `trantype` | `B` | Transaction type. B = Buy, S = Sell. |
| `prctyp` | `LMT` | Price type. One of LMT, MKT, SL-LMT or SL-MKT. |
| `ret` | `DAY` | Retention / validity. One of DAY, IOC or EOS. |
| `ordersource` | `API` | Order source. Use API. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/ModifyOrder" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "norenordno": "1234",
  "exch": "NSE",
  "tsym": "INFY-EQ",
  "qty": "1",
  "prc": "1584.5",
  "dscqty": "0",
  "prd": "C",
  "trantype": "B",
  "prctyp": "LMT",
  "ret": "DAY",
  "ordersource": "API"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Cancel Order

Cancel a pending order by its Noren order number.

`POST` `/CancelOrder` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "norenordno": ""
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `norenordno` | `""` | Noren order number returned by the OMS. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/CancelOrder" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "norenordno": ""
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Exit SNO Order

Exit a cover or bracket (special) order leg.

`POST` `/ExitSNOOrder` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "prd": "H",
  "norenordno": ""
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `prd` | `H` | Product code. C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order. |
| `norenordno` | `""` | Noren order number returned by the OMS. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/ExitSNOOrder" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "prd": "H",
  "norenordno": ""
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Order Book

List all orders placed during the current trading day.

`POST` `/OrderBook` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/OrderBook" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Single Order History

Fetch the full status history of a single order.

`POST` `/SingleOrdHist` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "norenordno": ""
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `norenordno` | `""` | Noren order number returned by the OMS. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/SingleOrdHist" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "norenordno": ""
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Trade Book

List all trades (fills) for the account during the current day.

`POST` `/TradeBook` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/TradeBook" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Position Book

Retrieve net and day-wise open positions for the account.

`POST` `/PositionBook` — Bearer token

### Request body

Sent as a raw `text/plain` body in `jData={...}` form.

```json
jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>"
}
```

### Parameters

| Field | Sample | Description |
|---|---|---|
| `uid` | `<CLIENT_ID>` | Logged-in user ID / client ID. |
| `actid` | `<CLIENT_ID>` | Trading account ID. Usually the same as the client ID. |

### Example request

```bash
curl -X POST "https://v2api.tradesmartonline.in/NorenWClientAPIv2/PositionBook" \
  -H "Content-Type: text/plain" -H "Authorization: Bearer <access_token>" \
  --data-raw 'jData={
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>"
}'
```

### Response

A successful response carries `stat: Ok`. A failed response carries `stat: Not_Ok` with an `emsg` where available. For order placement and modification, `norenordno` is returned once the OMS accepts the request.

---

## Suggested integration flow

A typical order lifecycle for an algo platform, from login to exit.

### Recommended flow

1. Create credentials and complete the login flow.
2. Generate an access token with `/GenAcsTok`.
3. Resolve instruments with `/SearchScrip` or `/GetSecurityInfo`.
4. Fetch quotes or candles with `/GetQuotes`, `/TPSeries` or WebSocket subscriptions.
5. Check funds and margin with `/Limits` and `/GetOrderMargin`.
6. Place the order with `/PlaceOrder`.
7. Track status via WebSocket order updates or `/OrderBook` and `/SingleOrdHist`.
8. Track fills with `/TradeBook` and positions with `/PositionBook`.
9. Modify, cancel or exit with `/ModifyOrder`, `/CancelOrder` or `/ExitSNOOrder`.

---

## WebSocket streaming

Stream live quotes, market depth, order updates and positions over a single WebSocket. All messages are JSON.

`WSS` `wss://v2api.tradesmartonline.in/NorenWSAPI/`

### Connect

After the socket opens, send a connect message with the user ID, account ID, source and access token.

```json
{
  "t": "a",
  "uid": "<CLIENT_ID>",
  "actid": "<CLIENT_ID>",
  "source": "API",
  "accesstoken": "<access_token>"
}
```

### Tasks

| Task | Request `t` | Ack / feed | Purpose |
|---|---|---|---|
| Connect | `a` | `ak` | Authenticate the socket session. |
| Subscribe touchline | `t` | `tk / tf` | LTP and top-of-book updates. |
| Unsubscribe touchline | `u` | `uk` | Stop touchline updates. |
| Subscribe depth | `d` | `dk / df` | Market-depth updates. |
| Unsubscribe depth | `ud` | `udk` | Stop depth updates. |
| Subscribe positions | `p` | `pk / pm` | Position updates. |
| Unsubscribe positions | `up` | `upk` | Stop position updates. |
| Subscribe LTP | `l` | `lk / lf` | LTP-only feed. |
| Unsubscribe LTP | `ul` | `ulk` | Stop LTP-only feed. |
| Heartbeat | `h` | `hk` | Keep-alive. |
| Order update | `automatic` | `om` | Status, fill, rejection, cancellation. |
| Alert update | `automatic` | `am` | Alert / GTT updates. |
| Admin message | `automatic` | `rm` | Broker / admin messages. |
| Market status | `automatic` | `ms` | Exchange market-status updates. |

### Subscription keys

Use `EXCHANGE|TOKEN`. Separate multiple instruments with `#`.

```json
{
  "t": "t",
  "k": "NSE|22#BSE|508123"
}
```

### Notes

- Touchline and depth messages after the first acknowledgement may contain only the changed fields.
- Order updates use `t=om`. Key fields: `norenordno`, `status`, `reporttype`, `fillshares`, `avgprc`, `rejreason`, `exchordid`, `exch_tm`, `ordersource`.
- Position updates use `t=pm` with quantities, average prices, realized P&L and net quantity.
- Send a heartbeat `{ "t": "h" }`; the acknowledgement is `t=hk` with a timestamp field `ft`.

---

## Reference

Enumerated values used across order placement, modification and book endpoints.

### Code reference

| Type | Values |
|---|---|
| Product codes | `C = CNC, M = NRML, I = MIS, F = MTF, H = Cover Order, B = Bracket Order` |
| Transaction type | `B = Buy, S = Sell` |
| Price type | `LMT, MKT, SL-LMT, SL-MKT` |
| Retention | `NSE: DAY, IOC · BSE/BFO/BCD: EOS, DAY, IOC · NFO/CDS/MCX: DAY, IOC` |
| Order status | `PENDING, CANCELED, OPEN, REJECTED, COMPLETE, TRIGGER_PENDING` |
