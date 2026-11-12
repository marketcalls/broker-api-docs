# Deprecated APIs

Superseded login, 2FA, and static-IP endpoints. Kept for reference only — use the current [Authentication](04-authentication.md) and [Web Dashboard](03-dashboard.md) flows instead.

## Login

`POST /login`

> **DANGER** — DEPRECATED
>
> This endpoint belongs to the **legacy password-based login flow** and is **deprecated**. It will be removed in a future release.
>
> Please migrate to the new OAuth-based flow: generate your API Key and Secret via the **[Samco Trade API Web Dashboard](03-dashboard.md#dashboard-user-manual)** and authenticate using the [Login Code](04-authentication.md#login-code) flow.

The Login API enables secure user authentication for accessing trading services on the SAMCO platform. To authenticate successfully, users must have a valid SAMCO Trading Account and an active subscription to the SAMCO Trade API Services.

> **INFO** — In the response of the Login API, you will receive a session token that you will need to use for accessing other APIs.

### Parameter

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | string | true | The unique identification code assigned to you by SAMCO upon the successful opening of your trading account. |
| `password` | string | true | Use the password set via any SAMCO platform (SAMCO Mobile App, SAMCO Web, or Stockbasket). If no password was set, use the one sent to you in the welcome email when you opened your account. |
| `yob` | string | false | Your year of birth. |
| `accessToken` | string | true | The access token generated from the Generate Access Token API. |

### Sample Request Body

```json
requestBody={
  "userId" : "DV99999",
  "password" : "abc1234",
  "accessToken" : "***************"
}
```

### Sample Code

**JavaScript**

```js
var headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
};
      
$.ajax({
  url     : 'https://tradeapi.samco.in/login',
  method  : 'post',
  data    : JSON.stringify(requestBody),
  headers : headers,
  success : function(data){
    console.log(JSON.stringify(data));
  },
  error : function(error){
    console.log(error);
  }
})
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
}

r = requests.post('https://tradeapi.samco.in/login', 
  data=json.dumps(requestBody),
  headers = headers)

print (r.json())
```

### Sample Response

**200**

```json
{
  "serverTime": "04/04/24 11:06:17",
  "msgId": "4d54c81c-2c57-4049-8683-af0ed3e307d8",
  "status": "Success",
  "statusMessage": "Login session token generated successfully",
  "sessionToken": "e0317d9c9d4749a0706e3994c80653bc",
  "accountID": "RMXXXX3",
  "accountName": "MXXXXXXD XXXH",
  "exchangeList": ["BFO","BSE","CDS","MCX","NSE","NFO"],
}
```

**400**

```json
{
  "serverTime": "10/05/24 10:41:13",
  "msgId": "f6e8c373-a658-470b-818b-90df682ff160",
  "status": "Failure",
  "statusMessage": "Invalid Password"
}
```

### Response Schema

Status Code **200**

| Name | Type | Description |
| --- | --- | --- |
| `serverTime` | string | The date and time when the server generated the response. |
| `msgId` | string | A unique identifier for the API response message. Useful for tracking or debugging purposes. |
| `status` | string | The status of the API response. Possible values are 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `sessionToken` | string | A unique token generated for the session. Used for authenticating subsequent API requests and maintaining the user's session. Valid for 24 hours from generation. |
| `accountID` | string | A unique identifier for the user's account, used to reference the user's specific account within the system. |
| `accountName` | string | The name associated with the account, providing a human-readable reference for the account holder. |
| `exchangeList` | [string] | A list of exchanges that the user has access to or can trade on. |
| `orderTypeList` | [string] | A list of order types available for trading. |
| `productList` | [string] | A list of product types enabled for the user, including CNC (Cash and Carry), BO (Bracket Order), CO (Cover Order), NRML (Normal), MIS (Intraday). |

---

## Generate OTP

`POST /otp/generateOtp`

> **DANGER** — DEPRECATED
>
> This endpoint belongs to the **legacy 2FA / API-key generation flow** and is **deprecated**. It will be removed in a future release.
>
> Please use the new **[Samco Trade API Web Dashboard](03-dashboard.md#dashboard-user-manual)** to generate your API Key and API Secret. The dashboard handles OTP delivery and credential issuance in a single OTP-gated workflow.

The Generate OTP API is used to start the process of getting a secret API key. To use this API, the user must have a valid SAMCO Trading Account and an active subscription to the SAMCO Trade API Services.When this API is called, a One-Time Password (OTP) is sent to the user’s registered mobile number and email ID. This OTP is required for the next step of API key generation.

### Parameter

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `uid` | string | true | The unique identification code assigned to you by SAMCO upon the successful opening of your trading account. |

### Sample Request Body

```json
requestBody={
  "uid" : "DV99999",
}
```

### Sample Code

**JavaScript**

```js
var headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
};
      
$.ajax({
  url     : 'https://tradeapi.samco.in/otp/generateOtp',
  method  : 'post',
  data    : JSON.stringify(requestBody),
  headers : headers,
  success : function(data){
    console.log(JSON.stringify(data));
  },
  error : function(error){
    console.log(error);
  }
})
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
}

r = requests.post('https://tradeapi.samco.in/otp/generateOtp', 
  data=json.dumps(requestBody),
  headers = headers)

print (r.json())
```

### Sample Response

**200**

```json
{
    "serverTime": "17/12/25 09:40:58",
    "msgId": "1e439d95-5e57-4810-b57e-df94e74776ea",
    "status": "Success",
    "statusMessage": "OTP sent to your mobile and email."
}
```

**400**

```json
{
    "serverTime": "17/12/25 09:41:30",
    "msgId": "7488e02e-9e5b-43e2-b6aa-21f92b6b1658",
    "status": "Failure",
    "statusMessage": "Failed to genererate otp for user"
}
```

### Response Schema

Status Code **200**

| Name | Type | Description |
| --- | --- | --- |
| `serverTime` | string | The date and time when the server generated the response. |
| `msgId` | string | A unique identifier for the API response message. Useful for tracking or debugging purposes. |
| `status` | string | The status of the API response. Possible values are 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |

---

## Generate Secret API Key

`POST /otp/secretKeyGenerator`

> **DANGER** — DEPRECATED
>
> This endpoint belongs to the **legacy 2FA / API-key generation flow** and is **deprecated**. It will be removed in a future release.
>
> Please use the new **[Samco Trade API Web Dashboard](03-dashboard.md#dashboard-user-manual)** to generate your API Key and API Secret in an OTP-gated workflow.

The Secret Key Generator API is used to generate a secret API key using a valid user ID and the OTP received from the Generate OTP API.Once the request is successful, the secret API key is sent to the user’s registered email ID.

> **INFO** — Do not share your secret API key with anyone.
>
> The secret API key does not have an expiry. You can use the same secret API key to generate the access token. To generate a new secret API key, you must start again with the OTP generation flow.

### Parameter

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `uid` | string | true | The unique identification code assigned to you by SAMCO upon the successful opening of your trading account. |
| `otp` | string | true | The OTP received on the registered mobile number or email ID. |

### Sample Request Body

```json
requestBody={
  "uid" : "DV99999",
  "otp" :"1234"
}
```

### Sample Code

**JavaScript**

```js
var headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
};
      
$.ajax({
  url     : 'https://tradeapi.samco.in/otp/secretKeyGenerator',
  method  : 'post',
  data    : JSON.stringify(requestBody),
  headers : headers,
  success : function(data){
    console.log(JSON.stringify(data));
  },
  error : function(error){
    console.log(error);
  }
})
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
}

r = requests.post('https://tradeapi.samco.in/otp/secretKeyGenerator', 
  data=json.dumps(requestBody),
  headers = headers)

print (r.json())
```

### Sample Response

**200**

```json
{
    "serverTime": "17/12/25 10:02:41",
    "msgId": "73d115fd-ed3a-47f2-ae04-f40083c3bccf",
    "status": "Success",
    "statusMessage": "The secret API key has been sent to your email."
}
```

**400**

```json
{
    "serverTime": "17/12/25 10:01:56",
    "msgId": "6b2e7b9f-df86-4b96-932e-8028cbf766cc",
    "status": "Failure",
    "statusMessage": "Invalid OTP."
}
```

### Response Schema

Status Code **200**

| Name | Type | Description |
| --- | --- | --- |
| `serverTime` | string | The date and time when the server generated the response. |
| `msgId` | string | A unique identifier for the API response message. Useful for tracking or debugging purposes. |
| `status` | string | The status of the API response. Possible values are 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |

---

## Generate Access Token

`POST /accessToken/token`

> **DANGER** — DEPRECATED
>
> This endpoint belongs to the **legacy 2FA / API-key generation flow** and is **deprecated**. It will be removed in a future release.
>
> Please migrate to the new OAuth-based flow: generate your API Key and Secret via the **[Samco Trade API Web Dashboard](03-dashboard.md#dashboard-user-manual)** and use those credentials with the new login flow.

The Token API is used to generate an access token using a valid user ID and the secret API key received from the Secret Key Generator API on your registered email ID.

> **INFO** — This token is valid for one day.
>
> - It expires before **8:00 AM** the next day.
> - If the access token expires, you can generate a new access token using the same secret API key.

### Parameter

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `uid` | string | true | The unique identification code assigned to you by SAMCO upon the successful opening of your trading account. |
| `secretApiKey` | string | true | The secret API key received on the registered email ID. |

### Sample Request Body

```json
requestBody={
  "uid" : "DV99999",
  "secretApiKey" : "XXXXXXXXXXXXkUM9"
}
```

### Sample Code

**JavaScript**

```js
var headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
};
      
$.ajax({
  url     : 'https://tradeapi.samco.in/accessToken/token',
  method  : 'post',
  data    : JSON.stringify(requestBody),
  headers : headers,
  success : function(data){
    console.log(JSON.stringify(data));
  },
  error : function(error){
    console.log(error);
  }
})
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
}

r = requests.post('https://tradeapi.samco.in/accessToken/token', 
  data=json.dumps(requestBody),
  headers = headers)

print (r.json())
```

### Sample Response

**200**

```json
{
    "serverTime": "17/12/25 10:15:08",
    "msgId": "66b290f4-343e-4e08-85e5-67f708feb5f0",
    "status": "Success",
    "accessToken": "XXXXXXXXXXXXXiSUg_Ps6A942Lif"
}
```

**400**

```json
{
    "serverTime": "17/12/25 10:16:26",
    "status": "Failure",
    "statusMessage": "Secret key does not match"
}
```

### Response Schema

Status Code **200**

| Name | Type | Description |
| --- | --- | --- |
| `serverTime` | string | The date and time when the server generated the response. |
| `msgId` | string | A unique identifier for the API response message. Useful for tracking or debugging purposes. |
| `status` | string | The status of the API response. Possible values are 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `accessToken` | string | A unique access token generated for the user. This token is valid for one day. It expires before 8:00 AM the next day. |

---

## IP Register

`POST /ip/ipRegistration`

> **DANGER** — DEPRECATED
>
> This endpoint is **deprecated** and will be removed in a future release. It authenticates with the trading-account password, which is no longer SEBI-compliant for API access (Feb 2025 guidelines).
>
> **Please migrate to the new flow:**
>
> - Use the [**Web Dashboard**](03-dashboard.md#static-ips) to register and manage your Static IPs with `apiKey` + `apiSecret`-based authentication.
>
> The endpoint below continues to work for existing integrations but should not be used for new ones.

The Ip Register API is used to register the primary and secondary static IP addresses for a client. Once IPs are registered, the client can access the APIs only from these IP addresses.

> **INFO** — The IP address must be a valid IPv4 address.
>
> If a user tries to access the API from any other IP address, the request will be rejected with an error.

### Parameter

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientId` | string | true | The unique identification code assigned to you by SAMCO upon the successful opening of your trading account. |
| `password` | string | true | Use the password set via any SAMCO platform (SAMCO Mobile App, SAMCO Web, or Stockbasket). If no password was set, use the one sent to you in the welcome email when you opened your account. |
| `primaryIp` | string | true | The primary static IP address from which API access is allowed. |
| `secondaryIp` | string | false | The secondary static IP address from which API access is allowed. This acts as a backup IP. |

### Sample Request Body

```json
requestBody={
    "clientId" : "DV99999",
    "primaryIp" : "XXX.XX.XX.XXX",
    "secondaryIp" : "XXX.XX.XX.XXX",
    "password" : "abc1234"
}
```

### Sample Code

**JavaScript**

```js
var headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
};
      
$.ajax({
  url     : 'https://tradeapi.samco.in/ip/ipRegistration',
  method  : 'post',
  data    : JSON.stringify(requestBody),
  headers : headers,
  success : function(data){
    console.log(JSON.stringify(data));
  },
  error : function(error){
    console.log(error);
  }
})
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
}

r = requests.post('https://tradeapi.samco.in/ip/ipRegistration', 
  data=json.dumps(requestBody),
  headers = headers)

print (r.json())
```

### Sample Response

**200**

```json
{
    "serverTime": "29/01/26 10:46:06",
    "msgId": "d5f083f3-1b04-4b97-9385-1e578fdfeb7a",
    "status": "Success",
    "statusMessage": "Client IPs registered successfully",
    "data": {
        "user_id": "DV99999",
        "primary_ip": "XXX.XX.XX.XXX",
        "secondary_ip": "XXX.XX.XX.XXX",
        "ip_updated_at": "2026-01-29T05:16:07.000Z"
    }
}
```

**400**

```json
{
    "serverTime": "29/01/26 10:48:56",
    "msgId": "3c08efeb-8c2b-4f91-ae93-8343a764beb6",
    "status": "Failure",
    "statusMessage": "clientId and primaryIp are required"
}
```

**401**

```json
{
    "serverTime": "29/01/26 10:48:08",
    "msgId": "7e7674d0-65e8-43f7-8e66-a681fb60bfb2",
    "status": "Failure",
    "statusMessage": "Incorrect Password"
}
```

**409**

```json
{
    "serverTime": "29/01/26 10:49:29",
    "msgId": "62130e11-740d-401c-b020-a5474aa70d4d",
    "status": "Failure",
    "statusMessage": "Both primary and secondary IP already registered"
}
```

### Response Schema

Status Code **200**

| Name | Type | Description |
| --- | --- | --- |
| `serverTime` | string | The date and time when the server generated the response. |
| `msgId` | string | A unique identifier for the API response message. Useful for tracking or debugging purposes. |
| `status` | string | The status of the API response. Possible values are 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `data` | Object | Contains the registered IP details of the user. |
| `user_id` | string | The unique client ID provided by SAMCO after account creation. |
| `primary_ip` | string | The registered primary static IP address of the user. |
| `secondary_ip` | string | The registered secondary static IP address of the user. |
| `ip_updated_at` | string | The date and time when the IP address was last updated. |

---

## IP Update

`POST /ip/ipUpdate`

> **DANGER** — DEPRECATED
>
> This endpoint is **deprecated** and will be removed in a future release. It authenticates with the trading-account password, which is no longer SEBI-compliant for API access (Feb 2025 guidelines).
>
> **Please migrate to the new flow:**
>
> - Use the [**Web Dashboard**](03-dashboard.md#static-ips) — handles both first-time registration and subsequent updates with `apiKey` + `apiSecret`-based authentication.
>
> The endpoint below continues to work for existing integrations but should not be used for new ones.

The IP Update API is used to update the primary and/or secondary static IP addresses for a client. Once the IPs are updated, the client can access the APIs only from the newly registered IP addresses.

> **INFO** — A user is allowed to update the IP addresses **once every 7 days** from their last change (per SEBI A.6). The IP address must be a valid IPv4 address. If a user tries to access the API from any other IP address, the request will be rejected with an error.

### Parameter

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `clientId` | string | true | The unique identification code assigned to you by SAMCO upon the successful opening of your trading account. |
| `password` | string | true | Use the password set via any SAMCO platform (SAMCO Mobile App, SAMCO Web, or Stockbasket). If no password was set, use the one sent to you in the welcome email when you opened your account. |
| `primaryIp` | string | true | The primary static IP address from which API access is allowed. |
| `secondaryIp` | string | false | The secondary static IP address from which API access is allowed. This acts as a backup IP. |

### Sample Request Body

```json
requestBody={
    "clientId" : "DV99999",
    "primaryIp" : "XXX.XX.XX.XXX",
    "secondaryIp" : "XXX.XX.XX.XXX",
    "password" : "abc1234"
}
```

### Sample Code

**JavaScript**

```js
var headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
};
      
$.ajax({
  url     : 'https://tradeapi.samco.in/ip/ipUpdate',
  method  : 'post',
  data    : JSON.stringify(requestBody),
  headers : headers,
  success : function(data){
    console.log(JSON.stringify(data));
  },
  error : function(error){
    console.log(error);
  }
})
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type' : 'application/json',
  'Accept' : 'application/json'
}

r = requests.post('https://tradeapi.samco.in/ip/ipUpdate', 
  data=json.dumps(requestBody),
  headers = headers)

print (r.json())
```

### Sample Response

**200**

```json
{
    "serverTime": "29/01/26 10:46:06",
    "msgId": "d5f083f3-1b04-4b97-9385-1e578fdfeb7a",
    "status": "Success",
    "statusMessage": "Client IPs updated successfully",
    "data": {
        "user_id": "DV99999",
        "primary_ip": "XXX.XX.XX.XXX",
        "secondary_ip": "XXX.XX.XX.XXX",
        "ip_updated_at": "2026-01-29T05:16:07.000Z"
    }
}
```

**400**

```json
{
    "serverTime": "29/01/26 11:12:30",
    "msgId": "80898911-95f9-4423-8615-f920400a574f",
    "status": "Failure",
    "statusMessage": "IP update allowed only once per calendar week"
}
```

**401**

```json
{
    "serverTime": "29/01/26 10:48:08",
    "msgId": "7e7674d0-65e8-43f7-8e66-a681fb60bfb2",
    "status": "Failure",
    "statusMessage": "Incorrect Password"
}
```

### Response Schema

Status Code **200**

| Name | Type | Description |
| --- | --- | --- |
| `serverTime` | string | The date and time when the server generated the response. |
| `msgId` | string | A unique identifier for the API response message. Useful for tracking or debugging purposes. |
| `status` | string | The status of the API response. Possible values are 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `data` | Object | Contains the registered IP details of the user. |
| `user_id` | string | The unique client ID provided by SAMCO after account creation. |
| `primary_ip` | string | The registered primary static IP address of the user. |
| `secondary_ip` | string | The registered secondary static IP address of the user. |
| `ip_updated_at` | string | The date and time when the IP address was last updated. |
