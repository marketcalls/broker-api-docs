# Margin

Two endpoints for calculating required margin, for a single order or a basket.

| Method | Endpoint | Processing Mode | Action |
| --- | --- | --- | --- |
| POST | `/preordermargin` | Single | Margin required for an order, considering existing positions |
| POST | `/spanexposure` | Single/Bulk | SPAN, exposure, and total margin for one or more instruments, ignoring existing positions/orders |

## Pre-order Margin

`POST /preordermargin`

**Headers:** `Authorization: Bearer <userSession>`

### Request

```json
{
  "instrumentId": "54786",
  "exchange": "NSEFO",
  "transactionType": "SELL",
  "quantity": "25",
  "orderComplexity": "REGULAR",
  "product": "NORMAL",
  "orderType": "MARKET",
  "validity": "DAY",
  "price": "1501.55",
  "slTriggerPrice": "1505.2",
  "slLegPrice": "1500",
  "targetLegPrice": "1600"
}
```

| Field | Data Type | Description | Approved/Example Values |
| --- | --- | --- | --- |
| `instrumentId`* | varchar | Unique identifier for the instrument | `1594` |
| `exchange`* | varchar | Exchange & segment | `NSEEQ`, `NSEFO`, `BSEEQ`, `BSEFO`, `NSECURR`, `BSECURR`, `MCXCOMM`, `NSECOMM`, `BSECOMM`, `NCDEXCOMM` |
| `transactionType`* | varchar | Buy or sell | `BUY`, `SELL` |
| `quantity`* | int | Units to trade | `100` |
| `orderComplexity`* | varchar | Order complexity | `REGULAR`, `AMO`, `BO`, `CO` |
| `product`* | varchar | Product type | `NORMAL`, `INTRADAY`, `DELIVERY`, `BNPL` |
| `orderType`* | varchar | Order type | `LIMIT`, `MARKET`, `SL`, `SLM` |
| `price` | double | Conditionally required if `orderType` is `LIMIT`/`SL` | `1501.55` |
| `slTriggerPrice` | double | Conditionally required if `orderType` is `SL`/`SLM` | `1505.2` |
| `slLegPrice` | double | Conditionally required if `orderComplexity` is `BO`/`CO` — exit price | `1500` |
| `targetLegPrice` | double | Conditionally required if `orderComplexity` is `BO` — profit booking price | `1600` |

### Response

```json
{
  "totalCashAvailable": "10006024.00",
  "preOrderMargin": "76624.00",
  "postOrderMargin": "88710.73",
  "currentOrderMargin": "12086.73",
  "rmsvalidationMessage": "OK",
  "fundShort": "0.00"
}
```

| Field | Description |
| --- | --- |
| `totalCashAvailable` | Total cash available |
| `preOrderMargin` | Portfolio margin used before this order executes |
| `postOrderMargin` | Portfolio margin used after this order executes |
| `currentOrderMargin` | Margin required to place this order |
| `rmsvalidationMessage` | `OK` / `NOT_OK` — whether RMS will allow the order |
| `fundShort` | Fund shortage, if any |

---

## SPAN and Exposure Margin

`POST /spanexposure`

**Headers:** `Authorization: Bearer <userSession>`

### Request

```json
[
  { "instrumentId": "35089", "exchange": "NSEFO", "transactionType": "BUY", "quantity": 25 },
  { "instrumentId": "35005", "exchange": "NSEFO", "transactionType": "SELL", "quantity": 25 }
]
```

| Field | Data Type | Description | Approved/Example Values |
| --- | --- | --- | --- |
| `instrumentId`* | varchar | Unique identifier for the instrument | `1594` |
| `exchange`* | varchar | Exchange & segment | `NSEEQ`, `NSEFO`, `BSEEQ`, `BSEFO`, `NSECURR`, `BSECURR`, `MCXCOMM`, `NSECOMM`, `BSECOMM`, `NCDEXCOMM` |
| `transactionType`* | varchar | Buy or sell | `BUY`, `SELL` |
| `quantity`* | int | Units to trade | `100` |

### Response

```json
{ "span": "11090.00", "exposureMargin": "4122.17", "totalMargin": "15212.17", "buyPremium": "0.00" }
```

| Field | Description |
| --- | --- |
| `span` | Minimum required margin based on worst-case risk scenarios for derivative positions |
| `exposureMargin` | Additional cushion margin for unexpected market moves |
| `totalMargin` | Combined SPAN + exposure margin |
| `buyPremium` | Total premium required to buy the option contracts in the request |
