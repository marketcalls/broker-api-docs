<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: GTT -->

# GTT

The currently supported exchange types are NSE and BSE only and the product types supported are DELIVERY and MARGIN only for now

For users utilizing the new static IP–based API key, the source IP address of Create GTT, Cancel GTT, and Modify GTT requests will be validated against the static IP registered by the user. The API request will be processed successfully only if the source IP matches the registered static IP.

| Request Type | API's | Endpoint | Description |
| --- | --- | --- | --- |
| POST | Create Rule | https://apiconnect.angelone.in/rest/secure/angelbroking/gtt/v1/createRule | Create GTT Rule |
| POST | Modify Rule | https://apiconnect.angelone.in/rest/secure/angelbroking/gtt/v1/modifyRule | Modify GTT Rule |
| POST | Cancel Rule | https://apiconnect.angelone.in/rest/secure/angelbroking/gtt/v1/cancelRule | Cancel GTT Rule |
| POST | Rule Details | https://apiconnect.angelone.in/rest/secure/angelbroking/gtt/v1/ruleDetails | Get GTT Rule Details |
| POST | Rule List | https://apiconnect.angelone.in/rest/secure/angelbroking/gtt/v1/ruleList | Get GTT Rule List |

## GTT Error Codes

| Sr. No | Error Code | Description |
| --- | --- | --- |
| 1 | AB9000 | Internal Server Error |
| 2 | AB9001 | Invalid Parameters |
| 3 | AB9002 | Method Not Allowed |
| 4 | AB9003 | Invalid Client ID |
| 5 | AB9004 | Invalid Status Array Size |
| 6 | AB9005 | Invalid Session ID |
| 7 | AB9006 | Invalid Order Quantity |
| 8 | AB9007 | Invalid Disclosed Quantity |
| 9 | AB9008 | Invalid Price |
| 10 | AB9009 | Invalid Trigger Price |
| 11 | AB9010 | Invalid Exchange Segment |
| 12 | AB9011 | Invalid Symbol Token |
| 13 | AB9012 | Invalid Trading Symbol |
| 14 | AB9013 | Invalid Rule ID |
| 15 | AB9014 | Invalid Order Side |
| 16 | AB9015 | Invalid Product Type |
| 17 | AB9016 | Invalid Time Period |
| 18 | AB9017 | Invalid Page Value |
| 19 | AB9018 | Invalid Count Value |

## Create Rule

When a rule is successfully created, the API returns a rule id.

#### All requests and its response structure is as below.

#### Create Rule Request

```json
{
"tradingsymbol":"SBIN-EQ",
"symboltoken":"3045",
"exchange":"NSE",
"transactiontype":"BUY",
"producttype":"DELIVERY",
"price":"195",
"qty":"1",
"triggerprice":"196",
"disclosedqty":"10"
}
```

#### Create Rule Response

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": {
"id": "1"
}
}
```

**Python**

```python
 import http.client

conn = http.client.HTTPSConnection("apiconnect.angelone.in")
payload = "{\r\n    \"tradingsymbol\": \"SBIN-EQ\",\r\n
 \"symboltoken\": \"3045\",\r\n    \"exchange\": \"NSE\",\r\n
   \"transactiontype\": \"BUY\",\r\n    \"producttype\": \"DELIVERY\",\r\n
    \"price\": \"195\",\r\n    \"qty\": \"1\",\r\n
       \"triggerprice\": \"196\",\r\n    \"disclosedqty\": \"10\"\r\n
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
conn.request("POST", "/rest/secure/angelbroking/
gtt/v1/createRule", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({"tradingsymbol":"SBIN-EQ",
"symboltoken":"3045","exchange":"NSE","transactiontype":"BUY",
"producttype":"DELIVERY","price":"195","qty":"1",
"triggerprice":"196","disclosedqty":"10"});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/gtt/v1/createRule',
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
RequestBody body = RequestBody.create(mediaType, "{\r\n
      \"tradingsymbol\": \"SBIN-EQ\",\r\n
       \"symboltoken\": \"3045\",\r\n    \"exchange\": \"NSE\",\r\n
        \"transactiontype\": \"BUY\",\r\n    \"producttype\": \"DELIVERY\",\r\n
         \"price\": \"195\",\r\n    \"qty\": \"1\",\r\n
           \"triggerprice\": \"196\",\r\n    \"disclosedqty\": \"10\"\r\n
            }");
