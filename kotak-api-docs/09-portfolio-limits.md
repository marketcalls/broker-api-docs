# Portfolio — Limits (Funds)

## 1. Introduction

The Limits API allows you to query real-time available limits, margins, collateral, exposure, and cash balances for your trading account, filtered by segment, exchange, and product type.

## 2. API Endpoint

```
POST <Base URL>/quick/user/limits
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
curl --location '<Base URL>/quick/user/limits' \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
--data-urlencode 'jData={"seg":"ALL","exch":"ALL","prod":"ALL"}'
```

**Request Body (`jData`)**

| Name | Type | Description | Allowed Values | Default |
| --- | --- | --- | --- | --- |
| seg | string | Segment to fetch limits for | `ALL`, `CASH`, `CUR`, `FO` | `ALL` |
| exch | string | Exchange to fetch limits for | `ALL`, `NSE`, `BSE` | `ALL` |
| prod | string | Product to fetch limits for | `ALL`, `NRML`, `CNC`, `MIS` | `ALL` |

## 5. Response

Example Success Response (truncated):

```json
{
  "Category": "CLIENT_MTF",
  "EntityId": "account-******",
  "BoardLotLimit": "5000",
  "CollateralValue": "10197.48",
  "Net": "10157.08",
  "MarginUsed": "40.4",
  "AdhocMargin": "0",
  "SpanMarginPrsnt": "0",
  "ExposureMarginPrsnt": "0",
  "NotionalCash": "0",
  "UnrealizedMtomPrsnt": "0",
  "RealizedMtomPrsnt": "0",
  "SpecialMarginPrsnt": "0",
  "PremiumPrsnt": "0",
  "MarginVarPrsnt": "0",
  "stCode": 200,
  "stat": "Ok"
}
```

### 200 Response Fields (most relevant)

| Field | Type | Description |
| --- | --- | --- |
| Category | string | Category |
| EntityId | string | Account ID |
| BoardLotLimit | string | Board lot limit |
| CollateralValue | string | Value of pledged securities/collateral |
| Net | string | Net available margin/cash |
| MarginUsed | string | Margin already used |
| AdhocMargin | string | Extra margin added |
| SpanMarginPrsnt | string | SPAN margin requirement |
| ExposureMarginPrsnt | string | Exposure margin requirement |
| NotionalCash | string | Notional (total) cash |
| UnrealizedMtomPrsnt | string | Unrealized Mark-to-Market (PnL) |
| RealizedMtomPrsnt | string | Realized Mark-to-Market (PnL) |
| SpecialMarginPrsnt | string | Special margin imposed |
| PremiumPrsnt | string | Premium margin present |
| MarginVarPrsnt | string | VAR margin present |
| stCode | int | Status code (200 = success) |
| stat | string | "Ok" for success |
| ... | ... | Additional technical/segment breakdown fields |

Example Error Response:

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid session",
  "stCode": 1003
}
```

## 6. Notes

- All numerical limits are provided as strings for precision.
- The response includes total cash, margin, and product/segment-wise breakdowns.
- Supply `ALL` for any parameter to fetch a consolidated report.
- Use fields such as `CollateralValue`, `Net`, `MarginUsed` to display funding or risk information.
- Use valid session and authentication tokens to avoid errors.
