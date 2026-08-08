# Orders

Place, modify, cancel, and track regular orders; positions, holdings, trades, and margin.

## Orders

`GET /api/oms/orders`

to get list of orders placed

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `symDetails` | `boolean` | No | Sending symDetails:'true' - will provide the symbol object in response for every record. Symbol object contains details such as price-tick, lotsize, token etc..,. Values: `true`, `false` |

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X GET "https://example.com/api/oms/orders" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `array<object>` |  |
| `d[].symId` | `string` |  |
| `d[].status` | `string` | Values: `open`, `completed`, `rejected`, `cancelled` |
| `d[].qty` | `number` | Order quantity |
| `d[].side` | `string` | Values: `buy`, `sell` |
| `d[].type` | `string` | Values: `limit`, `market`, `stoplimit`, `stopmarket` |
| `d[].validity` | `string` | Values: `day`, `ioc`, `eos`, `gtc` |
| `d[].validTill` | `string` |  |
| `d[].source` | `string` |  |
| `d[].limitPrice` | `number` |  |
| `d[].exchOrderId` | `string` |  |
| `d[].discQty` | `number` |  |
| `d[].product` | `string` | Values: `delivery`, `normal`, `intraday`, `cover`, `bracket` |
| `d[].exchTime` | `string` | Exchange order time in the format 'dd-MM-yyyy HH:mm:ss' |
| `d[].orderId` | `string` |  |
| `d[].orderTime` | `string` | Order time in the format 'dd-MM-yyyy HH:mm:ss' |
| `d[].avgPrice` | `number` |  |
| `d[].amo` | `boolean` |  |
| `d[].fillQty` | `number` |  |
| `d[].trigPrice` | `number` | This is required only for stoploss limit and stoploss market orders |
| `d[].reason` | `string` |  |
| `d[].pendingQty` | `number` |  |
| `d[].sym` | `object` |  |
| `d[].sym.id` | `string` |  |
| `d[].sym.symbol` | `string` |  |
| `d[].sym.tradSymbol` | `string` |  |
| `d[].sym.exchange` | `string` |  |
| `d[].sym.lot` | `string` |  |
| `d[].sym.instrument` | `string` |  |
| `d[].sym.companyName` | `string` |  |
| `d[].sym.expiry` | `string` |  |
| `d[].sym.dispSymbol` | `string` |  |
| `d[].sym.asset` | `string` |  |
| `d[].sym.empty` | `boolean` |  |
| `d[].mktProt` | `number` |  |
| `d[].stopTrigPrice` | `number` | Stop loss leg order trigger price. |
| `d[].targetPrice` | `number` | Target order or Profit order price |
| `d[].trailingStopPrice` | `number` | Trailing stop loss price. |
| `d[].remarks` | `string` | Remarks added while placing an order. |
| `d[].legType` | `string` | Leg Type. Applicable only for Cover and Bracket order. Values: `main`, `stoploss`, `target` |
| `d[].mainLegOrderId` | `string` | Main leg order id. Applicable only for Bracket and Cover order. It is used to exit the order. |
| `d[].orderValue` | `number` |  |
| `d[].tradeValue` | `number` | 'tradeValue' is filled quantity * average price |
| `d[].algType` | `string` | Algo type 'trailing' or 'regular'. Values: `trailing`, `regular` |
| `d[].modifiable` | `boolean` |  |
| `d[].cancellable` | `boolean` |  |
| `d[].exitable` | `boolean` |  |
| `d[].retriable` | `boolean` |  |
| `d[].orderPoll` | `boolean` |  |
| `d[].stopLimitPrice` | `number (double)` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": [
    {
      "symId": "EQT_RELIANCE_EQ_NSE",
      "status": "open",
      "qty": 10,
      "side": "b",
      "type": "l",
      "product": "cnc",
      "orderId": "210115000000001",
      "limitPrice": 2440,
      "fillQty": 0,
      "pendingQty": 10
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

---

## Place Order

`POST /api/oms/place-order`

to place the order

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `symId` | `string` | Yes | Unique identifier of the symbol. Example: `EQT_RELIANCE_EQ_NSE` |
| `qty` | `number` | Yes | No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50. Example: `10` |
| `side` | `string` | Yes | Order side 'buy' or 'sell'. Values: `buy`, `sell` |
| `type` | `string` | Yes | Price type of an order. Values: `limit`, `market`, `stoplimit`, `stopmarket` |
| `product` | `string` | Yes | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `intraday`, `normal` |
| `limitPrice` | `number` | No | This is required only for limit and stop limit orders. Example: `2700.55` |
| `trigPrice` | `number` | No | This is required only for stoploss limit and stoploss market orders |
| `validity` | `string` | Yes | Validity of an order, EOS is applicable for BSE scrips only. Values: `day`, `ioc`, `eos`, `gtc` |
| `discQty` | `number` | No | Disclosed quantity of an order. Example: `0` |
| `amo` | `boolean` | No | Pass this field as true to place an amo order. |
| `mktProt` | `number` | No | Market order protection percentage. Applicable only for market orders. Example: `5` |
| `remarks` | `string` | No | Any tag or message to track in orderbook.Allowed length upto 10 Characters. Please note remarks more than 10 characters will be stripped out. |

### Example Request

```bash
curl -X POST "https://example.com/api/oms/place-order" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'symId=EQT_RELIANCE_EQ_NSE&qty=10&side=buy&type=limit&product=delivery&validity=day'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `no-data`, `error` |
| `d` | `object` | Example: `{"msg": "Order Placed Successfully", "orderId": "210115000000001"}` |
| `d.msg` | `string` |  |
| `d.orderId` | `string` |  |
| `msg` | `string` |  |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "Order Placed Successfully",
    "orderId": "210115000000001"
  }
}
```

#### 400 Bad Request

Bad Request

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message describing which field failed validation or why the request was rejected. Values: `Internal Error occurred. Kindly try again.`, `Input validation failed. Kindly check your input contains required fields for the request` |

**Example**

```json
{
  "s": "error",
  "msg": "Input validation failed. Kindly check your input contains required fields for the request"
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

Too Many Requests — place order rate limit exceeded (10 req/sec per auth token).

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

---

## Modify Order

`PUT /api/oms/modify-order`

to modify the pending order

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `symId` | `string` | Yes | Unique identifier of the symbol. Example: `EQT_RELIANCE_EQ_NSE` |
| `orderId` | `string` | Yes | Order id of an order which needs modification. This id will be received in orders service |
| `qty` | `number` | Yes | Total order quantity after the modification. ( Filled Qty (if nonzero) + (Modified Qty or Pending Qty)). Example: If the order quantity is 100, out of that 60 is already filled, and if we are modifying the pending qty from 40 to 70 then qty => (60 + 70) = 130 should be sent. Example: `1` |
| `type` | `string` | Yes | Price type of an order. Values: `limit`, `market`, `stoplimit`, `stopmarket` |
| `limitPrice` | `number` | No | This is required only for limit and stop limit orders. Example: `2700.55` |
| `trigPrice` | `number` | No | This is required only for stoploss limit and stoploss market orders |
| `validity` | `string` | Yes | Validity of an order, EOS is applicable for BSE scrips only. Values: `day`, `ioc`, `eos`, `gtc` |
| `discQty` | `number` | No | Disclosed quantity of an order. Example: `0` |
| `mktProt` | `number` | No | Market order protection percentage. Applicable only for market orders. Example: `5` |
| `side` | `string` | No | Order side 'buy' or 'sell'. Values: `buy`, `sell` |

### Example Request

```bash
curl -X PUT "https://example.com/api/oms/modify-order" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'symId=EQT_RELIANCE_EQ_NSE&orderId=string&qty=1&type=limit&validity=day'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "Order Modified Successfully", "orderId": "210115000000001"}` |
| `d.msg` | `string` |  |
| `d.orderId` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "Order Modified Successfully",
    "orderId": "210115000000001"
  }
}
```

