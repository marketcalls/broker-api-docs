# Users

> Source: <https://zebumyntapi.web.app/Base/Users/>

## Login

POST - `https://go.mynt.in/NorenWClientTP/QuickAuth`

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| apkversion* |  | Application version. |
| pwd* |  | Sha256 of the user entered password. |
| factor2* |  | DOB or PAN as entered by the user. (DOB should be in DD-MM-YYYY) |
| vc* |  | Vendor code provided by noren team, along with connection URLs |
| appkey* |  | Sha256 of uid\|App_key detail in Introduction |
| imei* |  | Send mac if users logs in for desktop, imei is from mobile |
| addldivinf |  | Optional field, Value must be in below format: iOS - iosInfo.utsname.machine - iosInfo.systemVersion Android - androidInfo.model - androidInfo.version examples: iOS - iPhone 8.0 - 9.0 Android - Moto G - 9 PKQ1.181203.01 |
| ipaddr |  | Optional field |
| source | API |  |

Example

**curl**

```bash
curl   https://go.mynt.in/NorenWClientTP/QuickAuth
  jData={"uid":"ZXX123M","pwd":"7f0f73568c02b394f2e28962c484338bb9d64b9be8e86881999c8a5454c8df18","factor2":"########","apkversion":"1.0.8","imei":"","vc":"ZXX123M","appkey":"a9926f2ecd099bc2b691a889d6896957e402f4821d0d664c3d8f00d6b95001af","source":"API"}
```

**Python**

```python
import requests
import json
url = "https://go.mynt.in/NorenWClientTP/QuickAuth"
data ={"uid":"ZXX123M","pwd":"7f0f73568c02b394f2e28962c484338bb9d64b9be8e86881999c8a5454c8df18","factor2":"########","apkversion":"1.0.8","imei":"","vc":"ZXX123M","appkey":"a9926f2ecd099bc2b691a889d6896957e402f4821d0d664c3d8f00d6b95001af","source":"API"}
payload = "jData="+json.dumps(data)
headers = {'Content-Type': 'application/json'}
response = requests.post( url, headers=headers, data=payload)
print(response.text)
```

**Javascript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123M","pwd":"7f0f73568c02b394f2e28962c484338bb9d64b9be8e86881999c8a5454c8df18","factor2":"########","apkversion":"1.0.8","imei":"","vc":"ZXX123M","appkey":"a9926f2ecd099bc2b691a889d6896957e402f4821d0d664c3d8f00d6b95001af","source":"API"}
var raw = "jData="+JSON.stringify(data);
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/QuickAuth", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/QuickAuth";
var jsonData = new {uid="ZXX123M",pwd="x7f0f73568c02b394f2e28962c484338bb9d64b9be8e86881999c8a5454c8df18",factor2="########",apkversion="1.0.8",imei="",vc="ZXX123M",appkey="a9926f2ecd099bc2b691a889d6896957e402f4821d0d664c3d8f00d6b95001af",source="API"};
var jsonString = JsonConvert.SerializeObject(jsonData);
var payload = "jData=" + jsonString ;
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/QuickAuth");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json = new JSONObject();
      json.put("uid","ZXX123M");
      json.put("pwd","7f0f73568c02b394f2e28962c484338bb9d64b9be8e86881999c8a5454c8df18");
      json.put("factor2","########");
      json.put("apkversion","1.0.8");
      json.put("imei","");
      json.put("vc","ZXX123M");
      json.put("appkey","a9926f2ecd099bc2b691a889d6896957e402f4821d0d664c3d8f00d6b95001af");
      json.put("source","API");
      String payload = "jData="+json.toString();

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

