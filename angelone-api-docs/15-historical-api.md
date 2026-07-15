<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Historical API -->

# Historical API

Historical API provides past data of the indices and instruments. When a successful request is placed, corresponding data is returned. A single API endpoint provides the data for all segments. The exchange parameter in the request body is used to specify the segment whose data is required.

```
https://apiconnect.angelone.in/rest/secure/angelbroking/historical/v1/getCandleData
```

## Exchange Constants

| Param | Value | Description |
| --- | --- | --- |
| exchange | NSE | NSE Stocks and Indices |
|  | NFO | NSE Futures and Options |
|  | BSE | BSE Stocks and Indices |
|  | BFO | BSE Future and Options |
|  | MCX | Commodities Exchange |

## Interval Constants

| Interval | Description |
| --- | --- |
| ONE_MINUTE | 1 Minute |
| THREE_MINUTE | 3 Minute |
| FIVE_MINUTE | 5 Minute |
| TEN_MINUTE | 10 Minute |
| FIFTEEN_MINUTE | 15 Minute |
| THIRTY_MINUTE | 30 Minute |
| ONE_HOUR | 1 Hour |
| ONE_DAY | 1 Day |

## Max Days in one Request

The API can provide data of multiple days in one request. Below is the list of Max no of days upto which data can be provided for the requested intervals:

| Interval | Max Days in one Request |
| --- | --- |
| ONE_MINUTE | 30 |
| THREE_MINUTE | 60 |
| FIVE_MINUTE | 100 |
| TEN_MINUTE | 100 |
| FIFTEEN_MINUTE | 200 |
| THIRTY_MINUTE | 200 |
| ONE_HOUR | 400 |
| ONE_DAY | 2000 |

## Get Candle Data

#### All requests and its response structure is as below.

#### Get Candle Data Request

```json
{
"exchange": "NSE",
"symboltoken": "99926000"
"interval": "ONE_HOUR",
"fromdate": "2023-09-06 11:15"
"todate": "2023-09-06 12:00"
}
```

#### Get Candle Data Response

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": [
[
"2023-09-06T11:15:00+05:30",
19571.2,
19573.35,
19534.4,
19552.05,
0
]
]
}
```

**NOTE:**In Get Candle Data Request fromdate and todate format should be "yyyy-MM-dd hh:mm"The response is an array of records, where each record in turn is an array of the following values — [timestamp, open, high, low, close, volume].

**Python**

```python
import http.client

conn = http.client.HTTPSConnection("apiconnect.angelone.in")
payload = "{\r\n     \"exchange\": \"NSE\",\r\n
 \"symboltoken\": \"3045\",\r\n     \"interval\": \"ONE_MINUTE\",\r\n
    \"fromdate\": \"2021-02-08 09:00\",\r\n     \"todate\": \"2021-02-08 09:16\"\r\n}"
