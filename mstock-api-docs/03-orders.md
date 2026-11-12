# Orders

> Source: https://tradingapi.mstock.com/docs/v1/typeB/Orders/
>
> Section: Type B

### Glossary

| param | value | Description |
| --- | --- | --- |
| Variety | NORMAL | Normal Order (Regular) |
|  | AMO | After Market Order |
|  | STOPLOSS | Stop Loss Order |
| Order Type | MARKET | Market Order |
|  | LIMIT | Limit Order |
|  | STOPLOSS_LIMIT | Stop Loss Order |
|  | STOPLOSS_MARKET | Stop Loss Market Order |
| Product Type | DELIVERY | Cash & Carry for equity |
|  | INTRADAY | Margin Intraday Squareoff |
|  | MARGIN | Margin Delivery |
|  | CARRYFORWARD | Normal for futures and options |
| Duration | DAY | Regular order |
|  | IOC | Immediate or Cancel |

---

### Orders APIs

The order APIs let you place orders of different varities, modify and cancel pending orders, retrieve the daily order and more.

| method | path | description |
| --- | --- | --- |
| GET | https://api.mstock.trade/openapi/typeb/orders/regular | Place a new order |
| PUT | https://api.mstock.trade/openapi/typeb/orders/regular/{OrderID} | Modify a pending order |
| DELETE | https://api.mstock.trade/openapi/typeb/orders/regular/{OrderID} | Cancel a pending order |
| POST | https://api.mstock.trade/openapi/typeb/orders/cancelall | Cancel all pending order |
| GET | https://api.mstock.trade/openapi/typeb/orders | View all the existing orders. |
| GET | https://api.mstock.trade/openapi/typeb/trades | This endpoint returns a list of all trades generated upon the |
| GET | https://api.mstock.trade/openapi/typeb/order/details | View the status of individual order |

---

### Order Placement

This endpoint allows users to place a regular trading order in the specified market. Users must provide relevant order details such as the trading symbol, exchange, transaction type, and other order specifics.

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization :** A token-based authentication header. The format is token jwtToken.
- **Content-Type :** A token-based authentication header. The format is token jwtToken. Content-Type: For this request, it is set to application/json, which is used for submiting form data through body.
- **X-PrivateKey :** api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/orders/regular' \
    --header 'X-Mirae-Version: 1' \
    --header 'X-PrivateKey: api_key' \
    --header 'Authorization: Bearer jwtToken' \
    --header 'Content-Type: application/json' \
    --data '{
    "variety": "NORMAL",
    "tradingsymbol": "ACC-EQ",
    "symboltoken": "22",
    "exchange": "NSE",
    "transactiontype": "BUY",
    "ordertype": "MARKET",
    "quantity": "20",
    "producttype": "DELIVERY",
    "price": "194.50",
    "triggerprice": "0",
    "squareoff": "0",
    "stoploss": "0",
    "trailingStopLoss": "",
    "disclosedquantity": "",
    "duration": "DAY",
    "ordertag": ""
    }'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get(
