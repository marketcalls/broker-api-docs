<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Margin Calculator -->

# Margin Calculator

Margin Calculator API delivers the real time margin calculations for a basket of positions.

```
https://apiconnect.angelone.in/rest/secure/angelbroking/margin/v1/batch
```

## Field Description

| Field | Data type | Description |
| --- | --- | --- |
| exchange | BSE<br>NSE<br>NFO<br>MCX<br>BFO | BSE Equity<br>NSE Equity<br>NSE Future and Options<br>MCX Commodity<br>BSE Futures and Options |
| qty | int | Quantity. Pls note that in the NFO segment it denotes the no. of units in a lot. |
| price | int | Price |
| producttype | DELIVERY<br>CARRYFORWARD<br>MARGIN<br>INTRADAY<br>BO | Cash & Carry for equity (CNC)<br>Normal for futures and options (NRML)<br>Margin Delivery<br>Margin Intraday Squareoff (MIS)<br>Bracket Order (Only for ROBO) |
| token | String | Symbol/token being traded |
| tradetype | BUY<br>SELL | Buy<br>Sell |
| ordertype | LIMIT<br>MARKET<br>STOPLOSS_LIMIT<br>STOPLOSS_MARKET | Limit Order<br>Market order<br>Stoploss Limit Order<br>Stoploss Market Order |

## Margin Calculator

#### Request and its response structure is as below.

The default value for orderType field is "LIMIT"

#### Margin Calculator Request

```json
{
"positions":[
{
"exchange": "NFO",
"qty": 50,
"price": 0,
"productType": "INTRADAY",
"token": "67300",
"tradeType": "BUY",
"orderType": "LIMIT"
},
{
"exchange": "NFO",
"qty": 50,
"price": 0,
"productType": "INTRADAY",
"token": "67308",
"tradeType": "SELL",
"orderType": "MARKET"
}
]
}
```

#### Margin Calculator Response

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data":{
"totalMarginRequired": 29612.35,
"marginComponents":{
"netPremium": 5060,
"spanMargin": 0,
"marginBenefit": 79876.5,
"deliveryMargin": 0,
"nonNFOMargin": 0,
"totOptionsPremium": 10100
}
}
}
```

**Python**

```python
import http.client

conn = http.client.HTTPSConnection("apiconnect.angelone.in")
payload = "{\n" +
  "  \"positions\": [\n" +
  "    {\n" +
  "      \"exchange\": \"NFO\",\n" +
  "      \"qty\": 50,\n" +
  "      \"price\": 0,\n" +
  "      \"productType\": \"INTRADAY\",\n" +
  "      \"orderType\" : \"MARKET\",\n +
  "      \"token\": \"67300\",\n" +
  "      \"tradeType\": \"BUY\"\n" +
  "    },\n" +
  "    {\n" +
  "      \"exchange\": \"NFO\",\n" +
  "      \"qty\": 50,\n" +
  "      \"price\": 0,\n" +
  "      \"productType\": \"INTRADAY\",\n" +
  "      \"orderType\" : \"LIMIT\",\n +
  "      \"token\": \"67308\",\n" +
  "      \"tradeType\": \"SELL\"\n" +
  "    }\n" +
  "  ]\n" +
  "}"
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
conn.request("POST", "/rest/secure/angelbroking/margin/v1/batch", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({
     "positions": [
          {
               "exchange": "NFO",
               "qty": 50,
               "price": 0,
               "productType": "INTRADAY",
               "orderType":"LIMIT",
               "token": "67300",
               "tradeType": "BUY"
          },
          {
               "exchange": "NFO",
               "qty": 50,
               "price": 0,
               "productType": "INTRADAY",
               "orderType":"MARKET",
               "token": "67308",
               "tradeType": "SELL"
          }
     ]
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/margin/v1/batch',
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
RequestBody body = RequestBody.create(mediaType, "{\n" +
  "  \"positions\": [\n" +
  "    {\n" +
  "      \"exchange\": \"NFO\",\n" +
  "      \"qty\": 50,\n" +
  "      \"price\": 0,\n" +
  "      \"productType\": \"INTRADAY\",\n" +
  "      \"orderType\" : \"MARKET\",\n +
  "      \"token\": \"67300\",\n" +
  "      \"tradeType\": \"BUY\"\n" +
  "    },\n" +
  "    {\n" +
  "      \"exchange\": \"NFO\",\n" +
  "      \"qty\": 50,\n" +
  "      \"price\": 0,\n" +
  "      \"productType\": \"INTRADAY\",\n" +
  "      \"orderType\" : \"LIMIT\",\n +
  "      \"token\": \"67308\",\n" +
  "      \"tradeType\": \"SELL\"\n" +
  "    }\n" +
  "  ]\n" +
  "}");
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/margin/v1/batch")
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

url <- "https://apiconnect.angelone.in
/rest/secure/angelbroking/margin/v1/batch"
json_body <- jsonlite::toJSON(list(
  "positions": [
          {
               "exchange": "NFO",
               "qty": 50,
               "price": 0,
               "productType": "INTRADAY",
               "orderType" : "LIMIT",
               "token": "67300",
               "tradeType": "BUY"
          },
          {
               "exchange": "NFO",
               "qty": 50,
               "price": 0,
               "productType": "INTRADAY",
               "orderType" : "LIMIT",
               "token": "67308",
               "tradeType": "SELL"
          }
     ]
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
   rest/secure/angelbroking/margin/v1/batch"
   method := "POST"

   payload := strings.NewReader({
     "positions": [
          {
               "exchange": "NFO",
               "qty": 50,
               "price": 0,
               "productType": "INTRADAY",
               "orderType":"MARKET",
               "token": "67300",
               "tradeType": "BUY"
          },
          {
               "exchange": "NFO",
               "qty": 50,
               "price": 0,
               "productType": "INTRADAY",
               "orderType":"LIMIT",
               "token": "67308",
               "tradeType": "SELL"
          }
     ]
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
