# Market Quote and Instrument

> Source: https://tradingapi.mstock.com/docs/v1/typeB/market-quote-and-instrument/
>
> Section: Type B

> **Getting Token Numbers for Market Data**
>
> To fetch OHLC, LTP, or quote data for Type B users, you'll need the instrument token numbers. Use the Instrument Script Master API first to get the consolidated list of instruments with their corresponding token numbers and script names. Then use these token numbers in the Market OHLC Data API to retrieve the market data.

### Market Quote and Instrument APIs

| method | path | description |
| --- | --- | --- |
| GET | https://api.mstock.trade/openapi/typeb/typeb/instruments/quote | View OHLC market data |
| GET | https://api.mstock.trade/openapi/typeb/instruments/OpenAPIScripMaster | Provides the consolidated, csv formatted list of instruments |

---

### Market OHLC Data

This endpoint returns the OHLC market data identified by the exchange:tradingsymbol combination that are passed as values to the query parameter.

**Request Headers -**

- **X-Mirae-Version:** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization:** A token-based authentication header. The format is token api_key:access_token.
- **X-PrivateKey:** api_key

**cURL**

```bash
curl --location --request GET 'https://api.mstock.trade/openapi/typeb/instruments/quote' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwtToken' \
--header 'X-PrivateKey: api_key' \
--header 'Content-Type: application/json' \
--data '{
    "mode": "OHLC",
    "exchangeTokens": {
        "NSE": ["3045"],
        "BSE": ["500410"]
    }
}'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/instruments/quote', {
headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
},
// data: '{\n    "mode": "OHLC",\n    "exchangeTokens": {\n        "NSE": ["3045"],\n        "BSE": ["500410"]\n    }\n}',
data: {
    'mode': 'OHLC',
    'exchangeTokens': {
    'NSE': [
        '3045'
    ],
    'BSE': [
        '500410'
    ]
    }
}
});
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
    'mode': 'OHLC',
    'exchangeTokens': {
        'NSE': [
            '3045',
        ],
        'BSE': [
            '500410',
        ],
    },
}
conn.request(
    'GET',
    'openapi/typeb/instruments/quote',
    json.dumps(json_data),
    # '{\n    "mode": "OHLC",\n    "exchangeTokens": {\n        "NSE": ["3045"],\n        "BSE": ["500410"]\n    }\n}',
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/instruments/quote"))
    .method("GET", BodyPublishers.ofString("{\n    \"mode\": \"OHLC\",\n    \"exchangeTokens\": {\n        \"NSE\": [\"3045\"],\n        \"BSE\": [\"500410\"]\n    }\n}"))
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
| mode | string | `OHLC` `LTP` |
| exchangeTokens | string | `"NSE": ["3045"]` `"BSE": ["500410"]` |

**Request Body -** This endpoint does not require a request body or additional parameters in the query string for the retrieval of orders.

**Request Response -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): Successful OHLC Response

```json
{
    "status": "true",
    "message": "SUCCESS",
    "errorcode": "",
    "data": {
        "fetched": [
            {
                "exchange": "NSE",
                "tradingSymbol": "SBIN-EQ",
                "symbolToken": "3045",
                "ltp": 571.8,
                "open": 568.75,
                "high": 568.75,
                "low": 567.05,
                "close": 566.5
            }
        ],
        "unfetched": []
    }
}
```

-

Success (HTTP Status 200):

Successful LTP Response

```json
{
    "status": "true",
    "message": "SUCCESS",
    "errorcode": "",
    "data": {
        "fetched": [
            {
                "exchange": "NSE",
                "tradingSymbol": "SBIN-EQ",
                "symbolToken": "3045",
                "ltp": 571.75
            }
        ],
        "unfetched": []
    }
}
```

- Failure (HTTP Status 401): If the request fails due to authentication issues or invalid access token, the server will return an error message with below json format.

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

---

### Instrument Script Master

This endpoint provides the consolidated, csv formatted list of instruments available for trading

**Download:** [Script Master JSON](https://api.mstock.trade/openapi/typeb/instruments/OpenAPIScripMaster)

**Request Headers -**

- **X-Mirae-Version:** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization:** A token-based authentication header. The format is token api_key:access_token.
- **X-PrivateKey :** api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/instruments/OpenAPIScripMaster' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwt_Token' \
--header 'X-PrivateKey: api_key'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/instruments/OpenAPIScripMaster', {
headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwt_Token',
    'X-PrivateKey': 'api_key'
}
});
```

**Python**

```python
import http.client

conn = http.client.HTTPSConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwt_Token',
    'X-PrivateKey': 'api_key',
}
conn.request('GET', 'openapi/typeb/instruments/OpenAPIScripMaster', headers=headers)
response = conn.getresponse()
```

**Java**

```java
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newBuilder()
    .followRedirects(HttpClient.Redirect.NORMAL)
    .build();

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/instruments/OpenAPIScripMaster"))
    .GET()
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwt_Token")
    .setHeader("X-PrivateKey", "api_key")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -** This endpoint does not require a request body or additional parameters in the query string for the retrieval of orders.

**Request Response -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful request, the server returns a JSON array of object containing instrument details.

```json
[
     {
        "token": "877966",
        "symbol": "SENSEX",
        "name": "SENSEX25O2382700CE",
        "expiry": "23Oct2025",
        "strike": "82700",
        "lotsize": "20",
        "instrumenttype": "OPTIDX",
        "exch_seg": "BFO",
        "tick_size": "0.05"
    },
    {
        "token": "9552",
        "symbol": "RVNL",
        "name": "RVNL-EQ",
        "expiry": "",
        "strike": "",
        "lotsize": "1",
        "instrumenttype": "EQ",
        "exch_seg": "NSE",
        "tick_size": "0.05"
    },
]
```

- Failure (HTTP Status 401): If the request fails due to authentication issues or invalid access token, the server will return an error message with below json format.

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