Request request = new Request.Builder()
.url("https://apiconnect.angelone.in/rest/secure/angelbroking/gtt/v1/createRule")
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
rest/secure/angelbroking/
gtt/v1/createRule"
json_body <- jsonlite::toJSON(list(
    "tradingsymbol":"SBIN-EQ",
    "symboltoken":"3045",
    "exchange":"NSE",
    "transactiontype":"BUY",
    "producttype":"DELIVERY",
    "price":"195",
    "qty":"1",
    "triggerprice":"196",
    "disclosedqty":"10"

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
  rest/secure/angelbroking/gtt/v1/createRule"
  method := "POST"

  payload := strings.NewReader({
    "tradingsymbol":"SBIN-EQ",
    "symboltoken":"3045",
    "exchange":"NSE",
    "transactiontype":"BUY",
    "producttype":"DELIVERY",
    "price":"195",
    "qty":"1",
    "triggerprice":"196",
    "disclosedqty":"10"

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

## Modify Rule

When a rule is successfully modified, the API returns a rule id.

#### All requests and its response structure is as below.

#### Modify Rule Request

```json
{
"id":"1",
"symboltoken":"3045",
"exchange":"NSE",
"price":"195",
"qty":"1",
"triggerprice":"196",
"disclosedqty":"10"
}
```

#### Modify Rule Response

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": {
"id": "1"
}
}
```

**Python**

```python
import http.client

conn = http.client.HTTPSConnection("apiconnect.angelone.in")
payload = "{\r\n    \"id\": \"1\",\r\n
   \"symboltoken\": \"3045\",\r\n    \"exchange\": \"NSE\",\r\n
    \"price\": \"195\",\r\n    \"qty\": \"1\",\r\n
     \"triggerprice\": \"196\",\r\n    \"disclosedqty\": \"10\",\r\n
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
conn.request("POST", "/rest/secure/angelbroking/gtt/v1/modifyRule", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({"id":"1","symboltoken":"3045",
"exchange":"NSE","price":"195","qty":"1",
"triggerprice":"196","disclosedqty":"10"});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/gtt/v1/modifyRule',
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
  },
  data : data
};
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\r\n    \"id\": \"1\",\r\n
   \"symboltoken\": \"3045\",\r\n    \"exchange\": \"NSE\",\r\n    \"price\": \"195\",\r\n
      \"qty\": \"1\",\r\n    \"triggerprice\": \"196\",\r\n
       \"disclosedqty\": \"10\",\r\n }");
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/rest/secure/angelbroking/gtt/v1/modifyRule")
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
rest/secure/angelbroking/gtt/
v1/modifyRule"
json_body <- jsonlite::toJSON(list(
    "id": "1",
    "symboltoken":"3045",
    "exchange":"NSE",
    "price":"195",
    "qty":"1",
    "triggerprice":"196",
    "disclosedqty":"10"
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
  rest/secure/angelbroking/gtt/v1/modifyRule"
  method := "POST"

  payload := strings.NewReader({
    "id": "1",
    "symboltoken":"3045",
    "exchange":"NSE",
    "price":"195",
    "qty":"1",
    "triggerprice":"196",
    "disclosedqty":"10"

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

## Cancel Rule

When a rule is successfully cancelled, the API returns a rule id.

#### All requests and its response structure is as below.

#### Cancel Rule Request

```json
{
"id":"1",
"symboltoken":"3045",
"exchange":"NSE",
}
```

#### Cancel Rule Response

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": {
"id": "1"
}
}
```

**Python**

```python
import http.client

conn = http.client.HTTPSConnection("apiconnect.angelone.in")
payload = "{\r\n    \"id\": \"1\",\r\n
 \"symboltoken\": \"3045\",\r\n    \"exchange\": \"NSE\"\r\n}"
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
conn.request("POST", "/rest/secure/angelbroking/gtt/v1/cancelRule
", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({"id":"1","symboltoken":"3045",
"exchange":"NSE"});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/gtt/v1/cancelRule\n',
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
RequestBody body = RequestBody.create(mediaType, "{\r\n    \"id\": \"1\",\r\n
   \"symboltoken\": \"3045\",\r\n    \"exchange\": \"NSE\"\r\n}");
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/gtt/v1/cancelRule
")
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
}
```

**R**

```r
library(httr)

