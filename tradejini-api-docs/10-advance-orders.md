# Advance Orders

Bracket (BO), Cover (CO), GTT, and OCO order types.

## Place Bracket Order

`POST /api/oms/place-order/bo`

to place the bracket order

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `symId` | `string` | Yes | Unique identifier of the symbol. Example: `EQT_RELIANCE_EQ_NSE` |
| `qty` | `number` | Yes | No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50. Example: `1` |
| `side` | `string` | Yes | Order side 'buy' or 'sell'. Values: `buy`, `sell` |
| `type` | `string` | Yes | Price type of an order. Values: `limit`, `market`, `stoplimit` |
| `limitPrice` | `number` | No | Main leg order price. Required only for 'limit' and 'stoplimit' orders. Example: `2400` |
| `trigPrice` | `number` | No | This is applicable only for the main leg order and required only if the order type is 'stoplimit' |
| `mktProt` | `number` | No | This is applicable only for the main leg order and required only if the order type is 'market'. Example: `5` |
| `stopTrigPrice` | `number` | Yes | Stop loss leg trigger price. This is the difference of main leg price and the stop loss leg trigger price. If your main leg order price is '2400' and if you want to set the stop loss trigger at '2300' then pass the difference '100' in this field. Example: `100` |
| `targetPrice` | `number` | Yes | Target leg price. This is the difference of main leg price and the target leg price. If your main leg order price is '2400' and if you want to set the target or profit order price for 2500 then pass the difference '100' in this field. Example: `100` |
| `trailingStopPrice` | `number` | No | Trailing stop loss price. Example: `10` |
| `remarks` | `string` | No | Any tag or message to track in orderbook.Allowed length upto 10 Characters. Please note remarks more than 10 characters will be stripped out. |

### Example Request

```bash
curl -X POST "https://example.com/api/oms/place-order/bo" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'symId=EQT_RELIANCE_EQ_NSE&qty=1&side=buy&type=limit&stopTrigPrice=100&targetPrice=100'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "Order Placed Successfully", "orderId": "210115000000001"}` |
| `d.msg` | `string` |  |
| `d.orderId` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

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

## Modify Bracket Order

`PUT /api/oms/modify-order/bo`

to modify the bracket order

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
| `type` | `string` | Yes | Price type of an order. Values: `limit`, `market`, `stoplimit` |
| `limitPrice` | `number` | No | Main leg order price. Required only for 'limit' and 'stoplimit' orders. Example: `2400` |
| `trigPrice` | `number` | No | This is applicable only for the main leg order and required only if the order type is 'stoplimit' |
| `mktProt` | `number` | No | This is applicable only for the main leg order and required only if the order type is 'market'. Example: `5` |
| `stopTrigPrice` | `number` | Yes | Stop loss leg trigger price. This is the difference of main leg price and the stop loss leg trigger price. If your main leg order price is '2400' and if you want to set the stop loss trigger at '2300' then pass the difference '100' in this field. Example: `100` |
| `targetPrice` | `number` | Yes | Target leg price. This is the difference of main leg price and the target leg price. If your main leg order price is '2400' and if you want to set the target or profit order price for 2500 then pass the difference '100' in this field. Example: `100` |
| `trailingStopPrice` | `number` | No | Trailing stop loss price. Example: `10` |
| `side` | `string` | No | Order side 'buy' or 'sell'. Values: `buy`, `sell` |

### Example Request

