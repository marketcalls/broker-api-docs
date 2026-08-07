# Authentication

> Source: <https://zebumyntapi.web.app/OAuth/Authentication/>

> **OAuth 2.0 Authentication**
>
> Zebu APIs use OAuth 2.0 authentication to ensure secure access. All API requests must include a Bearer Token in the Authorization header.

## Overview

The OAuth 2.0 authentication process involves the following steps:

1. **Redirect User to Login**: Direct users to the Zebu OAuth login page
2. **User Authorization**: User logs in and authorizes your application
3. **Receive Authorization Code**: Your application receives an authorization code
4. **Exchange Code for Token**: Exchange the authorization code for an access token
5. **Make API Calls**: Use the access token to make authenticated API requests

## Redirect User to Login Page

| Method | APIs | Detail |
| --- | --- | --- |
| GET | https://go.mynt.in/OAuthlogin/authorize/oauth | Initiates OAuth 2.0 authorization flow by redirecting users to login page with client_id parameter for secure authentication |

Direct users to the Zebu OAuth login page with your client_id:

```
https://go.mynt.in/OAuthlogin/authorize/oauth?client_id=YOUR_CLIENT_ID
```

**Example:**

```
https://go.mynt.in/OAuthlogin/authorize/oauth?client_id=ZP0XXXX
```

## Receive Authorization Code

After successful login, the user will be redirected to your registered redirect URL with an authorization code:

```
https://your-redirect-url.com/callback?code=AUTHORIZATION_CODE
```

**Example:**

```
https://zebuetrade.com/?code=aafXXXXX-XXX7-4XX7-8XX8-8cXXXXXXXfa
```

Extract the `code` parameter from the redirect URL to use in the next step.

## Exchange Code for Access Token

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://go.mynt.in/NorenWClientAPI/GenAcsTok | Exchanges authorization code for access token and refresh token using SHA-256 checksum validation for secure API authentication |

Use the authorization code received in the previous step to obtain an access token.

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required authentication parameters |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| code |  | Authorization code received from the OAuth login redirect URL |
| checksum |  | SHA-256 hash generated from the concatenated client_id, secret_key, and authorization code for security validation<br><br>Example:<br><br>If your API's client id is ABC, secret code is 123, and code is x1y2z3, Combine them as: ABC123x1y2z3<br><br>Then generate the SHA-256 hash of that string.<br><br>**Input string:** ABC123x1y2z3<br><br>**SHA-256 hash:** 7d6bc03dfd8c1589620c52f4be08e50c04856ecf0022c7d81a |

**Example**

**cURL**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/GenAcsTok \
  -H "Content-Type: text/plain" \
  -d 'jData={"code": "c61de38b-7c0c-46e4-8abeacb1f6a15089","checksum": "e5ff9e0357cfa219885495ace4390b38280a39790ad434ea713afd27e6ec93"}'
```

**Python**

```python
import requests
import json
import hashlib

# Generate checksum
client_id = "ABC"
secret_key = "123"
code = "c61de38b-7c0c-46e4-8abeacb1f6a15089"
checksum_string = client_id + secret_key + code
checksum = hashlib.sha256(checksum_string.encode()).hexdigest()

# Make request
url = "https://go.mynt.in/NorenWClientAPI/GenAcsTok"
data = {
    "code": code,
    "checksum": checksum
}
payload = "jData=" + json.dumps(data)
headers = {"Content-Type": "text/plain"}
response = requests.post(url, data=payload, headers=headers)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");

// Generate checksum
const clientId = "ABC";
const secretKey = "123";
const code = "c61de38b-7c0c-46e4-8abeacb1f6a15089";
const checksumString = clientId + secretKey + code;
const checksum = CryptoJS.SHA256(checksumString).toString();

var data = {
    "code": code,
    "checksum": checksum
};

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: "jData=" + JSON.stringify(data),
    redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/GenAcsTok", requestOptions)
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
using System.Security.Cryptography;