url <- "https://apiconnect.angelone.in/
rest/secure/angelbroking/
gtt/v1/cancelRule"
json_body <- jsonlite::toJSON(list(
    "id": "1",
    "symboltoken":"3045",
    "exchange":"NSE"

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
  rest/secure/angelbroking/
  gtt/v1/cancelRule%0A"
  method := "POST"

  payload := strings.NewReader({
    "id": "1",
    "symboltoken":"3045",
    "exchange":"NSE"
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

## Rule Details Request

When a rule is successfully fetched, the API returns complete details of the rule.

#### All requests and its response structure is as below.

#### Rule Details Request

```json
{
"id":"1",
}
```

#### Rule Details Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":{
"status":"NEW",
"createddate":"2020-11-16T14:19:51Z",
"updateddate":"2020-11-16T14:28:01Z",
"expirydate":"2021-11-16T14:19:51Z",
"clientid":"100",
"tradingsymbol":"SBIN-EQ",
"symboltoken":"3045",
"exchange":"NSE",
"transactiontype":"BUY",
"producttype":"DELIVERY",
"price":"195",
"qty":"1",
"triggerprice":"196",
"disclosedqty":"10"
}
}
```

**Python**

```python
import http.client

conn = http.client.HTTPSConnection("apiconnect.angelone.in")
payload = "{\r\n    \"id\": \"1\"\r\n}"
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
conn.request("POST", "/rest/secure/angelbroking/
gtt/v1/ruleDetails", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({"id":"1"});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/gtt/
  v1/ruleDetails',
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
     "{\r\n    \"id\": \"1\"\r\n}");
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/
  gtt/v1/ruleDetails")
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
rest/secure/angelbroking/
gtt/v1/ruleDetails"
json_body <- jsonlite::toJSON(list(
    "id": "1",

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
  rest/secure/angelbroking/gtt/
  v1/ruleDetails"
  method := "POST"

  payload := strings.NewReader({

    "id": "1",

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

## Rule List Request

When a list of rules is successfully fetched, the API returns complete details for the list of rules.

#### All requests and its response structure is as below.

#### Rule List Request

```json
{
"status":[
"NEW",
"CANCELLED",
"ACTIVE",
"SENTTOEXCHANGE",
"FORALL"
],
"page":1,
"count":10
}
```

#### Rule List Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":{
"status":"NEW",
"createddate":"2020-11-16T14:19:51Z",
"updateddate":"2020-11-16T14:28:01Z",
"expirydate":"2021-11-16T14:19:51Z",
"clientid":"100",
"tradingsymbol":"SBIN-EQ",
"symboltoken":"3045",
"exchange":"NSE",
"transactiontype":"BUY",
"producttype":"DELIVERY",
"price":"195",
"qty":"1",
"triggerprice":"196",
"disclosedqty":"10"
}
}
```

**Python**

```python
import http.client

conn = http.client.HTTPSConnection("apiconnect.angelone.in")
payload = "{\r\n    \"status\": [\r\n        \"NEW\",\r\n
   \"CANCELLED\",\r\n        \"ACTIVE\",\r\n
     \"SENTTOEXCHANGE\",\r\n        \"FORALL\"\r\n    ],
     \r\n    \"page\": 1,\r\n    \"count\": 10\r\n}"
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
conn.request("POST", "/rest/secure/angelbroking/gtt/v1/ruleList
", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({"status":["NEW",
"CANCELLED","ACTIVE","SENTTOEXCHANGE",
"FORALL"],"page":1,"count":10});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/
  gtt/v1/ruleList\n',
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
RequestBody body = RequestBody.create(mediaType, "{\r\n
      \"status\": [\r\n        \"NEW\",\r\n
       \"CANCELLED\",\r\n        \"ACTIVE\",\r\n
            \"SENTTOEXCHANGE\",\r\n        \"FORALL\"\r\n    ],
            \r\n    \"page\": 1,\r\n    \"count\": 10\r\n}");
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/gtt/
  v1/ruleList"
  )
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
rest/secure/angelbroking/
gtt/v1/ruleList"
json_body <- jsonlite::toJSON(list(
    "status": [
        "NEW",
        "CANCELLED",
        "ACTIVE",
        "SENTTOEXCHANGE",
        "FORALL"
    ],
    "page": 1,
    "count": 10

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
  rest/secure/angelbroking/gtt/
  v1/ruleList%0A"
  method := "POST"

  payload := strings.NewReader({
    "status": [
        "NEW",
        "CANCELLED",
        "ACTIVE",
        "SENTTOEXCHANGE",
        "FORALL"
    ],
    "page": 1,
    "count": 10
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