```bash
curl -X PUT "https://example.com/api/oms/modify-order/bo" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'symId=EQT_RELIANCE_EQ_NSE&orderId=string&qty=1&type=limit&stopTrigPrice=100&targetPrice=100'
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

## Place Cover Order

`POST /api/oms/place-order/co`

to place the cover order

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `symId` | `string` | Yes | Unique identifier of the symbol. Example: `EQT_RELIANCE_EQ_NSE` |
| `qty` | `number` | Yes | No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50. Example: `1` |
| `side` | `string` | Yes | Order side 'buy' or 'sell'. Values: `buy`, `sell` |
| `type` | `string` | Yes | Price type of an order. Values: `limit`, `market`, `stoplimit` |
| `limitPrice` | `number` | No | Main leg order price. Required only for 'limit' and 'stoplimit' orders. Example: `2400` |
| `trigPrice` | `number` | No | This is applicable only for the main leg order and required only if the order type is 'stoplimit' |
| `mktProt` | `number` | No | This is applicable only for the main leg order and required only if the order type is 'market'. Example: `5` |
| `stopTrigPrice` | `number` | Yes | Stop loss leg trigger price. This is the difference of main leg price and the stop loss leg trigger price. If your main leg order price is '2400' and if you want to set the stop loss trigger at '2300' then pass the difference '100' in this field. Example: `100` |
| `remarks` | `string` | No | Any tag or message to track in orderbook.Allowed length upto 10 Characters. Please note remarks more than 10 characters will be stripped out. |

### Example Request

```bash
curl -X POST "https://example.com/api/oms/place-order/co" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'symId=EQT_RELIANCE_EQ_NSE&qty=1&side=buy&type=limit&stopTrigPrice=100'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "Order Placed Successfully", "orderId": "210115000000001"}` |
| `d.msg` | `string` |  |
| `d.orderId` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

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

## Modify Cover Order

`PUT /api/oms/modify-order/co`

to modify the cover order

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
| `type` | `string` | Yes | Price type of an order. Values: `limit`, `market`, `stoplimit` |
| `limitPrice` | `number` | No | Main leg order price. Required only for 'limit' and 'stoplimit' orders. Example: `2400` |
| `trigPrice` | `number` | No | This is applicable only for the main leg order and required only if the order type is 'stoplimit' |
| `mktProt` | `number` | No | This is applicable only for the main leg order and required only if the order type is 'market'. Example: `5` |
| `side` | `string` | No | Order side 'buy' or 'sell'. Values: `buy`, `sell` |
| `stopTrigPrice` | `number` | Yes | Stop loss leg trigger price. This is the difference of main leg price and the stop loss leg trigger price. If your main leg order price is '2400' and if you want to set the stop loss trigger at '2300' then pass the difference '100' in this field. Example: `100` |

### Example Request

```bash
curl -X PUT "https://example.com/api/oms/modify-order/co" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'symId=EQT_RELIANCE_EQ_NSE&orderId=string&qty=1&type=limit&stopTrigPrice=100'
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

## Place GTT Order

`POST /api/oms/place-order/gtt`

Place good till triggered order

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `symId` | `string` | Yes | Unique identifier of the symbol. Example: `EQT_RELIANCE_EQ_NSE` |
| `type` | `string` | Yes | Price type of an order. Values: `limit`; Example: `limit` |
| `side` | `string` | Yes | Order id of an order. This will be received in orders response. Values: `buy`, `sell` |
| `product` | `string` | Yes | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `normal` |
| `trigPricePer` | `number` | Yes | Price difference from the LTP in percentage, calculated using the formula: (trigPrice - LTP) / LTP × 100. This value can be positive or negative, depending on whether the trigPrice is above or below the LTP. Example: `-4.99` |
| `trigPrice` | `number` | Yes | Trigger price with respect to LTP. Example: `2760.65` |
| `qty` | `number` | Yes | No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50. Example: `1` |
| `limitPrice` | `number` | No | This is required only for limit and stop limit orders. Example: `2760.65` |

### Example Request

```bash
curl -X POST "https://example.com/api/oms/place-order/gtt" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'symId=EQT_RELIANCE_EQ_NSE&type=limit&side=buy&product=delivery&trigPricePer=-4.99&trigPrice=2760.65&qty=1'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "GTT Order Placed Successfully", "orderId": "210115000000004"}` |
| `d.msg` | `string` |  |
| `d.orderId` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "GTT Order Placed Successfully",
    "orderId": "210115000000004"
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

## Modify GTT Order

`PUT /api/oms/modify-order/gtt`

Modify good till triggered order

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `orderId` | `string` | Yes | Order Number is unique number which will be utilized while modifying and cancelling order |
| `symId` | `string` | Yes | Unique identifier of the symbol. Example: `EQT_RELIANCE_EQ_NSE` |
| `side` | `string` | Yes | Order id of an order. This will be received in orders response. Values: `buy`, `sell` |
| `type` | `string` | Yes | Price type of an order. Values: `limit`; Example: `limit` |
| `product` | `string` | Yes | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `normal` |
| `trigPricePer` | `number` | Yes | Price difference from the LTP in percentage, calculated using the formula: (trigPrice - LTP) / LTP × 100. This value can be positive or negative, depending on whether the trigPrice is above or below the LTP. |
| `trigPrice` | `number` | Yes | Trigger price with respect to LTP |
| `qty` | `number` | Yes | No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50. Example: `1` |
| `limitPrice` | `number` | No | This is required only for limit and stop limit orders. Example: `2120.55` |

### Example Request

