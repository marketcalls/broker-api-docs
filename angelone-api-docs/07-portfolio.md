<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Portfolio -->

# Portfolio

A portfolio is a collection of financial investments like stocks, bonds, commodities, cash, and cash equivalents, including long-term equity holdings and short-term positions. The portfolio APIs return instruments in a portfolio with updated profit and loss computations.

| Request Type | APIs | Endpoint | Description |
| --- | --- | --- | --- |
| GET | Get Holding | https://apiconnect.angelone.in/rest/secure/angelbroking/portfolio/v1/getHolding | To retrieve holding |
| GET | Get All Holding | https://apiconnect.angelone.in/rest/secure/angelbroking/portfolio/v1/getAllHolding | To retrieve all holding |
| GET | Get Position | https://apiconnect.angelone.in/rest/secure/angelbroking/order/v1/getPosition | To retrieve positIon |
| POST | Convert Position | https://apiconnect.angelone.in/rest/secure/angelbroking/order/v1/convertPosition | To convert position |

## Get Holdings

Holdings comprises of the user's portfolio of long-term equity delivery stocks. An instrument in a holding's portfolio remains there indefinitely until its sold or is delisted or changed by the exchanges. Underneath it all, instruments in the holdings reside in the user's DEMAT account, as settled by exchanges and clearing institutions.

#### Get Holding Response

