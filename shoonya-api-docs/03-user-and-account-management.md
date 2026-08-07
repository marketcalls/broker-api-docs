# User & Account Management

> Source: https://shoonya.com/api-documentation (User & Account Management)

## Contents

- [User Details](#user-details)
- [Client Details](#client-details)
- [Forgot Password](#forgot-password)
- [Change Password](#change-password)
- [Set Device Pin](#set-device-pin)
- [Login With Device Pin → Login with Device Pin](#login-with-device-pin)

---

## User Details

> Request to be POSTed to URL : /NorenWClientAPI/UserDetails

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged In User Id |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | User details success or failure indication. |
| exarr | - | Json array of strings with enabled exchange names |
| orarr | - | Json array of strings with enabled price types for user |
| prarr | - | Json array of Product Obj with enabled products, as defined below. |
| brkname | - | Broker id |
| brnchid | - | Broker id |
| email | - |   |
| actid | - | Account Id |
| uid | - | User Id |
| m_num | - | Mobile Number |
| uprev | - | Always it will be an INVESTOR, other types of user not allowed to login using this API. |
| access_type | - | Access Type |
| request_time | - | It will be present only in a successful response. |
| emsg | - | This will be present only in case of errors. |

**Product Obj format :**

| Parameter Name | Possible value | Description |
|---|---|---|
| prd | - | Product name |
| s_prdt_ali | - | Product display name |
| exch | - | Json array of strings with enabled, allowed exchange names |

**Sample Success Response:**

```json
{
"request_time": "20:20:04 19-05-2020",
"prarr": [
{ “prd”:"C",
“s_prdt_ali” : “Delivery”,
18
“exch” : [“NSE”, “BSE”]
},
{ “prd”:"I",
“s_prdt_ali” : “Intraday”,
“exch” : [“NSE”, “BSE”, “NFO”]
},
, { “prd”:"H",
“s_prdt_ali” : “High Leverage”,
“exch” : [“NSE”, “BSE”, “NFO”]
},
{ “prd”:"B",
“s_prdt_ali” : “Bracket Order”,
“exch” : [“NSE”, “BSE”, “NFO”]
}
],
"exarr": [
"NSE",
"NFO"
],
"orarr": [
"MKT",
"LMT",
"SL-LMT",
"SL-MKT",
"DS",
"2L",
"3L",
"4L"
],
"brkname": "VIDYA",
"brnchid": "VIDDU",
"email": "gururaj@gmail.com",
"actid": "GURURAJ",
"uprev": "INVESTOR",
"stat": "Ok"
}
```

**Sample Failure Response:**

```json
{
  "stat": "Not_Ok",
  "emsg": "Session Expired : Invalid Session Key"
}
```

## Client Details

> Request to be POSTed to URL : /NorenWClientAPI/ClientDetails

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | Logged In User Id |
| actid* | - | Login users account ID |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | - | User details success or failure indication. |
| actid | - | Account ID |
| creatdte | - | Creation date |
| creattme | - | Creation time |
| m_num | - | Mobile Number |
| email | - | Email ID |
| pan | - | PAN |
| dob | - | Date of birth in DDMMYYYY format |
| act_sts | - | Account Status |
| addr | - | Address |
| addroffice | - | Office address |
| addrcity | - | City |
| addrstate | - | State |
| bankdetails | - | Array Object, details given below. |
| dp_acct_num | - | Array Object, details given below. |
| exarr | ["CDS","NSE","NF         O","MCX","BSE","         NCX","BSTAR","B         CD"] | Json array of strings with enabled exchange names |
| mandate_id_list | - | Mandate Id List [ Array Object, details given below.] |
| partic_id_list | - | Partic Id List [Array Object, details given below.] |
| eqt_asba | True or False | - |
| der_asba | True or False | - |
| fx_asba | True or False | - |
| com_asba | True or False | - |
| request_time | - | It will be present only in a successful response. |
| emsg | - | This will be present only in case of errors. |

**bankdetails Obj format**

| Parameter Name | Possible value | Description |
|---|---|---|
| bankn | - | Bank name |
| acctnum | - | Account number |

**dp_acct_num Obj format**

| Parameter Name | Possible value | Description |
|---|---|---|
| dpnum | - | Dp account number |

**mandate_id_list Obj format**

| Parameter Name | Possible value | Description |
|---|---|---|
| mandate_id | - | Mandate Id |
| partic_id | - | Partic Id |

## Forgot Password

> Request to be POSTed to uri : /NorenWClientAPI/ForgotPassword

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User Id |
| pan* | - | Pan of the user |
| dob* | - | Date of birth |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Password reset is Success Or failure status |
| request_time | - | Response received time. |
| emsg | - | This will be present only if password reset fails. (“Invalid User or User Details”) |

**Sample Success Response:**

```json
{
  "request_time":"10:52:56 28-05-2020",
  "stat":"Ok"
}
```

**Sample Failure Response:**

```json
{
  "request_time":"17:42:13 26-05-2020",
  "stat":"Not_Ok",
  "emsg":"Error Occurred : Wrong user id or user details"
}
```

## Change Password

> Request to be POSTed to uri : /NorenWClientAPI/Changepwd

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User Id |
| oldpwd* | - | Sha256 of old password |
| pwd* | - | New password in plain text |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Password reset is Success Or failure status |
| request_time | - | Response received time. |
| dmsg | "Password Change Success. Your new password will expire in 60 days" | This will be present only in case of success. Number of days to expiry will be present in same. |
| emsg | 1) "Error Occurred : Password couldn't be changed as it is among the previous 3 passwords" 2) "Error Occurred : Please enter an alphanumeric password of minimum 8 characters. Refer password criteria for more details" | This will be present only if password change fails |

**Sample Success Response:**

```json
{
  "request_time":"10:20:04 27-05-2020",
  "stat":"Ok",
  "dmsg":"Password Change Success. Your new password will expire in 15"
}
```

**Sample Failure Response:**

```json
{
  "request_time":"10:21:09 27-05-2020",
  "stat":"Not_Ok",
  "emsg":"Error Occurred : Password already used"
}
```

## Set Device Pin

> Request to be POSTed to uri : /NorenWClientAPI/SetPin

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |
| jKey* | - | Key Obtained on login success. |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User Id |
| imei* | - | Imei or device unique fingerprint |
| source* | - | Access type (API) |
| dpin* | - | New pin in plain text |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | If Pin setting is Success Or failure status |
| request_time | - | This will be present only if password change succeeds. |
| emsg | - | This will be present only if password change fails |

**Sample Success Response:**

```json
{
  "request_time":"14:59:43 27-05-2020",
  "stat":"Ok"
}
```

**Sample Failure Response:**

```json
{
  "stat":"Not_Ok",
  "emsg":"Session Expired : Invalid Session Key"
}
```

## Login with Device Pin

> Request to be POSTed to uri : /NorenWClientAPI/PinAuth

### Request Details

| Parameter Name | Possible value | Description |
|---|---|---|
| jData* | - | Should send json object with fields in below list |

**Json Fields**

| Parameter Name | Possible value | Description |
|---|---|---|
| uid* | - | User Id |
| imei* | - | Imei or device unique fingerprint |
| source* | - | Access type (API) |
| dpin* | - | sha256 of entered device pin |
| vc* | - | Vendor code provided by noren team, along with connection URLs |
| appkey* | - | Sha256 of uid\|vendor_key |
| apkversion* | - | Application version number |
| ipaddr* | - | global Ip of internet access |

### Response Details

| Parameter Name | Possible value | Description |
|---|---|---|
| stat | Ok or Not_Ok | Login Success Or failure status |
| usertoken | - | It will be present only on login success. This data to be sent in subsequent requests in jKey field and web socket connection while connecting. |
| lastaccesstime | - | It will be present only on login success. |
| spasswordreset | Y | If Y Mandatory password reset to be enforced. Otherwise the field will be absent. |

**Sample Success Response:**

```json
{
  "request_time":"17:01:45 27-05-2020",
  "stat":"Ok",
  "usertoken":"b0856b3f6c4bac65741f7c95de3e2060567b8bd80665e0a8ab82bbde5c434936",
  "lastaccesstime":"1590579105"
}
```

**Sample Failure Response:**

```json
{
  "request_time":"11:19:56 28-05-2020",
  "stat":"Not_Ok",
  "emsg":"Invalid Input : Mpin Invalid"
}
```
