# Trading APIs — Place, Modify and Cancel Order

> **Note:** Bracket orders (BO) and Cover orders (CO) have been discontinued on Trade APIs since 1 April 2026.

---

## Place Order API

### 1. Introduction

The Place Order API allows you to place buy or sell orders across all supported exchange segments and order types. It supports product types like NRML, CNC, MIS, and MTF.

### 2. API Endpoint

```
POST <Base URL>/quick/order/rule/ms/place
```

Replace `<Base URL>` with the relevant Kotak environment base URL provided in the response from the `/tradeApiValidate` API.

### 3. Headers

| Name | Type | Description |
| --- | --- | --- |
| accept | string | Should always be `application/json` |
| Sid | string | session sid generated on login |
| Auth | string | session token generated on login |
| neo-fin-key | string | static value: `neotradeapi` |
| Content-Type | string | Always `application/x-www-form-urlencoded` |

### 4. Request Body

The request body is sent as a single field named `jData`, which is a stringified JSON object and must be URL-encoded.

```bash
curl -X POST "<baseUrl>/quick/order/rule/ms/place" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode 'jData={
  "am": "NO",
  "dq": "0",
  "es": "nse_cm",
  "mp": "0",
  "pc": "CNC",
  "pf": "N",
  "pr": "0",
  "pt": "MKT",
  "qt": "1",
  "rt": "DAY",
  "tp": "0",
  "ts": "ITBEES-EQ",
  "tt": "B"
}'
```

**Request Body Fields**

| Name | Type | Description | Allowed / Example Values |
| --- | --- | --- | --- |
| am | string | After Market Order flag | `NO` (normal), `YES` (AMO) |
| dq | string | Disclosed quantity | `0` or a partial quantity |
| es | string | Exchange segment code | `nse_cm`, `bse_cm`, `nse_fo`, `bse_fo`, `cde_fo`, `mcx_fo` |
| mp | string | Market protection value (used in some market orders) | `0` or numerical value |
| pc | string | Product code | `NRML`, `CNC`, `MIS`, `CO`, `BO`, `MTF` |
| pf | string | Portfolio flag | `N` |
| pr | string | Price for limit order, `0` for market order | e.g. `0`, `450.5` |
| pt | string | Order type | `L` (Limit), `MKT` (Market), `SL` (Stoploss), `SL-M` (SL-Market) |
| qt | string | Order quantity | e.g. `1`, `100` |
| rt | string | Validity / order duration | `DAY`, `IOC` |
| tp | string | Trigger price (used for SL/SL-M/CO) | `0` or actual trigger price |
| ts | string | Trading symbol (from scrip master file) | e.g. `ITBEES-EQ` |
| tt | string | Transaction type | `B` (Buy), `S` (Sell) |

### 5. Response

Success:

```json
{
  "nOrdNo": "250720000007242",
  "stat": "Ok",
  "stCode": 200
}
```

| Name | Type | Description |
| --- | --- | --- |
| nOrdNo | string | Unique order number assigned to your request |
| stat | string | Status message, "Ok" if successful |
| stCode | int | HTTP status code, 200 for success |

Error:

```json
{
  "stat": "Not_Ok",
  "emsg": "Insufficient balance.",
  "stCode": 1004
}
```

| Name | Type | Description |
| --- | --- | --- |
| stat | string | Status message, "Not_Ok" for errors |
| emsg | string | Error message in plain English |
| stCode | int | Error code |

**Tips & Notes**

- Ensure all header tokens and session information are obtained via prior authentication flows.
- Use the latest Scrip Master file to get correct trading symbols and instrument details.
- Handle all non-200 status codes for robust error management.

---

## Modify Order API

### 1. Introduction

The Modify Order API allows you to modify an already-placed order's parameters — quantity, price, validity, product type, and more — before it is executed or fully filled.

### 2. API Endpoint

```
POST <Base URL>/quick/order/vr/modify
```

### 3. Headers

Same as Place Order: `accept`, `Sid`, `Auth`, `neo-fin-key`, `Content-Type: application/x-www-form-urlencoded`.

### 4. Request Body

