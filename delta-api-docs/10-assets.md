# Assets

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-assets

Get Asset List

## Get list of all assets

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/assets', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/assets \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/assets',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /assets`

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 14,
      "symbol": "USD",
      "precision": 8,
      "deposit_status": "enabled",
      "withdrawal_status": "enabled",
      "base_withdrawal_fee": "0.000000000000000000",
      "min_withdrawal_amount": "0.000000000000000000"
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of [Asset schema](25-schemas.md#tocSasset)|Inline|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|deposit_status|enabled|Deposits are currently allowed for the asset|
|deposit_status|disabled|Deposits are currently not allowed for the asset|
|withdrawal_status|enabled|Withdrawals are currently allowed for the asset|
|withdrawal_status|disabled|Withdrawals are currently not allowed for the asset|

> **Note:** This operation does not require authentication.
