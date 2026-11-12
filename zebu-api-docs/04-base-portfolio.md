# Portfolio

> Source: <https://zebumyntapi.web.app/Base/Portfolio/>

## Holdings

POST - `https://go.mynt.in/NorenWClientTP/Holdings`

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| actid* |  | Account id of the logged in user. |
| prd* |  | Product name |

Example:

**curl**

```bash
curl https://go.mynt.in/NorenWClientTP/Holdings \
  jData= {"uid":"ZXX123M","actid":"ZXX123M","prd":"C"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/Holdings"
data = {"uid":"ZXX123M","actid":"ZXX123M","prd":"c"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)

print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append(
"Content-Type",
"application/json"
);
var data = {"uid":"ZXX123M","actid":"ZXX123M","prd":"C"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/Holdings", requestOptions)
.then(response => response.text())
.then(result => console.log(result))
.catch(error => console.log('error', error));
```

**C#**

```csharp
using System;
using System.Net.Http;
using Newtonsoft.Json;

class Programx
{
static void Main(string[] args)
{
var url = "https://go.mynt.in/NorenWClientTP/Holdings";
var jsonData = new {uid = "ZXX123M",actid="ZXX123M",prd = "C"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData="+jsonString+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var httpClient = new HttpClient();
var response = httpClient.PostAsync(url, new StringContent(payload)).Result;
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/Holdings");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json = new JSONObject();
      json.put("uid","ZXX123M");
      json.put("actid","ZXX123M");
      json.put("prd","C")
      String payload = "jData="+json.toString()+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
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

  url := "https://mynt.in/NorenWClientTP/Holdings"
  method := "POST"

  payload := strings.NewReader(`jData={"uid":"ZXX123M","actid":"ZXX123M","prd":"C"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "text/plain")

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

Response Details

Response data will be in json format with below fields in case of Success:

| Json Fields | Possible value | Description |
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

| Json Fields of object in values Array | Possible value | Description |
| --- | --- | --- |
| exch | NSE, BSE, NFO ... | Exchange |
| tsym |  | Trading symbol of the scrip (contract). |
| token |  | Token of the scrip (contract) |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |

Response data will be in json format with below fields in case of failure:

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Not_Ok | Position book request failure indication. |
| request_time |  | Response received time. |
| emsg |  | Error message |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |

Sample Success Response :

```json
[
 {
  "stat":"Ok",
  "exch_tsym":
  [
   {
    "exch":"NSE",
    "token":"2885",
    "tsym":"ABB-EQ"
   }
  ],
  "holdqty":"2000000",
  "colqty":"200",
  "btstqty":"0",
  "btstcolqty":"0",
  "usedqty":"0",
  "upldprc" : "1800.00"
 },
 {
  "stat":"Ok",
  "exch_tsym":
  [
   {
    "exch":"NSE",
    "token":"2885",
    "tsym":"ACC-EQ"
   }
  ],
  "holdqty":"2000000",
  "colqty":"200",
  "btstqty":"0",
  "btstcolqty":"0",
  "usedqty":"0",
  "upldprc" : "1400.00"
  }
]
```

Sample Failure Response :

```json
{
    "stat":"Not_Ok",
    "emsg":"Invalid Input : Missing uid or actid or prd."
}
```

## Positions Book

POST - https://go.mynt.in/NorenWClientTP/PositionBook

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |

Example:

**curl**

```bash
curl https://go.mynt.in/NorenWClientTP/PositionBook
jData= {"uid":"ZXX123M","actid":"ZXX123M"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json
url = "https://go.mynt.in/NorenWClientTP/PositionBook"
data = {"uid":"ZXX123M","actid":"ZXX123M"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123M","actid":"ZXX123M"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";

var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};

fetch("https://go.mynt.in/NorenWClientTP/PositionBook", requestOptions)
.then(response => response.text())
.then(result => console.log(result))
 .catch(error => console.log('error', error));
```

**C#**

