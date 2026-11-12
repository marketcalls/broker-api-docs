# Option Chain APIs

> Source: https://tradingapi.mstock.com/docs/v1/typeB/option-chain-apis/
>
> Section: Type B

### Option Chain APIs

The Option Chain APIs let you fetch the option chain master and option chain data of any stock.

| method | path | description |
| --- | --- | --- |
| GET | https://api.mstock.trade/openapi/typeb/getoptionchainmaster/{exch} | Fetch option chain master data |
| GET | https://api.mstock.trade/openapi/typeb/getoptionchainmaster/{exch}/{expiry}/{token} | Fetch option chain data for any stock |

---

### Option Chain Master {#option-chain-master} coming soon

This endpoint allows users to fetch the option chain master data

**Request Headers -**

- X-Mirae-Version: Specifies the version of the API being used. In this case, it is set to 1.
- Authorization: A token-based authentication header. The format is Bearer jwtToken
- Content-Type: For this request, it is set to application/x-www-form-urlencoded , which is used for submiting form data.

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/getoptionchainmaster/2' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwtToken' \
--header 'X-PrivateKey: api_key' \
--header 'Content-Type: application/json' \
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/getoptionchainmaster/2', {
headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
}
});
```

**Python**

```python
import http.client

conn = http.client.HTTPSConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json',
}
conn.request(
    'GET',
    'openapi/typeb/getoptionchainmaster/2',
    headers=headers
)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/getoptionchainmaster/2"))
    .GET()
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
    "status": true,
    "message": "SUCCESS",
    "errorcode": "",
    "data": {
        "dctExp": {
            "1": 1795876200,
            "2": 1429972200,
            "3": 1432996200,
            "4": 1435415400,
            "5": 1443277800,
            "6": 1451053800,
            "7": 1459002600,
            "8": 1429367400,
            "9": 1430490600,
            "10": 1431181800,
            "11": 1431786600,
            "12": 1466865000,
            "13": 1483194600,
            "14": 1498314600,
            "15": 1514644200,
            "16": 1530369000,
            "17": 1546093800,
            "18": 1561818600,
            "19": 1577543400
        },
        "FUTIDX": [
            "BANKNIFTY,26009,2,3,4",
            "FINNIFTY,26037,2,3,4",
            "MIDCPNIFTY,26074,2,3,4",
            "NIFTY,26000,2,3,4",
            "NIFTYNXT50,26013,2,3,4"
        ],
        "OPTIDX": [
            "BANKNIFTY,26009,2,3,4,5,6,7",
            "FINNIFTY,26037,2,3,4",
            "MIDCPNIFTY,26074,2,3,4",
            "NIFTY,26000,8,2,9,10,11,3,4,5,6,7,12,13,14,15,16,17,18,19",
            "NIFTYNXT50,26013,2,3,4"
        ],
        "OFSTK": [
            "AARTIIND,7,2,3,4",
            "ABB,13,2,3,4",
            "ABCAPITAL,21614,2,3,4",
            "ABFRL,30108,2,3,4",
            "ACC,22,2,3,4",
            "ADANIENSOL,10217,2,3,4",
            "ADANIENT,25,2,3,4",
            "ADANIGREEN,3563,2,3,4",
            "ADANIPORTS,15083,2,3,4",
            "ALKEM,11703,2,3,4",
            "AMBUJACEM,1270,2,3,4",
            "ANGELONE,324,2,3,4",
            "APLAPOLLO,25780,2,3,4",
            "APOLLOHOSP,157,2,3,4",
            "APOLLOTYRE,163,2,3",
            "ASHOKLEY,212,2,3,4",
            "ASIANPAINT,236,2,3,4",
            "ASTRAL,14418,2,3,4",
            "ATGL,6066,2,3,4",
            "AUBANK,21238,2,3,4",
            "AUROPHARMA,275,2,3,4",
            "AXISBANK,5900,2,3,4",
            "BAJAJ-AUTO,16669,2,3,4"
        ]
    }
}
```

- Failure (HTTP Status 401): If the order fails due to invalid parameters, authentication issues, or other errors, the server will return an error message with below json format.

```json
{
    "status": false,
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

### Option Chain

This endpoint allows users to fetch the option chain data for any stock

**Request Headers -**

- X-Mirae-Version: Specifies the version of the API being used. In this case, it is set to 1.
- Authorization: A token-based authentication header. The format is Bearer jwtToken
- Content-Type: For this request, it is set to application/x-www-form-urlencoded , which is used for submiting form data.

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/GetOptionChain/2/1429972200/25' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwtToken' \
--header 'X-PrivateKey: api_key' \
--header 'Content-Type: application/json' \
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/GetOptionChain/2/1429972200/25', {
headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
}
});
```

**Python**

```python
import http.client

conn = http.client.HTTPSConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json',
}
conn.request(
    'GET',
    'openapi/typeb/GetOptionChain/2/1429972200/25',
    headers=headers
)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/GetOptionChain/2/1429972200/25"))
    .GET()
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
    "status": true,
    "message": "SUCCESS",
    "errorcode": "",
    "data": {
        "contractModel": {
            "sym": "ACC",
            "exid": 2,
            "instn": 4,
            "ultk": 22,
            "exp": 1429972200,
            "expd": 0
        },
        "contractMasterModel": null,
        "call": [
            "42313,108000,0",
            "84549,112000,0",
            "51175,116000,0",
            "84553,120000,0",
            "46563,124000,0",
            "84555,128000,0",
            "84557,132000,0",
            "84559,136000,0",
            "42315,138000,0",
            "84561,140000,0",
            "64068,142000,0",
            "84563,144000,0",
            "64070,146000,0",
            "84566,148000,0",
            "64072,150000,0",
            "84603,152000,0",
            "64074,154000,0",
            "84605,156000,0"
        ],
        "put": [
            "42314,108000,0",
            "84550,112000,0",
            "51176,116000,0",
            "84554,120000,0",
            "46564,124000,0",
            "84556,128000,0",
            "84558,132000,0",
            "84560,136000,0",
            "42316,138000,0",
            "84562,140000,0",
            "64069,142000,0",
            "84564,144000,0",
            "64071,146000,0",
            "84567,148000,0",
            "64073,150000,0",
            "84604,152000,0",
            "64075,154000,0",
            "84606,156000,0",
            "64077,158000,0",
            "84612,160000,0",
            "64079,162000,0"
        ],
        "future": [
            "54458,-1,2969100"
        ],
        "spot": "ACC,22,NSEEQ"
    }
}
```

- Failure (HTTP Status 401): If the order fails due to invalid parameters, authentication issues, or other errors, the server will return an error message with below json format.

```json
{
    "status": false,
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
