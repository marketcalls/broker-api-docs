# Order  -

> Source: <https://zebumyntapi.web.app/Base/Order/>

## Placing Orders

POST - https://go.mynt.in/NorenWClientTP/PlaceOrder

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| actid* |  | Login users account ID |
| exch* | NSE / NFO / BSE / MCX | Exchange (Select from ‘exarr’ Array provided in User Details response) |
| tsym* |  | Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M) |
| qty* |  | Order Quantity |
| prc* |  | Order Price |
| trgprc |  | Only to be sent in case of SL-LMT / SL-MKT order. |
| dscqty |  | Disclosed quantity (Max 10% for NSE, and 50% for MCX) |
| prd* | C / M / H | Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call) |
| trantype* | B / S | B -> BUY, S -> SELL |
| prctyp* | LMT / MKT /SL-LMT / SL-MKT / DS / 2L / 3L |  |
| mkt_protection |  | Market order protection percentage. Applicable only for MKT orders in BSE/BFO/BCS and MCX segments. |
| ret* | DAY / EOS / IOC | Retention type (Show options as per allowed exchanges) |
| remarks |  | Any tag by user to mark order. |
| ordersource | MOB / WEB / TT | Used to generate exchange info fields. |
| bpprc |  | Book Profit Price applicable only if product is selected as B (Bracket order ) |
| blprc |  | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc |  | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| usr_agent |  | User Agent |
| app_inst_id |  | App Install Id |
| amo |  | Yes , If not sent, of Not “Yes”, will be treated as Regular order. |
| tsym2 |  | Trading symbol of second leg, mandatory for price type 2L and 3L (use url encoding to avoid special char error for symbols like M&M) |
| trantype2 |  | Transaction type of second leg, mandatory for price type 2L and 3L |
| qty2 |  | Quantity for second leg, mandatory for price type 2L and 3L |
| prc2 |  | Price for second leg, mandatory for price type 2L and 3L |
| tsym3 |  | Trading symbol of third leg, mandatory for price type 3L (use url encoding to avoid special char error for symbols like M&M) |
| trantype3 |  | Transaction type of third leg, mandatory for price type 3L |
| qty3 |  | Quantity for third leg, mandatory for price type 3L |
| prc3 |  | Price for third leg, mandatory for price type 3L |
| ipaddr |  | global Ip of internet access |
| algo_id |  | Exchange approved algo id |
| naic_code |  |  |

Example

**curl**