```csharp
using System;
using System.Net.Http;
using Newtonsoft.Json;

class Programx
{
static void Main(string[] args)
{
var url = "https://go.mynt.in/NorenWClientTP/PositionBook";
var jsonData = new {uid = "ZXX123M",actid="ZXX123M"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData="+jsonString+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var httpClient = new HttpClient();
var response = httpClient.PostAsync(url, new StringContent(payload)).Result;
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/PositionBook");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json= new JSONObject();
      json.put("uid","ZXX123M");
      json.put("actid","ZXX123M");

      String payload = "jData="+json.toString()+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
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

  url := "https://mynt.in/NorenWClientTP/PositionBook"
  method := "POST"

  payload := strings.NewReader(`jData={"uid":"ZXX123M","actid":"ZXX123M"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "text/plain")

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

Response Details

Response data will be in json format with Array of Objects with below fields in case of success.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat |  | Position book success or failure indication. |
| exch |  | Exchange segment |
| tsym |  | Trading symbol / contract. |
| token |  | Contract token |
| uid |  | User Id |
| actid |  | Account Id |
| prd |  | Product name to be shown. |
| netqty |  | Net Position quantity |
| netavgprc |  | Net position average price |
| daybuyqty |  | Day Buy Quantity |
| daysellqty |  | Day Sell Quantity |
| daybuyavgprc |  | Day Buy average price |
| daysellavgprc |  | Day Sell average price |
| daysellavgprc |  | Day Buy Amount |
| daysellamt |  | Day Sell Amount |
| cfbuyqty |  | Carry Forward Buy Quantity |
| cforgavgprc |  | Original Avg Price |
| cfsellqty |  | Carry Forward Sell Quantity |
| cfbuyavgprc |  | Carry Forward Buy average price |
| cfsellavgprc |  | Carry Forward Buy average price |
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

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Not_Ok | Position book request failure indication. |
| request_time |  | Response received time. |
| emsg |  | Error message |

Sample Success Response :

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

Sample Failure Response :

```json
{
"stat":"Not_Ok",
"request_time":"14:14:11 26-05-2020",
"emsg":"Error Occurred : 5 \"no data\""
}
```

## Product Conversion

POST - https://go.mynt.in/NorenWClientTP/ProductConversion

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| exch* |  | Exchange |
| tsym* |  | Unique id of contract on which order was placed. Can’t be modified, must be the same as that of original order. (use url encoding to avoid special char error for symbols like M&M) |
| qty* |  | Quantity to be converted. |
| uid* |  | User id of the logged in user. |
| actid* |  | Account id |
| prd* |  | Product to which the user wants to convert position. |
| prevprd* |  | Original product of the position. |
| trantype* |  | Transaction type |
| postype* | Day / CF | Converting Day or Carry forward position |
| ordersource | MOB | For Logging |

Example

**curl**

```bash
curl   https://go.mynt.in/NorenWClientTP/ProductConversion
jData= {"uid":"ZXX123M","actid":"ZXX123M","qty":"1","prd":"C","prevprd":"MIS","trantype":"B","ordersource":"API","postype":"CNC","exch":"BSE","tsym":"PGINVIT"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/ProductConversion"
data = {"uid":"ZXX123M","actid":"ZXX123M","qty":"1","prd":"C","prevprd":"MIS","trantype":"B","ordersource":"API","postype":"CNC","exch":"BSE","tsym":"PGINVIT"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data ={"uid":"ZXX123M","actid":"ZXX123M","qty":"1","prd":"C","prevprd":"MIS","trantype":"B","ordersource":"API","postype":"CNC","exch":"BSE","tsym":"PGINVIT"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/ProductConversion", requestOptions)
.then(response => response.text())
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
var url = "https://go.mynt.in/NorenWClientTP/ProductConversion";
var jsonData = new {uid = "ZXX123M",actid="ZXX123M",qty ="1",prd ="C",prevprd="MIS",trantype ="B",ordersource="API",postype ="CNC",exch="NSE",tsym ="PGINVIT"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData="+jsonString+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var httpClient = new HttpClient();
var response = httpClient.PostAsync(url, new StringContent(payload)).Result;
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/ProductConversion");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json=new JSONObject();
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
      String payload = "jData="+json.toString()+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
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

  url := "https://go.mynt.in/NorenWClientTP/ProductConversion"
  method := "POST"

  payload := strings.NewReader(`jData= {"qty":"ZXX123M","uid":"ZXX123M","actid":"ZXX123M","prd":"C","prevprd":"MIS","trantype":"B","ordersource":"API","postype":"CNC","exch":"NSE","tsym":"PGINVIT"}&jKey= 076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "text/plain")

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

