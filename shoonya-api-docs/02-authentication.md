# Authentication

> Source: https://shoonya.com/api-documentation (Authentication)

## Contents

- [Login](#login)
- [Logout](#logout)
- [Validate HS Token](#validate-hs-token)

---

## How to Get API Key?

01. **Login Account** — Sign in to your account with your credentials (trade.shoonya.com)
02. **Go to profile** — Click on your profile in the top menu
03. **API key button** — Click on the API key option in your settings
04. **Get Key** — Client ID & secret code will be shown there

## Login

> Request to be POSTed to URL : /NorenWClientAPI/GenAcsTok

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| code* | - | code will get from successful login url |
| checksum* | - | It is a SHA-256 hash created from the combination of the app key, secret key, and code without any spaces. Example: If your app key is ABC, secret key is 123, and code is x1y2z3, Combine them as: ABC123x1y2z3 Then generate the SHA-256 hash of that string |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Login Success Or failure status |
| susertoken | - | It will be present only on login success. |
| lastaccesstime | - | It will be present only on login success. |
| exarr | - | Json array of strings with enabled exchange names |
| uname | - | User name |
| prarr | - | Json array of Product Obj with enabled products, as defined below. |
| actid | - | Account id |
| email | - | Email Id |
| brkname | - | Broker id |
| uid | - | UserId |
| brnchid | - | Region |
| cname | - | Company Name |
| emsg | - | This will be present only if Login fails. (Redirect to force change password if message is “Invalid Input : Password E |
| dmsg | - | Display message, (will be present only in case of success). |
| access_type | - | Access Type |
| lastpwdtime | - | It will be represent last password updated time. |
| values | - | Json array of non empty Market watchlists name. |
| mws | - | Json array of Market Watchlist scripts. |
| USERID | - | User ID |
| access_token | - | Access Token |
| expires_in | - | Access Token Expire date. |
| refresh_token | - | Refresh token |
| scope | - | Scope |

**Example:**

```bash
curl --location 'http://apitest.kambala.co.in/NorenWClientAPI/GenAcsTok' --d 'jData={"code":"c61de38b-7c0c-46e4-8abeacb1f6a15089","checksum":"e5ff9e0357cfa219885495ace4390b38280a39790ad434ea713afd27e6ec93
c5"}'
```

**Sample Success Response :**

```json
{
"request_time": "20:18:47 19-05-2020",
"stat": "Ok",
"access_token": "ea97cd3fbb203ad9eb5ea51d296f7a5db18af504814a6b90209ea21aa76e867c",
"expires_in": "1756979040",
"refresh_token": "b3144ec3fb5610c07411d2544b0012a64d1a40d9f14f31de26c1d00d52143b79",
"lastaccesstime": "1589899727"
}
```

**Sample Failure Response :**

```json
{
"stat": "Not_Ok",
"emsg": "Invalid Input : INVALID_VERIFIER",
"uid": "TEST"
}
```

## Logout

> Request to be POSTed to uri : /NorenWClientAPI/Logout

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User Id of the login user |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Logout Success Or failure status |
| request_time | - | It will be present only on successful logout. |
| emsg | - | This will be present only if Logout fails. |

**Sample Success Response:**

```json
{
  "stat":"Ok",
  "request_time":"10:43:41 28-05-2020"
}
```

**Sample Failure Response:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Server Timeout : "
}
```

## Validate HS Token

> Request to be POSTed to uri : /NorenWClientAPI/ValidateHsToken

> (To be used only from server, Call this url from Browser / Client Side APKs)

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| LoginId* | - | Send sLoginId received from Initiator site |
| token* | - | Key Obtained on login success.0 |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| Response | TRUE or FALSE | Response data will be in plain text format TRUE if Token is valid and FALSE for invalid User Id or Token. |

### External Integration (Backoffice Url..etc) Flow:

```
1. Trading site will call the third party url on user clicking the specified link (eg: Back Office login)
2. Trading site will pass the User id , Token and Client ID to the third party ur
3. Third Party application/web server will make a server call to our web server using this “Validate HS Token” Url.
4. If Trading site web server says ok then Third party application will provide access to the user/client
```
