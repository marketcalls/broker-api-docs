<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Orders -->

# Orders

The order APIs allows you to place orders of different varieties like normal orders, after market orders & stoploss orders.

For users utilizing the new static IP–based API key, the source IP address of Place order, Modify order, Cancel order api requests will be validated against the static IP registered by the user. The API request will be processed successfully only if the source IP matches the registered static IP.

To execute cash orders for scrips under surveillance keep "scripconsent" as yes.

| Request Type | APIs | Endpoint | Description |
| --- | --- | --- | --- |
| POST | Place Order | https://apiconnect.angelone.in/rest/secure/angelbroking/order/v1/placeOrder | To place an order |
| POST | Modify Order | https://apiconnect.angelone.in/rest/secure/angelbroking/order/v1/modifyOrder | To modify an order |
| POST | Cancel Order | https://apiconnect.angelone.in/rest/secure/angelbroking/order/v1/cancelOrder | To cancel an order |
| GET | Get Order Book | https://apiconnect.angelone.in/rest/secure/angelbroking/order/v1/getOrderBook | To retrieve Order book |
| GET | Get Trade Book | https://apiconnect.angelone.in/rest/secure/angelbroking/order/v1/getTradeBook | To retrieve trade book |
| POST | Get LTP Data | https://apiconnect.angelone.in/rest/secure/angelbroking/order/v1/getLtpData | To retrieve LTP data |
| GET | Get Individual Order Data | https://apiconnect.angelone.in/rest/secure/angelbroking/order/v1/details/{UniqueOrderID} | To retrieve individual order data |

See the list of constants in below given table.

## Order Constants

Here are several of the constant enum values used for placing orders.

| Param | Value | Description |
| --- | --- | --- |
| variety | NORMAL<br>STOPLOSS<br>ROBO | Normal Order (Regular)<br>Stop loss order<br>ROBO (Bracket Order) |
| transactiontype | BUY<br>SELL | Buy<br>Sell |
| ordertype | MARKET<br>LIMIT<br>STOPLOSS_LIMIT<br>STOPLOSS_MARKET | Market Order(MKT)<br>Limit Order(L)<br>Stop Loss Limit Order(SL)<br>Stop Loss Market Order(SL-M) |
| producttype | DELIVERY<br>CARRYFORWARD<br>MARGIN<br>INTRADAY<br>BO | Cash & Carry for equity (CNC)<br>Normal for futures and options (NRML)<br>Margin Delivery<br>Margin Intraday Squareoff (MIS)<br>Bracket Order (Only for ROBO) |
| Duration | DAY<br>IOC | Regular Order<br>Immediate or Cancel |
| exchange | BSE<br>NSE<br>NFO<br>MCX<br>BFO | BSE Equity<br>NSE Equity<br>NSE Future and Options<br>MCX Commodity<br>BSE Futures and Options |

## Order Parameters

These parameters are common across different order varieties.

| Param | Description |
| --- | --- |
| tradingsymbol | Trading Symbol of the instrument |
| symboltoken | Symbol Token is unique identifier |
| Exchange | Name of the exchange |
| transactiontype | BUY or SELL |
| ordertype | Order type (MARKET, LIMIT etc.) |
| quantity | Quantity to transact |
| producttype | Product type (CNC,MIS) |
| price | The min or max price to execute the order at (for LIMIT orders) |
| triggerprice | The price at which an order should be triggered (SL, SL-M) |
| squareoff | Only For ROBO (Bracket Order) |
| stoploss | Only For ROBO (Bracket Order) |
| trailingStopLoss | Only For ROBO (Bracket Order) |
| disclosedquantity | Quantity to disclose publicly (for equity trades) |
| duration | Order duration (DAY,IOC) |
| ordertag | It is optional to apply to an order to identify. The length of the tag should be less than 20 characters. |
| scripconsent | To execute cash orders for scrips under surveillance keep "scripconsent" as yes. |

## Place Orders

When an order is successfully placed, the API returns an order_id. The status of the order is not known at the moment of placing because of the aforementioned reasons.

All the orders placed after market hours will be treated as AMO orders.