'https://api.mstock.trade/openapi/typeb/orders/regular',
// '{\n    "variety": "NORMAL",\n    "tradingsymbol": "ACC-EQ",\n    "symboltoken": "22",\n    "exchange": "NSE",\n    "transactiontype": "BUY",\n    "ordertype": "MARKET",\n    "quantity": "20",\n    "producttype": "DELIVERY",\n    "price": "194.50",\n    "triggerprice": "0",\n    "squareoff": "0",\n    "stoploss": "0",\n    "trailingStopLoss": "",\n    "disclosedquantity": "",\n    "duration": "DAY",\n    "ordertag": ""\n    }',
{
    'variety': 'NORMAL',
    'tradingsymbol': 'ACC-EQ',
    'symboltoken': '22',
    'exchange': 'NSE',
    'transactiontype': 'BUY',
    'ordertype': 'MARKET',
    'quantity': '20',
    'producttype': 'DELIVERY',
    'price': '194.50',
    'triggerprice': '0',
    'squareoff': '0',
    'stoploss': '0',
    'trailingStopLoss': '',
    'disclosedquantity': '',
    'duration': 'DAY',
    'ordertag': ''
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
import http.client
import json

conn = http.client.HTTPConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'X-PrivateKey': 'api_key',
    'Authorization': 'Bearer jwtToken',
    'Content-Type': 'application/json',
}
json_data = {
    'variety': 'NORMAL',
    'tradingsymbol': 'ACC-EQ',
    'symboltoken': '22',
    'exchange': 'NSE',
    'transactiontype': 'BUY',
    'ordertype': 'MARKET',
    'quantity': '20',
    'producttype': 'DELIVERY',
    'price': '194.50',
    'triggerprice': '0',
    'squareoff': '0',
    'stoploss': '0',
    'trailingStopLoss': '',
    'disclosedquantity': '',
    'duration': 'DAY',
    'ordertag': '',
}
conn.request(
    'GET',
    'openapi/typeb/orders/regular',
    json.dumps(json_data),
    # '{\n    "variety": "NORMAL",\n    "tradingsymbol": "ACC-EQ",\n    "symboltoken": "22",\n    "exchange": "NSE",\n    "transactiontype": "BUY",\n    "ordertype": "MARKET",\n    "quantity": "20",\n    "producttype": "DELIVERY",\n    "price": "194.50",\n    "triggerprice": "0",\n    "squareoff": "0",\n    "stoploss": "0",\n    "trailingStopLoss": "",\n    "disclosedquantity": "",\n    "duration": "DAY",\n    "ordertag": ""\n    }',
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
    .GET(BodyPublishers.ofString("{\n    \"variety\": \"NORMAL\",\n    \"tradingsymbol\": \"ACC-EQ\",\n    \"symboltoken\": \"22\",\n    \"exchange\": \"NSE\",\n    \"transactiontype\": \"BUY\",\n    \"ordertype\": \"MARKET\",\n    \"quantity\": \"20\",\n    \"producttype\": \"DELIVERY\",\n    \"price\": \"194.50\",\n    \"triggerprice\": \"0\",\n    \"squareoff\": \"0\",\n    \"stoploss\": \"0\",\n    \"trailingStopLoss\": \"\",\n    \"disclosedquantity\": \"\",\n    \"duration\": \"DAY\",\n    \"ordertag\": \"\"\n    }"))
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
| variety | string | Variety of the order ( `NORMAL` `AMO` `STOPLOSS` ) |
| tradingsymbol | string | Refer Trading Symbol in Tables |
| symboltoken | string | Token of the contract for which modify is being sent |
| exchange | string | Exchange name : `NSE` `BSE` `NFO` `BFO` |
| transaction_type | string | The trading side of transaction : `BUY` `SELL` |
| order_type | string | Order Type :`LIMIT` `MARKET` `STOP_LOSS` `STOP_LOSS_MARKET` |
| quantity | string | Number of shares for the order |
| producttype | string | Product Type `DELIVERY` `INTRADAY` `MARGIN` `CARRYFORWARD` |
| price | string | Price at which order is placed |
| trigger_price | string | Price at which the order is triggered, in case of `STOP_LOSS` `STOP_LOSS_MARKET` |
| squareoff | string | Auto Sqaure off |
| stoploss | string | Stop Loss order |
| trailingStopLoss | string | Trailing Stop Loss order |
| disclosedquantity | string | Number of shares visible (Keep more than 30% of quantity) |
| duration | string | Regular Order Immediate or Cancel |
| ordertag | string | It is optional to apply to an order to identify. The length of the tag should be less than 20 (alphanumeric) characters. |

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful order placement, the server returns a JSON object containing the order ID and status
```json
{
    "status": "true",
    "message": "SUCCESS",
    "errorcode": "",
    "data": {
        "script": "ACC-EQ",
        "orderid": "1191241106101",
        "uniqueorderid": ""
    }
}
```
- Failure (HTTP Status 400): If the order fails due to invalid parameters, authentication issues, or other errors, the server will return an error message with below json format.

```json
{
    "status": "false",
    "message": "Invalid request. Please try again.",
    "errorcode": "IA401",
    "data": null
}
```

- Failure (HTTP Status 200): If market is closed or not connected to NSE then api will return an error message with below json format.

```json
{
    "status": "false",
    "message": "RMS:1141241105101:NSE,EQUITY,22,ACC,INTRADAY,,EQ,XXXXX,B,1,I,22,ACC,INTRADAY,89.44995,FUND LIMIT INSUFFICIENT,AVAILABLE FUND=0,ADDITIONAL REQUIRED FUND=572.36,CALCULATED MARGIN FOR ORDER=572.36",
    "errorcode": "RS-0111",
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

### Order Modification

This endpoint allows users to update/modify an existing order by specifying the order ID and providing the updated order details.

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization :** A token-based authentication header. The format is token jwtToken.
- **Content-Type :** Indicated the media type of the resource. For this request, it is set to application/json, which is used for submiting form data through body
- **X-PrivateKey :** api_key

**cURL**

```bash
curl --location --request PUT 'https://api.mstock.trade/openapi/typeb/orders/regular/1191241106101' \
    --header 'X-Mirae-Version: 1' \
    --header 'X-PrivateKey: api_key' \
    --header 'Authorization: Bearer jwtToken' \
    --header 'Content-Type: application/json' \
    --data '{
    "variety": "NORMAL",
    "tradingsymbol": "ACC-EQ",
    "symboltoken": "22",
    "exchange": "NSE",
    "transactiontype": "BUY",
    "orderid": "1191241106101",
    "ordertype": "MARKET",
    "quantity": "15",
    "producttype": "DELIVERY",
    "duration": "DAY",
    "price": "2240",
    "triggerprice": "0",
    "disclosedquantity": "",
    "modqty_remng": "0"
    }'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.put(
