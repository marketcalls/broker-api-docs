# Portfolio — Margins (Check Margin)

## 1. Introduction

The Margin API allows you to check the required margin and available balance for a new order, including advanced order types such as Bracket Orders (BO) and Cover Orders (CO). This API helps you validate whether you have enough margin before placing an order.

## 2. API Endpoint

```
POST <Base URL>/quick/user/check-margin
```

Replace `<Base URL>` with the relevant Kotak environment base URL provided in the response from the `/tradeApiValidate` API.

## 3. Headers

| Name | Type | Description |
| --- | --- | --- |
| accept | string | `application/json` |
| Sid | string | session sid generated on login |
| Auth | string | session token generated on login |
| neo-fin-key | string | static value: `neotradeapi` |
| Content-Type | string | `application/x-www-form-urlencoded` |

## 4. Request

```bash
curl --location '<Base URL>/quick/user/check-margin' \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
--data-urlencode 'jData={"brkName":"KOTAK","brnchId":"ONLINE","exSeg":"nse_cm","prc":"12500","prcTp":"L","prod":"CNC","qty":"1","tok":"11536","trnsTp":"B"}'
```

**Request Body (`jData`)**

| Field | Type | Description | Required | Example |
| --- | --- | --- | --- | --- |
| brkName | string | Broker name (always send as `KOTAK`) | Yes | `KOTAK` |
| brnchId | string | Branch id of user (always send as `ONLINE`) | Yes | `ONLINE` |
| exSeg | string | Exchange segment, e.g., `nse_cm` | Yes | `nse_cm` |
| prc | string | Order price in Rupees (0 for market orders) | Yes | `12500` |
| prcTp | string | Order type (`L`, `MKT`, etc.) | Yes | `L` |
| prod | string | Product code (`CNC`, `NRML`, `MIS`, etc.) | Yes | `CNC` |
| qty | string | Order quantity | Yes | `1` |
| tok | string | Token number (from scrip master) | Yes | `11536` |
| trnsTp | string | Transaction type (`B` for Buy, `S` for Sell) | Yes | `B` |
| slAbsOrTks | string | Stop loss type (Absolute or Ticks, BO only) | No | |
| slVal | string | Stop loss value (BO only) | No | |
| sqrOffAbsOrTks | string | Square off type (Absolute or Ticks, BO only) | No | |
| sqrOffVal | string | Square off value (BO only) | No | |
| trailSL | string | Trailing stop loss (Y or N, BO only) | No | |
| trgPrc | string | Trigger price (CO only, in Rupees) | No | |
| tSLTks | string | Trailing SL value (BO only, "Y" or "N") | No | |

> For Bracket and Cover Orders, include the additional optional fields as needed.

## 5. Response

Example Success Response:

```json
{
  "avlCash": "10197.480000",
  "totMrgnUsd": "12540.400000",
  "mrgnUsd": "40.400000",
  "ordMrgn": "12500.000000",
  "rmsVldtd": "NOT_OK",
  "reqdMrgn": "12540.400000",
  "avlMrgn": "10197.480000",
  "insufFund": "2342.920000",
  "stat": "Ok",
  "stCode": 200
}
```

### 200 Response Fields

| Field | Type | Description |
| --- | --- | --- |
| avlCash | string | Total cash available |
| avlMrgn | string | Available margin after order is placed |
| insufFund | string | Insufficient funds required to place order |
| mrgnUsd | string | Margin already used |
| ordMrgn | string | Margin required for the order |
| reqdMrgn | string | Net required margin for the order |
| rmsVldtd | string | Value is typically `OK` or `NOT_OK` |
| stat | string | API status (`Ok` for success) |
| totMrgnUsd | string | Total margin used |
| stCode | int | HTTP status code (200 = success) |

Example Error Response:

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid session",
  "stCode": 1003
}
```

## 6. Notes

- Use this API before placing any order to check if you have enough funds/margin.
- For market orders, send `prc` as `"0"`.
- For BO/CO, include the SL, trailing stop loss, and square off fields as applicable.
- Use valid session and auth tokens to avoid authentication errors.
