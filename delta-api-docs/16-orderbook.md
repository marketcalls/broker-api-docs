# Orderbook

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-orderbook

L2Orderbook

## Get L2 orderbook

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/l2orderbook/{symbol}', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/l2orderbook/{symbol} \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/l2orderbook/{symbol}',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /l2orderbook/{symbol}`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|symbol|path|string|true|none|
|depth|query|integer|false|number of levels on each side|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "buy": [
      {
        "depth": "983",
        "price": "9187.5",
        "size": 205640
      }
    ],
    "last_updated_at": 1654589595784000,
    "sell": [
      {
        "depth": "1185",
        "price": "9188.0",
        "size": 113752
      }
    ],
    "symbol": "BTCUSD"
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|L2 orderbook for the product|Inline|

### Response Schema

> **Note:** This operation does not require authentication.