#### 400 Bad Request

Bad Request

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message describing which field failed validation or why the request was rejected. Values: `Internal Error occurred. Kindly try again.`, `Input validation failed. Kindly check your input contains required fields for the request` |

**Example**

```json
{
  "s": "error",
  "msg": "Input validation failed. Kindly check your input contains required fields for the request"
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

---

## Cancel Order

`DELETE /api/oms/cancel-order`

to cancel the pending order

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `orderId` | `string` | Yes | Order id of an order which needs to be cancelled. Order id is received from orders response |

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X DELETE "https://example.com/api/oms/cancel-order?orderId=string" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "Order Cancelled Successfully", "orderId": "210115000000001"}` |
| `d.msg` | `string` |  |
| `d.orderId` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "Order Cancelled Successfully",
    "orderId": "210115000000001"
  }
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

---

## History

`GET /api/oms/history`

to get an order history of an order

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `orderId` | `string` | Yes | Order id of an order. This will be received in orders response |

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X GET "https://example.com/api/oms/history?orderId=string" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"orderId": "210115000000001", "status": "filled", "reason": "", "avgPrice": 2450.75, "totalFillQty": 10, "remarks": "", "history": [{"msg": "Order placed", "fillId": "", "fillPrice": 0, "fillQty": 0, "time": "09:15:00"}, {"msg": "Order filled", "fillId": "210115000000001-1", "fillPrice": 2450.75, "fillQty": 10, "time": "09:32:15"}]}` |
| `d.orderId` | `string` |  |
| `d.status` | `string` | Values: `open`, `completed`, `rejected`, `cancelled` |
| `d.reason` | `string` |  |
| `d.avgPrice` | `number` |  |
| `d.totalFillQty` | `number` |  |
| `d.remarks` | `string` | Remarks added while placing an order. |
| `d.history` | `array<object>` |  |
| `d.history[].msg` | `string` |  |
| `d.history[].fillId` | `string` |  |
| `d.history[].fillPrice` | `number` |  |
| `d.history[].fillQty` | `number` |  |
| `d.history[].time` | `string` | Order log time in the format 'dd-MM-yyyy HH:mm:ss' |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "orderId": "210115000000001",
    "status": "filled",
    "avgPrice": 2450.75,
    "totalFillQty": 10,
    "history": [
      {
        "msg": "Order placed",
        "fillPrice": 0,
        "fillQty": 0,
        "time": "09:15:00"
      },
      {
        "msg": "Order filled",
        "fillId": "210115000000001-1",
        "fillPrice": 2450.75,
        "fillQty": 10,
        "time": "09:32:15"
      }
    ]
  }
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

---

## Trades

`GET /api/oms/trades`

to get a list of trade records

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `symDetails` | `boolean` | No | Sending symDetails:'true' - will provide the symbol object in response for every record. Symbol object contains details such as price-tick, lotsize, token etc..,. Values: `true`, `false` |

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X GET "https://example.com/api/oms/trades" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `array<object>` |  |
| `d[].symId` | `string` |  |
| `d[].side` | `string` | Values: `buy`, `sell` |
| `d[].type` | `string` | Values: `limit`, `market`, `stoplimit`, `stopmarket` |
| `d[].validity` | `string` | Values: `day`, `ioc`, `eos`, `gtc` |
| `d[].product` | `string` | Values: `delivery`, `normal`, `intraday`, `cover`, `bracket` |
| `d[].orderId` | `string` |  |
| `d[].fillId` | `string` |  |
| `d[].fillQty` | `number` |  |
| `d[].fillPrice` | `number` |  |
| `d[].fillValue` | `number` |  |
| `d[].time` | `string` | Traded time in the format 'dd-MM-yyyy HH:mm:ss' |
| `d[].exchOrderId` | `string` |  |
| `d[].avgPrice` | `number` |  |
| `d[].sym` | `object` |  |
| `d[].sym.id` | `string` |  |
| `d[].sym.symbol` | `string` |  |
| `d[].sym.tradSymbol` | `string` |  |
| `d[].sym.exchange` | `string` |  |
| `d[].sym.lot` | `string` |  |
| `d[].sym.instrument` | `string` |  |
| `d[].sym.companyName` | `string` |  |
| `d[].sym.expiry` | `string` |  |
| `d[].sym.dispSymbol` | `string` |  |
| `d[].sym.asset` | `string` |  |
| `d[].sym.empty` | `boolean` |  |
| `d[].remarks` | `string` | Remarks added while placing an order. |
| `d[].legType` | `string` | Leg Type. Applicable only for Cover and Bracket order. |
| `d[].mainLegOrderId` | `string` | Main leg order id. Applicable only for Bracket and Cover order. It is used to exit the order. |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": [
    {
      "symId": "EQT_RELIANCE_EQ_NSE",
      "side": "b",
      "type": "l",
      "product": "cnc",
      "orderId": "210115000000001",
      "fillId": "210115000000001-1",
      "fillQty": 5,
      "fillPrice": 2450.75,
      "fillValue": 12253.75,
      "time": "09:32:15"
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

---

## Positions 

`GET /api/oms/positions`

to get a list of positions records

**MTM Calculations:**
- **Realized:** realizedPnl
- **UnRealized:** ( netQty * ( LTP - netAvgPrice)) * multiplier * pricefactor
- **Total MTM:** Realized + UnRealized

**P&L Calculations:**
- **Realized:** realizedOrgPnl
- **UnRealized:** ( netQty * ( LTP - netOrgAvgPrice)) * multiplier * pricefactor
- **Total P&L:** Realized + UnRealized

**Day Positions - MTM Calculations:**
- **Realized:** dayRealizedPnl
- **UnRealized:** ( dayQty * ( LTP - dayAvg)) * multiplier * pricefactor
- **Total Day MTM:** Realized + UnRealized

**Note:**
- For the commodity (MCX), the net quantity should be multiplied by the lot size in the above calculations.
- The LTP mentioned above should be retrieved from real-time updates via the streaming SDK

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `symDetails` | `boolean` | No | Sending symDetails:'true' - will provide the symbol object in response for every record. Symbol object contains details such as price-tick, lotsize, token etc..,. Values: `true`, `false` |

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X GET "https://example.com/api/oms/positions" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `array<object>` |  |
| `d[].symId` | `string` |  |
| `d[].product` | `string` | Values: `delivery`, `normal`, `intraday`, `cover`, `bracket` |
| `d[].buyQty` | `number` |  |
| `d[].buyValue` | `number` |  |
| `d[].buyAvgPrice` | `number` |  |
| `d[].sellQty` | `number` |  |
| `d[].sellValue` | `number` |  |
| `d[].sellAvgPrice` | `number` |  |
| `d[].cfQty` | `number` | Carry forward positions quantity |
| `d[].cfValue` | `number` | Carry forward position value and it is calculated using cfQty * cfAvgPrice * multiplier * pricefactor. |
| `d[].cfAvgPrice` | `number` | The settlement price of the scrip from the last trading day, is used to calculate the mark-to-market (MTM) of the positions |
| `d[].netQty` | `number` |  |
| `d[].netAvgPrice` | `number` | The net average price is based on today's positions and carryforward positions. For carryforward positions, the average would be the settlement price from the last trading day (cfavgprice), while for today's positions, the average would be the day average price (dayavgprice) |
| `d[].netValue` | `number` | Net value of the position based on the net average price (netavgprice) |
| `d[].realizedPnl` | `number` | Realized pnl value |
| `d[].priceFactor` | `number` | Used for pnl calculations. PriceFactor:(General Numerator * Price Numerator)/(General Denominator * Price Denopminator) |
| `d[].multiplier` | `number` |  |
| `d[].sym` | `object` |  |
| `d[].sym.id` | `string` |  |
| `d[].sym.symbol` | `string` |  |
| `d[].sym.tradSymbol` | `string` |  |
| `d[].sym.exchange` | `string` |  |
| `d[].sym.lot` | `string` |  |
| `d[].sym.instrument` | `string` |  |
| `d[].sym.companyName` | `string` |  |
| `d[].sym.expiry` | `string` |  |
| `d[].sym.dispSymbol` | `string` |  |
| `d[].sym.asset` | `string` |  |
| `d[].sym.empty` | `boolean` |  |
| `d[].cfOrgAvgPrice` | `number` | The actual buy/sell price of the position, is used to calculate the overall PNL of the positions. |
| `d[].cfOrgValue` | `number` | Carry forward position original value and it is calculated using cfQty * cfOrgAvgPrice * multiplier * pricefactor |
| `d[].netOrgAvgPrice` | `number` | The net original average price is based on today's positions and carryforward positions. For carryforward positions, the average would be the actual buy or sell price of the scrip, while for today's positions, the average would be the day average price (dayavgprice) |
| `d[].netOrgValue` | `number` | Net original value of the position based on the net original average price (netorgavgprice) |
| `d[].realizedOrgPnl` | `number` |  |
| `d[].dayPos` | `object` | Today's position details. Example: `{"dayQty": 5, "dayAvg": 2450.75, "dayRealizedPnl": 125, "dayNetValue": 12253.75, "convertPos": false, "dayPremium": 0}` |
| `d[].dayPos.dayQty` | `number` |  |
| `d[].dayPos.dayAvg` | `number` |  |
| `d[].dayPos.dayRealizedPnl` | `number` |  |
| `d[].dayPos.dayNetValue` | `number` | dayNetValue is calculated by 'dayBuyValue - daySellValue'. |
| `d[].dayPos.convertPos` | `boolean` |  |
| `d[].dayPos.dayPremium` | `number` |  |
| `d[].convertPos` | `boolean` |  |
| `d[].netPremium` | `number` |  |
| `d[].transHistory` | `boolean` |  |
| `d[].createTSL` | `boolean` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": [
    {
      "symId": "EQT_RELIANCE_EQ_NSE",
      "product": "mis",
      "buyQty": 10,
      "buyAvgPrice": 2450.75,
      "sellQty": 5,
      "sellAvgPrice": 2475.65,
      "netQty": 5,
      "netAvgPrice": 2450.75,
      "realizedPnl": 124.5
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

---

## Convert Position 

`POST /api/oms/convert-position`

to convert a position from one product type to another

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `symId` | `string` | Yes | Unique identifier of the symbol. Example: `EQT_SBIN_EQ_NSE` |
| `qty` | `number` | Yes | No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50. Example: `1` |
| `fromProduct` | `string` | Yes | Current product type of a position record. Values: `delivery`, `intraday`, `normal` |
| `toProduct` | `string` | Yes | Product to which the user wants to convert. Values: `delivery`, `intraday`, `normal` |
| `side` | `string` | Yes | Order side 'buy' or 'sell'. Values: `buy`, `sell` |

### Example Request

```bash
curl -X POST "https://example.com/api/oms/convert-position" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'symId=EQT_SBIN_EQ_NSE&qty=1&fromProduct=delivery&toProduct=delivery&side=buy'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "Success"}` |
| `d.msg` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "Position Converted Successfully"
  }
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

---

## Order Margin

`POST /api/oms/margin`

to get the margin required and available margin info while placing an order

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `symId` | `string` | Yes | Unique identifier of the symbol. Example: `EQT_RELIANCE_EQ_NSE` |
| `qty` | `number` | Yes | 'qty' is number of shares for which required margin, for modification order 'qty' should be 'fillQty' + 'modified qty'. Example: `1` |
| `side` | `string` | Yes | Order side 'buy' or 'sell'. Values: `buy`, `sell`; Example: `buy` |
| `type` | `string` | Yes | Price type of an order. Values: `limit`, `market`, `stoplimit`, `stopmarket` |
| `product` | `string` | Yes | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `intraday`, `normal`, `bracket`, `cover` |
| `limitPrice` | `number` | No | This is required only for limit and stop limit orders |
| `trigPrice` | `number` | No | This is required only for stoploss limit and stoploss market orders |
| `stopTrigPrice` | `number` | No | Stop loss leg order trigger price. Example: `15` |
| `orgQty` | `number` | No | Original quantity is applicable for modification order, original quantity is 'qty' from orderbook |
| `orgLimitPrice` | `number` | No | Original limit price is applicable for modification order, original limit price is limit price from orderbook |
| `orgTrigPrice` | `number` | No | Original trigger price is applicable for modification order, original trigger price is trigger price from orderbook |
| `orgStopTrigPrice` | `number` | No | Original stop loss price is applicable only for Cover and Bracket order modification, original stop loss price is stop loss price from orderbook. |
| `fillQty` | `number` | No | fillQty is partially filled quantity, fillQty is 'fillQty' from orderbook. |
| `orderId` | `string` | No | Order id is applicable for bracket and cover order modification |
| `mainLegOrderId` | `string` | No | Mainleg order id field is applicable for bracket and cover order |

### Example Request

```bash
curl -X POST "https://example.com/api/oms/margin" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'symId=EQT_RELIANCE_EQ_NSE&qty=1&side=buy&type=limit&product=delivery'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"availableMargin": 45230.75, "requiredMargin": 12500, "shortfall": 0, "holdQty": 0, "remarks": "", "edisAuthRequired": false}` |
| `d.availableMargin` | `number` | Available margin to trade |
| `d.requiredMargin` | `number` | Required margin to trade |
| `d.shortfall` | `number` |  |
| `d.holdQty` | `number` | This is applicable only for SELL order of Equity ( Delivery ) |
| `d.remarks` | `string` | Remarks is applicable for failure cases |
| `d.edisAuthRequired` | `boolean` | 'edisAuthEnabled' flag should be consume in case of edis navigation |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "availableMargin": 45230.75,
    "requiredMargin": 12500,
    "shortfall": 0,
    "holdQty": 0,
    "edisAuthRequired": false
  }
}
```

