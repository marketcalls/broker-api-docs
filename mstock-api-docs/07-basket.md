# Basket Orders

> Source: https://tradingapi.mstock.com/docs/v1/typeB/Basket/
>
> Section: Type B

### Basket APIs

The Basket Order APIs let you create, fetch, update and delete existing baskets.

| method | path | description |
| --- | --- | --- |
| POST | https://api.mstock.trade/openapi/typeb/CreateBasket | Create new basket |
| PUT | https://api.mstock.trade/openapi/typeb/FetchBasket | Fetch all basket |
| DELETE | https://api.mstock.trade/openapi/typeb/RenameBasket | Rename existing basket |
| POST | https://api.mstock.trade/openapi/typeb/DeleteBasket | Delete existing basket |
| GET | https://api.mstock.trade/openapi/typeb/CalculateBasket | Calculate Basket |

---

### Create Basket

This endpoint allows users to create new basket. Users must provide relevant basket details such as basket name and description of basket.

**Request Headers -**

- X-Mirae-Version: Specifies the version of the API being used. In this case, it is set to 1.
- Authorization: A token-based authentication header. The format is Bearer jwtToken
- Content-Type: For this request, it is set to application/json , which is used for submiting form data.

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/CreateBasket' \
    --header 'X-Mirae-Version: 1' \
    --header 'Authorization: Bearer jwtToken' \
    --header 'X-PrivateKey: api_key' \
    --header 'Content-Type: application/json' \
    --data '{
        "BaskName": "Basket-1",
        "BaskDesc": "Basket-1 Description"
    }'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.post(
'https://api.mstock.trade/openapi/typeb/CreateBasket',
{
    'BaskName': 'Basket-1',
    'BaskDesc': 'Basket-1 Description'
},
{
    headers: {
    'X-Mirae-Version': '1',
    'X-PrivateKey': 'api_key',
    'Authorization': 'Bearer jwtToken',
    'Content-Type': 'application/json'
    }
}
);
```

**Python**

```python
import requests

conn = http.client.HTTPConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'X-PrivateKey': 'api_key',
    'Authorization': 'Bearer jwtToken',
    'Content-Type': 'application/json',
}
json_data = {
    'BaskName': 'Basket-1',
    'BaskDesc': 'Basket-1 Description'
}
conn.request(
    'POST',
    'openapi/typeb/CreateBasket',
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/orders/regular"))
    .POST(BodyPublishers.ofString("{\n  \"BaskName\": \"Basket-1\",\n  \"BaskDesc\": \"Basket-1 Description\"}"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -** The body of the request must be URL-encoded and include the following parameters:

| Field | Type | Description |
| --- | --- | --- |
| BaskName | string | Name of the basket |
| BaskDesc | string | Descrition of the basket |

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful basket creation, the server returns a JSON object as shown below

```json
{
    "status": true,
    "message": null,
    "errorcode": null,
    "data": "Basket Created Successfully"
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

- Failure (HTTP Status 200): If basket is already exists then api will return an error message with below json format.

```json
{
    "status": false,
    "message": "Basket Already Added For This Name",
    "errorcode": "MA408",
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

---

### Fetch Basket

This endpoint allows users to create new basket. Users must provide relevant basket details such as basket name and description of basket.

**Request Headers -**

- X-Mirae-Version: Specifies the version of the API being used. In this case, it is set to 1.
- Authorization: A token-based authentication header. The format is Bearer jwtToken
- Content-Type: For this request, it is set to application/json , which is used for submiting form data.

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/FetchBasket' \
    --header 'X-Mirae-Version: 1' \
    --header 'Authorization: Bearer jwtToken' \
    --header 'X-PrivateKey: api_key' \
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/FetchBasket', {
headers: {
    'X-Mirae-Version': '1', 
    'Authorization': 'Bearer jwtToken', 
    'X-PrivateKey': 'api_key'
}
});
```

**Python**

```python
import requests

headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key'
}

response = requests.get('https://api.mstock.trade/openapi/typeb/FetchBasket', headers=headers)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/FetchBasket"))
    .GET()
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -** This endpoint does not require a request body or additional parameters in the query string for the retrieval of orders.

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful basket fetch, the server returns a JSON object as shown below

```json
{
    "status": true,
    "message": "",
    "errorcode": "",
    "data": [
        {
            "BASKET_ID": 271,
            "BASKET_NAME": "AglTest-1",
            "COUNT": 0,
            "CREATE_DATE": "2025-04-04T09:50:09Z",
            "DESCRIPTOR": "AglTest-1"
        },
        {
            "BASKET_ID": 265,
            "BASKET_NAME": "AglTest-265-Updated",
            "COUNT": 0,
            "CREATE_DATE": "2025-03-20T06:11:24Z",
            "DESCRIPTOR": "AglTest-1"
        },
        {
            "BASKET_ID": 209,
            "BASKET_NAME": "BANKEX",
            "COUNT": 1,
            "CREATE_DATE": "2024-11-13T06:42:37Z",
            "DESCRIPTOR": ""
        }
    ]
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

---

### Rename Basket

This endpoint allows users to rename an existing baslet by specifying the new basket name and existing basket ID.

**Request Headers -**

- X-Mirae-Version: Specifies the version of the API being used. In this case, it is set to 1.
- Authorization: A token-based authentication header. The format is Bearer jwtToken.
- Content-Type: Indicated the media type of the resource. For this request, it is set to application/json , which is used for submiting form data.

**cURL**

```bash
curl --location --request PUT 'https://api.mstock.trade/openapi/typeb/RenameBasket' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwtToken' \
--header 'X-PrivateKey: api_key' \
--header 'Content-Type: application/json' \
--data-urlencode 'basketName=New Basket Name Updated' \
--data-urlencode 'BasketId=255'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.post(
'https://api.mstock.trade/openapi/typeb/RenameBasket',
{
    'BaskName': 'Basket-1',
    'BaskDesc': 'Basket-1 Description Updated'
},
{
    headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken,
    'X-PrivateKey': 'api_key', 
    'Content-Type': 'application/json'
    }
}
);
```

**Python**

```python
import requests

headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
}

data = {
    "basketName": "Basket-275-Updated",
    "BasketId": "275"
}

response = requests.post('https://api.mstock.trade/openapi/typeb/RenameBasket', headers=headers, data=data)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/RenameBasket"))
    .PUT(BodyPublishers.ofString("{\n    \"basketName\": \"Basket-275-Updated\",\n    \"BasketId\": \"275\"\n}"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -** The body of the request must be URL-encoded and include the following parameters:

| Field | Type | Description |
| --- | --- | --- |
| basketName | string | New name for the basket |
| BasketId | string | The unique identifier of the basket to be renamed |

**Request Response -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful rename of basket, the server returns a JSON object containing the status.

```json
{
    "status": true,
    "message": "",
    "errorcode": "",
    "data": null
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

- Failure (HTTP Status 200): If basket name is already exists then server will return below json reponse.

```json
{
    "status": false,
    "message": "Invalid request. Please check and try again.",
    "errorcode": "MA408",
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

---

### Delete Basket

This endpoint allows users to delete an existing basket by specifying the basket ID.

**Request Headers -**

- X-Mirae-Version: Specifies the version of the API being used. In this case, it is set to 1.
- Authorization: A token-based authentication header. The format is Bearer jwtToken.
- Content-Type: Indicated the media type of the resource. For this request, it is set to application/json , which is used for submiting form data.

**cURL**

```bash
curl --location --request DELETE 'https://api.mstock.trade/openapi/typeb/DeleteBasket' \
    --header 'X-Mirae-Version: 1' \
    --header 'Authorization: Bearer jwtToken'
    --header 'X-PrivateKey: api_key' \
    --header 'Content-Type: application/json' \
    --data '{
        "BasketId": "257"
    }'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.delete('https://api.mstock.trade/openapi/typeb/DeleteBasket', {
{
  "BasketId": "257"
},
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
import requests

headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
}

data = {
    'BasketId': '255'
}

response = requests.delete('https://api.mstock.trade/openapi/typeb/DeleteBasket', headers=headers, data=data)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/DeleteBasket"))
    .DELETE(BodyPublishers.ofString("{\n    \"BasketId\": \"257\"\n}"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Path Parameter -**

| Field | Description |
| --- | --- |
| BasketId | The unique identifier of the basket to be deleted. |

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful order deletion, the server returns a JSON object containing the order ID and status.

```json
{
    "status": true,
    "message": "",
    "errorcode": "",
    "data": "Basket Deleted Successfully"
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
    "status": false,
    "message": "API is suspended/expired for use. Please check your API subscription and try again.",
    "errorcode": "IA403",
    "data": null
}
```

---

### Calculate Basket

This endpoint allows users to calculate the basket. Users must provide relevant such as basket id, product, segment, script code, basekt name, etc.

**Request Headers -**

- X-Mirae-Version: Specifies the version of the API being used. In this case, it is set to 1.
- Authorization: A token-based authentication header. The format is Bearer jwtToken
- Content-Type: For this request, it is set to application/json , which is used for submiting form data.

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typea/CalculateBasket' \
    --header 'X-Mirae-Version: 1' \
    --header 'Authorization: Bearer jwtToken' \
    --header 'X-PrivateKey: api_key' \
    --header 'Content-Type: application/json' \
    --data '{
        "include_exist_pos": "0",
        "ord_product": "C",
        "disc_qty": "0",
        "segment": "E",
        "trigger_price": "0",
        "scriptcode": "11915",
        "ord_type": "LMT",
        "basket_name": "TestAgl",
        "operation": "I",
        "order_validity": "DAY",
        "order_qty": "1",
        "script_stat": "A",
        "buy_sell_indi": "B",
        "basket_priority": "1",
        "order_price": "19.02",
        "basket_id": "231",
        "exch_id": "NSE"
    }'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.post(
'https://api.mstock.trade/openapi/typeb/CalculateBasket',
{
    "include_exist_pos": "0",
    "ord_product": "C",
    "disc_qty": "0",
    "segment": "E",
    "trigger_price": "0",
    "scriptcode": "11915",
    "ord_type": "LMT",
    "basket_name": "TestAgl",
    "operation": "I",
    "order_validity": "DAY",
    "order_qty": "1",
    "script_stat": "A",
    "buy_sell_indi": "B",
    "basket_priority": "1",
    "order_price": "19.02",
    "basket_id": "231",
    "exch_id": "NSE"
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
import requests

headers = {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
}

data = {
    "include_exist_pos": "0",
    "ord_product": "C",
    "disc_qty": "0",
    "segment": "E",
    "trigger_price": "0",
    "scriptcode": "11915",
    "ord_type": "LMT",
    "basket_name": "TestAgl",
    "operation": "I",
    "order_validity": "DAY",
    "order_qty": "1",
    "script_stat": "A",
    "buy_sell_indi": "B",
    "basket_priority": "1",
    "order_price": "19.02",
    "basket_id": "231",
    "exch_id": "NSE"
}

response = requests.post('https://api.mstock.trade/openapi/typeb/CalculateBasket', headers=headers, data=data)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/CalculateBasket"))
    .POST(BodyPublishers.ofString("{\n    \"include_exist_pos\": \"0\",\n    \"ord_product\": \"C\",\n    \"disc_qty\": \"0\",\n    \"segment\": \"E\",\n    \"trigger_price\": \"0\",\n    \"scriptcode\": \"11915\",\n    \"ord_type\": \"LMT\",\n    \"basket_name\": \"TestAgl\",\n    \"operation\": \"I\",\n    \"order_validity\": \"DAY\",\n    \"order_qty\": \"1\",\n    \"script_stat\": \"A\",\n    \"buy_sell_indi\": \"B\",\n    \"basket_priority\": \"1\",\n    \"order_price\": \"19.02\",\n    \"basket_id\": \"231\",\n    \"exch_id\": \"NSE\"\n}"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -** The body of the request must be URL-encoded and include the following parameters:

| Field | Type | Description |
| --- | --- | --- |
| include_exist_pos | string | whether to include existing position or not (0) |
| ord_product | string | Product type (C) |
| disc_qty | string | Disclosed Quantity (0) |
| segment | string | Segment (E-Equity) |
| trigger_price | string | Trigger Price |
| scriptcode | string | Script Code of underlying |
| ord_type | string | Order Type (LMT-LIMIT and MKT-MARKET) |
| basket_name | string | Basket Name |
| operation | string | Operation Type (I-Insert, E-Modify, G-Get) |
| order_validity | string | Validaty or duration of order (DAY) |
| order_qty | string | Quantity of order |
| script_stat | string | Script Stat (A) |
| buy_sell_indi | string | Transaction Type (B-BUY and S-SELL) |
| basket_priority | string | Basket Priority (1) |
| order_price | string | Order Price |
| basket_id | string | Basket ID |
| exch_id | string | Exchange (NSE and BSE) |

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful API call, the server returns a JSON object as shown below

```json
{
    "status": true,
    "message": "",
    "errorcode": "",
    "data": {
        "TOTAL_FINAL_MARGIN": 19.02,
        "TOTAL_REQ_MARGIN": 19.02,
        "BASKET_DETAILS": [
            {
                "BASKET_ID": "231",
                "BASKET_NAME": "TestAgl",
                "BASKET_PRIORITY": 1,
                "BROKERAGE": 0,
                "BUY_SELL_IND": "B",
                "EQ_VARELM_MARGIN": 19.02,
                "EXCH_ID": "NSE",
                "OPT_BUY_PREM": 0,
                "ORD_DISC_QTY": 0,
                "ORD_PRICE": 19.02,
                "ORD_QTY": 1,
                "ORD_SYMBOL": "YESBANK",
                "ORD_SYM_NAME": "YESBANK",
                "ORD_TRIGG_PRICE": 0,
                "ORD_TYPE": "LMT",
                "ORD_VALIDITY": "DAY",
                "PRODUCT": "C",
                "REQ_EXP": 0,
                "REQ_MARGIN": 19.02,
                "REQ_SPAN": 0,
                "SCRIPT_CODE": "11915",
                "SCRIPT_STATUS": "A",
                "SEGMENT": "E"
            }
        ]
    }
}
```

- Failure (HTTP Status 401): If the API request fails due to invalid parameters, authentication issues, or other errors, the server will return an error message with below json format.

```json
{
    "status": false,
    "message": "Invalid request. Please try again.",
    "errorcode": "IA401",
    "data": null
}
```

- Failure (HTTP Status 200): If basket calculation is already done then below response will be done.

```json
{
    "status": false,
    "message": "Script Already Added",
    "errorcode": "MA408",
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

---
