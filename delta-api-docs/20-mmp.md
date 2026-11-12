# MMP

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-mmp

Market maker protection

## Update MMP config

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

r = requests.put('https://api.india.delta.exchange/v2/users/update_mmp', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/users/update_mmp \
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

result = RestClient.put 'https://api.india.delta.exchange/v2/users/update_mmp',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`PUT /users/update_mmp`

Channel provides updates when MMP is triggered. Market maker protection is available to registered market makers by default.

> Body parameter

```json
{
  "asset": "string",
  "window_interval": 0,
  "freeze_interval": 0,
  "trade_limit": "string",
  "delta_limit": "string",
  "vega_limit": "string",
  "mmp": "mmp1"
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[MMPConfigUpdateRequest](25-schemas.md#schemammpconfigupdaterequest)|true|mmp config for a given underlying asset|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "user_id": 57354187,
    "default_auto_topup": true,
    "mmp_config": null,
    "deto_for_commission": false,
    "vip_level": 0,
    "vip_discount_factor": "0.00",
    "volume_30d": "1060.675333",
    "email_preferences": {
      "adl": true,
      "liquidation": true,
      "margin_topup": false,
      "marketing": true,
      "order_cancel": true,
      "order_fill": true,
      "stop_order_trigger": true
    },
    "notification_preferences": {
      "adl": true,
      "liquidation": true,
      "margin_topup": false,
      "marketing": true,
      "order_cancel": false,
      "order_fill": true,
      "price_alert": true,
      "stop_order_trigger": true
    },
    "price_alert_assets": [
      "BTC",
      "ETH"
    ],
    "enabled_portfolios": {},
    "interest_credit": false
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the User Preference which contains mmp config|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if mmp is not enabled on the account|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Reset MMP

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

r = requests.put('https://api.india.delta.exchange/v2/users/reset_mmp', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/users/reset_mmp \
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

result = RestClient.put 'https://api.india.delta.exchange/v2/users/reset_mmp',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`PUT /users/reset_mmp`

> Body parameter

```json
{
  "asset": "string",
  "mmp": "mmp1"
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[MMPResetRequest](25-schemas.md#schemammpresetrequest)|true|reset mmp config for a given underlying asset|

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
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns back the User Preference which contains mmp config|[ApiSuccessResponse](25-schemas.md#schemaapisuccessresponse)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if mmp is not enabled on the account|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.