#### 400 Bad Request

Bad Request

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Response status. Always `error` for error responses. Values: `error` |
| `msg` | `string` | Error message describing which field failed validation or why the request was rejected. Values: `Internal Error occurred. Kindly try again.`, `Input validation failed. Kindly check your input contains required fields for the request` |

**Example**

```json
{
  "s": "error",
  "msg": "Input validation failed. Kindly check your input contains required fields for the request"
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

---

## Basket Order Margin

`POST /api/oms/basket-margin`

Basket order margin

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/json` *(required)*

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `basketOrders` | `array<object>` | No | Basket order is basket of multiple orders |
| `basketOrders[].symId` | `string` | Yes | Unique identifier of the symbol. Example: `EQT_RELIANCE_EQ_NSE` |
| `basketOrders[].qty` | `number` | Yes | No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50. Example: `1` |
| `basketOrders[].limitPrice` | `number` | No | This is required only for limit and stop limit orders |
| `basketOrders[].side` | `string` | Yes | Order side 'buy' or 'sell'. Values: `buy`, `sell`; Example: `buy` |
| `basketOrders[].type` | `string` | Yes | Price type of an order. Values: `limit`, `market`, `stoplimit`, `stopmarket` |
| `basketOrders[].product` | `string` | Yes | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `intraday`, `normal` |
| `basketOrders[].trigPrice` | `number` | No | This is required only for stoploss limit and stoploss market orders |

