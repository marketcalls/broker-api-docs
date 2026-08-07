# Order Management

> Source: <https://zebumyntapi.web.app/OAuth/Order/>

> **OAuth Authentication Required**
>
> All order management API requests require OAuth authentication. Include your Bearer Token in the Authorization header of each HTTP request.

## Overview

The Order Management APIs allow you to:
- **Place Orders**: Submit buy or sell orders for various instruments
- **Modify Orders**: Update existing order parameters like price, quantity, or type
- **Cancel Orders**: Revoke orders before execution
- **View Order Book**: Retrieve all active orders
- **Order History**: Get detailed history of specific orders
- **Trade Book**: View all executed trades

## Authentication

All API requests must include the OAuth access token in the Authorization header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Placing Orders

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}/NorenWClientAPI/PlaceOrder | Submits buy or sell orders for equity, derivatives, or commodities with support for various order types and product categories |

Request Details :

| Parameter Name | Type | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required order parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| actid |  | Account ID of the logged-in user |
| exch | NSE / NFO / BSE / MCX | Trading exchange identifier (select from enabled exchanges in user details) |
| tsym |  | Unique trading symbol identifier for the contract (URL encoding required for special characters) |
| qty |  | Order Quantity |
| prc |  | Order Price |
| trgprc |  | Only to be sent in case of SL-LMT / SL-MKT order. |
| dscqty |  | Disclosed quantity (Max 10% for NSE, and 50% for MCX) |
| prd | C / M / H | Product type identifier (select from enabled products for the chosen exchange) |
| trantype | B / S | B -> BUY, S -> SELL |
| prctyp | LMT / MKT /SL-LMT / SL-MKT / DS / 2L / 3L |  |
| mkt_protection |  | Market order protection percentage. Applicable only for MKT orders in BSE/BFO/BCS and MCX segments. |
| ret | DAY / EOS / IOC | Order retention type (varies by exchange rules) |
| remarks |  | Optional user-defined tag for order identification |
| ordersource | MOB / WEB / TT | Source identifier for exchange information generation |
| bpprc |  | Book Profit Price applicable only if product is selected as B (Bracket order ) |
| blprc |  | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc |  | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| usr_agent |  | User Agent |
| app_inst_id |  | App Install Id |
| amo |  | Yes , If not sent, of Not “Yes”, will be treated as Regular order. |
| tsym2 |  | Trading symbol for second leg (required for 2L and 3L price types, URL encoding required) |
| trantype2 |  | Transaction type of second leg, mandatory for price type 2L and 3L |
| qty2 |  | Quantity for second leg, mandatory for price type 2L and 3L |
| prc2 |  | Price for second leg, mandatory for price type 2L and 3L |
| tsym3 |  | Trading symbol for third leg (required for 3L price type, URL encoding required) |
| trantype3 |  | Transaction type of third leg, mandatory for price type 3L |
| qty3 |  | Quantity for third leg, mandatory for price type 3L |
| prc3 |  | Price for third leg, mandatory for price type 3L |
| ipaddr |  | global Ip of internet access |
| algo_id |  | Trading exchange identifier approved algo id |
| naic_code |  |  |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/PlaceOrder \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZP0XXXX","actid": "ZP0XXXX","exch": "NSE","tsym": "TCS-EQ","qty": "10","prctyp": "MKT","prc": "0","trantype": "B","prd": "I","ret": "DAY","dscqty": "0","mkt_protection": "2"}'
```

**Python**

```python
   import requests
   import json

   url = "https://go.mynt.in/NorenWClientAPI/PlaceOrder"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZP0XXXX",
    "actid": "ZP0XXXX",
    "exch": "NSE",
    "tsym": "TCS-EQ",
    "qty": "10",
    "prctyp": "MKT",
    "prc": "0",
    "trantype": "B",
    "prd": "I",
    "ret": "DAY",
    "dscqty": "0",
    "mkt_protection": "2"
}
payload = "jData=" + json.dumps(data)
response = requests.post(url, data=payload, headers=headers)
print(response.json())
```

**JavaScript**

```javascript
const data = {
    uid: "ZP0XXXX",
    actid: "ZP0XXXX",
    exch: "NSE",
    tsym: "TCS-EQ",
    qty: "10",
    prctyp: "MKT",
    prc: "0",
    trantype: "B",
    prd: "I",
    ret: "DAY",
    dscqty: "0",
    mkt_protection: "2"
};

fetch("https://go.mynt.in/NorenWClientAPI/PlaceOrder", {
    method: 'POST',
    headers: {
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    },
    body: "jData=" + JSON.stringify(data)
})
.then(response => response.json())
.then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**C#**

