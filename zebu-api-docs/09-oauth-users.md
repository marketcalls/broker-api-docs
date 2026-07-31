# Users

> Source: <https://zebumyntapi.web.app/OAuth/Users/>

> **OAuth Authentication Required**
>
> All user management API requests require OAuth authentication. Include your Bearer Token in the Authorization header of each HTTP request.

## Overview

The Users APIs provide access to user management functionalities including:
- **Client Details**: Retrieve detailed information about the logged-in user
- **Logout**: End the current user session

## Authentication

All API requests must include the OAuth access token in the Authorization header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## Client Details

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}//NorenWClientAPI/ClientDetails | Retrieves comprehensive client account information including user ID, account details, and broker information |

```bash
curl --location 'https://uat.mynt.in/NorenWClientAPI/ClientDetails'
--header 'Content-Type: text/plain'
--header 'Authorization: Bearer 584b99149bf55221XXXXXXXXXXXXX4fe2db35XXXXXXXXX8'
--data 'jData={"uid":"ZP0XXXX","actid":"ZP0XXXX"}'
```

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required user parameters |

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| uid |  | User ID of the authenticated user |
| actid |  | Account ID of the logged-in user |
| brkname |  | Broker ID of the logged-in user |

**Example**

**cURL**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/ClientDetails \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZP0XXXX","actid": "ZP0XXXX","brkname": "ZEBU"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/ClientDetails"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {
    "uid": "ZXX123M",
    "actid": "ZXX123M",
    "brkname": "ZEBU"
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
  "brkname": "ZEBU"
};
var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: "jData=" + JSON.stringify(data),
  redirect: 'follow'
};
fetch("https://go.mynt.in/NorenWClientAPI/ClientDetails", requestOptions)
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
        var url = "https://go.mynt.in/NorenWClientAPI/ClientDetails";
        var httpClient = new HttpClient();
        httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

        var jsonData = new {
            uid = "ZXX123M",
            actid = "ZXX123M",
            brkname = "ZEBU"
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
            URL url = new URL("https://go.mynt.in/NorenWClientAPI/ClientDetails");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "text/plain");
            conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

            JSONObject json = new JSONObject();
            json.put("uid", "ZXX123M");
            json.put("actid", "ZXX123M");
            json.put("brkname", "ZEBU");

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
    url := "https://go.mynt.in/NorenWClientAPI/ClientDetails"

    data := map[string]interface{}{
        "uid": "ZXX123M",
        "actid": "ZXX123M",
        "brkname": "ZEBU",
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

| Field | Type | Description |
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

| Fields | Type | Description |
| --- | --- | --- |
| bankn |  | Bank name |
| acctnum |  | Account number |

Dp_acct_num Obj format

| Fields | Type | Description |
| --- | --- | --- |
| dpnum |  | Dp account number |

Mandate_id_list Obj format

| Fields | Type | Description |
| --- | --- | --- |
| mandate_id |  | Mandate Id |

**Sample Success Response**

```json
{
  "request_time": "16:01:51 04-10-2025",
  "actid": "ZPXXXXX",
  "cliname": "ABC",
  "act_sts": "Activated",
  "creatdte": "1672987491",
  "creattme": "1759571790",
  "m_num": "1234567890",
  "email": "ABC@GMAIL.COM",
  "pan": "BJXXXXXXXX",
  "dob": "",
  "addr": "Flat 202, 2nd Floor  Sunrise Residency, Haryana – 122003  India",
  "addroffice": "",
  "addrcity": "",
  "addrstate": "",
  "partic_id_list": [
    {
      "partic_id": "",
      "exch": "NSE"
    },
    {
      "partic_id": "",
      "exch": "NFO"
    },
    {
      "partic_id": "",
      "exch": "CDS"
    },
    {
      "partic_id": "",
      "exch": "MCX"
    },
    {
      "partic_id": "",
      "exch": "BSE"
    },
    {
      "partic_id": "",
      "exch": "BFO"
    },
    {
      "partic_id": "",
      "exch": "BCD"
    },
    {
      "partic_id": "",
      "exch": "NCOM"
    },
    {
      "partic_id": "",
      "exch": "BSTAR"
    }
  ],
  "eqt_asba": "false",
  "der_asba": "false",
  "fx_asba": "false",
  "com_asba": "false",
  "mandate_id_list": [],
  "exarr": [
    "NSE",
    "NFO",
    "CDS",
    "BSE",
    "BFO",
    "BCD",
    "NCOM",
    "BSTAR"
  ],
  "bankdetails": [
    {
      "bankn": "XYZ Bank",
      "acctnum": "XXXXXXXXX",
      "ifsc_code": "ICIXXXXXXXX"
    }
  ],
  "dp_acct_num": [
    {
      "dpnum": "1208040000412718"
    }
  ],
  "stat": "Ok"
}
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired :  Invalid Session Key"
}
```

## Logout

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://{{Base URL}}/NorenWClientAPI/Logout | Terminates the current user session and invalidates the access token for secure logout |

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required user parameters |

| Fields | Type | Description |
| --- | --- | --- |
| uid |  | User Id of the login user |

**Example**

**cURL**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/Logout \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123M"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/Logout"
headers = {
    "Content-Type": "text/plain",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN"
}
data = {"uid": "ZXX123M"}
payload = "jData=" + json.dumps(data)
response = requests.post(url, data=payload, headers=headers)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");
myHeaders.append("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var data = {"uid": "ZXX123M"};
var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: "jData=" + JSON.stringify(data),
    redirect: 'follow'
};
fetch("https://go.mynt.in/NorenWClientAPI/Logout", requestOptions)
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
        var url = "https://go.mynt.in/NorenWClientAPI/Logout";
        var httpClient = new HttpClient();
        httpClient.DefaultRequestHeaders.Add("Authorization", "Bearer YOUR_ACCESS_TOKEN");

        var jsonData = new {uid = "ZXX123M"};
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
            URL url = new URL("https://go.mynt.in/NorenWClientAPI/Logout");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "text/plain");
            conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

            JSONObject json = new JSONObject();
            json.put("uid", "ZXX123M");

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
    url := "https://go.mynt.in/NorenWClientAPI/Logout"

    data := map[string]interface{}{
        "uid": "ZXX123M",
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

Response data will be in json format with below fields.

| Fields | Type | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Logout Success Or failure status |
| request_time |  | It will be present only on successful logout. |
| emsg |  | This will be present only if Logout fails. |

**Sample Success Response**

```json
{
  "stat": "Ok",
  "request_time": "10:43:41 28-05-2020"
}
```

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Server Timeout : "
}
```
