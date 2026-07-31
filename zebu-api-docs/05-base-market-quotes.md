# Market Quotes

> Source: <https://zebumyntapi.web.app/Base/MarketQuotes/>

## Quotes

POST - https://go.mynt.in/NorenWClientTP/GetQuotes

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| exch |  | Exchange |
| token |  | Contract Token |

Example:

**curl**

```bash
curl https://go.mynt.in/NorenWClientTP/GetQuotes
jData= {"uid":"ZXX123M", "exch":"NSE" , "token":"2885"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/GetQuotes"
data = {"uid":"ZXX123M","exch":"NSE","token":"2885"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type","application/json");
var data = {"uid":"ZXX123M","exch":"NSE","token":"2885"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/GetQuotes", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/GetQuotes";
var jsonData = new {uid ="ZXX123M",exch ="NSE",token ="2885"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/GetQuotes");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json= new JOSNObject();
      json.put("uid","ZXX123M");
      json.put("exch","NSE");
      json.put("token","2885");
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

  url := "https://go.mynt.in/NorenWClientTP/GetQuotes"
  method := "POST"

  payload := strings.NewReader(`jData={"uid":"ZXX123M","exch":"NSE" , "token":"2885"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

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
| stat | Ok or Not_Ok | Watch list update success or failure indication. |
| request_time |  | It will be present only in a successful response. |
| exch | NSE, BSE, NFO ... | Exchange |
| tsym |  | Trading Symbol |
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
| token |  | Token |
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

Sample Success Response

```json
{
    "request_time":"12:05:21 18-05-2021",
    "stat":"Ok"
    ,"exch":"NSE",
    "tsym":"ACC-EQ",
    "cname":"ACC LIMITED",
    "symname":"ACC",
    "seg":"EQT",
    "instname":"EQ",
    "isin":"INE012A01025",
    "pp":"2",
    "ls":"1",
    "ti":"0.05",
    "mult":"1",
    "uc":"2093.95",
    "lc":"1713.25",
    "prcftr_d":"(1 / 1 ) * (1 / 1)",
    "token":"22",
    "lp":"0.00",
    "h":"0.00",
    "l":"0.00",
    "v":"0",
    "ltq":"0",
    "ltt":"05:30:00",
    "bp1":"2000.00",
    "sp1":"0.00",
    "bp2":"0.00",
    "sp2":"0.00",
    "bp3":"0.00",
    "sp3":"0.00",
    "bp4":"0.00",
    "sp4":"0.00",
    "bp5":"0.00",
    "sp5":"0.00",
    "bq1":"2",
    "sq1":"0",
    "bq2":"0",
    "sq2":"0",
    "bq3":"0",
    "sq3":"0",
    "bq4":"0",
    "sq4":"0",
    "bq5":"0",
    "sq5":"0",
    "bo1":"2",
    "so1":"0",
    "bo2":"0",
    "so2":"0",
    "bo3":"0",
    "so3":"0",
    "bo4":"0",
    "so4":"0",
    "bo5":"0",
    "So5":"0"
}
```

Sample Failure Response

```json
{
    "stat":"Not_Ok",
    "request_time":"10:50:54 10-12-2020",
    "emsg":"Error Occurred : 5 "no data" "
}
```

## OHLC Quotes

## LTP Quotes

## Historical candle data

### Get Time Price Data

POST - https://go.mynt.in/NorenWClientTP/TPSeries

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| exch* |  | Exchange |
| token* |  |  |
| st |  | Start time (seconds since 1 jan 1970) converter in Epoch formet |
| et |  | End Time (seconds since 1 jan 1970) converter in Epoch formet |
| intrv | “1”, ”3”, “5”, “10”, “15”, “30”, “60”, “120”, “240” | Candle size in minutes (optional field, if not given assume to be “1”) |

Example

**curl**

```bash
curl https://go.mynt.in/NorenWClientTP/TPSeries
jData = { "uid":"ZXX123M","exch":"NSE","token":"PAYTM-EQ","st":"1710698300","et":"1710863909","intrv":"5"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/TPSeries"
data = {"uid":"ZXX123M","exch":"NSE","token":"PAYTM-EQ","st":"1710698300","et":"1710863909","intrv":"5"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type","application/json");
var data = {"uid":"ZXX123M","exch":"NSE","token":"PAYTM-EQ","st":"1710698300","et":"1710863909","intrv":"5"};
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/TPSeries", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/TPSeries";
var jsonData = new {uid ="ZXX123M",exch ="NSE",token="PAYTM-EQ",st="1710698300",et="1710863909",intrv="5"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/TPSeries");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json= new JSONObject();
      json.put("uid", "ZXX123M");
      json.put("exch", "NSE");
      json.put("token","PAYTM-EQ");
      json.put("st","1710698300");
      json.put("et","1710863909");
      json.put("intrv","5");
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

  url := "https://go.mynt.in/NorenWClientTP/TPSeries"
  method := "POST"

  payload := strings.NewReader(`jData={"uid":"ZXX123M","exch":"NSE","token":"PAYTM-EQ","st":"1710698300","et":"1710863909","intrv":"5"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

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

Response data will be in json format in case for failure.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Not_Ok | TPData failure indication. |
| emsg |  | This will be present only in case of errors. |

Response data will be in json format in case for success.

| Json Fields | Possible value | Description |
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

Sample Success Response

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

Sample Failure Response

```json
{
 "stat":"Not_Ok",
 "emsg":"Session Expired : Invalid Session Key"
}
```

### EOD Chart Data

POST - https://go.mynt.in/NorenWClientTP/EODChartData

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| sym* |  | Symbol name |
| from* |  | From date converter in Epoch formet |
| to* |  | To date converter in Epoch formet |

Example

**curl**

```bash
curl https://go.mynt.in/NorenWClientTP/EODChartData
jData={"sym":"NSE:RELIANCE-EQ","from":1624838400,"to":1663718400}&jKey=GHUDWU53H32MTHPA536Q32WR
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/EODChartData"
data = {"sym":"NSE:RELIANCE-EQ","from":"1624838400","to":"1663718400"}
payload = "jData="+json.dumps(datqa)+"&jKey=GHUDWU53H32MTHPA536Q32WR"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"sym":"NSE:RELIANCE-EQ","from":"1624838400","to":"1663718400"}
var raw = "jData="+JOSN.stingify(data)+"&jKey=GHUDWU53H32MTHPA536Q32WR";
var requestOptions = { method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
 fetch("https://go.mynt.in/NorenWClientTP/EODChartData", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/EODChartData";
var jsonData = new {sym ="NSE:RELIANCE-EQ",from ="1624838400",to="1663718400"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData="+jsonString+"&jKey=GHUDWU53H32MTHPA536Q32WR";
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/EODChartData");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json= new JSONObject();
      json.put("sym", "NSE:RELIANCE-EQ");
      json.put("form", "1624838400");
      json.put("to", "1663718400");

      String payload = "jData="+json.toString()+"&jKey=GHUDWU53H32MTHPA536Q32WR";
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

  url := "https://go.mynt.in/NorenWClientTP/EODChartData"
  method := "POST"

  payload := strings.NewReader(`jData={"sym":"NSE:RELIANCE-EQ","from":1624838400,"to":1663718400}&jKey=GHUDWU53H32MTHPA536Q32WR`)

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

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| time |  | DD/MM/CCYY hh:mm:ss |
| into |  | Interval open |
| inth |  | Interval high |
| intl |  | Interval low |
| intc |  | Interval close |
| ssboe |  | Date,Seconds in 1970 format |
| intv |  | Interval volume |

Sample Success Response

```json
[
 "{
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
    }"
  ]
```

## Master Files

NSE CASH - [https://go.mynt.in/NSE_symbols.txt.zip](https://go.mynt.in/NSE_symbols.txt.zip)

NSE  F&O - [https://go.mynt.in/NFO_symbols.txt.zip](https://go.mynt.in/NFO_symbols.txt.zip)

NSE  CDS - [https://go.mynt.in/CDS_symbols.txt.zip](https://go.mynt.in/CDS_symbols.txt.zip)

BSE CASH - [https://go.mynt.in/BSE_symbols.txt.zip](https://go.mynt.in/BSE_symbols.txt.zip)

BSE  F&O - [https://go.mynt.in/BFO_symbols.txt.zip](https://go.mynt.in/BFO_symbols.txt.zip)

MCX      - [https://go.mynt.in/MCX_symbols.txt.zip](https://go.mynt.in/MCX_symbols.txt.zip)

## Market Info

#### Get Index List

POST - https://go.mynt.in/NorenWClientTP/GetIndexList

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| exch* |  | Exchange |

Example:

**curl**

```bash
curl    https://go.mynt.in/NorenWClientTP/GetIndexList
jData={ "uid*":"ZXX123M","exch":"NSE"}&jKey= 076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/GetIndexList"
data = {"uid":"ZXX123M","exch":"NSE"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123M","exch":"NSE"}
var raw = "jData="+JsON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
  fetch("https://go.mynt.in/NorenWClientTP/GetIndexList", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/GetIndexList";
var jsonData = new {uid = "ZXX123M",exch ="NSE"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/GetIndexList");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json = new JSONObject();
      json.put("uid", "ZXX123M");
      json.put("exch","NSE");
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

  url := "https://mynt.in/NorenWClientTP/GetIndexList"
  method := "POST"

  payload := strings.NewReader(`jData={ "uid*":"ZXX123M","exch":"NSE"}&jKey= 076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

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
| stat | Ok or Not_Ok | TopListNames success or failure indication |
| values |  | Array Of Basket, Criteria pair. |
| request_time |  | This will be present only in a successful response. |
| emsg |  | This will be present only in case of errors. |

Basket, Criteria pair Object :

| Json Fields | Possible value | Description |
| --- | --- | --- |
| idxname |  | Index Name |
| token |  | Index token used to subscribe |

Sample Success Response:

```json
{
"request_time": "20:12:29 13-12-2020",
"values": [
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
},
}
```

Sample Failure Response

```json
{
  "stat":"Not_Ok",
  "emsg":"Invalid Input : Missing uid or actid or prd."
}
```

#### Get Option Chain

POST - https://go.mynt.in/NorenWClientTP/GetOptionChain

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| tsym* |  | Trading symbol of any of the option or future. Option chain for that underlying will be returned. (use url encoding to avoid special char error for symbols like M&M) |
| exch* |  | Exchange (UI need to check if exchange in NFO / CDS / MCX / or any other exchange which has options, if not don't allow) |
| strprc* |  | Mid price for option chain selection |
| cnt* |  | Number of strike to return on one side of the mid price for PUT and CALL. (example cnt is 4, total 16 contracts will be returned, if cnt is is 5 total 20 contract will be returned) |

Example:

**curl**

```bash
curl    https://go.mynt.in/NorenWClientTP/GetOptionChain
jData={"uid":"ZXX123M","exch":"NFO","tsym":"RELIANCE25APR24P4120","cnt":"5","strprc":"2973.90"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/GetOptionChain"
data = {"uid":"ZXX123M","exch":"NSE","tsym":"RELIANCE25APR24P4120","cnt":"5","strprc":"2973.90"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers,data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123M","exch":"NSE","tsym":"RELIANCE25APR24P4120","cnt":"5","strprc":"2973.90"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/GetOptionChain", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/GetOptionChain";
var jsonData = new {uid = "ZXX123M",exch ="NSE",tsym ="RELIANCE25APR24P4120",cnt ="5",strprc ="2973.90"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/GetLinkedScrips");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json = new JSONObject()
      json.put("uid","ZXX123M");
      json.put("tsym","RELIANCE25APR24P4120");
      json.put("exch","NSE");
      json.put("strprc","2973.90");
      json.put("cnt", "5");
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

  url := "https://mynt.in/NorenWClientTP/GetLinkedScrips"
  method := "POST"

  payload := strings.NewReader(`jData={ "uid":"ZXX123M","tsym":"RELIANCE25APR24P4120","exch":"NSE","strprc":"2973.90","cnt":"5"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

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
| stat | Ok or Not_Ok | Market watch success or failure indication. |
| values |  | Array of json objects. (object fields given in below table) |
| emsg |  | This will be present only in case of errors. That is :<br><br>Invalid Input<br>Session Expired |

| Json Fields of object in values Array | Possible value | Description |
| --- | --- | --- |
| exch | CDS, NFO ... | Exchange |
| tsym |  | Trading symbol of the scrip (contract) |
| token |  | Token of the scrip (contract) |
| optt |  | Option Type |
| strprc |  | Strike price |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |

Sample Success Response

````json
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
                },
              ]
            }
 ```

<p>Sample Failure Response</p>

``` py
      {
      "stat":"Not_Ok",
      "emsg":"Invalid Input : Missing uid or actid or prd."
      }
````

### Get Linked Scrips

POST - https://go.mynt.in/NorenWClientTP/GetLinkedScrips

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| token* |  | Trading symbol of any of the options or future. Option chain for that underlying will be returned. (use url encoding to avoid special char error for symbols like M&M) |
| exch* |  | Exchange (UI need to check if exchange in NFO / CDS / MCX / or any other exchange which has options, if not don't allow) |

Example

```
jData={"uid":"ZXX123M","exch":"NSE","token":"2885"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientTP/GetLinkedScrips"
data = {"uid":"ZXX123M","exch":"NSE","token":"2885"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123M","exch":"NSE","token":"2885"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/GetLinkedScrips", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/GetLinkedScrips";
var jsonData = new {uid = "ZXX123M",exch ="NSE",token="2885"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/GetLinkedScrips");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json =new JSONObject();
      json.push("uid","ZXX123M");
      json.push("exch","NSE");
      json.push("token","2885");

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

  url := "https://mynt.in/NorenWClientTP/GetLinkedScrips"
  method := "POST"

  payload := strings.NewReader(`jData={"uid":"ZXX123M","exch":"NSE","token":"2885"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

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
| stat | Ok or Not_Ok | Market watch success or failure indication. |
| equls |  | Array of json objects equls. (object fields given in below table) |
| fut |  | Array of json objects fut. (object fields given in below table) |
| opt_exp |  | Array of json objects opt_exp. (object fields given in below table) |
| emsg |  | This will be present only in case of errors. That is :<br><br>Invalid Input<br>Session Expired |

| equls Json Fields of object in values Array | Possible value | Description |
| --- | --- | --- |
| exch | NSE, BSE ... | Exchange |
| tsym |  | Trading symbol of the scrip (contract) |
| token |  | Token of the scrip (contract) |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |
| mult |  | Contract price multiplier, (used for order value calculation) |

| fut Json Fields of object in values Array | Possible value | Description |
| --- | --- | --- |
| exch | NFO, MCX ... | Exchange |
| tsym |  | Trading symbol of the scrip (contract) |
| token |  | Token of the scrip (contract) |
| exd |  | Expiry date |
| pp |  | Price precision |
| ti |  | Tick size |
| ls |  | Lot size |
| mult |  | Contract price multiplier, (used for order value calculation) |

| opt_exp Json Fields of object in values Array | Possible value | Description (Used to show dropdown in option chain) |
| --- | --- | --- |
| exd |  | Used for calling option chain api |
| exch | NFO, MCX ... Ex | Exchange |
| tsym |  | One of the random Trading symbol on given expiry, useful in calling option chain |

Sample Success Response

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
  "mult": "1",
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

}
```

Sample Failure Response

```json
{
 "stat":"Not_Ok",
  "emsg":"Invalid Input : Missing uid or actid or prd."
}
```
