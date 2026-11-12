# Portfolio

> Source: <https://zebumyntapi.web.app/OAuth/Portfolio/>

> **OAuth Authentication Required**
>
> All portfolio management API requests require OAuth authentication. Include your Bearer Token in the Authorization header of each HTTP request.

## Overview

The Portfolio APIs provide access to portfolio management functionalities including:
- **Holdings**: Retrieve long-term equity holdings and their details
- **Positions Book**: Get all open positions for the day including F&O carryforward positions
- **Product Conversion**: Convert positions from intraday to delivery or vice versa
- **Close Position**: Close open positions entirely or partially

## Authentication

All API requests must include the OAuth access token in the Authorization header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Holdings

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}/NorenWClientAPI/Holdings | Retrieves comprehensive equity holdings portfolio with current values, P&L, and product type details (CNC/MTF) |

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required portfolio parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| actid |  | Account id of the logged in user. |
| prd |  | Product name |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/Holdings \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123M","actid": "ZXX123M","prd": "C"}'
```

**Python**

```python
  import requests
  import json

  url = "https://go.mynt.in/NorenWClientAPI/Holdings"
  headers = {
      "Content-Type": "text/plain",
      "Authorization": "Bearer YOUR_ACCESS_TOKEN"
  }
  data = {
      "uid": "ZXX123M",
      "actid": "ZXX123M",
      "prd": "C"
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

var data = {"uid":"ZXX123M","actid":"ZXX123M","prd":"C"};
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/Holdings", requestOptions)
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
        var url = "https://go.mynt.in/NorenWClientAPI/Holdings";
        var httpClient = new HttpClient();
        httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

        var jsonData = new {
            uid = "ZXX123M",
            actid = "ZXX123M",
            prd = "C"
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
            URL url = new URL("https://go.mynt.in/NorenWClientAPI/Holdings");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "text/plain");
            conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

            JSONObject json = new JSONObject();
            json.put("uid", "ZXX123M");
            json.put("actid", "ZXX123M");
            json.put("prd", "C");

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
    url := "https://go.mynt.in/NorenWClientAPI/Holdings"

    data := map[string]interface{}{
        "uid": "ZXX123M",
        "actid": "ZXX123M",
        "prd": "C",
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

    body, _ := ioutil.ReadAll(res.Body)
    fmt.Println(string(body))
}
```

**Response Details**

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Holding request success or failure indication. |
| exch_tsym |  | Array of objects exch_tsym objects as defined below. |
| holdqty |  | Holding quantity |
| dpqty |  | DP Holding quantity |
| npoadqty |  | Non Poa display quantity |
| colqty |  | Collateral quantity |
| benqty |  | Beneficiary quantity |
| unplgdqty |  | Unpledged quantity |
| brkcolqty |  | Broker Collateral |
| btstqty |  | BTST quantity |
| btstcolqty |  | BTST Collateral quantity |
| usedqty |  | Holding used today |
| upldprc |  | Average price uploaded along with holdings |
| hair_cut |  | Hair Cut |

Notes:

```
Valuation : btstqty + holdqty + brkcolqty + unplgdqty + benqty + Max(npoadqty, dpqty) - usedqty
Salable: btstqty + holdqty + unplgdqty + benqty + dpqty - usedqty
```

Exch_tsym object:

| Fields | Type | Description |
| --- | --- | --- |
| exch | NSE, BSE, NFO ... | Trading exchange identifier |
| tsym |  | Unique trading symbol identifier for the contract |
| token |  | Unique identifier for the trading contract |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |

**Response Details**

| Fields | Type | Description |
| --- | --- | --- |
| stat | Not_Ok | Position book request failure indication. |
| request_time |  | Response received time. |
| emsg |  | Error message |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |

**Sample Success Response**

```json
[
  {
    "stat": "Ok",
    "exch_tsym": [
      {
        "exch": "NSE",
        "token": "2885",
        "tsym": "ABB-EQ"
      }
    ],
    "holdqty": "2000000",
    "colqty": "200",
    "btstqty": "0",
    "btstcolqty": "0",
    "usedqty": "0",
    "upldprc": "1800.00"
  },
  {
    "stat": "Ok",
    "exch_tsym": [
      {
        "exch": "NSE",
        "token": "2885",
        "tsym": "ACC-EQ"
      }
    ],
    "holdqty": "2000000",
    "colqty": "200",
    "btstqty": "0",
    "btstcolqty": "0",
    "usedqty": "0",
    "upldprc": "1400.00"
      }
    ]
```

**Sample Failure Response**

```json
          {
"stat": "Not_Ok",
"emsg": "Invalid Input : Missing uid or actid or prd."
          }
```

## Positions Book

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}/NorenWClientAPI/PositionBook | Retrieves all active trading positions including intraday and carryforward F&O positions with real-time P&L and margin details |

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required portfolio parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| actid |  | Account ID of the logged-in user |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/PositionBook \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123M","actid": "ZXX123M"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/PositionBook"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123M",
    "actid": "ZXX123M"
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

var data = {"uid":"ZXX123M","actid":"ZXX123M"};
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/PositionBook", requestOptions)
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
        var url = "https://go.mynt.in/NorenWClientAPI/PositionBook";
        var httpClient = new HttpClient();
        httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

        var jsonData = new {
            uid = "ZXX123M",
            actid = "ZXX123M"
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/PositionBook");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid", "ZXX123M");
      json.put("actid", "ZXX123M");

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
  url := "https://go.mynt.in/NorenWClientAPI/PositionBook"
  data := map[string]string{
    "uid":   "ZXX123M",
    "actid": "ZXX123M",
  }
  jsonData, _ := json.Marshal(data)

    payload := "jData=" + string(jsonData)
    req, _ := http.NewRequest("POST", url, bytes.NewBufferString(payload))
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

Response data will be in json format with Array of Objects with below fields in case of success.

| Fields | Type | Description |
| --- | --- | --- |
| stat |  | Position book success or failure indication. |
| exch |  | Trading exchange identifier segment |
| tsym |  | Unique trading symbol identifier for the contract |
| token |  | Unique contract identifier for the trading instrument |
| uid |  | User ID of the authenticated user |
| actid |  | Account Id |
| prd |  | Product name to be shown. |
| netqty |  | Net Position quantity |
| netavgprc |  | Net position average price |
| daybuyqty |  | Day Buy Quantity |
| daysellqty |  | Day Sell Quantity |
| daybuyavgprc |  | Day Buy average price |
| daysellavgprc |  | Day Sell average price |
| daysellamt |  | Day Sell Amount |
| cfbuyqty |  | Carry Forward Buy Quantity |
| cforgavgprc |  | Original Avg Price |
| cfsellqty |  | Carry Forward Sell Quantity |
| cfbuyavgprc |  | Carry Forward Buy average price |
| cfsellavgprc |  | Carry Forward Sell average price |
| cfbuyamt |  | Carry Forward Buy Amount |
| cfsellamt |  | Carry Forward Sell Amount |
| lp |  | LTP |
| rpnl |  | RealizedPNL |
| urmtom |  | UnrealizedMTOM. (Can be recalculated in LTP update : = netqty * (lp from web socket - netavgprc) * prcftr |
| bep |  | Break even price |
| openbuyqty |  | Open Buy Quantity |
| opensellqty |  | Open Sell Quantity |
| openbuyamt |  | Open Buy Amount |
| opensellamt |  | Open Sell Amount |
| openbuyavgprc |  | Open Buy Average Price |
| opensellavgprc |  | Open Sell Average Price |
| mult |  | Contract price multiplier, (used for order value calculation) |
| pp |  | Price precision |
| prcftr |  | gn*pn/(gd*pd). |
| ti |  | Tick size |
| ls |  | Lot size |
| upldprc |  | Upload price |
| netupldprc |  | Net Upload Price |
| request_time |  | This will be present only in a failure response. |
| dname |  | Broker specific contract display name, present only if applicable. |

Response data will be in json format with below fields in case of failure:

| Fields | Type | Description |
| --- | --- | --- |
| stat | Not_Ok | Position book request failure indication. |
| request_time |  | Response received time. |
| emsg |  | Error message |

**Sample Success Response**

```json
[
 {
  "stat":"Ok",
  "uid":"ZXX123M",
  "actid":"ZXX123M",
  "exch":"NSE",
  "tsym":"ACC-EQ",
  "prarr":"C",
  "pp":"2",
  "ls":"1",
  "ti":"5.00",
  "mult":"1",
  "prcftr":"1.000000",
  "daybuyqty":"2",
  "daysellqty":"2",
  "daybuyamt":"2610.00",
  "daybuyavgprc":"1305.00",
  "daysellamt":"2610.00",
  "daysellavgprc":"1305.00",
  "cfbuyqty":"0",
  "cfsellqty":"0",
  "cfbuyamt":"0.00",
  "cfbuyavgprc":"0.00",
  "cfsellamt":"0.00",
  "cfsellavgprc":"0.00",
  "openbuyqty":"0",
  "opensellqty":"23",
  "openbuyamt":"0.00",
  "openbuyavgprc":"0.00",
  "opensellamt":"30015.00",
  "opensellavgprc":"1305.00",
  "netqty":"0",
  "netavgprc":"0.00",
  "lp":"0.00",
  "urmtom":"0.00",
  "rpnl":"0.00",
  "cforgavgprc":"0.00"
 }
]
```

**Sample Failure Response**

```json
{
"stat":"Not_Ok",
"request_time":"14:14:11 26-05-2020",
"emsg":"Error Occurred" : / "no data"
}
```

## Product Conversion

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}/NorenWClientAPI/ProductConversion | Converts trading positions between intraday and delivery modes with automatic margin and settlement adjustments |

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required portfolio parameters |

| Fields | Type | Description |
| --- | --- | --- |
| exch |  | Trading exchange identifier |
| tsym |  | Unique trading symbol identifier for the contract |
| qty |  | Quantity to be converted. |
| uid |  | User id of the logged in user. |
| actid |  | Account id |
| prd |  | Product to which the user wants to convert position. |
| prevprd |  | Original product of the position. |
| trantype |  | Transaction type |
| postype | Day / CF | Converting Day or Carry forward position |
| ordersource | MOB | For Logging |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/ProductConversion \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZP0XXXX","actid": "ZP0XXXX","exch": "NSE","tsym": "TCS-EQ","qty": "1","prd": "M","prevprd": "C","trantype": "B","postype": "DAY","ordersource": "API"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/ProductConversion"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123M",
    "actid": "ZXX123M",
    "qty": "1",
    "prd": "C",
    "prevprd": "MIS",
    "trantype": "B",
    "ordersource": "API",
    "postype": "CNC",
    "exch": "BSE",
    "tsym": "PGINVIT"
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
  "uid": "ZXX123M",
  "actid": "ZXX123M",
  "qty": "1",
  "prd": "C",
  "prevprd": "MIS",
  "trantype": "B",
  "ordersource": "API",
  "postype": "CNC",
  "exch": "BSE",
  "tsym": "PGINVIT"
};
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/ProductConversion", requestOptions)
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
        var url = "https://go.mynt.in/NorenWClientAPI/ProductConversion";
        var httpClient = new HttpClient();
        httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

        var jsonData = new {
            uid = "ZXX123M",
            actid = "ZXX123M",
            qty = "1",
            prd = "C",
            prevprd = "MIS",
            trantype = "B",
            ordersource = "API",
            postype = "CNC",
            exch = "NSE",
            tsym = "PGINVIT"
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/ProductConversion");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("qty","1");
      json.put("uid","ZXX123M");
      json.put("actid","ZXX123M");
      json.put("prd","C");
      json.put("prevprd","MIS");
      json.put("trantype","B");
      json.put("ordersource","API");
      json.put("postype","CNC");
      json.put("exch","NSE");
      json.put("tsym","PGINVIT");

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
  url := "https://go.mynt.in/NorenWClientAPI/ProductConversion"

  data := map[string]interface{}{
    "qty":         "1",
    "uid":         "ZXX123M",
    "actid":       "ZXX123M",
    "prd":         "C",
    "prevprd":     "MIS",
    "trantype":    "B",
    "ordersource": "API",
    "postype":     "CNC",
    "exch":        "NSE",
    "tsym":        "PGINVIT",
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

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Position conversion success or failure indication. |
| emsg |  | This will be present only if Position conversion fails. |

**Sample Success Response**

```json
  {
"request_time": "10:52:12 02-06-2020",
"stat": "Ok"
  }
```

**Sample Failure Response**

```json
  {
"stat": "Not_Ok",
"emsg": "Invalid Input : Invalid Position Type"
  }
```
