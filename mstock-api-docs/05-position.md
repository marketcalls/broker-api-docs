# Net Position

> Source: https://tradingapi.mstock.com/docs/v1/typeB/Position/
>
> Section: Type B

### Net Position APIs

| method | path | description |
| --- | --- | --- |
| GET | https://api.mstock.trade/openapi/typeb/portfolio/positions | view all their existing orders |
| POST | https://api.mstock.trade/openapi/typeb/portfolio/convertposition | Convert position |

---

### Net Position

This endpoint allows users to retrieve a list of their trading orders. Users can view all their existing orders

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization :** A token-based authentication header. The format is token api_key:jwtToken.
- **X-PrivateKey :** api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/portfolio/positions' \
    --header 'X-Mirae-Version: 1' \
    --header 'X-PrivateKey: api_key' \
    --header 'Authorization: Bearer jwtToken'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/portfolio/positions', {
headers: {
    'X-Mirae-Version': '1',
    'X-PrivateKey': 'api_key',
    'Authorization': 'Bearer jwtToken'
}
});
```

**Python**

```python
import http.client

conn = http.client.HTTPConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'X-PrivateKey': 'api_key',
    'Authorization': 'Bearer jwtToken',
}
conn.request('GET', 'openapi/typeb/portfolio/positions', headers=headers)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/portfolio/positions"))
    .GET()
    .setHeader("X-Mirae-Version", "1")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Authorization", "Bearer jwtToken")
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
    "errorcode": "",
    "data": [
        {
            "exchange": "NSE",
            "symboltoken": "50374",
            "producttype": "INTRADAY",
            "tradingsymbol": "",
            "symbolname": "NIFTY-07Nov2024-24000-CE",
            "instrumenttype": "OPTIDX",
            "priceden": "",
            "pricenum": "",
            "genden": "",
            "gennum": "",
            "precision": "",
            "multiplier": "1",
            "boardlotsize": "",
            "buyqty": "100",
            "sellqty": "600",
            "buyamount": "800.1",
            "sellamount": "799.97",
            "symbolgroup": "",
            "strikeprice": "24000",
            "optiontype": "CE",
            "expirydate": "07-Nov-2024",
            "lotsize": "25",
            "cfbuyqty": "0",
            "cfsellqty": "0",
            "cfbuyamount": "",
            "cfsellamount": "",
            "buyavgprice": "800.1",
            "sellavgprice": "799.97",
            "avgnetprice": "799.94",
            "netvalue": "399970",
            "netqty": "-500",
            "totalbuyvalue": "80010",
            "totalsellvalue": "479980",
            "cfbuyavgprice": "0",
            "cfsellavgprice": "0",
            "totalbuyavgprice": "",
            "totalsellavgprice": "",
            "netprice": "799.94"
        },
        {
            "exchange": "NSE",
            "symboltoken": "50374",
            "producttype": "CARRYFORWARD",
            "tradingsymbol": "",
            "symbolname": "NIFTY-07Nov2024-24000-CE",
            "instrumenttype": "OPTIDX",
            "priceden": "",
            "pricenum": "",
            "genden": "",
            "gennum": "",
            "precision": "",
            "multiplier": "1",
            "boardlotsize": "",
            "buyqty": "150",
            "sellqty": "100",
            "buyamount": "800.1",
            "sellamount": "799.9",
            "symbolgroup": "",
            "strikeprice": "24000",
            "optiontype": "CE",
            "expirydate": "07-Nov-2024",
            "lotsize": "25",
            "cfbuyqty": "0",
            "cfsellqty": "0",
            "cfbuyamount": "",
            "cfsellamount": "",
            "buyavgprice": "800.1",
            "sellavgprice": "799.9",
            "avgnetprice": "800.5",
            "netvalue": "-40025",
            "netqty": "50",
            "totalbuyvalue": "120015",
            "totalsellvalue": "79990",
            "cfbuyavgprice": "0",
            "cfsellavgprice": "0",
            "totalbuyavgprice": "",
            "totalsellavgprice": "",
            "netprice": "800.5"
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

### Position Converstion

Each position has one margin product. These products affect how the user's margin usage and free cash values are computed, and a user may wish to convert or change a position's margin product on timely basis.

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization :** A token-based authentication header. The format is Bearer jwtToken.
- **X-PrivateKey:** api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/portfolio/convertposition' \
    --header 'X-Mirae-Version: 1' \
    --header 'Authorization: Bearer jwtToken'\
    --header 'X-PrivateKey: api_key'\
    --data '{
    "exchange": "NSE",
    "symboltoken": "3787",
    "oldproducttype": "DELIVERY",
    "newproducttype": "INTRADAY",
    "tradingsymbol": "WIPRO-EQ",
    "symbolname": "WIPRO",
    "instrumenttype": "",
    "priceden": "",
    "pricenum": "",
    "genden": "",
    "gennum": "",
    "precision": "",
    "multiplier": "",
    "boardlotsize": "",
    "buyqty": "",
    "sellqty": "",
    "buyamount": "",
    "sellamount": "",
    "transactiontype": "BUY",
    "quantity": 1,
    "type": "DAY"
    }'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.post(
'https://api.mstock.trade/openapi/typeb/portfolio/convertposition',
'{\n    "exchange": "NSE",\n    "symboltoken": "3787",\n    "oldproducttype": "DELIVERY",\n    "newproducttype": "INTRADAY",\n    "tradingsymbol": "WIPRO-EQ",\n    "symbolname": "WIPRO",\n    "instrumenttype": "",\n    "priceden": "",\n    "pricenum": "",\n    "genden": "",\n    "gennum": "",\n    "precision": "",\n    "multiplier": "",\n    "boardlotsize": "",\n    "buyqty": "",\n    "sellqty": "",\n    "buyamount": "",\n    "sellamount": "",\n    "transactiontype": "BUY",\n    "quantity": 1,\n    "type": "DAY"\n    }',
{
    headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
}
);
```

**Python**

```python
import http.client

conn = http.client.HTTPConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/x-www-form-urlencoded',
}
conn.request(
    'POST',
    'openapi/typeb/portfolio/convertposition',
    '{\n    "exchange": "NSE",\n    "symboltoken": "3787",\n    "oldproducttype": "DELIVERY",\n    "newproducttype": "INTRADAY",\n    "tradingsymbol": "WIPRO-EQ",\n    "symbolname": "WIPRO",\n    "instrumenttype": "",\n    "priceden": "",\n    "pricenum": "",\n    "genden": "",\n    "gennum": "",\n    "precision": "",\n    "multiplier": "",\n    "boardlotsize": "",\n    "buyqty": "",\n    "sellqty": "",\n    "buyamount": "",\n    "sellamount": "",\n    "transactiontype": "BUY",\n    "quantity": 1,\n    "type": "DAY"\n    }',
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/portfolio/convertposition"))
    .POST(BodyPublishers.ofString("{\n    \"exchange\": \"NSE\",\n    \"symboltoken\": \"3787\",\n    \"oldproducttype\": \"DELIVERY\",\n    \"newproducttype\": \"INTRADAY\",\n    \"tradingsymbol\": \"WIPRO-EQ\",\n    \"symbolname\": \"WIPRO\",\n    \"instrumenttype\": \"\",\n    \"priceden\": \"\",\n    \"pricenum\": \"\",\n    \"genden\": \"\",\n    \"gennum\": \"\",\n    \"precision\": \"\",\n    \"multiplier\": \"\",\n    \"boardlotsize\": \"\",\n    \"buyqty\": \"\",\n    \"sellqty\": \"\",\n    \"buyamount\": \"\",\n    \"sellamount\": \"\",\n    \"transactiontype\": \"BUY\",\n    \"quantity\": 1,\n    \"type\": \"DAY\"\n    }"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Content-Type", "application/x-www-form-urlencoded")
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
    "errorcode": "",
    "data": null
}
```

- Failure (HTTP Status 200): bad request

```json
{
    "status": "false",
    "message": "NSE EQUITY 3787 EQ AJAY B 1 C INSUFICIENT QUANTITY TO CONVERT. INSUFICIENT QUANTITY: 1 AVAILABLE QUANTITY: 0",
    "errorcode": "MA0034",
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
