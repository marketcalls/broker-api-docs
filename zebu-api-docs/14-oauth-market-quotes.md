# Market Quotes

> Source: <https://zebumyntapi.web.app/OAuth/Market%20Quotes/>

> **OAuth Authentication Required**
>
> All market data API requests require OAuth authentication. Include your Bearer Unique identifier for the trading instrument in the Authorization header of each HTTP request.

## Overview

The Market Quotes APIs provide access to real-time and historical market data including:
- **Real-time Quotes**: Get current market prices, bid/ask, volume, and other trading data
- **Index Lists**: Retrieve available market indices and their tokens
- **Option Chains**: Get option contracts for specific underlying assets
- **Linked Scrips**: Find related equity, futures, and options for a given symbol
- **Historical Data**: Access time-series price data and end-of-day chart data

## Authentication

All API requests must include the OAuth access token in the Authorization header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Quotes

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}/NorenWClientAPI/GetQuotes | Retrieves real-time market quotes for multiple instruments including LTP, volume, high/low prices, and market depth data |

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required market data parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| exch |  | Trading exchange identifier |
| token |  | Unique contract identifier for the trading instrument |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/GetQuotes \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123M","exch": "NSE","token": "2885"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/GetQuotes"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123M",
    "exch": "NSE",
    "token": "2885"
}
payload = "jData=" + json.dumps(data)
response = requests.post(url, data=payload, headers=headers)
print(response.text)
```

**JavaScript**

```javascript
const data = {
    uid: "ZXX123M",
    exch: "NSE",
    token: "2885"
};

