# Order Management

Six endpoints to place, modify, and cancel orders, and to access the order book, trade book, order history, and pre-order margin.

| Method | Endpoint | Processing Mode | Action |
| --- | --- | --- | --- |
| POST | `/orders` | Single/Bulk | Place new orders |
| PUT | `/orders/{brokerOrderId}` | Single | Modify a pending order |
| DELETE | `/orders/{brokerOrderId}` | Single | Cancel a pending order |
| GET | `/orders` | Single | Fetch all orders placed today |
| GET | `/orders/{brokerOrderId}` | Single | Fetch the history of a specific order |
| GET | `/trades` | Single | Fetch all executed trades for today |

All commodity segments (`MCXCOMM`, `NSECOMM`, `BSECOMM`, `NCDEXCOMM`) take `quantity` in lots for the Order and Margin APIs; every other segment takes absolute quantity. `NCDEXCOMM` uses the trading symbol as `instrumentId` (e.g. `DHANIYA10JUL25PE8600FJUL25`); every other segment uses the numeric instrument token (e.g. `2885`).

## Place Order

`POST /orders`

**Headers:** `Authorization: Bearer <userSession>`

### Request

```json
[
  {
    "instrumentId": "1594",
    "exchange": "NSEEQ",
    "transactionType": "BUY",
    "quantity": "1",
    "orderComplexity": "REGULAR",
    "product": "INTRADAY",
    "orderType": "MARKET",
    "validity": "DAY",
    "price": "1501.55",
    "slTriggerPrice": "1505.2",
    "slLegPrice": "1500",
    "targetLegPrice": "1600",
    "disclosedQuantity": "500",
    "marketProtectionPercent": "1400",
    "apiOrderSource": "XYZ",
    "algoId": "1234",
    "orderTag": "Stangle Leg 1"
  }
]
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
| `validity`* | varchar | Time the order stays active | `DAY`, `IOC` |
| `disclosedQuantity` | int | Optional — partial quantity disclosed to the market | `500` |
| `marketProtectionPercent` | double | Optional — protects the order from executing beyond this % of the reference price | `1400` |
| `apiOrderSource` | varchar | Optional — fintech partners should identify themselves here | `PlatformName1` |
| `algoId` | varchar | Optional — identifier for the placing algorithm | `1234` |
| `orderTag` | varchar | Optional — custom label for the order | `Stangle Leg 1` |

### Response

```json
{
  "status": "Ok",
  "message": "Success",
  "result": [
    { "status": "Success", "message": "Success", "brokerOrderId": "240919000000041", "requestTime": "19-Sep-2024 18:48:46" }
  ]
}
```

| Field | Description |
| --- | --- |
| `status` | Status of the request or error code (`Success`, `EC004`, ...) |
| `message` | Additional message or error description |
| `brokerOrderId` | IIFL's unique order number |
| `requestTime` | Request timestamp |

---

## Modify Order

`PUT /orders/{brokerOrderId}`

**Headers:** `Authorization: Bearer <userSession>`

### Request

```json
[
  {
    "quantity": "1",
    "orderType": "MARKET",
    "validity": "DAY",
    "price": "1501.55",
    "slTriggerPrice": "1505.2",
    "disclosedQuantity": "500",
    "marketProtectionPercent": "1400"
  }
]
```

Only send the fields you want to change (plus anything required to support that change):

| Field | Data Type | Description |
| --- | --- | --- |
| `quantity` | int | Optional |
| `orderType` | varchar | Optional — `LIMIT`, `MARKET`, `SL`, `SLM` |
| `price` | double | Conditionally required if `orderType` is `LIMIT`/`SL` |
| `slTriggerPrice` | double | Conditionally required if `orderType` is `SL`/`SLM` |
| `validity` | varchar | Optional — `DAY`, `IOC` |
| `disclosedQuantity` | int | Optional |
| `marketProtectionPercent` | double | Optional |

**Use case I** — change quantity to 15:

```json
{ "quantity": "15" }
```

**Use case II** — change from MARKET to LIMIT at 100:

```json
{ "orderType": "LIMIT", "price": "100" }
```

**Use case III** — change from LIMIT to SL with trigger 99, same price:

```json
{ "orderType": "SL", "slTriggerPrice": "99" }
```

### Response

```json
{
  "status": "Ok",
  "message": "Success",
  "result": { "status": "Success", "message": "Success", "brokerOrderId": "240919000000041", "requestTime": "19-Sep-2024 18:48:46" }
}
```

---

## Cancel Order

`DELETE /orders/{brokerOrderId}`

**Headers:** `Authorization: Bearer <userSession>`

No request body.

### Response

```json
{
  "status": "Ok",
  "message": "Success",
  "result": { "status": "Success", "message": "Success", "brokerOrderId": "240919000000041", "requestTime": "19-Sep-2024 18:48:46" }
}
```

---

## Order Book

`GET /orders`

**Headers:** `Authorization: Bearer <userSession>`

No request body.

### Response

```json
[
  {
    "clientId": "TEST102",
    "placedBy": "TEST102",
    "brokerOrderId": "240920000000124",
    "exchangeOrderId": "1100000000089930",
    "orderStatus": "cancelled",
    "formattedInstrumentName": "INFOSYS LIMITED",
    "tradingSymbol": "INFY-EQ",
    "instrumentId": "1594",
    "exchange": "NSEEQ",
    "transactionType": "BUY",
    "quantity": "1",
    "product": "INTRADAY",
    "orderComplexity": "REGULAR",
    "orderType": "LIMIT",
    "price": "180000.0",
    "averageTradedPrice": "0.0",
    "slTriggerPrice": "0.0",
    "validity": "DAY",
    "disclosedQty": "0",
    "marketProtectionPercent": "0.0",
    "exchangeTimestamp": "20-Sep-2024 16:05:33",
    "exchangeUpdateTime": "20-Sep-2024 16:05:32",
    "rejectionReason": "",
    "mainLegOrderId": "NA",
    "pendingQuantity": "1",
    "filledQuantity": "0",
    "appKey": "NA",
    "apiOrderSource": "API",
    "algoId": "",
    "source": "API",
    "orderTag": "NA",
    "brokerUpdateTime": "17-Feb-2025 06:48:39"
  }
]
```

| Field | Description |
| --- | --- |
| `clientId` | Unique client identifier |
| `placedBy` | User (client or dealer) who placed the order |
| `brokerOrderId` | IIFL Capital's order ID |
| `exchangeOrderId` | Exchange's order ID |
| `orderStatus` | Open, Complete, Rejected, Cancelled, etc. |
| `formattedInstrumentName` | Display name of the instrument |
| `tradingSymbol` | Instrument's trading symbol |
| `instrumentId` | Unique instrument identifier |
| `exchange` | Exchange where the order is placed |
| `transactionType` | Buy or sell |
| `quantity` | Shares/contracts in the order |
| `product` | Product used (intraday, delivery, ...) |
| `orderComplexity` | Regular, AMO, BO, or CO |
| `orderType` | Market, Limit, etc. |
| `price` | Limit order price |
| `averageTradedPrice` | Average execution price |
| `slTriggerPrice` | Stop-loss trigger price |
| `validity` | DAY / IOC |
| `disclosedQuantity` | Partial quantity disclosed to market |
| `marketProtectionPercent` | Market protection band |
| `exchangeTimestamp` | When the order was placed |
| `exchangeUpdateTime` | When the exchange last updated the order |
| `rejectionReason` | Rejection reason, if applicable |
| `mainLegOrderId` | Parent order ID, for BO/CO child orders |
| `pendingQuantity` | Unfilled quantity remaining |
| `filledQuantity` | Quantity filled |
| `appKey` | App that placed the order |
| `apiOrderSource` | Source the API order was placed from (fintech partner name, if applicable) |
| `algoId` | Placing algorithm's identifier |
| `source` | Platform the order was placed from (Web, App, API) |
| `orderTag` | Custom tag/label |
| `brokerUpdateTime` | Broker's last update timestamp |

---

## Order History

`GET /orders/{brokerOrderId}`

**Headers:** `Authorization: Bearer <userSession>`

No request body. Returns the same fields as [Order Book](#order-book), plus `cancelledQuantity` (quantity cancelled).

---

## Trade Book

`GET /trades`

**Headers:** `Authorization: Bearer <userSession>`

No request body.

### Response

```json
[
  {
    "clientId": "31625881",
    "placedBy": "31625881",
    "brokerOrderId": "240807000000068",
    "exchangeOrderId": "900000000000000",
    "exchangeTradeId": "893487609000000",
    "formattedInstrumentName": "IDEA VODAFONE",
    "tradingSymbol": "IDEA-EQ",
    "instrumentId": "14366",
    "exchange": "NSEEQ",
    "transactionType": "BUY",
    "product": "NORMAL",
    "orderComplexity": "REGULAR",
    "orderType": "MARKET",
    "validity": "DAY",
    "tradedPrice": "1560",
    "filledQuantity": "50",
    "fillTimestamp": "07-Aug-2024 16:14:17",
    "algoId": "algo123",
    "orderTag": "123abc"
  }
]
```

| Field | Description |
| --- | --- |
| `exchangeTradeId` | Exchange's unique trade ID |
| `tradedPrice` | Price the order was filled at |
| `filledQuantity` | Quantity filled |
| `fillTimestamp` | When the order was filled |

Other fields share the same meaning as [Order Book](#order-book).
