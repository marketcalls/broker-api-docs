# GTT Order

> Source: <https://zebumyntapi.web.app/OAuth/GTT%20Order/>

> **OAuth Authentication Required**
>
> All GTT (Good Till Triggered) order API requests require OAuth authentication. Include your Bearer Token in the Authorization header of each HTTP request.

## Overview

The GTT Order APIs provide access to Good Till Triggered order management functionalities including:
- **Place GTT Order**: Create new GTT orders with trigger conditions
- **Get Pending GTT Orders**: Retrieve all pending GTT orders
- **Get Enabled GTTs**: Get list of enabled GTT order types
- **Modify GTT Order**: Update existing GTT order parameters
- **Cancel GTT Order**: Cancel pending GTT orders

## Authentication

All API requests must include the OAuth access token in the Authorization header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Place GTTOrder

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{Base URL}/NorenWClientAPI/PlaceGTTOrder | Creates Good Till Triggered orders with conditional execution based on price triggers and target levels for automated trading |

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required GTT order parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| actid |  | Account ID of the logged-in user |
| exch | NSE / NFO / BSE / MCX | Trading exchange identifier (Select from ‘exarr’ Array provided in User Details response) |
| tsym |  | Unique trading symbol identifier for the contract (URL encoding required for special characters) |
| qty |  | Order Quantity |
| prc |  | Order Price |
| prd | C / M / H | Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call) |
| trantype | B / S | B -> BUY, S -> SELL |
| prctyp | LMT / MKT /SL-LMT / SL-MKT / DS / 2L / 3L |  |
| ret | DAY / EOS / IOC | Retention type (Show options as per allowed exchanges) |
| ai_t |  | Algo/Instruction type – defines trigger mechanism |
| validity |  | How long the order remains active |
| d |  | Trigger value/price – the price at which the GTT order activates |

**Example**

**cURL**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/PlaceGTTOrder \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123N","tsym": "RELIANCE-EQ","exch": "NSE","ai_t": "LTP_B_O","validity": "GTT","d": "12","trantype": "B","prctyp": "LMT","prd": "C","ret": "DAY","actid": "ZXX123N","qty": "1","prc": "146.4"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/PlaceGTTOrder"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123N",
    "tsym": "RELIANCE-EQ",
    "exch": "NSE",
    "ai_t": "LTP_B_O",
    "validity": "GTT",
    "d": "12",
    "trantype": "B",
    "prctyp": "LMT",
    "prd": "C",
    "ret": "DAY",
    "actid": "ZXX123N",
    "qty": "1",
    "prc": "146.4"
}
payload = "jData=" + json.dumps(data)
response = requests.post(url, data=payload, headers=headers)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");
myHeaders.append("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var data = {
  "uid": "ZXX123N",
  "tsym": "RELIANCE-EQ",
  "exch": "NSE",
  "ai_t": "LTP_B_O",
  "validity": "GTT",
  "d": "12",
  "trantype": "B",
  "prctyp": "LMT",
  "prd": "C",
  "ret": "DAY",
  "actid": "ZXX123N",
  "qty": "1",
  "prc": "146.4"
};

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
      body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/PlaceGTTOrder", requestOptions)
  .then(response => response.text())
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
var url = "https://go.mynt.in/NorenWClientAPI/PlaceGTTOrder";
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var jsonData = new {
  uid = "ZXX123N",
  tsym = "RELIANCE-EQ",
  actid = "ZXX123N",
  exch = "NSE",
  ai_t = "LTP_B_O",
  qty = "1",
  validity = "GTT",
  d = "12",
  trantype = "B",
  prc = "146.4",
  prd = "C",
  prctyp = "LMT",
  ret = "DAY"
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/PlaceGTTOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid","ZXX123N");
      json.put("tsym","RELIANCE-EQ");
      json.put("exch","NSE");
      json.put("ai_t","LTP_B_O");
      json.put("validity", "GTT");
      json.put("d","12");
      json.put("trantype","B");
      json.put("prctyp","LMT");
      json.put("prd","C");
      json.put("ret","DAY");
      json.put("actid","ZXX123N");
      json.put("qty","1");
      json.put("prc","146.4");

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
  "bytes"
  "encoding/json"
  "fmt"
  "io/ioutil"
  "net/http"
)