Response Details :

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Position conversion success or failure indication. |
| emsg |  | This will be present only if Position conversion fails. |

Sample Success Response :

```json
{
"request_time":"10:52:12 02-06-2020",
"stat":"Ok"
}
```

Sample Failure Response :

```json
{
"stat":"Not_Ok",
"emsg":"Invalid Input : Invalid Position Type"
}
```

## Close position

POST - [`https://be.mynt.in/close_position`]

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| actid* |  | Login users account ID |
| emsg |  | This will be present only in a failure response. |

Example

**curl**

```bash
curl  https://be.mynt.in/close_position
jData={"uid":"ZXX123M","actid":"ZXX123M"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json
url = "https://be.mynt.in/close_position"
data = {"uid":"ZXX123M","actid":"ZXX123M"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)

print(response.text)
```

**JavaScript**

```javascript
const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123M","actid":"ZXX123M"}
const raw = "jData="+JSON.stringify(data)+"&jKey=ec04d1e2d482dfc48aba4e7b68d0f315d10d4071168d19152835a2d00096e496";

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("https://be.mynt.in/close_position", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
.catch((error) => console.error(error));
```

**C#**

```csharp
using System;
using System.Net.Http;
using Newtonsoft.Json;
class Programx
{
static void Main(string[] args)
{
var url = "https://be.mynt.in/close_position";
var jsonData = new {uid = "ZXX123M",actid="ZXX123M"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData="+jsonString+"&jKey=d41bc850df3cb6b97ceed8a3b8ea67da33bc972694cd9da0550c091a48035cff";
var httpClient = new HttpClient();
var response = httpClient.PostAsync(url, new StringContent(payload)).Result;
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
      URL url = new URL("https://be.mynt.in/close_position");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json=new JSONObject();
      json.put("uid","ZXX123M");
      json.put("actid","ZXX123M");
      String payload = "jData="+json.toString()+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
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
      "io/ioutil"
      "net/http"
      "strings"
    )

    func main() {

      url := "https://be.mynt.in/close_position"
      method := "POST"

      payload := strings.NewReader(`jData={"uid":"ZXX123M","actid":"ZXX123M"}&jKey=d41bc850df3cb6b97ceed8a3b8ea67da33bc972694cd9da0550c091a48035cff`)

      client := &http.Client{}
      req, err := http.NewRequest(method, url, payload)

      if err != nil {
        fmt.Println(err)
        return
      }
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

Sample Success Response:

```json
[
  {
    "buy_or_sell":"S",
    "discloseqty":"0",
    "exchange":"NSE",
    "norenordno":"24040200027318",
    "price":"0",
    "price_type":"MKT",
    "product_type":"C",
    "quantity":"1",
    "request_time":"12:52:38 02-04-2024",
    "session":"5fadf7f92c9b70fc145144f725de8b2fbc19f4b8bc75bda9a489329c279d3cc9",
    "stat":"Ok",
    "tradingsymbol":"IDEA-EQ",
    "uid":"ZXX123M"
  }
]
```

Sample Failure Response:

```json
{
"emsg":"Session Expired :  Invalid Session Key","stat":"Not_Ok"
}
```

## Close Partially

POST - [`https://be.mynt.in/close_position`]

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| actid* |  | Login users account ID |
| tsym* |  | Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M) |
| qty* |  | Order Quantity |
| prctyp* | LMT / MKT /SL-LMT / SL-MKT / DS / 2L / 3L |  |
| emsg |  | This will be present only in a failure response. |

Example

**curl**

```bash
curl  https://be.mynt.in/close_position
jData={"uid":"ZXX123M","actid":"ZXX123M","partial":[{"tradingsymbol":"TCS-EQ","order_type":"MIS","quantity" : "1"},{"tradingsymbol":"IDEA-EQ","order_type":"MIS","quantity" : "2"}]}&jKey=7b4598927454a64b74bc0d86b323752b3616d17018e4f270567b6b333787e45e
```