headers = {
  'X-PrivateKey': 'API_KEY',
  'Accept': 'application/json',
  'X-SourceID': 'WEB',
  'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
  'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
  'X-MACAddress': 'MAC_ADDRESS',
  'X-UserType': 'USER',
  'Authorization': 'Bearer AUTHORIZATION_TOKEN',
  'Accept': 'application/json',
  'X-SourceID': 'WEB',
  'Content-Type': 'application/json'
}
conn.request("POST", "/rest/secure/angelbroking/historical/v1/getCandleData", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({"exchange":"NSE","symboltoken":"3045",
"interval":"ONE_MINUTE","fromdate":"2021-02-08 09:00",
"todate":"2021-02-08 09:16"});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/historical/v1/
  getCandleData',
  headers: {
    'X-PrivateKey': 'API_KEY',
    'Accept': 'application/json, application/json',
    'X-SourceID': 'WEB, WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-UserType': 'USER',
    'Authorization': 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type': 'application/json'
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
      \"exchange\": \"NSE\",\r\n     \"symboltoken\": \"3045\",\r\n
         \"interval\": \"ONE_MINUTE\",\r\n     \"fromdate\": \"2021-02-08 09:00\",\r\n
           \"todate\": \"2021-02-08 09:16\"\r\n}");
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/historical/v1/
  getCandleData")
  .method("POST", body)
  .addHeader("X-PrivateKey", "API_KEY")
  .addHeader("Accept", "application/json")
  .addHeader("X-SourceID", "WEB")
  .addHeader("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  .addHeader("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  .addHeader("X-MACAddress", "MAC_ADDRESS")
  .addHeader("X-UserType", "USER")
  .addHeader("Authorization", "Bearer AUTHORIZATION_TOKEN")
  .addHeader("Accept", "application/json")
  .addHeader("X-SourceID", "WEB")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

**R**

```r
library(httr)

url <- "https://apiconnect.angelone.in/
rest/secure/angelbroking/
historical/v1/getCandleData"
json_body <- jsonlite::toJSON(list(
      "exchange": "NSE",
      "symboltoken": "3045",
      "interval": "ONE_MINUTE",
      "fromdate": "2021-02-08 09:00",
      "todate": "2021-02-08 09:16"

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
   rest/secure/angelbroking/historical/v1/
   getCandleData"
   method := "POST"

   payload := strings.NewReader({

      "exchange": "NSE",
      "symboltoken": "3045",
      "interval": "ONE_MINUTE",
      "fromdate": "2021-02-08 09:00",
      "todate": "2021-02-08 09:16"
 })

   client := &http.Client {
   }
   req, err := http.NewRequest(method, url, payload)

   if err != nil {
     fmt.Println(err)
     return
   }
   req.Header.Add("X-PrivateKey", "API_KEY")
   req.Header.Add("Accept", "application/json")
   req.Header.Add("X-SourceID", "WEB")
   req.Header.Add("X-ClientLocalIP", "CLIENT_LOCAL_IP")
   req.Header.Add("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
   req.Header.Add("X-MACAddress", "MAC_ADDRESS")
   req.Header.Add("X-UserType", "USER")
   req.Header.Add("Authorization", "Bearer AUTHORIZATION_TOKEN")
   req.Header.Add("X-PrivateKey", "API_KEY")
   req.Header.Add("Accept", "application/json")
   req.Header.Add("X-SourceID", "WEB")
   req.Header.Add("Content-Type", "application/json")

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

## Get Historical OI Data

Historical OI Data is available for live F&O contracts. Historical OI can be fetched using the token from the scrip master and passing it into the request body.

```
https://apiconnect.angelone.in/rest/secure/angelbroking/historical/v1/getOIData
```

#### Get OI Data Request

```json
{
"exchange": "NFO",
"symboltoken": "46823"
"interval": "THREE_MINUTE",
"fromdate": "2023-09-06 11:15"
"todate": "2023-09-06 12:00"
}
```

#### Get OI Data Response

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": [
{
"time": "2024-08-19T12:24:00+05:30",
"oi": 166100
}
]
}
```

**Python**

```python
import http.client

conn = http.client.HTTPSConnection("apiconnect.angelone.in")
payload = "{\r\n     \"exchange\": \"NFO\",\r\n
 \"symboltoken\": \"46823\",\r\n     \"interval\": \"ONE_MINUTE\",\r\n
    \"fromdate\": \"2021-02-08 09:00\",\r\n     \"todate\": \"2021-02-08 09:16\"\r\n}"
headers = {
  'X-PrivateKey': 'API_KEY',
  'Accept': 'application/json',
  'X-SourceID': 'WEB',
  'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
  'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
  'X-MACAddress': 'MAC_ADDRESS',
  'X-UserType': 'USER',
  'Authorization': 'Bearer AUTHORIZATION_TOKEN',
  'Accept': 'application/json',
  'X-SourceID': 'WEB',
  'Content-Type': 'application/json'
}
conn.request("POST", "/rest/secure/angelbroking/historical/v1/getOIData", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({"exchange":"NFO","symboltoken":"46823",
"interval":"ONE_MINUTE","fromdate":"2021-02-08 09:00",
"todate":"2021-02-08 09:16"});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/historical/v1/
  getOIData',
  headers: {
    'X-PrivateKey': 'API_KEY',
    'Accept': 'application/json, application/json',
    'X-SourceID': 'WEB, WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-UserType': 'USER',
    'Authorization': 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type': 'application/json'
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
      \"exchange\": \"NFO\",\r\n     \"symboltoken\": \"46823\",\r\n
         \"interval\": \"ONE_MINUTE\",\r\n     \"fromdate\": \"2021-02-08 09:00\",\r\n
           \"todate\": \"2021-02-08 09:16\"\r\n}");
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/historical/v1/
  getOIData")
  .method("POST", body)
  .addHeader("X-PrivateKey", "API_KEY")
  .addHeader("Accept", "application/json")
  .addHeader("X-SourceID", "WEB")
  .addHeader("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  .addHeader("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  .addHeader("X-MACAddress", "MAC_ADDRESS")
  .addHeader("X-UserType", "USER")
  .addHeader("Authorization", "Bearer AUTHORIZATION_TOKEN")
  .addHeader("Accept", "application/json")
  .addHeader("X-SourceID", "WEB")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

**R**

```r
library(httr)

url <- "https://apiconnect.angelone.in/
rest/secure/angelbroking/
historical/v1/getCandleData"
json_body <- jsonlite::toJSON(list(
      "exchange": "NFO",
      "symboltoken": "46823",
      "interval": "ONE_MINUTE",
      "fromdate": "2021-02-08 09:00",
      "todate": "2021-02-08 09:16"

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
   rest/secure/angelbroking/historical/v1/
   getOIData"
   method := "POST"

   payload := strings.NewReader({

      "exchange": "NFO",
      "symboltoken": "46823",
      "interval": "ONE_MINUTE",
      "fromdate": "2021-02-08 09:00",
      "todate": "2021-02-08 09:16"
 })

   client := &http.Client {
   }
   req, err := http.NewRequest(method, url, payload)

   if err != nil {
     fmt.Println(err)
     return
   }
   req.Header.Add("X-PrivateKey", "API_KEY")
   req.Header.Add("Accept", "application/json")
   req.Header.Add("X-SourceID", "WEB")
   req.Header.Add("X-ClientLocalIP", "CLIENT_LOCAL_IP")
   req.Header.Add("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
   req.Header.Add("X-MACAddress", "MAC_ADDRESS")
   req.Header.Add("X-UserType", "USER")
   req.Header.Add("Authorization", "Bearer AUTHORIZATION_TOKEN")
   req.Header.Add("X-PrivateKey", "API_KEY")
   req.Header.Add("Accept", "application/json")
   req.Header.Add("X-SourceID", "WEB")
   req.Header.Add("Content-Type", "application/json")

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