The request body uses a single field named `jData`, a URL-encoded JSON object.

```bash
curl -X POST "<baseUrl>/quick/order/vr/modify" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode 'jData={
  "am": "NO",
  "dq": "0",
  "es": "nse_cm",
  "mp": "0",
  "pc": "NRML",
  "pf": "N",
  "pr": "0",
  "pt": "MKT",
  "qt": "1",
  "rt": "DAY",
  "tp": "0",
  "ts": "TATAPOWER-EQ",
  "tt": "B",
  "no": "<orderNo>"
}'
```

**Request Body Fields**

| Name | Type | Description | Allowed / Example Values |
| --- | --- | --- | --- |
| tk | string | Token (instrument token from scrip master, as `pSymbol` column) | `11536`, or from scrip master `pSymbol` |
| fq | string | Filled Quantity (optional) | `10`, `0` |
| mp | string | Market protection value | `0` |
| pc | string | Product code | `NRML`, `CNC`, `MIS`, `CO`, `BO` |
| dd | string | Date/Days (trailing validity, if applicable) | `NA` or as required |
| dq | string | Disclosed quantity | `0` or a partial quantity |
| vd | string | Validity (order duration) | `DAY`, `IOC` |
| ts | string | Trading Symbol (from scrip master) | `TCS-EQ`, etc. |
| tt | string | Transaction type | `B` (Buy), `S` (Sell) |
| pr | string | Price | e.g. `3001` |
| tp | string | Trigger price (for SL, SL-M) | `0` or actual trigger price |
| qt | string | Quantity | e.g. `10` |
| no | string | Nest Order Number (system order id for the original order) | e.g. `220106000000185` |
| es | string | Exchange Segment | `nse_cm`, `bse_cm`, `nse_fo`, `bse_fo`, `cde_fo` |
| pt | string | Order Type | `L` (Limit), `MKT` (Market), `SL` (Stoploss), `SL-M` (SL-Market) |

### 5. Response

Success:

```json
{
  "nOrdNo": "250720000007242",
  "stat": "Ok",
  "stCode": 200
}
```

Error:

```json
{
  "stat": "Not_Ok",
  "emsg": "Order cannot be modified as it is already executed.",
  "stCode": 1006
}
```

**Notes**

- Only orders that are not yet executed or completed can be modified.
- Always use valid instrument tokens, symbols, and original order numbers.
- Use the latest scrip master data for token and symbol lookups.

---

## Cancel Order API

### 1. Introduction

Kotak Securities provides an API for cancelling open orders.

### 2. API Endpoint

| Order Type | Endpoint (after `<Base URL>`) |
| --- | --- |
| Regular Order | `/quick/order/cancel` |

### 3. Headers

Same as Place Order: `accept`, `Sid`, `Auth`, `neo-fin-key`, `Content-Type: application/x-www-form-urlencoded`.

### 4. Request Body

The request body is a single URL-encoded field named `jData` containing a JSON object.

```bash
curl -X POST "<baseUrl>/quick/order/cancel" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode 'jData={"on":"<orderNo>","am":"NO"}'
```

**Request Body Fields**

| Name | Type | Description | Required | Example |
| --- | --- | --- | --- | --- |
| am | string | AMO flag (`YES` for AMO orders; omit/`NO` for others) | Optional | `YES`, `NO` |
| on | string | Nest order number (unique order id) | Required | `2105199703091997` |
| ts | string | Trading symbol (mandatory for AMO orders) | Optional | `TCS-EQ` |

### 5. Response

Success:

```json
{
  "nOrdNo": "2105199703091997",
  "stat": "Ok",
  "stCode": 200
}
```

Error:

```json
{
  "stat": "Not_Ok",
  "emsg": "Order already cancelled or not found.",
  "stCode": 1006
}
```

### 6. Usage Notes

- For AMO cancellation, `am: "YES"` and `ts` (trading symbol) are mandatory.
- Orders already fully executed or cancelled cannot be cancelled again.
- Use the exact `on` (Nest order number) as returned in order placement or status queries.
- Always check for `"stat":"Ok"` in the response for a successful cancellation.