func main() {
  url := "https://go.mynt.in/NorenWClientAPI/PlaceGTTOrder"

  data := map[string]interface{}{
    "uid":      "ZXX123N",
    "tsym":     "RELIANCE-EQ",
    "exch":     "NSE",
    "ai_t":     "LTP_B_O",
    "validity": "GTT",
    "d":        "12",
    "trantype": "B",
    "prctyp":   "LMT",
    "prd":      "C",
    "ret":      "DAY",
    "actid":    "ZXX123N",
    "qty":      "1",
    "prc":      "146.4",
  }

  jsonData, _ := json.Marshal(data)
  payload := "jData=" + string(jsonData)
  req, err := http.NewRequest("POST", url, bytes.NewBufferString(payload))
  if err != nil {
    fmt.Println(err)
    return
  }

  req.Header.Set("Content-Type", "text/plain")
  req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

  client := &http.Client{}
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
| stat | Ok or Not_Ok | PlaceGTTOrder success or failure indication. |
| request_time |  | Response received time. |
| emsg |  | This will be present only if PlaceGTTOrder fails |

**Sample Success Response**

```json
{
  "request_time": "11:07:57 05-04-2023",
  "stat": "OI created",
  "al_id": "XXXXXXXXXX"
}
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired :  Invalid User Id"
}
```

## Get Pending GTTOrder

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{Base URL}/NorenWClientAPI/GetPendingGTTOrder | Retrieves all pending GTT orders with current status, trigger conditions, and execution details for monitoring |

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required GTT order parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |

**Example**

**cURL**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/GetPendingGTTOrder \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123N"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/GetPendingGTTOrder"
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
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");
myHeaders.append("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var data = {"uid": "ZXX123N"};
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
      body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};
fetch("https://go.mynt.in/NorenWClientAPI/GetPendingGTTOrder", requestOptions)
  .then(response => response.text())
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
var url = "https://go.mynt.in/NorenWClientAPI/GetPendingGTTOrder";
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/GetPendingGTTOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid","ZXX123N");

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
  "bytes"
  "encoding/json"
  "fmt"
  "io/ioutil"
  "net/http"
)

func main() {
  url := "https://go.mynt.in/NorenWClientAPI/GetPendingGTTOrder"

  data := map[string]interface{}{
    "uid": "ZXX123N",
  }

  jsonData, _ := json.Marshal(data)
  payload := "jData=" + string(jsonData)
  req, err := http.NewRequest("POST", url, bytes.NewBufferString(payload))
  if err != nil {
    fmt.Println(err)
    return
  }

  req.Header.Set("Content-Type", "text/plain")
  req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

  client := &http.Client{}
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
| stat | Ok or Not_Ok | stat Ok or Not_Ok Limits request success or failure indication. |
| emsg |  | This will be present only in a failure response. |

**Sample Success Response**

```json
[
  {
    "stat": "Ok",
    "ai_t": "XXXXX",
    "al_id": "XXX",
    "tsym": "XXXX-EQ",
    "exch": "NSE",
    "token": "C",
    "remarks": "",
    "validity": "V",
    "norentm": "XXXXX",
    "pp": "XXX",
    "ls": "XXX",
    "ti": "0.05",
    "brkname": "XXXXX",
    "actid": "XXXXXXXXX",
    "trantype": "XXX",
    "prctyp": "XX",
    "qty": 1,
    "prc": "XXXX",
    "C": "XXX",
    "prd": "C",
    "ordersource": "XXX",
    "place_order_params": {
      "actid": "XXXXX",
      "trantype": "XXX",
      "prctyp": "XXXX",
      "qty": 1,
      "prc": "XXXX",
      "C": "XXXX",
      "s_prdt_ali": "XXXXXXXXX",
      "prd": "XXXXXXXXX",
      "ordersource": "XXXXXXX",
      "ipaddr": "XXXXS"
    },
    "d": "",
    "oivariable": [
      {
        "var_name": "x",
        "d": "XXX"
      }
    ]
  }
]
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired :  User Id "
}
```

## Get Enabled GTTs

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{Base URL}/NorenWClientAPI/GetEnabledGTTs | Retrieves all enabled GTT orders that are actively monitoring market conditions for trigger execution |

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required GTT order parameters |

| Fields | Possible value | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |

**Example**

**cURL**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/GetEnabledGTTs \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123N"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/GetEnabledGTTs"
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
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");
myHeaders.append("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var data = {"uid": "ZXX123N"};
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
      body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};
fetch("https://go.mynt.in/NorenWClientAPI/GetEnabledGTTs", requestOptions)
  .then(response => response.text())
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
var url = "https://go.mynt.in/NorenWClientAPI/GetEnabledGTTs";
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/GetEnabledGTTs");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid","ZXX123N");

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
  "bytes"
  "encoding/json"
  "fmt"
  "io/ioutil"
  "net/http"
)