Response Details

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Login Success Or failure status |
| susertoken |  | It will be present only on login success. This data to be sent in subsequent requests in jKey field and web socket connection while connecting. |
| lastaccesstime |  | It will be present only on login success. |
| spasswordreset | Y | If Y Mandatory password reset to be enforced. Otherwise the field will be absent. |
| exarr |  | Json array of strings with enabled exchange names |
| uname |  | User name |
| prarr |  | Json array of Product Obj with enabled products, as defined below. |
| actid |  | Account id |
| email |  | Email Id |
| brkname |  | Broker id |
| uid |  | UserId |
| brnchid |  | Region |
| emsg |  | This will be present only if Login fails. (Redirect to force change password if message is “Invalid Input : Password Expired” or “Invalid<br>Input : Change Password”) |

Sample Success Response

```json
{
"request_time": "18:07:30 20-01-2023",
"actid": "ZXX123M",
"access_type": [
          "TT",
          "MOB",
          "WEB",
          "API",
          "CPPAPI"
      ],
"uname": "ABCDEFFF",
"prarr": [
          {
          "prd": "C",
          "s_prdt_ali": "CNC",
          "exch":[
                  "NSE"
                ]
          },
          {
            "prd": "M",
            "s_prdt_ali": "NRML",
            "exch":[
                  "NFO",
                  "CDS",
                  "MCX"
                  ]
          },
          {
            "prd": "I",
            "s_prdt_ali": "MIS",
            "exch": [
                  "NSE",
                  "NFO",
                  "CDS",
                  "MCX"
              ]
          },
          {
            "prd": "F",
            "s_prdt_ali": "MTF",
            "exch": [
                  "NSE"
              ]
          },
          {
            "prd": "H",
            "s_prdt_ali": "CO",
            "exch": [
                  "NSE",
                  "NFO",
                  "CDS",
                  "MCX"
              ]
          },
          {
            "prd": "B",
            "s_prdt_ali": "BO",
            "exch": [
                  "NSE",
                  "NFO",
                  "CDS",
                  "MCX"
              ]
          }
      ],
      "stat": "Ok",
      "susertoken": "cfcf93704b4b6d771806a2847b309c0760a1c307ae6ed18c657bcc8a8697deec",
      "email": "xxxxxx@gmail.com",
      "uid": "ZXX123M",
      "brnchid": "HO",
      "totp_set": "1",
      "orarr": [
          "LMT",
          "MKT",
          "SL-LMT",
          "SL-MKT",
          "DS",
          "2L",
          "3L"
      ],
      "exarr": [
          "NSE",
          "NFO",
          "CDS",
          "MCX"
      ],
      "values": [
          "1"
      ],
      "mws": {
          "1": [
              {
                  "exch": "NFO",
                  "token": "35048",
                  "tsym": "NIFTY25JAN23F",
                  "instname": "FUTIDX",
                  "pp": "2",
                  "ls": "50",
                  "ti": "0.05",
                  "optt": "XX"
              },
              {
                  "exch": "NSE",
                  "token": "2885",
                  "tsym": "RELIANCE-EQ",
                  "instname": "EQ",
                  "pp": "2",
                  "ls": "1",
                  "ti": "0.05"
              }
          ]
      },
      "brkname": "ZEBU",
      "lastaccesstime": "1674218250"
  }
```

