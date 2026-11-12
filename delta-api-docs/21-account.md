# Account

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-account

Account level settings

## Get users trading preferences

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/users/trading_preferences', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/users/trading_preferences \
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

result = RestClient.get 'https://api.india.delta.exchange/v2/users/trading_preferences',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /users/trading_preferences`

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
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|User trading preferences attached to the account|Inline|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Update users trading preferences

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

r = requests.put('https://api.india.delta.exchange/v2/users/trading_preferences', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/users/trading_preferences \
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

result = RestClient.put 'https://api.india.delta.exchange/v2/users/trading_preferences',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`PUT /users/trading_preferences`

> Body parameter

```json
{
  "default_auto_topup": true,
  "showMarketOrdersForOptionsInBracket": true,
  "interest_credit": false,
  "email_preferences": {
    "adl": true,
    "liquidation": true,
    "order_fill": true,
    "stop_order_trigger": true,
    "order_cancel": true,
    "marketing": true
  },
  "notification_preferences": {
    "adl": false,
    "liquidation": true,
    "order_fill": true,
    "stop_order_trigger": true,
    "price_alert": true,
    "marketing": true
  }
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[EditUserPreference](25-schemas.md#schemaedituserpreference)|true|trading preferences|

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
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|User trading preferences attached to the account|Inline|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Get subaccounts

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/sub_accounts', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/sub_accounts \
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

result = RestClient.get 'https://api.india.delta.exchange/v2/sub_accounts',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /sub_accounts`

This api returns all the subaccounts belonging to the same parent/main user. Make sure to call this api from the parent user.

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": "98765432",
      "email": "[email protected]",
      "account_name": "Main",
      "first_name": "Rajesh",
      "last_name": "Sharma",
      "dob": "1985-08-25",
      "country": "India",
      "phone_number": "9876543210",
      "margin_mode": "isolated",
      "pf_index_symbol": ".DEXBTUSD",
      "is_sub_account": false,
      "is_kyc_done": true
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Subaccounts belonging to the same parent account.|Inline|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Get user

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'api-key': '****',
  'signature': '****',
  'timestamp': '****'
}

r = requests.get('https://api.india.delta.exchange/v2/profile', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/profile \
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

result = RestClient.get 'https://api.india.delta.exchange/v2/profile',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /profile`

This api returns the user object.

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "id": "98765432",
    "email": "[email protected]",
    "account_name": "Main",
    "first_name": "Rajesh",
    "last_name": "Sharma",
    "dob": "1985-08-25",
    "country": "India",
    "phone_number": "9876543210",
    "margin_mode": "isolated",
    "pf_index_symbol": ".DEXBTUSD",
    "is_sub_account": false,
    "is_kyc_done": true
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|User Object|Inline|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Change margin mode

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

r = requests.put('https://api.india.delta.exchange/v2/users/margin_mode', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X PUT https://api.india.delta.exchange/v2/users/margin_mode \
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

result = RestClient.put 'https://api.india.delta.exchange/v2/users/margin_mode',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`PUT /users/margin_mode`

> Body parameter

```json
{
  "margin_mode": "isolated",
  "subaccount_user_id": "5112346"
}
```

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ChangeMarginModeRequest](25-schemas.md#schemachangemarginmoderequest)|true|changes margin mode of the user|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "id": "5112346",
    "margin_mode": "isolated"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns the [ChangeMarginModeResponse](25-schemas.md#tocSchangemarginmoderesponse) with the updated margin mode|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Returns error if margin mode could not be changed|[ApiErrorResponse](25-schemas.md#schemaapierrorresponse)|

### Response Schema

> **Note:** To perform this operation, you must be sign the request using your api key and secret. See Authentication section for more details.

## Get current rate limit quota

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/rate_limits/quota', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/rate_limits/quota \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/rate_limits/quota',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /rate_limits/quota`

> Example responses
>
> 200 Response

```json
{
  "current_quota": 42,
  "remaining_time_in_milliseconds": 120632
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|This api returns the current rate limit quota.|[RateLimitQuotaResponse](25-schemas.md#schemaratelimitquotaresponse)|

> **Note:** This operation does not require authentication.