func main() {
  url := "https://go.mynt.in/NorenWClientAPI/GetEnabledGTTs"

  data := map[string]interface{}{
    "uid": "ZXX123N",
  }

  jsonData, _ := json.Marshal(data)
  payload := "jData=" + string(jsonData)
  req, err := http.NewRequest("POST", url, bytes.NewBufferString(payload))
  if err != nil {
    fmt.Println(err)
    return
  }

  req.Header.Set("Content-Type", "text/plain")
  req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

  client := &http.Client{}
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
| emsg |  | This will be present only if Order placement fails |

**Sample Success Response**

```json
{
  "stat": "Ok",
  "request_time": "05042023150257",
  "ai_ts": []
}
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired :  Invalid User Id"
}
```

## Modify GTTOrder

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{Base URL}/NorenWClientAPI/ModifyGTTOrder | Modifies existing GTT orders by updating trigger prices, quantities, and target levels before execution |

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required GTT order parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| tsym |  | Unique trading symbol identifier for the contract (URL encoding required for special characters) |
| exch | NSE / NFO / BSE / MCX | Trading exchange identifier (Select from ‘exarr’ Array provided in User Details response) |
| ai_t |  |  |
| validity |  |  |
| al_id |  |  |
| d |  |  |
| trantype | B / S | B -> BUY, S -> SELL |
| prctyp | LMT / MKT /SL-LMT / SL-MKT / DS / 2L / 3L |  |
| prd | C / M / H | Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call) |
| ret | DAY / EOS / IOC | Retention type (Show options as per allowed exchanges) |
| actid |  | Account ID of the logged-in user |
| qty |  | Order Quantity |
| prc |  | Order Price |

**Example**

**cURL**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/ModifyGTTOrder \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123N","tsym": "PGINVIT","exch": "BSE","ai_t": "LTP_B_O","validity": "GTT","al_id": "24032700000188","d": "11","trantype": "B","prctyp": "MKT","prd": "C","ret": "DAY","actid": "ZXX123N","qty": "1","prc": "0"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/ModifyGTTOrder"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123N",
    "tsym": "PGINVIT",
    "exch": "BSE",
    "ai_t": "LTP_B_O",
    "validity": "GTT",
    "al_id": "24032700000188",
    "d": "11",
    "trantype": "B",
    "prctyp": "MKT",
    "prd": "C",
    "ret": "DAY",
    "actid": "ZXX123N",
    "qty": "1",
    "prc": "0"
}
payload = "jData=" + json.dumps(data)
response = requests.post(url, data=payload, headers=headers)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");
myHeaders.append("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var data = {
  "uid": "ZXX123N",
  "tsym": "PGINVIT",
  "exch": "BSE",
  "ai_t": "LTP_B_O",
  "validity": "GTT",
  "al_id": "24032700000188",
  "d": "11",
  "trantype": "B",
  "prctyp": "MKT",
  "prd": "C",
  "ret": "DAY",
  "actid": "ZXX123N",
  "qty": "1",
  "prc": "0"
};

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
      body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/ModifyGTTOrder", requestOptions)
  .then(response => response.text())
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
var url = "https://go.mynt.in/NorenWClientAPI/ModifyGTTOrder";
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var jsonData = new {
  uid = "ZXX123N",
  actid = "ZXX123N",
  tsym = "PGINVIT",
  exch = "BSE",
  ai_t = "LTP_B_O",
  validity = "GTT",
  al_id = "24032700000188",
  d = "11",
  trantype = "B",
  prctyp = "MKT",
  prd = "C",
  ret = "DAY",
  qty = "1",
  prc = "0"
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/ModifyGTTOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid","ZXX123N");
      json.put("tsym","PGINVIT");
      json.put("exch","BSE");
      json.put("ai_t","LTP_B_O");
      json.put("validity", "GTT");
      json.put("d","11");
      json.put("trantype","B");
      json.put("prctyp","MKT");
      json.put("prd","C");
      json.put("ret","DAY");
      json.put("actid","ZXX123N");
      json.put("qty","1");
      json.put("prc","0");
      json.put("al_id","24032700000188");

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
  "bytes"
  "encoding/json"
  "fmt"
  "io/ioutil"
  "net/http"
)