All the market orders will be converted into limit orders by AngelOne as per the MPP limits specified [here](https://www.angelone.in/news/product-updates/market-price-protection-mpp-on-angel-one-safeguarding-your-orders).

IOC orders are not allowed for commodities segment.

#### All requests and its response structure is as below.

#### Place Order Request

```json
{
"variety":"NORMAL",
"tradingsymbol":"SBIN-EQ",
"symboltoken":"3045",
"transactiontype":"BUY",
"exchange":"NSE",
"ordertype":"MARKET",
"producttype":"INTRADAY",
"duration":"DAY",
"price":"194.50",
"squareoff":"0",
"stoploss":"0",
"quantity":"1",
"scripconsent":"yes"
}
```

#### Place Order Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":{
 "script":"SBIN-EQ",
 "orderid":"200910000000111"
 "uniqueorderid":"34reqfachdfih"
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
       \"exchange\": \"NSE\",
       \n    \"tradingsymbol\": \"INFY-EQ\",
       \n    \"quantity\": 5,
       \n    \"disclosedquantity\": 3,
       \n    \"transactiontype\": \"BUY\",
       \n    \"ordertype\": \"MARKET\",
       \n    \"variety\": \"STOPLOSS\",
       \n    \"producttype\": \"INTRADAY\"
       \n    \"scripconsent\": \"yes"\"
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
v1/placeOrder",
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
    "exchange":"NSE",
    "tradingsymbol":"INFY-EQ",
    "quantity":5,
    "disclosedquantity":3,
    "transactiontype":"BUY",
    "ordertype":"MARKET",
    "variety":"NORMAL",
    "producttype":"INTRADAY",
    "scripconsent": "yes"
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
   rest/secure/angelbroking/order/
   v1/placeOrder',
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
        \"exchange\": \"NSE\",\n
        \"tradingsymbol\": \"INFY-EQ\",\n
        \"quantity\": 5,\n
        \"disclosedquantity\": 3,\n
        \"transactiontype\": \"BUY\",\n
        \"ordertype\": \"MARKET\",\n
        \"variety\": \"NORMAL\",\n
        \"producttype\": \"INTRADAY\",\n
        \"scripconsent\": \"yes"\"\n
    }");

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/placeOrder")
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
v1/placeOrder"
json_body <- jsonlite::toJSON(list(
    "exchange":"NSE",
    "tradingsymbol":"INFY-EQ",
    "quantity":5,
    "disclosedquantity":3,
    "transactiontype":"BUY",
    "ordertype":"MARKET",
    "variety":"NORMAL",
    "producttype":"INTRADAY",
    "scripconsent": "yes"
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
  rest/secure/angelbroking/order/v1/placeOrder"
  method := "POST"

  payload := strings.NewReader({
    "variety":"NORMAL",
    "tradingsymbol":"SBIN-EQ",
    "symboltoken":"3045",
    "transactiontype":"BUY",
    "exchange":"NSE",
    "ordertype":"MARKET",
    "producttype":"INTRADAY",
    "duration":"DAY",
    "price":"194.50",
    "squareoff":"0",
    "stoploss":"0",
    "quantity":"1",
    "scripconsent":"yes"
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

## Modify Order

As long as on order is open or pending in the system, certain attributes of it may be modified. It is important to sent the right value for :variety in the URL.

#### Modify Order Request

```json
{
"variety":"NORMAL",
"orderid":"201020000000080",
"ordertype":"LIMIT",
"producttype":"INTRADAY",
"duration":"DAY",
"price":"194.00",
"quantity":"1",
"tradingsymbol":"SBIN-EQ",
"symboltoken":"3045",
"exchange":"NSE"
}
```

#### Modify Order Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":{
 "orderid":"201020000000080"
 "uniqueorderid":"34reqfachdfih"
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
    \"variety\": \"NORMAL\",\n
    \"orderid\": \"201020000000080\",\n
    \"ordertype\": \"LIMIT\",\n
    \"producttype\": \"INTRADAY\",\n
    \"duration\": \"DAY\",\n
    \"price\": \"194.00\",\n
    \"quantity\": \"1\"\n
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
v1/modifyOrder",
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
    "variety":"NORMAL",
    "orderid":"201020000000080",
    "ordertype":"LIMIT",
    "producttype":"INTRADAY",
    "duration":"DAY",
    "price":"194.00",
    "quantity":"1"
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/modifyOrder',
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
        \"variety\": \"NORMAL\",\n
        \"orderid\": \"201020000000080\",\n
        \"ordertype\": \"LIMIT\",\n
        \"producttype\": \"INTRADAY\",\n
        \"duration\": \"DAY\",\n
        \"price\": \"194.00\",\n
        \"quantity\": \"1\"\n
    }");

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/modifyOrder")
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
v1/modifyOrder"
json_body <- jsonlite::toJSON(list(
    "variety":"NORMAL",
    "orderid":"201020000000080",
    "ordertype":"LIMIT",
    "producttype":"INTRADAY",
    "duration":"DAY",
    "price":"194.00",
    "quantity":"1"
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
  rest/secure/angelbroking/order/v1/modifyOrder"
  method := "POST"

  payload := strings.NewReader({
    "variety":"NORMAL",
    "orderid":"201020000000080",
    "ordertype":"LIMIT",
    "producttype":"INTRADAY",
    "duration":"DAY",
    "price":"194.00",
    "quantity":"1"
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

## Cancel Order

As long as on order is open or pending in the system, it can be cancelled.

#### Cancel Order Request

```json
{
"variety":"NORMAL",
"orderid":"201020000000080",
}
```

#### Cancel Order Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":{
 "orderid":"201020000000080"
 "uniqueorderid":"34reqfachdfih"
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
    \"variety\": \"NORMAL\",\n
    \"orderid\": \"201020000000080\"\n
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
 v1/cancelOrder",
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
    "variety":"NORMAL",
    "orderid":"201020000000080"
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/cancelOrder',
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
     \"variety\": \"NORMAL\",\n
     \"orderid\": \"201020000000080\"\n
    }");

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/cancelOrder")
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
v1/cancelOrder"
json_body <- jsonlite::toJSON(list(
    "variety":"NORMAL",
    "orderid":"201020000000080"
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
  rest/secure/angelbroking/order/v1/cancelOrder"
  method := "POST"

  payload := strings.NewReader({
    "variety":"NORMAL",
    "orderid":"201020000000080",
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

## Get Order Book

#### Get Order Status Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":[{
"variety":NORMAL,
"ordertype":LIMIT,
"producttype":INTRADAY,
"duration":DAY,
"price":"194.00",
"triggerprice":"0",
"quantity":"1",
"disclosedquantity":"0",
"squareoff":"0",
"stoploss":"0",
"trailingstoploss":"0",
"tradingsymbol":"SBIN-EQ",
"transactiontype":BUY,
"exchange":NSE,
"symboltoken":null,
"instrumenttype":"",
"strikeprice":"-1",
"optiontype":"",
"expirydate":"",
"lotsize":"1",
"cancelsize":"1",
"averageprice":"0",
"filledshares":"0",
"unfilledshares":"1",
"orderid":201020000000080,
"text":"",
"status":"cancelled",
"orderstatus":"cancelled",
"updatetime":"20-Oct-2020 13:10:59",
"exchtime":"20-Oct-2020 13:10:59",
"exchorderupdatetime":"20-Oct-2020 13:10:59",
"fillid":"",
"filltime":"",
"parentorderid":"",
"uniqueorderid":"34reqfachdfih",
"exchangeorderid":"1100000000048358"
 }]
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
"/rest/secure/angelbroking/order/
v1/getOrderBook",
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
  url: 'https://apiconnect.angelone.in
  /rest/secure/angelbroking/order/
  v1/getOrderBook',
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
  rest/secure/angelbroking/order/
  v1/getOrderBook")

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
rest/secure/angelbroking/order/
v1/getOrderBook"

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
  rest/secure/angelbroking/order/v1/getOrderBook"
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

## Get Trade Book

It provides the trades for the current day

#### Get Trade Book Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":[{
"exchange":NSE,
"producttype":DELIVERY,
"tradingsymbol":"ITC-EQ",
"instrumenttype":"",
"symbolgroup":"EQ",
"strikeprice":"-1",
"optiontype":"",
"expirydate":"",
"marketlot":"1",
"precision":"2",
"multiplier":"-1",
"tradevalue":"175.00",
"transactiontype":"BUY",
"fillprice":"175.00",
"fillsize":"1",
"orderid":"201020000000095",
"fillid":"50005750",
"filltime":"13:27:53",
 }]
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
"/rest/secure/angelbroking/order/
v1/getTradeBook",
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
  rest/secure/angelbroking/order/
  v1/getTradeBook',
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
  rest/secure/angelbroking/order/
  v1/getTradeBook")
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
rest/secure/angelbroking/order/
v1/getTradeBook"
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
  rest/secure/angelbroking/order/v1/getTradeBook"
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

## Get LTP Data

#### Get LTP Data Request

```json
{
"exchange":"NSE",
"tradingsymbol":"SBIN-EQ"
"symboltoken":"3045"
}
```

#### Get LTP Data Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":{
"exchange":"NSE",
"tradingsymbol":"SBIN-EQ",
"symboltoken":"3045",
"open":"186",
"high":"191.25",
"low":"185",
"close":"187.80",
"ltp":"191",
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
    \"exchange\": \"NSE\",\n
    \"tradingsymbol\": \"SBIN-EQ\",\n
    \"symboltoken\":\"3045\"\n
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
v1/getLtpData",
payload,
headers
)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({
    "exchange":"NSE",
    "tradingsymbol":"SBIN-EQ",
    "symboltoken":"3045"
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
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
RequestBody body = RequestBody.create(mediaType, "{\n
        \"exchange\": \"NSE\",\n
        \"tradingsymbol\": \"SBIN-EQ\",\n
        \"symboltoken\":\"3045\"\n
    }");
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
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
rest/secure/angelbroking/order/
v1/getLtpData"

json_body <- jsonlite::toJSON(list(
    "exchange":"NSE",
    "tradingsymbol":"SBIN-EQ",
    "symboltoken":"3045"
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
  rest/secure/angelbroking/order/v1/getLtpData"
  method := "POST"

  payload := strings.NewReader({
    "exchange":"NSE",
    "tradingsymbol":"SBIN-EQ"
    "symboltoken":"3045"
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

## Individual Order Status

This API allows you to retrieve the status of individual orders using the "uniqueorderid" you receive in the response when placing, modifying, or canceling orders.

#### Individual Order Status Request

```
https://apiconnect.angelone.in/rest/secure/angelbroking/order/v1/details/05ebf91b-bea4-4a1d-b0f2-4259606570e3
```

#### Individual Order Status Response

```json
{
"status":true,
"message":"SUCCESS",
"errorcode":"",
"data":{
"variety":"NORMAL",
"ordertype":"LIMIT",
"producttype":"DELIVERY",
"duration":"DAY",
"price":2298.25,
"triggerprice":0,
"quantity":"1",
"disclosedquantity":"0",
"squareoff":0,
"stoploss":0,
"trailingstoploss":0,
"tradingsymbol":"RELIANCE-EQ",
"transactiontype":"BUY",
"exchange":"NSE",
"symboltoken":"2885",
"instrumenttype":"",
"strikeprice":-1,
"optiontype":"",
"expirydate":"",
"lotsize":"1",
"cancelsize":"0",
"averageprice":0,
"filledshares":"0",
"unfilledshares":"1",
"orderid":"231010000000970",
"text":"Your order has been rejected due to Insufficient Funds. Available funds - Rs. 937.00 . You require Rs. 2298.25 funds to execute this order.",
"status":"rejected",
"orderstatus":"rejected",
"updatetime":"10-Oct-2023 09:00:16",
"exchtime":"",
"exchorderupdatetime":"",
"fillid":"",
"filltime":"",
"parentorderid":"",
"ordertag":"",
"uniqueorderid":"05ebf91b-bea4-4a1d-b0f2-4259606570e3"
}
}
```

**NOTE:****Unique Order ID -** This identifier will be included in the response every time you interact with our APIs, whether you're placing an order, modifying it, canceling it, or checking your order book. This unique identifier simplifies the process of tracking and managing your orders with precision.

**Python**

```python
import http.client

conn = http.client.HTTPSConnection("apiconnect.angelone.in")

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

conn.request("GET", "/rest/secure/angelbroking/
order/v1/details/05ebf91b-bea4-4a1d-b0f2-4259606570e3", "", headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
 var axios = require('axios');

  var config = {
    method: 'get',
    url: "https://apiconnect.angelone.in/rest
    /secure/angelbroking/order/v1/details/05ebf91b-bea4-4a1d-b0f2-4259606570e3",
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
OkHttpClient client = new OkHttpClient().newBuilder().build();

Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/rest
  /secure/angelbroking/order/v1/details/05ebf91b-bea4-4a1d-b0f2-4259606570e3")
  .method("GET", null)
  .addHeader("X-PrivateKey", "API_KEY")
  .addHeader("Accept", "application/json")
  .addHeader("X-SourceID", "WEB")
  .addHeader("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  .addHeader("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  .addHeader("X-MACAddress", "MAC_ADDRESS")
  .addHeader("X-UserType", "USER")
  .addHeader("Authorization", "Bearer AUTHORIZATION_TOKEN")
  .build();

Response response = client.newCall(request).execute();
```

**R**

```r
library(httr)

url <- "https://apiconnect.angelone.in/
rest/secure/angelbroking/order/
v1/details/05ebf91b-bea4-4a1d-b0f2-4259606570e3"

response <- GET(url,
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
    rest/secure/angelbroking/order/
    v1/details/05ebf91b-bea4-4a1d-b0f2-4259606570e3"
   method := "GET"

   client := &http.Client {
   }
   req, err := http.NewRequest(method, url)

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