```bash
curl -X PUT "https://example.com/api/oms/modify-order/gtt" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'orderId=string&symId=EQT_RELIANCE_EQ_NSE&side=buy&type=limit&product=delivery&qty=1'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "GTT Order Modified Successfully", "orderId": "210115000000004"}` |
| `d.msg` | `string` |  |
| `d.orderId` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "GTT Order Modified Successfully",
    "orderId": "210115000000004"
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

## Place OCO Order

`POST /api/oms/place-order/oco`

Place A one-cancels-the-other order

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `symId` | `string` | Yes | Unique identifier of the symbol. Example: `EQT_RELIANCE_EQ_NSE` |
| `side` | `string` | Yes | Order id of an order. This will be received in orders response. Values: `buy`, `sell` |
| `stopLossType` | `string` | Yes | Price type of an order. Values: `limit`; Example: `limit` |
| `stopLossProduct` | `string` | Yes | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `normal` |
| `stopTrigPrice` | `number` | Yes | Trigger price with respect to LTP |
| `stopQty` | `number` | Yes | No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50. Example: `1` |
| `stopPrice` | `number` | No | This is required only for limit and stop limit orders. Example: `2120.55` |
| `targetType` | `string` | Yes | Price type of an order. Values: `limit`; Example: `limit` |
| `targetProduct` | `string` | Yes | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `normal` |
| `targetTrigPrice` | `number` | Yes | Trigger price with respect to LTP |
| `targetQty` | `number` | Yes | No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50. Example: `1` |
| `targetPrice` | `number` | No | This is required only for limit and stop limit orders. Example: `2120.55` |

### Example Request

```bash
curl -X POST "https://example.com/api/oms/place-order/oco" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'symId=EQT_RELIANCE_EQ_NSE&side=buy&stopLossType=limit&stopLossProduct=delivery&stopQty=1&targetType=limit&targetProduct=delivery&targetQty=1'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "OCO Order Placed Successfully", "orderId": "210115000000003"}` |
| `d.msg` | `string` |  |
| `d.orderId` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "OCO Order Placed Successfully",
    "orderId": "210115000000003"
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

## Modify OCO Order

`PUT /api/oms/modify-order/oco`

Modify one-cancels-the-other order

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `orderId` | `string` | Yes | Order Number is unique number which will be utilized while modifying and cancelling order. Example: `22052700000013` |
| `symId` | `string` | Yes | Unique identifier of the symbol. Example: `EQT_RELIANCE_EQ_NSE` |
| `side` | `string` | Yes | Order id of an order. This will be received in orders response. Values: `buy`, `sell` |
| `stopLossType` | `string` | Yes | Price type of an order. Values: `limit`; Example: `limit` |
| `stopLossProduct` | `string` | Yes | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `normal` |
| `stopTrigPrice` | `number` | Yes | Stoploss trigger price |
| `stopQty` | `number` | Yes | No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50. Example: `5` |
| `stopPrice` | `number` | No | This is required only for limit and stop limit orders. Example: `2800.55` |
| `targetType` | `string` | Yes | Price type of an order. Values: `limit`; Example: `limit` |
| `targetProduct` | `string` | Yes | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `normal` |
| `targetTrigPrice` | `number` | Yes | Target trigger price |
| `targetQty` | `number` | Yes | No of shares to buy or sell. For derivatives, pass the quantity by multiplying with lot size. Example: To buy 1 lot of NIFTY option, pass the quantity as 50. Example: `5` |
| `targetPrice` | `number` | No | This is required only for limit and stop limit orders. Example: `2600` |

### Example Request

```bash
curl -X PUT "https://example.com/api/oms/modify-order/oco" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'orderId=22052700000013&symId=EQT_RELIANCE_EQ_NSE&side=buy&stopLossType=limit&stopLossProduct=delivery&stopQty=5&targetType=limit&targetProduct=delivery&targetQty=5'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "OCO Order Modified Successfully", "orderId": "210115000000003"}` |
| `d.msg` | `string` |  |
| `d.orderId` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "OCO Order Modified Successfully",
    "orderId": "210115000000003"
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

## GTT OrderBook

`GET /api/oms/orders/gtt`

