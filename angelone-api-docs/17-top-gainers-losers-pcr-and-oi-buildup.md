<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Top Gainers/Losers, PCR and OI Buildup -->

# Top Gainers/Losers, PCR and OI Buildup

## 1. Top Gainers/ Losers

Top Gainers/Losers API gives you the Top gainers and Losers in the derivatives segment for the day. You can choose from which types of data you want. The data is available for three time periods, i.e. near(Current Month), next(Next Month), Far (The month after next month).

The API endpoint for the same is :

```
https://apiconnect.angelone.in/rest/secure/angelbroking/marketData/v1/gainersLosers
```

Headers are same as for all other requests.

#### The Request packet is as follows:

```json
{
"datatype": "PercOIGainers", // Type of Data you want(PercOILosers/PercOIGainers/PercPriceGainers/PercPriceLosers)
"expirytype": "NEAR" // Expiry Type (NEAR/NEXT/FAR)
}
```

#### The response received for the request is as follows:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": [
{
"tradingSymbol": "HDFCBANK25JAN24FUT",
"percentChange": 20.02,
"symbolToken": 55394,
"opnInterest": 118861600,
"netChangeOpnInterest": 1.98253E7
},
{
"tradingSymbol": "IEX25JAN24FUT",
"percentChange": 15.57,
"symbolToken": 55409,
"opnInterest": 77827500,
"netChangeOpnInterest": 1.0485E7
},
{
"tradingSymbol": "KOTAKBANK25JAN24FUT",
"percentChange": 11.07,
"symbolToken": 55428,
"opnInterest": 30164800,
"netChangeOpnInterest": 3007600.0
},
{
"tradingSymbol": "ICICIGI25JAN24FUT",
"percentChange": 7.91,
"symbolToken": 55402,
"opnInterest": 3954500,
"netChangeOpnInterest": 290000.0
},
{
"tradingSymbol": "DRREDDY25JAN24FUT",
"percentChange": 7.17,
"symbolToken": 55376,
"opnInterest": 2211625,
"netChangeOpnInterest": 148000.0
},
{
"tradingSymbol": "TATASTEEL25JAN24FUT",
"percentChange": 6.73,
"symbolToken": 55503,
"opnInterest": 234679500,
"netChangeOpnInterest": 1.4795E7
},
{
"tradingSymbol": "OFSS25JAN24FUT",
"percentChange": 6.5,
"symbolToken": 55462,
"opnInterest": 770400,
"netChangeOpnInterest": 47000.0
},
{
"tradingSymbol": "INDUSINDBK25JAN24FUT",
"percentChange": 6.23,
"symbolToken": 55417,
"opnInterest": 16300000,
"netChangeOpnInterest": 956500.0
},
{
"tradingSymbol": "CUB25JAN24FUT",
"percentChange": 5.99,
"symbolToken": 55367,
"opnInterest": 32735000,
"netChangeOpnInterest": 1850000.0
},
{
"tradingSymbol": "GUJGASLTD25JAN24FUT",
"percentChange": 5.98,
"symbolToken": 55389,
"opnInterest": 6023750,
"netChangeOpnInterest": 340000.0
}
]
}
```

This lists down all the OI Gainers for the day. Please note that this data is cumulative of OI of all strike prices for the Option Contracts, hence maps all the data to the futures token of the same expiry date. Futures Token here just denotes expiry date and the underlying stock. OI Gainers/ Losers or Price Gainers/ Losers data is for options contracts only.

| Key | Possible Values |
| --- | --- |
| DataType | PercPriceGainers<br>PercPriceLosers<br>PercOILosers<br>PercOIGainers |
| ExpiryType | NEAR<br>FAR<br>NEXT |

**Python**

```python
import http.client
import mimetypes
conn = http.client.HTTPSConnection(
    "apiconnect.angelone.in"
    )