Sample Failure Response

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired :  Invalid Session Key"
}
```

Error Message list

| Message | Description |
| --- | --- |
| "Invalid Input : Missing jData" | Common error message of any of the API (dev issue) |
| “Invalid Input : Request data is missing.” | Common error message of any of the API (dev issue) |
| "Invalid Input : jData is not valid json object" | Common error message of any of the API (dev issue) |
| "Invalid Input : {<Mandatory field name 1>} {or <Mandatory field name n>}... is Missing." Example: | Common error message of any of the API (dev issue) |
| "Invalid Input : One or more input parameters are not in string format" | Common error message of any of the API (dev issue) |
| "Invalid Input : Invalid App Key" | API enablement configuration issue (dev/deploy issue) |
| "Invalid Input : Invalid Vendor code" | API enablement configuration issue (dev/deploy issue) |
| “Invalid Input : Latest app available, please update” | Version blocked at API server level |
| "Invalid Input : Wrong PAN/DOB" |  |
| "Invalid Input : Wrong Password" |  |
| "Invalid Input : Invalid User" |  |
| "Invalid Input : Deactivated" |  |
| "Invalid Input : Version blocked: Please download latest version" | Version blocked in OMS level |
| "Invalid Input : User Blocked due to multiple wrong attempts" |  |
| "Invalid Input : User Not enabled on : WEB" Or "Invalid Input : User Not enabled on : ---" | Depending on custom access type configured in the system message will change |
| "Error Occurred : 1 "unknown request"" Or “Server Timeout : ” | OMS is down and Web server only up, (EOD/BOD time) |
| "Invalid Input : Invalid Access Type" | API server instance is not configured to handle input access type. (Mismatch in API URL) |
| "Invalid Input : Password Expired" | Password expired after configured number of days, Redirect to Change password screen. |
| "Invalid Input : Change Password" | If password reset by admin/system, Redirect to Change password screen. |

## Client Details

POST - `https://go.mynt.in/NorenWClientTP/ClientDetails`

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| actid* |  | Login users account ID |
| brkname* |  | Login users broker ID |

Example

**curl**

```bash
curl   https://go.mynt.in/NorenWClientTP/ClientDetails
jData={"uid":"ZXX123M"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json
url = "https://go.mynt.in/NorenWClientTP/ClientDetails"
data = {"uid":"ZXX123M","actid":"ZXX123M","brkname":"ZEBU"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post(url,headers=headers,data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123M","actid":"ZXX123M","brkname":"ZEBU"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/ClientDetails", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/ClientDetails";
var jsonData = new {uid = "ZXX123M",actid = "ZXX123M",brkname = "ZEBU"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/ClientDetails");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json = new JSONObject();
      json.put("uid","ZXX123M");
      json.put("actide","ZXX123M");
      json.put("brkname","ZEBU");
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

  url := "https://go.mynt.in/NorenWClientTP/ClientDetails"
  method := "POST"

  payload := strings.NewReader(`jData={"uid":"ZXX123M","actid":"ZXX123M"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

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

Request Details :

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | User details success or failure indication. |
| actid |  | Account ID |
| creatdte |  | Creation date |
| creattme |  | Creation time |
| m_num |  | Mobile Number |
| email |  | Email ID |
| pan |  | PAN |
| addr |  | Address |
| addroffice |  | Office address |
| addrcity |  | City |
| addrstate |  | State |
| bankdetails |  | Array Object, details given below. |
| dp_acct_num |  | Array Object, details given below. |
| exarr | ["CDS" , "NSE", "NFO", "MCX", "BSE", "NCX", "BSTAR", "BCD" ] | Json array of strings with enabled exchange names |
| mandate_id_list |  | Mandate Id List [ Array Object, details given below.] |
| request_time |  | It will be present only in a successful response. |
| emsg |  | This will be present only in case of errors. |

Bankdetails Obj format

| Json Fields | Possible value | Description |
| --- | --- | --- |
| bankn |  | Bank name |
| acctnum |  | Account number |

Dp_acct_num Obj format

| Json Fields | Possible value | Description |
| --- | --- | --- |
| dpnum |  | Dp account number |

Mandate_id_list Obj format

| Json Fields | Possible value | Description |
| --- | --- | --- |
| mandate_id |  | Mandate Id |

Sample Success Response

```json
    {
    "request_time": "15:34:12 31-01-2023",
    "actid": "ZXX123M",
    "cliname": "NAMEXXXXXXXX",
    "act_sts": "Activated",
    "creatdte": "0",
    "creattme": "0",
    "m_num": "82628XXXXXX",
    "email": "XXXXXXXXXXXXX@gmail.com",
    "pan": "CLKPNXXXXE",
    "addr": "10B 8 xxxxxxxx yyyyyyy NNNNNNN CHENNAI TAMIL NADU 600001 INDIA",
    "addroffice": "",
    "addrcity": "",
    "addrstate": "",
    "mandate_id_list": [],
    "exarr": [
        "NSE"
    ],
    "bankdetails": [
        {
            "bankn": "UNION BANK OF INDIA",
            "acctnum": "11234xxxxxxxxxxxxx",
            "ifsc_code": "UBINxxxxxxx"
        }
    ],
    "dp_acct_num": [
        {
            "dpnum": "12xxxxxxxxxxxxxxx"
        }
    ],
    "stat": "Ok"
}
```

Sample Failure Response

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired :  Invalid Session Key"
}
```

## Limits

POST - `https://go.mynt.in/NorenWClientTP/Limits`