```csharp
using System;
using System.Net.Http;
using System.Text;
using Newtonsoft.Json;

class Program
{
    static void Main(string[] args)
    {
        var url = "https://go.mynt.in/NorenWClientAPI/PlaceOrder";
        var httpClient = new HttpClient();
        httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

        var jsonData = new {
            uid = "ZP0XXXX",
            actid = "ZP0XXXX",
            exch = "NSE",
            tsym = "TCS-EQ",
            qty = "10",
            prctyp = "MKT",
            prc = "0",
            trantype = "B",
            prd = "I",
            ret = "DAY",
            dscqty = "0",
            mkt_protection = "2"
        };
        var jsonString = JsonConvert.SerializeObject(jsonData);
        var payload = "jData=" + jsonString;

        var content = new StringContent(payload, Encoding.UTF8, "text/plain");
        var response = httpClient.PostAsync(url, content).Result;
        var responseString = response.Content.ReadAsStringAsync().Result;
        Console.WriteLine(responseString);
    }
}
```

**Java**

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.simple.JSONObject;

public class App {
  public static void main(String[] args) {
    try {
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/PlaceOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");
      JSONObject json = new JSONObject();
      json.put("uid","ZXX123N");
      json.put("actid","ZXX123N");
      json.put("exch","NSE");
      json.put("tsym":"TCS-EQ");
      json.put("qty","10");
      json.put("prctyp":"MKT");
      json.put("prc","0");
      json.put("trantype":"B");
      json.put("prd","I");
      json.put("ret":"DAY");
      json.put("dscqty":"0");
      json.put("mkt_protection","2");

      String payload = "jData=" + json.toString();
      OutputStream os = conn.getOutputStream();
      os.write(payload.getBytes());
      os.flush();

      BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));
      StringBuilder response = new StringBuilder();
      String output;
      while ((output = br.readLine()) != null) {
        response.append(output);
      }

      System.out.println(response.toString());

      conn.disconnect();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

**Go**

```go
package main

import (
"fmt"
"strings"
"net/http"
"io/ioutil"
)

func main() {

url := "https://go.mynt.in/NorenWClientAPI/PlaceOrder"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZP0XXXX","actid":"ZP0XXXX","exch":"NSE","tsym":"TCS-EQ","qty":"10","prctyp":"MKT","prc":"0","trantype":"B","prd":"I","ret":"DAY","dscqty":"0","mkt_protection":"2"}`)

client := &http.Client {
}
req, err := http.NewRequest(method, url, payload)

if err != nil {
fmt.Println(err)
return
}
req.Header.Add("Content-Type", "text/plain")
req.Header.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN")

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

**Response Details**

Response data will be in json format with below fields.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Place order success or failure indication. |
| request_time |  | Response received time. |
| norenordno |  | It will be present only on successful Order placement to OMS. |
| emsg |  | This will be present only if Order placement fails |

**Sample Success Response**

```json
{
  "request_time": "10:48:03 20-05-2020",
  "stat": "Ok",
  "norenordno": "24033000000002"
}
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired :  Invalid Session Key"
}
```

## Modifying Orders

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{Base URL}/NorenWClientAPI/ModifyOrder | Modifies existing pending orders by updating price, quantity, or order type while maintaining order priority and execution rules |

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required order parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| actid |  | Account ID of the logged-in user |
| exch |  | Trading exchange identifier |
| norenordno |  | Noren order number, which needs to be modified |
| prctyp | LMT / MKT / SL-MKT / SL-LMT | This can be modified. |
| prc |  | Modified / New price |
| qty |  | Modified / New Quantity<br>Quantity to Fill / Order Qty - This is the total qty to be filled for the order. Its Open Qty/Pending Qty plus Filled Shares (cumulative for the order) for the order. * Please do not send only the pending qty in this field |
| tsym |  | Unque id of contract on which order was placed. Can’t be modified, must be the same as that of original order. (use url encoding to avoid special char error for symbols like M&M) |
| ret | DAY / IOC / EOS | New Retention type of the order. |
| mkt_protection |  | Market order protection percentage. Applicable only for MKT orders in BSE/BFO/BCS and MCX segments. |
| trgprc |  | New trigger price in case of SL-MKT or SL-LMT |
| dscqty |  | Disclosed quantity (Max 10% for NSE, and 50% for MCX) |
| uid |  | User id of the logged in user. |
| usr_agent |  | User Agent |
| app_inst_id |  | App Install Id |
| bpprc |  | Book Profit Price applicable only if product is selected as B (Bracket order ) |
| blprc |  | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc |  | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ). |
| ipaddr |  | global Ip of internet access |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/ModifyOrder \
-H "Content-Type: text/plain" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-d 'jData={"uid": "ZP0XXXX","exch": "NSE","norenordno": "25100400000003","prctyp": "MKT","prc": "0","qty": "15","tsym": "TCS-EQ","ret": "DAY","mkt_protection": "2","dscqty": "0"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/ModifyOrder"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123N",
    "exch": "NSE",
    "norenordno": "29052024844658",
    "prctyp": "MKT",
    "prc": "0",
    "qty": "10",
    "tsym": "TCS-EQ",
    "ret": "DAY",
    "mkt_protection": "2",
    "dscqty": "0"
}
payload = "jData=" + json.dumps(data)
response = requests.post(url, data=payload, headers=headers)
print(response.text)
```

**JavaScript**

```javascript
const data = {
    uid: "ZXX123N",
    exch: "NSE",
    norenordno: "29052024844658",
    prctyp: "MKT",
    prc: "0",
    qty: "10",
    tsym: "TCS-EQ",
    ret: "DAY",
    mkt_protection: "2",
    dscqty: "0"
};