**Python**

```python
import requests
import json

url = "https://be.mynt.in/close_position"
data = {"uid":"ZXX123M","actid":"ZXX123M","partial":[{"tradingsymbol":"TCS-EQ","order_type":"MIS","quantity" : "1"},{"tradingsymbol":"IDEA-EQ","order_type":"MIS","quantity" : "2"}]}
payload = "jData="+json.dumps(data)+"&jKey=7b4598927454a64b74bc0d86b323752b3616d17018e4f270567b6b333787e45e"

headers = {
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

**JavaScript**

```javascript
const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
const raw = "jData={"uid":"ZXX123M","actid":"ZXX123M","partial":[{"tradingsymbol":"TCS-EQ","order_type":"MIS","quantity" : "1"},{"tradingsymbol":"IDEA-EQ","order_type":"MIS","quantity" : "2"}]}&jKey=7b4598927454a64b74bc0d86b323752b3616d17018e4f270567b6b333787e45e";

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("https://be.mynt.in/close_position", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));
```

**C#**

```csharp
class Programx
     {
     static void Main(string[] args)
     {
     var url = "https://be.mynt.in/close_position";
     var obj1 = new {tradingsymbol="TCS-EQ",order_type="MIS",quantity= "1"};
     var obj2 = new {tradingsymbol="IDEA-EQ",order_type="MIS",quantity = "2"};
     object[] array = {obj1,obj2};
     var jsonData = new {uid="ZXX123M",actid="ZXX123M",partial=array};
     var jsonString = JsonConvert.SerializeObject(jsonData);
     var payload = "jData="+jsonString+"&jKey=d41bc850df3cb6b97ceed8a3b8ea67da33bc972694cd9da0550c091a48035cff";
     var httpClient = new HttpClient();
     var response = httpClient.PostAsync(url, new StringContent(payload)).Result;
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
import org.json.JSONArray;
import org.json.simple.JSONObject;

public class App {
  public static void main(String[] args) {
    try {
      URL url = new URL("https://be.mynt.in/close_position");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");

      JSONObject obj1= new JOSNObject();
      obj1.put("tradingsymbol","TCS-EQ");
      obj1.put("order_type","MIS");
      obj1.put("quantity", "1");
      JSONObject obj2 = new JSONObjct();
      obj2.put("tradingsymbol","IDEA-EQ");
      obj2.put("order_type","MIS");
      obj2.put("quantity ", "2");

      JSONArray pets = new JSONArray();
      pets.put(obj1);
      pets.put(obj2);
      JSONObject json=new JSONObject();
      json.put("uid","ZXX123M");
      json.put("actid","ZXX123M");
      json.put("partial",val);
      String payload = "jData="+json.toString()+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
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
func main() {

  url := "https://be.mynt.in/close_position"
  method := "POST"

  payload := strings.NewReader(`jData={"uid":"ZXX123M","actid":"ZXX123M","partial":[{"tradingsymbol":"TCS-EQ","order_type":"MIS","quantity" : "1"},{"tradingsymbol":"IDEA-EQ","order_type":"MIS","quantity" : "2"}]}&jKey=d41bc850df3cb6b97ceed8a3b8ea67da33bc972694cd9da0550c091a48035cff`)

  client := &http.Client{}
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
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

Sample Success Response:

```json
[
  {
    "buy_or_sell":"S",
    "discloseqty":"0",
    "exchange":"NSE",
    "norenordno":"24040200027318",
    "price":"0",
    "price_type":"MKT",
    "product_type":"C",
    "quantity":"1",
    "request_time":"12:52:38 02-04-2024",
    "session":"5fadf7f92c9b70fc145144f725de8b2fbc19f4b8bc75bda9a489329c279d3cc9",
    "stat":"Ok",
    "tradingsymbol":"IDEA-EQ",
    "uid":"ZXX123M"
  }
]
```

Sample Failure Response:

```json
{
"emsg":"Session Expired :  Invalid Session Key","stat":"Not_Ok"
}
```
