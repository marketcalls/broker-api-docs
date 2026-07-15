# Order Management

> Source: https://api-docs.indstocks.com/normal_orders/

Endpoints for placing, modifying, cancelling, and tracking regular orders and trades.

## Endpoints Overview

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/order` | Place a new order |
| POST | `/order/modify` | Modify a pending order |
| POST | `/order/cancel` | Cancel a pending order |
| GET | `/order-book` | Retrieve the day's orders |
| GET | `/order` | Get a single order's details |
| GET | `/trades/{order_id}` | Get trades for a specific order |
| GET | `/trade-book` | Get all executed trades for a segment |

---

## Place Order

**Endpoint:** `POST /order`

### Request Parameters

| Parameter | Type | Required | Details |
|-----------|------|----------|---------|
| `txn_type` | string | ✅ | `"BUY"` or `"SELL"` |
| `exchange` | string | ✅ | `"NSE"` or `"BSE"` |
| `segment` | string | ✅ | `"DERIVATIVE"` or `"EQUITY"` |
| `product` | string | ✅ | `"MARGIN"`, `"INTRADAY"`, or `"CNC"` |
| `order_type` | string | ✅ | `"LIMIT"` or `"MARKET"` |
| `validity` | string | ✅ | `"DAY"` or `"IOC"` |
| `security_id` | string | ✅ | Instrument identifier (from Instruments Master) |
| `qty` | integer | ✅ | Order quantity |
| `algo_id` | string | ✅ | `"99999"` (NSE) or `"9999999999999999"` (BSE) |
| `limit_price` | number | ❌ | Required for `LIMIT` orders |
| `is_amo` | boolean | ❌ | After-Market Order flag |

### Request

```bash
curl --location 'https://api.indstocks.com/order' \
--header 'Authorization: YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
  "txn_type": "BUY",
  "exchange": "BSE",
  "segment": "EQUITY",
  "product": "CNC",
  "order_type": "LIMIT",
  "limit_price": 850,
  "validity": "DAY",
  "security_id": "500112",
  "qty": 1,
  "is_amo": false,
  "algo_id": "99999"
}'
```

### Response

```json
{
  "status": "success",
  "data": {
    "order_id": "DRV-29301125",
    "order_status": "O-PENDING"
  }
}
```

---

## Modify Order

**Endpoint:** `POST /order/modify`

### Request Parameters

| Parameter | Type | Required | Details |
|-----------|------|----------|---------|
| `order_id` | string | ✅ | Order to modify |
| `segment` | string | ✅ | `"DERIVATIVE"` or `"EQUITY"` |
| `qty` | integer | ✅ | New quantity |
| `limit_price` | number | ✅ | New limit price |

### Request

```bash
curl --location 'https://api.indstocks.com/order/modify' \
--header 'Authorization: YOUR_ACCESS_TOKEN' \
--data '{
  "segment": "DERIVATIVE",
  "limit_price": 73,
  "qty": 75,
  "order_id": "DRV-2049"
}'
```

> Up to **25 modifications** are allowed per order.

---

## Cancel Order

**Endpoint:** `POST /order/cancel`

### Request Parameters

| Parameter | Type | Required | Details |
|-----------|------|----------|---------|
| `order_id` | string | ✅ | Order to cancel |
| `segment` | string | ✅ | `"DERIVATIVE"` or `"EQUITY"` |

### Request

```bash
curl --location 'https://api.indstocks.com/order/cancel' \
--header 'Authorization: YOUR_ACCESS_TOKEN' \
--data '{
  "segment": "DERIVATIVE",
  "order_id": "DRV-2049"
}'
```

---

## Get Order Book

Retrieves all orders placed during the current trading day.

**Endpoint:** `GET /order-book`

### Request

```bash
curl --location 'https://api.indstocks.com/order-book' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
  "status": "success",
  "data": [{
    "created_at": "2025-07-02T15:47:07.079035+05:30",
    "updated_at": "2025-07-02T17:43:02.635379+05:30",
    "user_id": "710354",
    "security_id": "58757",
    "isin": "",
    "name": "NIFTY 3 JUL 27400 CE",
    "id": "GTT-2914581",
    "exch_order_id": "",
    "txn_type": "SELL",
    "exchange": "NSE",
    "segment": "DERIVATIVE",
    "product": "MARGIN",
    "order_type": "OCO",
    "validity": "",
    "mkt_type": "NL",
    "off_mkt_flag": "",
    "traded_qty": 0,
    "requested_qty": 75,
    "requested_price": "",
    "traded_price": "",
    "sl_trigger_price": "0.3",
    "sl_limit_price": "0.2",
    "tgt_trigger_price": "0.75",
    "tgt_limit_price": "",
    "status": "CANCELLED",
    "extra_info": ""
  }]
}
```

---

## Get Order Details

**Endpoint:** `GET /order`

### Request Parameters

| Parameter | Type | Required | Details |
|-----------|------|----------|---------|
| `order_id` | string | ✅ | Order identifier |
| `segment` | string | ✅ | `"DERIVATIVE"` or `"EQUITY"` |

### Request

```bash
curl --location --request GET 'https://api.indstocks.com/order' \
--header 'Authorization: YOUR_ACCESS_TOKEN' \
--data '{
  "order_id": "DRV-27373858",
  "segment": "DERIVATIVE"
}'
```

---

## Get Trades for an Order

**Endpoint:** `GET /trades/{order_id}`

### Request

```bash
curl --location 'https://api.indstocks.com/trades/DRV-2049' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
  "status": "success",
  "data": [{
    "trade_id": "INDT20250512XYZ789",
    "order_id": "INDM20250512ABC123",
    "exchange_order_id": "1000000001234567",
    "exchange_trade_id": "2000000009876543",
    "exchange_segment": "NSE_EQ",
    "security_id": "12345",
    "trading_symbol": "RELIANCE-EQ",
    "transaction_type": "BUY",
    "product_type": "CNC",
    "quantity": 5,
    "price": 2500.45,
    "trade_timestamp": "2025-05-12T10:15:35Z"
  }]
}
```

---

## Get Trade Book

Returns all executed trades for a segment.

**Endpoint:** `GET /trade-book`

### Query Parameters

| Parameter | Type | Required | Details |
|-----------|------|----------|---------|
| `segment` | string | ✅ | `"EQUITY"` or `"DERIVATIVE"` |

### Request

```bash
curl --location 'https://api.indstocks.com/trade-book?segment=DERIVATIVE' \
--header 'Authorization: YOUR_ACCESS_TOKEN'