func main() {
  url := "https://go.mynt.in/NorenWClientAPI/ModifyGTTOrder"

  data := map[string]interface{}{
    "uid":      "ZXX123N",
    "tsym":     "PGINVIT",
    "exch":     "BSE",
    "ai_t":     "LTP_B_O",
    "validity": "GTT",
    "al_id":    "24032700000188",
    "d":        "11",
    "trantype": "B",
    "prctyp":   "MKT",
    "prd":      "C",
    "ret":      "DAY",
    "actid":    "ZXX123N",
    "qty":      "1",
    "prc":      "0",
  }

  jsonData, _ := json.Marshal(data)
  payload := "jData=" + string(jsonData)
  req, err := http.NewRequest("POST", url, bytes.NewBufferString(payload))
  if err != nil {
    fmt.Println(err)
    return
  }

  req.Header.Set("Content-Type", "text/plain")
  req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

  client := &http.Client{}
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
| stat | Ok or Not_Ok | Login Success Or failure status. |
| request_time |  | Response received time. |
| emsg |  | This will be present only in a failure response. |

**Sample Success Response**

```json
{
  "request_time": "XXXXXXXX",
  "stat": "Invalid Oi",
  "al_id": "XXXX"
}
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired :  Invalid User Id"
}
```

## Cancel GTTOrder

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{Base URL}/NorenWClientAPI/CancelGTTOrder | Cancels active GTT orders before trigger execution, providing immediate termination with confirmation status |

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required GTT order parameters |

| Fields | Possible value | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| al_id |  |  |

**Example**

**cURL**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/CancelGTTOrder \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123N","al_id": "24040300000211"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/CancelGTTOrder"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123N",
    "al_id": "24040300000211"
}
payload = "jData=" + json.dumps(data)
response = requests.post(url, data=payload, headers=headers)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");
myHeaders.append("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var data = {
  "uid": "ZXX123N",
  "al_id": "24040300000211"
};

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
      body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/CancelGTTOrder", requestOptions)
  .then(response => response.text())
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
var url = "https://go.mynt.in/NorenWClientAPI/CancelGTTOrder";
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var jsonData = new {
  uid = "ZXX123N",
  al_id = "24040300000211"
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/CancelGTTOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid","ZXX123N");
      json.put("al_id","24040300000211");

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
  "bytes"
  "encoding/json"
  "fmt"
  "io/ioutil"
  "net/http"
)

func main() {
  url := "https://go.mynt.in/NorenWClientAPI/CancelGTTOrder"

  data := map[string]interface{}{
    "uid":   "ZXX123N",
    "al_id": "24040300000211",
  }

  jsonData, _ := json.Marshal(data)
  payload := "jData=" + string(jsonData)
  req, err := http.NewRequest("POST", url, bytes.NewBufferString(payload))
  if err != nil {
    fmt.Println(err)
    return
  }

  req.Header.Set("Content-Type", "text/plain")
  req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

  client := &http.Client{}
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
| stat | Ok or Not_Ok | Login Success Or failure status. |
| request_time |  | Response received time. |
| emsg |  | This will be present only in a failure response. |

**Sample Success Response**

```json
{
  "request_time": "16:51:42 03-04-2022",
  "stat": "OI deleted",
  "al_id": "24040300000211"
}
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired :  Invalid User Id"
}
```