payload = "{\n
       \"datatype\": \"PercOIGainers\",
       \n    \"expirytype\": \"NEAR\",
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
"/rest/secure/angelbroking/order/
v1/gainersLosers",
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
    "datatype":"PercOIGainers",
    "expirytype":"NEAR",
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
   rest/secure/angelbroking/order/
   v1/gainersLosers',
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
RequestBody body = RequestBody.create(mediaType, "{\n
        \"datatype\": \"PercOIGainers\",\n
        \"expirytype\": \"NEAR\",\n
    }");

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/gainersLosers")
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
rest/secure/angelbroking/order/
v1/gainersLosers"
json_body <- jsonlite::toJSON(list(
    "datatype":"PercOIGainers",
    "expirytype":"NEAR"
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
  rest/secure/angelbroking/order/v1/gainersLosers"
  method := "POST"

  payload := strings.NewReader({
    "datatype":"PercOIGainers",
    "expirytype":"NEAR",
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

## 2. PCR Volume API

PCR Volume API gives the ratio of Put - Call Ratio for Options Contracts in the market using which you can gauge the market sentiments and make you trading decisions.

The API endpoint is:

```
https://apiconnect.angelone.in/rest/secure/angelbroking/marketData/v1/putCallRatio
```

Headers remain same as in all other requests.

#### Request Body:

```
//No request Body
```

#### Response from the API:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": [
{
"pcr": 1.04,
"tradingSymbol": "NIFTY25JAN24FUT,

},
{
"pcr": 0.58,
"tradingSymbol": "HEROMOTOCO25JAN24FUT,

},
{
"pcr": 0.65,
"tradingSymbol": "ADANIPORTS25JAN24FUT",
}
]
}
```

Please note that PCR here represents the cumulative PCR of Options Contracts for all strike prices, hence the Trading Symbol has been mapped to the corresponding futures instrument for each underlying stock. It represents PCR for Options only.

**Python**

```python
import http.client
import mimetypes
conn = http.client.HTTPSConnection(
    "apiconnect.angelone.in"
    )
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
"/rest/secure/angelbroking/order/
v1/putCallRatio",
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
   rest/secure/angelbroking/order/
   v1/putCallRatio',
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

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/putCallRatio")
  .method("GET")
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
rest/secure/angelbroking/order/
v1/putCallRatio"

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
  rest/secure/angelbroking/order/v1/putCallRatio"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url)

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

## 3. OI BuildUp

Using this API, you can check for Long Buildup, Short Buildup, Short Covering and Long Unwinding. Pass the requisite keys in the API and you'd get the appropriate list for your usage.

The API end point is:

```
https://apiconnect.angelone.in/rest/secure/angelbroking/marketData/v1/OIBuildup
```

Headers will be same as all the other APIs

#### The request Body will be as follows:

```json
{
"expirytype": "NEAR",
"datatype": "Long Built Up"
}
```

Similar to Top Gainers/ Losers API, we can pass multiple values in the data_type and expiry_type keys.

The values are as follows:

| Key | Possible Values |
| --- | --- |
| DataType | Long Built Up<br>Short Built Up<br>Short Covering<br>Long Unwinding |
| ExpiryType | NEAR<br>FAR<br>NEXT |

Please note that there is a single space between the different words in datatype, i.e. Long<single space>Built<single-space>Up

#### The response will be as follows:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": [
{
"symbolToken": "55424",
"ltp": "723.8",
"netChange": "-28.25",
"percentChange": "-3.76",
"opnInterest": "24982.5",
"netChangeOpnInterest": "-76.25",
"tradingSymbol": "JINDALSTEL25JAN24FUT"
},
{
"symbolToken": "55452",
"ltp": "134.25",
"netChange": "-5.05",
"percentChange": "-3.63",
"opnInterest": "67965.0",
"netChangeOpnInterest": "-3120.0",
"tradingSymbol": "NATIONALUM25JAN24FUT"
}
]
}
```

You will get all the responses on passing the correct values for data type and expiry time.

Currently top gainers/losers, PCR and OI buildup APIs are available only for NSE.

**Python**

```python
import http.client
import mimetypes
conn = http.client.HTTPSConnection(
    "apiconnect.angelone.in"
    )
payload = "{\n
       \"datatype\": \"Long Built Up\",
       \n    \"expirytype\": \"NEAR\",
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
"/rest/secure/angelbroking/order/
v1/OIBuildup",
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
    "datatype":"Long Built Up",
    "expirytype":"NEAR",
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
   rest/secure/angelbroking/order/
   v1/OIBuildup',
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
RequestBody body = RequestBody.create(mediaType, "{\n
        \"datatype\": \"Long Built Up\",\n
        \"expirytype\": \"NEAR\",\n
    }");

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/OIBuildup")
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
rest/secure/angelbroking/order/
v1/OIBuildup"
json_body <- jsonlite::toJSON(list(
    "datatype":"Long Built Up",
    "expirytype":"NEAR"
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
  rest/secure/angelbroking/order/v1/OIBuildup"
  method := "POST"

  payload := strings.NewReader({
    "datatype":"Long Built Up",
    "expirytype":"NEAR",
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
