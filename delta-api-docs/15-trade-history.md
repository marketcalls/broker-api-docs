# TradeHistory

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-tradehistory

Get Orders History, Get Fill History

## Get order history (cancelled and closed)

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/orders/history', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/orders/history \
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

result = RestClient.get 'https://api.india.delta.exchange/v2/orders/history',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /orders/history`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_ids|query|string|false|Comma separated product IDs. Maximum 10 IDs allowed.|
|contract_types|query|string|false|comma separated list of desired contract types|
|order_types|query|string|false|comma separated order types|
|start_time|query|integer|false|from time in micro-seconds in epoc|
|end_time|query|integer|false|from time in micro-seconds in epoc|
|after|query|string|false|after cursor for pagination|
|before|query|string|false|before cursor for pagination|
|page_size|query|integer|false|number of records per page|

#### Enumerated Values

|Parameter|Value|Description|
|---|---|---|
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
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of closed and cancelled orders. [Order schema](25-schemas.md#tocSorder)|Inline|

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

## GET user fills by filters

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/fills', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/fills \
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

result = RestClient.get 'https://api.india.delta.exchange/v2/fills',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /fills`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_ids|query|string|false|Comma separated product IDs. Maximum 10 IDs allowed.|
|contract_types|query|string|false|comma separated list of desired contract types|
|start_time|query|integer|false|from time in micro-seconds in epoc|
|end_time|query|integer|false|from time in micro-seconds in epoc|
|after|query|string|false|after cursor for pagination|
|before|query|string|false|before cursor for pagination|
|page_size|query|integer|false|number of records per page|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 0,
      "size": 0,
      "fill_type": "normal",
      "side": "buy",
      "price": "string",
      "role": "taker",
      "commission": "string",
      "created_at": "string",
      "product_id": 0,
      "product_symbol": "string",
      "order_id": "string",
      "settling_asset_id": 0,
      "settling_asset_symbol": "string",
      "meta_data": {
        "commission_deto": "string",
        "commission_deto_in_settling_asset": "string",
        "effective_commission_rate": "string",
        "liquidation_fee_deto": "string",
        "liquidation_fee_deto_in_settling_asset": "string",
        "order_price": "string",
        "order_size": "string",
        "order_type": "string",
        "order_unfilled_size": "string",
        "tfc_used_for_commission": "string",
        "tfc_used_for_liquidation_fee": "string",
        "total_commission_in_settling_asset": "string",
        "total_liquidation_fee_in_settling_asset": "string"
      }
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
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Array of [fills](25-schemas.md#tocSfill)|Inline|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|fill_type|normal|Regular fill from matching against the orderbook|
|fill_type|adl|Fill from auto-deleveraging to balance counterparty exposure|
|fill_type|liquidation|Fill resulting from forced liquidation of a position|
|fill_type|settlement|Fill generated at contract settlement or expiry|
|fill_type|otc|Off-exchange (over-the-counter) fill|
|side|buy|Buy order on the product|
|side|sell|Sell order on the product|
|role|taker|Fill where the user removed liquidity from the orderbook|
|role|maker|Fill where the user added liquidity to the orderbook|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Download Fills history

> Code samples

```python
import requests
headers = {
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/fills/history/download/csv', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/fills/history/download/csv \
  -H 'api-key: ****' \
  -H 'signature: ****' \
  -H 'timestamp: ****'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'api-key' => '****',
  'signature' => '****',
  'timestamp' => '****'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/fills/history/download/csv',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /fills/history/download/csv`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_ids|query|string|false|comma separated product ids|
|contract_types|query|string|false|comma separated list of desired contract types|
|start_time|query|integer|false|from time in micro-seconds in epoc|
|end_time|query|integer|false|from time in micro-seconds in epoc|

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|csv of fills for the filter query|None|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
