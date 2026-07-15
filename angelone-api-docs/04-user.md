<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: User -->

# User

## Login Flow

The login flow starts by navigating to the public SmartAPI login endpoint:

```
https://smartapi.angelone.in/publisher-login?api_key=xxx&redirect_url=yyy&state=statevariable
```

After successful login, user gets redirected to the URL specified under MyApps. With the URL we pass auth_token & feed_token as query parameters.

| Request Type | APIs | Endpoint | Description |
| --- | --- | --- | --- |
| POST | Authenticate with Angel | https://apiconnect.angelone.in/rest/auth/angelbroking/user/v1/loginByPassword | Authenticate with Angel Login Credential |
| POST | Generate Token | https://apiconnect.angelone.in/rest/auth/angelbroking/jwt/v1/generateTokens | Generate jwt token on expire |
| GET | Get Profile | https://apiconnect.angelone.in/rest/secure/angelbroking/user/v1/getProfile | Retrieve the user profile |

## Authentication with Angel (Login Services)

You can authenticate to get APIs trading access using AngelOne Ltd. Account Id. In order to login, you need a client code, valid pin and TOTP. The session established via SmartAPI remains active till 12 midnight, unless the user chooses to log out.

### Login Request

```json
{
"clientcode":"Your_client_code",
"password":"Your_pin",
"totp":"enter_the_code_displayed_on_your_authenticator_app",
"state":"state_or_environment_variable"
}
```

Note: State variable is an optional parameter that is used in specific use cases. It is either passed in the request body of the login API as a key value pair or as a query parameter in the publisher login URL. It accepts a string and returns the same string in response.

### Login Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":{
"jwtToken":"eyJhbGciOiJIUzUxMiJ9.eyJzdWI...",
"refreshToken":"eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1OTk0ODkwMz...",
"feedToken":"eyJhbGciOiJIUzUxMiJ9.eyJ1c2Vy…"
"state":"live"
  }
}
```

#### Note:- As a best practice we suggest the user to logout everyday after their activity.

**Python**

```python
import http.client
import mimetypes
conn = http.client.HTTPSConnection(
    "apiconnect.angelone.in"
    )
payload = "{\n\"clientcode\":\"CLIENT_ID\"
            ,\n\"password\":\"CLIENT_PIN\"\n
		,\n\"totp\":\"TOTP_CODE\"\n
    ,\n\"state\":\"STATE_VARIABLE\"\n}"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  }
conn.request(
    "POST",
    "/rest/auth/angelbroking/user/
    v1/loginByPassword",
     payload,
     headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({
    "clientcode":"CLIENT_ID",
    "password":"CLIENT_PIN",
	"totp":"TOTP_CODE",
  "state":"STATE_VARIABLE"
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
    /rest/auth/angelbroking/user/
  v1/loginByPassword',

  headers : {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  }
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType,
     "{\n
        \"clientcode\":\"CLIENT_ID\",\n
        \"password\":\"CLIENT_PIN\",\n
		\"totp\":\"TOTP_CODE\",\n
    \"state\":\"STATE_VARIABLE\"\n
    }"
     );
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/auth/angelbroking/user/
  v1/loginByPassword")

  .method("POST", body)
  .addHeader("Content-Type", "application/json")
  .addHeader("Accept", "application/json")
  .addHeader("X-UserType", "USER")
  .addHeader("X-SourceID", "WEB")
  .addHeader("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  .addHeader("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  .addHeader("X-MACAddress", "MAC_ADDRESS")
  .addHeader("X-PrivateKey", "API_KEY")
  .build();
Response response = client.newCall(request).execute();
```

**R**

```r
library(httr)

url <- "https://apiconnect.angelone.in/
rest/auth/angelbroking/user/
v1/loginByPassword"

json_body <- jsonlite::toJSON(list(
    "clientcode":"CLIENT_ID",
    "password":"CLIENT_PIN",
	"totp":"TOTP_CODE",
  "state":"STATE_VARIABLE"
    ))

response <- POST(url,
    config = list(
    add_headers(
    'Content-Type'= 'application/json',
    'Accept'= 'application/json',
    'X-UserType'= 'USER',
    'X-SourceID'= 'WEB',
    'X-ClientLocalIP'= 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP'= 'CLIENT_PUBLIC_IP',
    'X-MACAddress'= 'MAC_ADDRESS',
    'X-PrivateKey'= 'API_KEY'
    ))
    ),
    body = json_body,
    encode = "raw"

print(response)
```

**GO**

```go
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://apiconnect.angelone.in/
  rest/auth/angelbroking/user/v1/loginByPassword"
  method := "POST"

  payload := strings.NewReader({
    "clientcode": "Your_client_code",
    "password": "Your_Pin",
	"totp":"TOTP_CODE",
  "state":"STATE_VARIABLE"
})

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Accept", "application/json")
  req.Header.Add("X-UserType", "USER")
  req.Header.Add("X-SourceID", "WEB")
  req.Header.Add("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  req.Header.Add("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  req.Header.Add("X-MACAddress", "MAC_ADDRESS")
  req.Header.Add("X-PrivateKey", "API_KEY")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := ioutil.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

## Generate Token

Generate token helps to obtain the token after the login flow. After successful login, you get a JWT token and a Refresh token. You can use JWT token to make any transaction.

#### Generate Token Request

```json
{
"refreshToken":"eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1OTk0OD..."
}
```

#### Generate Token Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":{
"jwtToken":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIi...",
"refreshToken":"eyJhbGciOiJIUzUxMiJ9.e...",
"feedToken":"eyJhbGciOiJIUzUxMiJ9.eyJ1c2Vy…"
  }
}
```

**Python**

```python
import http.client
import mimetypes
conn = http.client.HTTPSConnection(
    "apiconnect.angelone.in"
    )
payload = "{\n
    \"refreshToken\":\"REFRESH_TOKEN\"
    \n}"