fetch("https://go.mynt.in/NorenWClientAPI/ModifyOrder", {
    method: 'POST',
    headers: {
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    },
    body: "jData=" + JSON.stringify(data)
})
.then(response => response.json())
.then(result => console.log(result))
.catch(error => console.log('error', error));
```

**C#**

```csharp
using System;
using System.Net.Http;
using Newtonsoft.Json;

class Program
{
static void Main(string[] args)
{
var url = "https://go.mynt.in/NorenWClientAPI/ModifyOrder";
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var jsonData = new {
    uid = "ZXX123N",
    exch = "NSE",
    norenordno = "29052024844658",
    prctyp = "MKT",
    prc = "0",
    qty = "10",
    tsym = "TCS-EQ",
    ret = "DAY",
    mkt_protection = "2",
    dscqty = "0"
};

var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData=" + jsonString;
        var content = new StringContent(payload, Encoding.UTF8, "text/plain");
var response = httpClient.PostAsync(url, content).Result;
var responseString = response.Content.ReadAsStringAsync().Result;
Console.WriteLine(responseString);
}
}
```

**Java**

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.simple.JSONObject;

public class App {
  public static void main(String[] args) {
    try {
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/ModifyOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid", "ZXX123N");
      json.put("exch", "NSE");
      json.put("norenordno", "24033000000002");
      json.put("tsym", "TCS-EQ");
      json.put("prctyp", "MKT");
      json.put("prc", "0");
      json.put("qty", "10");
      json.put("ret", "DAY");
      json.put("mkt_protection", "2");
      json.put("dscqty", "0");

      String payload = "jData=" + json.toString();
      OutputStream os = conn.getOutputStream();
      os.write(payload.getBytes());
      os.flush();

      BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));
      StringBuilder response = new StringBuilder();
      String output;
      while ((output = br.readLine()) != null) {
        response.append(output);
      }

      System.out.println(response.toString());

      conn.disconnect();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

**Go**

```go
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://go.mynt.in/NorenWClientAPI/ModifyOrder"
  method := "POST"

  // Create the JSON payload
  data := `{
    "uid": "ZXX123N",
    "exch": "NSE",
    "norenordno": "29052024844658",
    "prctyp": "MKT",
    "prc": "0",
    "qty": "10",
    "tsym": "TCS-EQ",
    "ret": "DAY",
    "mkt_protection": "2",
    "dscqty": "0"
  }`
  payload := "jData=" + strings.NewReader(data)

  client := &http.Client{}
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "text/plain")
  req.Header.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN")

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

**Response Details**

Response data will be in json format with below fields.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Modify order success or failure indication. |
| result |  | Noren Order number of the order modified. |
| request_time |  | Response received time. |
| emsg |  | This will be present only if Order modification fails |

**Sample Success Response**

```json
{
  "request_time": "14:14:08 26-05-2020",
  "stat": "Ok",
  "result": "XXXXXXXXXX"
}
```

**Sample Failure Response**

```json
{
  "request_time": "16:03:29 28-05-2020",
  "stat": "Not_Ok",
  "emsg": "Rejected : ORA:Order not found"
}
```

## Cancelling Orders

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{Base URL}/NorenWClientAPI/CancelOrder | Cancels pending orders before execution, providing immediate order termination with confirmation of cancellation status |

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required order parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User id of the logged in user. |
| norenordno |  | Noren order number |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/CancelOrder \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123N","norenordno": "24033000000002"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/CancelOrder"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123N",
    "norenordno": "24033000000002"
}

