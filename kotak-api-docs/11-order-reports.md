# Order Report APIs

Covers: Order Book, Orderbook by Order ID, Order History, Trade Book.

## 1. Introduction

Kotak Securities offers APIs to fetch your:

- **Order Book** — all open, completed, and rejected orders
- **Order book by order ID**
- **Order History** — all order status changes/updates for a particular order
- **Trade Book** — details of completed trades for the trading day

## 2. API Endpoints

| API | Endpoint (after `<Base URL>`) | Method |
| --- | --- | --- |
| Order Book | `/quick/user/orders` | GET |
| Orderbook by order id | `/quick/user/orders/<order_no>` | GET |
| Order History | `/quick/order/history` | POST |
| Trade Book | `/quick/user/trades` | GET |

Replace `<Base URL>` with the relevant Kotak environment base URL provided in the response from the `/tradeApiValidate` API.

## 3. Headers

Applicable to all APIs:

| Name | Type | Description |
| --- | --- | --- |
| accept | string | Should always be `application/json` |
| Sid | string | session sid generated on login |
| Auth | string | session token generated on login |
| neo-fin-key | string | static value: `neotradeapi` |
| Content-Type | string | Always `application/x-www-form-urlencoded` |

## 4. Requests

### 4.1 GET Order Book

```bash
curl -X GET "<baseUrl>/quick/user/orders" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi"
```

### 4.2 GET Order Book by Order ID

```bash
curl -X GET "<baseUrl>/quick/user/orders/<order_no>" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi"
```

No request body or parameters required.

### 4.3 POST Order History

Send `jData` as URL-encoded JSON.

```bash
curl -X POST "<baseUrl>/quick/order/history" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi" \
--data-urlencode 'jData={"nOrdNo":"250720000007242"}'
```

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| nOrdNo | string | Nest order number for which history is required | Yes |

### 4.4 GET Trade Book

```bash
curl -X GET "<baseUrl>/quick/user/trades" \
-H "Auth: <session_token>" \
-H "Sid: <session_sid>" \
-H "neo-fin-key: neotradeapi"
```

No request body or parameters required.

## 5. Responses

### 5.1 Order Book Response

```json
{
  "stat": "Ok",
  "data": [
    {
      "nOrdNo": "250720000007242",
      "ordSt": "rejected",
      "trdSym": "ITBEES-EQ",
      "qty": 1,
      "prc": "0.00",
      "avgPrc": "0.00",
      "trnsTp": "B",
      "prcTp": "L",
      "vldt": "DAY"
    },
    {
      "nOrdNo": "250720000007588",
      "ordSt": "after market order req received",
      "trdSym": "ITBEES-EQ",
      "qty": 1,
      "prc": "0.00",
      "avgPrc": "0.00"
    }
  ],
  "stCode": 200
}
```

| Field | Type | Description |
| --- | --- | --- |
| nOrdNo | string | Nest order number |
| ordSt / stat | string | Order status ("open", "rejected", etc.) |
| trdSym | string | Trading symbol e.g., "ITBEES-EQ" |
| qty | int | Quantity |
| prc | string | Placed price |
| avgPrc | string | Average traded price |
| trnsTp | string | Transaction type — "B"=Buy, "S"=Sell |
| prcTp | string | Order type: "L"=Limit, "MKT"=Market, etc. |
| vldt | string | Validity (DAY/IOC) |
| rejRsn | string | Rejection reason if any |
| exSeg | string | Exchange segment e.g., "nse_cm" |
| ordGenTp | string | "AMO" for after-market orders, else blank |
| ordDtTm | string | Order date/time |
| stat | string | Overall status at top level: "Ok" for success |

### 5.2 Order History Response

```json
{
  "stat": "Ok",
  "stCode": 200,
  "data": [
    {
      "nOrdNo": "250720000007242",
      "flDtTm": "20-Jul-2025 20:21:42",
      "ordSt": "rejected",
      "rejRsn": "ADAPTER is down",
      "qty": 1,
      "prc": "0.00",
      "avgPrc": "0.00",
      "prod": "MIS",
      "trnsTp": "B",
      "prcTp": "L"
    },
    {
      "nOrdNo": "250720000007242",
      "flDtTm": "20-Jul-2025 20:21:42",
      "ordSt": "open pending"
    }
  ]
}
```

| Field | Type | Description |
| --- | --- | --- |
| nOrdNo | string | Nest order number |
| ordSt | string | Status at this stage |
| flDtTm | string | Date/time for the update |
| qty | int | Order quantity at this status |
| prc | string | Order price at this status |
| avgPrc | string | Average price at this stage |
| prod | string | Product type ("MIS", "CNC") |
| trnsTp | string | Transaction type ("B"=Buy, "S"=Sell) |
| prcTp | string | Order type ("L", "MKT", etc.) |
| rejRsn | string | Rejection reason if applicable |

### 5.3 Trade Book Response

```json
{
  "stat": "Ok",
  "stCode": 200,
  "data": [
    {
      "nOrdNo": "221007000000354",
      "trdSym": "TCS-EQ",
      "qty": 11,
      "avgPrc": "3194.00",
      "fldQty": 11,
      "flDt": "07-Oct-2022",
      "exOrdId": "1100000000047870",
      "exTm": "07-Oct-2022 13:04:14",
      "prcTp": "L",
      "prod": "CNC",
      "ordDur": "DAY",
      "trnsTp": "B",
      "usrId": "PRABHAT"
    }
  ]
}
```

| Field | Type | Description |
| --- | --- | --- |
| nOrdNo | string | Nest order number |
| trdSym | string | Trading symbol |
| qty | int | Trade quantity |
| avgPrc | string | Average execution price |
| fldQty | int | Filled quantity |
| flDt | string | Trade date |
| exOrdId | string | Exchange order ID |
| exTm | string | Trade execution datetime |
| prcTp | string | Order type (L/MKT/SL/etc.) |
| prod | string | Product code ("CNC", "MIS", etc.) |
| ordDur | string | Order validity (DAY/IOC) |
| trnsTp | string | Transaction type (B/S) |
| usrId | string | User/client ID |

### Common Response Fields

| Field | Type | Description |
| --- | --- | --- |
| stat | string | "Ok" for success, "Not_Ok" for errors |
| stCode | int | HTTP status code (200 = success, else error) |
| data | array | List of order/trade detail objects |
| emsg | string | Present only for errors: error message |

## 6. Usage Notes

- Use correct headers with valid session and auth tokens.
- Order Book / Trade Book: access all your recent orders/trades for the day.
- Order History: always provide the correct `nOrdNo` to fetch its full lifecycle/status changes.
- Handle `"stat": "Not_Ok"` and use `emsg` for debugging.
- Field meanings and data formats remain consistent across all order-related APIs.
- Reference the scrip master for symbol/segment mapping as needed.
