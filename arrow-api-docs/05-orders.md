> Source: https://docs.arrow.trade/rest-api/orders/

# Orders API

The Orders API provides enterprise-grade trading capabilities with real-time order management, portfolio tracking, and detailed execution analytics. Built for algorithmic trading, portfolio management platforms, and advanced trading applications.

## Base Configuration

### Authentication & Headers

All API requests require the following authentication headers:

Header | Type | Required | Description
---|---|---|---
`appID` | string | ✓ | Your application identifier
`token` | string | ✓ | User authentication token

### Base URL

```
https://edge.arrow.trade
```

## Endpoint Reference

Method | Endpoint | Description
---|---|---
`POST` | `/order/:variety` | Place new trading orders
`PATCH` | `/order/:variety/:order_id` | Modify existing open orders
`DELETE` | `/order/:variety/:order_id` | Cancel pending orders
`GET` | `/order/:order_id` | Retrieve order details and history
`GET` | `/user/orders` | Get complete order book
`GET` | `/user/trades` | Access executed trades

## Trading Parameters

### Order Varieties

Variety | Description | Risk Management
---|---|---
`regular` | Standard order execution | Basic order controls

### Exchange Support

Exchange | Code | Market Segment | Regular Trading Hours
---|---|---|---
**NSE** | `NSE` | Equity | 9:15 AM - 3:30 PM
**NFO** | `NFO` | Futures & Options | 9:15 AM - 3:30 PM
**BSE** | `BSE` | Equity | 9:15 AM - 3:30 PM
**BFO** | `BFO` | Futures & Options | 9:15 AM - 3:30 PM

### Order Types

Type | Code | Description | Use Case
---|---|---|---
**Market Order** | `MKT` | Plain `MKT` is disabled by default on the API (regulatory). Pass `mpp: true` to mimic a market order: the platform sends the order at the Upper Limit or DPR, depending on instrument type | Immediate-style execution via the supported `mpp` path
**Limit Order** | `LMT` | Execute at specified price or better | Price control priority
**Stop Loss Limit** | `SL-LMT` | Limit order activated at trigger | Risk management with price control
**Stop Loss Market** | `SL-MKT` | Market order activated at trigger | Risk management with speed priority

Market orders (`MKT`) and `mpp`

Under current regulations, **market (`MKT`) orders are disabled by default** when placing orders through the API. Arrow Trade supports an optional flag **`mpp`** (boolean). When set to **`true`** , the platform sends a **`LIMIT`** order at the **Upper Limit** or **DPR (Daily Price Range)** boundary, **depending on the instrument type** , to mimic market-style execution. In rare cases of **extreme volatility or sharp price movement** , this can still result in an **open (unfilled/partially filled) order**.

### Product Categories

Product | Code | Description | Settlement
---|---|---|---
**Intraday** | `I` | Same-day position closure | Auto-squared off at 3:15 PM
**Delivery** | `C` | Equity delivery orders | T+1 settlement
**Normal** | `M` | F&O orders | Standard margin

### Order Validity

Validity | Code | Description | Expiry
---|---|---|---
**Day Order** | `DAY` | Valid until market close | End of trading session
**Immediate or Cancel** | `IOC` | Execute immediately or cancel | Immediate

## Order Execution

### Place Regular Order

Execute standard trading orders with full parameter control.

Endpoint Details

**Method:** `POST`
**URL:** `/order/regular`
**Header:** Required (`appID` \+ `token`)

#### Request Parameters

Parameter | Type | Required | Description
---|---|---|---
`exchange` | string | ✓ | Exchange identifier (NSE, NFO, BSE, etc.)
`symbol` | string | ✓ | Trading symbol
`quantity` | string | ✓ | Order quantity
`transactionType` | string | ✓ | Transaction type (`B` = Buy, `S` = Sell)
`order` | string | ✓ | Order type (LMT, MKT, SL-LMT, SL-MKT)
`product` | string | ✓ | Product type (`I`, `C`, `M`)
`price` | string | ✓ | Order price (use "0" for market orders)
`validity` | string | ✓ | Order validity (`DAY`, `IOC`)
`disclosedQty` | string | - | Disclosed quantity for iceberg orders
`remarks` | string | - | Custom tags for order identification (max 16 characters)
`mpp` | boolean | - | When `true`, mimics a market order for supported types by using Upper Limit or DPR per instrument (see note above). Default is effectively `false` / omitted

