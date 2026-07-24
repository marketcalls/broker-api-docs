# Brokerage and Charges APIs

Three endpoints that calculate transaction charges for a client, instrument, and order, including a full breakup of brokerage and statutory/transaction charges.

> These endpoints use a **different base URL** than the rest of the API:
> `https://brkschemeapp.azurewebsites.net/api/brokerageScheme` (cash & F&O), `https://brkschemeapp-points.azurewebsites.net/api/brokerageScheme` (commodity).

| Method | Endpoint | Processing Mode | Action |
| --- | --- | --- | --- |
| POST | `https://brkschemeapp.azurewebsites.net/api/brokerageScheme/getCashBrokerageCharges` | Single | Brokerage & charges for a cash-segment order |
| POST | `https://brkschemeapp.azurewebsites.net/api/brokerageScheme/getFnoCharges` | Single | Brokerage & statutory charges for an F&O order |
| POST | `https://brkschemeapp-points.azurewebsites.net/api/brokerageScheme/getCommodityCharges` | Single | Brokerage & statutory charges for a commodity order |

**Headers:** `Authorization: Bearer <userSession>`

## Request

```json
{
  "clientCode": "31775624",
  "scripDetails": {
    "scripCode": 532648,
    "exchange": "b",
    "exchangeType": "c"
  },
  "orderDetails": {
    "orderPrice": 83.45,
    "product": "d",
    "qty": 5,
    "multiplier": 1,
    "orderType": "b"
  }
}
```

| Field | Description | Values |
| --- | --- | --- |
| `clientCode` | Unique client identifier | `TEST102` |
| `scripCode` | Unique instrument identifier | `408065` |
| `exchange` | Exchange of the instrument | `n`: NSE, `b`: BSE, `m`: MCX |
| `exchangeType` | Exchange segment | `c`: Cash, `d`: Derivatives (F&O of NSE/BSE/MCX), `y`: NSE & BSE Commodity |
| `orderPrice` | Order price | `150` |
| `product` | Product type | `d`: delivery, `t`: intraday |
| `qty` | Units to trade | `50` |
| `multiplier` | Lot-size multiplier for P&L | `1` |
| `orderType` | Buy or sell | `b`: buy, `s`: sell |

## Response

```json
{
  "succeeded": true,
  "message": [],
  "errors": [],
  "data": {
    "clientCode": "31798624",
    "orderDetails": { "orderPrice": 83.45, "netQty": 5, "turnOver": 417.25 },
    "scripDetails": { "scripCode": 532648, "exchange": "b", "exchangeType": "c" },
    "transactionCharges": {
      "brokerage": 0.04,
      "charges": {
        "exchangeCharges": { "key": "0.00375% of Turnover", "value": 0.02 },
        "stt": { "key": "0.1% of Turnover", "value": 0.42 },
        "sebiCharges": { "key": "0.0001% of Turnover", "value": 0 },
        "stampDuty": { "key": "0.015% of Turnover", "value": 0.06 },
        "dpCharges": { "key": "Zero Charges", "value": 0 },
        "clearingCharges": { "key": "Zero Charges", "value": 0 },
        "investoryProtectionfund": { "key": "Zero Charges", "value": 0 },
        "gst": { "key": "18% on (Brokerage + Exchange Charges + SEBI Fees + Clearing Charges)", "value": 0.01 }
      },
      "totalCharges": 0.55
    }
  }
}
```

| Field | Description |
| --- | --- |
| `turnOver` | Total traded value (`orderPrice × netQty`) |
| `brokerage` | Broker's fee for the order |
| `exchangeCharges` | Fee levied by the exchange on turnover |
| `stt` | Securities Transaction Tax |
| `sebiCharges` | Regulatory charges imposed by SEBI |
| `stampDuty` | State-mandated duty on traded value |
| `dpCharges` | Depository Participant fee (equity delivery) |
| `clearingCharges` | Clearing & settlement charges |
| `investoryProtectionfund` | Investor Protection Fund contribution |
| `gst` | GST on brokerage and applicable charges |
| `totalCharges` | Sum of brokerage and all applicable charges |