headers = {
    'Authorization': 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  }
conn.request("POST",
 "/rest/auth/angelbroking/jwt/
 v1/generateTokens",
  payload,
  headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({
    "refreshToken":"REFRESH_TOKEN"
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/auth/angelbroking/jwt/
  v1/generateTokens',

  headers: {
    'Authorization': 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  }
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType,
     "{\n\"refreshToken\":\"REFRESH_TOKEN\"\n}"
     );

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/auth/angelbroking/jwt/
  v1/generateTokens")

  .method("POST", body)
  .addHeader("Authorization", "Bearer AUTHORIZATION_TOKEN")
  .addHeader("Content-Type", "application/json")
  .addHeader("Accept", "application/json")
  .addHeader("X-UserType", "USER")
  .addHeader("X-SourceID", "WEB")
  .addHeader("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  .addHeader("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  .addHeader("X-MACAddress", "MAC_ADDRESS")
  .addHeader("X-PrivateKey", "API_KEY")
  .build();
Response response = client.newCall(request).execute();
```

**R**

```r
library(httr)

url <- "https://apiconnect.angelone.in/
rest/auth/angelbroking/jwt/
v1/generateTokens"

json_body <- jsonlite::toJSON(list(
    "refreshToken":"REFRESH_TOKEN"
    ))

response <- POST(url,
    config = list(
    add_headers(
    'Authorization'= 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type'= 'application/json',
    'Accept'= 'application/json',
    'X-UserType'= 'USER',
    'X-SourceID'= 'WEB',
    'X-ClientLocalIP'= 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP'= 'CLIENT_PUBLIC_IP',
    'X-MACAddress'= 'MAC_ADDRESS',
    'X-PrivateKey'= 'API_KEY'
    ))
    ),
    body = json_body,
    encode = "raw"

print(response)
```

**GO**

```go
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://apiconnect.angelone.in/
  rest/auth/angelbroking/jwt/v1/generateTokens"
  method := "POST"

  payload := strings.NewReader({
    "refreshToken": "eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1OTk0OD..."
})

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer AUTHORIZATION_TOKEN")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Accept", "application/json")
  req.Header.Add("X-UserType", "USER")
  req.Header.Add("X-SourceID", "WEB")
  req.Header.Add("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  req.Header.Add("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  req.Header.Add("X-MACAddress", "MAC_ADDRESS")
  req.Header.Add("X-PrivateKey", "API_KEY")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := ioutil.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

## Get Profile

This allows to fetch the complete information of the user who is logged in.

#### Get Profile Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":{
"clientcode":"YOUR_CLIENT_CODE",
"name":"YOUR_NAME",
"email":"",
"mobileno":"",
"exchanges":"[ "NSE", "BSE", "MCX", "CDS", "NCDEX", "NFO" ]",
"products":"[ "DELIVERY", "INTRADAY", "MARGIN"]",
"lastlogintime":"",
"brokerid":"B2C",
  }
}
```

**Python**

```python
import http.client
import mimetypes
conn = http.client.HTTPSConnection(
    " apiconnect.angelone.in "
    )
payload = ''
headers = headers = {
    'Authorization': 'Bearer AUTHORIZATION_TOKEN',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  }
conn.request("GET",
 "/rest/secure/angelbroking/user/
 v1/getProfile",
 payload,
 headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');

var config = {
  method: 'get',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/user/
  v1/getProfile',

  headers : {
    'Authorization': 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/user/
  v1/getProfile")

  .method("GET", null)
  .addHeader("Authorization", "Bearer AUTHORIZATION_TOKEN")
  .addHeader("Accept", "application/json")
  .addHeader("X-UserType", "USER")
  .addHeader("X-SourceID", "WEB")
  .addHeader("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  .addHeader("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  .addHeader("X-MACAddress", "MAC_ADDRESS")
  .addHeader("X-PrivateKey", "API_KEY")
  .build();
Response response = client.newCall(request).execute();
```

**R**

```r
library(httr)

url <- "https://apiconnect.angelone.in/
rest/secure/angelbroking/user/
v1/getProfile"

response <- GET(url, add_headers(
    'Authorization'= 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type'= 'application/json',
    'Accept'= 'application/json',
    'X-UserType'= 'USER',
    'X-SourceID'= 'WEB',
    'X-ClientLocalIP'= 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP'= 'CLIENT_PUBLIC_IP',
    'X-MACAddress'= 'MAC_ADDRESS',
    'X-PrivateKey'= 'API_KEY'
    ))

print(response)
```

**GO**

```go
package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://apiconnect.angelone.in/
  rest/secure/angelbroking/user/v1/getProfile"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer AUTHORIZATION_TOKEN")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Accept", "application/json")
  req.Header.Add("X-UserType", "USER")
  req.Header.Add("X-SourceID", "WEB")
  req.Header.Add("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  req.Header.Add("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  req.Header.Add("X-MACAddress", "MAC_ADDRESS")
  req.Header.Add("X-PrivateKey", "API_KEY")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := ioutil.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

## Funds and Margins

The GET Request to RMS returns fund, cash and margin information of the user for equity and commodity segments.

| Request Type | APIs | Endpoint | Description |
| --- | --- | --- | --- |
| GET | Get RMS Limit | https://apiconnect.angelone.in/rest/secure/angelbroking/user/v1/getRMS | To retrieve RMS limit |

### RMS (Risk Management System)

The RMS Limit defines margin rules to ensure that traders don't default on payments & delivery of their orders.

#### Get RMS Limit Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":{
"net":"9999999999999",
"availablecash":"9999999999999",
"availableintradaypayin":"0",
"availablelimitmargin":"0",
"collateral":"0",
"m2munrealized":"0",
"m2mrealized":"0",
"utiliseddebits":"0",
"utilisedspan":"0",
"utilisedoptionpremium":"0",
"utilisedholdingsales":"0",
"utilisedexposure":"0",
"utilisedturnover":"0",
"utilisedpayout":"0",
 }
}
```

**Python**

```python
import http.client
import mimetypes
conn = http.client.HTTPSConnection(
    " apiconnect.angelone.in "
    )
payload = ''
headers = {
    'Authorization': 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  }
conn.request("GET",
"/rest/secure/angelbroking/user/
v1/getRMS",
payload,
headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');

var config = {
  method: 'get',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/user/
  v1/getRMS',

  headers : {
    'Authorization': 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/user/v1/getRMS")
  .method("GET", null)
  .addHeader("Authorization", "Bearer AUTHORIZATION_TOKEN")
  .addHeader("Accept", "application/json")
  .addHeader("X-UserType", "USER")
  .addHeader("X-SourceID", "WEB")
  .addHeader("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  .addHeader("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  .addHeader("X-MACAddress", "MAC_ADDRESS")
  .addHeader("X-PrivateKey", "API_KEY")
  .build();
Response response = client.newCall(request).execute();
```

**R**

```r
library(httr)

url <- "https://apiconnect.angelone.in/
rest/secure/angelbroking/user/
v1/getRMS"
response <- GET(url, add_headers(
    'Authorization'= 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type'= 'application/json',
    'Accept'= 'application/json',
    'X-UserType'= 'USER',
    'X-SourceID'= 'WEB',
    'X-ClientLocalIP'= 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP'= 'CLIENT_PUBLIC_IP',
    'X-MACAddress'= 'MAC_ADDRESS',
    'X-PrivateKey'= 'API_KEY'
    ))

print(response)
```

**GO**

```go
package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://apiconnect.angelone.in/
  rest/secure/angelbroking/user/v1/getRMS"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer AUTHORIZATION_TOKEN")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Accept", "application/json")
  req.Header.Add("X-UserType", "USER")
  req.Header.Add("X-SourceID", "WEB")
  req.Header.Add("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  req.Header.Add("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  req.Header.Add("X-MACAddress", "MAC_ADDRESS")
  req.Header.Add("X-PrivateKey", "API_KEY")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := ioutil.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```

## Logout

The API session is destroyed by this call and it invalidates the access_token. The user will be sent through a new login flow after this. User is not logged out of the official SmartAPI web.

| Request Type | APIs | Endpoint | Description |
| --- | --- | --- | --- |
| POST | Logout | https://apiconnect.angelone.in/rest/secure/angelbroking/user/v1/logout | To logout |

#### Logout Request

```json
{
"clientcode":"CLIENT_CODE",
}
```

#### Logout Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":"",
}
```

**Python**

```python
import http.client
import mimetypes
conn = http.client.HTTPSConnection(
    " apiconnect.angelone.in "
    )
payload = "{\n
    \"clientcode\": \"CLIENT_CODE\"\n
}"
headers = {
    'Authorization': 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  }
conn.request("POST",
"/rest/secure/angelbroking/user/v1/logout",
payload,
headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({
    "clientcode":"CLIENT_CODE"
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/user/
  v1/logout',
  headers : {
    'Authorization': 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserType': 'USER',
    'X-SourceID': 'WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-PrivateKey': 'API_KEY'
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType,
     "{\n     \"clientcode\": \"CLIENT_CODE\"\n}"
     );

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/user/
  v1/logout")
  .method("POST", body)
  .addHeader("Authorization", "Bearer AUTHORIZATION_TOKEN")
  .addHeader("Content-Type", "application/json")
  .addHeader("Accept", "application/json")
  .addHeader("X-UserType", "USER")
  .addHeader("X-SourceID", "WEB")
  .addHeader("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  .addHeader("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  .addHeader("X-MACAddress", "MAC_ADDRESS")
  .addHeader("X-PrivateKey", "API_KEY")
  .build();
Response response = client.newCall(request).execute();
```

**R**

```r
library(httr)

url <- "https://apiconnect.angelone.in/
rest/secure/angelbroking/user/
v1/logout"

json_body <- jsonlite::toJSON(list(
    "clientcode":"CLIENT_CODE"
    ))

response <- POST(url,
    config = list(
    add_headers(
    'Authorization'= 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type'= 'application/json',
    'Accept'= 'application/json',
    'X-UserType'= 'USER',
    'X-SourceID'= 'WEB',
    'X-ClientLocalIP'= 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP'= 'CLIENT_PUBLIC_IP',
    'X-MACAddress'= 'MAC_ADDRESS',
    'X-PrivateKey'= 'API_KEY'
    ))
    ),
    body = json_body,
    encode = "raw"

print(response)
```

**GO**

```go
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://apiconnect.angelone.in/
  rest/secure/angelbroking/user/v1/logout"
  method := "POST"

  payload := strings.NewReader({
    "clientcode": "CLIENT_CODE"
})

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Authorization", "Bearer AUTHORIZATION_TOKEN")
  req.Header.Add("Content-Type", "application/json")
  req.Header.Add("Accept", "application/json")
  req.Header.Add("X-UserType", "USER")
  req.Header.Add("X-SourceID", "WEB")
  req.Header.Add("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  req.Header.Add("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  req.Header.Add("X-MACAddress", "MAC_ADDRESS")
  req.Header.Add("X-PrivateKey", "API_KEY")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := ioutil.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```