```bash
curl   https://go.mynt.in/NorenWClientTP/PlaceOrder \
jData = {"uid":"ZXX123N","exch":"NSE","prctyp":"MKT","prc":"0","qty":"10","tsym":"TCS-EQ","ret":"DAY","mkt_protection":"2","prc":"0","dscqty":"0"},"jKey":"076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/PlaceOrder"
data = {"uid":"ZXX123N","actid":"ZXX123N","exch":"BSE","tsym":"PGINVIT","qty":"1","mkt_protection":"1","prc":"94.06","trgprc":"B","dscqty":"0","prd":"C","trantype":"B","prctyp":"LMT","ret":"DAY","ordersource":"API"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data ={"uid":"ZXX123N","actid":"ZXX123N","exch":"BSE","tsym":"PGINVIT","qty":"1","mkt_protection":"1","prc":"94.06","trgprc":"B","dscqty":"0","prd":"C","trantype":"B","prctyp":"LMT","ret":"DAY","ordersource":"API"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/PlaceOrder", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/PlaceOrder";
var jsonData = new {uid = "ZXX123N",actid="ZXX123N",exch="BSE",tsym="PGINVIT",qty ="1",mkt_protection ="1",prc="94.06",trgprc="B",dscqty="0",prd="C",trantype ="B",prctyp ="LMT",ret ="DAY",ordersource = "API"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/PlaceOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json= new JSONObject();
      json.put("uid","ZXX123N");
      json.put("actid","ZXX123N");
      json.put("exch","NSE");
      json.put("tsym","JINDWORLD-EQ");
      json.put("qty","1");
      json.put("mkt_protection","1");
      json.put("prc","");
      json.put("trgprc","B");
      json.put("dscqty","0");
      json.put("prd","C");
      json.put("trantype","B");
      json.put("prctyp","SL-LMT");
      json.put("ret","DAY");
      json.put("ordersource", "API");
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

url := "https://go.mynt.in/NorenWClientTP/PlaceOrder"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N","actid":"ZXX123N","exch":"NSE","tsym":"JINDWORLD-EQ","qty":"1","mkt_protection":"1","prc":"150","trgprc":"0","dscqty":"0","prd":"C","trantype":"B","prctyp":"SL-LMT","ret":"DAY","ordersource":"API"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

client := &http.Client {
}
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

Response Details

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Place order success or failure indication. |
| request_time |  | Response received time. |
| norenordno |  | It will be present only on successful Order placement to OMS. |
| emsg |  | This will be present only if Order placement fails |

Sample Success Response

```json
{
"request_time": "10:48:03 20-05-2020",
"stat": "Ok",
"norenordno": "24033000000002"
}
```

Sample Error Response

```json
{
"stat": "Not_Ok",
"emsg": "Session Expired :  Invalid Session Key"
}
```

## Modifying Orders

POST - /NorenWClientTP/ModifyOrder

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| exch* |  | Exchange |
| norenordno* |  | Noren order number, which needs to be modified |
| prctyp | LMT / MKT / SL-MKT / SL-LMT | This can be modified. |
| prc |  | Modified / New price |
| qty |  | Modified / New Quantity<br>Quantity to Fill / Order Qty - This is the total qty to be filled for the order. Its Open Qty/Pending Qty plus Filled Shares (cumulative for the order) for the order. * Please do not send only the pending qty in this field |
| tsym* |  | Unque id of contract on which order was placed. Can’t be modified, must be the same as that of original order. (use url encoding to avoid special char error for symbols like M&M) |
| ret | DAY / IOC / EOS | New Retention type of the order. |
| mkt_protection |  | Market order protection percentage. Applicable only for MKT orders in BSE/BFO/BCS and MCX segments. |
| trgprc |  | New trigger price in case of SL-MKT or SL-LMT |
| dscqty |  | Disclosed quantity (Max 10% for NSE, and 50% for MCX) |
| uid* |  | User id of the logged in user. |
| usr_agent |  | User Agent |
| app_inst_id |  | App Install Id |
| bpprc |  | Book Profit Price applicable only if product is selected as B (Bracket order ) |
| blprc |  | Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order ) |
| trailprc |  | Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order ). |
| ipaddr |  | global Ip of internet access |

Example

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientTP/ModifyOrder \
-H "Content-Type: application/json" \
-d '{"jData":{"uid":"ZXX123N","exch":"NSE","norenordno":"29052024844658","prctyp":"MKT","prc":"0","qty":"10","tsym":"TCS-EQ","ret":"DAY","mkt_protection":"2","prc":"0","dscqty":"0"},"jKey":"076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/ModifyOrder"
data ={"uid":"ZXX123N","exch":"NSE","norenordno":"29052024844658","prctyp":"MKT","prc":"0","qty":"10","tsym":"TCS-EQ","ret":"DAY","mkt_protection":"2","prc":"0","dscqty":"0"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data ={"uid":"ZXX123N","exch":"NSE","norenordno":"29052024844658","prctyp":"MKT","prc":"0","qty":"10","tsym":"TCS-EQ","ret":"DAY","mkt_protection":"2","prc":"0","dscqty":"0"}
var raw = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/ModifyOrder", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/ModifyOrder";
var jsonData = data ={"uid":"ZXX123N","exch":"NSE","norenordno":"29052024844658","prctyp":"MKT","prc":"0","qty":"10","tsym":"TCS-EQ","ret":"DAY","mkt_protection":"2","prc":"0","dscqty":"0"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/ModifyOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json =new JSONObject();
      json.put("uid", "ZXX123N");
      json.put("exch", "NFO");
      json.put("norenordno", "24033000000002");
      json.put("tsym", "BANKNIFTY25JAN23P53000");
      json.put("prctyp", "MKT");
      json.put("prc", "0");
      json.put("qty", "10");
      json.put("ret", "DAY");
      json.put("mkt_protection", "2");
      json.put("dscqty", "0");

      String payload =  "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
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

  url := "https://go.mynt.in/NorenWClientTP/ModifyOrder"
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
    "prc": "0",
    "dscqty": "0"
  }`
  payload := strings.NewReader("jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832")

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