#### Place Regular Order

```bash
curl --location 'https://edge.arrow.trade/order/regular' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>' \
--data '{
    "exchange": "NSE",
    "quantity": "2",
    "disclosedQty": "0",
    "remarks": "234",
    "product": "I",
    "symbol": "IDEA-EQ",
    "transactionType": "B",
    "order": "LMT",
    "price": "7.5",
    "validity": "DAY"
}'
```

#### Success Response

```json
{
    "data": {
        "orderNo": "24012400000321",
        "requestTime": "21:45:55 24-01-2024"
    },
    "status": "success"
}
```

### Modify Regular Order

Endpoint Details

**Method:** `PATCH`
**URL:** `/order/regular/{orderID}`
**Header:** Required (`appID` \+ `token`)

#### Request Parameters

Parameter | Type | Required | Description
---|---|---|---
`exchange` | string | ✓ | Exchange identifier (NSE, NFO, BSE, etc.)
`symbol` | string | ✓ | Trading symbol
`quantity` | string | ✓ | Order quantity
`transactionType` | string | ✓ | Transaction type (`B` = Buy, `S` = Sell)
`order` | string | ✓ | Order type (LMT, MKT, SL-LMT, SL-MKT)
`product` | string | ✓ | Product type (`I`, `C`, `M`)
`price` | string | ✓ | Order price (use "0" for market orders)
`validity` | string | ✓ | Order validity (`DAY`, `IOC`)
`disclosedQty` | string | - | Disclosed quantity for iceberg orders
`remarks` | string | - | Custom tags for order identification (max 16 characters)
`mpp` | boolean | - | When `true`, mimics a market order for supported types by using Upper Limit or DPR per instrument (see note above). Default is effectively `false` / omitted

#### Modify Regular Order

```bash
curl --location --request PATCH 'https://edge.arrow.trade/order/regular/24032900000003' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>' \
--data '{
    "exchange": "NSE",
    "quantity": "2",
    "disclosedQty": "0",
    "remarks": "234",
    "product": "I",
    "symbol": "IDEA-EQ",
    "transactionType": "B",
    "order": "LMT",
    "price": "7.5",
    "validity": "DAY"
}'
```

#### Success Response

```json
{
    "data": {
        "orderNo": "24012400000321",
        "requestTime": "21:45:55 24-01-2024"
    },
    "status": "success"
}
```

### Cancel Order

Cancel pending orders that are no longer required.

Endpoint Details

**Method:** `DELETE`
**URL:** `/order/:variety/:order_id`
**Header:** Required (`appID` \+ `token`)

#### Request Example

```bash
curl --location --request DELETE 'https://edge.arrow.trade/order/regular/24032900000003' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

#### Success Response

```json
{
    "data": {
        "message": "order cancellation request accepted"
    },
    "status": "success"
}
```

## Order Tracking

### Get Order Details

Retrieve comprehensive order history and execution details for specific orders.

Endpoint Details

**Method:** `GET`
**URL:** `/order/:order_id`
**Header:** Required (`appID` \+ `token`)

#### Request Example

```bash
curl --location 'https://edge.arrow.trade/order/24030700000042' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

```json
{
    "data": [
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26100",
            "id": "25120202000010",
            "price": "34",
            "quantity": "75",
            "product": "M",
            "orderStatus": "COMPLETE",
            "reportType": "Fill",
            "transactionType": "B",
            "order": "MKT",
            "cumulativeFillQty": "75",
            "fillShares": "75",
            "averagePrice": "34",
            "exchangeOrderID": "1400000055208129",
            "cancelQuantity": "0",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "token": "46799",
            "orderTime": "2025-12-02T10:16:16",
            "exchangeUpdateTime": "2025-12-02T10:16:16",
            "exchangeTime": "2025-12-02T10:16:16",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "0",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        },
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26100",
            "id": "25120202000010",
            "price": "34",
            "quantity": "75",
            "product": "M",
            "orderStatus": "OPEN",
            "reportType": "NewAck",
            "transactionType": "B",
            "order": "MKT",
            "cumulativeFillQty": "0",
            "fillShares": "0",
            "averagePrice": "0",
            "exchangeOrderID": "1400000055208129",
            "cancelQuantity": "0",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "token": "46799",
            "orderTime": "2025-12-02T10:16:16",
            "exchangeUpdateTime": "2025-12-02T10:16:16",
            "exchangeTime": "2025-12-02T10:16:16",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "75",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        },
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26100",
            "id": "25120202000010",
            "price": "0",
            "quantity": "75",
            "product": "M",
            "orderStatus": "PENDING",
            "reportType": "PendingNew",
            "transactionType": "B",
            "order": "MKT",
            "cumulativeFillQty": "0",
            "fillShares": "0",
            "averagePrice": "0",
            "exchangeOrderID": "0",
            "cancelQuantity": "0",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "token": "46799",
            "orderTime": "2025-12-02T10:16:16",
            "orderSource": "WEB",
            "leavesQuantity": "75",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        }
    ],
    "status": "success"
}
```

