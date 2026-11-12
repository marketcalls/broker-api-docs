# Orders

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-orders

Placing Orders, Cancelling Orders, Placing batch orders, Cancelling batch orders, Get Open orders, Change Orders Leverage. Rate limits have been introduced recently that allows only set number of operations inside a matching engine in a timeframe. The current rate limits is 500 operations/sec for each product. For ex - placing 50 orders in a batch is equivalent to 50 operations as these orders will be processed by matching engine. Rate limits do not apply when cancelling orders.

## Place Order

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/orders', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/orders \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/orders',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`POST /orders`

> Body parameter

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "limit_price": "59000",
  "size": 10,
  "side": "buy",
  "order_type": "limit_order",
  "stop_order_type": "stop_loss_order",
  "stop_price": "56000",
  "trail_amount": "50",
  "stop_trigger_method": "last_traded_price",
  "bracket_stop_trigger_method": "last_traded_price",
  "bracket_stop_loss_limit_price": "57000",
  "bracket_stop_loss_price": "56000",
  "bracket_trail_amount": "50",
  "bracket_take_profit_limit_price": "62000",
  "bracket_take_profit_price": "61000",
  "time_in_force": "gtc",
  "mmp": "disabled",
  "post_only": false,
  "reduce_only": false,
  "client_order_id": "my_signal_345212",
  "cancel_orders_accepted": false
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateOrderRequest](25-schemas.md#schemacreateorderrequest)|true|Order which needs to be created. Rate limits apply.|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "my_signal_34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the order object with assigned id and latest state|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns [error](27-place-order-errors.md) if order could not be placed|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|stop_order_type|stop_loss_order|Order triggered when stop price is hit to limit losses|
|reduce_only|false|Order can open or increase a position|
|reduce_only|true|Order can only reduce or close an existing position|
|state|open|Order is active and resting in the orderbook|
|state|pending|Order is waiting for its trigger condition to be met|
|state|closed|Order has been fully filled|
|state|cancelled|Order was cancelled before being fully filled|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Cancel Order

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.delete('https://api.india.delta.exchange/v2/orders', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X DELETE https://api.india.delta.exchange/v2/orders \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.delete 'https://api.india.delta.exchange/v2/orders',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`DELETE /orders`

> Body parameter

```json
{
  "id": 13452112,
  "client_order_id": "my_signal_34521712",
  "product_id": 27
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[DeleteOrderRequest](25-schemas.md#schemadeleteorderrequest)|true|Order which needs to be cancelled|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "my_signal_34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the order object|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if order could not be cancelled|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|stop_order_type|stop_loss_order|Order triggered when stop price is hit to limit losses|
|reduce_only|false|Order can open or increase a position|
|reduce_only|true|Order can only reduce or close an existing position|
|state|open|Order is active and resting in the orderbook|
|state|pending|Order is waiting for its trigger condition to be met|
|state|closed|Order has been fully filled|
|state|cancelled|Order was cancelled before being fully filled|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Edit Order

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.put('https://api.india.delta.exchange/v2/orders', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/orders \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.put 'https://api.india.delta.exchange/v2/orders',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`PUT /orders`

> Body parameter

```json
{
  "id": 34521712,
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "limit_price": "59000",
  "size": 15,
  "mmp": "disabled",
  "post_only": false,
  "stop_price": "56000",
  "trail_amount": "50"
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EditOrderRequest](25-schemas.md#schemaeditorderrequest)|true|Order which needs to be edited. Rate limits apply.|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "my_signal_34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the order object with assigned id and latest state|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns [error](27-place-order-errors.md) if order could not be placed|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|stop_order_type|stop_loss_order|Order triggered when stop price is hit to limit losses|
|reduce_only|false|Order can open or increase a position|
|reduce_only|true|Order can only reduce or close an existing position|
|state|open|Order is active and resting in the orderbook|
|state|pending|Order is waiting for its trigger condition to be met|
|state|closed|Order has been fully filled|
|state|cancelled|Order was cancelled before being fully filled|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Get Active Orders

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/orders', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/orders \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/orders',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /orders`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_ids|query|string|false|Comma-separated product IDs. Maximum 10 IDs allowed. If not specified, all the orders will be returned|
|states|query|string|false|comma separated list of states - open,pending|
|contract_types|query|string|false|comma separated list of desired contract types, if not specified any parameters then, all the orders will be returned|
|order_types|query|string|false|comma separated order types|
|start_time|query|integer|false|from time in micro-seconds in epoc; referring to the order creation time|
|end_time|query|integer|false|from time in micro-seconds in epoc; referring to the order creation time|
|after|query|string|false|after cursor for pagination; becomes null if page after the current one does not exist|
|before|query|string|false|before cursor for pagination; becomes null if page before the current one does not exist|
|page_size|query|integer|false|number of records per page|

#### Enumerated Values

|Parameter|Value|Description|
|---|---|---|
|contract_types|futures|Dated futures contracts with a fixed expiry|
|contract_types|perpetual_futures|Futures contracts with no expiry, funded via funding rate|
|contract_types|call_options|Call option contracts|
|contract_types|put_options|Put option contracts|
|order_types|market|Market order executed at the best available price|
|order_types|limit|Limit order placed at a specified price|
|order_types|stop_market|Stop order that triggers a market order at the stop price|
|order_types|stop_limit|Stop order that triggers a limit order at the stop price|
|order_types|all_stop|All stop orders (stop_market and stop_limit)|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 123,
      "user_id": 453671,
      "size": 10,
      "unfilled_size": 2,
      "side": "buy",
      "order_type": "limit_order",
      "limit_price": "59000",
      "stop_order_type": "stop_loss_order",
      "stop_price": "55000",
      "paid_commission": "0.5432",
      "commission": "0.5432",
      "reduce_only": false,
      "client_order_id": "my_signal_34521712",
      "state": "open",
      "created_at": "1725865012000000",
      "product_id": 27,
      "product_symbol": "BTCUSD"
    }
  ],
  "meta": {
    "after": "g3QAAAACZAAKY3JlYXRlZF9hdHQAAAAN",
    "before": "a2PQRSACZAAKY3JlYXRlZF3fnqHBBBNZL"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of orders as per the query|Inline|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|stop_order_type|stop_loss_order|Order triggered when stop price is hit to limit losses|
|reduce_only|false|Order can open or increase a position|
|reduce_only|true|Order can only reduce or close an existing position|
|state|open|Order is active and resting in the orderbook|
|state|pending|Order is waiting for its trigger condition to be met|
|state|closed|Order has been fully filled|
|state|cancelled|Order was cancelled before being fully filled|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Place Bracket order

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/orders/bracket', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/orders/bracket \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/orders/bracket',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`POST /orders/bracket`

A bracket order is a set of TP and SL order. For a bracket order , size need not be specified as it closes the entire position. For a given contract, you can have multiple bracket orders for open orders but only a single bracket order for any open position.

> Body parameter

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "stop_loss_order": {
    "order_type": "limit_order",
    "stop_price": "56000",
    "trail_amount": "50",
    "limit_price": "55000"
  },
  "take_profit_order": {
    "order_type": "limit_order",
    "stop_price": "65000",
    "limit_price": "64000"
  },
  "bracket_stop_trigger_method": "last_traded_price"
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateBracketOrderRequest](25-schemas.md#schemacreatebracketorderrequest)|true|Bracket Order which needs to be updated|

> Example responses
>
> 200 Response

```json
{
  "success": true
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns back success response|[ApiSuccessResponse](25-schemas.md#schemaapisuccessresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if orders could not be updated|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Edit Bracket order

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.put('https://api.india.delta.exchange/v2/orders/bracket', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/orders/bracket \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.put 'https://api.india.delta.exchange/v2/orders/bracket',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`PUT /orders/bracket`

A bracket order is a set of TP and SL order. You can specify bracket order with an order that will create a new position. Use this api to change the bracket params attached with an order.

> Body parameter

```json
{
  "id": 34521712,
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "bracket_stop_loss_limit_price": "55000",
  "bracket_stop_loss_price": "56000",
  "bracket_take_profit_limit_price": "65000",
  "bracket_take_profit_price": "64000",
  "bracket_trail_amount": "50",
  "bracket_stop_trigger_method": "last_traded_price"
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EditBracketOrderRequest](25-schemas.md#schemaeditbracketorderrequest)|true|Bracket Order which needs to be updated|

> Example responses
>
> 200 Response

```json
{
  "success": true
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns back success response|[ApiSuccessResponse](25-schemas.md#schemaapisuccessresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if orders could not be updated|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Cancel all open orders

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.delete('https://api.india.delta.exchange/v2/orders/all', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X DELETE https://api.india.delta.exchange/v2/orders/all \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.delete 'https://api.india.delta.exchange/v2/orders/all',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`DELETE /orders/all`

Cancels all orders for a given product id. If product id is not provided, it cancels orders for provided contract types. If none of them are provided, it cancels all the orders. Provide either product id or list of contract types at a time. If both are provided, contract types will be ignored.

> Body parameter

```json
{
  "product_id": 27,
  "contract_types": "perpetual_futures,put_options,call_options",
  "cancel_limit_orders": false,
  "cancel_stop_orders": false,
  "cancel_reduce_only_orders": false
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CancelAllFilterObject](25-schemas.md#schemacancelallfilterobject)|false|Filters for selecting orders that needs to be cancelled|

> Example responses
>
> 200 Response

```json
{
  "success": true
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns back success response|[ApiSuccessResponse](25-schemas.md#schemaapisuccessresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if orders could not be cancelled|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Create batch orders

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/orders/batch', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/orders/batch \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/orders/batch',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`POST /orders/batch`

Orders in a batch should belong to the same contract. Max allowed size limit in a batch is 50. Rate limits apply. Please note that ioc is not valid time in force values for creating batch orders.

> Body parameter

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "limit_price": "59000",
      "size": 10,
      "side": "buy",
      "order_type": "limit_order",
      "time_in_force": "gtc",
      "mmp": "disabled",
      "post_only": false,
      "client_order_id": "my_signal_34521712"
    }
  ]
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchCreateOrdersRequest](25-schemas.md#schemabatchcreateordersrequest)|true|Does not support time_in_force flag for orders, All orders in batch create are assumed to be gtc orders. batch create does not support stop orders, it support only limit orders|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 123,
      "user_id": 453671,
      "size": 10,
      "unfilled_size": 2,
      "side": "buy",
      "order_type": "limit_order",
      "limit_price": "59000",
      "stop_order_type": "stop_loss_order",
      "stop_price": "55000",
      "paid_commission": "0.5432",
      "commission": "0.5432",
      "reduce_only": false,
      "client_order_id": "my_signal_34521712",
      "state": "open",
      "created_at": "1725865012000000",
      "product_id": 27,
      "product_symbol": "BTCUSD"
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the orders placed|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|returns error if orders couldnt be placed|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|stop_order_type|stop_loss_order|Order triggered when stop price is hit to limit losses|
|reduce_only|false|Order can open or increase a position|
|reduce_only|true|Order can only reduce or close an existing position|
|state|open|Order is active and resting in the orderbook|
|state|pending|Order is waiting for its trigger condition to be met|
|state|closed|Order has been fully filled|
|state|cancelled|Order was cancelled before being fully filled|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Edit batch orders

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.put('https://api.india.delta.exchange/v2/orders/batch', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/orders/batch \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.put 'https://api.india.delta.exchange/v2/orders/batch',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`PUT /orders/batch`

Orders to be edited in a batch. Rate limits apply.

> Body parameter

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "id": 34521712,
      "limit_price": "59000",
      "size": 15,
      "mmp": "disabled",
      "post_only": false
    }
  ]
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchEditOrdersRequest](25-schemas.md#schemabatcheditordersrequest)|true|none|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 123,
      "user_id": 453671,
      "size": 10,
      "unfilled_size": 2,
      "side": "buy",
      "order_type": "limit_order",
      "limit_price": "59000",
      "stop_order_type": "stop_loss_order",
      "stop_price": "55000",
      "paid_commission": "0.5432",
      "commission": "0.5432",
      "reduce_only": false,
      "client_order_id": "my_signal_34521712",
      "state": "open",
      "created_at": "1725865012000000",
      "product_id": 27,
      "product_symbol": "BTCUSD"
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of edited orders|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|returns error if orders couldnt be edited|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|stop_order_type|stop_loss_order|Order triggered when stop price is hit to limit losses|
|reduce_only|false|Order can open or increase a position|
|reduce_only|true|Order can only reduce or close an existing position|
|state|open|Order is active and resting in the orderbook|
|state|pending|Order is waiting for its trigger condition to be met|
|state|closed|Order has been fully filled|
|state|cancelled|Order was cancelled before being fully filled|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Delete batch orders

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.delete('https://api.india.delta.exchange/v2/orders/batch', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X DELETE https://api.india.delta.exchange/v2/orders/batch \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.delete 'https://api.india.delta.exchange/v2/orders/batch',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`DELETE /orders/batch`

> Body parameter

```json
{
  "product_id": 27,
  "product_symbol": "BTCUSD",
  "orders": [
    {
      "id": 13452112,
      "client_order_id": "my_signal_34521712"
    }
  ]
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[BatchDeleteOrdersRequest](25-schemas.md#schemabatchdeleteordersrequest)|true|none|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 123,
      "user_id": 453671,
      "size": 10,
      "unfilled_size": 2,
      "side": "buy",
      "order_type": "limit_order",
      "limit_price": "59000",
      "stop_order_type": "stop_loss_order",
      "stop_price": "55000",
      "paid_commission": "0.5432",
      "commission": "0.5432",
      "reduce_only": false,
      "client_order_id": "my_signal_34521712",
      "state": "open",
      "created_at": "1725865012000000",
      "product_id": 27,
      "product_symbol": "BTCUSD"
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the orders deleted|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|returns error if orders couldnt be deleted|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|stop_order_type|stop_loss_order|Order triggered when stop price is hit to limit losses|
|reduce_only|false|Order can open or increase a position|
|reduce_only|true|Order can only reduce or close an existing position|
|state|open|Order is active and resting in the orderbook|
|state|pending|Order is waiting for its trigger condition to be met|
|state|closed|Order has been fully filled|
|state|cancelled|Order was cancelled before being fully filled|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Get Order by id

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/orders/{order_id}', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/orders/{order_id} \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/orders/{order_id}',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /orders/{order_id}`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|order_id|path|string|true|Id of the order|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "my_signal_34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the order object with assigned id and latest state|Inline|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|stop_order_type|stop_loss_order|Order triggered when stop price is hit to limit losses|
|reduce_only|false|Order can open or increase a position|
|reduce_only|true|Order can only reduce or close an existing position|
|state|open|Order is active and resting in the orderbook|
|state|pending|Order is waiting for its trigger condition to be met|
|state|closed|Order has been fully filled|
|state|cancelled|Order was cancelled before being fully filled|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Get Order by client oid

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/orders/client_order_id/{client_oid}', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/orders/client_order_id/{client_oid} \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/orders/client_order_id/{client_oid}',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /orders/client_order_id/{client_oid}`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|client_oid|path|string|true|Custom user provided order id (max 32 length)|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "id": 123,
    "user_id": 453671,
    "size": 10,
    "unfilled_size": 2,
    "side": "buy",
    "order_type": "limit_order",
    "limit_price": "59000",
    "stop_order_type": "stop_loss_order",
    "stop_price": "55000",
    "paid_commission": "0.5432",
    "commission": "0.5432",
    "reduce_only": false,
    "client_order_id": "my_signal_34521712",
    "state": "open",
    "created_at": "1725865012000000",
    "product_id": 27,
    "product_symbol": "BTCUSD"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the order object with assigned client order id and latest state|Inline|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|order_type|limit_order|Order placed at a specified limit price|
|order_type|market_order|Order executed at the best available market price|
|stop_order_type|stop_loss_order|Order triggered when stop price is hit to limit losses|
|reduce_only|false|Order can open or increase a position|
|reduce_only|true|Order can only reduce or close an existing position|
|state|open|Order is active and resting in the orderbook|
|state|pending|Order is waiting for its trigger condition to be met|
|state|closed|Order has been fully filled|
|state|cancelled|Order was cancelled before being fully filled|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Change order leverage

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.post('https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.post 'https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`POST /products/{product_id}/orders/leverage`

> Body parameter

```json
{
  "leverage": 10
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|path|integer|true|Product id of the ordered product. Either product_id or product_symbol must be preseent.|
|product_symbol|path|string|true|Product symbol of the ordered product. Either product_id or product_symbol must be preseent.|
|body|body|object|true|none|
|» leverage|body|string|true|Order leverage|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "leverage": 10,
    "order_margin": "563.2",
    "product_id": 27
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the OrderLeverage object|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if leverage couldnt be changed|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Get order leverage

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage \
  -H 'Accept: application/json' \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/products/{product_id}/orders/leverage',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /products/{product_id}/orders/leverage`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|path|integer|true|Product id of the ordered product|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "leverage": 10,
    "order_margin": "563.2",
    "product_id": 27
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the OrderLeverage object|Inline|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
