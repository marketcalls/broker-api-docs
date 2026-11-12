# Intraday Chart Data

> Source: https://tradingapi.mstock.com/docs/v1/typeB/intraday-chart-data/
>
> Section: Type B

### Intraday Chart Data APIs

| method | path | description |
| --- | --- | --- |
| GET | https://api.mstock.trade/openapi/typeb/instruments/intraday | View intraday Chart Data |

The Intraday Chart data API provides the current data chart data for instruments across various exchange segment based on interval frame.

> **Intraday Chart Data Limit**
>
> Only current date data will be show for that script and exchange based on interval frame

**Request Headers -**

- X-Mirae-Version: Specifies the version of the API being used. In this case, it is set to 1.
- Authorization: A token-based authentication header. The format is Bearer jwtToken.
- X-PrivateKey: api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/instruments/intraday' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwtToken' \
--header 'X-PrivateKey: api_key' \
--header 'Content-Type: application/json' \
--data '{
    "exchange": "1",
    "symboltoken": "22",
    "interval": "THREE_MINUTE"
}'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.post(
'https://api.mstock.trade/openapi/typeb/instruments/intraday',
// '{\n    "exchange": "1",\n    "symboltoken": "22",\n    "interval": "THREE_MINUTE"\n}',
{
    'exchange': '1',
    'symboltoken': '22',
    'interval': 'THREE_MINUTE'
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

conn = http.client.HTTPSConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json',
}
json_data = {
    'exchange': '1',
    'symboltoken': '22',
    'interval': 'THREE_MINUTE',
}
conn.request(
    'POST',
    '/openapi/typeb/instruments/intraday',
    json.dumps(json_data),
    # '{\n    "exchange": "1",\n    "symboltoken": "22",\n    "interval": "THREE_MINUTE"\n}',
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/instruments/intraday"))
    .POST(BodyPublishers.ofString("{\n    \"exchange\": \"1\",\n    \"symboltoken\": \"22\",\n    \"interval\": \"THREE_MINUTE\"\n}"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Query Parameter -**

| Field | Type | Description |
| --- | --- | --- |
| Exchange | string | Exchange segment (1-NSE, 2-NFO, 3-CDS, 4-BSE, 5-BFO) |
| symboltoken | string | Symbol Token based on Exchange Security file |
| interval | string | Interval frame (minute, 3minute, 5minute, 10minute, 15minute, 30minute, 60minute, day) |

**Request Body -** This endpoint does not require a request body or additional parameters in the query string for the retrieval of orders.

**Request Response -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful order update, the server returns a JSON object containing the order ID and status.

```json
{
    "status": true,
    "message": "SUCCESS",
    "errorcode": "",
    "data": {
        "candles": [
            [
                "2025-04-04 15:27",
                553.1,
                554.65,
                553,
                554,
                420272
            ],
            [
                "2025-04-04 15:24",
                552.7,
                553.35,
                552.35,
                553.3,
                108013
            ],
            [
                "2025-04-04 15:21",
                552.5,
                552.5,
                552.05,
                552.2,
                94234
            ],
            [
                "2025-04-04 15:18",
                551.45,
                552.5,
                551.45,
                552.25,
                164762
            ],
            [
                "2025-04-04 15:15",
                552,
                552,
                551.2,
                551.4,
                173718
            ]
        ]
    }
}
```

- Failure (HTTP Status 401): If the order fails due to invalid parameters, authentication issues, or other errors, the server will return an error message with below json format.

```json
{
    "status": false,
    "message": "Incorrect auth. Please try again.",
    "errorcode": "IA401",
    "data": null
}
```

- Failure (HTTP Status 400): If the API Key is Invalid or expired.

```json
{
    "status": false,
    "message": "API is suspended/expired for use. Please check your API subscription and try again.",
    "errorcode": "IA403",
    "data": null
}
```
