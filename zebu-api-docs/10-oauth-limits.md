# Limits

> Source: <https://zebumyntapi.web.app/OAuth/Limits/>

> **OAuth Authentication Required**
>
> All limits API requests require OAuth authentication. Include your Bearer Token in the Authorization header of each HTTP request.

## Overview

The Limits API provides access to user trading limits and margin details across different segments and exchanges. This includes:

- **Cash Margins**: Available cash balance and margin details
- **Payin/Payout**: Amounts transferred and withdrawn today
- **Collateral**: Prevalued collateral amounts and uncleared cash
- **Margin Usage**: Total margin used, SPAN, exposure, and premium margins
- **P&L Details**: Realized and unrealized P&L across different segments
- **Brokerage**: Brokerage amounts for different product types
- **Turnover Limits**: Daily turnover and pending order value limits

## Authentication

All API requests must include the OAuth access token in the Authorization header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## API Endpoint

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | `https://go.mynt.in/NorenWClientAPI/Limits` | Retrieves comprehensive trading limits, margin details, P&L information, and brokerage data across all segments |

Request Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| uid | string | Yes | Logged in User ID |
| actid | string | Yes | Account ID of the logged in user |
| prd | string | No | Product name |
| seg | string | No | Segment (CM / FO / FX / COM) |
| exch | string | No | Exchange |

**Example**

**curl**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/Limits \
  -H "Content-Type: text/plain" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -d 'jData={"uid": "ZXX123M","actid": "ZXX123M"}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/Limits"
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

var data = {
    "uid": "ZXX123M",
    "actid": "ZXX123M"
};

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: "jData=" + JSON.stringify(data),
    redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/Limits", requestOptions)
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
        var url = "https://go.mynt.in/NorenWClientAPI/Limits";
        var jsonData = new {uid = "ZXX123M", actid = "ZXX123M"};
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
      URL url = new URL("https://go.mynt.in/NorenWClientAPI/Limits");
      HttpURLConnection conn = (HttpURLConnection) url.openConnection();
      conn.setDoOutput(true);
      conn.setRequestMethod("POST");
      conn.setRequestProperty("Content-Type", "text/plain");
      conn.setRequestProperty("Authorization", "Bearer YOUR_ACCESS_TOKEN");

      JSONObject json = new JSONObject();
      json.put("uid","ZXX123M");
      json.put("actid","ZXX123M");

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
  url := "https://go.mynt.in/NorenWClientAPI/Limits"
  method := "POST"

  payload := strings.NewReader('jData`{"uid":"ZXX123M","actid":"ZXX123M"}`')

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

Response data will be in JSON format with the following fields:

| Fields | Type | Description |
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

**Sample Success Response**

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

**Sample Failure Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid Input :  Request data is missing."
}
```
