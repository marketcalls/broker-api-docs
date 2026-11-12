# Indices

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-indices

Get Indices List

## Get indices

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/indices', params={

}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/indices \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/indices',
  params: {
  }, headers: headers

p JSON.parse(result)
```

`GET /indices`

Indices refer to spot price indices that Delta Exchange creates by combining spot prices of prominent crypto exchanges. These indices form the underlying of futures and options contracts listed on Delta Exchange. All details of indices on Delta Exchange are available [here](https://www.delta.exchange/indices).

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "id": 14,
      "symbol": ".DEXBTUSD",
      "constituent_exchanges": [
        {
          "name": "ExchangeA",
          "weight": 0.25
        }
      ],
      "underlying_asset_id": 13,
      "quoting_asset_id": 14,
      "tick_size": "0.5",
      "index_type": "spot_pair"
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of [Spot Index schema](25-schemas.md#tocSindex)|Inline|

### Response Schema

#### Enumerated Values

|Property|Value|Description|
|---|---|---|
|index_type|spot_pair|Index based on a spot trading pair|
|index_type|fixed_interest_rate|Index based on a fixed interest rate|
|index_type|floating_interest_rate|Index based on a floating interest rate|

> **Note:** This operation does not require authentication.
