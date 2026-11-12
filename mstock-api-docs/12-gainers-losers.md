# Top Gainers and Losers

> Source: https://tradingapi.mstock.com/docs/v1/typeB/gainers-losers/
>
> Section: Type B

### Top Gainers and Losers API

| method | path | description |
| --- | --- | --- |
| POST | https://api.mstock.trade/openapi/typea/losergainer | This endpoint allows users to retrieve top gainers and losers |

---

### Top Gainer/Losers API

This endpoint allows users to retrieve list of top gainers and losers.

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization :** A token-based authentication header. The format is token api_key:access_token.
- **Content-Type :** Indicated the media type of the resource. For this request, it is set to [application/x-www-form-urlencoded](https://mapi.mirae-asset.co.in/developer/type-a/application/x-www-form-urlencoded), which is used for submiting form data.

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typea/losergainer' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwtToken' \
--header 'X-PrivateKey: api_key' \
--header 'Content-Type: application/json' \
--data '{
    "Exchange": 1,
    "SecurityIdCode": 13,
    "segment": 1,
    "TypeFlag": "G"
}'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.post(
'https://api.mstock.trade/openapi/typea/losergainer',
{
    'Exchange': '1',
    'SecurityIdCode': '13',
    'segment': '1',
    'TypeFlag': 'G'
},
{
    headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
    }
}
);
```

**Python**

```python
import http.client
import json

conn = http.client.HTTPConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json',
}
json_data = {
    'Exchange': '1',
    'SecurityIdCode': '13',
    'segment': '1',
    'TypeFlag': 'G'
}
conn.request(
    'POST',
    'openapi/typea/losergainer',
    json.dumps(json_data),
    headers
)
response = conn.getresponse()
```

**Java**

```java
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpRequest.BodyPublishers;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newBuilder()
    .followRedirects(HttpClient.Redirect.NORMAL)
    .build();

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.mstock.trade/openapi/typea/losergainer"))
    .POST(BodyPublishers.ofString("{\n        \"Exchange\": \"1\",\n        \"SecurityIdCode\": \"13\",\n        \"segment\": \"1\",\n        \"TypeFlag\": \"G\"}"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey": "api_key")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -** The body of the request must be URL-encoded and include the following parameters:

| Field | Type | Description |
| --- | --- | --- |
| Exchange | int | Exchange ID |
| SecurityIdCode | int | Security ID Code |
| segment | int | Segment ID |
| TypeFlag | string | Flag Type |

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful request execution, server will return the below json formated data.

```json
{
    "status": true,
    "message": "SUCCESS",
    "errorcode": "",
    "data": [
        {
            "exchange": "NSE",
            "segment": "E",
            "security_id": 5258,
            "ltp": 732.2,
            "Pclose": 0,
            "Open": 0,
            "TickSize": 0.05,
            "Multiplier": 1,
            "per_month_change": 0,
            "month_change": 0,
            "Price1": 0,
            "volume": 6227379,
            "per_change": 6.19,
            "change": 42.700000000000045,
            "Price": 0,
            "symbol_name": "INDUSIND BANK LIMITED",
            "isin": "INE095A01012",
            "instrument": "EQUITY",
            "series": "EQ",
            "lot_size": 1,
            "expiry_date": "01-01-0001 00:00:00",
            "strike_price": "",
            "option_type": "",
            "display_name": "INDUSIND BANK LIMITED",
            "symbol": "INDUSINDBK",
            "exchange_inst_name": "EQ",
            "Message": "0"
        },
        {
            "exchange": "NSE",
            "segment": "E",
            "security_id": 11483,
            "ltp": 3259,
            "Pclose": 0,
            "Open": 0,
            "TickSize": 0.1,
            "Multiplier": 1,
            "per_month_change": 0,
            "month_change": 0,
            "Price1": 0,
            "volume": 808275,
            "per_change": 4.59,
            "change": 143.05000000000018,
            "Price": 0,
            "symbol_name": "LARSEN & TOUBRO LTD.",
            "isin": "INE018A01030",
            "instrument": "EQUITY",
            "series": "EQ",
            "lot_size": 1,
            "expiry_date": "01-01-0001 00:00:00",
            "strike_price": "",
            "option_type": "",
            "display_name": "LARSEN & TOUBRO LTD.",
            "symbol": "LT",
            "exchange_inst_name": "EQ",
            "Message": "0"
        }
    ]
}
```

- Failure (HTTP Status 200): If authentication fails, the server will return an error message

```json
{
    "status": false,
    "message": "Invalid request. Please try again.",
    "errorcode": "IA401",
    "data": null
}
```

-

Failure (HTTP Status 400):

If the API Key is Invalid or expired.

```json
{
    "status": false,
    "message": "API is suspended/expired for use. Please check your API subscription and try again.",
    "errorcode": "IA403",
    "data": null
}
```