to get the list of pending gtt, oco orders orders

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X GET "https://example.com/api/oms/orders/gtt" \
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
| `d[].exchange` | `string` |  |
| `d[].orderId` | `string` |  |
| `d[].side` | `string` |  |
| `d[].triggerType` | `string` | Values: `Single`, `OCO` |
| `d[].single` | `object` | Example: `{"product": "cnc", "type": "l", "qty": 10, "price": 2440, "trigPrice": 0, "remarks": ""}` |
| `d[].single.remarks` | `string` | Any message entered during order entry |
| `d[].single.trigPrice` | `number` | Trigger price with respect to LTP |
| `d[].single.product` | `string` | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `normal` |
| `d[].single.type` | `string` | Values: `limit` |
| `d[].single.qty` | `number` |  |
| `d[].single.price` | `number` |  |
| `d[].stopLoss` | `object` | Example: `{"product": "cnc", "type": "l", "qty": 10, "price": 2440, "trigPrice": 0, "remarks": ""}` |
| `d[].stopLoss.remarks` | `string` | Any message entered during order entry |
| `d[].stopLoss.trigPrice` | `number` | Trigger price with respect to LTP |
| `d[].stopLoss.product` | `string` | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `normal` |
| `d[].stopLoss.type` | `string` | Values: `limit` |
| `d[].stopLoss.qty` | `number` |  |
| `d[].stopLoss.price` | `number` |  |
| `d[].target` | `object` | Example: `{"product": "cnc", "type": "l", "qty": 10, "price": 2440, "trigPrice": 0, "remarks": ""}` |
| `d[].target.remarks` | `string` | Any message entered during order entry |
| `d[].target.trigPrice` | `number` | Trigger price with respect to LTP |
| `d[].target.product` | `string` | Product type of an order. 'delivery' is applicable for equities. 'normal' is applicable for derivatives. 'intraday' is applicable for both equity and derivatives. Values: `delivery`, `normal` |
| `d[].target.type` | `string` | Values: `limit` |
| `d[].target.qty` | `number` |  |
| `d[].target.price` | `number` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": [
    {
      "symId": "EQT_RELIANCE_EQ_NSE",
      "exchange": "NSE",
      "orderId": "210115000000004",
      "side": "b",
      "triggerType": "single"
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

## Exit Order

`POST /api/oms/exit-order`

to exit bracket or cover order.

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Request Body

Content-Type: `application/x-www-form-urlencoded`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `orderId` | `string` | Yes | Main leg order id of bracker or cover order should be passed here. It will be received from the field 'mainLegOrderId' in orders response |
| `product` | `string` | Yes | Pass the respective product type bracket or cover here to exit. Values: `bracket`, `cover` |

### Example Request

```bash
curl -X POST "https://example.com/api/oms/exit-order" \
  -H "Authorization: Bearer <api Key>:<access token>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'orderId=string&product=bracket'
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "SNO Order Exited Successfully"}` |
| `d.msg` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "SNO Order Exited Successfully"
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

## Cancel OCO Order

`DELETE /api/oms/cancel-order/oco`

Cancel A one-cancels-the-other order

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `orderNo` | `string` | Yes | Order Number is unique number which will be utilized while modifying and cancelling order |

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X DELETE "https://example.com/api/oms/cancel-order/oco?orderNo=string" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "OCO Order Cancelled Successfully", "orderId": "210115000000003"}` |
| `d.msg` | `string` |  |
| `d.orderId` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "OCO Order Cancelled Successfully",
    "orderId": "210115000000003"
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

## Cancel GTT Order

`DELETE /api/oms/cancel-order/gtt`

to cancel the GTT order

### Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `orderNo` | `string` | Yes | Order Number is unique number which will be utilized while modifying and cancelling order |

### Header Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `Authorization` | `string` | Yes | Access token in the following format: Bearer `<api_key>`:`<access_token>` Both values are required. The `api_key` is your app credential from the Apps Section. The `access_token` is obtained from the authentication endpoint and is valid for 24 hours. Example: `Bearer <api Key>:<access token>` |

### Example Request

```bash
curl -X DELETE "https://example.com/api/oms/cancel-order/gtt?orderNo=string" \
  -H "Authorization: Bearer <api Key>:<access token>"
```

### Responses

#### 200 OK

OK

Content-Type: `application/json`

| Field | Type | Description |
| --- | --- | --- |
| `s` | `string` | Values: `ok`, `error`, `no-data`; Example: `ok` |
| `d` | `object` | Example: `{"msg": "GTT Order Cancelled Successfully", "orderId": "210115000000004"}` |
| `d.msg` | `string` |  |
| `d.orderId` | `string` |  |
| `msg` | `string` | Values: `no-data`, `error msg` |

**Example**

```json
{
  "s": "ok",
  "d": {
    "msg": "GTT Order Cancelled Successfully",
    "orderId": "210115000000004"
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