class Program
{
    static void Main(string[] args)
    {
        // Generate checksum
        string clientId = "ABC";
        string secretKey = "123";
        string code = "c61de38b-7c0c-46e4-8abeacb1f6a15089";
        string checksumString = clientId + secretKey + code;
        string checksum = ComputeSha256Hash(checksumString);

        var url = "https://go.mynt.in/NorenWClientAPI/GenAcsTok";
        var jsonData = new {code = code, checksum = checksum};
        var jsonString = JsonConvert.SerializeObject(jsonData);
        var payload = "jData=" + jsonString;

        var httpClient = new HttpClient();
        var content = new StringContent(payload, Encoding.UTF8, "text/plain");
        var response = httpClient.PostAsync(url, content).Result;
        var responseString = response.Content.ReadAsStringAsync().Result;
        Console.WriteLine(responseString);
    }

    static string ComputeSha256Hash(string rawData)
    {
        using (SHA256 sha256Hash = SHA256.Create())
        {
            byte[] bytes = sha256Hash.ComputeHash(Encoding.UTF8.GetBytes(rawData));
            return Convert.ToHexString(bytes).ToLower();
        }
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
import java.security.MessageDigest;
import org.json.simple.JSONObject;

public class App {
    public static void main(String[] args) {
        try {
            // Generate checksum
            String clientId = "ABC";
            String secretKey = "123";
            String code = "c61de38b-7c0c-46e4-8abeacb1f6a15089";
            String checksumString = clientId + secretKey + code;
            String checksum = getSHA256(checksumString);

            URL url = new URL("https://go.mynt.in/NorenWClientAPI/GenAcsTok");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "text/plain");

            JSONObject json = new JSONObject();
            json.put("code", code);
            json.put("checksum", checksum);

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

    public static String getSHA256(String input) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hash = digest.digest(input.getBytes("UTF-8"));
            StringBuilder hexString = new StringBuilder();
            for (byte b : hash) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) {
                    hexString.append('0');
                }
                hexString.append(hex);
            }
            return hexString.toString();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
```

**Go**

```go
package main

import (
    "bytes"
    "crypto/sha256"
    "encoding/hex"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
)

func main() {
    // Generate checksum
    clientId := "ABC"
    secretKey := "123"
    code := "c61de38b-7c0c-46e4-8abeacb1f6a15089"
    checksumString := clientId + secretKey + code
    hash := sha256.Sum256([]byte(checksumString))
    checksum := hex.EncodeToString(hash[:])

    url := "https://go.mynt.in/NorenWClientAPI/GenAcsTok"

    data := map[string]interface{}{
        "code":     code,
        "checksum": checksum,
    }

    jsonData, _ := json.Marshal(data)
    payload := "jData=" + string(jsonData)
    req, err := http.NewRequest("POST", url, bytes.NewBufferString(payload))
    if err != nil {
        fmt.Println(err)
        return
    }

    req.Header.Set("Content-Type", "text/plain")

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

| Json Field | Possible Value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Token generation success or failure indication. |
| access_token | string | Present only on success. Bearer token for API authentication. |
| refresh_token | string | Present only on success. Token to refresh access token. |
| expires_in | string | Present only on success. Token expiration time in seconds. |
| request_time | string | Response received time. |
| emsg | string | Present only if token generation fails. |

**Sample Success Response**

```json
{
  "stat": "Ok",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "def50200a1b2c3d4e5f6...",
  "expires_in": "3600",
  "request_time": "10:06:54 21-01-2023"
}
```

**Sample Error Response**

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid authorization code",
  "request_time": "10:06:54 21-01-2023"
}
```

## Making Authenticated API Calls

Once you have the access token, you can make authenticated API calls by including it in the Authorization header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

**Example API Call:**

**cURL**

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
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");
myHeaders.append("Authorization", "Bearer YOUR_ACCESS_TOKEN");

var data = {
    "uid": "ZXX123M",
    "exch": "NSE",
    "token": "2885"
};

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: "jData=" + JSON.stringify(data),
    redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/GetQuotes", requestOptions)
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

    data := map[string]interface{}{
        "uid": "ZXX123M",
        "exch": "NSE",
        "token": "2885",
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

## Token Refresh

| Method | APIs | Detail |
| --- | --- | --- |
| POST | https://go.mynt.in/NorenWClientAPI/RefreshToken | Refreshes expired access token using valid refresh token to maintain continuous API access without re-authentication |

When the access token expires, you can use the refresh token to obtain a new access token without requiring the user to log in again.

Request Details :

| Parameter Name | Possible value | Description |
| --- | --- | --- |
| jData |  | JSON object containing the required authentication parameters |

| Json Fields | Possible value | Description |
| --- | --- | --- |
| refresh_token |  | The refresh token obtained from the initial authentication |

# Example

**cURL**

```bash
curl -X POST https://go.mynt.in/NorenWClientAPI/RefreshToken \
  -H "Content-Type: text/plain" \
  -d 'jData={"refresh_token": "def50200a1b2c3d4e5f6..."}'
```

**Python**

```python
import requests
import json

url = "https://go.mynt.in/NorenWClientAPI/RefreshToken"
data = {
    "refresh_token": "def50200a1b2c3d4e5f6..."
}
payload = "jData=" + json.dumps(data)
headers = {"Content-Type": "text/plain"}
response = requests.post(url, data=payload, headers=headers)
print(response.text)
```

**JavaScript**

```javascript
var myHeaders = new Headers();
myHeaders.append("Content-Type", "text/plain");

var data = {
    "refresh_token": "def50200a1b2c3d4e5f6..."
};

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: "jData=" + JSON.stringify(data),
    redirect: 'follow'
};

fetch("https://go.mynt.in/NorenWClientAPI/RefreshToken", requestOptions)
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
        var url = "https://go.mynt.in/NorenWClientAPI/RefreshToken";
        var httpClient = new HttpClient();

