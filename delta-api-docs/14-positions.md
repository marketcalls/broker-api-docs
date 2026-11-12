# Positions

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-positions

Get Open positions, Change Position Margin, Close Position, Close All Position

## Get margined positions

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/positions/margined', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/positions/margined \
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

result = RestClient.get 'https://api.india.delta.exchange/v2/positions/margined',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /positions/margined`

Change in position may take upto 10secs to reflect. Use 'GET /position' for real-time data.

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_ids|query|string|false|Comma-separated product IDs. Maximum 10 IDs allowed. If not specified, all the open positions will be returned|
|contract_types|query|string|false|comma separated list of desired contract types. If not specified any parameters then, all the open positions will be returned|

#### Enumerated Values

|Parameter|Value|Description|
|---|---|---|
|contract_types|perpetual_futures|Futures contracts with no expiry, funded via funding rate|
|contract_types|call_options|Call option contracts|
|contract_types|put_options|Put option contracts|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "user_id": 0,
      "size": 0,
      "entry_price": "string",
      "margin": "string",
      "liquidation_price": "string",
      "bankruptcy_price": "string",
      "adl_level": 0,
      "product_id": 0,
      "product_symbol": "string",
      "commission": "string",
      "realized_pnl": "string",
      "realized_funding": "string"
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of all [open positions](25-schemas.md#tocSposition)|Inline|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Get position

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/positions', params={
  'product_id': '0'
}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/positions?product_id=0 \
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

result = RestClient.get 'https://api.india.delta.exchange/v2/positions',
  params: {
  'product_id' => '0'
}, headers: headers

p JSON.parse(result)
```

`GET /positions`

Get real-time positions data.

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|product_id|query|integer|true|id of the product. Only send either product_id or underlying_asset_symbol.|
|underlying_asset_symbol|query|string|false|Underlying asset symbol. e.g. 'BTC', 'ETH'. This gives a list of all positions in products which have the given underlying asset. Only send either product_id or underlying_asset_symbol.|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "size": 0,
    "entry_price": "string"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Open position for the give product id|Inline|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Auto Topup

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

r = requests.put('https://api.india.delta.exchange/v2/positions/auto_topup', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/positions/auto_topup \
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

result = RestClient.put 'https://api.india.delta.exchange/v2/positions/auto_topup',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`PUT /positions/auto_topup`

Changes position auto topup flag. Positions automatically inherits auto topup flag of the account. If account level auto topop is set to false, use this api to change auto topup flag for individual positions.

> Body parameter

```json
{
  "product_id": 0,
  "auto_topup": "false"
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» product_id|body|integer|true|none|
|» auto_topup|body|boolean|true|none|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "user_id": 0,
    "size": 0,
    "entry_price": "string",
    "margin": "string",
    "liquidation_price": "string",
    "bankruptcy_price": "string",
    "adl_level": 0,
    "product_id": 0,
    "product_symbol": "string",
    "commission": "string",
    "realized_pnl": "string",
    "realized_funding": "string"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the position object|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if position margin could not be changed|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Add/Remove position margin

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

r = requests.post('https://api.india.delta.exchange/v2/positions/change_margin', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/positions/change_margin \
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

result = RestClient.post 'https://api.india.delta.exchange/v2/positions/change_margin',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`POST /positions/change_margin`

> Body parameter

```json
{
  "product_id": 0,
  "delta_margin": "string"
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» product_id|body|integer|true|none|
|» delta_margin|body|string|true|Delta in the position margin, positive in case of adding margin & negative in case of removing margin|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "user_id": 0,
    "size": 0,
    "entry_price": "string",
    "margin": "string",
    "liquidation_price": "string",
    "bankruptcy_price": "string",
    "adl_level": 0,
    "product_id": 0,
    "product_symbol": "string",
    "commission": "string",
    "realized_pnl": "string",
    "realized_funding": "string"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|returns the position object|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if position margin could not be changed|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Close all positions

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

r = requests.post('https://api.india.delta.exchange/v2/positions/close_all', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/positions/close_all \
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

result = RestClient.post 'https://api.india.delta.exchange/v2/positions/close_all',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`POST /positions/close_all`

> Body parameter

```json
{
  "close_all_portfolio": true,
  "close_all_isolated": true,
  "user_id": 0
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|
|» close_all_portfolio|body|boolean|true|none|
|» close_all_isolated|body|boolean|true|none|
|» user_id|body|integer|true|none|

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
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if not able to close all positions|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