payload = "jData=" + json.dumps(data)
response = requests.post(url, data=payload, headers=headers)
print(response.text)
```

**JavaScript**

```javascript
const data = {
    uid: "ZXX123N",
    norenordno: "24033000000002"
};

fetch("https://go.mynt.in/NorenWClientAPI/CancelOrder", {
    method: 'POST',
    headers: {
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    },
    body: "jData=" + JSON.stringify(data)
})
.then(response => response.json())
.then(result => console.log(result))
.catch(error => console.log('error', error));
```

**C#**

```csharp
using System;
using System.Net.Http;
using Newtonsoft.Json;

class Program
{
static void Main(string[] args)
{
var url = "https://go.mynt.in/NorenWClientAPI/CancelOrder";
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var jsonData = new {
    uid = "ZXX123N",
    norenordno = "24033000000002"
};

var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData=" + jsonString;
        var content = new StringContent(payload, Encoding.UTF8, "text/plain");
var response = httpClient.PostAsync(url, content).Result;
var responseString = response.Content.ReadAsStringAsync().Result;
Console.WriteLine(responseString);
}
}
```

**Java**

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.simple.JSONObject;

public class App {
  public static void main(String[] args) {
    try {
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/CancelOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid", "ZXX123N");
      json.put("norenordno", "24033000000002");

      String payload = "jData=" + json.toString();
      OutputStream os = conn.getOutputStream();
      os.write(payload.getBytes());
      os.flush();

      BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));
      StringBuilder response = new StringBuilder();
      String output;
      while ((output = br.readLine()) != null) {
        response.append(output);
      }

      System.out.println(response.toString());

      conn.disconnect();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

**Go**

```go
package main

import (
"fmt"
"strings"
"net/http"
"io/ioutil"
)

