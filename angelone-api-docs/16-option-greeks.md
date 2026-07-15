<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Option Greeks -->

# Option Greeks

Option Greeks Delta(Δ), Gamma (Γ), Theta(Θ) and Vega(ν) along with implied volatility are available on SmartAPI platform.

The API endpoint is:

```
https://apiconnect.angelone.in/rest/secure/angelbroking/marketData/v1/optionGreek
```

Headers are same as other requests.

#### The request body is as follows :

```json
{
"name": "TCS", // Here Name represents the Underlying stock
"expirydate": "25JAN2024"
}
```

Once you pass the underlying and the desired expiry date, it provides you the four greeks, i.e. Delta, Gamma, Theta, Vega and Implied Volatility (IV) for multiple strike prices.

#### Sample Response:

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data":[
{
"name": "TCS",
"expiry": "25JAN2024",
"strikePrice": "3900.000000",
"optionType": "CE",
"delta": "0.492400",
"gamma": "0.002800",
"theta": "-4.091800",
"vega": "2.296700",
"impliedVolatility": "16.330000",
"tradeVolume": "24048.00"
},
{
"name": "TCS",
"expiry": "25JAN2024",
"strikePrice": "4000.000000",
"optionType": "CE",
"delta": "0.239000",
"gamma": "0.002200",
"theta": "-3.033500",
"vega": "1.785400",
"impliedVolatility": "22.190000",
"tradeVolume": "12976.00"
}
]
}
```

There will be multiple JSON objects in the response, each for a specific strike price.

Currently option greeks are available only for NSE.

**Python**

```python
import http.client
import mimetypes
conn = http.client.HTTPSConnection(
    "apiconnect.angelone.in"
    )
payload = "{\n
       \"name\": \"TCS\",
       \n    \"expirydate\": \"25JAN2024\",
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
v1/optionGreek",
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
    "name":"TCS",
    "expirydate":"25JAN2024"
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
   rest/secure/angelbroking/order/
   v1/optionGreek',
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
        \"name\": \"TCS\",\n
        \"expirydate\": \"25JAN2024\",\n
    }");

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/optionGreek")
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
v1/optionGreek"
json_body <- jsonlite::toJSON(list(
    "name":"TCS",
    "expirydate":"25JAN2024"
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
  rest/secure/angelbroking/order/v1/optionGreek"
  method := "POST"

  payload := strings.NewReader({
    "name":"TCS",
    "expirydate":"25JAN2024",
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
