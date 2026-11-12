# User Authentication System

Login and access-token generation. Every REST call carries the resulting bearer token.

## Contents

- [OAuth Login (Web Based)](#oauth-login-web-based)
- [Access Token](#access-token)

---

## OAuth Login (Web Based)

> Source: https://xstream.5paisa.com/dev-docs/user-authentication-system/oauth-login

**Type:** Plugin · **Method:** POST

The OAuth mechanism is built for customer login flow on partner’s platform built on 5paisa Open APIs. It redirects the customer to 5paisa Web Login page through partner’s platform (web or app) and let customer login through 5paisa demat account credentials.

The OAuth mechanism enables a secure and seamless customer login flow on the partner’s platform using 5paisa’s Open APIs. When a customer initiates login from the partner’s web or mobile app, they are redirected to the official 5paisa login page to authenticate using their demat account credentials.

After successful login, the customer is redirected back to the partner’s platform via a predefined callback URL. This flow ensures that authentication is handled securely by 5paisa while allowing the partner platform authorized access to the customer's data as per the granted permissions.

The login flow starts from navigating to public Xstream login endpoint.

A successful login comes with a RequestToken as a URL query parameter to redirect the URL registered for that API key

### REQUEST URL

```
https://dev-openapi.5paisa.com/WebVendorLogin/VLogin/Index?VendorKey=<Your Vendor Key>&ResponseURL=<Redirect URL>&State=<Pass reference value if needed>
```

> **Note — NOTE**
> Partner has to redirect customer to the URL mentioned above and along with it pass parameters listed below through POST method.
>
> This login has been updated as per the SEBI regulations of 2-factor authentication. It is based on client code, PIN and a real-time OTP/TOTP.

### Parameters

| Parameters | Discription |
|---|---|
| ResponseURL | The callback URL where partner wants to redirect customer after <br>successful login through OAuth. |
| VendorKey | The API key of the partner provided by 5pasia along with other API credentials. Partner can use the key provided to them or User can use his own User Key. |
| State | This is the redirection params , which is passed to the response URL on successful login. |

### SAMPLE OAUTH REDIRECTION

**ResponseURL**

```
https://www.google.com/?RequestToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjUwMDUyNzcwIiwicm9sZSI6IlluSjRKWXBkWndlQ09oWDJ6QVhlV2lPZzdFWndrVmQ0IiwibmJmIjoxNzE1MjQwODAyLCJleHAiOjE3MTUyNDA4MzIsImlhdCI6MTcxNTI0MDgwMn0.-CqCohv02yld8D-XbEF3SCFzWEpfQAVhjL-H-_evZSs&state=MAE
```

After successful login, user will be redirected to the callback URL provided by the partner/user and partner/user will receive following parameters as URL Params.

| PARAMETERS | DESCRIPTION |
|---|---|
| State Params | State Variables to be send on response URL as URI params. |
| RequestToken | Request Token which can be used to obtain access token. Valid for 60 min. |

### Fetch Access Token

The Request Token returned on successful login is valid for 60 min only. This token is to be used to call fetch Access token which can be used for sending request through all other Open APIs.

Please refer below documentation to know how to fetch access token.

> **Note — Validity of Request Token**
> The request token generated after successful login request remains valid for 60 min from the time of its generation. However the access token generated from above request token is valid for a day. Please refer next documentation to obtain access token.

---

## Access Token

> Source: https://xstream.5paisa.com/dev-docs/user-authentication-system/access-token

**Type:** Rest API · **Method:** POST

The API serves all the partners of IIFL Securities by providing a separate session management for partners. This login is helpful when there is a need for reconciliation of transactions done by clients through partner’s channels. The login requires email id and contact number provided by the client while generating their API credentials. The head of this API request requires userID and password to be passed in the encrypted format.

The API is designed to generate access token for a client with help of Request Token obtained from OAuth Login.

To generate the access token, partner/client needs to provide AppKey in the head of the payload whereas UserID and encryptionKey needs to be passed in body. The successful API call will provide the partner a Access token which is valid throughout a day. This access token can be used to call all further API's.

### REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/GetAccessToken
```

### Headers

| KEY | VALUE |
|---|---|
| Content-Type | application/json |

### Request body

| FIELD NAME |  | MANDATORY | DESCRIPTION |
|---|---|---|---|
| head | key<br>STRING | Yes | AppKey of user or partner |
| body | requestToken<br>STRING | Yes | This is the token received after logging in through TOTP or OAUTH. |
| body | EncryKey<br>STRING | Yes | Encryption Key of the User or Partner received along with API credentials. |
| body | userID<br>STRING | Yes | Encryption Key of the User or Partner received along with API credentials. |

> **Note — Access Token - FAQ**
> The EncrypKey and UserId correspond to the partner when the client logs in through a partner and to the client when the client logs in independently.
>
> Client keys can be find [here](https://xstream.5paisa.com/dashboard)
>
> After successful login Partner will receive **client code** in response.

### SAMPLE REQUEST BODY

**JSON**

```json
{
    "head": {
        "Key": "{{Partner/User App key}}"
    },
    "body": {
        "RequestToken": "{{request_token}}",
        "EncryKey": "{{Parter/User_encrykey}}",
        "UserId": "{{Parter/User_userid}}"
    }
}
```

**cURL**

```bash
curl --location 'https://Openapi.5paisa.com/VendorsAPI/Service1.svc/GetAccessToken' \
--header 'Content-Type: application/json' \
--data '{
    "head": {
        "Key": "{{Partner/User App key}}"
    },
    "body": {
        "RequestToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjUwMDUyNzcwIiwicm9sZSI6ImdpUUlvYXR5R2NYQUR3eFYwNXVXSGlPVzJRT1dOTGNzIiwibmJmIjoxNjgxMzcwMzk0LCJleHAiOjE2ODEzNzA0MjQsImlhdCI6MTY4MTM3MDM5NH0.q7kkfnsZPkVowiFXOE5EIM28oxOVVJuMAvg-tWfOTA0",
        "EncryKey": "{{Parter/User_encrykey}}",
        "UserId": "{{Parter/User_userid}}"
    }
}'
```

**Python**

```python
cred={
    "APP_NAME":"YOUR APP_NAME",
    "APP_SOURCE":"YOUR APP_SOURCE",
    "USER_ID":"YOUR USER_ID",
    "PASSWORD":"YOUR PASSWORD",
    "USER_KEY":"YOUR USERKEY",
    "ENCRYPTION_KEY":"YOUR ENCRYPTION_KEY"
    }

client = FivePaisaClient(cred=cred)
client.get_access_token('Your Request Token')
```

> **Note — Validity of Access Token**
> The access token generated after successful login request remains valid thought a day from the time of its generation. Token expires every day at 11:59 PM.

### Response body

| FIELD NAME |  | VALUES | DESCRIPTION |
|---|---|---|---|
| body | AccessToken<br>STRING | - | This is the access token(JWT) after successful user login. |
| body | ClientCode<br>STRING | 50012322 | The client code of the logged in user. |
| body | ClientName<br>STRING | Mahendra | The client Name of the logged in user. |
| body | POAStatus<br>STRING | Y/N | The Power of attorney status of the logged in user. |
| body | ClientType<br>STRING | 1 | The client type of the logged in user. |
| body | CustomerType<br>STRING | BASIC | Subscription Plan client has subscribed to. |
| body | AllowBseCash<br>STRING | Y/N | Segment Activation Flags, please find the list below. |
| body | StatusDescription<br>STRING | 0: Success<br>2: Invalid Inputs | It is the description of the status of the API request. |
| body | Status<br>INTEGER | 0<br>2 | It is numeric code for the status of the API request. |

> **Note — Segment Activation Flags**
> AllowBseCash,AllowBseDeriv,AllowBseMF,AllowMCXComm,AllowMcxSx,AllowNSECurrency,AllowNSEL,AllowNseCash,AllowNseComm,AllowNseDeriv,AllowNseMF,CommodityEnabled

### SAMPLE SUCCESS RESPONSE

```json
{
   "body": {
       "AccessToken": "{{Access_Token}}",
       "AllowBseCash": "Y",
       "AllowBseDeriv": "Y",
       "AllowBseMF": "Y",
       "AllowMCXComm": "Y",
       "AllowMcxSx": "N",
       "AllowNSECurrency": "Y",
       "AllowNSEL": "Y",
       "AllowNseCash": "Y",
       "AllowNseComm": "N",
       "AllowNseDeriv": "Y",
       "AllowNseMF": "N",
       "BulkOrderAllowed": 0,
       "CleareDt": "/Date(1715225400000+0530)/",
       "ClientCode": "{clientCode}",
       "ClientName": "{client_name}",
       "ClientType": "1",
       "CommodityEnabled": "Y",
       "CustomerType": "BASIC",
       "DPInfoAvailable": "Y",
       "DemoTrial": "N",
       "DirectMFCharges": 10,
       "IsIDBound": 0,
       "IsIDBound2": 0,
       "IsOnlyMF": "N",
       "IsPLM": 0,
       "IsPLMDefined": 0,
       "Message": "Success",
       "OTPCredentialID": "",
       "PGCharges": 10,
       "PLMsAllowed": 0,
       "POAStatus": "Y",
       "PasswordChangeFlag": 0,
       "PasswordChangeMessage": "",
       "ReferralBenefits": 250,
       "RefreshToken": "{refresh_token}",
       "RunningAuthorization": 0,
       "Status": 0,
       "VersionChanged": 0
   },
   "head": {
       "Status": 0,
       "StatusDescription": "Success"
   }
}
```

### SAMPLE FAILURE RESPONSE:

Failure due to wrong Expired API credentials or request code in the head

```json
{
   "body": {
       "AccessToken": "",
       "AllowBseCash": "",
       "AllowBseDeriv": "",
       "AllowBseMF": "",
       "AllowMCXComm": "",
       "AllowMcxSx": "",
       "AllowNSECurrency": "",
       "AllowNSEL": "",
       "AllowNseCash": "",
       "AllowNseComm": "",
       "AllowNseDeriv": "",
       "AllowNseMF": "",
       "BulkOrderAllowed": 0,
       "CleareDt": "/Date(1715580830932+0530)/",
       "ClientCode": "",
       "ClientName": "",
       "ClientType": "",
       "CommodityEnabled": "",
       "CustomerType": "",
       "DPInfoAvailable": "",
       "DemoTrial": "",
       "DirectMFCharges": 0,
       "IsIDBound": 0,
       "IsIDBound2": 0,
       "IsOnlyMF": "",
       "IsPLM": 0,
       "IsPLMDefined": 0,
       "Message": "Token Expired.",
       "OTPCredentialID": "",
       "PGCharges": 0,
       "PLMsAllowed": 0,
       "POAStatus":"
```

### SAMPLE FAILURE RESPONSE:

Failure due to invalid resquest token

```json
{
   "body": {
       "AccessToken": "",
       "AllowBseCash": "",
       "AllowBseDeriv": "",
       "AllowBseMF": "",
       "AllowMCXComm": "",
       "AllowMcxSx": "",
       "AllowNSECurrency": "",
       "AllowNSEL": "",
       "AllowNseCash": "",
       "AllowNseComm": "",
       "AllowNseDeriv": "",
       "AllowNseMF": "",
       "BulkOrderAllowed": 0,
       "CleareDt": "/Date(1715258267376+0530)/",
       "ClientCode": "",
       "ClientName": "",
       "ClientType": "",
       "CommodityEnabled": "",
       "CustomerType": "",
       "DPInfoAvailable": "",
       "DemoTrial": "",
       "DirectMFCharges": 0,
       "IsIDBound": 0,
       "IsIDBound2": 0,
       "IsOnlyMF": "",
       "IsPLM": 0,
       "IsPLMDefined": 0,
       "Message": "Server Unable to process your request",
       "OTPCredentialID": "",
       "PGCharges": 0,
       "PLMsAllowed": 0,
       "POAStatus":"
```