curl --location 'https://api.indstocks.com/trade-book?segment=EQUITY' \
--header 'Authorization: YOUR_ACCESS_TOKEN'
```

### Response

```json
{
  "status": "success",
  "data": [{
    "fill_id": 1020280,
    "exch_order_id": "2400000124991381",
    "quantity": 2425,
    "price": 1.55,
    "trade_date": "2025-11-11T17:48:23+05:30",
    "trade_serial_no": "17628437030186581215",
    "scrip_code": "99133"
  }]
}
```

---

## Reference Values

**Transaction types:** `BUY`, `SELL`

**Exchanges:** `NSE`, `BSE`

**Segments:** `EQUITY`, `DERIVATIVE`

**Products:** `CNC` (equity delivery), `INTRADAY`, `MARGIN` (derivatives)

**Order types:** `LIMIT`, `MARKET`

**Validity:** `DAY`, `IOC`

**Order ID prefixes:** `EQ-` (equity), `DRV-` (derivative), `GTT-` (smart/GTT child)

### Order Status Values

`QUEUED`, `O-PENDING`, `SL-PENDING`, `PROCESSING`, `ABORTED`, `INITIATED`, `SUCCESS`,
`CANCELLED`, `MODIFIED`, `PENDING`, `EXPIRED`, `FAILED`, `PARTIALLY FILLED`,
`PARTIALLY FILLED - CANCELLED`, `PARTIALLY FILLED - EXPIRED`