### Order Status Types

Status | Description | Next Action
---|---|---
`PENDING` | Order submitted, awaiting confirmation | Monitor for updates
`OPEN` | Order active in the market | Can modify or cancel
`COMPLETE` | Order fully executed | Review execution details
`CANCELLED` | Order cancelled by user/system | No further action
`REJECTED` | Order rejected by exchange | Check rejection reason

## Portfolio Views

### Get Order Book

Access your complete order book for comprehensive order tracking.

Endpoint Details

**Method:** `GET`
**URL:** `/user/orders`
**Header:** Required (`appID` \+ `token`)

#### Request Example

```bash
curl --location 'https://edge.arrow.trade/user/orders' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

#### Response Schema

```json
{
    "data": [
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NSE",
            "symbol": "IDEA-EQ",
            "id": "25120202000013",
            "price": "10",
            "quantity": "10",
            "product": "I",
            "orderStatus": "CANCELLED",
            "reportType": "Canceled",
            "transactionType": "B",
            "order": "LMT",
            "cumulativeFillQty": "0",
            "fillShares": "0",
            "averagePrice": "0",
            "exchangeOrderID": "1100000029104706",
            "cancelQuantity": "10",
            "remarks": "234",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.01",
            "lotSize": "1",
            "token": "14366",
            "orderTime": "2025-12-02T11:33:07",
            "exchangeUpdateTime": "2025-12-02T11:33:07",
            "exchangeTime": "2025-12-02T11:33:07",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "0",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        },
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NSE",
            "symbol": "IDEA-EQ",
            "id": "25120202000012",
            "rejectReason": "The price lies outside the DPR range",
            "price": "7.5",
            "quantity": "2",
            "product": "I",
            "orderStatus": "REJECTED",
            "reportType": "Rejected",
            "transactionType": "B",
            "order": "LMT",
            "cumulativeFillQty": "0",
            "fillShares": "0",
            "averagePrice": "0",
            "exchangeOrderID": "0",
            "cancelQuantity": "0",
            "remarks": "234",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.01",
            "lotSize": "1",
            "token": "14366",
            "orderTime": "2025-12-02T11:32:31",
            "exchangeUpdateTime": "2025-12-02T11:32:31",
            "exchangeTime": "2025-12-02T11:32:31",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "0",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        },
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26200",
            "id": "25120202000011",
            "price": "10.4",
            "quantity": "150",
            "product": "M",
            "orderStatus": "COMPLETE",
            "reportType": "Fill",
            "transactionType": "S",
            "order": "MKT",
            "cumulativeFillQty": "150",
            "fillShares": "75",
            "averagePrice": "10.45",
            "exchangeOrderID": "1600000050515119",
            "cancelQuantity": "0",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "token": "46803",
            "orderTime": "2025-12-02T10:16:16",
            "exchangeUpdateTime": "2025-12-02T10:16:16",
            "exchangeTime": "2025-12-02T10:16:16",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "0",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        },
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26100",
            "id": "25120202000010",
            "price": "34",
            "quantity": "75",
            "product": "M",
            "orderStatus": "COMPLETE",
            "reportType": "Fill",
            "transactionType": "B",
            "order": "MKT",
            "cumulativeFillQty": "75",
            "fillShares": "75",
            "averagePrice": "34",
            "exchangeOrderID": "1400000055208129",
            "cancelQuantity": "0",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "token": "46799",
            "orderTime": "2025-12-02T10:16:16",
            "exchangeUpdateTime": "2025-12-02T10:16:16",
            "exchangeTime": "2025-12-02T10:16:16",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "0",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        },
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "BFO",
            "symbol": "SENSEX04DEC25P85000",
            "id": "25120202000009",
            "price": "138.95",
            "quantity": "20",
            "product": "M",
            "orderStatus": "COMPLETE",
            "reportType": "Fill",
            "transactionType": "S",
            "order": "MKT",
            "cumulativeFillQty": "20",
            "fillShares": "20",
            "averagePrice": "139.9",
            "exchangeOrderID": "1764648423443199412",
            "cancelQuantity": "0",
            "validity": "DAY",
            "pricePrecision": "0",
            "tickSize": "0.05",
            "lotSize": "20",
            "token": "2131475",
            "orderTime": "2025-12-02T09:38:50",
            "exchangeUpdateTime": "2025-12-02T09:38:50",
            "exchangeTime": "2025-12-02T09:38:50",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "0",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        },
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26100",
            "id": "25120202000008",
            "price": "77.55",
            "quantity": "75",
            "product": "M",
            "orderStatus": "COMPLETE",
            "reportType": "Fill",
            "transactionType": "S",
            "order": "LMT",
            "cumulativeFillQty": "75",
            "fillShares": "75",
            "averagePrice": "79.55",
            "exchangeOrderID": "1400000007439929",
            "cancelQuantity": "0",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "token": "46799",
            "orderTime": "2025-12-02T09:21:34",
            "exchangeUpdateTime": "2025-12-02T09:21:34",
            "exchangeTime": "2025-12-02T09:21:34",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "0",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        },
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26200",
            "id": "25120202000007",
            "price": "29.45",
            "quantity": "150",
            "product": "M",
            "orderStatus": "COMPLETE",
            "reportType": "Fill",
            "transactionType": "B",
            "order": "LMT",
            "cumulativeFillQty": "150",
            "fillShares": "150",
            "averagePrice": "29.15",
            "exchangeOrderID": "1600000007077847",
            "cancelQuantity": "0",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "token": "46803",
            "orderTime": "2025-12-02T09:21:29",
            "exchangeUpdateTime": "2025-12-02T09:21:29",
            "exchangeTime": "2025-12-02T09:21:29",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "0",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        },
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26100",
            "id": "25120202000006",
            "rejectReason": "\u003cerr\u003eMARGIN ERROR: MARGIN BREACH,SHORTFALL=40091.080000",
            "price": "82.95",
            "quantity": "75",
            "product": "M",
            "orderStatus": "REJECTED",
            "reportType": "Rejected",
            "transactionType": "S",
            "order": "LMT",
            "cumulativeFillQty": "0",
            "fillShares": "0",
            "averagePrice": "0",
            "exchangeOrderID": "0",
            "cancelQuantity": "0",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "token": "46799",
            "orderTime": "2025-12-02T09:21:18",
            "exchangeUpdateTime": "2025-12-02T09:21:18",
            "exchangeTime": "2025-12-02T09:21:18",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "0",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        },
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25P26200",
            "id": "25120202000003",
            "price": "74.2",
            "quantity": "75",
            "product": "M",
            "orderStatus": "COMPLETE",
            "reportType": "Fill",
            "transactionType": "B",
            "order": "MKT",
            "cumulativeFillQty": "75",
            "fillShares": "75",
            "averagePrice": "74.45",
            "exchangeOrderID": "1600000006186330",
            "cancelQuantity": "0",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "token": "46804",
            "orderTime": "2025-12-02T09:20:34",
            "exchangeUpdateTime": "2025-12-02T09:20:34",
            "exchangeTime": "2025-12-02T09:20:34",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "0",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        },
        {
            "userID": "AJ0001",
            "accountID": "AJ0001",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25P26200",
            "id": "25120202000002",
            "price": "77.55",
            "quantity": "75",
            "product": "M",
            "orderStatus": "COMPLETE",
            "reportType": "Fill",
            "transactionType": "S",
            "order": "LMT",
            "cumulativeFillQty": "75",
            "fillShares": "75",
            "averagePrice": "77.55",
            "exchangeOrderID": "1600000005064178",
            "cancelQuantity": "0",
            "validity": "DAY",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "token": "46804",
            "orderTime": "2025-12-02T09:19:28",
            "exchangeUpdateTime": "2025-12-02T09:19:28",
            "exchangeTime": "2025-12-02T09:19:28",
            "orderSource": "WEB",
            "isAck": true,
            "leavesQuantity": "0",
            "twap": {},
            "gorilla": {},
            "vwap": {},
            "slicer": {},
            "pov": {}
        }
    ],
    "status": "success"
}
```

### Get Trade Book

Review all executed trades for performance analysis and reconciliation.

Endpoint Details

**Method:** `GET`
**URL:** `/user/trades`
**Header:** Required (`appID` \+ `token`)

#### Response Schema

```json
{
    "data": [
        {
            "userID": "AJ0001",
            "accountID": "",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26100",
            "id": "25120202000010",
            "quantity": "75",
            "product": "M",
            "transactionType": "B",
            "order": "MKT",
            "fillShares": "75",
            "averagePrice": "34",
            "exchangeOrderID": "1400000055208129",
            "remarks": "",
            "retention": "",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "customFirm": "",
            "fillTime": "1764650776",
            "fillID": "4349940",
            "fillPrice": "34",
            "fillQuantity": "75",
            "orderSource": "1",
            "token": "46799",
            "exchangeUpdateTime": "2025-12-02T10:16:16",
            "snoOrderDirection": "",
            "snoOrderID": "",
            "requestTime": "2025-12-02T10:16:16",
            "errorMessage": ""
        },
        {
            "userID": "AJ0001",
            "accountID": "",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26200",
            "id": "25120202000011",
            "quantity": "150",
            "product": "M",
            "transactionType": "S",
            "order": "MKT",
            "fillShares": "75",
            "averagePrice": "10.4",
            "exchangeOrderID": "1600000050515119",
            "remarks": "",
            "retention": "",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "customFirm": "",
            "fillTime": "1764650776",
            "fillID": "2781151",
            "fillPrice": "10.45",
            "fillQuantity": "75",
            "orderSource": "1",
            "token": "46803",
            "exchangeUpdateTime": "2025-12-02T10:16:16",
            "snoOrderDirection": "",
            "snoOrderID": "",
            "requestTime": "2025-12-02T10:16:16",
            "errorMessage": ""
        },
        {
            "userID": "AJ0001",
            "accountID": "",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26200",
            "id": "25120202000011",
            "quantity": "150",
            "product": "M",
            "transactionType": "S",
            "order": "MKT",
            "fillShares": "150",
            "averagePrice": "10.4",
            "exchangeOrderID": "1600000050515119",
            "remarks": "",
            "retention": "",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "customFirm": "",
            "fillTime": "1764650776",
            "fillID": "2781152",
            "fillPrice": "10.45",
            "fillQuantity": "75",
            "orderSource": "1",
            "token": "46803",
            "exchangeUpdateTime": "2025-12-02T10:16:16",
            "snoOrderDirection": "",
            "snoOrderID": "",
            "requestTime": "2025-12-02T10:16:16",
            "errorMessage": ""
        },
        {
            "userID": "AJ0001",
            "accountID": "",
            "exchange": "BFO",
            "symbol": "SENSEX04DEC25P85000",
            "id": "25120202000009",
            "quantity": "20",
            "product": "M",
            "transactionType": "S",
            "order": "MKT",
            "fillShares": "20",
            "averagePrice": "138.95",
            "exchangeOrderID": "1764648423443199412",
            "remarks": "",
            "retention": "",
            "pricePrecision": "0",
            "tickSize": "0.05",
            "lotSize": "20",
            "customFirm": "",
            "fillTime": "1764648530",
            "fillID": "950660",
            "fillPrice": "139.9",
            "fillQuantity": "20",
            "orderSource": "1",
            "token": "2131475",
            "exchangeUpdateTime": "2025-12-02T09:38:50",
            "snoOrderDirection": "",
            "snoOrderID": "",
            "requestTime": "2025-12-02T09:38:50",
            "errorMessage": ""
        },
        {
            "userID": "AJ0001",
            "accountID": "",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26100",
            "id": "25120202000008",
            "quantity": "75",
            "product": "M",
            "transactionType": "S",
            "order": "LMT",
            "fillShares": "75",
            "averagePrice": "77.55",
            "exchangeOrderID": "1400000007439929",
            "remarks": "",
            "retention": "",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "customFirm": "",
            "fillTime": "1764647494",
            "fillID": "765295",
            "fillPrice": "79.55",
            "fillQuantity": "75",
            "orderSource": "1",
            "token": "46799",
            "exchangeUpdateTime": "2025-12-02T09:21:34",
            "snoOrderDirection": "",
            "snoOrderID": "",
            "requestTime": "2025-12-02T09:21:34",
            "errorMessage": ""
        },
        {
            "userID": "AJ0001",
            "accountID": "",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25C26200",
            "id": "25120202000007",
            "quantity": "150",
            "product": "M",
            "transactionType": "B",
            "order": "LMT",
            "fillShares": "150",
            "averagePrice": "29.45",
            "exchangeOrderID": "1600000007077847",
            "remarks": "",
            "retention": "",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "customFirm": "",
            "fillTime": "1764647489",
            "fillID": "597377",
            "fillPrice": "29.15",
            "fillQuantity": "150",
            "orderSource": "1",
            "token": "46803",
            "exchangeUpdateTime": "2025-12-02T09:21:29",
            "snoOrderDirection": "",
            "snoOrderID": "",
            "requestTime": "2025-12-02T09:21:29",
            "errorMessage": ""
        },
        {
            "userID": "AJ0001",
            "accountID": "",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25P26200",
            "id": "25120202000003",
            "quantity": "75",
            "product": "M",
            "transactionType": "B",
            "order": "MKT",
            "fillShares": "75",
            "averagePrice": "74.2",
            "exchangeOrderID": "1600000006186330",
            "remarks": "",
            "retention": "",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "customFirm": "",
            "fillTime": "1764647434",
            "fillID": "539591",
            "fillPrice": "74.45",
            "fillQuantity": "75",
            "orderSource": "1",
            "token": "46804",
            "exchangeUpdateTime": "2025-12-02T09:20:34",
            "snoOrderDirection": "",
            "snoOrderID": "",
            "requestTime": "2025-12-02T09:20:34",
            "errorMessage": ""
        },
        {
            "userID": "AJ0001",
            "accountID": "",
            "exchange": "NFO",
            "symbol": "NIFTY02DEC25P26200",
            "id": "25120202000002",
            "quantity": "75",
            "product": "M",
            "transactionType": "S",
            "order": "LMT",
            "fillShares": "75",
            "averagePrice": "77.55",
            "exchangeOrderID": "1600000005064178",
            "remarks": "",
            "retention": "",
            "pricePrecision": "2",
            "tickSize": "0.05",
            "lotSize": "75",
            "customFirm": "",
            "fillTime": "1764647368",
            "fillID": "453996",
            "fillPrice": "77.55",
            "fillQuantity": "75",
            "orderSource": "1",
            "token": "46804",
            "exchangeUpdateTime": "2025-12-02T09:19:28",
            "snoOrderDirection": "",
            "snoOrderID": "",
            "requestTime": "2025-12-02T09:19:26",
            "errorMessage": ""
        }
    ],
    "status": "success"
}
```

## Error Handling

Standard HTTP status codes with detailed error responses:

```json
{
    "status": "error",
    "message": "Insufficient margin for this order",
    "code": "MARGIN_ERROR"
}
```

Common Error Codes

  * **400 Bad Request:** Invalid order parameters or missing fields
  * **401 Unauthorized:** Invalid or expired authentication credentials
  * **403 Forbidden:** Insufficient trading permissions or account restrictions
  * **409 Conflict:** Order conflicts with existing positions or limits
  * **429 Too Many Requests:** Rate limit exceeded
  * **500 Internal Server Error:** Exchange connectivity or system issues

## Integration Guidelines

Best Practices

  * **Pre-flight Validation:** Check margin requirements before placing orders
  * **Order Status Monitoring:** Implement real-time order status tracking
  * **Error Recovery:** Build robust error handling and retry mechanisms
  * **Rate Limit Management:** Implement intelligent request throttling
  * **Idempotency:** Use unique tags to prevent duplicate order submissions

Market Hours

Orders can be placed during market hours and as AMO (After Market Orders) for next-day execution. Always verify exchange-specific trading hours and holiday schedules.

Risk Considerations

  * Always validate order parameters before submission
  * Monitor position limits and margin requirements
  * Implement proper stop-loss mechanisms for risk management
  * Test thoroughly in paper trading environments before live deployment