        var jsonData = new {refresh_token = "def50200a1b2c3d4e5f6..."};
        var jsonString = JsonConvert.SerializeObject(jsonData);
        var payload = "jData=" + jsonString;
        var content = new StringContent(payload, System.Text.Encoding.UTF8, "text/plain");
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
            URL url = new URL("https://go.mynt.in/NorenWClientAPI/RefreshToken");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setDoOutput(true);
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "text/plain");

            JSONObject json = new JSONObject();
            json.put("refresh_token", "def50200a1b2c3d4e5f6...");

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
    url := "https://go.mynt.in/NorenWClientAPI/RefreshToken"

    data := map[string]interface{}{
        "refresh_token": "def50200a1b2c3d4e5f6...",
    }

    jsonData, _ := json.Marshal(data)
    payload := "jData=" + string(jsonData)
    req, err := http.NewRequest("POST", url, bytes.NewBufferString(payload))
    if err != nil {
        fmt.Println(err)
        return
    }

    req.Header.Set("Content-Type", "text/plain")

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

# Response Details

Response data will be in json format with below fields.

| Json Field | Possible Value | Description |
| --- | --- | --- |
| stat | Ok or Not_Ok | Token refresh success or failure indication. |
| access_token | string | Present only on success. New bearer token for API authentication. |
| expires_in | string | Present only on success. Token expiration time in seconds. |
| request_time | string | Response received time. |
| emsg | string | Present only if token refresh fails. |

# Sample Success Response

```json
{
  "stat": "Ok",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": "3600",
  "request_time": "10:06:54 21-01-2023"
}
```

# Sample Error Response

```json
{
  "stat": "Not_Ok",
  "emsg": "Invalid refresh token",
  "request_time": "10:06:54 21-01-2023"
}
```
