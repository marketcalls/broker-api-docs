# Historical OHLC Candles/Sparklines

> Source: https://docs.delta.exchange/#delta-exchange-api-v2-historical-ohlc-candles-sparklines

## GET historical ohlc candles

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/history/candles', params={
  'resolution': '5m',  'symbol': 'BTCUSD',  'start': '1685618835',  'end': '1722511635'
}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/history/candles?resolution=5m&symbol=BTCUSD&start=1685618835&end=1722511635 \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/history/candles',
  params: {
  'resolution' => '5m',
'symbol' => 'BTCUSD',
'start' => '1685618835',
'end' => '1722511635'
}, headers: headers

p JSON.parse(result)
```

`GET /history/candles`

It returns historical Open-High-Low-Close(ohlc) candles data of the symbol as per input values for resolution, start time and end time. Also, it can return only upto 2000 candles maximum in a response.

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|resolution|query|string|true|ohlc candle time frames like 1m, 5m, 1h|
|symbol|query|string|true|To get funding history pass symbol as FUNDING:${symbol}, mark price MARK:${symbol} and OI data OI:${symbol} for e.g. - FUNDING:BTCUSD, MARK:C-BTC-66400-010824, OI:ETHUSD|
|start|query|integer|true|Start time: unix timestamp in seconds|
|end|query|integer|true|End time: unix timestamp in seconds|

#### Enumerated Values

|Parameter|Value|Description|
|---|---|---|
|resolution|1m|1-minute candles|
|resolution|3m|3-minute candles|
|resolution|5m|5-minute candles|
|resolution|15m|15-minute candles|
|resolution|30m|30-minute candles|
|resolution|1h|1-hour candles|
|resolution|2h|2-hour candles|
|resolution|4h|4-hour candles|
|resolution|6h|6-hour candles|
|resolution|1d|1-day candles|
|resolution|1w|1-week candles|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": [
    {
      "time": 0,
      "open": 0,
      "high": 0,
      "low": 0,
      "close": 0,
      "volume": 0
    }
  ]
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|ohlc|Inline|

### Response Schema

> **Note:** This operation does not require authentication.

## GET product history sparklines

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.india.delta.exchange/v2/history/sparklines', params={
  'symbols': 'ETHUSD,MARK:BTCUSD'
}, headers = headers)

print r.json()
```

```shell
# You can also use wget
curl -X GET https://api.india.delta.exchange/v2/history/sparklines?symbols=ETHUSD%2CMARK%3ABTCUSD \
  -H 'Accept: application/json'
```

```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get 'https://api.india.delta.exchange/v2/history/sparklines',
  params: {
  'symbols' => 'ETHUSD,MARK:BTCUSD'
}, headers: headers

p JSON.parse(result)
```

`GET /history/sparklines`

### Parameters

|Parameter|In|Type|Required|Description|
|---|---|---|---|---|
|symbols|query|string|true|comma separated product symbols|

> Example responses
>
> 200 Response

```json
{
  "success": true,
  "result": {
    "ETHUSD": [
      [
        1594214051,
        0.00003826
      ],
      [
        1594214051,
        0.00003826
      ]
    ],
    "MARK:BTCUSD": [
      [
        1594215270,
        0.00003826
      ]
    ]
  }
}
```

### Responses

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|product history sparkline|Inline|

### Response Schema

> **Note:** This operation does not require authentication.
