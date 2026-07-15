<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Brokerage Calculator -->

# Brokerage Calculator

Brokerage Calculator API is used to calculate Brokerage charges and taxes et. al. that will be incurred by the user for placing the trade.

The API endpoint is:

```
https://apiconnect.angelone.in/rest/secure/angelbroking/brokerage/v1/estimateCharges
```

Headers are same as other requests.

#### The request body is :

```json
{
"orders":[
{
"product_type":"DELIVERY",
"transaction_type":"BUY",
"quantity":"10",
"price":"800",
"exchange":"NSE",
"symbol_name":"745AS33",
"token":"17117"
},{
"product_type":"DELIVERY",
"transaction_type":"BUY",
"quantity":"10",
"price":"800",
"exchange":"BSE",
"symbol_name":"PIICL151223",
"token":"726131"
}
]
}
```

#### Response Structure:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": {
"summary": {
"total_charges": 3.0796,
"trade_value": 16000,
"breakup": [
{
"name": "Angel One Brokerage",
"amount": 0.0,
"msg": "",
"breakup": []
},
{
"name": "External Charges",
"amount": 2.976,
"msg": "",
"breakup": [
{
"name": "Exchange Transaction Charges",
"amount": 0.56,
"msg": "",
"breakup": []
},
{
"name": "Stamp Duty",
"amount": 2.4,
"msg": "",
"breakup": []
},
{
"name": "SEBI Fees",
"amount": 0.016,
"msg": "",
"breakup": []
}
]
},
{
"name": "Taxes",
"amount": 0.1036,
"msg": "",
"breakup": [
{
"name": "Security Transaction Tax",
"amount": 0.0,
"msg": "",
"breakup": []
},
{
"name": "GST",
"amount": 0.1036,
"msg": "",
"breakup": []
}
]
}
]
},
"charges": [
{
"total_charges": 1.5162,
"trade_value": 8000,
"breakup": {
"name": "Angel One Brokerage",
"amount": 0.0,
"msg": "",
"breakup": []
},
{
"name": "External Charges",
"amount": 2.976,
"msg": "",
"breakup": [
{
"name": "Exchange Transaction Charges",
"amount": 0.56,
"msg": "",
"breakup": []
},
{
"name": "Stamp Duty",
"amount": 2.4,
"msg": "",
"breakup": []
},
{
"name": "SEBI Fees",
"amount": 0.016,
"msg": "",
"breakup": []
}
]
},
{
"name": "Taxes",
"amount": 0.1036,
"msg": "",
"breakup": [
{
"name": "Security Transaction Tax",
"amount": 0.0,
"msg": "",
"breakup": []
},
{
"name": "GST",
"amount": 0.1036,
"msg": "",
"breakup": []
}
]
}
]
},

},
{
"total_charges": 1.5634,
"trade_value": 8000,
"breakup": {
"name": "Angel One Brokerage",
"amount": 0.0,
"msg": "",
"breakup": []
},
{
"name": "External Charges",
"amount": 2.976,
"msg": "",
"breakup": [
{
"name": "Exchange Transaction Charges",
"amount": 0.56,
"msg": "",
"breakup": []
},
{
"name": "Stamp Duty",
"amount": 2.4,
"msg": "",
"breakup": []
},
{
"name": "SEBI Fees",
"amount": 0.016,
"msg": "",
"breakup": []
}
]
},
{
"name": "Taxes",
"amount": 0.1036,
"msg": "",
"breakup": [
{
"name": "Security Transaction Tax",
"amount": 0.0,
"msg": "",
"breakup": []
},
{
"name": "GST",
"amount": 0.1036,
"msg": "",
"breakup": []
}
]
}
]
}
]
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
    \"orders\": [\n
        {\n
            \"product_type\": \"DELIVERY\",\n
            \"transaction_type\": \"BUY\",\n
            \"quantity\": \"10\",\n
            \"price\": \"800\",\n
            \"exchange\": \"NSE\",\n
            \"symbol_name\": \"SBIN-EQ\",\n
            \"token\": \"3045\"\n
        }\n
    ]\n
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
"/rest/secure/angelbroking/order/
v1/estimateCharges",
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
   "orders": [
        {
            "product_type": "DELIVERY",
            "transaction_type": "BUY",
            "quantity": "10",
            "price": "800",
            "exchange": "NSE",
            "symbol_name": "SBIN-EQ",
            "token": "3045"
        }
    ]
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
   rest/secure/angelbroking/order/
   v1/estimateCharges',
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
RequestBody body = RequestBody.create(mediaType, "{\n" +
    "  \"orders\": [\n" +
    "    {\n" +
    "      \"product_type\": \"DELIVERY\",\n" +
    "      \"transaction_type\": \"BUY\",\n" +
    "      \"quantity\": \"10\",\n" +
    "      \"price\": \"800\",\n" +
    "      \"exchange\": \"NSE\",\n" +
    "      \"symbol_name\": \"SBIN-EQ\",\n" +
    "      \"token\": \"3045\"\n" +
    "    }\n" +
    "  ]\n" +
    "}");

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/estimateCharges")
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
v1/estimateCharges"
library(jsonlite)

json_body <- toJSON(list(
  orders = list(
    list(
      product_type = "DELIVERY",
      transaction_type = "BUY",
      quantity = "10",
      price = "800",
      exchange = "NSE",
      symbol_name = "SBIN-EQ",
      token = "3045"
    )
  )
), auto_unbox = TRUE)

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
  rest/secure/angelbroking/order/v1/estimateCharges"
  method := "POST"

  payload := strings.NewReader({"orders": [
        {
            "product_type": "DELIVERY",
            "transaction_type": "BUY",
            "quantity": "10",
            "price": "800",
            "exchange": "NSE",
            "symbol_name": "SBIN-EQ",
            "token": "3045"
        }
    ]})

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
