# Heartbeat Management

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-heartbeat-management

## Create Heartbeat

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

r = requests.post('https://api.india.delta.exchange/v2/heartbeat/create', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/heartbeat/create \
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

result = RestClient.post 'https://api.india.delta.exchange/v2/heartbeat/create',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`POST /heartbeat/create`

> Body parameter

```json
{
  "heartbeat_id": "string",
  "impact": "low",
  "contract_types": [
    "string"
  ],
  "underlying_assets": [
    "string"
  ],
  "product_symbols": [
    "string"
  ],
  "config": [
    {
      "action": "cancel_orders",
      "unhealthy_count": 0,
      "tag": "string"
    }
  ]
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CreateHeartbeat](25-schemas.md#schemacreateheartbeat)|true|heartbeat creation details|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "heartbeat_id": "string",
    "status": "string"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Heartbeat created successfully|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns if heartbeat couldnt be created|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Send Heartbeat Acknowledgment

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

r = requests.post('https://api.india.delta.exchange/v2/heartbeat', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X POST https://api.india.delta.exchange/v2/heartbeat \
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

result = RestClient.post 'https://api.india.delta.exchange/v2/heartbeat',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`POST /heartbeat`

> Body parameter

```json
{
  "heartbeat_id": "string",
  "ttl": 0
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[HeartbeatAck](25-schemas.md#schemaheartbeatack)|true|heartbeat acknowledgment details|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "process_enabled": "string",
    "heartbeat_timestamp": "string"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Heartbeat acknowledged successfully|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns if heartbeat acknowledgment failed|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Get Heartbeats

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/heartbeat', params={
  'user_id': '0'
}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/heartbeat?user_id=0 \
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

result = RestClient.get 'https://api.india.delta.exchange/v2/heartbeat',
  params: {
  'user_id' => '0'
}, headers: headers

p JSON.parse(result)
```

`GET /heartbeat`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|user_id|query|integer|true|User ID|
|heartbeat_id|query|string|false|Specific heartbeat ID to retrieve|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "heartbeat_id": "string",
      "impact": "string",
      "contract_types": [
        "string"
      ],
      "underlying_assets": [
        "string"
      ],
      "product_symbols": [
        "string"
      ],
      "config": [
        {
          "action": "cancel_orders",
          "unhealthy_count": 0,
          "tag": "string"
        }
      ],
      "status": "string",
      "last_ack": "string",
      "next_ack_required_by": "string"
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of active heartbeats|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns if heartbeats couldnt be retrieved|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|action|cancel_orders|Cancel the user's open orders when the heartbeat goes unhealthy|
|action|spreads|Widen quote spreads when the heartbeat goes unhealthy|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