### Example Request

```bash
curl -X POST "https://example.com/api/oms/basket-margin" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"requiredMargin": 37500, "finalMargin": 32000, "existingMarginUsed": 29769.25, "combinedRequiredMargin": 67269.25, "combinedFinalMargin": 61769.25, "availableMargin": 45230.75}` |
| `d.requiredMargin` | `number` | Required margin |
| `d.finalMargin` | `number` | Final margin |
| `d.existingMarginUsed` | `number` | Existing margin used |
| `d.combinedRequiredMargin` | `number` | Combined required margin is a combination of required margin of an order and margin used |
| `d.combinedFinalMargin` | `number` | Combined Final margin is a combination of final margin of an order and margin used |
| `d.availableMargin` | `number` | Available margin to trade |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "requiredMargin": 37500,
    "finalMargin": 32000,
    "availableMargin": 45230.75,
    "combinedRequiredMargin": 67269.25
  }
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

---

## Holdings 

`GET /api/oms/holdings`

to get the list of holding records

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `symDetails` | `boolean` | No | Sending symDetails:'true' - will provide the symbol object in response for every record. Symbol object contains details such as price-tick, lotsize, token etc..,. Values: `true`, `false` |

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X GET "https://example.com/api/oms/holdings" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"hasNonPoaRecord": false, "holdings": [{"symId": "EQT_RELIANCE_EQ_NSE", "qty": 10, "avgPrice": 2450.75, "saleableQty": 10, "t1Qty": 0, "dpQty": 10, "realizedPnl": 0}, {"symId": "EQT_INFY_EQ_NSE", "qty": 5, "avgPrice": 1380, "saleableQty": 5, "t1Qty": 0, "dpQty": 5, "realizedPnl": 125.5}]}` |
| `d.holdings` | `array<object>` |  |
| `d.holdings[].symId` | `string` |  |
| `d.holdings[].sym` | `object` |  |
| `d.holdings[].sym.id` | `string` |  |
| `d.holdings[].sym.symbol` | `string` |  |
| `d.holdings[].sym.tradSymbol` | `string` |  |
| `d.holdings[].sym.exchange` | `string` |  |
| `d.holdings[].sym.lot` | `string` |  |
| `d.holdings[].sym.instrument` | `string` |  |
| `d.holdings[].sym.companyName` | `string` |  |
| `d.holdings[].sym.expiry` | `string` |  |
| `d.holdings[].sym.dispSymbol` | `string` |  |
| `d.holdings[].sym.asset` | `string` |  |
| `d.holdings[].sym.empty` | `boolean` |  |
| `d.holdings[].qty` | `number` | Quantity is sum of ( btstQuantity, holdingQuantity, brokerQuantity, unPledgedQty, beneficiaryQuantity, MaxOf(nonPoaQuantity,dpQuantity)) minus tradedQuantity |
| `d.holdings[].avgPrice` | `number` | Average buy price |
| `d.holdings[].t1Qty` | `number` | T1 or BTST quantity |
| `d.holdings[].saleableQty` | `number` | Saleable quantity is sum of ( btstQuantity, holdingQuantity, unPledgedQty, beneficiaryQuantity, dpQuantity ) minus tradedQty |
| `d.holdings[].pledgeQty` | `number` | Collateral or pledged quantity |
| `d.holdings[].nonPoaQty` | `number` | Non POA quantity |
| `d.holdings[].dpQty` | `number` | DP holding quantity |
| `d.holdings[].benQty` | `number` | Beneficiary quantity |
| `d.holdings[].unpledgedQty` | `number` | Unpledged quantity |
| `d.holdings[].brokerColQty` | `number` | Broker collateral |
| `d.holdings[].btstColqty` | `number` | BTST collateral quantity |
| `d.holdings[].usedQty` | `number` | Holding quantity used today |
| `d.holdings[].tradedQty` | `number` | Holding quantity traded today |
| `d.holdings[].realizedPnl` | `number` | 'realizedPnL |
| `d.holdings[].totalQty` | `number` |  |
| `d.holdings[].transHistory` | `boolean` |  |
| `d.holdings[].dayQty` | `number` |  |
| `d.hasNonPoaRecord` | `boolean` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "hasNonPoaRecord": false,
    "holdings": [
      {
        "symId": "EQT_RELIANCE_EQ_NSE",
        "qty": 10,
        "avgPrice": 2450.75,
        "saleableQty": 10
      },
      {
        "symId": "EQT_INFY_EQ_NSE",
        "qty": 5,
        "avgPrice": 1380,
        "saleableQty": 5
      }
    ]
  }
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