```json
{
"tradingsymbol": "TATASTEEL-EQ",
"exchange": "NSE",
"isin": "INE081A01020",
"t1quantity": 0,
"realisedquantity": 2,
"quantity": 2,
"authorisedquantity": 0,
"product": "DELIVERY",
"collateralquantity": null,
"collateraltype": null,
"haircut": 0,
"averageprice": 111.87,
"ltp": 130.15,
"symboltoken": "3499",
"close": 129.6,
"profitandloss": 37,
"pnlpercentage": 16.34
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
"/rest/secure/angelbroking/portfolio/
v1/getHolding",
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
  rest/secure/angelbroking/portfolio/
  v1/getHolding',

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
  rest/secure/angelbroking/portfolio/
  v1/getHolding")

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
rest/secure/angelbroking/portfolio/
v1/getHolding"

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
  rest/secure/angelbroking/portfolio/v1/getHolding"
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

## Get All Holdings

This endpoint offers a more comprehensive view of your entire investments, including individual stock holdings and a summary of your total investments. In addition to the updates for individual stock holdings, we have introduced a new section in the response called "totalholding," which provides a summary of your entire investments, including:

- totalholdingvalue: The total value of all your holdings.
- totalinvvalue: The total investment value.
- totalprofitandloss: The total profit and loss across all holdings.
- totalpnlpercentage: The total profit and loss percentage for your entire portfolio.

#### Get Holding Response

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": {
"holdings": [
{
"tradingsymbol": "TATASTEEL-EQ",
"exchange": "NSE",
"isin": "INE081A01020",
"t1quantity": 0,
"realisedquantity": 2,
"quantity": 2,
"authorisedquantity": 0,
"product": "DELIVERY",
"collateralquantity": null,
"collateraltype": null,
"haircut": 0,
"averageprice": 111.87,
"ltp": 130.15,
"symboltoken": "3499",
"close": 129.6,
"profitandloss": 37,
"pnlpercentage": 16.34
},
{
"tradingsymbol": "PARAGMILK-EQ",
"exchange": "NSE",
"isin": "INE883N01014",
"t1quantity": 0,
"realisedquantity": 2,
"quantity": 2,
"authorisedquantity": 0,
"product": "DELIVERY",
"collateralquantity": null,
"collateraltype": null,
"haircut": 0,
"averageprice": 154.03,
"ltp": 201,
"symboltoken": "17130",
"close": 192.1,
"profitandloss": 94,
"pnlpercentage": 30.49
},
{
"tradingsymbol": "SBIN-EQ",
"exchange": "NSE",
"isin": "INE062A01020",
"t1quantity": 0,
"realisedquantity": 8,
"quantity": 8,
"authorisedquantity": 0,
"product": "DELIVERY",
"collateralquantity": null,
"collateraltype": null,
"haircut": 0,
"averageprice": 573.1,
"ltp": 579.05,
"symboltoken": "3045",
"close": 570.5,
"profitandloss": 48,
"pnlpercentage": 1.04
}
],
"totalholding": {
"totalholdingvalue": 5294,
"totalinvvalue": 5116,
"totalprofitandloss": 178.14,
"totalpnlpercentage": 3.48
}
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
"/rest/secure/angelbroking/portfolio/v1/getAllHolding",
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
  rest/secure/angelbroking/portfolio/v1/getAllHolding',

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
  rest/secure/angelbroking/portfolio/v1/getAllHolding")

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
rest/secure/angelbroking/portfolio/v1/getAllHolding"

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
  rest/secure/angelbroking/portfolio/v1/getAllHolding"
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

## Get Position

This API returns two sets of positions, net and day. net is the actual, current net position portfolio, while day is a snapshot of the buying and selling activity for that particular day.

#### Get Position Response

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data":[
{
"exchange": "NSE",
"symboltoken": "2885",
"producttype": "DELIVERY",
"tradingsymbol": "RELIANCE-EQ",
"symbolname": "RELIANCE",
"instrumenttype": "",
"priceden": "1",
"pricenum": "1",
"genden": "1",
"gennum": "1",
"precision": "2",
"multiplier": "-1",
"boardlotsize": "1",
"buyqty": "1",
"sellqty": "0",
"buyamount": "2235.80",
"sellamount": "0",
"symbolgroup": "EQ",
"strikeprice": "-1",
"optiontype": "",
"expirydate": "",
"lotsize": "1",
"cfbuyqty": "0",
"cfsellqty": "0",
"cfbuyamount": "0",
"cfsellamount": "0",
"buyavgprice": "2235.80",
"sellavgprice": "0",
"avgnetprice": "2235.80",
"netvalue": "- 2235.80",
"netqty": "1",
"totalbuyvalue": "2235.80",
"totalsellvalue": "0",
"cfbuyavgprice": "0",
"cfsellavgprice": "0",
"totalbuyavgprice": "2235.80",
"totalsellavgprice": "0",
"netprice": "2235.80"
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
"/rest/secure/angelbroking/order/
v1/getPosition",
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
  v1/getPosition',

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
  v1/getPosition")

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
v1/getPosition"

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
  rest/secure/angelbroking/order/v1/getPosition"
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

## Convert Position

Each position has one margin product. These products affect how the user's margin usage and free cash values are computed, and a user may wish to convert or change a position's margin product on timely basis.

#### Position Conversion Request

```json
{
"exchange": "NSE",
"symboltoken": "2885",
"oldproducttype": "DELIVERY",
"newproducttype": "INTRADAY",
"tradingsymbol": "RELIANCE-EQ",
"symbolname": "RELIANCE",
"instrumenttype": "",
"priceden": "1",
"pricenum": "1",
"genden": "1",
"gennum": "1",
"precision": "2",
"multiplier": "-1",
"boardlotsize": "1",
"buyqty": "1",
"sellqty": "0",
"buyamount": "2235.80",
"sellamount": "0",
"transactiontype": "BUY",
"quantity": 1,
"type": "DAY"
}
```

#### Position Conversion Response

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": null
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
    \"exchange\": \"NSE\",\n
    \"symboltoken\": \"2885\",\n
    \"oldproducttype\": \"DELIVERY\",\n
    \"newproducttype\": \"INTRADAY\",\n
    \"tradingsymbol\": \"RELIANCE-EQ\",\n
    \"symbolname\": \"RELIANCE\",\n
    \"instrumenttype\": \"\",\n
    \"priceden\": \"1\",\n
    \"pricenum\": \"1\",\n
    \"genden\": \"1\",\n
    \"gennum\": \"1\",\n
    \"precision\": \"2\",\n
    \"multiplier\": \"-1\",\n
    \"boardlotsize\": \"1\",\n
    \"buyqty\": \"1\",\n
    \"sellqty\": \"0\",\n
    \"buyamount\": \"2235.80\",\n
    \"sellamount\": \"0\",\n
    \"transactiontype\": \"BUY\",\n
    \"quantity\": 1,\n
    \"type\": \"DAY\"\n
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
 v1/convertPosition",
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
    "symboltoken":"2885",
    "oldproducttype":"DELIVERY",
    "newproducttype":"INTRADAY",
    "tradingsymbol":"RELIANCE-EQ",
    "symbolname":"RELIANCE",
    "instrumenttype":"",
    "priceden":"1",
    "pricenum":"1",
    "genden":"1",
    "gennum":"1",
    "precision":"2",
    "multiplier":"-1",
    "boardlotsize":"1",
    "buyqty":"1",
    "sellqty":"0",
    "buyamount":"2235.80",
    "sellamount":"0",
    "transactiontype":"BUY",
    "quantity":1,
    "type":"DAY"
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/convertPosition',
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
    \"exchange\": \"NSE\",\n
    \"symboltoken\": \"2885\",\n
    \"oldproducttype\": \"DELIVERY\",\n
    \"newproducttype\": \"INTRADAY\",\n
    \"tradingsymbol\": \"RELIANCE-EQ\",\n
    \"symbolname\": \"RELIANCE\",\n
    \"instrumenttype\": \"\",\n
    \"priceden\": \"1\",\n
    \"pricenum\": \"1\",\n
    \"genden\": \"1\",\n
    \"gennum\": \"1\",\n
    \"precision\": \"2\",\n
    \"multiplier\": \"-1\",\n
    \"boardlotsize\": \"1\",\n
    \"buyqty\": \"1\",\n
    \"sellqty\": \"0\",\n
    \"buyamount\": \"2235.80\",\n
    \"sellamount\": \"0\",\n
    \"transactiontype\": \"BUY\",\n
    \"quantity\": 1,\n
    \"type\": \"DAY\"\n
}");
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/
  rest/secure/angelbroking/order/
  v1/convertPosition")

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
v1/convertPosition"
json_body <- jsonlite::toJSON(list(
    "exchange":"NSE",
    "symboltoken":"2885",
    "oldproducttype":"DELIVERY",
    "newproducttype":"INTRADAY",
    "tradingsymbol":"RELIANCE-EQ",
    "symbolname":"RELIANCE",
    "instrumenttype":"",
    "priceden":"1",
    "pricenum":"1",
    "genden":"1",
    "gennum":"1",
    "precision":"2",
    "multiplier":"-1",
    "boardlotsize":"1",
    "buyqty":"1",
    "sellqty":"0",
    "buyamount":"2235.80",
    "sellamount":"0",
    "transactiontype":"BUY",
    "quantity":1,
    "type":"DAY"
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
  rest/secure/angelbroking/order/v1/convertPosition"
  method := "POST"

  payload := strings.NewReader({
    "exchange":"NSE",
    "symboltoken":"2885",
    "oldproducttype":"DELIVERY",
    "newproducttype":"INTRADAY",
    "tradingsymbol":"RELIANCE-EQ",
    "symbolname":"RELIANCE",
    "instrumenttype":"",
    "priceden":"1",
    "pricenum":"1",
    "genden":"1",
    "gennum":"1",
    "precision":"2",
    "multiplier":"-1",
    "boardlotsize":"1",
    "buyqty":"1",
    "sellqty":"0",
    "buyamount":"2235.80",
    "sellamount":"0",
    "transactiontype":"BUY",
    "quantity":1,
    "type":"DAY"
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
