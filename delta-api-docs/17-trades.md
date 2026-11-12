# Trades

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-trades

Get Trades of a contract

## Get public trades

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/trades/{symbol}', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/trades/{symbol} \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/trades/{symbol}',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /trades/{symbol}`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|symbol|path|string|true|none|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "trades": [
      {
        "side": "buy",
        "size": 0,
        "price": "string",
        "timestamp": 0
      }
    ]
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of recent trades of the product|Inline|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|side|buy|Trade where the aggressor was a buyer|
|side|sell|Trade where the aggressor was a seller|

> **Note:** This operation does not require authentication.