fetch("https://go.mynt.in/NorenWClientAPI/GetQuotes", {
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
var url = "https://go.mynt.in/NorenWClientAPI/GetQuotes";
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var jsonData = new {
    uid = "ZXX123M",
    exch = "NSE",
    token = "2885"
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/GetQuotes");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid", "ZXX123M");
      json.put("exch", "NSE");
      json.put("token", "2885");

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
  url := "https://go.mynt.in/NorenWClientAPI/GetQuotes"
  data := map[string]string{
    "uid":   "ZXX123M",
    "exch":  "NSE",
    "token": "2885",
  }
  jsonData, _ := json.Marshal(data)
  payload := "jData=" + string(jsonData)

  req, _ := http.NewRequest("POST", url, bytes.NewBufferString(payload))
  req.Header.Set("Content-Type", "text/plain")
  req.Header.Set("Authorization", "Bearer YOUR_ACCESS_TOKEN")

  client := &http.Client{}
  resp, err := client.Do(req)
  if err != nil {
    panic(err)
  }
  defer resp.Body.Close()
  body, _ := ioutil.ReadAll(resp.Body)
  fmt.Println(string(body))
}
```

**Response Details**

Response data will be in json format with below fields.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Watch list update success or failure indication. |
| request_time |  | It will be present only in a successful response. |
| exch | NSE, BSE, NFO ... | Trading exchange identifier |
| tsym |  | Unique trading symbol identifier for the instrument |
| cname |  | Company Name |
| symname |  | Symbol Name |
| seg |  | Segment |
| instname |  | Instrument Name |
| isin |  | ISIN |
| pp |  | Price precision |
| ls |  | Lot Size |
| ti |  | Tick Size |
| mult |  | Multiplier |
| uc |  | Upper circuit limitlc |
| lc |  | Lower circuit limit |
| prcftr_d |  | Price factor ((GN / GD) * (PN/PD)) |
| token |  | Unique contract identifier for the trading instrument |
| lp |  | LTP |
| o |  | Open Price |
| h |  | Day High Price |
| l |  | Day Low Price |
| v |  | Volume |
| ap |  | Average trade price or VWAP for day |
| ltq |  | Last trade quantity |
| ltt |  | Last trade time |
| bp1 |  | Best Buy Price 1 |
| sp1 |  | Best Sell Price 1 |
| bp2 |  | Best Buy Price 2 |
| sp2 |  | Best Sell Price 2 |
| bp3 |  | Best Buy Price 3 |
| sp3 |  | Best Sell Price 3 |
| bp4 |  | Best Buy Price 4 |
| sp4 |  | Best Sell Price 4 |
| bp5 |  | Best Buy Price 5 |
| sp5 |  | Best Sell Price 5 |
| bq1 |  | Best Buy Quantity 1 |
| sq1 |  | Best Sell Quantity 1 |
| bq2 |  | Best Buy Quantity 2 |
| sq2 |  | Best Sell Quantity 2 |
| bq3 |  | Best Buy Quantity 3 |
| sq3 |  | Best Sell Quantity 3 |
| bq4 |  | Best Buy Quantity 4 |
| sq4 |  | Best Sell Quantity 4 |
| bq5 |  | Best Buy Quantity 5 |
| sq5 |  | Best Sell Quantity 5 |
| bo1 |  | Best Buy Orders 1 |
| so1 |  | Best Sell Orders 1 |
| bo2 |  | Best Buy Orders 2 |
| so2 |  | Best Sell Orders 2 |
| bo3 |  | Best Buy Orders 3 |
| so3 |  | Best Sell Orders 3 |
| bo4 |  | Best Buy Orders 4 |
| so4 |  | Best Sell Orders 4 |
| bo5 |  | Best Buy Orders 5 |
| so5 |  | Best Sell Orders 5 |

**Sample Success Response**

```json
{
  "request_time": "12:05:21 18-05-2021",
  "stat": "Ok",
  "exch": "NSE",
  "tsym": "ACC-EQ",
  "cname": "ACC LIMITED",
  "symname": "ACC",
  "seg": "EQT",
  "instname": "EQ",
  "isin": "INE012A01025",
  "pp": "2",
  "ls": "1",
  "ti": "0.05",
  "mult": "1",
  "uc": "2093.95",
  "lc": "1713.25",
  "prcftr_d": "(1 / 1 ) * (1 / 1)",
  "token": "22",
  "lp": "0.00",
  "h": "0.00",
  "l": "0.00",
  "v": "0",
  "ltq": "0",
  "ltt": "05:30:00",
  "bp1": "2000.00",
  "sp1": "0.00",
  "bp2": "0.00",
  "sp2": "0.00",
  "bp3": "0.00",
  "sp3": "0.00",
  "bp4": "0.00",
  "sp4": "0.00",
  "bp5": "0.00",
  "sp5": "0.00",
  "bq1": "2",
  "sq1": "0",
  "bq2": "0",
  "sq2": "0",
  "bq3": "0",
  "sq3": "0",
  "bq4": "0",
  "sq4": "0",
  "bq5": "0",
  "sq5": "0",
  "bo1": "2",
  "so1": "0",
  "bo2": "0",
  "so2": "0",
  "bo3": "0",
  "so3": "0",
  "bo4": "0",
  "so4": "0",
  "bo5": "0",
  "So5": "0"
}
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "request_time": "10:50:54 10-12-2020",
  "emsg": "Error Occurred : 5 "no data" "
}
```

## Index List

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}/NorenWClientAPI/GetIndexList | Retrieves comprehensive list of market indices with real-time values, percentage changes, and index-specific metadata |

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required market data parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| exch |  | Trading exchange identifier |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/GetIndexList \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123M","exch": "NSE"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/GetIndexList"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123M",
    "exch": "NSE"
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

var data = {"uid":"ZXX123M","exch":"NSE"};
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};

  fetch("https://go.mynt.in/NorenWClientAPI/GetIndexList", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientAPI/GetIndexList";
var jsonData = new {uid = "ZXX123M", exch = "NSE"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/GetIndexList");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid", "ZXX123M");
      json.put("exch", "NSE");

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
  url := "https://go.mynt.in/NorenWClientAPI/GetIndexList"
  data := map[string]string{
    "uid":  "ZXX123M",
    "exch": "NSE",
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

Response data will be in json format with below fields.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | TopListNames success or failure indication |
| values |  | Array Of Basket, Criteria pair. |
| request_time |  | This will be present only in a successful response. |
| emsg |  | This will be present only in case of errors. |

Basket, Criteria pair Object :

| Fields | Type | Description |
| --- | --- | --- |
| idxname |  | Index Name |
| token |  | Unique identifier for the market index |

**Sample Success Response**

```json
{
  "request_time": "20:12:29 13-12-2020",
  "values": [
    {
      "idxname": "HangSeng BeES-NAV",
      "token": "26016"
    },
    {
      "idxname": "India VIX",
      "token": "26017"
    },
    {
      "idxname": "Nifty 50",
      "token": "26000"
    },
    {
      "idxname": "Nifty IT",
      "token": "26008"
    },
    {
      "idxname": "Nifty Next 50",
      "token": "26013"
    },
    {
      "idxname": "Nifty Bank",
      "token": "26009"
    },
    {
      "idxname": "Nifty 500",
      "token": "26004"
    },
    {
      "idxname": "Nifty 100",
      "token": "26012"
    },
    {
      "idxname": "Nifty Midcap 50",
      "token": "26014"
    }
  ]
}
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid Input : Missing uid or exch"
}
```

## Option Chain

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}/NorenWClientAPI/GetOptionChain | Retrieves complete option chain data with strike prices, premiums, Greeks, and open interest for derivatives trading |

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required market data parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| tsym |  | Trading symbol for options or futures underlying (URL encoding required for special characters) |
| exch |  | Trading exchange identifier (must support options trading like NFO, CDS, MCX) |
| strprc |  | Mid price for option chain selection |
| cnt |  | Number of strike to return on one side of the mid price for PUT and CALL. (example cnt is 4, total 16 contracts will be returned, if cnt is is 5 total 20 contract will be returned) |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/GetOptionChain \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZP0XXXX","exch": "NFO","tsym": "NIFTY28OCT25F","strprc": "19500","cnt": "5"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/GetOptionChain"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZP0XXXX",
    "exch": "NFO",
    "tsym": "NIFTY28OCT25F",
    "strprc": "19500",
    "cnt": "5"
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

var data = {"uid":"ZP0XXXX","exch":"NFO","tsym":"NIFTY28OCT25F","strprc":"19500","cnt":"5"};
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/GetOptionChain", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientAPI/GetOptionChain";
var jsonData = new {uid = "ZP0XXXX", exch = "NFO", tsym = "NIFTY28OCT25F", strprc = "19500", cnt = "5"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/GetOptionChain");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid", "ZP0XXXX");
      json.put("exch", "NFO");
      json.put("tsym", "NIFTY28OCT25F");
      json.put("strprc", "19500");
      json.put("cnt", "5");

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
  url := "https://go.mynt.in/NorenWClientAPI/GetOptionChain"
  data := map[string]string{
    "uid":    "ZP0XXXX",
    "exch":   "NFO",
    "tsym":   "NIFTY28OCT25F",
    "strprc": "19500",
    "cnt":    "5",
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

Response data will be in json format with below fields.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Market watch success or failure indication. |
| values |  | Array of json objects. (object fields given in below table) |
| emsg |  | This will be present only in case of errors. That is :<br><br>Invalid Input<br>Session Expired |

| Fields | Type | Description |
| --- | --- | --- |
| exch | CDS, NFO ... | Trading exchange identifier |
| tsym |  | Unique trading symbol identifier for the contract |
| token |  | Unique identifier for the trading contract |
| optt |  | Option Type |
| strprc |  | Strike price |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |

**Sample Success Response**

```json
{
  "stat": "Ok",
  "values": [
    {
      "exch": "NFO",
      "token": "55523",
      "tsym": "BANKNIFTY25JAN23C42900",
      "optt": "CE",
      "pp": "2",
      "ls": "25",
      "ti": "0.05",
      "strprc": "42900.00"
    },
    {
      "exch": "NFO",
      "token": "55525",
      "tsym": "BANKNIFTY25JAN23C43000",
      "optt": "CE",
      "pp": "2",
      "ls": "25",
      "ti": "0.05",
      "strprc": "43000.00"
    },
    {
      "exch": "NFO",
      "token": "55530",
      "tsym": "BANKNIFTY25JAN23C43100",
      "optt": "CE",
      "pp": "2",
      "ls": "25",
      "ti": "0.05",
      "strprc": "43100.00"
    }
  ]
}
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid Input : Missing uid or actid or prd."
}
```

## Linked Scrips

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}/NorenWClientAPI/GetLinkedScrips | Retrieves linked scrip information showing related instruments, derivatives, and associated trading symbols for comprehensive market analysis |

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required market data parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| token |  | Unique contract identifier for the trading instrument |
| exch |  | Trading exchange identifier (must support options trading like NFO, CDS, MCX) |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/GetLinkedScrips \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123M","exch": "NSE","token": "2885"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/GetLinkedScrips"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123M",
    "exch": "NSE",
    "token": "2885"
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

var data = {"uid":"ZXX123M","exch":"NSE","token":"2885"};
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/GetLinkedScrips", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientAPI/GetLinkedScrips";
var jsonData = new {uid = "ZXX123M", exch = "NSE", token = "2885"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/GetLinkedScrips");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid", "ZXX123M");
      json.put("exch", "NSE");
      json.put("token", "2885");

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
  url := "https://go.mynt.in/NorenWClientAPI/GetLinkedScrips"
  data := map[string]string{
    "uid":   "ZXX123M",
    "exch":  "NSE",
    "token": "2885",
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

| Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Market watch success or failure indication. |
| equls |  | Array of json objects equls. (object fields given in below table) |
| fut |  | Array of json objects fut. (object fields given in below table) |
| opt_exp |  | Array of json objects opt_exp. (object fields given in below table) |
| emsg |  | This will be present only in case of errors. That is :<br><br>Invalid Input<br>Session Expired |

| Fields | Type | Description |
| --- | --- | --- |
| exch | NSE, BSE ... | Trading exchange identifier |
| tsym |  | Unique trading symbol identifier for the contract |
| token |  | Unique identifier for the trading contract |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |
| mult |  | Contract price multiplier, (used for order value calculation) |

| Fields | Type | Description |
| --- | --- | --- |
| exd |  | Used for calling option chain api |
| exch | NFO, MCX ... Ex | Trading exchange identifier |
| tsym |  | Sample trading symbol for the given expiry (used for option chain retrieval) |

**Sample Success Response**

```json
{
  "request_time": "17:21:38 23-01-2023",
  "stat": "Ok",
  "equls": [
    {
      "exch": "NXXX",
      "token": "1234",
      "tsym": "RELXXX",
      "pp": "2",
      "ti": "0.05",
      "ls": "1",
      "mult": "1"
    },
    {
      "exch": "BSE",
      "token": "500325",
      "tsym": "RELIANCEXX",
      "pp": "2",
      "ti": "0.05",
      "ls": "1",
      "mult": "1"
    }
  ],
  "fut": [
    {
      "exch": "NXX",
      "token": "57701",
      "tsym": "RELIXXXX",
      "pp": "2",
      "ls": "250",
      "ti": "0.05",
      "mult": "1",
      "exd": "23-FEB-2023"
    },
    {
      "exch": "NFO",
      "token": "55270",
      "tsym": "RELIAXXX",
      "pp": "2",
      "ls": "250",
      "ti": "0.05",
      "mult": "1"
    },
    {
      "exch": "NXXX",
      "token": "52481",
      "tsym": "RELXXXX",
      "pp": "2",
      "ls": "250",
      "ti": "0.05",
      "mult": "1",
      "exd": "29-MAR-2023"
    }
  ]
}
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid Input : Missing uid or actid or prd."
}
```

## Historical candle data

## Get Time Price Data

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}/NorenWClientAPI/TPSeries | Retrieves historical time-series price data with customizable intervals for technical analysis and charting applications |

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required market data parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| exch |  | Trading exchange identifier |
| token |  | Unique contract identifier for the trading instrument |
| st |  | Start time (seconds since 1 jan 1970) converter in Epoch formet |
| et |  | End Time (seconds since 1 jan 1970) converter in Epoch formet |
| intrv | “1”, ”3”, “5”, “10”, “15”, “30”, “60”, “120”, “240” | Candle size in minutes (optional field, if not given assume to be “1”) |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/TPSeries \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZP0XXXX","exch": "NSE","token": "3045","st": "1744577700","et": "1744603800","intrv": "1"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/TPSeries"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123M",
    "exch": "NSE",
    "token": "PAYTM-EQ",
    "st": "1710698300",
    "et": "1710863909",
    "intrv": "5"
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

var data = {"uid":"ZXX123M","exch":"NSE","token":"PAYTM-EQ","st":"1710698300","et":"1710863909","intrv":"5"};
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/TPSeries", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientAPI/TPSeries";
var jsonData = new {uid = "ZXX123M", exch = "NSE", token = "PAYTM-EQ", st = "1710698300", et = "1710863909", intrv = "5"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/TPSeries");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid", "ZXX123M");
      json.put("exch", "NSE");
      json.put("token", "PAYTM-EQ");
      json.put("st", "1710698300");
      json.put("et", "1710863909");
      json.put("intrv", "5");

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
  url := "https://go.mynt.in/NorenWClientAPI/TPSeries"
  data := map[string]string{
    "uid":   "ZXX123M",
    "exch":  "NSE",
    "token": "PAYTM-EQ",
    "st":    "1710698300",
    "et":    "1710863909",
    "intrv": "5",
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

Response data will be in json format in case for success.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok | TPData success indication |
| time |  | DD/MM/CCYY hh:mm:ss |
| into |  | Interval open |
| inth |  | Interval high |
| intl |  | Interval low |
| intc |  | Interval close |
| intvwap |  | Interval vwap |
| intv |  | Interval volume |
| v |  | volume |
| intoi |  | Interval io change |
| oi |  | oi |

Response data will be in json format in case for failure.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Not_Ok | TPData failure indication. |
| emsg |  | This will be present only in case of errors. |

**Sample Success Response**

```json
[
 {
  "stat":"Ok",
  "time":"02-06-2020 15:46:23",
  "into":"0.00",
  "inth":"0.00",
  "intl":"0.00",
  "intc":"0.00",
  "intvwap":"0.00",
  "intv":"0",
  "intoi":"0",
  "v":"980515",
  "oi":"128702"
 },
 {
  "stat":"Ok",
  "time":"02-06-2020 15:45:23",
  "into":"0.00",
  "inth":"0.00",
  "intl":"0.00",
  "intc":"0.00",
  "intvwap":"0.00",
  "intv":"0",
  "intoi":"0",
  "v":"980515",
  "oi":"128702"
 },
 {
  "stat":"Ok",
  "time":"02-06-2020 15:44:23",
  "into":"0.00",
  "inth":"0.00",
  "intl":"0.00",
  "intc":"0.00",
  "intvwap":"0.00",
  "intv":"0",
  "intoi":"0",
  "v":"980515",
  "oi":"128702"
 },
 {
  "stat":"Ok",
  "time":"02-06-2020 15:43:23",
  "into":"1287.00",
  "inth":"1287.00",
  "intl":"0.00",
  "intc":"1287.00",
  "intvwap":"128702.00",
  "intv":"4",
  "intoi":"128702",
  "v":"980515",
  "oi":"128702"
 },
 {
  "stat":"Ok",
  "time":"02-06-2020 15:42:23",
  "into":"0.00",
  "inth":"0.00",
  "intl":"0.00",
  "intc":"0.00",
  "intvwap":"0.00",
  "intv":"0",
  "intoi":"0",
  "v":"980511",
  "oi":"128702"
 }
]
```

**Sample Failure Response**

```json
{
 "stat":"Not_Ok",
 "emsg":"Session Expired : Invalid Session Key"
}
```

## EOD Chart Data

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}/NorenWClientAPI/EODChartData | Retrieves end-of-day historical chart data with OHLCV values for comprehensive market analysis and backtesting |

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required market data parameters |

| Fields | Type | Description |
| --- | --- | --- |
| sym |  | Symbol name |
| from |  | From date converter in Epoch formet |
| to |  | To date converter in Epoch formet |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/EODChartData \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"sym": "NSE:RELIANCE-EQ","from": 1624838400,"to": 1663718400}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/EODChartData"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "sym": "NSE:RELIANCE-EQ",
    "from": "1624838400",
    "to": "1663718400"
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

var data = {"sym":"NSE:RELIANCE-EQ","from":"1624838400","to":"1663718400"};
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};

 fetch("https://go.mynt.in/NorenWClientAPI/EODChartData", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientAPI/EODChartData";
var jsonData = new {sym = "NSE:RELIANCE-EQ", from = "1624838400", to = "1663718400"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var httpClient = new HttpClient();
httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/EODChartData");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("sym", "NSE:RELIANCE-EQ");
      json.put("from", "1624838400");
      json.put("to", "1663718400");

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
  url := "https://go.mynt.in/NorenWClientAPI/EODChartData"
  data := map[string]interface{}{
    "sym":  "NSE:RELIANCE-EQ",
    "from": 1624838400,
    "to":   1663718400,
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

Response data will be in json format with below fields.

| Fields | Type | Description |
| --- | --- | --- |
| time |  | DD/MM/CCYY hh:mm:ss |
| into |  | Interval open |
| inth |  | Interval high |
| intl |  | Interval low |
| intc |  | Interval close |
| ssboe |  | Date,Seconds in 1970 format |
| intv |  | Interval volume |

**Sample Success Response**

```json
[

     {
       "time":"21-SEP-2022",
       "into":"2496.75",
       "inth":"2533.00",
       "intl":"2495.00",
       "intc":"2509.75",
       "ssboe":"1663718400",
       "intv":"4249172.00"
      }",
      "{
        "time":"15-SEP-2022",
        "into":"2583.00",
        "inth":"2603.55",
        "intl":"2556.75",
        "intc":"2562.70",
        "ssboe":"1663200000",
        "intv":"4783723.00"
       }",
       "{
         "time":"28-JUN-2021",
         "into":"2122.00",
         "inth":"2126.50",
         "intl":"2081.00",
         "intc":"2086.00",
         "ssboe":"1624838400",
         "intv":"9357852.00"
        }
      ]
```

**Sample Failure Response**

```json
{
 "stat":"Not_Ok",
 "emsg":"Session Expired : Invalid Session Key"
}
```