'https://api.mstock.trade/openapi/typeb/orders/regular/1191241106101',
// '{\n    "variety": "NORMAL",\n    "tradingsymbol": "ACC-EQ",\n    "symboltoken": "22",\n    "exchange": "NSE",\n    "transactiontype": "BUY",\n    "orderid": "1191241106101",\n    "ordertype": "MARKET",\n    "quantity": "15",\n    "producttype": "DELIVERY",\n    "duration": "DAY",\n    "price": "2240",\n    "triggerprice": "0",\n    "disclosedquantity": "",\n    "modqty_remng": "0"\n    }',
{
    'variety': 'NORMAL',
    'tradingsymbol': 'ACC-EQ',
    'symboltoken': '22',
    'exchange': 'NSE',
    'transactiontype': 'BUY',
    'orderid': '1191241106101',
    'ordertype': 'MARKET',
    'quantity': '15',
    'producttype': 'DELIVERY',
    'duration': 'DAY',
    'price': '2240',
    'triggerprice': '0',
    'disclosedquantity': '',
    'modqty_remng': '0'
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
import http.client
import json

conn = http.client.HTTPConnection('api.mstock.trade')
headers = {
    'X-Mirae-Version': '1',
    'X-PrivateKey': 'api_key',
    'Authorization': 'Bearer jwtToken',
    'Content-Type': 'application/json',
}
json_data = {
    'variety': 'NORMAL',
    'tradingsymbol': 'ACC-EQ',
    'symboltoken': '22',
    'exchange': 'NSE',
    'transactiontype': 'BUY',
    'orderid': '1191241106101',
    'ordertype': 'MARKET',
    'quantity': '15',
    'producttype': 'DELIVERY',
    'duration': 'DAY',
    'price': '2240',
    'triggerprice': '0',
    'disclosedquantity': '',
    'modqty_remng': '0',
}
conn.request(
    'PUT',
    'openapi/typeb/orders/regular/1191241106101',
    json.dumps(json_data),
    # '{\n    "variety": "NORMAL",\n    "tradingsymbol": "ACC-EQ",\n    "symboltoken": "22",\n    "exchange": "NSE",\n    "transactiontype": "BUY",\n    "orderid": "1191241106101",\n    "ordertype": "MARKET",\n    "quantity": "15",\n    "producttype": "DELIVERY",\n    "duration": "DAY",\n    "price": "2240",\n    "triggerprice": "0",\n    "disclosedquantity": "",\n    "modqty_remng": "0"\n    }',
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/orders/regular/1191241106101"))
    .PUT(BodyPublishers.ofString("{\n    \"variety\": \"NORMAL\",\n    \"tradingsymbol\": \"ACC-EQ\",\n    \"symboltoken\": \"22\",\n    \"exchange\": \"NSE\",\n    \"transactiontype\": \"BUY\",\n    \"orderid\": \"1191241106101\",\n    \"ordertype\": \"MARKET\",\n    \"quantity\": \"15\",\n    \"producttype\": \"DELIVERY\",\n    \"duration\": \"DAY\",\n    \"price\": \"2240\",\n    \"triggerprice\": \"0\",\n    \"disclosedquantity\": \"\",\n    \"modqty_remng\": \"0\"\n    }"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Path Parameter -**

| Field | Description |
| --- | --- |
| order_id | The unique identifier of the order to be updated or modified |

**Request Body -** The body of the request must be URL-encoded and include the following parameters:

| Field | Type | Description |
| --- | --- | --- |
| variety | string | Variety of the order ( `NORMAL` `AMO` `STOPLOSS` ) |
| tradingsymbol | string | Refer Trading Symbol in Tables |
| symboltoken | string | Token of the contract for which modify is being sent |
| exchange | string | Exchange name : `NSE` `BSE` |
| transaction_type | string | The trading side of transaction : `BUY` `SELL` |
| orderid | string | Order Id Number |
| order_type | string | Order Type :`LIMIT` `MARKET` `STOP_LOSS` `STOP_LOSS_MARKET` |
| quantity | string | Number of shares for the order |
| producttype | string | Product Type `DELIVERY` `INTRADAY` `MARGIN` `CARRYFORWARD` `CNC` `INTRADAY` `MARGIN` `MTF` `CO` `BO` |
| duration | string | Regular Order Immediate or Cancel |
| price | string | Price at which order is placed |
| trigger_price | string | Price at which the order is triggered, in case of `STOP_LOSS` `STOP_LOSS_MARKET` |
| squareoff | string | Auto Sqaure off |
| disclosedquantity | string | Number of shares visible (Keep more than 30% of quantity) |
| modqty_remng | string | Remaining quantity |

**Request Response -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful order update, the server returns a JSON object containing the order ID and status.

```json
{
    "status": "true",
    "message": "SUCCESS",
    "errorcode": "",
    "data": {
        "orderid": " 1191241106101",
        "uniqueorderid": ""
    }
}
```

- Failure (HTTP Status 401): If the order fails due to invalid parameters, authentication issues, or other errors, the server will return an error message with below json format.

```json
{
    "status": "false",
    "message": "Enter valid trigger price.",
    "errorcode": "400",
    "data": null
}
```

- Failure (HTTP Status 200): If orderid does not exist then server will return below json reponse.

```json
{
    "status": "false",
    "message": "Order is Cancelled.Kindly refresh your OrderBook",
    "errorcode": "RS-0034",
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

### Order Cancellation

This endpoint allows users to delete an existing order specified by the order ID. Deleting an order will cancel the specified order.

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization :** A token-based authentication header. The format is token jwtToken.
- **Content-Type :** Indicated the media type of the resource. For this request, it is set to application/json, which is used for submiting form data through body
- **X-PrivateKey :** api_key

**cURL**

```bash
curl --location --request DELETE 'https://api.mstock.trade/openapi/typeb/orders/regular/1112241106105' \
    --header 'X-Mirae-Version: 1' \
    --header 'X-PrivateKey: api_key' \
    --header 'Authorization: Bearer jwtToken' \
    --header 'Content-Type: application/json' \
    --data '{
    "variety": "NORMAL",
    "orderid": "1181250130106"
    }'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.delete('https://api.mstock.trade/openapi/typeb/orders/regular/1112241106105', {
headers: {
    'X-Mirae-Version': '1',
    'X-PrivateKey': 'api_key',
    'Authorization': 'Bearer jwtToken',
    'Content-Type': 'application/json'
},
// data: '{\n    "variety": "NORMAL",\n    "orderid": "1181250130106"\n    }',
data: {
    'variety': 'NORMAL',
    'orderid': '1181250130106'
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
    'X-PrivateKey': 'api_key',
    'Authorization': 'Bearer jwtToken',
    'Content-Type': 'application/json',
}
json_data = {
    'variety': 'NORMAL',
    'orderid': '1181250130106',
}
conn.request(
    'DELETE',
    'openapi/typeb/orders/regular/1112241106105',
    json.dumps(json_data),
    # '{\n    "variety": "NORMAL",\n    "orderid": "1181250130106"\n    }',
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/orders/regular/1112241106105"))
    .method("DELETE", BodyPublishers.ofString("{\n    \"variety\": \"NORMAL\",\n    \"orderid\": \"1181250130106\"\n    }"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Path Parameter -**

| Field | Description |
| --- | --- |
| order_id | The unique identifier of the order to be updated or modified |

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful order deletion, the server returns a JSON object containing the order ID and status.

```json
{
    "status": "true",
    "message": "SUCCESS",
    "errorcode": "",
    "data": {
        "orderid": "201020000000080",
        "uniqueorderid": ""
    }
}
```

- Failure (HTTP Status 200): If orderid does not exist then server will return below json reponse.

```json
{
    "status": "false",
    "message": "Order is Cancelled.Kindly refresh your OrderBook",
    "errorcode": "RS-00093",
    "data": null
}
```

- Failure (HTTP Status 400): Invalid product error

```json
{
    "status": "false",
    "message": "Invalid product. valid product types allowed are DELIVERY, INTRADAY and CARRYFORWARD.",
    "errorcode": "400",
    "data": null
}
```

---

### Cancel All

This endpoint allows users to cancel all the orders at once.

**Request Headers -**

- **X-Mirae-Version:** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization:** A token-based authentication header. The format is token jwtToken.
- **X-PrivateKey:** api_key

**cURL**

```bash
curl --location --request POST 'https://api.mstock.trade/openapi/typeb/orders/cancelall' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwtToken' \
--header 'X-PrivateKey: api_key' \
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.post(
'https://api.mstock.trade/openapi/typeb/orders/cancelall',
'',
{
    headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key'
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
}
conn.request('POST', 'openapi/typeb/orders/cancelall', headers=headers)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/orders/cancelall"))
    .POST(HttpRequest.BodyPublishers.noBody())
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful order deletion, the server returns a JSON object containing the order ID and status.

```json
{
    "status": "success",
    "data": {
        "order_id": "1161241001100"
    }
}
```

- Failure (HTTP Status 200): If orderid does not exist then server will return below json reponse.

```json
{
    "status": "error",
    "message": "Order Does not Exsist.Need to refresh orderbook / relogin in application ",
    "error_type": "InputException",
    "data": null
}
```

-

Failure (HTTP Status 400):

If the API Key is Invalid or expired.

```json
{
    "status": "false",
    "message": "API is suspended/expired for use. Please check your API subscription and try again.",
    "errorcode": "IA403",
    "data": null
}
```

---

### Order Book

This endpoint allows users to retrieve a list of their trading orders. Users can view all their existing orders.

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization :** A token-based authentication header. The format is token jwtToken.
- **X-PrivateKey :** api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/orders' \
    --header 'X-Mirae-Version: 1' \
    --header 'X-PrivateKey: api_key' \
    --header 'Authorization: Bearer jwtToken' \
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/orders', {
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
conn.request('GET', 'openapi/typeb/orders', headers=headers)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/orders"))
    .GET()
    .setHeader("X-Mirae-Version", "1")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Authorization", "Bearer jwtToken")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -** This endpoint does not require a request body or additional parameters in the query string for the retrieval of orders.

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful order deletion, the server returns a JSON object containing the order ID and status.

```json
{
    "status": "true",
    "message": "SUCCESS",
    "errorcode": "",
    "data": [
        {
            "variety": null,
            "ordertype": "SL",
            "producttype": "MARGIN",
            "duration": "DAY",
            "price": "2400.00",
            "triggerprice": "2390",
            "quantity": "900",
            "disclosedquantity": "0",
            "squareoff": "0",
            "stoploss": "0",
            "trailingstoploss": "0",
            "tradingsymbol": "ACC-28Nov2024-2400-CE",
            "transactiontype": "BUY",
            "exchange": "NSE",
            "symboltoken": "75307",
            "instrumenttype": "OPTSTK",
            "strikeprice": "2400",
            "optiontype": "CE",
            "expirydate": "2024-Nov-28",
            "lotsize": "",
            "cancelsize": "0",
            "averageprice": "0",
            "filledshares": "0",
            "unfilledshares": "0",
            "orderid": "1142241106106",
            "text": "EXCH:16284:The order price is out of the days price range.",
            "status": "Rejected",
            "orderstatus": "Rejected",
            "updatetime": "2024-Nov-06 12:42:18",
            "exchtime": "",
            "exchorderupdatetime": "2024-Nov-06 12:42:18",
            "fillid": "",
            "filltime": "",
            "parentorderid": "",
            "uniqueorderid": "",
            "exchangeorderid": "1000000000017285"
        },
        {
            "variety": null,
            "ordertype": "SL",
            "producttype": "MARGIN",
            "duration": "DAY",
            "price": "2400.00",
            "triggerprice": "2390",
            "quantity": "900",
            "disclosedquantity": "0",
            "squareoff": "0",
            "stoploss": "0",
            "trailingstoploss": "0",
            "tradingsymbol": "ACC-28Nov2024-FUT",
            "transactiontype": "BUY",
            "exchange": "NSE",
            "symboltoken": "35593",
            "instrumenttype": "FUTSTK",
            "strikeprice": "-0.01",
            "optiontype": "XX",
            "expirydate": "2024-Nov-28",
            "lotsize": "",
            "cancelsize": "0",
            "averageprice": "0",
            "filledshares": "0",
            "unfilledshares": "0",
            "orderid": "1132241106107",
            "text": "CONFIRMED",
            "status": "Pending",
            "orderstatus": "Pending",
            "updatetime": "2024-Nov-06 12:41:00",
            "exchtime": "",
            "exchorderupdatetime": "2024-Nov-06 12:41:00",
            "fillid": "",
            "filltime": "",
            "parentorderid": "",
            "uniqueorderid": "",
            "exchangeorderid": "1000000000017276"
        }
    ]
}
```

- Failure (HTTP Status 400): If authentication fails, the server will return an error message

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

### Trade Book

This endpoint returns the trade book with all executed trades.

**Request Headers -**

- X-Mirae-Version: Specifies the version of the API being used. In this case, it is set to 1.
- Authorization: A token-based authentication header. The format is token jwtToken.
- X-PrivateKey: api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/tradebook' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwtToken' \
--header 'X-PrivateKey: api_key'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/tradebook', {
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
conn.request('GET', 'openapi/typeb/tradebook', headers=headers)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/tradebook"))
    .GET()
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -** This endpoint does not require a request body or additional parameters in the query string.

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful request, the server returns a JSON object containing the trade book data.

```json
{
  "status": "true",
  "message": "SUCCESS",
  "errorcode": "",
  "data": [
    {
      "ALGO_ID": "0",    
      "BUY_SELL": "Sell",
      "CLIENT_ID": "MA68XXXXX",
      "ENCASH_FLG": "N",
      "EXCHANGE": "NSE",
      "EXCH_ORDER_NUMBER": "1100000048872942",
      "EXPIRY_DATE": "0",
      "FULL_SYMBOL": "VODAFONE IDEA LIMITED",
      "GTC_FLG": "N",
      "INSTRUMENT_NAME": "EQUITY",
      "MKT_PROTECT_FLG": "N",
      "MKT_PROTECT_VAL": 0,
      "MKT_TYPE": "NL",
      "OPT_TYPE": "XX",
      "ORDER_DATE_TIME": "10-06-2025 13:08:42",
      "ORDER_NUMBER": "21612506101476",
      "ORDER_TYPE": "MARKET",
      "PAN_NO": "BYYPCXXXXX",
      "PARTICIPANT_TYPE": "B",
      "PRICE": 6.98,
      "PRODUCT": "CNC",
      "QUANTITY": 4,
      "R": 1,
      "REMARKS1": "NA",
      "REMARKS2": "NA",
      "SEC_ID": "14366",
      "SEGMENT": "E",
      "SETTLOR": "90144",
      "SOURCE_FLG": "WEB",
      "STRIKE_PRICE": 0,
      "SYMBOL": "IDEA",
      "TRADE_NUMBER": "206465040",
      "TRADE_VALUE": 27.92
    },
    {
      "ALGO_ID": "0",
      "BUY_SELL": "Buy",
      "CLIENT_ID": "MA68XXXXX",
      "ENCASH_FLG": "N",
      "EXCHANGE": "NSE",
      "EXCH_ORDER_NUMBER": "1100000045177810",
      "EXPIRY_DATE": "0",
      "FULL_SYMBOL": "VODAFONE IDEA LIMITED",
      "GTC_FLG": "N",
      "INSTRUMENT_NAME": "EQUITY",
      "MKT_PROTECT_FLG": "N",
      "MKT_PROTECT_VAL": 0,
      "MKT_TYPE": "NL",
      "OPT_TYPE": "XX",
      "ORDER_DATE_TIME": "10-06-2025 12:43:56",
      "ORDER_NUMBER": "21612506101398",
      "ORDER_TYPE": "MARKET",
      "PAN_NO": "BYYPCXXXXX",
      "PARTICIPANT_TYPE": "B",
      "PRICE": 6.99,
      "PRODUCT": "CNC",
      "QUANTITY": 1,
      "R": 2,
      "REMARKS1": "NA",
      "REMARKS2": "NA",
      "SEC_ID": "14366",
      "SEGMENT": "E",
      "SETTLOR": "90144",
      "SOURCE_FLG": "WEB",
      "STRIKE_PRICE": 0,
      "SYMBOL": "IDEA",
      "TRADE_NUMBER": "205988815",
      "TRADE_VALUE": 6.99
    }
  ]
0488",
"filltime": "12:39:05"
}
]
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

### Trade History

While an orders is sent as single entry but, it may get executed in arbitrary chunks at the exchange level. This endpoint returns a list of all trades generated upon the execution of orders for that day.

**Request Headers -**

- **X-Mirae-Version:** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization:** A token-based authentication header. The format is token jwtToken.
- **X-PrivateKey:** api_key

**cURL**

```bash
curl --location --request GET 'https://api.mstock.trade/openapi/typeb/trades' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwtToken' \
--header 'X-PrivateKey: api_key' \
--header 'Content-Type: application/json' \
--data '{
    "fromdate": "2024-01-06",
    "todate" : "2025-01-07"
}'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/trades', {
headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
},
// data: '{\n    "fromdate": "2024-01-06",\n    "todate" : "2025-01-07"\n}',
data: {
    'fromdate': '2024-01-06',
    'todate': '2025-01-07'
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
    'fromdate': '2024-01-06',
    'todate': '2025-01-07',
}
conn.request(
    'GET',
    'openapi/typeb/trades',
    json.dumps(json_data),
    # '{\n    "fromdate": "2024-01-06",\n    "todate" : "2025-01-07"\n}',
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/trades"))
    .method("GET", BodyPublishers.ofString("{\n    \"fromdate\": \"2024-01-06\",\n    \"todate\" : \"2025-01-07\"\n}"))
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
| fromdate | string | 2024-01-06 |
| todate | string | 2025-01-07 |

**Request Response -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful order update, the server returns a JSON object containing the order ID and status.

```json
{
    "status": "true",
    "message": "SUCCESS",
    "errorcode": "",
    "data": [
        {
            "exchange": "NSE",
            "producttype": "DELIVERY",
            "tradingsymbol": "RASHTRIYA CHEMICALS & FER",
            "instrumenttype": "",
            "symbolgroup": "",
            "strikeprice": "",
            "optiontype": "",
            "expirydate": "",
            "marketlot": "",
            "precision": "",
            "multiplier": "",
            "tradevalue": "",
            "transactiontype": "SELL",
            "fillprice": "145.45",
            "fillsize": "1",
            "orderid": "1300000040250500",
            "fillid": "68346395",
            "filltime": "14:48:23"
        },
        {
            "exchange": "NSE",
            "producttype": "DELIVERY",
            "tradingsymbol": "RASHTRIYA CHEMICALS & FER",
            "instrumenttype": "",
            "symbolgroup": "",
            "strikeprice": "",
            "optiontype": "",
            "expirydate": "",
            "marketlot": "",
            "precision": "",
            "multiplier": "",
            "tradevalue": "",
            "transactiontype": "BUY",
            "fillprice": "145.60",
            "fillsize": "1",
            "orderid": "1300000040194885",
            "fillid": "68334426",
            "filltime": "14:47:53"
        }
    ]
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

### Individual Order Details

This endpoint allows users to retrieve the status of individual order using the order id.

**Request Headers -**

- **X-Mirae-Version:** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization:** A token-based authentication header. The format is token jwtToken.
- **X-PrivateKey:** api_key

**cURL**

```bash
curl --location --request GET 'https://api.mstock.trade/openapi/typeb/order/details' \
--header 'X-Mirae-Version: 1' \
--header 'Authorization: Bearer jwtToken' \
--header 'X-PrivateKey: api_key' \
--header 'Content-Type: application/json' \
--data '{
    "order_no": "1181250130105",
    "segment": "E"
}'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/order/details', {
headers: {
    'X-Mirae-Version': '1',
    'Authorization': 'Bearer jwtToken',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
},
// data: '{\n    "order_no": "1181250130105",\n    "segment": "E"\n}',
data: {
    'order_no': '1181250130105',
    'segment': 'E'
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
    'order_no': '1181250130105',
    'segment': 'E',
}
conn.request(
    'GET',
    'openapi/typeb/order/details',
    json.dumps(json_data),
    # '{\n    "order_no": "1181250130105",\n    "segment": "E"\n}',
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/order/details"))
    .method("GET", BodyPublishers.ofString("{\n    \"order_no\": \"1181250130105\",\n    \"segment\": \"E\"\n}"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -** This endpoint does not require a request body or additional parameters in the query string for the retrieval of orders.

| Field | Type | Description |
| --- | --- | --- |
| order_id | string | The unique identifier of the order for which details need to be retrieved. |
| segment | string | E (Equity) / D (Derivative) -- Optional |

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful order deletion, the server returns a JSON object containing the order ID and status.

```json
{
    "status": "true",
    "message": "SUCCESS",
    "errorcode": "",
    "data": [
        {
            "variety": null,
            "ordertype": "MARKET",
            "producttype": "DELIVERY",
            "duration": "DAY",
            "price": 0,
            "triggerprice": 0,
            "quantity": "20",
            "disclosedquantity": "0",
            "squareoff": 0,
            "stoploss": 0,
            "trailingstoploss": 0,
            "tradingsymbol": "ACC",
            "transactiontype": "SELL",
            "exchange": "NSE",
            "symboltoken": "22",
            "instrumenttype": "EQUITY",
            "strikeprice": 0,
            "optiontype": "",
            "expirydate": "2025-Jan-23",
            "lotsize": "",
            "cancelsize": "0",
            "averageprice": "0",
            "filledshares": "20",
            "unfilledshares": "0",
            "orderid": "1000000000016254",
            "text": "CONFIRMED",
            "status": "Pending",
            "orderstatus": "Pending",
            "updatetime": "23-01-2025 03:14:25 PM",
            "exchtime": "",
            "exchorderupdatetime": "",
            "fillid": "",
            "filltime": "",
            "parentorderid": "",
            "ordertag": "",
            "uniqueorderid": ""
        }
    ]
}
```

- Failure (HTTP Status 200): If authentication fails, the server will return an error message

```json
{
    "status": "error",
    "message": "Please provide valid api version.",
    "error_type": "VersionException",
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
