# User Details and Authentication

> Source: https://tradingapi.mstock.com/docs/v1/typeB/User/
>
> Section: Type B

### Login flow

**Step 1:** Generate API Key,

Go to [trade.mstock.com](https://trade.mstock.com) to generate the Api Key. Click [here](https://www.mstock.com/trading-api) if you have not yet generated. This Api-key has to be passed in all the API call as headers mentioned here.

> **Note**
>
> mStock account is manadatory to genreate the API key. If you still do not have mstock account, [Open Account](https://www.mstock.com/open-demat-account).

**Step 2:** Using the Api key, you can now login using the user name & password with connect/login api. This will generate the OTP.

**Step 3:** You can use the OTP to generate the access Token, & use that with all the subsequent api calls.

![Image title](https://tradingapi.mstock.com/docs/img/OpenAPItypeBuser.svg)

> **Warning**
>
> Avoid api_key exposure. It's unsafe to embed it in mobile apps or client code! Never let access_token be public.

---

### User APIs

| method | path | description |
| --- | --- | --- |
| POST | https://api.mstock.trade/openapi/typeb/connect/login | This endpoint allows users to log in to the application |
| POST | https://api.mstock.trade/openapi/typeb/session/token | This endpoint is used to retrieve a session token based on the provided API key, request token, and checksum. |
| POST | https://api.mstock.trade/openapi/typeb/openapi/typeb/session/verifytotp | This endpoint is used to verify the TOTP for multi-factor authentication during the login process. |
| GET | https://api.mstock.trade/openapi/typeb/user/fundsummary | This endpoint used get the funds, cash and margin information for the user. |
| GET | https://api.mstock.trade/openapi/typeb/logout | This API call wil invalidate the access token and current API session. |

---

### Login

This endpoint allows users to log in to the application by providing their username and password. Successful authentication will send the OTP to users registered mobile no that can be used for subsequent requests.

**Request Headers -**

- **X-Mirae-Version:** Specifies the version of the API being used. In this case, it is set to 1.
- **Content-Type:** For this request, it is set to application/x-www-form-urlencoded, which is used for submiting form data through body.

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/connect/login' \
    --header 'X-Mirae-Version: 1' \
    --header 'Content-Type: application/json' \
    --data-raw '{
    "clientcode": "XXXXX",
    "password": "YYYYY",
    "totp": "",
    "state": ""
    }'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.post(
'https://api.mstock.trade/openapi/typeb/connect/login',
// '{\n    "clientcode": "XXXXX",\n    "password": "YYYYY",\n    "totp": "",\n    "state": ""\n    }',
{
    'clientcode': 'XXXXX',
    'password': 'YYYYY',
    'totp': '',
    'state': ''
},
{
    headers: {
    'X-Mirae-Version': '1',
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
    'Content-Type': 'application/json',
}
json_data = {
    'clientcode': 'XXXXX',
    'password': 'YYYYY',
    'totp': '',
    'state': '',
}
conn.request(
    'POST',
    '/openapi/typeb/connect/login',
    json.dumps(json_data),
    # '{\n    "clientcode": "XXXXX",\n    "password": "YYYYY",\n    "totp": "",\n    "state": ""\n    }',
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/connect/login"))
    .POST(BodyPublishers.ofString("{\n    \"clientcode\": \"XXXXX\",\n    \"password\": \"YYYYY\",\n    \"totp\": \"\",\n    \"state\": \"\"\n    }"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -**

The body of the request must be URL-encoded and include the following parameters:

| Field | Type | Description |
| --- | --- | --- |
| clientcode | string | The username of the user attempting to log in. (Example: XXXXX) |
| password | string | The password associated with the username. (Example: XYZ@123) |
| totp | string | Empty string |
| state | string | Empty string |

**Note -**

Generated JWT token will be valid till 12:00 AM of generated day.

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful login, the server returns a JSON object containing the authentication token and any relevant user information.

```json
{
    "status": "true",
    "message": "Please enter the OTP that we sent on XXXXXXX452 and XXXX00@GMAIL.COM",
    "errorcode": "",
    "data": {
        "jwtToken": "697c39bf-9411-46b0-81c2-67448ee99c72",
        "refreshToken": "",
        "feedToken": "",
        "state": "live"
    }
}
```

-

Failure (HTTP Status 400):

If the version is incorrect, the server will return an error message.

```json
{
    "status": "false",
    "message": "Please provide valid clientcode and password.",
    "errorcode": "400",
    "data": null
}
```

- Failure (HTTP Status 200): If the login credentials are incorrect, the server will return an error message.

```json
{
    "status": "false",
    "message": "Invalid username or password. 9 attempts remaining ",
    "errorcode": "MA500",
    "data": null
}
```

---

### Generate Session with OTP

This endpoint is used to retrieve a session token based on the provided refreshToken and otp. The session token is essential for authenticating subsequent API requests.

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Content-Type :** For this request, it is set to application/json, which is used for submiting form through data.
- **X-PrivateKey :** api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/session/token' \
    --header 'X-Mirae-Version: 1' \
    --header 'X-PrivateKey: api_key' \
    --header 'Content-Type: application/json' \
    --data '{
        "refreshToken": "refreshToken",
        "otp":"XXXXXX"
    }'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.post(
'https://api.mstock.trade/openapi/typeb/session/token',
// '{\n        "refreshToken": "refreshToken",\n        "otp":"XXXXXX"\n    }',
{
    'refreshToken': 'refreshToken',
    'otp': '123'
},
{
    headers: {
    'X-Mirae-Version': '1',
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
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json',
}
json_data = {
    'refreshToken': 'refreshToken',
    'otp': 'XXXXXX',
}
conn.request(
    'POST',
    'openapi/typeb/session/token',
    json.dumps(json_data),
    # '{\n        "refreshToken": "refreshToken",\n        "otp":"XXXXXX"\n    }',
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/session/token"))
    .POST(BodyPublishers.ofString("{\n        \"refreshToken\": \"refreshToken\",\n        \"otp\":\"XXXXXX\"\n    }"))
    .setHeader("X-Mirae-Version", "1")
    .setHeader("X-PrivateKey", "api_key")
    .setHeader("Content-Type", "application/json")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -**

The body of the request must be URL-encoded and include the following parameters:

| Field | Type | Description |
| --- | --- | --- |
| refreshToken | string | A refreshToken is provided in the response from the login API. |
| otp | string | Please enter the OTP sent to your mobile number or email |

n.Tasc Fields mapping with mStock API Parameters –

| Field | Type | Description |
| --- | --- | --- |
| refreshToken | string | A refreshToken is provided in the response from the login API. |
| request_token | string | OTP (XXXXXX); |

**Response Structure -**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful login, the server returns a JSON object containing the authentication token and any relevant user details.

> **Note**
>
> In below response access_token, enctoken and refresh_token are pasted half because its size is very large.

```json
{
    "status": "true",
    "message": "Please enter the OTP that we sent on XXXXXXX928 and XXXXEY@XXXXXCM.COM",
    "errorcode": "",
    "data": {
        "jwtToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVU0VSTkFNRSI6IlJBSFVMIiwiQVBJVFlQRSI6IkFHTCIsIm5iZiI6MTczNTYyNDQxNSwiZXhwIjoxNzM1NjI0NzE1LCJpYXQiOjE3MzU2MjQ0MTV9.MQGh5S801_tccVXx0k-Njj_yqkcXBaN5T0mZnUjLlHI",
        "refreshToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVU0VSTkFNRSI6IlJBSFVMIiwiQVBJVFlQRSI6IkFHTCIsIm5iZiI6MTczNTYyNDQxNSwiZXhwIjoxNzM1NjI0NzE1LCJpYXQiOjE3MzU2MjQ0MTV9.MQGh5S801_tccVXx0k-Njj_yqkcXBaN5T0mZnUjLlHI",
        "feedToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVU0VSTkFNRSI6IlJBSFVMIiwiQVBJVFlQRSI6IkFHTCIsIm5iZiI6MTczNTYyNDQxNSwiZXhwIjoxNzM1NjI0NzE1LCJpYXQiOjE3MzU2MjQ0MTV9.MQGh5S801_tccVXx0k-Njj_yqkcXBaN5T0mZnUjLlHI",
        "state": "live"
    }
}
```

- Failure (HTTP Status 200): If the request fails due to an invalid OTP passed, the server will return an error message.

```json
{
    "status": "false",
    "message": "Entered OTP has been expired. Please regenerate a new one & enter the same.",
    "errorcode": "MA500",
    "data": null
}
```

- Failure (HTTP Status 403): If the API Key is Invalid or expired.

```json
{
    "status": "error",
    "message": "API is suspended/expired for use. Please check your API subscription and try again.",
    "data": null
}
```

---

### Process to Enable TOTP on mStock

**Step 1: Login** - Go to [trade.mstock.com](https://trade.mstock.com) - Enter your credentials to log in to your account

**Step 2: Open Menu** - Click on the hamburger menu icon located at the top-left corner of the screen

**Step 3: Navigate to Trading APIs** - In the menu, go to **Products** - Then click on **Trading APIs**

**Step 4: Enable TOTP** - You will see an option labeled "Enable TOTP" - Click on it to begin the TOTP setup process

> **Note**
>
> If TOTP is enabled, OTP will not be triggered for login trading API requests.

---

### Generate Session with TOTP (Verify TOTP)

This endpoint is used to retrieve a session token and verify TOTP based on the provided `refreshToken` and `totp`. The session token is essential for authenticating subsequent API requests.

**Request Headers -**

- X-Mirae-Version : Specifies the version of the API being used. In this case, it is set to 1.
- Content-Type : For this request, it is set to application/json , which is used for submitting JSON data.
- X-PrivateKey : Your API key.

**cURL Command -**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/session/verifytotp' \
--header 'X-Mirae-Version: 1' \
--header 'X-PrivateKey: api_key'\ 
--header 'Content-Type: application/json' \ 
--data '{
    "refreshToken": "ENTER_REFRESH_TOKEN_HERE",
    "totp": "XXXXXX"
}'
```

**Node.js**

```
import axios from 'axios';

const response = await axios.post(
  'https://api.mstock.trade/openapi/typeb/session/verifytotp',
  {
    refreshToken: 'ENTER_REFRESH_TOKEN_HERE',
    totp: 'XXXXXX'
  },
  {
    headers: {
      'X-Mirae-Version': '1',
      'X-PrivateKey': 'api_key',
      'Content-Type': 'application/json'
    }
  }
);
```

**Python**

```
import requests

headers = {
    'X-Mirae-Version': '1',
    'X-PrivateKey': 'api_key',
    'Content-Type': 'application/json'
}

data = {
    'refreshToken': 'ENTER_REFRESH_TOKEN_HERE',
    'totp': 'XXXXXX'
}

response = requests.post('https://api.mstock.trade/openapi/typeb/session/verifytotp', json=data, headers=headers)
```

**Java**

```
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

HttpClient client = HttpClient.newHttpClient();
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/session/verifytotp"))
    .header("X-Mirae-Version", "1")
    .header("X-PrivateKey", "api_key")
    .header("Content-Type", "application/json")
    .POST(HttpRequest.BodyPublishers.ofString("{"refreshToken":"ENTER REFRESH TOKEN HERE","totp":"XXXXXX"}"))
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -**

| Field | Type | Description |
| --- | --- | --- |
| refreshToken | string | The refreshToken is received in the response of the login API and it used to generate a new session |
| totp | string | The TOTP generated by the authenticator app |

**Response Structure -**

- **Success (HTTP 200):**
```json
{
    "status": true,
    "message": "SUCCESS",
    "errorcode": "",
    "data": {
        "ClientName": "XXXXXXXXX",
        "ClientId": "YYYYYYYY",
        "exchanges": [
            "XXXXX..."
        ],
        "jwtToken": "<<jwtToken.....>>",
        "refreshToken": "<<Refresh_token....>>",
        "feedToken": "<<feedToken...>>"
    }
}
```
- **Failure (HTTP 400):**
```json
{
    "status": "error",
    "message": "Please enter correct TOTP",
    "error_type": "MA400",
    "data": null
}
```
- **Failure (HTTP 403):**
```json
{
  "status": "error",
  "message": "API is suspended/expired for use. Please check your API subscription and try again.",
  "data": null
}
```

---

### Fund Summary

This endpoint used get the funds, cash and margin information for the user.

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization :** A token-based authentication header. The format is token api_key:access_token.
- **X-PrivateKey :** api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/user/fundsummary' \
    --header 'X-Mirae-Version: 1' \
    --header 'Authorization: Bearer jwtToken' \
    --header 'X-PrivateKey: api_key'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.put(
'https://api.mstock.trade/openapi/typeb/user/fundsummary',
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
conn.request('PUT', 'openapi/typeb/user/fundsummary', headers=headers)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/user/fundsummary"))
    .PUT(HttpRequest.BodyPublishers.noBody())
    .setHeader("X-Mirae-Version", "1")
    .setHeader("Authorization", "Bearer jwtToken")
    .setHeader("X-PrivateKey", "api_key")
    .build();

HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
```

**Request Body -**

This endpoint does not require a request body or additional parameters in the query string for the retrieval of orders

**Response Structure-**

The response of the request will be based on authentication outcome.

- Success (HTTP Status 200): On successful request, the server returns a JSON object containing the session token and any relevant user details

> **Note**
>
> In below response access_token, enctoken and refresh_token are pasted half because its size is very large.

```json
{
    "status": true,
    "message": "SUCCESS",
    "errorcode": "",
    "data": [
        {
            "ADDITIONAL_MARGIN": "0.0",
            "ADHOC_LIMIT": "99999999999",
            "AMOUNT_UTILIZED": "27395824.71",
            "AVAILABLE_BALANCE": "299972678840.29",
            "BANK_HOLDING": "99999999999",
            "CLEAR_BALANCE": "199999949998",
            "COLLATERALS": "74668",
            "LIMIT_SOD": "99999999999",
            "LIMIT_TYPE": "CAPITAL",
            "MF_COLLATERAL": "0.0",
            "MTF_AVAILABLE_BALANCE": "299972678840.29",
            "MTF_COLLATERAL": "0.0",
            "MTF_UTILIZE": "0.0",
            "MTM_COMBINED": "0",
            "OFS_UTILIZED": "0.0",
            "OPT_BUY_PRIMIUM_UTILIZE": "0.0",
            "PAY_OUT_AMT": "50000.0",
            "PEAK_MARGIN": "33222959.73",
            "PHYSICAL_MARGIN": "0.0",
            "REALISED_PROFITS": "0",
            "RECEIVABLES": "0",
            "SEG": "A",
            "SUM_OF_ALL": "300000024665",
            "UNCLEAR_BALANCE": "0"
        }
    ]
}
```

- Failure (HTTP Status 400): If the API Key is Invalid or expired.

```json
{
    "status": "error",
    "message": "API is suspended/expired for use. Please check your API subscription and try again.",
    "data": null
}
```

---

### Logout

This endpoint allows users to retrieve a list of their trading orders. Users can view all their existing orders.

**Request Headers -**

- **X-Mirae-Version :** Specifies the version of the API being used. In this case, it is set to 1.
- **Authorization :** A token-based authentication header. The format is Bearer jwtToken.
- **X-PrivateKey :** api_key

**cURL**

```bash
curl --location 'https://api.mstock.trade/openapi/typeb/logout' \
    --header 'X-Mirae-Version: 1' \
    --header 'X-PrivateKey: api_key' \
    --header 'Authorization: Bearer jwtToken'
```

**Node.js**

```javascript
import axios from 'axios';

const response = await axios.get('https://api.mstock.trade/openapi/typeb/logout', {
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
conn.request('GET', '/openapi/typeb/logout', headers=headers)
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
    .uri(URI.create("https://api.mstock.trade/openapi/typeb/logout"))
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

- Success (HTTP Status 200): On logout api call the api will return the below response.

```json
{
    "status": true,
    "message": "Success",
    "errorcode": null,
    "data": null
}
```

- Failure (HTTP Status 401): If authentication fails, the server will return an error message

```json
{
    "status": false,
    "message": "Invalid request. Please try again.",
    "errorcode": "IA401",
    "data": null
}
```

- Failure (HTTP Status 403): If the API Key is Invalid or expired.

```json
{
    "status": "false",
    "message": "API is suspended/expired for use. Please check your API subscription and try again.",
    "errorcode": "IA403",
    "data": null
}
```

---
