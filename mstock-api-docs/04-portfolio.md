# Portfolio

> Source: https://tradingapi.mstock.com/docs/v1/typeB/Portfolio/
>
> Section: Type B

### Portfolio APIs

| method | path | description |
| --- | --- | --- |
| GET | https://api.mstock.trade/openapi/typeb/portfolio/holdings | View all holdings |

---

### Holdings

This endpoint offers the users to retrieve all the list of holdings that contain the user's portfolio of long term equity delivery stocks.

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization :** A token-based authentication header. The format is Bearer jwtToken.
- **X-PrivateKey:** api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/portfolio/holdings' \
    --header 'X-Mirae-Version: 1' \
    --header 'Authorization: Bearer jwtToken'
    --header 'X-PrivateKey: api_key'\
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/portfolio/holdings', {
headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key'
}
});
```

**Python**

```python
import http.client

conn = http.client.HTTPConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
}
conn.request('GET', 'openapi/typeb/portfolio/holdings', headers=headers)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/portfolio/holdings"))
    .GET()
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -**

This endpoint does not require a request body or additional parameters in the query string for the retrieval of orders.

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful retrieval, the server returns a JSON array of client positions.

```json
{
    "status": "true",
    "message": "SUCCESS",
    "errorcode": null,
    "data": [
        {
            "tradingsymbol": "BANK OF MAHARASHTRA",
            "exchange": null,
            "isin": "INE457A01014",
            "t1quantity": 0,
            "realisedquantity": 0,
            "quantity": 10,
            "authorisedquantity": 0,
            "product": null,
            "collateralquantity": 0,
            "collateraltype": null,
            "haircut": 0,
            "averageprice": 30,
            "ltp": 84.7,
            "symboltoken": "11377",
            "close": 51.1,
            "profitandloss": 0,
            "pnlpercentage": 0
        },
        {
            "tradingsymbol": "PSP PROJECTS LIMITED",
            "exchange": null,
            "isin": "INE488V01015",
            "t1quantity": 0,
            "realisedquantity": 0,
            "quantity": 100,
            "authorisedquantity": 0,
            "product": null,
            "collateralquantity": 100,
            "collateraltype": null,
            "haircut": 0,
            "averageprice": 513.35,
            "ltp": 774.75,
            "symboltoken": "20877",
            "close": 659.95,
            "profitandloss": 0,
            "pnlpercentage": 0
        }
    ]
}
```

-

Failure (HTTP Status 401):

If authentication fails, the server will return an error message

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