func main() {

url := "https://go.mynt.in/NorenWClientAPI/CancelOrder"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N","norenordno":"24033000000002"}`)

client := &http.Client {
}
req, err := http.NewRequest(method, url, payload)

if err != nil {
fmt.Println(err)
return
}
req.Header.Add("Content-Type", "text/plain")
req.Header.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN")

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

**Response Details**

Response data will be in json format with below fields.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Cancel order success or failure indication. |
| result |  | Noren Order number of the canceled order. |
| request_time |  | Response received time. |
| emsg |  | This will be present only if Order cancelation fails |

**Sample Success Response**

```json
{
  "request_time": "14:14:10 26-05-2020",
  "stat": "Ok",
  "result": "XXXXXXXXXX"
}
```

**Sample Failure Response**

```json
{
  "request_time": "16:01:48 28-05-2020",
  "stat": "Not_Ok",
  "emsg": "Rejected : ORA:Order not found to Cancel"
}
```

## Order Book

| Method | APIs | Detail |
| --- | --- | --- |
| GET | https://{Base URL}/NorenWClientAPI/OrderBook | Retrieves comprehensive order book containing all pending buy and sell orders with real-time status and execution details |

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required order parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| prd | H / M / ... | Product name |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/OrderBook \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123N"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/OrderBook"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {"uid": "ZXX123N"}
payload = "jData=" + json.dumps(data)
response = requests.post(url, data=payload, headers=headers)
print(response.text)
```

**JavaScript**

```javascript
const data = {
    uid: "ZXX123N"
};

fetch("https://go.mynt.in/NorenWClientAPI/OrderBook", {
    method: 'POST',
    headers: {
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    },
    body: "jData=" + JSON.stringify(data)
})
.then(response => response.json())
.then(result => console.log(result))
.catch(error => console.log('error', error));
```

**C#**

```csharp
using System;
using System.Net.Http;
using Newtonsoft.Json;

class Program
{
static void Main(string[] args)
{
var url = "https://go.mynt.in/NorenWClientAPI/OrderBook";
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var jsonData = new {uid = "ZXX123N"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData=" + jsonString;
        var content = new StringContent(payload, Encoding.UTF8, "text/plain");
var response = httpClient.PostAsync(url, content).Result;
var responseString = response.Content.ReadAsStringAsync().Result;
Console.WriteLine(responseString);
}
}
```

**Java**

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.simple.JSONObject;

public class App {
  public static void main(String[] args) {
    try {
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/OrderBook");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid", "ZXX123N");

      String payload = "jData=" + json.toString();
      OutputStream os = conn.getOutputStream();
      os.write(payload.getBytes());
      os.flush();

      BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));
      StringBuilder response = new StringBuilder();
      String output;
      while ((output = br.readLine()) != null) {
        response.append(output);
      }

      System.out.println(response.toString());

      conn.disconnect();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

**Go**

```go
 package main

 import (
 "fmt"
 "strings"
 "net/http"
 "io/ioutil"
 )

 func main() {

 url := "https://go.mynt.in/NorenWClientAPI/OrderBook"
 method := "POST"

 payload := strings.NewReader(`jData={"uid":"ZXX123N"}`)

 client := &http.Client {
 }
 req, err := http.NewRequest(method, url, payload)

 if err != nil {
 fmt.Println(err)
return
}
req.Header.Add("Content-Type", "text/plain")
req.Header.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN")

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

**Response Details**

Response data will be in json Array of objects with below fields in case of success.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Order book success or failure indication. |
| uid |  | User Id |
| actid |  | Account ID |
| exch |  | Trading exchange identifier Segment |
| tsym |  | Trading symbol / contract on which order is placed. |
| norenordno |  | Noren Order Number |
| prc |  | Order Price |
| qty |  | Order Quantity |
| mkt_protection |  | Market Protection percentage |
| prd |  | Display product alias name, using prarr returned in user details. |
| status |  | Order status |
| trantype | B / S | Transaction type of the order |
| prctyp | LMT/MKT/SL-MKT/SL-LMT | Price type |
| fillshares |  | Total Traded Quantity of this order (will not be present if no trades for this order) |
| avgprc |  | Average trade price of total traded quantity (will not be present if no trades for this order) |
| rejreason |  | If order is rejected, reason in text form |
| exchordid |  | Trading exchange identifier Order Number |
| cancelqty |  | Canceled quantity for order which is in status cancelled. |
| remarks |  | Any message Entered during order entry. |
| dscqty |  | Order disclosed quantity. |
| trgprc |  | Order trigger price |
| ret | DAY / IOC / EOS | Order validity |
| bpprc |  | Book Profit Price applicable only if product is selected as B (Bracket order ) |
| blprc |  | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc |  | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| amo |  | Yes / No |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |
| token |  | Contract Token |
| norentm |  | Noren time stamp |
| ordenttm |  | Order entry time |
| exch_tm |  | Trading exchange identifier update time Format: dd-mm-YYYY hh:MM:SS |
| snoordt |  | 0 for profit leg and 1 for stoploss leg |
| snonum |  | This field will be present for product H and B; and only if it is profit/sl order. |
| prcftr |  | Contract price factor (GN*PN)/(GD*PD), (used for order value calculation)g |
| mult |  | Contract price multiplier, (used for order value calculation) |
| dname |  | Broker specific contract display name, present only if applicable. |
| rqty |  | To be used in get margin from modify window. |
| dname |  | Broker specific contract display name, present only if applicable. |
| rprc |  | To be used in get margin from modify window. |
| rtrgprc |  | To be used in get margin from modify window, for H/B products only |
| rblprc |  | To be used in get margin from modify window, for H/B products only |
| rorgqty |  | To be used in get margin from modify window. |
| rorgprc |  | To be used in get margin from modify window. |
| orgtrgprc |  | To be used in get margin from modify window, for H/B products only |
| rorgprc |  | To be used in get margin from modify window. |
| orgblprc |  | To be used in get margin from modify window, for H/B products only |

Failure Response Details

| Fields | Type | Description |
| --- | --- | --- |
| stat | Not_Ok | Order book failure indication. |
| request_time |  | Response received time. |
| emsg |  | Error message |

**Sample Success Response**

```json
[
  {
    "stat": "Ok",
    "exch": "NSE",
    "tsym": "ACC-EQ",
    "norenordno": "24033000000002",
    "prc": "127230",
    "qty": "100",
    "prd": "C",
    "status": "Open",
    "trantype": "B",
    "prctyp": "LMT",
    "fillshares": "0",
    "avgprc": "0",
    "exchordid": "250620000000343421",
    "uid": "ZXX123N",
    "actid": "ZXX123N",
    "ret": "DAY",
    "amo": "Yes"
  },
  {
    "stat": "Ok",
    "exch": "NSE",
    "tsym": "ABB-EQ",
    "norenordno": "24033000000002",
    "prc": "127830",
    "qty": "50",
    "prd": "C",
    "status": "REJECT",
    "trantype": "B",
    "prctyp": "LMT",
    "fillshares": "0",
    "avgprc": "0",
    "rejreason": "Insufficient funds",
    "uid": "ZXX123N",
    "actid": "ZXX123N",
    "ret": "DAY",
    "amo": "No"
  }
]
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired : Invalid Session Key"
}
```

## Order's history

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{Base URL}/NorenWClientAPI/SingleOrdHist | Retrieves detailed historical record of specific orders with complete lifecycle tracking from placement to execution or cancellation |

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required order parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User Id |
| norenordno |  | Noren Order Number |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/SingleOrdHist \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123N","norenordno": "25100400000003"}'
```

**Python**

```python
 import requests
 import json

 url = "https://go.mynt.in/NorenWClientAPI/SingleOrdHist"
 headers = {
     "Content-Type": "text/plain",
     "Authorization": "Bearer YOUR_ACCESS_TOKEN"
 }
 data = {
     "uid": "ZXX123N",
     "norenordno": "24033000000002"
 }
 payload = "jData=" + json.dumps(data)
response = requests.post(url, data=payload, headers=headers)
 print(response.text)
```

**JavaScript**

```javascript
const data = {
    uid: "ZXX123N",
    norenordno: "24033000000002"
};

fetch("https://go.mynt.in/NorenWClientAPI/SingleOrdHist", {
    method: 'POST',
    headers: {
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    },
    body: "jData=" + JSON.stringify(data)
})
.then(response => response.json())
.then(result => console.log(result))
.catch(error => console.log('error', error));
```

**C#**

```csharp
using System;
using System.Net.Http;
using Newtonsoft.Json;

class Program
{
static void Main(string[] args)
{
var url = "https://go.mynt.in/NorenWClientAPI/SingleOrdHist";
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var jsonData = new {
    uid = "ZXX123N",
    norenordno = "24033000000002"
};

var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData=" + jsonString;
        var content = new StringContent(payload, Encoding.UTF8, "text/plain");
var response = httpClient.PostAsync(url, content).Result;
var responseString = response.Content.ReadAsStringAsync().Result;
Console.WriteLine(responseString);
}
}
```

**Java**

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.simple.JSONObject;

public class App {
  public static void main(String[] args) {
    try {
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/SingleOrdHist");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid", "ZXX123N");
      json.put("norenordno", "24033000000002");

      String payload = "jData=" + json.toString();
      OutputStream os = conn.getOutputStream();
      os.write(payload.getBytes());
      os.flush();

      BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));
      StringBuilder response = new StringBuilder();
      String output;
      while ((output = br.readLine()) != null) {
        response.append(output);
      }

      System.out.println(response.toString());

      conn.disconnect();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

**Go**

```go
package main

import (
"fmt"
"strings"
"net/http"
"io/ioutil"
)

func main() {

url := "https://go.mynt.in/NorenWClientAPI/SingleOrdHist"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N","norenordno":"24033000000002"}`)

client := &http.Client {
}
req, err := http.NewRequest(method, url, payload)

if err != nil {
fmt.Println(err)
return
}
req.Header.Add("Content-Type", "text/plain")
req.Header.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN")

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

**Response Details**

Response data will be in json Array of objects with below fields in case of success.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Order book success or failure indication. |
| exch |  | Trading exchange identifier Segment |
| tsym |  | Trading symbol / contract on which order is placed. |
| norenordno |  | Noren Order Number |
| prc |  | Order Price |
| qty |  | Order Quantity |
| prd |  | Display product alias name, using prarr returned in user details. |
| status |  | Order status |
| rpt |  | Report Type (fill/complete etc) |
| trantype | B / S | Transaction type of the order |
| prctyp | LMT / MKT | Price type |
| fillshares |  | Total Traded Quantity of this orderr |
| avgprc |  | Average trade price of total traded quantity |
| rejreason |  | If order is rejected, reason in text form |
| exchordid |  | Trading exchange identifier Order Number |
| cancelqty |  | Canceled quantity for order which is in status cancelled. |
| remarks |  | Any message Entered during order entry |
| dscqty |  | Order disclosed quantity. |
| trgprc |  | Order trigger price |
| ret | DAY / IOC / EOS | Order validity |
| uid |  | User Id |
| actid |  | Account ID |
| bpprc |  | Book Profit Price applicable only if product is selected as B (Bracket order ) |
| blprc |  | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc |  | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| amo |  | Yes / No |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |
| token |  | Contract Token |
| norentm |  |  |
| ordenttm |  |  |
| exch_tm |  | Format: dd-mm-YYYY hh:MM:SS |

**Response Details**

| Fields | Type | Description |
| --- | --- | --- |
| stat | Not_Ok | Order book failure indication. |
| request_time |  | Response received time. |
| emsg |  | Error message |

**Sample Success Response**

```json
[
  {
    "stat": "Ok",
    "norenordno": "24033000000002",
    "uid": "ZXX123N",
    "actid": "ZXX123N",
    "exch": "NSE",
    "tsym": "ACCELYA-EQ",
    "qty": "180",
    "trantype": "B",
    "prctyp": "LMT",
    "ret": "DAY",
    "token": "7053",
    "pp": "2",
    "ls": "1",
    "ti": "0.05",
    "prc": "800.00",
    "avgprc": "800.00",
    "dscqty": "0",
    "prd": "M",
    "status": "COMPLETE",
    "rpt": "Fill",
    "fillshares": "180",
    "norentm": "19:59:32 13-12-2020",
    "exch_tm": "01-01-1980 00:00:00",
    "remarks": "WC TEST Order",
    "exchordid": "6858"
  },
  {
    "stat": "Ok",
    "norenordno": "24033000000002",
    "uid": "ZXX123N",
    "actid": "ZXX123N",
    "exch": "NSE",
    "tsym": "ACCELYA-EQ",
    "qty": "180",
    "trantype": "B",
    "prctyp": "LMT",
    "ret": "DAY",
    "token": "7053",
    "pp": "2",
    "ls": "1",
    "ti": "0.05",
    "prc": "800.00",
    "dscqty": "0",
    "prd": "M",
    "status": "OPEN",
    "rpt": "New",
    "norentm": "19:59:32 13-12-2020",
    "exch_tm": "01-01-1980 00:00:00",
    "remarks": "WC TEST Order",
    "exchordid": "6858"
  },
  {
    "stat": "Ok",
    "norenordno": "24033000000002",
    "uid": "ZXX123N",
    "actid": "ZXX123N",
    "exch": "NSE",
    "tsym": "ACCELYA-EQ",
    "qty": "180",
    "trantype": "B",
    "prctyp": "LMT",
    "ret": "DAY",
    "token": "7053",
    "pp": "2",
    "ls": "1",
    "ti": "0.05",
    "prc": "800.00",
    "dscqty": "0",
    "prd": "M",
    "status": "PENDING",
    "rpt": "PendingNew",
    "norentm": "19:59:32 13-12-2020",
    "remarks": "WC TEST Order"
  },
  {
    "stat": "Ok",
    "norenordno": "24033000000002",
    "uid": "ZXX123N",
    "actid": "ZXX123N",
    "exch": "NSE",
    "tsym": "ACCELYA-EQ",
    "qty": "180",
    "trantype": "B",
    "prctyp": "LMT",
    "ret": "DAY",
    "token": "7053",
    "pp": "2",
    "ls": "1",
    "ti": "0.05",
    "prc": "800.00",
    "prd": "M",
    "status": "PENDING",
    "rpt": "NewAck",
    "norentm": "19:59:32 13-12-2020",
    "remarks": "WC TEST Order"
  }
]
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired : Invalid Session Key"
}
```

## Trade Book

| Method | APIs | Detail |
| --- | --- | --- |
| GET | https://{Base URL}/NorenWClientAPI/TradeBook | Retrieves complete trade history with executed trade details including price, quantity, timestamp, and settlement information |

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required order parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User Id |
| actid |  | Account Id of logged in user |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/TradeBook \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123N","actid": "ZXX123N"}'
```

**Python**

```python
 import requests
 import json

 url = "https://go.mynt.in/NorenWClientAPI/TradeBook"
 headers = {
     "Content-Type": "text/plain",
     "Authorization": "Bearer YOUR_ACCESS_TOKEN"
 }
 data = {
     "uid": "ZXX123N",
     "actid": "ZXX123N"
 }
 payload = "jData=" + json.dumps(data)
response = requests.post(url, data=payload, headers=headers)
 print(response.text)
```

**JavaScript**

```javascript
const data = {
    uid: "ZXX123N",
    actid: "ZXX123N"
};

fetch("https://go.mynt.in/NorenWClientAPI/TradeBook", {
    method: 'POST',
    headers: {
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    },
    body: "jData=" + JSON.stringify(data)
})
.then(response => response.json())
.then(result => console.log(result))
.catch(error => console.log('error', error));
```

**C#**

```csharp
using System;
using System.Net.Http;
using Newtonsoft.Json;

class Program
{
static void Main(string[] args)
{
var url = "https://go.mynt.in/NorenWClientAPI/TradeBook";
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var jsonData = new {
    uid = "ZXX123N",
    actid = "ZXX123N"
};

var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData=" + jsonString;
        var content = new StringContent(payload, Encoding.UTF8, "text/plain");
var response = httpClient.PostAsync(url, content).Result;
var responseString = response.Content.ReadAsStringAsync().Result;
Console.WriteLine(responseString);
}
}
```

**Java**

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.simple.JSONObject;

public class App {
  public static void main(String[] args) {
    try {
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/TradeBook");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid", "ZXX123N");
      json.put("actid", "ZXX123N");

      String payload = "jData=" + json.toString();
      OutputStream os = conn.getOutputStream();
      os.write(payload.getBytes());
      os.flush();

      BufferedReader br = new BufferedReader(new InputStreamReader((conn.getInputStream())));
      StringBuilder response = new StringBuilder();
      String output;
      while ((output = br.readLine()) != null) {
        response.append(output);
      }

      System.out.println(response.toString());

      conn.disconnect();
    } catch (IOException e) {
      e.printStackTrace();
    }
  }
}
```

**Go**

```go
package main

import (
"fmt"
"strings"
"net/http"
"io/ioutil"
)

func main() {

url := "https://go.mynt.in/NorenWClientAPI/TradeBook"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N","actid":"ZXX123N"}`)

client := &http.Client {
}
req, err := http.NewRequest(method, url, payload)

if err != nil {
fmt.Println(err)
return
}
req.Header.Add("Content-Type", "text/plain")
req.Header.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN")

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

**Response Details**

Response data will be in json Array of objects with below fields in case of success.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Order book success or failure indication. |
| exch |  | Trading exchange identifier Segment |
| qty |  | Order Quantity |
| tsym |  | Trading symbol / contract on which order is placed. |
| norenordno |  | Noren Order Number |
| prd |  | Display product alias name, using prarr returned in user details. |
| trantype | B / S | Transaction type of the order |
| prctyp | LMT / MKT | Price type |
| fillshares |  | Total Traded Quantity of this order |
| exchordid |  | Trading exchange identifier Order Number |
| remarks |  | Any message Entered during order entry. |
| ret | DAY / IOC / EOS | Order validity |
| uid |  | User ID of the authenticated user |
| actid |  | Account ID of the logged-in user |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |
| cstFrm |  | Custom Firm |
| fltm |  | Fill Time |
| flid |  | Fill ID |
| flqty |  | Fill Qty |
| flprc |  | Fill Price |
| ordersource |  | Order Source |
| token |  | Token |
| norentm |  | Noren time stamp |
| exch_tm |  | Trading exchange identifier update time Format: dd-mm-YYYY hh:MM:SS |
| snoordt |  | 0 for profit leg and 1 for stoploss leg |
| snonum |  | This field will be present for product H and B; and only if it is profit/sl order. |

**Response Details**

| Fields | Type | Description |
| --- | --- | --- |
| stat | Not_Ok | Order book failure indication. |
| request_time |  | Response received time. |
| emsg |  | Error message |

**Sample Success Response**

```json
[
  {
    "stat": "Ok",
    "norenordno": "24033000000002",
    "uid": "ZXX123N",
    "actid": "ZXX123N",
    "exch": "NSE",
    "prctyp": "LMT",
    "ret": "DAY",
    "prd": "M",
    "flid": "102",
    "fltm": "01-01-1980 00:00:00",
    "trantype": "S",
    "tsym": "ACCELYA-EQ",
    "qty": "180",
    "token": "7053",
    "fillshares": "180",
    "flqty": "180",
    "pp": "2",
    "ls": "1",
    "ti": "0.05",
    "prc": "800.00",
    "flprc": "800.00",
    "norentm": "19:59:32 13-12-2020",
    "exch_tm": "01-01-1980 00:00:00",
    "remarks": "WC TEST Order",
    "exchordid": "6857"
  },
  {
    "stat": "Ok",
    "norenordno": "24033000000002",
    "uid": "ZXX123N",
    "actid": "ZXX123N",
    "exch": "NSE",
    "prctyp": "LMT",
    "ret": "DAY",
    "prd": "M",
    "flid": "101",
    "fltm": "01-01-1980 00:00:00",
    "trantype": "B",
    "tsym": "ACCELYA-EQ",
    "qty": "180",
    "token": "7053",
    "fillshares": "180",
    "flqty": "180",
    "pp": "2",
    "ls": "1",
    "ti": "0.05",
    "prc": "800.00",
    "flprc": "800.00",
    "norentm": "19:59:32 13-12-2020",
    "exch_tm": "01-01-1980 00:00:00",
    "remarks": "WC TEST Order",
    "exchordid": "6858"
  }
]
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired : Invalid Session Key"
}
```