Response Details

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Modify order success or failure indication. |
| result |  | Noren Order number of the order modified. |
| request_time |  | Response received time. |
| emsg |  | This will be present only if Order modification fails |

Sample Success Response

```json
{
"request_time":"14:14:08 26-05-2020",
"stat":"Ok",
"result":"XXXXXXXXXX"
}
```

Sample Failure Response

```json
{
"request_time":"16:03:29 28-05-2020",
"stat":"Not_Ok",
"emsg":"Rejected : ORA:Order not found"
}
```

## Cancelling Orders

POST - https://go.mynt.in/NorenWClientTP/CancelOrder

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| norenordno* |  | Noren order number, which needs to be modified |
| uid* |  | User id of the logged in user. |

Example

**curl**

```bash
curl https://go.mynt.in/NorenWClientTP/CancelOrder
jData= {"uid":"ZXX123N","norenordno":"24033000000002"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/CancelOrder"
data = {"uid":"ZXX123N","norenordno":"24033000000002"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}

response = requests.post( url, headers=headers, data=payload)

print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123N","norenordno":"24033000000002"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/CancelOrder", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/CancelOrder";
var jsonData = new {uid = "ZXX123N",norenordno="24033000000002"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/CancelOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json = new JSONObject();
      json.put("uid","ZXX123N");
      json.put("norenordno", "24033000000002")
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

url := "https://go.mynt.in/NorenWClientTP/CancelOrder"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N","norenordno":"24033000000002"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

client := &http.Client {
}
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

Response Details

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Cancel order success or failure indication. |
| result |  | Noren Order number of the canceled order. |
| request_time |  | Response received time. |
| emsg |  | This will be present only if Order cancelation fails |

Sample Success Response

```json
{
    "request_time":"14:14:10 26-05-2020",
    "stat":"Ok",
    "result":"XXXXXXXXXX"
}
```

Sample Failure Response

```json
{
    "request_time":"16:01:48 28-05-2020",
    "stat":"Not_Ok",
    "emsg":"Rejected : ORA:Order not found to Cancel"
}
```

## Retrieving orders

POST - https://go.mynt.in/NorenWClientTP/OrderBook

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| prd | H / M / ... | Product name |

Example

**curl**

```bash
curl https://go.mynt.in/NorenWClientTP/OrderBook
jData= {"uid":"ZXX123N"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/OrderBook"
data = {"uid":"ZXX123N"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123N"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/OrderBook", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/OrderBook";
var jsonData = new {uid = "ZXX123N"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/OrderBook");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json =new JSONObject();
      json.put("uid","ZXX123N")
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

 url := "https://go.mynt.in/NorenWClientTP/OrderBook"
 method := "POST"

 payload := strings.NewReader(`jData={"uid":"ZXX123N"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

 client := &http.Client {
 }
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

Response Details

Response data will be in json Array of objects with below fields in case of success.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Order book success or failure indication. |
| uid |  | User Id |
| actid |  | Account ID |
| exch |  | Exchange Segment |
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
| exchordid |  | Exchange Order Number |
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
| exch_tm |  | Exchange update time Format: dd-mm-YYYY hh:MM:SS |
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

Response data will be in json format with below fields in case of failure

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Not_Ok | Order book failure indication. |
| request_time |  | Response received time. |
| emsg |  | Error message |

Sample Success Output

```json
[
    {
        “stat” : “Ok”,
        “exch” : “NSE” ,
        “tsym” : “ACC-EQ” ,
        “norenordno” : “24033000000002”,
        “prc” : “127230”,
        “qty” : “100”,
        “prd” : “C”,
        “status”: “Open”,
        “trantype” : “B”,
        “prctyp” : ”LMT”,
        “fillshares” : “0”,
        “avgprc” : “0”,
        “exchordid” : “250620000000343421”,
        “uid” : “ZXX123N”,
        “actid” : “ZXX123N”,
        “ret” : “DAY”,
        “amo” : “Yes”
    },
    {
        “stat” : “Ok”,
        “exch” : “NSE” ,
        “tsym” : “ABB-EQ” ,
        “norenordno” : “24033000000002”,
        “prc” : “127830”,
        “qty” : “50”,
        “prd” : “C”,
        “status”: “REJECT”,
        “trantype” : “B”,
        “prctyp” : ”LMT”,
        “fillshares” : “0”,
        “avgprc” : “0”,
        “rejreason” : “Insufficient funds”
        “uid” : “ZXX123N”,
        “actid” : “ZXX123N”,
        “ret” : “DAY”,
        “amo” : “No”
    }
]
```

Sample Failure Response

```json
{
    "stat":"Not_Ok",
    "emsg":"Session Expired : Invalid Session Key"
}
```

## Retrieving an order's history

POST - `https://go.mynt.in/NorenWClientTP/SingleOrdHist`

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | User Id |
| norenordno* |  | Noren Order Number |

Example

**curl**

```bash
curl  https://go.mynt.in/NorenWClientTP/SingleOrdHist
jData= {"uid":"ZXX123N"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json
url = "https://go.mynt.in/NorenWClientTP/SingleOrdHist"
data = {"uid":"ZXX123N","norenordno":"24033000000002"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123N","norenordno":"24033000000002"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/SingleOrdHist", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/SingleOrdHist";
var jsonData = new {uid = "ZXX123N",norenordno="24033000000002"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/SingleOrdHist");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json=new JSONObject();
      json.put("uid","ZXX123N");
      json.put("norenordno", "24033000000002");
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

url := "https://go.mynt.in/NorenWClientTP/SingleOrdHist"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N","norenordno":"24033000000002"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

client := &http.Client {
}
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

Response Details

Response data will be in json Array of objects with below fields in case of success.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Order book success or failure indication. |
| exch |  | Exchange Segment |
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
| exchordid |  | Exchange Order Number |
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

Response data will be in json format with below fields in case of failure

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Not_Ok | Order book failure indication. |
| request_time |  | Response received time. |
| emsg |  | Error message |

Sample Success Output

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

## Retrieving all trades

POST - https://go.mynt.in/NorenWClientTP/TradeBook

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | User Id |
| actid* |  | Account Id of logged in user |

Example

**curl**

```bash
curl https://go.mynt.in/NorenWClientTP/TradeBook
jData= {"uid":"ZXX123N","actid":"ZXX123N"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/TradeBook"
data = {"uid":"ZXX123N","actid":"ZXX123N"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123N","actid":"ZXX123N"};
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/TradeBook", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/TradeBook";
var jsonData = new {uid = "ZXX123N",actid = "ZXX123N"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/TradeBook");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json =new JSONObject();
      json.put("uid","ZXX123N");
      json.put("actid", "ZXX123N");
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

url := "https://go.mynt.in/NorenWClientTP/TradeBook"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N","actid":"ZXX123N"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

client := &http.Client {
}
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

Response Details

Response data will be in json Array of objects with below fields in case of success.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Order book success or failure indication. |
| exch |  | Exchange Segment |
| qty |  | Order Quantity |
| tsym |  | Trading symbol / contract on which order is placed. |
| norenordno |  | Noren Order Number |
| prd |  | Display product alias name, using prarr returned in user details. |
| trantype | B / S | Transaction type of the order |
| prctyp | LMT / MKT | Price type |
| fillshares |  | Total Traded Quantity of this order |
| exchordid |  | Exchange Order Number |
| remarks |  | Any message Entered during order entry. |
| ret | DAY / IOC / EOS | Order validity |
| uid |  | Logged in User Id |
| actid |  | Login users account ID |
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
| exch_tm |  | Exchange update time Format: dd-mm-YYYY hh:MM:SS |
| snoordt |  | 0 for profit leg and 1 for stoploss leg |
| snonum |  | This field will be present for product H and B; and only if it is profit/sl order. |

Response data will be in json format with below fields in case of failure

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Not_Ok | Order book failure indication. |
| request_time |  | Response received time. |
| emsg |  | Error message |

Sample Success Output

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
        "norentm": "19:59:32 13-12-2020"
        "exch_tm": "01-01-1980 00:00:00",
        "remarks": "WC TEST Order",
        "exchordid": "6858"
    }
]
```

## GTT Order

### Place GTTOrder

POST - https://go.mynt.in/NorenWClientTP/PlaceGTTOrder

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| actid* |  | Login users account ID |
| exch* | NSE / NFO / BSE / MCX | Exchange (Select from ‘exarr’ Array provided in User Details response) |
| tsym* |  | Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M) |
| qty* |  | Order Quantity |
| prc* |  | Order Price |
| prd* | C / M / H | Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call) |
| trantype* | B / S | B -> BUY, S -> SELL |
| prctyp* | LMT / MKT /SL-LMT / SL-MKT / DS / 2L / 3L |  |
| ret* | DAY / EOS / IOC | Retention type (Show options as per allowed exchanges) |
| ai_t* |  |  |
| validity* |  |  |
| d* |  |  |

Example

**curl**

```bash
curl   https://go.mynt.in/NorenWClientTP/PlaceGTTOrder
jData={"uid":"ZXX123N","tsym":"RELIANCE-EQ","exch":"NSE","ai_t":"LTP_B_O","validity":"GTT","d":"12","trantype":"B","prctyp":"LMT","prd":"C","ret":"DAY","actid":"ZXX123N","qty":"","prc":"146.4"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/PlaceGTTOrder"

payload = jData={"uid":"ZXX123N","tsym":"RELIANCE-EQ","exch":"NSE","ai_t":"LTP_B_O","validity":"GTT","d":"12","trantype":"B","prctyp":"LMT","prd":"C","ret":"DAY","actid":"ZXX123N","qty":"","prc":"146.4"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
headers = {'Content-Type': 'application/json'}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = jData={"uid":"ZXX123N","tsym":"RELIANCE-EQ","exch":"NSE","ai_t":"LTP_B_O","validity":"GTT","d":"12","trantype":"B","prctyp":"LMT","prd":"C","ret":"DAY","actid":"ZXX123N","qty":"1","prc":"146.4"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832;

var requestOptions = {
method: 'POST',
headers: myHeaders,
body: raw,
redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientTP/PlaceGTTOrder", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/PlaceGTTOrder";
var jsonData = new {uid = "ZXX123N",tsym="RELIANCE-EQ",actid="ZXX123N",exch="NSE",ai_t="LTP_B_O",qty ="1",validity="GTT",d="12",trantype="B",prc="146.4",prd="C",prctyp ="LMT",ret ="DAY"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/PlaceGTTOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json= new JSONObejct();
      json.put("uid","ZXX123N");
      json.put("tsym","RELIANCE-EQ");
      json.put("exch","NSE");
      josn.put("ai_t","LTP_B_O");
      json.put("validity", "GTT");
      json.put("d","12");
      json.put("trantype","B");
      json.put("prctyp","LMT");
      json.put("prd","C");
      json.put("ret","DAY");
      json.put("actid","ZXX123N");
      json.put("qty","1");
      json.put("prc","146.4");
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

url := "https://go.mynt.in/NorenWClientTP/PlaceGTTOrder"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N","tsym":"RELIANCE-EQ","exch":"NSE","ai_t":"XXXXX","validity":"XXXXX","d":"XXXXX","trantype":"","prctyp":"XXXXX","prd":"C","ret":"DAY","actid":"ZXX123N","qty":"1","prc":"146.4"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
client := &http.Client {
}
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

Response Details

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | PlaceGTTOrder success or failure indication. |
| request_time |  | Response received time. |
| emsg |  | This will be present only if PlaceGTTOrder fails |

Sample Success Response

```json
{
  "request_time": "11:07:57 05-04-2023",
  "stat": "OI created",
  "al_id": "XXXXXXXXXX"
}
```

Sample Error Response

```json
{
 "stat": "Not_Ok",
 "emsg": "Session Expired :  Invalid User Id"
}
```

### Get Pending GTTOrder

POST - https://go.mynt.in/NorenWClientTP/GetPendingGTTOrder

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |

Example

**curl**

```bash
curl   https://go.mynt.in/NorenWClientTP/GetPendingGTTOrder
jData={"uid":"ZXX123N"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/GetPendingGTTOrder"
data = {"uid":"ZXX123N"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123N"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/GetPendingGTTOrder", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/GetPendingGTTOrder";
var jsonData = new {uid = "ZXX123N"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/GetPendingGTTOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json= new JSONObejct();
      json.put("uid","ZXX123N");
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

url := "https://go.mynt.in/NorenWClientTP/GetPendingGTTOrder"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

client := &http.Client {
}
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

Response Details

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | stat Ok or Not_Ok Limits request success or failure indication. |
| emsg |  | This will be present only in a failure response. |

Sample Success Response

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
     "ipaddr": "XXXXS
   },
      "d": "",
     "oivariable": [
   {
     "var_name": "x",
     "d": "XXX"
   }
  ]
  },

  ]
```

Sample Error Response

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired :  User Id "
}
```

### Get Enabled GTTs

POST - https://go.mynt.in/NorenWClientTP/GetEnabledGTTs

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |

Example

**curl**

```bash
curl   https://go.mynt.in/NorenWClientTP/GetEnabledGTTs
jData={"uid":"ZXX123N"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/GetEnabledGTTs"
data = {"uid":"ZXX123N"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123N"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/GetEnabledGTTs", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/GetEnabledGTTs";
var jsonData = new {uid = "ZXX123N"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/GetEnabledGTTs");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json= new JSONObejct();
      json.put("uid","ZXX123N");
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

url := "https://go.mynt.in/NorenWClientTP/GetEnabledGTTs"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

client := &http.Client {
}
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

Response Details

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Place order success or failure indication. |
| request_time |  | Response received time. |
| emsg |  | This will be present only if Order placement fails |

Sample Success Response

```json
{
  "stat": "Ok",
  "request_time": "05042023150257",
  "ai_ts": []
}
```

Sample Error Response

```json
{
 "stat": "Not_Ok",
 "emsg": "Session Expired :  Invalid User Id"
}
```

### Modify GTTOrder

POST - https://go.mynt.in/NorenWClientTP/ModifyGTTOrder

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| tsym* |  | Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M) |
| exch* | NSE / NFO / BSE / MCX | Exchange (Select from ‘exarr’ Array provided in User Details response) |
| ai_t* |  |  |
| validity* |  |  |
| al_id* |  |  |
| d* |  |  |
| trantype* | B / S | B -> BUY, S -> SELL |
| prctyp* | LMT / MKT /SL-LMT / SL-MKT / DS / 2L / 3L |  |
| prd* | C / M / H | Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call) |
| ret* | DAY / EOS / IOC | Retention type (Show options as per allowed exchanges) |
| actid* |  | Login users account ID |
| qty* |  | Order Quantity |
| prc* |  | Order Price |

Example

**curl**

```bash
curl   https://go.mynt.in/NorenWClientTP/ModifyGTTOrder
jData={"uid":"ZXX123N","tsym":"PGINVIT","exch":"BSE","ai_t":"LTP_B_O","validity":"GTT","al_id":"24032700000188","d":"11","trantype":"B","prctyp":"MKT","prd":"DAY","ret":"DAY","actid":"ZXX123N","qty":"1","prc":"0"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/ModifyGTTOrder"
data = {"uid":"ZXX123N","tsym":"PGINVIT","exch":"BSE","ai_t":"LTP_B_O","validity":"GTT","al_id":"24032700000188","d":"11","trantype":"B","prctyp":"MKT","prd":"DAY","ret":"DAY","actid":"ZXX123N","qty":"1","prc":"0"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {
           'Content-Type': 'application/json'
          }
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data ={"uid":"ZXX123N","tsym":"PGINVIT","exch":"BSE","ai_t":"LTP_B_O","validity":"GTT","al_id":"24032700000188","d":"11","trantype":"B","prctyp":"MKT","prd":"DAY","ret":"DAY","actid":"ZXX123N","qty":"1","prc":"0"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";

var requestOptions = {
method: 'POST',
headers: myHeaders,
body: raw,
redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientTP/ModifyGTTOrder", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/ModifyGTTOrder";
var jsonData = new {uid = "ZXX123N",actid="ZXX123N",tsym="PGINVIT",exch="BSE",ai_t="LTP_B_O",validity="GTT",al_id ="24032700000188",d="11",trantype="B",prctyp ="MKT",prd="C",ret ="DAY",qty ="1",prc="0"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/ModifyGTTOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json= new JSONObejct();
      json.put("uid","ZXX123N");
      json.put("tsym","PGINVIT");
      json.put("exch","BSE");
      josn.put("ai_t","LTP_B_O");
      json.put("validity", "GTT");
      json.put("d","11");
      json.put("trantype","B");
      json.put("prctyp","MKT");
      json.put("prd","C");
      json.put("ret","DAY");
      json.put("actid","ZXX123N");
      json.put("qty","1");
      json.put("prc","146.4");
       json.put("al_id","24032700000188");
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

url := "https://go.mynt.in/NorenWClientTP/ModifyGTTOrder"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N","tsym":"PGINVIT","exch":"BSE","ai_t":"LTP_B_O","validity":"GTT","al_id":"24032700000188","d":"11","trantype":"XXXXX","prctyp":"X","prd":"DAY","ret":"ZXX123N","actid":"","qty":"XX4","prc":"146.4"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

client := &http.Client {
}
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

Response Details

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Login Success Or failure status. |
| request_time |  | Response received time. |
| emsg |  | This will be present only in a failure response. |

Sample Success Response

```json
{
  "request_time": "XXXXXXXX",
  "stat": "Invalid Oi",
  "al_id": "XXXX"
}
```

Sample Error Response

```json
{
 "stat": "Not_Ok",
 "emsg": "Session Expired :  Invalid User Id"
}
```

### Cancel GTTOrder

POST - https://go.mynt.in/NorenWClientTP/CancelGTTOrder

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| al_id* |  |  |

Example

**curl**

```bash
curl   https://go.mynt.in/NorenWClientTP/CancelGTTOrder
jData={"uid":"ZXX123N","al_id":"24040300000211"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/CancelGTTOrder"
data= {"uid":"ZXX123N","al_id":"24040300000211"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {
           'Content-Type': 'application/json'
          }

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data ={"uid":"ZXX123N","al_id":"24040300000211"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";

var requestOptions = {
method: 'POST',
headers: myHeaders,
body: raw,
redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientTP/CancelGTTOrder", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/CancelGTTOrder";
var jsonData = new {uid = "ZXX123N",al_id ="24040300000211"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/CancelGTTOrder");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json= new JSONObejct();
      json.put("uid","ZXX123N");
       json.put("al_id","24040300000211");
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

url := "https://go.mynt.in/NorenWClientTP/CancelGTTOrder"
method := "POST"

payload := strings.NewReader(`jData={"uid":"ZXX123N","al_id":"24040300000211"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

client := &http.Client {
}
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

Response Details

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Login Success Or failure status. |
| request_time |  | Response received time. |
| emsg |  | This will be present only in a failure response. |

Sample Success Response

```json
{
   "request_time": "16:51:42 03-04-2022",
  "stat": "OI deleted",
  "al_id": "24040300000211"
}
```

Sample Error Response

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired :  Invalid User Id"
}
```
