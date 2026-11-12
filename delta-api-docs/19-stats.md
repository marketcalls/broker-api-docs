# Stats

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-stats

Get Volume Stats

## Get volume stats

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/stats', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/stats \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/stats',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /stats`

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "last_30_days_volume": 0,
    "last_7_days_volume": 0,
    "total_volume": 0
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|sum of turnover in the last 7 and 30 days along with Total Volume in the last 24 hours (in USD)|Inline|

### Response Schema

> **Note:** This operation does not require authentication.
