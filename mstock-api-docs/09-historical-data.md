# Historical Data

> Source: https://tradingapi.mstock.com/docs/v1/typeB/historical-candle/
>
> Section: Type B

### Historical Data APIs

| method | path | description |
| --- | --- | --- |
| GET | https://api.mstock.trade/openapi/typeb/instruments/historical | View historical data |

The historical data API provides the historical data for instruments across various exchange segment.

**Request Headers -**

- **X-Mirae-Version:** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization:** A token-based authentication header. The format is Bearer jwtToken.
- **X-Private-key:** api_key

**cURL**

```bash
curl --location --request GET 'https://api.mstock.trade/openapi/typeb/instruments/historical' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwtToken' \
--header 'X-PrivateKey: api_key' \
--header 'Content-Type: application/json' \
--data '{
    "exchange": "NSE",
    "symboltoken": "11536",
    "interval": "ONE_MINUTE",
    "fromdate": "2024-08-02 09:15",
    "todate": "2024-08-04 09:20"
}' \
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/instruments/historical', {
headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
},
// data: '{\n    "exchange": "NSE",\n    "symboltoken": "11536",\n    "interval": "ONE_MINUTE",\n    "fromdate": "2024-08-02 09:15",\n    "todate": "2024-08-04 09:20"\n}',
data: {
    'exchange': 'NSE',
    'symboltoken': '11536',
    'interval': 'ONE_MINUTE',
    'fromdate': '2024-08-02 09:15',
    'todate': '2024-08-04 09:20'
}
});
```

**Python**

```python
import http.client
import json

conn = http.client.HTTPSConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json',
}
json_data = {
    'exchange': 'NSE',
    'symboltoken': '11536',
    'interval': 'ONE_MINUTE',
    'fromdate': '2024-08-02 09:15',
    'todate': '2024-08-04 09:20',
}
conn.request(
    'GET',
    'openapi/typeb/instruments/historical',
    json.dumps(json_data),
    # '{\n    "exchange": "NSE",\n    "symboltoken": "11536",\n    "interval": "ONE_MINUTE",\n    "fromdate": "2024-08-02 09:15",\n    "todate": "2024-08-04 09:20"\n}',
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/instruments/historical"))
    .method("GET", BodyPublishers.ofString("{\n    \"exchange\": \"NSE\",\n    \"symboltoken\": \"11536\",\n    \"interval\": \"ONE_MINUTE\",\n    \"fromdate\": \"2024-08-02 09:15\",\n    \"todate\": \"2024-08-04 09:20\"\n}"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -** This endpoint does not require a request body or additional parameters in the query string for the retrieval of orders.

**Request Response -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful order update, the server returns a JSON object containing the order ID and status.

```json
{
    "status": "true",
    "message": "success",
    "errorcode": "",
    "data": {
        "candles": [
            [
                "2024-01-01T09:15:00+05",
                3790,
                3832,
                3773.35,
                3803,
                825219
            ],
            [
                "2024-01-02T09:15:00+05",
                3811.1,
                3811.1,
                3767.25,
                3781.15,
                1343722
            ]
        ]
    }
}
```

- Failure (HTTP Status 401): If the order fails due to invalid parameters, authentication issues, or other errors, the server will return an error message with below json format.

```json
{
    "status": "false",
    "message": "Invalid request. Please try again.",
    "errorcode": "IA401",
    "data": null
}
```

- Failure (HTTP Status 400): If the API Key is Invalid or expired.

```json
{
    "status": "false",
    "message": "API is suspended/expired for use. Please check your API subscription and try again.",
    "errorcode": "IA403",
    "data": null
}
```