Request Details

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | Logged in User Id |
| actid* |  | Account id of the logged in user. |
| prd |  | Product name/td> |
| seg | CM / FO / FX / COM | Segment |
| exch |  | Exchange |

Example

**curl**

```bash
curl  https://go.mynt.in/NorenWClientTP/Limits
jData={"uid":"ZXX123M","actid":"ZXX123M"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json
url = "https://go.mynt.in/NorenWClientTP/Limits"
data = {"uid":"ZXX123M","actid":"ZXX123M"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post(url,headers=headers,data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123M","actid":"ZXX123M"}
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/Limits", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/Limits";
var jsonData = new {uid = "ZXX123M",actid = "ZXX123M"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/Limits");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json = new JSONObject();
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

  url := "https://go.mynt.in/NorenWClientTP/Limits"
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

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Limits request success or failure indication. |
| actid |  | Account id |
| prd |  | Product name |
| seg | CM / FO / FX | Segment |
| exch |  | Exchange |
| cash |  | Cash Margin available |
| payin |  | Total Amount transferred using Payins today |
| payout |  | Total amount requested for withdrawal today |
| brkcollamt |  | Prevalued Collateral Amount |
| unclearedcash |  | Uncleared Cash (Payin through cheques) |
| daycash |  | Additional leverage amount / Amount added to handle system errors - by broker. |
| exch |  | Exchange |
| marginused |  | Total margin / fund used today |
| mtomcurper |  | Mtom current percentage |
| cbu |  | CAC Buy used |
| csc |  | CAC Sell Credits |
| rpnl |  | Current realized PNL |
| unmtom |  | Current unrealized mtom |
| marprt |  | Covered Product margins |
| span |  | Span used |
| expo |  | Exposure margin |
| varelm |  | Var Elm Margin |
| premium |  | Premium used |
| grexpo |  | Gross Exposure |
| greexpo_d |  | Gross Exposure derivative |
| scripbskmar |  | Scrip basket margin |
| addscripbskmrg |  | Additional scrip basket margin |
| brokerage |  | Brokerage amount |
| collateral |  | Collateral calculated based on uploaded holdings |
| grcoll |  | Scrip basket margin |
| scripbskmar |  | Valuation of uploaded holding pre haircut |
| turnoverlmt |  |  |
| pendordvallmt |  |  |
| turnover |  | Turnover |
| pendordval |  | Pending Order value |
| rzpnl_e_i |  | Current realized PNL (Equity Intraday) |
| rzpnl_e_m |  | Current realized PNL (Equity Margin) |
| rzpnl_e_c |  | Current realized PNL (Equity Cash n Carry) |
| rzpnl_d_i |  | Current realized PNL (Derivative Intraday) |
| rzpnl_d_m |  | Current realized PNL (Derivative Margin) |
| rzpnl_f_i |  | Current realized PNL (FX Intraday) |
| rzpnl_f_m |  | Current realized PNL (FX Margin) |
| rzpnl_c_i |  | Current realized PNL (Commodity Intraday) |
| rzpnl_c_m |  | Current realized PNL (Commodity Margin) |
| uzpnl_e_i |  | Current unrealized MTOM (Equity Intraday) |
| uzpnl_e_m |  | Current unrealized MTOM (Equity Margin) |
| uzpnl_e_c |  | Current unrealized MTOM (Equity Cash n Carry) |
| uzpnl_d_i |  | Current unrealized MTOM (Derivative Intraday) |
| uzpnl_d_m |  | Current unrealized MTOM (Derivative Margin) |
| uzpnl_f_i |  | Current unrealized MTOM (FX Intraday) |
| uzpnl_f_m uzpnl_c_i Current unrealized MTOM (Commodity Intraday) |  | Current unrealized MTOM (FX Margin) |
| uzpnl_c_i |  | Current unrealized MTOM (Commodity Intraday) |
| uzpnl_c_m |  | Current unrealized MTOM (Commodity Margin) |
| span_d_i |  | Span Margin (Derivative Intraday) |
| span_d_m |  | Span Margin (Derivative Margin) |
| span_f_i |  | Span Margin (FX Intraday) |
| span_f_m |  | Span Margin (FX Margin) |
| span_c_i |  | Span Margin (Commodity Intraday) |
| span_c_m |  | Span Margin (Commodity Margin) |
| expo_d_i |  | Exposure Margin (Derivative Intraday) |
| expo_d_m |  | Exposure Margin (Derivative Margin) |
| expo_f_i |  | Exposure Margin (FX Intraday) |
| expo_f_m |  | Exposure Margin (FX Margin) |
| expo_c_i |  | Exposure Margin (Commodity Intraday) |
| expo_c_m |  | Exposure Margin (Commodity Margin) |
| premium_d_i |  | Option premium (Derivative Intraday) |
| premium_d_m |  | Option premium (Derivative Margin) |
| premium_f_i |  | Option premium (FX Intraday) |
| premium_f_m |  | Option premium (FX Margin) |
| premium_c_i |  | Option premium (Commodity Intraday) |
| premium_c_m |  | Option premium (Commodity Margin) |
| varelm_e_i |  | Var Elm (Equity Intraday) |
| varelm_e_m |  | Var Elm (Equity Margin) |
| varelm_e_c |  | Var Elm (Equity Cash n Carry) |
| marprt_e_h |  | Covered Product margins (Equity High leverage) |
| marprt_e_b |  | Covered Product margins (Equity Bracket Order) |
| marprt_d_h |  | Covered Product margins (Derivative High leverage) |
| marprt_d_b |  | Covered Product margins (Derivative Bracket Order) |
| marprt_f_h |  | Covered Product margins (FX High leverage) |
| marprt_f_b |  | Covered Product margins (FX Bracket Order) |
| marprt_c_h |  | Covered Product margins (Commodity High leverage) |
| marprt_c_b |  | Covered Product margins (Commodity Bracket Order) |
| scripbskmar_e_i |  | Scrip basket margin (Equity Intraday) |
| scripbskmar_e_m |  | Scrip basket margin (Equity Margin) |
| scripbskmar_e_c |  | Scrip basket margin (Equity Cash n Carry) |
| addscripbskmrg_ d_i |  | Additional scrip basket margin (Derivative Intraday) |
| addscripbskmrg_ d_m |  | Additional scrip basket margin (Derivative Margin) |
| addscripbskmrg_f _i |  | Additional scrip basket margin (FX Intraday) |
| addscripbskmrg_f _m |  | Additional scrip basket margin (FX Margin) |
| addscripbskmrg_ c_i |  | Additional scrip basket margin (Commodity Intraday) |
| addscripbskmrg_ c_m |  | Additional scrip basket margin (Commodity Margin) |
| brkage_e_i |  | Brokerage (Equity Intraday) |
| brkage_e_m |  | Brokerage (Equity Margin) |
| brkage_e_c |  | Brokerage (Equity CAC) |
| brkage_e_h |  | Brokerage (Equity High Leverage) |
| brkage_e_b |  | Brokerage (Equity Bracket Order) |
| brkage_d_i |  | Brokerage (Derivative Intraday) |
| brkage_d_m |  | Brokerage (Derivative Margin) |
| brkage_d_h |  | Brokerage (Derivative High Leverage) |
| brkage_d_b |  | Brokerage (Derivative Bracket Order) |
| brkage_f_i |  | Brokerage (FX Intraday) |
| brkage_f_m |  | Brokerage (FX Margin) |
| brkage_f_h |  | Brokerage (FX High Leverage) |
| brkage_f_b |  | Brokerage (FX Bracket Order) |
| brkage_c_i |  | Brokerage (Commodity Intraday) |
| brkage_c_m |  | Brokerage (Commodity Margin) |
| brkage_c_h |  | Brokerage (Commodity High Leverage) |
| brkage_c_b |  | Brokerage (Commodity Bracket Order) |
| peak_mar |  | Peak margin used by the client |
| request_time |  | This will be present only in a successful response. |
| emsg |  | This will be present only in a failure response. |

Sample Success Response

```json
{
  "request_time": "10:06:54 21-01-2023",
  "stat": "Ok",
  "prfname": "ZEBUETRADE",
  "cash": "0.00",
  "payin": "0.00",
  "payout": "0.00",
  "brkcollamt": "0.00",
  "unclearedcash": "0.00",
  "aux_daycash": "0.00",
  "aux_brkcollamt": "0.00",
  "aux_unclearedcash": "0.00",
  "daycash": "0.00",
  "turnoverlmt": "10000000000000.00",
  "pendordvallmt": "1000000000000.00",
  "blk_amt": "0.00"
}
```

Sample Failure Response :

```json
{
"stat": "Not_Ok",
"emsg": "Invalid Input :  Request data is missing."
}
```

## Logout

POST - https://go.mynt.in/NorenWClientTP/Logout

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData* |  | Should send json object with fields in below list |
| jKey* |  | Key Obtained on login success. |

Example

**curl**

```bash
curl  https://go.mynt.in/NorenWClientTP/Logout \
jData= {"uid":"ZXX123M"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832
```

**Python**

```python
import requests
import json
url = "https://go.mynt.in/NorenWClientTP/Logout"
data = ={"uid":"ZXX123M"}
payload = "jData="+json.dumps(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832"
headers = {'Content-Type': 'application/json'}
response = requests.post(url,headers=headers, data=payload)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
var data = {"uid":"ZXX123M"};
var raw = "jData="+JSON.stringify(data)+"&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832";
var requestOptions = {method: 'POST',headers: myHeaders,body: raw,redirect: 'follow'};
fetch("https://go.mynt.in/NorenWClientTP/Logout", requestOptions)
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
var url = "https://go.mynt.in/NorenWClientTP/Logout";
var jsonData = new {uid = "ZXX123M"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientTP/Logout");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "application/json");
      JSONObject json =new JSONObject();
      json.put("uid","ZXX123M");
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

  url := "https://go.mynt.in/NorenWClientTP/Logout"
  method := "POST"

  payload := strings.NewReader(`jData={"uid":"ZXX123M"}&jKey=076c487f63be8c809c281e22bc221a79eb37a2c498271edf35a94f1f33cf2832`)

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

| Json Fields | Possible value | Description |
| --- | --- | --- |
| uid* |  | User Id of the login user |

Response Details:

Response data will be in json format with below fields.

| Json Fields | Possible value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Logout Success Or failure status |
| request_time |  | It will be present only on successful logout. |
| emsg |  | This will be present only if Logout fails. |

Sample Success Response

```json
{
"stat":"Ok",
"request_time":"10:43:41 28-05-2020"
}
```

Sample Failure Response

```json
{
"stat":"Not_Ok",
"emsg":"Server Timeout : "
}
```
