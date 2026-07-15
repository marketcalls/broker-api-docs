<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Instruments -->

# Instruments

| Request Type | Endpoint | Description |
| --- | --- | --- |
| GET | https://margincalculator.angelone.in/OpenAPI_File/files/OpenAPIScripMaster.json | Retrieve the CSV dump of all tradable instruments |
| POST | https://apiconnect.angelone.in/order-service/rest/secure/angelbroking/order/v1/getLtpData | Retrieve LTP quotes for one or more instruments |
| GET | https://apiconnect.angelone.in/rest/secure/angelbroking/marketData/v1/nseIntraday | NSE Scrips Allowed for Intraday |
| GET | https://apiconnect.angelone.in/rest/secure/angelbroking/marketData/v1/bseIntraday | BSE Scrips Allowed for Intraday |
| GET | https://apiconnect.angelone.in/rest/secure/angelbroking/securities/v1/cautionaryScrips | To find out cautionary messages as per the exchanges for tokens of individual scrips |

Various kinds of instruments exist between multiple exchanges and segments that trade. Any application that facilitates trading needs to have a master list of these instruments. The instruments API provides a consolidated, import-ready CSV list of instruments available for trading.

## Fetching the full instrument list

The instrument list API returns a gzipped CSV dump of instruments across all exchanges that can be imported into a database. The dump is generated once every day and hence last_price is not real time.

```
https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json
```

This is the only URL for fetching instrument data as below:.

```json
[{“token":"2885","symbol":"RELIANCE-EQ","name":"RELIANCE","expiry":"","strike":"-1.000000","lotsize":"1","instrumenttype":"","exch_seg":"nse_cm","tick_size":"5.000000”}, …]
```

### Fetching LTP quotes for instrument

Note: Authorization header is mandatory here.

#### Request:

```json
{
"exchange": "NSE",
"tradingsymbol": "SBIN-EQ",
"symboltoken": "3048"
}
```

#### Response:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": [
{
"exchange": "NSE",
"tradingsymbol": "SBIN-EQ",
"symboltoken": 3048,
"open": "18600",
"high": "12689",
"low": "86864",
"close": "88775",
"ltp": "19100",
}
}
```

### Fetching Token for Individual Scrips

Tokens of Individual scrips can be looked up by the use of Search Scrip API.

```
https://apiconnect.angelone.in/rest/secure/angelbroking/order/v1/searchScrip
```

Note: Please note that only one Scrip is permitted per request.

#### Request:

```json
{
"exchange": "NSE",
"searchscrip": "SBIN"
}
```

#### Response:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data":[
{
"exchange": "NSE",
"tradingsymb{ol": "SBIN-AF",
"symboltoken": "11128"
},
{
"exchange": "NSE",
"tradingsymbol": "SBIN-BE",
"symboltoken": "4884"
},
{
"exchange": "NSE",
"tradingsymbol": "SBIN-BL",
"symboltoken": "12740"
},
{
"exchange": "NSE",
"tradingsymbol": "SBIN-EQ",
"symboltoken": "3045"
},
{
"exchange": "NSE",
"tradingsymbol": "SBIN-IQ",
"symboltoken": "28450"
},
{
"exchange": "NSE",
"tradingsymbol": "SBIN-RL",
"symboltoken": "16382"
},
{
"exchange": "NSE",
"tradingsymbol": "SBIN-U3",
"symboltoken": "22351"
},
{
"exchange": "NSE",
"tradingsymbol": "SBIN-U4",
"symboltoken": "22353"
}
]
}
```

### CSV response columns

| Column | Description |
| --- | --- |
| exchange_tokenstring | The numerical identifier issued by the exchange representing the instrument. |
| tradingsymbolstring | Exchange tradingsymbol of the instrument |
| namestring | Name of the company (for equity instruments) |
| expirystring | Expiry date (for derivatives) |
| strikefloat | Strike (for options) |
| tick_sizefloat | Value of a single price tick |
| lot_sizeint | Quantity of a single lot |
| instrument_typestring | EQ, FUT, CE, PE |

**Python**

