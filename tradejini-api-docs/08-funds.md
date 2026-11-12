# Funds

Available margin, cash balances, and limits.

## Limits

`GET /api/oms/limits`

to get the limits

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X GET "https://example.com/api/oms/limits" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"segment": "NSE", "totalCredits": 75000, "availMargin": 45230.75, "availCash": 45230.75, "marginUsed": 29769.25, "payIn": 10000, "payOut": 0, "peakMargin": 30000, "span": 0, "exposure": 0, "realizedPnl": 1250.5, "unrealizedPnL": -320.25, "brokerage": 40, "adHocMargin": 0, "stockCollateral": 0, "optionPremium": 0, "premium": 0, "unclearedCash": 0, "auxCash": 0, "turnOverLmt": 0, "pendOrdValLmt": 0, "turnover": 125000, "pendOrdValue": 0}` |
| `d.totalCredits` | `number` | Total credits is sum of availableCash, payIn, , adHocMargin, unclearedCash, brokerCollateralAmt,stockCollateral and auxCollateral |
| `d.availMargin` | `number` | Available margin is calculated by ( totalcredits - marginused ) |
| `d.brokerage` | `number` | Brokerage amount |
| `d.availCash` | `number` | Cash Margin available |
| `d.peakMargin` | `number` | Peak margin used by the user |
| `d.payIn` | `number` | Total Amount transferred using Payin's today |
| `d.span` | `number` | Span used |
| `d.realizedPnl` | `number` | Current realized PnL |
| `d.unrealizedPnL` | `number` | Unrealized PnL |
| `d.exposure` | `number` | Exposure margin |
| `d.adHocMargin` | `number` | Additional leverage amount or the amount added to handle system errors - by broker. |
| `d.stockCollateral` | `number` | Collateral amount calculated based on uploaded holdings |
| `d.optionPremium` | `number` | Derivative Margin |
| `d.segment` | `string` | Segment |
| `d.payOut` | `number` | Total amount requested for withdrawal today |
| `d.brkCollatAmount` | `number` | Broker Collateral Amount |
| `d.unclearedCash` | `number` | Uncleared Cash |
| `d.auxCash` | `number` | Aux day Cash |
| `d.auxCollatAmount` | `number` |  |
| `d.auxUnclearedCash` | `number` |  |
| `d.dayCash` | `number` | Additional leverage amount or the amount added to handle system errors - by broker. |
| `d.turnOverLmt` | `number` |  |
| `d.pendOrdValLmt` | `number` |  |
| `d.turnover` | `number` | Turnover |
| `d.pendOrdValue` | `number` | Pending Order value |
| `d.marginUsed` | `number` | Total margin or total fund used today |
| `d.premium` | `number` | Premium used |
| `d.brokerageDerivativesBO` | `number` | Brokerage Derivative Bracket Order |
| `d.brokerageDerivativesMargin` | `number` | Brokerage Derivative Margin |
| `d.optPremiumDerMarg` | `number` | Option premium Derivative Margin |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": [
    {
      "segment": "NSE",
      "totalCredits": 75000,
      "availMargin": 45230.75,
      "availCash": 45230.75,
      "marginUsed": 29769.25,
      "payIn": 10000,
      "payOut": 0,
      "realizedPnl": 1250.5,
      "unrealizedPnL": -320.25
    }
  ]
}
```

#### 401 Unauthorized

Unauthorized — one of: (1) invalid or expired access token — tokens expire after 24 hours, re-authenticate to get a new one; (2) `Authorization` header missing or malformed — use format `Bearer <api_key>:<access_token>`.

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. Values: `Unauthorized` |

**Example**

```json
{
  "s": "error",
  "msg": "Unauthorized"
}
```

#### 429 Too Many Requests

Too Many Requests — rate limit exceeded. General API: 10 req/sec per auth token (400 req/min).

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message indicating the rate limit was exceeded. |

**Example**

```json
{
  "s": "error",
  "msg": "Too many requests"
}
```

#### 500 Internal Server Error

Internal Server Error — retry with backoff; contact support if it persists.

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message. |

**Example**

```json
{
  "s": "error",
  "msg": "Internal server error"
}
```