```python
import http.client
import mimetypes
conn = http.client.HTTPSConnection(
    "apiconnect.angelone.in"
    )
payload = "{\n     \"exchange\": \"NSE\",\n
    \"tradingsymbol\": \"SBIN-EQ\",\n
    \"symboltoken\": \"3045\"\n}"
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
"/order-service/rest/secure/angelbroking/order/
v1/getLtpData",
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
    "exchange": "NSE",
    "tradingsymbol": "SBIN-EQ",
    "symboltoken": "3045"

});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  order-service/rest/secure/angelbroking/order/
  v1/getLtpData',
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
    "{\n
        \"symbol_token\": 11915\n
    }");

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  order-service/rest/secure/angelbroking/order/
  v1/getLtpData")
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
order-service/rest/secure/angelbroking/order/
v1/getLtpData"

json_body <- jsonlite::toJSON(list(
    "exchange": "NSE",
    "tradingsymbol": "SBIN-EQ",
    "symboltoken": "3045"

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
  order-service/rest/secure/angelbroking/order/v1/getLtpData"
  method := "POST"

  payload := strings.NewReader({
    "exchange": "NSE",
    "tradingsymbol": "SBIN-EQ",
    "symboltoken": "3045"

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

## Scrips Allowed for Intraday trading

To find out which of the scrips are allowed for Intraday trading along with their respective multipliers for margin trading, you can use the following APIs.

#### For NSE

```
https://apiconnect.angelone.in/rest/secure/angelbroking/marketData/v1/nseIntraday
```

#### Response:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data":[
{
"exchange": "NSE",
"SymbolName": "CHEMPLASTS",
"Multiplier": "5.0"
},
{
"exchange": "NSE",
"SymbolName": "SANGHVIMOV",
"Multiplier": "5.0"
},
]
}
```

#### For BSE

```
https://apiconnect.angelone.in/rest/secure/angelbroking/marketData/v1/bseIntraday
```

#### Response:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data":[
{
"exchange": "NSE",
"SymbolName": "TAALENT",
"Multiplier": "1.0"
},
{
"exchange": "NSE",
"SymbolName": "ARE&M",
"Multiplier": "5.0"
},
]
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
"/rest/secure/angelbroking/marketData/v1/nseIntraday",
payload,
headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = '';

var config = {
  method: 'get',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/marketData/
  v1/nseIntraday',

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
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
rest/secure/angelbroking/marketData
/v1/nseIntraday")

  .method("GET", null)
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
rest/secure/angelbroking/marketData/
v1/nseIntraday"

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
  rest/secure/angelbroking/marketData/v1/nseIntraday"
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

## Scrips under cautionary messages

To find out cautionary messages as per the exchanges for tokens of individual scrips.

#### Request:

```json
{
"scripconsent": "yes"
}
```

#### Response:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data":[
{
"token": "532083",
"symbol": "SHKALYN",
"message": "Security is under Gross settlement (Trade for Trade)"
},
{
"token": "512477",
"symbol": "BETXIND",
"message": "Stage 1 Long Term ASM scrip. The scrip PE is greater than 50 for previous 4 trailing quarters,Average daily number of unique Clients/PAN traded in the scrip in previous 30 days is less than 100"
},
{
"token": "511147",
"symbol": "WSFX",
"message": "Average daily number of unique Clients/PAN traded in the scrip in previous 30 days is less than 100, Close to Close price movement was greater than 25% in previous 1 month"
},
{
"token": "523127",
"symbol": "EIHAHOTELS",
"message": "Average daily number of unique Clients/PAN traded in the scrip in previous 30 days is less than 100"
},
{
"token": "524458",
"symbol": "INDOEURO",
"message": "Average daily number of unique Clients/PAN traded in the scrip in previous 30 days is less than 100"
}
]
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
"/rest/secure/angelbroking/securities/v1/cautionaryScrips",
payload,
headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = '';

var config = {
  method: 'get',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/securities/v1/cautionaryScrips',

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
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
rest/secure/angelbroking/securities/v1/cautionaryScrips")

  .method("GET", null)
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
rest/secure/angelbroking/securities/v1/cautionaryScrips"

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
  rest/secure/angelbroking/securities/v1/cautionaryScrips"
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
