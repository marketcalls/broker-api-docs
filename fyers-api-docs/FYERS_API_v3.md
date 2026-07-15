# FYERS API v3 Documentation

> Converted from the official FYERS API v3 reference (`API - FYERS.pdf`, 166 pages, exported 2026-07-09). Structure, tables, and code samples were reconstructed programmatically from the PDF's embedded text layout, so some tables with irregular/nested cells (e.g. Permission Templates, Change Log) may have minor formatting quirks — cross-check those against the live docs at https://myapi.fyers.in/docsv3 if precision matters. Only the code-sample language tab active at export time is included per endpoint (usually cURL).

## FYERS APIS

Fyers API is a set of **REST-like APIs** that provide integration with our in-house trading platform with which you can build your own customized trading applications.

## Introduction

Fyers API is a set of **REST-like APIs** that provide integration with our in-house trading platform with which you can build your own customized trading applications. You can place fresh single or multiple orders, modify and cancel existing orders in real-time. You can also get account related information such as orderbook, tradebook, net positions, holdings, and funds. We have ensured maximum security for our APIs which prevent unauthorised transactions. All API requests and received only over HTTPS protocol. [You can read more about when we introduced FYERS APIs ](https://fyers.in/community/blogs-gdppin8d/post/introducing-trading-apis-W8sq24HwJyjzGrR)**[here](https://fyers.in/community/blogs-gdppin8d/post/introducing-trading-apis-W8sq24HwJyjzGrR)**

## Libraries and SDKs

Certainly! To make it even easier for you to use the Fyers API in different programming languages, we have provided dedicated libraries/packages that handle the API calls for you. These libraries/packages abstract away the complexities of raw HTTP calls, allowing you to focus on integrating the API seamlessly into your applications. Below are the links to the libraries/packages. **[Fyers Python library](https://pypi.org/project/fyers-apiv3)** - Supports Python 3.8 to 3.12 version **[Fyers Node.js library](https://www.npmjs.com/package/fyers-api-v3)**[ - Supports Node.js 12 to 21.6.2 version](https://www.npmjs.com/package/fyers-api-v3) **[Fyers Web JS library](https://www.npmjs.com/package/fyers-web-sdk-v3)** - Supports in Browser **[Fyers C# library](https://www.nuget.org/packages/fyers-api-v3/1.1.1)** - Supports .NET 8.0.4 **[Fyers Java library](https://github.com/FyersDev/fyers-java-sdk)** - Supports Java 8 **[Fyers Go library](https://github.com/FyersDev/fyers-go-sdk)**[ - Supports Go 1.18](https://github.com/FyersDev/fyers-go-sdk) **[Fyers C library](https://github.com/FyersDev/fyers-c-sdk)** - Supports C11 **CDN Link**

| **Versions** | **Links** |
| --- | --- |
| 1.3.0 | **[https://cdn.fyers.in/js/sdk/1.3.0/fyers-web-sdk-v3/index.min.js](https://cdn.fyers.in/js/sdk/1.3.0/fyers-web-sdk-v3/index.min.js)** |
| 1.2.1 | **[https://cdn.fyers.in/js/sdk/1.2.1/fyers-web-sdk-v3/index.min.js](https://cdn.fyers.in/js/sdk/1.2.1/fyers-web-sdk-v3/index.min.js)** |
| 1.2.0 | **[https://cdn.fyers.in/js/sdk/1.2.0/fyers-web-sdk-v3/index.min.js](https://cdn.fyers.in/js/sdk/1.2.0/fyers-web-sdk-v3/index.min.js)** |
| 1.1.0 | **[https://cdn.fyers.in/js/sdk/1.1.0/fyers-web-sdk-v3/index.min.js](https://cdn.fyers.in/js/sdk/1.1.0/fyers-web-sdk-v3/index.min.js)** |
| 1.0.0 | **[https://cdn.fyers.in/js/sdk/1.0.0/fyers-web-sdk-v3/index.min.js](https://cdn.fyers.in/js/sdk/1.0.0/fyers-web-sdk-v3/index.min.js)** |

## Community

We have a dedicated community to discuss, share and raise feature requests on FYERS API. Our goal is to empower the AlgoTrading community in India with the most robust and easy to integrate APIs. [You can interact with us on our dedicated topic on ](https://fyers.in/community/api-algo-trading-bihtdkgq)**[FYERS API & Algo](https://fyers.in/community/api-algo-trading-bihtdkgq)** on **[FYERS Community](https://fyers.in/community/)**

## Request & Response Structure

Everything about Request & Response Structure

### Authorization Headers

Once the authentication is completed, you will receive an access_token. For all of the following requests, you will be required to send a combination of appId and access_token (api_id:access_token) in the HTTP Authorization header.

**Request samples**

```bash
curl -H “Authorization:  api_id: access_token”
curl -H “Authorization:  aaa-99:bbb”
```

### Success

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | “ok” |
| code | int | 200 |
| message | string | “” |
| Additional key | object / list / int / string | Each request will contain its own key based on the request |

### Failure

The error response attributes will contain the following

### Response Attribute

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | “error” |
| code | int | Negative integer to identify the specific error |
| message | string | Error message to identify error |
| HTTP Header | int | Refer to the error codes table View Details |

### HTTP Status Codes

The status codes contain the following

| **Status Code** | **Meaning** |
| --- | --- |
| 200 | Request was successful |
| 400 | Bad request. The request is invalid or certain other errors |
| 401 | Authorization error. User could not be authenticated |
| 403 | Permission error. User does not have the necessary permissions |
| 429 | Rate limit exceeded. Users have been blocked for exceeding the rate limit. |
| 500 | Internal server error. |

### Common API Error Codes

The status codes contain the following

| **Code** | **Description** |
| --- | --- |
| -8 | This error occurs when token is Expired |
| -15 | This error occurs when Invalid token is provided |
| -16 | This error occurs when server is unable to authenticate user token |
| -17 | This error occurs when token is passed is either Invalid or Expired |
| -50 | This error occurs when one or more invalid parameters are passed. The message field in the API response will include details about the specific invalid inputs. |
| -51 | This error occurs when invalid Order ID is passed while fetching Orders or Order Modification |
| -53 | This error occurs when invalid position ID is passed |
| -99 | This error occurs when order placement get rejected with rejection message in the API response |
| -300 | This error occurs when invalid symbol provided **Note:** Symbols containing special characters (ex: "M&M") must be URL-encoded (ex:"M%26M") when using direct URLs. This is handled automatically in the SDKs. |
| -352 | This error occurs when invalid App ID is provided |
| -352 | This error occurs in exit position API, if no position available to exit |
| -429 | This error occurs when the API rate limit is exceeded, either per second, minute, or day. |
| 400 | This error occurs in multi leg order placement when invalid input passed |

### Rate Limits

**Note:**[ Due to SEBI’s retail algo trading regulations, changes to its usage may take effect on April 1, 2026. Please refer to the ](https://myapi.fyers.in/mandatory-regulatory-changes#tag/Rate-Limits)[link](https://myapi.fyers.in/mandatory-regulatory-changes#tag/Rate-Limits) for further details.

| **Timeframe** | **Rate Limit** |
| --- | --- |
| Per Second | 10 |
| Per Minute | 200 |
| Per Day | 1,00,000 |

### Permission Templates

You can provide different app permissions for each application at the time of creation.

| **Permission Template** | **Basic** | **Transactions Info** | **Order Placement** | **Market Data** |
| --- | --- | --- | --- | --- |
| 1. Profile Details 2. Logout App List of activities allowed 3. Logout |  | 1. Basic Included 1. Transactions Info Included 2. Orders 2. Order Placement 3. Positions 3. Order Modification 4. Trades 4. Order Cancellation 5. Holdings 5. Exit Positions 6. Funds 6. Convert Positions 7. Market Status | 1. Historical data 2. Market Depth 3. Quotes |  |

### User blocking

The user will be blocked for the rest of the day if the per minute rate limit is exceeded more than 3 times in the day.

## App Creation

**Note:**[ Due to SEBI’s retail algo trading regulations, changes to its usage may take effect on April 1, 2026. Please refer to the ](https://myapi.fyers.in/mandatory-regulatory-changes#tag/App-Creation-and-Activation)**[link](https://myapi.fyers.in/mandatory-regulatory-changes#tag/App-Creation-and-Activation)** for further details.

### Individual Apps

These are apps which are created for your own personal usage. These apps can be used only by the creator of the app and no other client can login and make use of this particular app. To create an app, you need to follow the following steps:- [1. Login to API ](https://myapi.fyers.in/dashboard)**[Dashboard](https://myapi.fyers.in/dashboard)** 2. Click on Create App 3. Provide the following details App Icon App Name Redirect URL Description (Optional) App Permissions - Refer Permissions Template

### Third Party Apps

These apps are used by platform providers which would allow end users to login to the app and make use of the functionality. These apps are created by third party application providers to enable FYERS clients to use their applications. To create a common app, you can get in touch with us at **[api-support@fyers.in](mailto:api-support@fyers.in)**[.](mailto:api-support@fyers.in)

### Redirect URI

The user will be redirected to the redirect uri after successfully logging in using the FYERS credentials. The redirect uri should be in your control as the auth token is sensitive information.

## Authentication & Login Flow - User Apps

### Authentication Steps

**Note:**[ Due to SEBI’s retail algo trading regulations, changes to its usage may take effect on April 1, 2026. Please refer to the ](https://myapi.fyers.in/mandatory-regulatory-changes#tag/Authentication-and-Login-Flow)[link](https://myapi.fyers.in/mandatory-regulatory-changes#tag/Authentication-and-Login-Flow) for further details. The login flow is as follows: 1. Navigate to the Login API endpoint 2. After successful login, user is redirected to the redirect uri with the auth_code 3. POST the auth_code and appIdHash (SHA-256 of api_id + app_secret) to Validate Authcode API endpoint 4. Obtain the access_token use that for all the subsequent requests

### Request Parameters for Step 1

### Request Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| client_id | string | This is the app_id which you have received after creating the app. Eg: “qwerty-100” |
| redirect_uri | string | This is where the user will be redirected after successful login. Eg: [https://trade.fyers.in/api-login/redirect-uri/index.html](https://trade.fyers.in/api-login/redirect-uri/index.html) **This should be the same as what was provided at the time of app creation** |
| response_type | string | This value must always be “code” |
| **Attribute** | **Data Type** | **Description** |
| state | string | You send a random value. The same value will be returned after successful login to the redirect uri. Eg: “abcdefg” |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | This is the code to identify specific responses |
| message | string | This is the message to identify the specific error responses |
| auth_code | string | String value which will be used to generate the access_token |
| state | string | This value is returned as is from the first request |

**Request samples**

```bash
curl --location --request GET 'https://api-t1.fyers.in/api/v3/generate-authcode?client_id=SPXXXXE7-
100&redirect_uri=https://trade.fyers.in/api-login/redirect-uri/index.html&response_type=code&state=sample_state'
```

### Request Parameters for Step 2

### Request Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| grant_type | string | This value must always be “authorization_code |
| appIdHash | string | SHA-256 of api_id + app_secret Eg: SHA-256 of app_id:app_secret is 7c7120d2b5004f8de22d8dc2da0453b4d7e6211e37a4108b83712 66ecff00498 You can use this [online tool](https://emn178.github.io/online-tools/sha256.html)[ for reference](https://emn178.github.io/online-tools/sha256.html) |
| code | string | This is the auth_code which is received from the first step |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | This is the code to identify specific responses |
| message | string | This is the message to identify the specific error responses |
| access_token | string | This value will be used for all the subsequent requests. |

**Request samples**

```bash
curl --location --request POST 'https://api-t1.fyers.in/api/v3/validate-authcode' \
--header 'Content-Type: application/json' \
--data-raw '{
"grant_type": "authorization_code",
"appIdHash": "c3efb1075ef2332b3a4ec7d44b0f05c1********************",
"code": "eyJ0eXAi*******.eyJpc3MiOiJhcGkubG9********.r_65Awa1kGdsNTAgD******"
}'
```

**Sample Success Response**

```json
{
's':'ok',
'code':200,
'message':'',
'access_token':'eyJ0eXAiOi***.eyJpc3MiOiJh***.HrSubihiFKXOpUOj_7***',
'refresh_token':'eyJ0eXAiO***.eyJpc3MiOiJh***.67mXADDLrrleuEH_EE***'
}
```

### Refresh Token

**Note:** Refresh token will be discontinued from 1st April. When we validate the auth code to generate the access token, a refresh token is also sent in the response. The refresh token has a validity of 15 days. A new access token can be generated using the refresh token as long as the refresh token is valid. The following parameters must be passed in the body for the POST request **Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| grant_type string | The grant_type parameter must be set to “refresh_token”. |
| appIdHash string | SHA-256 of api_id + app_secret. Eg: SHA-256 of app_id:app_secret is c7120d2b5004f8de22d8dc2da0453b4d7e6211e37a4108b8371266ecff00498. You can use this online tool for [reference (](https://emn178.github.io/online-tools/sha256.html)[https://emn178.github.io/online-tools/sha256.html](https://emn178.github.io/online-tools/sha256.html)) |
| refresh_token string | The refresh token previously issued to the client from the validate auth code API |
| pin string | The user's pin |

**Request samples**

```bash
curl --location --request POST 'https://api-t1.fyers.in/api/v3/validate-refresh-token' \
--header 'Content-Type: application/json' \
--data-raw '{
"grant_type":"refresh_token",
"appIdHash":"c3efb1075ef2332b3a4ec7d44b0f05c1********************",
"refresh_token":"eyJ0eXAiOiJKV1***.eyJpc3MiOiJhcGkuZn***.5_Qpnd1nQXBw1T_wNJNFF***",
"pin":"****"
}'
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"",
"access_token":"eyJ0eXAiOiJK***.eyJpc3MiOiJhcGkuZnllcnM***.IzcuRxg4tnXiULCx3***"
}
```

### Best Practices

These are the recommended best practises that you should follow while using the APIs 1. Never share your app_secret with anyone 2. Never share your access_token with anyone 3. Do not provide trading permissions unless you want to use the app to place orders 4. Provide a redirect_uri which is in your control rather than a public endpoint such as google.com 5. You should send a random value in the state parameter and verify whether the same value has been returned to you

## Authentication & Login Flow - Third Party Apps

OAuth2 is authentication flow for Third Party Apps

### OAuth2 - Auth Flow

This is a simple OAuth 2 Authentication Flows. This is recommended for applications which have a backend server which can authenticate the second step This is **not recommended** for Single Page Applications (SPA) **Diagram**

### **Request Parameters for Step 1**

You need to navigate the user to the FYERS login url with the correct get parameters

### Request Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| client_id | string | This is the app_id which you have received after creating the app. Eg: “qwerty-102” |
| redirect_uri | string | This is where the user will be redirected after successful login. Eg: [https://trade.fyers.in/api-login/redirect-uri/index.html](https://trade.fyers.in/api-login/redirect-uri/index.html) **This should be the same as what was provided at the time of app creation** |
| response_type | string | This value must always be “code” |
| state | string | You send a random value. The same value will be returned after successful login to the redirect uri. Eg: “abcdefg” |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | This is the code to identify specific responses |
| message | string | This is the message to identify the specific error responses |
| auth_code | string | String value which will be used to generate the access_token |
| state | string | This value is returned as is from the first request |

### **Request Parameters for Step 2**

### Request Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| grant_type | string | This value must always be “authorization_code” |
| appIdHash | string | SHA-256 of api_id + app_secret Eg: SHA-256 of app_id:app_secret is c7120d2b5004f8de22d8dc2da0453b4d7e6211e37a4108b8371266ecff00498 [You can use this ](https://emn178.github.io/online-tools/sha256.html)[online tool](https://emn178.github.io/online-tools/sha256.html) for reference |
| code | string | This is the auth_code which is received from the first step |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | This is the code to identify specific responses |
| message | string | This is the message to identify the specific error responses |
| access_token | string | This value will be used for all the subsequent requests. |

**Request samples**

```bash
curl -H "Content-Type: application/json"-X POST -d
'{
"grant_type": "authorization_code," "appIdHash:" "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "code"
} ' https://api-t1.fyers.in/api/v3/validate-authcode
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"",
"access_token":"eyJ..."
}
```

### Best Practices

These are the recommended best practises that you should follow while using the APIs Never share your app_secret with anyone Never share your access_token with anyone Do not provide trading permissions unless you want to use the app to place orders Provide a redirect_uri which is in your control rather than a public endpoint such as google.com You should send a random value in the state parameter and verify whether the same value has been returned to you Do not store the app_secret in the front end. It should be securely kept without exposing it to third parties.

## Sample Code

### Postman Collection

We have created an extensive Postman collection which will make it easier for implementation. Kindly import the postman_collection & postman_environment_variables [Download and import the postman collection from ](https://github.com/FyersDev/fyers-api-sample-code/blob/sample_v3/v3/Postman%20V3/FYERS%20API%20V3.postman_collection.json)**[here](https://github.com/FyersDev/fyers-api-sample-code/blob/sample_v3/v3/Postman%20V3/FYERS%20API%20V3.postman_collection.json)** Download and import the postman environment variables from **[here](https://github.com/FyersDev/fyers-api-sample-code/blob/sample_v3/v3/Postman%20V3/FYERS%20API%20V3.postman_environment.json)** You can check the sample Script to get started with from **[here](https://github.com/FyersDev/fyers-api-sample-code/tree/sample_v2/My%20API%20Sample%20Script(GET%20STARTED))** We have provided dummy data in the environment variables. Kindly update the correct values after you import it.

## User

### FyersModel Class (Python SDK)

When initialized, it requires parameters such as client_id and access_token for authentication.This class supports synchronous execution by default (is_async=False). Additionally, it enables logging functionality, allowing users to specify a log path (log_path) where logs will be stored. By default, the logging level is set to 'error', but users have the option to set it to 'debug' for more detailed logging information.

### Arguments in FyersModel Class

| **Arguments** | **Data Type** | **Description** |
| --- | --- | --- |
| client_id | string | For authentication |
| access_token | string | For authentication |
| isAsync(optional) | boolean | Default value is False for synchronous flow, for asynchronous set it True |
| log_path(optional) | string | Specify the file path where you want to store the logs |
| log_level(optional) | string | By default, the logging level is set to 'ERROR', level can be set 'DEBUG' for more detailed logs. |

### Profile

This allows you to fetch basic details of the client.

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| name | string | Name of the client |
| display_name | string | Display name, if any, provided by the client |
| fy_id | string | The client id of the fyers user |
| image | string | URL link to the user’s profile picture, if any. |
| email_id | string | Email address of the client |
| pan | string | PAN of the client |
| pin_change_date | string | Date when last PIN was updated |
| pwd_change_date | string | Date when last password was updated |
| mobile_number | string | Registered mobile number |
| totp | boolean | Status of TOTP |
| pwd_to_expire | int | Number of days until the current password expires |
| ddpi_enabled | boolean | Status of DDPI |
| mtf_enabled | boolean | Status of MTF |

**Note:** As per our privacy policy and in line with compliance requirements, PII (Personally Identifiable Information) information will be masked to safeguard [customer information. If you notice any issues, please report to us at ](mailto:api-support@fyers.in)[api-support@fyers.in](mailto:api-support@fyers.in)[ for remedial action as may be necessary.](mailto:api-support@fyers.in)

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization:app_id:access_token" https://api-t1.fyers.in/api/v3/profile
```

**Sample Response**

```json
{
"s":"ok",
"code":200,
"message":"",
"data": {
"name":"JXXX X X",
"image":"https://fyers-user-details.s3.amazonaws.com/image/FK0000000001?X-Amz-Algorithm=AWS4-HMAC",
"display_name": "JD",
"email_id": "jxxxxxxx@example.com",
"PAN":"FYxxxxxx0S",
"fy_id":"FX0011",
"pin_change_date":"19-08-2020 14:58:41",
"mobile_number":"99xxxxxx99",
"totp":true,
"pwd_change_date":"19-08-2020 14:58:41",
"pwd_to_expire":42,
"ddpi_enabled":false,
"mtf_enabled":false
}
}
```

### Funds

Shows the balance available for the user for capital as well as the commodity market.

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| id | int | Unique identity for particular fund |
| title | string | Each title represents a heading of the ledger |
| equityAmount | float | The amount in the capital ledger for the above-mentioned title |
| commodityAmount | float | The amount in the commodity ledger for the above-mentioned title |

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/funds
```

**Sample Response**

```json
{
"code":200,
"message": "",
"s": "ok",
"fund_limit":[
{
"id":1 ,
"title": "Total Balance",
"equityAmount":58.150000000000006,
"commodityAmount":0
},
{
"id":2 ,
"title": "Utilized Amount",
"equityAmount":0.3,
"commodityAmount":0
},
{
"id":3 ,
"title": "Clear Balance",
"equityAmount":58.150000000000006,
"commodityAmount":0
},
{
"id":4 ,
"title": "Realized Profit and Loss",
"equityAmount":-0.3,
"commodityAmount":0
},
{
"id":5 ,
"title": "Collaterals",
"equityAmount":0 ,
"commodityAmount":0
},
{
"id":6 ,
"title": "Fund Transfer",
"equityAmount":0 ,
"commodityAmount":0
},
{
"id":7 ,
"title": "Receivables",
"equityAmount":0 ,
"commodityAmount":0
},
{
"id":8 ,
"title": "Adhoc Limit",
"equityAmount":0 ,
"commodityAmount":0
},
{
"id":9 ,
"title": "Limit at start of the day",
"equityAmount":58.45,
"commodityAmount":0
},
{
"id":10,
"title": "Available Balance",
"equityAmount":58.150000000000006,
"commodityAmount":0
}
```

```
]
}
```

### Holdings

Fetches the equity and mutual fund holdings which the user has in this demat account. This will include T1 and demat holdings.

### Request Attributes - For each holding

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol | string | Eg: NSE:RCOM-EQ |
| holdingType | string | Identify the type of holding View Details |
| quantity | int | The quantity of the symbol which the user has at the beginning of the day |
| remainingQuantity | int | This reflects the quantity - the quantity sold during the day |
| pl | float | Profit and loss made |
| costPrice | float | The original buy price of the holding |
| marketVal | float | The Market value of the current holding |
| ltp | float | LTP is the price from which the next sale of the stocks happens |
| id | int | The unique value for each holding |
| fytoken | string | Fytoken is a unique identifier for every symbol. View Details |
| exchange | int | The exchange in which order is placed. View Details |
| segment | int | The segment in which the holding is taken. View Details |
| isin | string | Unique ISIN provided by exchange for each symbol |
| qty_t1 | int | Quantity t+1 day |
| remainingPledgeQuantity | int | Remaining Pledged quantity |
| collateralQuantity | int | Pledged quantity |

### Response Attributes - Overall holdings

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| count_total | int | Total number of holdings present |
| total_investment | float | Invested amount for the current holdings |
| total_current_value | float | The present value of the holdings |
| total_pl | float | Total profit and loss made |
| pnl_perc | float | Percentage value of the total pnl |

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/holdings
```

**Sample Response**

```json
{
"s":"ok",
"code":200,
"message":"",
"holdings":
[{
"holdingType": "HLD",
"quantity":1 ,
"costPrice":1.55,
"marketVal":3.75,
"remainingQuantity":1 ,
"pl":2.2,
"ltp":3.75,
"id":1 ,
"fyToken":101000000011460,
"exchange":10,
"symbol": "NSE:JPASSOCIAT-EQ",
"segment":10,
"isin":"INE669E01016",
"qty_t1":1,
"remainingPledgeQuantity":-1,
"collateralQuantity":0,
},
{
"holdingType": "HLD",
"quantity":1 ,
"costPrice":192.6,
"marketVal":149.70,
"remainingQuantity":1 ,
"pl":-42.9,
"ltp":149.7,
"id":2 ,
"fyToken":10100000003812,
"exchange":10,
"symbol": "NSE:ZEEL-EQ",
"segment":10,
"isin":"INE669E01016",
"qty_t1":1,
"remainingPledgeQuantity":-1,
"collateralQuantity":0,
}],
"overall":
{
"count_total":2 ,
"total_investment":194.15,
"total_current_value":153.45,
"total_pl":-40.7,
"pnl_perc":-10.48,
}
}
```

### Logout

This invalidates the access token, revoking it only for the specific app without affecting other active apps or web and mobile sessions.

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization: app_id:access_token" POST 'https://api-t1.fyers.in/api/v3/logout'
```

**Sample Response**

```json
{
"s":"ok",
"code":200,
"message":"you are successfully logged out",
}
```

## Transaction Info

### Trades

Fetches all the trades for the current day across all platforms and exchanges in the current trading day.

### Response attributes - For each trade

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol | string | Eg: NSE:SBIN-EQ |
| row | int | The unique value to sort the trades |
| orderDateTime | string | The time when the trade occurred in “DD-MM-YYYY hh:mm:ss” format in IST |
| orderNumber | string | The order id for which the trade occurred |
| tradeNumber | string | The trade number generated by the exchange |
| tradePrice | float | The traded price |
| tradeValue | float | The total traded value |
| tradedQty | int | The total traded qty |
| side | int | 1 => Buy -1 => Sell View Details |
| productType | string | The product in which the order was placed View Details |
| exchangeOrderNo | string | The order number provided by the exchange |
| segment | int | The segment in which order is placed View Details |
| exchange | int | The exchange in which order is placed View Details |
| fyToken | string | Fytoken is a unique identifier for every symbol. |
| orderTag | string | ordertag provided when placing the order **Note**: 1: will be concatenated at the start of tag provided by user. 2: will be concatenated at the start of tag generated internally by Fyers. Default value if tag not provided when order is placed is 1:Untagged |

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/tradebook
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"",
"tradeBook":
[{
"clientId": "FXXXXX",
"orderDateTime": "07-Aug-2020 13:51:12",
"orderNumber": "120080789075",
"exchangeOrderNo":"1200000009204725",
"exchange":10,
"side":1 ,
"segment":10,
"orderType":2 ,
"fyToken": "101000000010666",
"productType": "CNC",
"tradedQty":10,
"tradePrice":32.7,
"tradeValue":327.0,
"tradeNumber": "52605023",
"row":52605023,
"symbol": "NSE:PNB-EQ",
"orderTag":"1:Ordertag"
},
{
"clientId": "FXXXXX",
"orderDateTime": "07-Aug-2020 13:48:12",
"orderNumber": "120080789139",
"exchangeOrderNo":"1000000012031528",
"exchange":10,
"side":1 ,
"segment":10,
"orderType":2 ,
"fyToken": "101000000010454",
"productType": "CNC",
"tradedQty":19,
"tradePrice":14.1,
"tradeValue":267.9,
"tradeNumber": "3281523",
"row":3281523,
"symbol": "NSE:CENTRUM-EQ",
"orderTag":"1:Ordertag"
},
{
"clientId": "FXXXXX1",
"orderDateTime": "07-Aug-2020 13:47:22",
"orderNumber": "120080797993",
"exchangeOrderNo":"1100000008047027",
"exchange":10,
"side":1 ,
"segment":10,
"orderType":2 ,
"fyToken": "101000000018783",
"productType": "CNC",
"tradedQty":4 ,
"tradePrice":115.5,
"tradeValue":462.0,
"tradeNumber": "27945307",
"row":27945307,
"symbol": "NSE:IDFNIFTYET-EQ",
"orderTag":"1:Ordertag"
}]
}
```

### Trades Filter By Order tag

You can query for a particular orderTag by passing the orderTag in the get parameters.

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/tradebook?order_tag=1:Ordertag
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"",
"tradeBook":
[{
"clientId": "FXXXXX",
"orderDateTime": "07-Aug-2020 13:51:12",
"orderNumber": "120080789075",
"exchangeOrderNo":"1200000009204725",
"exchange":10,
"side":1 ,
"segment":10,
"orderType":2 ,
"fyToken": "101000000010666",
"productType": "CNC",
"tradedQty":10,
"tradePrice":32.7,
"tradeValue":327.0,
"tradeNumber": "52605023",
"row":52605023,
"symbol": "NSE:PNB-EQ",
"orderTag":"1:Ordertag"
},
{
"clientId": "FXXXXX",
"orderDateTime": "07-Aug-2020 13:48:12",
"orderNumber": "120080789139",
"exchangeOrderNo":"1000000012031528",
"exchange":10,
"side":1 ,
"segment":10,
"orderType":2 ,
"fyToken": "101000000010454",
"productType": "CNC",
"tradedQty":19,
"tradePrice":14.1,
"tradeValue":267.9,
"tradeNumber": "3281523",
"row":3281523,
"symbol": "NSE:CENTRUM-EQ",
"orderTag":"1:Ordertag"
},
{
"clientId": "FXXXXX1",
"orderDateTime": "07-Aug-2020 13:47:22",
"orderNumber": "120080797993",
"exchangeOrderNo":"1100000008047027",
"exchange":10,
"side":1 ,
"segment":10,
"orderType":2 ,
"fyToken": "101000000018783",
"productType": "CNC",
"tradedQty":4 ,
"tradePrice":115.5,
"tradeValue":462.0,
"tradeNumber": "27945307",
"row":27945307,
"symbol": "NSE:IDFNIFTYET-EQ",
"orderTag":"1:Ordertag"
}]
}
```

### Orders

Fetches all the orders placed by the user across all platforms and exchanges in the current trading day.

### Response attributes - For each order

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| id string | The unique order id assigned for each order |
| exchOrdId string | The order id provided by the exchange |
| id_fyers string | Fyers system-generated unique identifier for the order |
| symbol string | The symbol for which order is placed |
| qty int | The original order qty |
| remainingQuantity int | The remaining qty |
| filledQty int | The filled qty after partial trades |
| status int | 1 => Canceled 2 => Traded / Filled 3 => (Not used currently) 4 => Transit 5 => Rejected 6 => Pending 7 => Expired View Details |
| slNo int | This is used to sort the orders based on the time |
| message string | The error messages are shown here |
| segment int | 10 => E (Equity) 11 => D (F&O) 12 => C (Currency) 20 => M (Commodity) View Details |
| limitPrice float | The limit price for the order |
| stopPrice float | The limit price for the order |
| productType string | The product type |
| type int | 1 => Limit Order 2 => Market Order 3 => Stop Order (SL-M) 4 => Stoplimit Order (SL-L) |
| side int | 1 => Buy -1 => Sell View Details |
| disclosedQty int | Disclosed quantity |
| orderValidity string | DAY IOC |
| orderDateTime string | The order time as per DD-MMM-YYYY hh:mm:ss in IST |
| parentId string | The parent order id will be provided only for applicable orders.. Eg: BO Leg 2 & 3 and CO Leg 2 |
| tradedPrice float | The average traded price for the order |
| source string | Source from where the order was placed. View Details |
| **Data** **Attribute** **Type** | **Description** |
| fytoken string | Fytoken is a unique identifier for every symbol. View Details |
| offlineOrder boolean | False => When market is open True => When placing AMO order |
| pan string | PAN of the client |
| clientId string | The client id of the fyers user |
| exchange int | The exchange in which order is placed View Details |
| instrument int | Exchange instrument type View Details |
| discloseQty int | Disclosed quantity |
| orderTag string | ordertag provided when placing the order **Note**: 1: will be concatenated at the start of tag provided by user. 2: will be concatenated at the start of tag generated internally by Fyers. Default value if tag not provided when order is placed is 2:Untagged |
| takeProfit float | Take profit price for bracket orders (BO). This field is applicable only for bracket order types. |
| stopLoss float | Stop loss price for bracket orders (BO) or cover orders (CO). This field is applicable for both bracket and cover order types. |

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/orders
```

**Sample Success Response**

```bash
Response structure:
{
"s":"ok",
"code":200,
"message":"",
"orderBook": [{
"clientId":"X******",
"id":"23030900015105",
"id_fyers":"c6697c04-d9ab-4a7c-a6f4-b0cc4ca698f6",
"exchOrdId":"1100000001089341",
"qty":1,
"remainingQuantity":0,
"filledQty":1,
"discloseQty":0,
"limitPrice":6.95,
"stopPrice":0,
"tradedPrice":6.95,
"type":1,
"fyToken":"101000000014366",
"exchange":10,
"segment":10,
"symbol":"NSE:IDEA-EQ",
"instrument":0,
"message":"",
"offlineOrder":false,
"orderDateTime":"09-Mar-2023 09:34:38",
"orderValidity":"DAY",
"pan":"",
"productType":"CNC",
"side":-1,
"status":2,
"source":"W",
"ex_sym":"IDEA",
"description":"VODAFONE IDEA LIMITED",
"ch":-0.1,
"chp":-1.44,
"lp":6.85,
"slNo":1,
"dqQtyRem":0,
"orderNumStatus":"23030900015105:2",
"disclosedQty":0,
"orderTag":"1:Ordertag",
"takeProfit":0 ,
"stopLoss":0
}]
}
```

### Order Filter By Order Id

You can query for a particular order id by passing the id in the get parameters

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization:app_id:access_token"  https://api-t1.fyers.in/api/v3/orders?id=sample_order_id
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"",
"orderBook": [{
"clientId":"X******",
"id":"23030900015105",
"exchOrdId":"1100000001089341",
"qty":1,
"remainingQuantity":0,
"filledQty":1,
"discloseQty":0,
"limitPrice":6.95,
"stopPrice":0,
"tradedPrice":6.95,
"type":1,
"fyToken":"101000000014366",
"exchange":10,
"segment":10,
"symbol":"NSE:IDEA-EQ",
"instrument":0,
"message":"",
"offlineOrder":false,
"orderDateTime":"09-Mar-2023 09:34:38",
"orderValidity":"DAY",
"pan":"",
"productType":"CNC",
"side":-1,
"status":2,
"source":"W",
"ex_sym":"IDEA",
"description":"VODAFONE IDEA LIMITED",
"ch":-0.1,
"chp":-1.44,
"lp":6.85,
"slNo":1,
"dqQtyRem":0,
"orderNumStatus":"23030900015105:2",
"disclosedQty":0,
"orderTag":"1:Ordertag",
"takeProfit":0 ,
"stopLoss":0
}]
}
```

### Order Filter By Order tag

You can query for a particular orderTag by passing the orderTag in the get parameters

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization:app_id:access_token"  https://api-t1.fyers.in/api/v3/orders??order_tag=1:Ordertag
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"",
"orderBook": [{
"clientId":"X******",
"id":"23030900015105",
"exchOrdId":"1100000001089341",
"qty":1,
"remainingQuantity":0,
"filledQty":1,
"discloseQty":0,
"limitPrice":6.95,
"stopPrice":0,
"tradedPrice":6.95,
"type":1,
"fyToken":"101000000014366",
"exchange":10,
"segment":10,
"symbol":"NSE:IDEA-EQ",
"instrument":0,
"message":"",
"offlineOrder":false,
"orderDateTime":"09-Mar-2023 09:34:38",
"orderValidity":"DAY",
"pan":"",
"productType":"CNC",
"side":-1,
"status":2,
"source":"W",
"ex_sym":"IDEA",
"description":"VODAFONE IDEA LIMITED",
"ch":-0.1,
"chp":-1.44,
"lp":6.85,
"slNo":1,
"dqQtyRem":0,
"orderNumStatus":"23030900015105:2",
"disclosedQty":0,
"orderTag":"1:Ordertag",
"takeProfit":0 ,
"stopLoss":0
}]
}
```

### Positions

Fetches the current open and closed positions for the current trading day. Note that previous trading day’s closed positions will not be shown here.

### Response attributes - For each position

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol | string | Eg: NSE:SBIN-EQ |
| id | string | The unique value for each position |
| buyAvg | float | Average buy price |
| buyQty | int | Total buy qty |
| sellAvg | float | Average sell price |
| **Attribute** | **Data Type** | **Description** |
| sellQty | int | Total sell qty |
| netAvg | float | netAvg |
| netQty | int | Net qty |
| side | int | The side shows whether the position is long / short View Details |
| qty | int | Absolute value of net qty |
| productType | string | The product type of the position View Details |
| realized_profit | float | The realized p&l of the position |
| pl | float | The total p&l of the position |
| crossCurrency | string | Y => It is cross currency position N => It is not a cross currency position |
| rbiRefRate | float | Incase of cross currency position, the rbi reference rate will be required to calculate the p&l |
| qtyMulti_com | float | Incase of commodity positions, this multiplier is required for p&l calculation |
| segment | int | The segment in which the position is taken. View Details |
| exchange | int | The exchange in which the position is taken. View Details |
| ltp | float | LTP is the price from which the next sale of the stocks happens |
| fytoken | string | Fytoken is a unique identifier for every symbol. View Details |
| cfBuyQty | int | Carry forward buy quantity |
| cfSellQty | int | Carry forward sell quantity |
| dayBuyQty | int | Day forward buy quantity |
| daySellQty | int | Day forward sell quantity |
| exchange | int | The exchange in which order is placed View Details |
| slNo | int | ---Deprecated--- This is used for sorting of positions |

### Response attributes - Overall Positions

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| count_total | int | Total number of positions present |
| count_open | int | Total number of positions opened |
| pl_total | float | Total profit and losses |
| pl_realized | float | Profit and losses when the owned product is sold |
| pl_unrealized | float | Profit and loses when the product is owned , but is not sold |

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/positions
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"",
"netPositions":
[{
"netQty":1 ,
"qty":1 ,
"avgPrice":72256.0,
"netAvg":71856.0,
"side":1 ,
"productType": "MARGIN",
"realized_profit":400.0,
"unrealized_profit":461.0,
"pl":861.0,
"ltp":72717.0,
"buyQty":2 ,
"buyAvg":72256.0,
"buyVal":144512.0,
"sellQty":1 ,
"sellAvg":72656.0,
"sellVal":72656.0,
"slNo":0 ,
"fyToken": "1120200831217406",
"crossCurrency": "N",
"rbiRefRate":1.0,
"qtyMulti_com":1.0,
"segment":20,
"symbol": "MCX:SILVERMIC20AUGFUT",
"id": "MCX:SILVERMIC20AUGFUT-MARGIN",
"cfBuyQty":0,
"cfSellQty":0,
"dayBuyQty":0,
"daySellQty":1,
"exchange":10,
}],
"overall":
{
"count_total":1 ,
"count_open":1 ,
"pl_total":861.0,
"pl_realized":400.0,
"pl_unrealized":461.0
}
}
```

## Reports

### Order History

Fetches all historical orders within the specified date range. If no range is specified, the system automatically defaults to the current financial year.

### Request attributes - For each order

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol | string | Eg: NSE:SBIN-EQ |
| page_size | string | The number of records to be fetched in one page (default is 100) |
| page_no | string | The page number to fetch (default is 1) |
| from_date | string | The start date for fetching orders in “YYYY-MM-DD” format (default is the start of the current financial year) |
| to_date | string | The end date for fetching orders in “YYYY-MM-DD” format (default is the current date) |
| segment_type | string | 0 → Includes all Segments [default] 1 → Includes only Equity 2 → Includes only Equity Derivatives 3 → Includes Currency Derivatives 4 → Includes only Commodity Derivatives |
| exchange_type | string | 0 → Includes all Exchanges [default] 1 → Includes only NSE 2 Includes only BSE → 3 → Includes only MCX |
| status | string | 0 → All Status [default] 1 → Executed 2 Cancelled → 3 → Rejected |

### Response attributes - For each order

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol | string | Eg: NSE:SBIN-EQ |
| clientId | string | The client id of the fyers user |
| id_fyers | string | Fyers system-generated unique identifier for the order |
| exchOrdId | string | The order number provided by the exchange |
| exchange | int | The exchange in which order is placed View Details |
| segment | int | The segment in which order is placed View Details |
| instrument | int | Exchange instrument type View Details |
| description | string | The description of the symbol |
| trade_date_time | int | The epoch time when the trade occurred |
| transaction_type | string | The type of transaction (BUY/SELL) |
| trade_date | string | The time when the trade occurred in “DD-MM-YYYY hh:mm:ss” format in IST |
| product_type | string | The product in which the order was placed View Details |
| status | string | The status of the trade (E.g., Executed, Rejected, etc.) |
| ordertype | string | The order type (E.g., Market, Limit, etc.) |
| qty | int | The quantity of the trade |
| tradedQty | int | The total traded qty |
| traded_price | float | The traded price |
| limit_price | float | The limit price set for the order |
| ord_source | string | The source from which the order was placed |
| rejection_reason | string | The reason for rejection if the order was rejected |
| **Attribute** | **Data Type** | **Description** |
| is_symbol_active | boolean | Indicates if the symbol is currently active for trading |

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/order-history?
symbol=INFIBEAM&page_size=100&page_no=1&from_date=2025-04-01&to_date=2025-12-
22&segment_type=0&exchange_type=0&status=0
```

**Sample Success Response**

```json
{
"s":"ok",
"data": [
{
"symbol":"MCX:GOLDPETAL26FEBFUT",
"clientId":"XXXXXX",
"id_fyers":"26020100012037",
"exchOrdId":"603210324081559",
"exchange":11,
"segment":20,
"instrument":30,
"description":"GOLDPETAL26FEBFUT",
"trade_date_time":1769920009000,
"trade_date ":"01-02-2026 09:56:49",
"transaction_type":"SELL",
"product_type":"Overnight",
"status":"Executed",
"ordertype":"Limit",
"qty":1,
"tradedqty":1,
"traded_price":15013,
"limit_price":15013,
"ord_source":"Mobile",
"rejection_reason":"",
"is_symbol_active":true
}
],
"message":"Order Book data fetched successfully",
"code":200
}
```

### Trade History

Fetches all trades for a specified date range. If no date range is provided, it defaults to the current financial year.

### Request attributes - For each order

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol | string | Eg: NSE:SBIN-EQ |
| page_size | string | The number of records to be fetched in one page (default is 100) |
| page_no | string | The page number to fetch (default is 1) |
| **Attribute** | **Data Type** | **Description** |
| from_date | string | The start date for fetching orders in “YYYY-MM-DD” format (default is the start of the current financial year) |
| to_date | string | The end date for fetching orders in “YYYY-MM-DD” format (default is the current date) |
| segment_type | string | 0 → Includes all Segments [default] 1 → Includes only Equity 2 → Includes only Equity Derivatives 3 → Includes Mutal Funds 4 → Includes only Currency Derivatives 5 → Includes only Commodity Derivatives |
| exchange_type | string | 0 → Includes all Exchanges [default] 1 → Includes only NSE 2 Includes only BSE → 3 → Includes only MCX |

### Response attributes - For each trade

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol | string | Eg: NSE:SBIN-EQ |
| clientId | string | The client id of the fyers user |
| description | string | The symbol name to display |
| exchange | int | The exchange in which order is placed View Details |
| orderDateTime | int | The epoch time when the trade occurred |
| orderNumber | string | The order id for which the trade occurred |
| tradeNumber | string | The trade number generated by the exchange |
| exchangeOrderNo | string | The order number provided by the exchange |
| side | string | 1 => Buy -1 => Sell View Details |
| product_type | string | The product in which the order was placed View Details |
| traded_qty | int | The quantity of the trade |
| trade_price | float | The traded price |
| segment | int | The segment in which order is placed View Details |
| trade_value | float | The total traded value |
| is_symbol_active | bool | This will show if the symbol is tradable or not |

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/trade-history?
exchange_type=0&from_date=2025-04-01&to_date=2025-12-22&page_no=1&page_size=10&segment_type=0&symbol=NSE%3ASUZLON-A-EQ
```

**Sample Success Response**

```json
{
"s":"ok",
"data": [
{
"symbol":"MCX:GOLDPETAL25JUNFUT",
"clientId":"XXXXXX",
"description":"GOLDPETAL25JUNFUT",
"orderDateTime":"13-Jun-2025 20:05:38",
"orderNumber":"25061300346219",
"tradeNumber":"100388805",
"exchangeOrderNo":"516410327756710",
"side":1,
"exchange":11,
"segment":20,
"product_type":"Overnight",
"traded_qty":1,
"trade_price":10007,
"trade_value":10007,
"is_symbol_active":false
}
],
"message":"Trade Book data fetched successfully"
}
```

### Charges History

Fetches all charges for a specified date range. If no date range is provided, it defaults to the current financial year.

### Request attributes - For fetching record

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| page_size | string | Number of records to fetch on single response (default is 100) |
| page_no | string | The page number to fetch (default is 1) |
| from_date | string | The start date for fetching charges in “YYYY-MM-DD” format (default is the start of the current financial year) |
| to_date | string | The end date for fetching charges in “YYYY-MM-DD” format (default is the current date) |
| segment_type | string | 0 → Includes all Segments [default] 1 → Includes only Equity 2 → Includes only Equity Derivatives 3 Includes Mutal Funds → 4 → Includes only Currency Derivatives 5 → Includes only Commodity Derivatives |
| exchange_type | string | 0 → Includes all Exchanges [default] 1 → Includes only NSE 2 → Includes only BSE 3 → Includes only MCX |
| report_type | string | 1 → Includes only date wise [default] 2 Includes summarised data (segment wise) → |

### Response attributes - For each charge

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| brokerage | float | Brokerage charges for trade execution. |
| gst | float | GST levied on profit, brokerage, and transaction charges. |
| ipft | float | The IPFT charged for the order. |
| sebi_toc | float | Regulatory fee charged by SEBI on turnover. |
| stamp_duty | float | The stamp duty charged for the order. |
| stt | float | Securities or Commodity Transaction Tax applied on trades. |
| total | float | Combined value of all charges and taxes for the day. |
| trade_date | int | Date on which the trades were executed. |
| turnover | float | Total traded value calculated by the exchange. |
| transaction_charges | float | Transaction charges include exchange charges and other charges. |

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/charges-history?
exchange_type=0&from_date=2026-04-01&to_date=2027-03-31&page_no=1&page_size=1&segment_type=0
```

**Sample Success Response**

```json
{
"s":"ok",
"data": [
{
"brokerage":40,
"gst":8.04,
"ipft":0,
"sebi_toc":0.01,
"stamp_duty":0,
"stt":9,
"total":61.69,
"trade_date":1779408000000,
"turnover":929.5,
"transaction_charges":4.61
},
{
"brokerage":280,
"gst":64.34,
"ipft":0,
"sebi_toc":0.87,
"stamp_duty":9.55,
"stt":116,
"total":547.3199999999999,
"trade_date":1779321600000,
"turnover":60934.4,
"transaction_charges":76.56
}
],
"summary_data": {
"brokerage":8651.02,
"ctt_only":1580,
"transaction_charges":1644.8099999999993,
"gst":2010.7899999999997,
"ipft":0,
"sebi_toc":35.150000000000006,
"stamp_duty":359.95000000000005,
"stt":4096,
"stt_only":2516,
"total":17637.95,
"turnover":1243559.9855999998
},
"message":"Turnover report data fetched successfully",
"total_count":37,
"code":200
}
```

### Realised Profit & Loss

Fetches all realised profit & loss for a specified date range. If no date range is provided, it defaults to the current financial year.

### Request attributes - For each realised profit & loss

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| symbol string | For equities and mutual funds, the ISIN is required.Example : INE000A01020 For derivatives, the trading symbol is required. Example : BSE:SENSEX2640976500CE |
| page_size string | Number of records to fetch on single response (default is 100) |
| **Data** **Attribute** **Type** | **Description** |
| page_no string | The page number to fetch (default is 1) |
| from_date string | The start date for fetching realised profit & loss history in “YYYY-MM-DD” format (default is the start of the current financial year) |
| to_date string | The end date for fetching realised profit & loss history in “YYYY-MM-DD” format (default is the current date) |
| segment_type string | 0 → Includes all Segments [default] 1 → Includes only Equity 2 → Includes only Equity Derivatives 3 Includes Mutal Funds → 4 → Includes only Currency Derivatives 5 → Includes only Commodity Derivatives |
| exchange_type string | 0 → Includes all Exchanges [default] 1 → Includes only NSE 2 → Includes only BSE 3 → Includes only MCX |

### Response data attributes - For each realised profit & loss

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| exch_id | int | The exchange ID |
| seg_id | int | The segment ID |
| segment_name | string | Market category where the security was traded or invested in. |
| exchange_name | string | The name of the exchange |
| symbol_name | string | Name of the stock, mutual fund, or F&O contract traded. |
| realized_pnl | float | Profit or loss from positions that are fully closed. |
| buy_qty | int | Total quantity or units bought. |
| buy_rate | float | Price per unit, share, or contract at which it was bought. |
| sell_qty | int | Total quantity or units sold. |
| sell_rate | float | Price per unit, share, or contract at which it was sold. |
| is_symbol_active | boolean | Whether the symbol is active or not |

### Response summary attributes - For the summary of the realised profit & loss

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| gross_pnl | float | The gross profit & loss of the trade |
| net_pnl | float | The net profit & loss of the trade |
| charges | float | The charges of the trade |

**Request samples**

**Curl Request Method**

```bash
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/realised-pnl-history?
exchange_type=0&from_date=2026-04-01&to_date=2027-03-31&page_no=1&page_size=10&segment_type=0&symbol=NSE%3ASUZLON-A-EQ
```

**Sample Success Response**

```json
{
"code":200,
"message":"Global PnL report data fetched successfully",
"data": [
{
"buy_qty":36,
"buy_rate":11.3053,
"exch_id":10,
"exchange_name":"NSE",
"is_symbol_active":true,
"realized_pnl":-7.2,
"symbol_name":"NSE:IDEA-EQ",
"seg_id":10,
"segment_name":"NSE_CASH",
"sell_qty":36,
"sell_rate":11.1053
}
],
"s":"ok",
"summary_data": {
"charges":9.77,
"gross_pnl":33.6,
"net_pnl":23.83
}
}
```

### Tax Profit & Loss

Fetches all tax profit & loss for a specified date range. If no date range is provided, it defaults to the current financial year.

### Request attributes - For fetching tax profit & loss history

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| fin_year | string | The financial year for fetching tax profit & loss history (default is the current financial year) |
| page_size | string | The number of records to be fetched in one page (default is 100) |
| page_no | string | The page number to fetch (default is 1) |
| segment | string | 0 → Includes all Segments [default] 1 → Includes only Equity 2 → Includes only Equity Derivatives 3 Includes Mutal Funds → 4 → Includes only Currency Derivatives 5 → Includes only Commodity Derivatives |
| transaction_type | string | 0 → Includes all Types [default] 1 → TRADING 2 → SHORTTERM 3 LONGTERM → 4 → Future_Book 5 → Option_Book |

### Response data attributes - For each tax profit & loss

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol_name | string | Name of the symbol |
| **Attribute** | **Data Type** | **Description** |
| transaction_type | string | The type of transaction |
| segment | string | Market category where the security was traded or invested in. |
| buy_date | string | Date when the stock, contract, or MF units were purchased. |
| buy_qty | float | Total quantity or units bought. |
| buy_rate | float | Price per unit, share, or contract at which it was bought. |
| sell_date | string | Date when the stock, contract, or MF units were sold. |
| sell_qty | float | Total quantity or units sold. |
| sell_rate | float | Price per unit, share, or contract at which it was sold. |
| pnl_amount | float | Profit or loss amount from the specific trade or redemption. |
| total_days | int | Number of total calendar days between buy and sell date. |
| isin | string | Unique identification number for the stock or mutual fund. |
| turnover | float | Trade value considered for tax purposes based on transaction type. |

### Response summary attributes - For the summary of the tax profit & loss

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| gross_tax_pnl | float | The gross tax profit & loss of the trade |
| net_tax_pnl | float | The net tax profit & loss of the trade |
| taxable_intrady | float | The taxable intraday profit & loss of the trade |
| taxable_future | float | The taxable future profit & loss of the trade |
| taxable_option | float | The taxable option profit & loss of the trade |
| realized_pnl | float | Realised profit or loss from positions that have been fully closed. |
| turnover_equity | float | Total turnover from your equity trades. |
| turnover_fno | float | Total turnover from your F&O trades. |
| total_charges | float | Total charges levied for all transactions in a year. |

**Request samples**

```bash
Curl Request Method`
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/tax-pnl-history?
fin_year=2026&transaction_type=0&page_size=1
```

**Sample Success Response**

```json
{
"s":"ok",
"data": [
{
"symbol_name":"IC8098-DP-L0",
"transaction_type":"Long-term",
"segment":"BSE-MF",
"buy_date":"31 Jan, 2022",
"buy_qty":0,
"buy_rate":100.2,
"sell_date":"20 May, 2026",
"sell_qty":0,
"sell_rate":100.2,
"pnl_amount":0,
"total_days":1570,
"isin":"INF109K01Q98",
"turnover":0
},
{
"symbol_name":"PSB",
"transaction_type":"Long-term",
"segment":"BSE-Cash",
"buy_date":"29 Jul, 2022",
"buy_qty":1,
"buy_rate":14.99,
"sell_date":"11 May, 2026",
"sell_qty":1,
"sell_rate":24.87,
"pnl_amount":9.88,
"total_days":1382,
"isin":"INE608A01012",
"turnover":0
}
],
"summary_data": {
"net_ltcg":-19.62,
"net_stcg":0,
"taxable_intrady":-5748.01,
"taxable_future":168999,
"taxable_option":31198.25,
"realized_pnl":194429.62,
"turnover_equity":5748.01,
"turnover_fno":1408804.43,
"total_charges":17915.46
},
"message":"Tax PnL report data fetched successfully",
"total_count":206,
"code":200
}
```

### Ledger

Fetches all ledger for a specified date range. If no date range is provided, it defaults to the current financial year.

### Request attributes - For fetching ledger history

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| page_size | string | The number of records to be fetched in one page (default is 100) |
| **Attribute** | **Data Type** | **Description** |
| page_no | string | The page number to fetch (default is 1) |
| segment_type | string | 0 → Includes all Segments [default] 1 → Includes only Equity 2 → Includes only Equity Derivatives 3 → Includes Mutal Funds 4 → Includes only Currency Derivatives 5 → Includes only Commodity Derivatives |
| exchange_type | string | 0 → Includes all Exchanges [default] 1 → Includes only NSE 2 Includes only BSE → 3 → Includes only MCX |
| transaction_type | string | 0 → Includes all transaction types [default] 1 → BR(Funds added) 2 → BP(Funds withdrawn) 3 → SJ(Trading) 4 → JV(Non trading) 5 → MTF(Margin Trading Facility) |

### Response data attributes - For each ledger

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| date | int | Date on which the transaction occurred. |
| transaction_type | int | Type of transaction such as fund transfer or charges. |
| description | string | Details of the transaction performed on that day. |
| credit_amount | string | Amount credited to your account. |
| debit_amount | string | Amount debited from your account. |
| running_balance | string | Your current account balance. |

### Response summary attributes - For the summary of the ledger

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| funds_withdrawn | float | Total amount withdrawn by you from your trading account. |
| funds_added | float | Total amount added by you to your trading account. |
| opening_balance | float | Account balance at the beginning of the selected period. |
| closing_balance | float | Account balance at the end of the selected period. |

**Request samples**

```bash
Curl Request Method`
curl -H "Authorization: app_id:access_token" https://api-t1.fyers.in/api/v3/ledger-history?page_size=1
```

**Sample Success Response**

```json
{
"s":"ok",
"data": [
{
"date":1779667200000,
"transaction_type":"Trading",
"description":"Margin released for F&O position",
"credit_amount":110983.62,
"debit_amount":0,
"running_balance":56822.889999999956
},
{
"date":1779667200000,
"transaction_type":"Trading",
"description":"Margin released for F&O position",
"credit_amount":123004.44,
"debit_amount":0,
"running_balance":-54160.73000000004
}
],
"summary_data": {
"funds_withdrawn":139351.74,
"funds_added":104456,
"opening_balance":-101237.61,
"closing_balance":56822.889999999956
},
"message":"Ledger report data fetched successfully",
"total_count":291,
"code":200
}
```

## Order Placement Guide

**Note:**[ Due to SEBI’s retail algo trading regulations, changes to its usage may take effect on April 1, 2026. Please refer to the ](https://myapi.fyers.in/mandatory-regulatory-changes#tag/Order-Type-Restrictions)**[link](https://myapi.fyers.in/mandatory-regulatory-changes#tag/Order-Type-Restrictions)** for further details.

### Order Placement Guide

The order placement process requires you to carefully input several parameters at the time of making the request. There are several validations which are required to be done before sending the request.

### Overview - Sync and Async APIs

### **Sync APIs (****)**

```
/sync
```

All existing /sync order endpoints (single order, multi-order, multileg, and related /sync flows documented under **Sync Order Placement**) **remain** **unchanged** in request shape and response shape. They continue to return the exchange order reference id (and other fields) as today. Execution is subject to a **10 orders per second (OPS)** limit.

### **Async APIs (**/async**)**

Async counterparts use the same request bodies and HTTP methods as sync where applicable, but target: POST https://<host>/api/v3/orders/async — place order (intraday / margin / CNC / CO / BO, same attributes as sync). PATCH https://<host>/api/v3/orders/async — modify order (same body rules as sync; id in the body is the order reference once known). DELETE https://<host>/api/v3/orders/async — cancel order (JSON body with id, same idea as sync). **Queuing:** When you call an async endpoint, the request is **accepted and queued** immediately. A **queuing mechanism** drains the queue and sends work downstream **at most 10 orders per second** (aligned with the OPS limit). High burst traffic is absorbed in the queue rather than failing fast for rate at the HTTP edge—**final placement, modification, or cancellation outcomes are not implied by an HTTP 200 alone**. **Immediate HTTP response:** On success, the async API returns id_fyers (Fyers system identifier for the queued/async operation). It does **not** return id (exchange order number) in this immediate response. Use id_fyers to correlate with: **Order WebSocket** — subscribe to order updates; payloads include identifiers such as id and id_fyers (see **Order Websocket Usage Guide**). **GET APIs** — e.g. order book GET /api/v3/orders and related transaction GET APIs documented under **Transaction Info**. **Hosts:** Examples below use https://api-t1.fyers.in for parity with the rest of this document; other environments may use the same path suffixes on a different host (e.g. https://api-y1.fyers.in)—set <host> accordingly. **Reference collection:** Parity with the internal Postman collection Async apiv3 orders (place/modify/cancel and CO/BO legs).

### Order Types

**Limit Order** type: 1 A limit order allows you to buy or sell an asset at a specific price (limitPrice) or better. It will only be executed at the specified price or lower for a buy order, and at the specified price or higher for a sell order. Sample input:

```json
{"symbol":"NSE:SBIN-EQ","qty":100,"type":1,"side":1,"productType":"INTRADAY","limitPrice":100,"stopPrice"
```

**Market Order** type: 2 A market order allows you to buy or sell an asset at the current market price. The limitPrice and stopPrice should be set to 0, as it is not used in this order type. Sample input:

```json
{"symbol":"NSE:SBIN-EQ","qty":100,"type":2,"side":1,"productType":"INTRADAY","limitPrice":0,"stopPrice":
```

**Stop Order / SL-M** type: 3 A stop order is designed to limit losses on a position. It becomes a market order when the stopPrice is reached. The stopPrice is the trigger price at which the market order will be placed. The stopPrice must not be higher than the Last Traded Price (ltp) for a sell order and not lower than the ltp for a buy order. Sample input:

```json
{"symbol":"NSE:SBIN-EQ","qty":100,"type":3,"side":1,"productType":"INTRADAY","limitPrice":0,"stopPrice":
```

**Stop Limit Order / SL-L** type: 4 A stop-limit order combines features of a stop order and a limit order. It triggers a limit order once the stopPrice is reached. The stopPrice must not be higher than the Last Traded Price (ltp) for a sell order and not lower than the ltp for a buy order. The stopPrice must be lower than the limitPrice for a buy order and higher than the limitPrice for a sell order. Sample input:

```json
{"symbol":"NSE:SBIN-EQ","qty":100,"type":4,"side":1,"productType":"INTRADAY","limitPrice":100,"stopPrice"
```

### Product Types

**Intraday** Used to place orders which will be bought and sold the same day Order type can be anything (Market, Limit, Stop, and Stop Limit) **CNC** Used to place orders only in stocks which will be carried forward Order type can be anything (Market, Limit, Stop, and Stop Limit) **Margin** Used to place orders in derivative contracts which will be carried forward Order type can be anything (Market, Limit, Stop, and Stop Limit) **Cover Order (CO)** stopLoss is a mandatory input stopLoss price is given in points denominated. (Eg: SBIN LTP = 300. For the above example, for buy CO, if you want to put stop loss as 298 then you have to pass "stopLoss" value as 2 (difference between ltp and your desired stop loss) ) Note: 1. "stopLoss" value can be float but should be multiple of 0.0500. 2. Now let's say if you don't provide stopLoss value as multiple of 0.0500 then you can find this error message {'code': -50, 'message': 'StopLoss not a multiple of tick size 0.0500', 's': 'error'} The order type can be either market or limit (If the market order, then the stop loss price should not be higher than the ltp in buy and lower than the ltp for sell. If the limit order, then the stop loss price should not be higher than the limit price in buy and lower than the limit for sell) Validity should be “DAY.” Disclosed quantity should be 0. **Bracket Order (BO)** stopLoss is a mandatory input takeProfit is a mandatory input The stopLoss and takeProfit are denominated in rupees above and below the trade price. (Eg: SBIN LTP = 300. So the user can give a target of Rs. 10 and stop loss or Rs. 5.) Order type can be either market, limit, stop, or stop limit Validity should be “DAY.” Disclosed quantity should be 0 **Margin Trading Facility (MTF)** This order type is for placing trades with additional margin. MTF orders require activation. Only stocks from the approved MTF list are allowed. Supported order types: Market, Limit, Stop, and Stop Limit.

### Price Validations

For all transaction requests (Order placement / modification), the price input should be in accordance with the exchange provided tick size for the particular symbol. Tick size is applicable for all price inputs (Limit / stop / stopLoss / target) Each symbol will have its own tick size All price inputs have to be in multiples of the tick size The tick size is available in the symbol master

### Quantity Validations

For all transaction requests (Order placement / modification), the quantity input should be in accordance with the exchange provided minimum lot size.

| **Segment** | **Minimum Quantity Details** |
| --- | --- |
| Equities | The quantity will be in multiples of 1 |
| Equity Derivatives | The quantity will be in multiples of the lot size specified by the exchange |
| Currency Derivatives | The quantity will be in multiples of 1 |
| Commodity Derivatives | The quantity will be in multiples of 1 |

### Order Tag

For all Order placement requests where tags are passed they should meet following requirements. Ordertag string should be Alphanumeric i.e. no space or special characters will be allowed. Ordertag string should not exceed length of 30 characters and should have minimum length of 1 character. Ordertag string cannot be your **clientID** or string **Untagged**. Ordertagging is currently not supported for ProductType **BO** & **CO**. Orders with ordertag for CO/BO product Type will be rejeceted.

### Auto-Order Slice

Use the auto-slice feature to place large orders that exceed the exchange’s freeze-quantity limits. Enable it by setting **"isSliceOrder": true** in the order request. When enabled, the system automatically splits the order into smaller quantities based on the applicable freeze limit. Each slice is submitted as a separate order with its own "Order ID". **Note:** Slicing is only allowed for NSE CM, NFO and BFO. Maximum slices per request: 10. **Sample input :**

```json
{"symbol":"NSE:BANKNIFTY25NOV58900PE","qty":3150,"type":2,"side":1,"productType":"MARGIN","limitPrice":0,"sto
```

**Response Output :**

```json
{
"code": 1101,
"message": "Order Slice placed successfully",
"data": [
{
"statusCode": 200,
"body": {
"code": 1101,
"message": "Successfully placed order",
"s": "ok",
"id": "25120400000372"
},
"statusDescription": "OK"
},
{
"statusCode": 200,
"body": {
"code": 1101,
"message": "Successfully placed order",
"s": "ok",
"id": "25120400000373"
},
"statusDescription": "OK"
},
{
"statusCode": 200,
"body": {
"code": 1101,
"message": "Successfully placed order",
"s": "ok",
"id": "25120400000374"
},
"statusDescription": "OK"
}
]
}
```

## Sync Order Placement

**Note:** Ensure that not more than 10 orders are placed per second; any requests beyond this limit will be rejected. This includes placing new orders, cancellations, and modifications.

### Single Order

This allows the user to place an order to any exchange via Fyers **Endpoint:**POST /api/v3/orders/sync

### Order rate limiting (HTTP 429)

When order rate limiting is hit, the API returns HTTP 429 Too Many Requests. Retry timing is provided in response headers (not in the response body): Retry-After: wait time in **seconds** (standard HTTP header) X-Retry-After-Ms: wait time in **milliseconds** (precision header)

### Request attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol* | string | Eg: NSE:SBIN-EQ |
| qty* | int | The quantity should be in multiples of lot size for derivatives. |
| type* | int | 1 => Limit Order 2 => Market Order 3 => Stop Order (SL-M) 4 => Stoplimit Order (SL-L) View Details |
| side* | int | 1 => Buy -1 => Sell View Details |
| productType* | string | CNC => For equity only INTRADAY => Applicable for all segments. MARGIN => Applicable only for derivatives CO => Cover Order BO => Bracket Order MTF => Approved Symbols Only View Details |
| limitPrice* | float | Default => 0 Provide valid price for Limit and Stoplimit orders |
| stopPrice* | float | Default => 0 Provide valid price for Stop and Stoplimit orders |
| disclosedQty* | int | Default => 0 Allowed only for Equity |
| validity* | string | IOC => Immediate or Cancel DAY => Valid till the end of the day |
| offlineOrder* | boolean | False => When market is open True => When placing AMO order |
| stopLoss | float | Default => 0 Provide valid price for CO and BO orders |
| takeProfit | float | Default => 0 Provide valid price for BO orders |
| orderTag | string | (Optional) Tag you want to assign to the specific order |
| isSliceOrder | boolean | False => The full quantity is placed as one single order. [True => The quantity is placed in multiple smaller orders if the total quantity is more than the ](https://support.fyers.in/portal/en/kb/articles/what-are-price-bands-and-freeze-quantities#Freeze_quantity)[freeze quantity](https://support.fyers.in/portal/en/kb/articles/what-are-price-bands-and-freeze-quantities#Freeze_quantity)[.](https://support.fyers.in/portal/en/kb/articles/what-are-price-bands-and-freeze-quantities#Freeze_quantity) |

### Response attributes

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| s string | ok / error |
| code int | This is the code to identify specific responses If 201 comes in code it implies that order request has been made but no acknowledgement has been received in this case check orderbook before placing order |
| message string | Message to clarify the request status. Eg: Order submitted successfully. Your Order Ref. No.119062829763 |
| id string | The order number of the placed order. Eg: 119031547242 |

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X POST -d '{
"symbol": "MCX:SILVERMIC20NOVFUT",
"qty":1 ,
"type":1 ,
"side":1 ,
"productType": "INTRADAY",
"limitPrice":0 ,
"stopPrice":0 ,
"validity": "DAY",
"disclosedQty":0 ,
"offlineOrder":false,
"stopLoss":0 ,
"takeProfit":0 ,
"orderTag": "tag1",
"isSliceOrder":false
}' https://api-t1.fyers.in/api/v3/orders/sync
```

**Sample Success Response**

```json
{
"s":"ok",
"code":1101,
"message":"Order submitted successfully.Your Order Ref.No.808058117761",
"id": "808058117761"
}
```

### Multi Order

You can place upto 10 orders simultaneously via the API. While Placing Multi orders you need to pass an ARRAY containing the orders request attributes **Endpoint:**POST /api/v3/multi-order/sync

### Order rate limiting (HTTP 429)

When order rate limiting is hit, the API returns HTTP 429 Too Many Requests. Retry timing is provided in response headers (not in the response body): Retry-After: wait time in **seconds** (standard HTTP header) X-Retry-After-Ms: wait time in **milliseconds** (precision header) Sample Request :

```json
[{"symbol": "MCX:SILVERM20NOVFUT","qty":1 ,"type":1 ,"side":1 ,"productType": "INTRADAY","limitPrice":61050,"stopPrice"
```

**Request samples**

```bash
curl -H "Authorization:appId:access_token"-H "Content-Type: application/json"-X POST -d '[
{
"symbol": "NSE:ITC-EQ",
"qty":1 ,
"type":1 ,
"side":1 ,
"productType": "INTRADAY",
"limitPrice":165,
"stopPrice":0 ,
"disclosedQty":0 ,
"validity": "DAY",
"offlineOrder":true,
"stopLoss":0 ,
"takeProfit":0 ,
"orderTag": "tag1"
},
{
"symbol": "NSE:ITC-EQ",
"qty":1 ,
"type":1 ,
"side":1 ,
"productType": "INTRADAY",
"limitPrice":165.10,
"stopPrice":0 ,
"disclosedQty":0 ,
"validity": "DAY",
"offlineOrder":true,
"stopLoss":0 ,
"takeProfit":0 ,
"orderTag": "tag1"
},
{
"symbol": "NSE:ITC-EQ",
"qty":1 ,
"type":1 ,
"side":1 ,
"productType": "INTRADAY",
"limitPrice":165.10,
"stopPrice":0 ,
"disclosedQty":0 ,
"validity": "DAY",
"offlineOrder":true,
"stopLoss":0 ,
"takeProfit":0 ,
"orderTag": "tag1"
}
]' https://api-t1.fyers.in/api/v3/multi-order/sync
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"",
"data": [{"statusCode":200,
"body": {
"s":"ok",
"code":200,
"message": "Order submitted successfully.Your Order Ref.No.120080778988",
"id":"120080778988"
},
"statusDescription":"HTTP OK"
},
{
"statusCode":200,
"body":
{
```

```
"s":"ok",
"code":200,
"message": "Order submitted successfully.Your Order Ref.No.120080777359",
"id":"120080777359"
},
"statusDescription":"HTTP OK"
},
{
"statusCode":200,
"body":
{
"s":"ok",
"code":200,
"message": "Order submitted successfully.Your Order Ref.No.120080777379",
"id":"120080777379"
},"statusDescription":"HTTP OK"
}]
}
```

### MultiLeg Order

This allows the user to place an MultiLeg order to NSE via Fyers. **Note:** As per exchange mandate, while selecting symbols please check the "stream" key in the symbol master JSON file to ensure both legs belong to the same stream. **Endpoint:**POST /api/v3/multileg/orders/sync

### Order rate limiting (HTTP 429)

When order rate limiting is hit, the API returns HTTP 429 Too Many Requests. Retry timing is provided in response headers (not in the response body): Retry-After: wait time in **seconds** (standard HTTP header) X-Retry-After-Ms: wait time in **milliseconds** (precision header)

### Request attributes

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| orderTag string | (Optional) Tag you want to assign to the specific order |
| productType* string | INTRADAY => Applicable for NFO segments. MARGIN => Applicable for NFO segments. |
| offlineOrder* boolean | False => When market is open True => When placing AMO order. |
| orderType* string | 3L => Applicable for 3 leg order. 2L => Applicable for 2 leg order. |
| validity* string | IOC => Immediate or Cancel |
| legs* json | It represents multiple trading legs in a multi-leg order. Each leg within the legs object corresponds to a specific trading instrument and order details. Each leg is identified by a unique key (leg1, leg2, leg3 ) |

### Leg attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol* | string | Eg: NSE:SBIN24JUNFUT |
| qty* | int | The quantity should be in multiples of lot size for derivatives. |
| **Attribute** | **Data Type** | **Description** |
| side* | int | 1 => Buy -1 => Sell |
| type* | int | 1 => Limit Order |
| limitPrice* | float | Provide valid price for Limit orders |

### Response attributes

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| s string | ok / error |
| code int | This is the code to identify specific responses If 201 comes in code it implies that order request has been made but no acknowledgement has been received in this case check orderbook before placing order |
| message string | Message to clarify the request status. Eg: Order submitted successfully. Your Order Ref. No.119062829763 |
| id string | The order number of the placed order. Eg: 119031547242 |

### Input Validations

| **Error Message** | **Description** |
| --- | --- |
| The input symbol is invalid. | Input symbol ticker is not found in the exchange data |
| Only NFO symbols are allowed | Options and Future symbols listed in NSE are allowed. |
| The input symbol is banned for FNO trading. | The input symbol is banned for trading by the exchange. |
| All symbols must be related to the same underlying symbol. | All symbols must be related to same symbol |
|  | Input qty(Quantity) should be multiples of minimum lot size of that |

```
Quantity should be multiples of the lot size.
```

symbol You cannot add same symbol for two legs.Input data should not have same symbol in more than one leg. Group combination not foundInput Symbols do not belong to same stream group.

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X POST -d '{
"orderTag":"tag1",
"productType":"MARGIN",
"offlineOrder":false,
"orderType":"3L",
"validity":"IOC",
"legs": {
"leg1": {
"symbol":"NSE:SBIN24JUNFUT",
"qty":750,
"side":1,
"type":1,
"limitPrice":800
},
"leg2": {
"symbol":"NSE:SBIN24JULFUT",
"qty":750,
"side":1,
"type":1,
"limitPrice":800
},
"leg3": {
"symbol":"NSE:SBIN24JUN900CE",
"qty":750,
"side":1,
"type":1,
"limitPrice":3
}
}
}' https://api-t1.fyers.in/api/v3/multileg/orders/sync
```

**Sample Success Response**

```json
{
"s":"ok",
"code":1101,
"message":"Successfully placed order",
"id": "808058117761"
}
```

## Async Order Placement

Asynchronous order APIs (/api/v3/orders/async, /api/v3/multi-order/async, and related). For /sync vs /async behavior, queuing, **10** **OPS**, id_fyers, hosts, and the Postman reference collection, see **Order Placement Guide** (section Overview - Sync and Async APIs).

### Overview - Sync and Async APIs

Full /sync vs /async overview (queuing, **10 OPS**, id_fyers, hosts, Postman parity) is documented under **Order Placement Guide** — Overview - Sync and Async APIs.

### Place order (async)

Same JSON attributes as synchronous **Place order** (/api/v3/orders/sync). POST to /api/v3/orders/async.

### Immediate response attributes (async)

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | Response code (same semantics family as sync where applicable) |
| message | string | Status message |
| id_fyers | string | Fyers queue/async operation id (use for WebSocket and GET correlation). id** is not returned here.** |

**Request samples**

```bash
curl -H "Authorization: app_id:access_token"-H "Content-Type: application/json"-X POST -d '{
"symbol": "NSE:SBIN-EQ",
"qty":1 ,
"type":1 ,
"side":1 ,
"productType": "CNC",
"limitPrice":0 ,
"stopPrice":0 ,
"disclosedQty":0 ,
"validity": "DAY",
"offlineOrder":true,
"stopLoss":0 ,
"takeProfit":0
}' https://api-t1.fyers.in/api/v3/orders/async
Sample immediate success response ( async — note id_fyers,  no id)
{
"s":"ok",
"code":1101,
"message":"Order queued successfully.",
"id_fyers":"c6697c04-d9ab-4a7c-a6f4-b0cc4ca698f6"
}
```

### Modify order (async)

Same JSON attributes as synchronous modify. PATCH to /api/v3/orders/async. For CO/BO, id may be leg-scoped (e.g. 808278287301-CO-1).

### Immediate response attributes (async)

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | Response code |
| **Attribute** | **Data Type** | **Description** |
| message | string | Status message |
| id_fyers | string | Fyers id for the async modify request. id** (order ref) is not returned in this immediate response.** |

**Request samples**

```bash
curl -H "Authorization: app_id:access_token"-H "Content-Type: application/json"-X PATCH -d '{
"id": "52009117318",
"type":1 ,
"limitPrice":200,
"qty":1
}' https://api-t1.fyers.in/api/v3/orders/async
```

### Cancel order (async)

JSON body with id of the order to cancel. DELETE to /api/v3/orders/async.

### Immediate response attributes (async)

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | Response code |
| message | string | Status message |
| id_fyers | string | Fyers id for the async cancel request. |

**Request samples**

```bash
curl -H "Authorization: app_id:access_token"-H "Content-Type: application/json"-X DELETE -d '{
"id": "52009117318"
}' https://api-t1.fyers.in/api/v3/orders/async
```

### Multi-order async — queue and response pattern

**POST / PATCH / DELETE**https://<host>/api/v3/multi-order/async with a **JSON array** in the body (same structure as /api/v3/multi-order/sync). Each element is queued; the system processes work respecting **10 OPS**. The HTTP response returns id_fyers (per- item or envelope as implemented—correlate via message/WebSocket/order book). **Exchange **id and terminal status for each leg come from the **order** **WebSocket** and **GET** APIs (order book).

### Place multiple orders (async)

Body is an **array** of order objects (same fields as sync multi-order). POST to /api/v3/multi-order/async.

**Request samples**

```bash
curl -H "Authorization: app_id:access_token"-H "Content-Type: application/json"-X POST -d '[
{"symbol": "NSE:SBIN-
EQ", "qty":1 ,"type":1 ,"side":1 ,"productType": "INTRADAY", "limitPrice":190,"stopPrice":0 ,"disclosedQty":0 ,"validity": "DAY"
{"symbol": "NSE:SBIN-
EQ", "qty":1 ,"type":1 ,"side":1 ,"productType": "CNC," "limitPrice":0 ,"stopPrice":0 ,"disclosedQty":0 ,"validity": "DAY", "offli
]' https://api-t1.fyers.in/api/v3/multi-order/async
```

### Modify multiple orders (async)

Body is an **array** of modify payloads (each includes id and fields to change). PATCH to /api/v3/multi-order/async.

**Request samples**

```bash
curl -H "Authorization: app_id:access_token"-H "Content-Type: application/json"-X PATCH -d '[
{"id": "52009117324", "type":1 ,"limitPrice":196,"offlineOrder":true},
{"id": "52009117325", "type":1 ,"limitPrice":196,"offlineOrder":true}
]' https://api-t1.fyers.in/api/v3/multi-order/async
```

### Cancel multiple orders (async)

Body is an **array** of objects with id. DELETE to /api/v3/multi-order/async.

**Request samples**

```bash
curl -H "Authorization: app_id:access_token"-H "Content-Type: application/json"-X DELETE -d '[
{"id": "52009117324"},
{"id": "52009117325"}
]' https://api-t1.fyers.in/api/v3/multi-order/async
```

## GTT Orders

GTT (Good Till Trigger) is used to create orders with longer validity. It helps you set a Target or Stop-Loss for your open positions or holdings, and you can also use it to take new positions. The order remains active for up to one year.

### GTT Single

This type is used to create a single GTT order. It supports placing orders for CNC, Margin, and MTF. It can be applied either as a Target or Stop Loss for your existing holdings/positions. Alternatively, it can be used to create a GTT order for a new position/holding.

### Request attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| Side | integer | Indicates the side of the order: 1 for buy, -1 for sell. |
| symbol* | string | The instrument's unique identifier, e.g., "NSE:CHOLAFIN-EQ" |
| productType* | string | The product type for the order. Valid values: "CNC", "MARGIN", "MTF". |
| orderInfo* | object | Contains information about the GTT/OCO order legs. |
| orderInfo.leg1* | object | Details for GTT order leg. Mandatory for all orders. |
| orderInfo.leg1.price* | number | Price at which the order |
| orderInfo.leg1.triggerPrice | number | Trigger price for the GTT order. NOTE: for OCO order this leg trigger price should be always above LTP |
| orderInfo.leg1.qty* | integer | Quantity for the GTT order leg. |
| orderInfo.leg2* | object | Details for OCO order leg. Optional and included only for OCO orders. |
| orderInfo.leg2.price* | number | Price at which the second leg of the OCO order should be placed. |
| orderInfo.leg2.triggerPrice* | number | Trigger price for the second leg of the OCO order. NOTE: for OCO order this leg trigger price should be always below LTP |
| orderInfo.leg2.qty* | integer | Quantity for the second leg of the OCO order.. |
| orderTag | string | ordertag provided when placing the order **Note**: 1:GTT will be concatenated at the start of tag provided by user. Default value if tag not provided when order is placed is 2:GTTUntagged |

### Response attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code indicating the outcome of the request: - 1101: Order placed successfully. - 201: Order is in transit. Confirm details using the Orderbook API. - Other codes represent specific error conditions. |
| message* | string | Descriptive message about the request status, e.g., "Successfully placed order". |
| s* | string | Request status indicator: "ok" for success, "error" for failure. |
| id* | string | Unique identifier for the placed order, returned when the order is successfully processed. |

**Request samples**

```bash
curl --location 'https://api-t1.fyers.in/api/v3/gtt/orders/sync' \
--header 'Authorization: accessToken' \
--header 'Content-Type: application/json' \
--data '{
"side":1,
"symbol":"NSE:SBIN-EQ",
"productType": "CNC",
"orderInfo": {
"leg1": {
"price":1000,
"triggerPrice":1000,
"qty":1
}
}
}'
```

**Sample Success Response**

```json
{
"code":1101,
"message":"Successfully placed order",
"s":"ok",
"id": "25012400002074"
}
```

### GTT OCO

This type allows you to place both a Stop Loss and a Target order simultaneously. If one order is triggered, the other gets automatically canceled. To avoid rejections: For Leg1: The trigger price must always be greater than the LTP For Leg 2: The trigger price must always be less than the LTP

### Request attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| Side | integer | Indicates the side of the order: 1 for buy, -1 for sell. |
| symbol* | string | The instrument's unique identifier, e.g., "NSE:CHOLAFIN-EQ" |
| productType* | string | The product type for the order. Valid values: "CNC", "MARGIN", "MTF". |
| orderInfo* | object | Contains information about the GTT/OCO order legs. |
| orderInfo.leg1* | object | Details for GTT order leg. Mandatory for all orders. |
| orderInfo.leg1.price* | number | Price at which the order |
| orderInfo.leg1.triggerPrice | number | Trigger price for the GTT order. NOTE: for OCO order this leg trigger price should be always above LTP |
| orderInfo.leg1.qty* | integer | Quantity for the GTT order leg. |
| orderInfo.leg2* | object | Details for OCO order leg. Optional and included only for OCO orders. |
| orderInfo.leg2.price* | number | Price at which the second leg of the OCO order should be placed. |
| **Attribute** | **Data Type** | **Description** |
| orderInfo.leg2.triggerPrice* | number | Trigger price for the second leg of the OCO order. NOTE: for OCO order this leg trigger price should be always below LTP |
| orderInfo.leg2.qty* | integer | Quantity for the second leg of the OCO order.. |

### Response attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code indicating the outcome of the request: - 1101: Order placed successfully. - 201: Order is in transit. Confirm details using the Orderbook API. - Other codes represent specific error conditions. |
| message* | string | Descriptive message about the request status, e.g., "Successfully placed order". |
| s* | string | Request status indicator: "ok" for success, "error" for failure. |
| id* | string | Unique identifier for the placed order, returned when the order is successfully processed. |

**Request samples**

```bash
curl --location 'https://api-t1.fyers.in/api/v3/gtt/orders/sync' \
--header 'Authorization: accessToken' \
--header 'Content-Type: application/json' \
--data '{
"side":1,
"symbol":"NSE:CHOLAFIN-EQ",
"productType": "CNC",
"orderInfo": {
"leg1": {
"price":10000,
"triggerPrice":10000,
"qty":1
},
"leg2": {
"price":990,
"triggerPrice":990,
"qty":3
}
}
}'
```

**Sample Success Response**

```json
{
"code":1101,
"message":"Successfully placed order",
"s":"ok",
"id": "25012400002074"
}
```

### GTT Modify Order

This allows the user to modify pending GTT orders. Users can provide parameters which need to be modified. In case a particular parameter has not been provided, the original value will be considered.

### Request attributes

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| id* string | Unique identifier for the order to be modified, e.g., "25010700000001". |
| orderInfo* object | Contains updated information about the GTT/OCO order legs. |
| orderInfo.leg1* object | Details for GTT order leg. Mandatory for all modifications. |
| orderInfo.leg1.price* number | Updated price at which the order should be placed. |
| orderInfo.leg1.triggerPrice* number | Updated trigger price for the GTT order. NOTE: for OCO order this leg trigger price should be always above LTP. |
| orderInfo.leg1.qty* integer | Updated quantity for the GTT order leg. |
| orderInfo.leg2* object | Details for OCO order leg. Required if the order is an OCO type. |
| orderInfo.leg2.price* number | Updated price for the second leg of the OCO order. |
| orderInfo.leg2.triggerPrice* number | Updated trigger price for the second leg of the OCO order. NOTE: for OCO order this leg trigger price should be always below LTP. |
| orderInfo.leg2.qty* integer | Updated quantity for the second leg of the OCO order. |

### Response attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | Status code indicating the outcome of the modification request: - 1102: Order modification successful. - 201: Order modification is in transit. Confirm details using the Orderbook API. - Other codes represent specific error conditions. |
| message | string | Descriptive message about the modification request. e.g., "Successfully modified order". |
| id | string | Unique identifier for the modified order, returned if the modification is successful. |

**Request samples**

```bash
curl --location --request PATCH 'https://api-t1.fyers.in/api/v3/gtt/orders/sync' \
--header 'Authorization: accesstoken' \
--header 'Content-Type: application/json' \
--data '{
"id":"25012400002074",
"orderInfo": {
"leg1": {
"price":1010,
"triggerPrice":1010,
"qty":5
},
"leg2": {
"price":1010,
"triggerPrice":1010,
"qty":5
}
}
}'
```

**Sample Success Response**

```json
{
"code":1102,
"message": "Successfully modified order',
"s":"ok",
"id": '25012400002074"
}
```

### GTT Cancel Order

You can cancel pending orders before they trigger.

### Request attributes - For each order

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| id* | string | Unique identifier for the order to be cancelled, e.g., "25010700000001". |

### Response attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | Status code indicating the outcome of the cancellation request: - 1103: Order cancellation successful. - Other codes represent specific error conditions. |
| message | string | Descriptive message about the cancellation request, e.g., "Successfully |
| id | string | Unique identifier for the cancelled order, returned if the cancellation is successful. |

**Request samples**

```bash
curl --location --request DELETE 'https://api-t1.fyers.in/api/v3/gtt/orders/sync' \
--header 'Authorization: accesstoken' \
--header 'Content-Type: application/json' \
--data '{"id":"25012400002099"}'
```

**Sample Success Response**

```json
{
"code":1103,
"message":"Successfully cancelled order",
"s":"ok",
"id":"25012400002099"
}
```

### GTT Order Book

You can fetch all pending GTT Orders.

### Response attributes - For each order

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code of the API response: - 200: Request successful. - Other codes represent specific error conditions. |
| message | string | Optional message about the API request (can be empty for successful requests). |
| s | string | Status of the request: "ok" for success, "error" for failure. |
| orderBook | array | List of order details. |
| orderBook[].client_id | string | Client identifier associated with the order. |
| orderBook[].exchange | integer | Exchange code where the order is placed, e.g., 10 for NSE. |
| orderBook[].fy_token | string | Unique token for the instrument in the order. |
| orderBook[].id_fyers | string | Fyers system-generated unique identifier for the order. |
| orderBook[].id | string | Order ID provided by the system. |
| orderBook[].instrument | integer | Instrument type, e.g., 0 for equity. |
| orderBook[].lot_size | integer | Lot size of the instrument in the order. |
| orderBook[].multiplier | integer | Multiplier for the instrument (e.g., for derivatives). |
| orderBook[].ord_status | integer | Order status code: - 1: Cancelled - 2: Traded / Filled - 3: For future use - 4: Transit - 5: Rejected - 6: Pending |
| orderBook[].precision | integer | Decimal precision for the instrument's price. |
| orderBook[].price_limit | number | Limit price for the first leg of the order. |
| orderBook[].price2_limit | number | Limit price for the second leg (if OCO). |
| orderBook[].price_trigger | number | Trigger price for the first leg of the order. |
| orderBook[].price2_trigger | number | Trigger price for the second leg (if OCO). |
| orderBook[].product_type | string | Product type, e.g., "CNC", "MARGIN", "MTF". |
| orderBook[].qty | integer | Quantity for the first leg of the order. |
| orderBook[].qty2 | integer | Quantity for the second leg (if OCO). |
| **Attribute** | **Data Type** | **Description** |
| orderBook[].report_type | string | Status of the order, e.g., "CANCELLED", "PLACED". |
| orderBook[].segment | integer | Segment code, e.g., 10 for equity. |
| orderBook[].symbol | string | Symbol of the instrument, e.g., "NSE:CHOLAFIN-EQ". |
| orderBook[].symbol_desc | string | Full description of the symbol, e.g., "CHOLAMANDALAM IN & FIN CO". |
| orderBook[].symbol_exch | string | Symbol short code on the exchange, e.g., "CHOLAFIN". |
| orderBook[].tick_size | number | Minimum price increment for the instrument. |
| orderBook[].tran_side | integer | Transaction side: 1 for buy, -1 for sell. |
| orderBook[].gtt_oco_ind | integer | Indicator for the order type: - 1: GTT order. 2: OCO order. |
| orderBook[].create_time | string | Creation timestamp of the order in human-readable format. |
| orderBook[].create_time_epoch | integer | Creation timestamp of the order in epoch seconds. |
| orderBook[].oms_msg | string | Message from the Order Management System (OMS) about the order's status. |
| orderBook[].ltp_ch | number | Last traded price change. |
| orderBook[].ltp_chp | number | Last traded price change percentage. |
| orderBook[].ltp | number | Last traded price of the instrument. |

**Request samples**

```bash
curl --location 'https://api-t1.fyers.in/api/v3/gtt/orders' \
--header 'Authorization: accesstoken' \
```

**Sample Success Response**

```bash
Response structure:
{
"s":"ok",
"code":200,
"message":"",
"orderBook": [
{
"clientId":"X******",
"exchange":10,
"fy_token":"10100000003045",
"id_fyers":"c6697c04-d9ab-4a7c-a6f4-b0cc4ca698f6",
"id":"25012400002074",
"instrument":0,
"lot_size":1,
"multiplier":0,
"ord_status":1,
"precision":2,
"price_limit":1020,
"price2_limit":620,
"price_trigger":1020,
"price2_trigger":620,
"product_type":"CNC",
"qty":5,
"qty2":5,
"report_type":"CANCELLED",
"segment":10,
"symbol":"NSE:SBIN-EQ",
"symbol_desc":"STATE BANK OF INDIA",
"symbol_exch":"SBIN",
"tick_size":0.05,
"tran_side":1,
"gtt_oco_ind":2,
"create_time":"24-Jan-2025 16:13:31",
"create_time_epoch":1737715411,
"oms_msg":"GTT/OCO order cancelled successfully.",
"ltp_ch":0,
"ltp_chp":0,
"ltp":0
},
{
"clientId":"X******",
"exchange":10,
"fy_token":"10100000003045",
"id_fyers":"142849a0-d32b-44b5-9108-b7db5ee5e59b",
"id":"25012400002099",
"instrument":0,
"lot_size":1,
"multiplier":0,
"ord_status":1,
"precision":2,
"price_limit":1000,
"price2_limit":600,
"price_trigger":1000,
"price2_trigger":600,
"product_type":"MTF",
"qty":3,
"qty2":3,
"report_type":"CANCELLED",
"segment":10,
"symbol":"NSE:SBIN-EQ",
"symbol_desc":"STATE BANK OF INDIA",
"symbol_exch":"SBIN",
"tick_size":0.05,
"tran_side":-1,
```

```
"gtt_oco_ind":2,
"create_time":"24-Jan-2025 16:10:27",
"create_time_epoch":1737715227,
"oms_msg":"GTT/OCO order cancelled successfully.",
"ltp_ch":0,
"ltp_chp":0,
"ltp":0
}
]
}
```

## Smart Orders

### Smart Limit Order

Smart Limit Orders allow you to place limit orders that remain active until the specified end time. Once the end time is reached, the order can be converted to an MPP order or cancelled. Note: Supports order placement under CNC, MARGIN, MTF, and INTRADAY. You can define a price range (HPR/LPR) to restrict execution within your specified limits. Supports only selected NSE and BSE symbols.

### Request Attributes

| **Attribute** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| symbol | string | Yes | The instrument's unique identifier, e.g., "NSE:SBIN-EQ" |
| side | integer | Yes | Order side: 1 for Buy, -1 for Sell (enum: 1, -1) |
| qty | integer | Yes | Order quantity (Min: 1, Max: 999999; must be a multiple of lot size) |
| productType | string | Yes | Must be one of: "CNC", "MARGIN", "INTRADAY", "MTF" |
| limitPrice | number | Yes | The price at which the order should be placed (Min: 0.01) |
| endTime | integer | Yes | Order expiry time as a Unix timestamp (epoch) |
| orderType | integer | Yes | Order type: 1 for Limit, 4 for Stop-Limit (enum: 1, 4) |
| onExp | integer | Yes | Action on expiry: 1 = Cancel, 2 = Market (enum: 1, 2) |
| stopPrice | number | No | Default: 0. Required when orderType is 4 (Stop-Limit) |
| hpr | number | No | Default: 0. 0 = no upper price limit. If provided, order executes only below this price |
| lpr | number | No | Default: 0. 0 = no lower price limit. If provided, order executes only above this price |
| mpp | number | No | Default: 0. 0 = no market protection. Valid values: 0–3 or -1 (disabled) |

### Validations & Error Handling

| **Field** | **Validation Rule** | **Error Message** |
| --- | --- | --- |
| symbol | Must be a valid trading symbol | "The symbol entered is invalid." |
| symbol | Must be allowed for smart orders | "The selected symbol is not allowed for placing smart orders. Please try again with a different symbol." |
| symbol | Must be allowed for this segment | "The smart order not allowed for this segment" |
| side | Must be 1 or -1 (enum) | "The input details entered is invalid." |
| qty | Min: 1, Max: 999999, must be multiple of lot size | "Quantity should be multiple of min lot size." |
| **Field** | **Validation Rule** | **Error Message** |
| qty | Must not exceed freeze limit | "Quantity exceeds the allowable freeze limit." |
| productType | Must be one of: CNC, MARGIN, INTRADAY, MTF | "productType must be one of the following: CNC, MARGIN, INTRADAY, MTF" |
| productType | MTF requires MTF activation | "MTF is not enabled. Please use a different productType" |
| limitPrice | Min: 0.01 | "The input details entered is invalid." |
| orderType | Must be 1 or 4 (enum) | "orderType must be one of the following: 1, 4" |
| onExp | Must be 1 or 2 (enum) | "onExp must be one of the following: 1, 2" |
| endTime | Must not be 0 | "EndTime is required and cannot be 0." |
| endTime | Must be within market hours | "End time cannot fall within market closed hours." |
| endTime | Must not be in the past | "The end time entered is earlier than the current time." |
| endTime | Must be within current day | "The end time cannot extend beyond midnight of the current day." |
| hpr (buy) | Min: 0, if provided (>0), must be >= limitPrice | "The maximum price must be higher than the limit price." |
| lpr (sell) | Min: 0, if provided (>0), must be <= limitPrice | "The minimum price must be lower than the limit price." |
| stopPrice (buy) | Min: 0, if orderType=4, must be < limitPrice | "For buy orders, the stop price must be lower than the limit price." |
| stopPrice (sell) | Min: 0, if orderType=4, must be > limitPrice | "For sell orders, the stop price must be higher than the limit price." |
| mpp | If provided (>0), must be 0-3 or -1 | "MPP must be either -1 or a value between 0 to 3% (0 to 3)." |
| flowtype | Must be a valid smart order type | "The smart order specified in the URL path is not recognized." |
| User | Must not be banned for smart orders | "You are banned for smart order. Please contact support" |
| Trading day | Must not be market-closed day | "You can't create smart orders on market-closed day" |
| Trading day | Smart orders not allowed on special trading day | "Smart orders are not allowed on special trading day" |
| Trading hours | Must not be after market hours | "Smart orders cannot be created after market hours." |
| Trading hours | Must not be before 8:00 AM | "Smart orders are not allowed to be created before 8:00 AM." |
| Trading hours | Must be within regular trading hours | "You can't place a smart order outside regular trading hours" |

```
productType
```

Symbol/exchange must support MTF"This symbol or exchange is not supported for MTF." (MTF) "The selected contract expiry is not allowed for placing smart orders. Please try DerivativesExpiry must be allowed (F&O/CD) again with a near expiry contract." Strike price must be within allowed"The selected strike price is out of the permitted range. Please try with a strike Derivatives range (F&O/CD)price closer to the LTP" Daily limitMax 100 smart orders/day"You have exceeded the maximum limit of creating 100 smart orders for the day."

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code: 200 for success; negative values indicate errors. |
| message | string | Describes the response — e.g., "Request sent successfully to place smart order" or an error message. |
| s | string | "ok" for success, "error" for failure. |
| id | string | Unique identifier for the placed smart order (returned only on success). |

**Request samples**

```bash
curl --location 'https://api-t1.fyers.in/api/v3/smart-order/limit' \
--header 'Authorization: accessToken' \
--header 'Content-Type: application/json' \
--data '{
"symbol":"NSE:SBIN-EQ",
"side":1,
"qty":1,
"productType":"CNC",
"limitPrice":750,
"stopPrice":700,
"orderType":1,
"endTime":1738396200,
"hpr":800,
"lpr":700,
"mpp":1,
"onExp":2
}'
```

**Sample Success Response**

```json
{
"code":200,
"message":"Request sent successfully to place smart order",
"s":"ok",
"id":"1bf162b1-6406-407a-911a-5a3309e1aaba"
}
```

### Smart Trail (Trailing Stop Loss)

A Smart Trail Order is a trailing stop-loss that automatically adjusts the stop price as the market moves in your favour. The stop price trails the market by a specified jump price. Note: For sell orders, the stop price moves up as the price rises. For buy orders, the stop price moves down as the price falls. The order is triggered when the market price hits the trailing stop price. You can optionally set a target price to book profits automatically. Supports both Limit and Market (MPP) order types for execution. Supports only selected NSE and BSE symbols.

### Request Attributes

| **Attribute** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| symbol | string | Yes | The instrument's unique identifier, e.g., "NSE:SBIN-EQ" |
| side | integer | Yes | Order side: 1 for Buy, -1 for Sell (enum: 1, -1) |
| qty | integer | Yes | Order quantity (Min: 1, Max: 999999; must be a multiple of lot size) |
| productType | string | Yes | Must be one of: "CNC", "MARGIN", "INTRADAY", "MTF" |
| orderType | integer | Yes | Order type: 1 for Limit Order, 2 for Market Order (enum: 1, 2) |
| stopPrice | number | Yes | Initial stop/trigger price (must be greater than 0) |
| jump_diff | number | Yes | Jump price — the value by which the stop price trails (Min: 0.2) |
| limitPrice | number | No | Default: 0. If not provided, executes at market price. Required if orderType = 1. |
| target_price | number | No | Default: 0 (no target). If provided, must be greater than current LTP. |
| **Attribute** | **Data Type** | **Required** | **Description** |
| mpp | number | No | Default: 0 (no market protection). Valid values: 0–3 or -1 (disabled). |

### Validations & Error Messages

| **Field** | **Validation Rule** | **Error Message** |
| --- | --- | --- |
| symbol | Must be a valid trading symbol | "The symbol entered is invalid." |
| symbol | Must be allowed for smart orders | "The selected symbol is not allowed for placing smart orders. Please try again with a different symbol." |
| symbol | Must be allowed for this segment | "The smart order not allowed for this segment" |
| side | Must be 1 or -1 | "The input details entered is invalid." |
| qty | Min: 1, Max: 999999, must be multiple of lot size | "Quantity should be multiple of min lot size." |
|  | Must be one of: CNC, MARGIN, | "productType must be one of the following: CNC, MARGIN, INTRADAY, |

```
productType
```

INTRADAY, MTFMTF" orderTypeMust be 1 or 2"orderType must be one of the following: 1, 2" stopPriceMin: 0, cannot be 0 for placing order"Stop Price is required to place orders." jump_diffMin: 0.2, must be > 20× tick size"The jump price must be more than 20 times the tick size." limitPrice (buy)If orderType=1, must be < stopPrice"For buy orders, the stop price must be lower than the limit price." limitPrice (sell)If orderType=1, must be > stopPrice"For sell orders, the stop price must be higher than the limit price." "The target price must be greater than the last traded price for sell target_price (sell)If provided (>0), must be > current LTP orders." "The target price must be lesser than the last traded price for buy target_price (buy)If provided (>0), must be < current LTP orders." mppIf provided (>0), must be 0-3 or -1"MPP must be either -1 or a value between 0 to 3% (0 to 3)." If orderType=2 (Market), limitPrice must be limitPrice"Limit price is not required." 0 / not provided stopPrice (buy,"For buy orders, the stop price must be greater than the last traded Must be >= current LTP orderType=2)price." stopPrice (sell, Must be <= current LTP"For sell orders, the stop price must be less than the last traded price." orderType=2) flowtypeMust be a valid smart order type"The smart order specified in the URL path is not recognized." UserMust not be banned for smart orders"You are banned for smart order. Please contact support" Trading dayMust not be market-closed day"You can't create smart orders on market-closed day" Smart orders not allowed on special trading Trading day"Smart orders are not allowed on special trading day" day Trading hoursMust not be after market hours"Smart orders cannot be created after market hours." Trading hoursMust not be before 8:00 AM"Smart orders are not allowed to be created before 8:00 AM." Trading hoursMust be within regular trading hours"You can't place a smart order outside regular trading hours" "You have exceeded the maximum limit of creating 100 smart orders for Daily limitMax 100 smart orders/day the day."

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code: 200 indicates success; negative values indicate errors. |
| message | string | Descriptive message — e.g., "Request sent successfully to place smart order." or error reason. |
| s | string | "ok" for success, "error" for failure. |
| id | string | Unique identifier for the placed smart order (returned only on success). |

**Request samples**

```bash
curl --location 'https://api-t1.fyers.in/api/v3/smart-order/trail' \
--header 'Authorization: accessToken' \
--header 'Content-Type: application/json' \
--data '{
"symbol":"NSE:SBIN-EQ",
"side":-1,
"qty":1,
"productType":"CNC",
"stopPrice":740,
"jump_diff":5,
"orderType":2,
"mpp":1
}'
```

**Sample Success Response**

```json
{
"code":200,
"message":"Request sent successfully to place smart order",
"s":"ok",
"id":"2cf273c2-7517-518b-a22b-6b4420f2bcbc"
}
```

### Smart Step Order

Smart Step Order lets you average your position by placing orders at predefined price intervals, helping you build the position gradually across multiple price levels. Note: Starts with an initial quantity, followed by averaging based on defined step intervals. Direction determines whether orders are placed as the price increases or decreases. Orders are placed automatically at each step until the total quantity is fulfilled. Supports both price-based and time-based step execution. Supports only selected NSE and BSE symbols.

### Request Attributes

| **Attribute** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| symbol | string | Yes | The instrument's unique identifier, e.g., "NSE:SBIN-EQ" |
| side | integer | Yes | Order side: 1 for Buy, -1 for Sell (enum: 1, -1) |
| qty | integer | Yes | Total order quantity (Min: 1, Max: 999999; must be ≥ initQty + avgqty) |
| productType | string | Yes | Must be one of: "CNC", "MARGIN", "INTRADAY", "MTF" |
| orderType | integer | Yes | Order type: 1 for Limit, 2 for Market (enum: 1, 2). If orderType = 1, limitPrice is required. |
| avgqty | integer | Yes | Quantity to place at each averaging step (Min: 1, Max: 999999) |
| avgdiff | number | Yes | Price difference between averaging steps (Min: 0.01) |
| direction | integer | Yes | 1 for averaging on price decrease, -1 for averaging on price increase (enum: 1, -1) |
| startTime | integer | Yes | Unix timestamp (epoch) when the order should start executing |
| endTime | integer | Yes | Unix timestamp (epoch) when the order should expire |
| **Attribute** | **Data Type** | **Required** | **Description** |
| limitPrice | number | Conditional | Default: 0. Required if orderType = 1. Not needed for market orders. |
| initQty | integer | No | Default: 0. Quantity to place immediately. 0 = no initial order (Max: 999999) |
| hpr | number | No | Default: 0. 0 = no upper price limit. If set, execution allowed only below this price. |
| lpr | number | No | Default: 0. 0 = no lower price limit. If set, execution is allowed only above this price. |
| mpp | number | No | Default: 0. 0 = no market protection. Valid values: 0–3, or -1 (disabled) |

### Validations & Error Messages

| **Field** | **Validation Rule** | **Error Message** |
| --- | --- | --- |
| symbol | Must be a valid trading symbol | "The symbol entered is invalid." |
| symbol | Must be allowed for smart orders | "The selected symbol is not allowed for placing smart orders. Please try again with a different symbol." |
| symbol | Must be allowed for this segment | "The smart order not allowed for this segment" |
| side | Must be 1 or -1 (enum) | "The input details entered is invalid." |
|  | Min: 1, Max: 999999, must be >= initQty + | "Total Quantity should be greater than or equal to the sum of Initial Qty and Average |

```
qty
```

avgqtyQty." Must be one of: CNC, MARGIN, productType"productType must be one of the following: CNC, MARGIN, INTRADAY, MTF" INTRADAY, MTF orderTypeMust be 1 or 2 (enum)"orderType must be one of the following: 1, 2" limitPriceRequired if orderType=1"The input details entered is invalid." Min: 1, Max: 999999, must be multiple of avgqty"Avg quantity should be multiple of min lot size." lot size avgdiffMin: 0.01, must be > 20× tick size"The average entry price must be more than 20 times the tick size." directionMust be 1 or -1 (enum)"The input details entered is invalid." startTimeCannot be 0"Start Time is required to place orders." startTimeMust be within market hours"Start time cannot fall within market closed hours." startTimeCannot be in the past"The start time entered is earlier than the current time." startTimeMust be within current day"The start time cannot extend beyond midnight of the current day." endTimeCannot be 0"End Time is required to place orders." endTimeMust be within market hours"End time cannot fall within market closed hours." initQtyMin: 0, Max: 999999"The input details entered is invalid." hpr (buy, Min: 0, if provided must be >= limitPrice"The limit price cannot be higher than the upper price range." limit) lpr (buy, Min: 0, if provided must be <= limitPrice"The limit price cannot be lower than the lower price range." limit) mppIf provided (>0), must be 0-3 or -1"MPP must be either -1 or a value between 0 to 3% (0 to 3)." flowtypeMust be a valid smart order type"The smart order specified in the URL path is not recognized." UserMust not be banned for smart orders"You are banned for smart order. Please contact support" Trading dayMust not be market-closed day"You can't create smart orders on market-closed day" Smart orders not allowed on special Trading day"Smart orders are not allowed on special trading day" trading day Trading hoursMust not be after market hours"Smart orders cannot be created after market hours." Trading hoursMust not be before 8:00 AM"Smart orders are not allowed to be created before 8:00 AM." Trading hoursMust be within regular trading hours"You can't place a smart order outside regular trading hours" Daily limitMax 100 smart orders/day"You have exceeded the maximum limit of creating 100 smart orders for the day." **Note:** After the order starts executing, the following fields cannot be modified: initQty, limitPrice, orderType

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code: 200 for success; negative values indicate errors. |
| message | string | Text message describing the result — e.g., "Request sent successfully" or the error reason. |
| s | string | "ok" for success, "error" for failure. |
| id | string | Unique identifier for the placed smart order (returned only on success). |

**Request samples**

```bash
curl --location 'https://api-t1.fyers.in/api/v3/smart-order/step' \
--header 'Authorization: accessToken' \
--header 'Content-Type: application/json' \
--data '{
"symbol":"NSE:SBIN-EQ",
"side":1,
"qty":10,
"productType":"CNC",
"initQty":2,
"avgqty":2,
"avgdiff":5,
"direction":1,
"limitPrice":750,
"orderType":1,
"startTime":1738383000,
"endTime":1738396200,
"hpr":800,
"lpr":700,
"mpp":1
}'
```

**Sample Success Response**

```json
{
"code":200,
"message":"Request sent successfully to place smart order",
"s":"ok",
"id":"1bf162b1-6406-407a-911a-5a3309e1aaba"
}
```

### Smart SIP (Systematic Investment Plan)

Smart SIP allows you to automate recurring investments in equity stocks, ETFs, with orders placed automatically at your selected frequency—daily, weekly, monthly, or on custom dates. Note: Available only for **Equity segment** symbols on NSE/BSE CM. You can invest using either a fixed amount or a specified quantity. Use price range protection (HPR/LPR) to skip execution when prices move beyond your defined range. With the step-up option, you can gradually increase the investment amount or quantity over time.

### Request Attributes

| **Attribute** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| symbol | string | Yes | The instrument's unique identifier (Equity only), e.g., "NSE:SBIN-EQ" |
| productType | string | Yes | Must be one of: "CNC", "MTF" |
| freq | integer | Yes | SIP frequency (enum: 1, 2, 3, 6) |
| sip_day | integer | Yes | Day of the month for SIP execution (Min: 1, Max: 28) |
| qty OR | integer/number | Yes | At least one required - Quantity or amount per SIP instalment (Max: 999999) |

```
amount
```

Required if freq = 1 (Daily). Unix timestamp for SIP execution time (must be within market sip_timeintegerConditional hours) imd_startbooleanNoWhether to start SIP immediately. true = start now, false = wait for schedule endTimeintegerNoDefault: 0 (no end date). Unix timestamp when the SIP should end hprnumberNoDefault: 0. Skips SIP if price is above this upper limit lprnumberNoDefault: 0. Skips SIP if price is below this lower limit step_up_freqintegerNoFrequency of step-up increase (enum: 3, 5). Default: 0 (no step-up) step_up_qtyintegerNoQuantity to increase at each step-up (Default: 0; Max: 999999) step_up_amountnumberNoAmount to increase at each step-up (Default: 0; Max: 999999) exp_qtyintegerNoQuantity for expiry/final SIP order (Default: 0; Max: 999999)

### SIP Frequency Values

| **Value** | **Frequency** | **Required Field** | **Description** |
| --- | --- | --- | --- |
| 1 | Daily | sip_time | Invests every trading day at the specified time |
| 2 | Weekly | sip_day | Invests once a week on the specified day |
| 3 | Monthly | sip_day | Invests once a month on the specified day |
| 6 | Custom | sip_day | Invests on selected dates each month |

### Validations & Error Messages

| **Field** | **Validation Rule** | **Error Message** |
| --- | --- | --- |
| qty & amount | Provide either amount or qty (exactly one) | "Please enter either the amount or qty to place an order." |
| symbol | Must be Equity segment (NSE/BSE CM) | "Equity SIP is not available for the selected symbol. Please choose a different symbol." |
| productType | Must be CNC or MTF | "productType must be one of the following: CNC, MTF" |
| freq | Must be 1, 2, 3, or 6 (enum) | "The input details entered is invalid." |
| sip_day | Min: 1, Max: 28 | "The input details entered is invalid." |
| sip_time | Required if freq=1 | "Please select a SIP time." |
| sip_time | Must be within 9:15 AM - 3:30 PM | "Please select an SIP time within market hours." |
| qty | Max: 999999, must be multiple of lot size | "Quantity should be multiple of min lot size." |
| amount | If amount-based SIP, amount must not be < LTP | "The SIP amount cannot be less than the LTP." |
| step_up_freq | Must be >= freq (enum: 3, 5) | "Step-up frequency should be greater than or equal to the SIP frequency." |
| step_up_amount & step_up_qty | Only one of step_up_amount or step_up_qty allowed | "Please provide either step_up_amount or step_up_qty, not both." |
| step_up_freq | Step-up not allowed for custom frequency SIP | "Step-up is not allowed for custom frequency SIP." |
| **Field** | **Validation Rule** | **Error Message** |
| step_up_amount / step_up_qty | Step-up field must match SIP mode (amount vs qty) | "Please provide step_up_amount for amount based SIP or step_up_qty for qty based SIP." |
| hpr & lpr | HPR must be > LPR | "The high price range must be greater than the low price range." |
| sip_day | Required for SIP scheduling | "Please select a SIP day." |
| endTime | Must be > current day | "End time must be greater than the current day." |
| endTime | Expiry date must not fall on weekend | "The expiry date shouldn't be on a weekend." |
| endTime (Daily) | Must be >= 4 days from today | "Please select an expiry date at least 4 days from today." |
| endTime (Weekly/Monthly) | Must be >= 30 days from today | "Please select an expiry date at least 30 days from today." |
| Custom SIP | Custom SIP for today not allowed past cutoff | "You can't place a custom SIP for today past 11:00 AM." |
| sip_time | SIP time cannot be in the past | "The SIP time cannot be in the past. Please select a future date and time." |
| sip_day (weekly) | Weekly SIP day must be Mon–Fri (1–5) | "For weekly SIP, please select a day between 1 (Monday) and 5 (Friday)." |
| sip_day (monthly) | Monthly SIP day must be 1–28 | "For monthly SIP, please select a day between 1 and 28." |
| endTime & exp_qty | Provide either endTime or expired quantity, not both | "Please provide either endTime or expired quantity, not both." |
| Daily limit | Max SIP orders allowed | "You have exceeded the maximum limit of creating X SIP orders for the day." |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code: 200 for success; negative values indicate errors. |
| message | string | Success or error message. Example: "Your Equity SIP for {symbol} has been successfully initiated" |
| s | string | "ok" for success, "error" for failure. |
| id | string | Unique identifier for the placed SIP order (returned only on success). |

**Request samples**

```bash
# Monthly SIP with step-up
curl --location 'https://api-t1.fyers.in/api/v3/smart-order/sip' \
--header 'Authorization: accessToken' \
--header 'Content-Type: application/json' \
--data '{
"symbol":"NSE:SBIN-EQ",
"side":1,
"amount":5000,
"productType":"CNC",
"freq":3,
"sip_day":15,
"imd_start":false,
"endTime":1769846400,
"hpr":900,
"lpr":600,
"step_up_freq":3,
"step_up_amount":500
}'
```

**Sample Success Response**

```json
{
"code":200,
"message":"Your Equity SIP for NSE:SBIN-EQ has been successfully initiated",
"s":"ok",
"id":"1bf162b1-6406-407a-911a-5a3309e1aaba"
}
```

### Modify Smart Order

You can modify a pending Smart Order by updating parameters such as quantity, price, and time settings, depending on the order type. Note: The order must be in a paused state to be modified (except SIP orders). Only include the parameters you want to update. All others will retain their original values. Certain parameters cannot be modified once the order has started executing.

### Request Attributes

| **Attribute** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| flowId | string | Yes | Unique identifier of the Smart Order to be modified |

### Optional Request Attributes (by Order Type)

### **Limit Order (flowtype: 4)**

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| qty | integer | To update order quantity |
| limitPrice | number | To update limit price |
| stopPrice | number | To update stop/trigger price |
| endTime | integer | To update expiry time (Unix timestamp) |
| hpr | number | To update upper price limit (High Price Range) |
| lpr | number | To update lower price limit (Low Price Range) |
| mpp | number | To update market protection percentage |
| onExp | integer | To update expiry action (1 = Cancel, 2 = Market Order) |

### **Trail Order (flowtype: 6)**

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| qty | integer | To update order quantity |
| limitPrice | number | To update limit price (required if orderType = 1; must be 0 if orderType = 2) |
| stopPrice | number | To update stop/trigger price |
| jump_diff | number | To update jump value for trailing stop |
| target_price | number | To update target price (optional profit booking) |
| unsetTargetPrice | boolean | Set true to remove/unset the existing target_price |
| mpp | number | To update market protection percentage |

### **Step Order (flowtype: 3)**

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| qty | integer | To update total order quantity |
| startTime | integer | To update order start time |
| endTime | integer | To update order end time |
| hpr | number | To update upper price limit (High Price Range) |
| lpr | number | To update lower price limit (Low Price Range) |
| mpp | number | To update market protection percentage |
| avgqty | integer | To update quantity per averaging step |
| avgdiff | number | To update price gap between steps |
| initQty | integer | To update initial quantity (only before order starts) |
| limitPrice | number | To update limit price (only before order starts) |
| direction | integer | To update direction for averaging (1 = price drop, -1 = price rise) |

### **SIP Order (flowtype: 7)**

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| qty | integer | To update investment quantity per instalment |
| amount | number | To update investment amount per instalment |
| hpr | number | To update upper price limit (skip if price is above this) |
| lpr | number | To update lower price limit (skip if price is below this) |
| sip_day | integer | To update SIP day (applicable for monthly/custom frequency) |
| sip_time | integer | To update SIP time (required for daily/custom frequency) |
| step_up_amount | number | To update step-up amount (amount-based SIP only) |
| step_up_qty | integer | To update step-up quantity (qty-based SIP only) |
| exp_qty | integer | To update expiry quantity (optional) |
| exp_amount | number | To update expiry amount (optional) |

### Validations & Error Handling

### **General Validations**

| **Scenario** | **Error Message** |
| --- | --- |
| Invalid flowid | "The provided smart order ID is invalid." |
| Invalid request payload | "The input details entered is invalid." |
| Invalid order type | "Invalid Order type" |
| Order not paused (v3) | "The smart order must be paused before it can be modified." |
| **Scenario** | **Error Message** |
| Order already executed | "The modification attempt failed as the smart order was already executed." |
| Order already cancelled | "The modification attempt failed as the smart order was already cancelled." |
| Order cancelled by system | "The modification attempt failed as the smart order cancelled by system" |
| Qty < remaining qty | "Modification attempt failed as the specified quantity is less than the remaining quantity." |
| Qty not multiple of lot size | "Quantity should be multiple of min lot size." |
| Qty exceeds freeze limit | "Quantity exceeds the allowable freeze limit." |
| Field not allowed | "Amount field is not allowed." |
| SIP: changing frequency | "SIP frequency cannot be changed. Please use the same frequency as the existing order." |
| SIP: changing amount->qty | "Cannot change from amount-based SIP to qty-based SIP. Please use amount to modify this order." |
| SIP: changing qty->amount | "Cannot change from qty-based SIP to amount-based SIP. Please use qty to modify this order." |

### **Limit Order Validations (flowtype: 4)**

| **Field** | **Validation Rule** | **Error Message** |
| --- | --- | --- |
| endTime | Must be within market hours | "End time cannot fall within market closed hours." |
| endTime | Must not be in the past | "The end time entered is earlier than the current time." |
| endTime | Must be within current day | "The end time cannot extend beyond midnight of the current day." |
| hpr (buy) | If provided (>0), must be >= limitPrice | "The maximum price must be higher than the limit price." |
| lpr (sell) | If provided (>0), must be <= limitPrice | "The minimum price must be lower than the limit price." |
| stopPrice (buy) | If orderType=4, must be < limitPrice | "For buy orders, the stop price must be lower than the limit price." |
| stopPrice (sell) | If orderType=4, must be > limitPrice | "For sell orders, the stop price must be higher than the limit price." |
| mpp | Must be 0-3 or -1 (disabled) | "MPP must be either -1 or a value between 0 to 3% (0 to 3)." |

### **Trail Order Validations (flowtype: 6)**

| **Field** | **Validation Rule** | **Error Message** |
| --- | --- | --- |
| stopPrice | Required for trail orders | "Stop Price is required to place orders." |
| limitPrice | Required when orderType=1 (Limit) | "Limit price is required." |
| limitPrice (buy) | If orderType=1, must be < stopPrice | "For buy orders, the stop price must be lower than the limit price." |
| limitPrice (sell) | If orderType=1, must be > stopPrice | "For sell orders, the stop price must be higher than the limit price." |
| target_price | If provided (>0), must be > current LTP | "The target price must be greater than the last traded price." |
| jump_diff | Must be > 20× tick size | "The jump price must be more than 20 times the tick size." |
| mpp | Must be 0-3 or -1 (disabled) | "MPP must be either -1 or a value between 0 to 3% (0 to 3)." |

### **Step Order Validations (flowtype: 3)**

| **Field** | **Validation Rule** | **Error Message** |
| --- | --- | --- |
| startTime | Not allowed in modify request | "Start time is not required for modify orders." |
| startTime | Must not be in the past | "The start time entered is earlier than the current time." |
| startTime | Must be within market hours | "Start time cannot fall within market closed hours." |
| endTime | Must not be in the past | "The end time entered is earlier than the current time." |
| endTime | Must be within market hours | "End time cannot fall within market closed hours." |
| avgqty | Must be multiple of lot size | "Avg quantity should be multiple of min lot size." |
| initQty | Cannot modify after order starts | "You cannot modify the initial quantity after the order has been placed." |
| limitPrice | Cannot modify after order starts | "You cannot modify the Limit price after the order has been placed." |
| orderType | Cannot modify after order starts | "You cannot modify the order type after the order has been placed." |
| **Field** | **Validation Rule** | **Error Message** |
| qty | Total qty >= initQty + avgQty | "Total Quantity should be greater than or equal to the sum of Initial Qty and Average Qty." |
| mpp | Must be 0-3 or -1 (disabled) | "MPP must be either -1 or a value between 0 to 3% (0 to 3)." |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code: 200 for success; negative values indicate errors. |
| message | string | Message indicating success or failure. Example: "Request sent successfully to modify smart order." |
| s | string | "ok" for success, "error" for failure. |

**Request samples**

```bash
curl --location --request PATCH 'https://api-t1.fyers.in/api/v3/smart-order/modify' \
--header 'Authorization: accessToken' \
--header 'Content-Type: application/json' \
--data '{
"flowId":"9d12ded8-f046-440f-89f5-e750a37e6048",
"qty":5,
"limitPrice":760,
"endTime":1738396200
}'
```

**Sample Success Response**

```json
{
"code":200,
"message":"Request sent successfully to modify smart order",
"s":"ok"
}
```

### Cancel Smart Order

Cancel a pending Smart Order. Once cancelled, the order cannot be resumed.

### Request Attributes

| **Attribute** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| flowId | string | Yes | Unique identifier of the Smart Order to cancel |

### Validations & Error Handling

| **Scenario** | **Error Message** |
| --- | --- |
| Invalid flowid | "The provided smart order ID is invalid." |
| Invalid request payload | "The input details entered is invalid." |
| Internal error | "Error in Unmarshal" |
| Order already executed | "The cancellation attempt failed as the smart order was already executed." |
| **Scenario** | **Error Message** |
| Order already cancelled | "The cancellation attempt failed as the smart order was already cancelled." |
| Order cancelled by system | "The cancellation attempt failed as the smart order cancelled by system" |
| Invalid cancel request | "Smart order cannot be cancel." |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code: 200 for success; negative values indicate errors. |
| message | string | "Request sent successfully to cancel smart order" or error description. |
| s | string | "ok" for success, "error" for failure. |

**Request samples**

```bash
curl --location --request DELETE 'https://api-t1.fyers.in/api/v3/smart-order/cancel' \
--header 'Authorization: accessToken' \
--header 'Content-Type: application/json' \
--data '{
"flowId":"9d12ded8-f046-440f-89f5-e750a37e6048"
}'
```

**Sample Success Response**

```json
{
"code":200,
"message":"Request sent successfully to cancel smart order",
"s":"ok"
}
```

### Pause Smart Order

Pause a running smart order. This temporarily stops order execution without cancelling it. To modify a Smart Order, it must be paused first (pausing is not mandatory for Smart Limit order modification). The order can be resumed later using the Resume API.

### Request Attributes

| **Attribute** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| flowId | string | Yes | Unique identifier of the smart order to pause |

### Validations & Error Handling

| **Scenario** | **Error Message** |
| --- | --- |
| Invalid flowId | "The provided smart order ID is invalid." |
| Internal error | "Error in Unmarshal" |
| Order already executed | "You are attempting to pause a smart order that has already been executed." |
| **Scenario** | **Error Message** |
| Order already cancelled | "You are attempting to pause a smart order that has already been cancelled." |
| Order already paused | "The smart order is already paused and cannot be paused again." |
| Order in progress | "The smart order cannot be paused as it is already in progress." |
| Limit order during market hours | "Pausing is not allowed during market hours for limit orders." |
| Order cancelled by system | "The pause attempt failed as the smart order cancelled by system" |
| Invalid pause request | "Smart order cannot be paused." |
| Failed during creation | "The smart order cannot be paused as it has failed during creation." |
| Failed during modification | "The smart order cannot be paused as it has failed during modification." |
| Failed during resume | "The smart order cannot be paused as it has failed during resume." |
| Failed during pause | "The smart order cannot be paused as it has failed during pause." |
| Failed during deletion | "The smart order cannot be paused as it has failed during deletion." |
| Rejected | "The smart order cannot be paused as it has been rejected." |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code: 200 for success, negative values for errors |
| message | string | "Request sent successfully to pause smart order." or an error description |
| s | string | "ok" for success, "error" for failure |

**Request samples**

```bash
curl --location --request PATCH 'https://api-t1.fyers.in/api/v3/smart-order/pause' \
--header 'Authorization: accessToken' \
--header 'Content-Type: application/json' \
--data '{
"flowId":"9d12ded8-f046-440f-89f5-e750a37e6048"
}'
```

**Sample Success Response**

```json
{
"code":200,
"message":"Request sent successfully to pause smart order",
"s":"ok"
}
```

### Resume Smart Order

Resume a paused Smart Order. This restarts the order for execution and is mandatory after modifying the order.

### Request Attributes

| **Attribute** | **Data Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| flowId | string | Yes | Unique identifier of the smart order to resume |

### Validations & Error Handling

| **Scenario** | **Error Message** |
| --- | --- |
| Invalid flowId | "The provided smart order ID is invalid." |
| Internal error | "Error in Unmarshal" |
| Order not paused | "The smart order must be paused before it can be resumed." |
| Order already executed | "The smart order has already been executed and cannot be resumed." |
| Order already cancelled | "A canceled smart order cannot be resumed." |
| Order already running | "The smart order is already resumed and cannot be resumed again." |
| Order in progress | "The smart order cannot be resumed as it is already in progress." |
| Order cancelled by system | "The resume attempt failed as the smart order cancelled by system" |
| Invalid resume request | "Smart order cannot be resumed." |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code: 200 for success, negative for errors |
| message | string | "Request sent successfully to resume smart order." or error description |
| s | string | "ok" for success, "error" for failure |

**Request samples**

```bash
curl --location --request PATCH 'https://api-t1.fyers.in/api/v3/smart-order/resume' \
--header 'Authorization: accessToken' \
--header 'Content-Type: application/json' \
--data '{
"flowId":"9d12ded8-f046-440f-89f5-e750a37e6048"
}'
```

**Sample Success Response**

```json
{
"code":200,
"message":"Request sent successfully to resume smart order",
"s":"ok"
}
```

### Smart Order Book

Retrieve the list of all smart orders (active, completed, and cancelled).

### Optional Query Parameters

**Data**

| **Parameter** | **Default** | **Description** |
| --- | --- | --- |
| **Type** |  |  |
| flowtype integer[] | (all types) | Filter by order type (repeatable query param): 3 = Step, 4 = Limit, 5 = Peg, 6 = Trail, 7 = SIP |
| messageType integer[] | (all) | Filter by order status/message type (repeatable query param) |
| page_no integer | 1 | Page number for pagination |
| page_size integer | 15 | Number of records per page |
| sort_by string | "UpdatedTime" | Sort by field: "CreatedTime", "UpdatedTime", "Alphabet" |
| ord_by integer | -1 | Sort order: 1 for ascending, -1 for descending |
| side integer[] | (all) | Filter by side (repeatable query param): 1 for buy, -1 for sell |
| exchange string[] | (all) | Filter by exchange (repeatable query param): "NSE", "BSE", "MCX" |
| product string[] | (all) | Filter by product type (repeatable query param): "CNC", "MARGIN", "INTRADAY", "MTF" |
| search string | (none) | Search by symbol name |

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| code | integer | Status code: 200 indicates success |
| s | string | "ok" indicates success |
| orderBook | array | List of smart orders retrieved |
| count | integer | Total number of smart orders (before filters) |
| filterCount | integer | Number of smart orders after applying filters |

### Order Book Item Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| flowId | string | Unique order identifier |
| flowtype | integer | Order type (3=Step, 4=Limit, 6=Trail, 7=SIP) |
| symbol | string | Symbol ticker |
| side | integer | 1=Buy, -1=Sell |
| qty | integer | Total quantity |
| filledQty | integer | Executed quantity |
| status | integer | Order status |
| productType | string | Product type |
| createdTime | integer | Creation timestamp (epoch) |
| updatedTime | integer | Last update timestamp (epoch) |

**Request samples**

```bash
curl --location 'https://api-t1.fyers.in/api/v3/smart-order/orderbook?page_no=1&page_size=15' \
--header 'Authorization: accessToken'
```

**Sample Success Response**

```json
{
"code":200,
"s":"ok",
"orderBook": [
{
"flowId":"9d12ded8-f046-440f-89f5-e750a37e6048",
"flowtype":4,
"symbol":"NSE:SBIN-EQ",
"side":1,
"qty":5,
"filledQty":0,
"status":6,
"productType":"CNC",
"limitPrice":760,
"createdTime":1738383000,
"updatedTime":1738383000
}
],
"count":1,
"filterCount":1
}
```

## Other Transactions

### Modify Orders

This allows the user to modify a pending order. User can provide parameters which needs to be modified. In case a particular parameter has not been provided, the original value will be considered. **Endpoint:**PATCH /api/v3/orders/sync

### Order rate limiting (HTTP 429)

When order rate limiting is hit, the API returns HTTP 429 Too Many Requests. Retry timing is provided in response headers (not in the response body): Retry-After: wait time in **seconds** (standard HTTP header) X-Retry-After-Ms: wait time in **milliseconds** (precision header)

### Request attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| id* | string | Mandatory. Eg: 119031547242 |
| type* | int | Mandatory. |
| limitPrice | float | Mandatory. Only incase of Limit/ Stoplimit orders |
| stopPrice | float | Mandatory. Only incase of Stop/ Stoplimit orders |
| qty | int | Mandatory. Incase you want to modify the quantity |
| disclosedQty | int | Disclosed quantity (Optional) |

### Response attributes

**Data**

| **Attribute** | *******Description** |
| --- | --- |
| **Type** |  |
| s string | ok / error |
| code int | This is the code to identify specific responses If 201 comes in code it implies that order request has been made but no acknowledgement has been received in this case check orderbook before placing order |
| message string | Message to clarify the request status. Eg: Successfully modified order |
| id string | The order number of the modified order Eg: 119031547242 |

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X PATCH -d '{
"id":"809229222111",
"qty":1,
"type":2,
"side":1,
"limitPrice":61200
}' https://api-t1.fyers.in/api/v3/orders/sync
```

**Sample Success Response**

```json
{
"s":"ok",
"code":1101,
"message":"Successfully modified order', 'id': '808058117761"
}
```

### Modify Multi Orders

You can modify upto 10 orders simultaneously via the API. While Modifying Multi orders you need to pass an ARRAY containing the orders request attributes **Endpoint:**PATCH /api/v3/multi-order/sync

### Order rate limiting (HTTP 429)

When order rate limiting is hit, the API returns HTTP 429 Too Many Requests. Retry timing is provided in response headers (not in the response body): Retry-After: wait time in **seconds** (standard HTTP header) X-Retry-After-Ms: wait time in **milliseconds** (precision header) Sample Request :

```json
[{
"id":orderId,
"type":1,
"limitPrice": 61049,
"qty":1
},
{
"id":orderId,
"type":1,
"limitPrice": 61049,
"qty":1
}]
```

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X PATCH -d '[
{
"id":8102710298291,
"type":1,
"limitPrice":61049,
"qty":1
},
{
"id":8102710298292,
"type":1,
"limitPrice":61049,
"qty":1
}
]' https://api-t1.fyers.in/api/v3/multi-order/sync
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"",
"data": [{"statusCode":200,
"body": {
"s":"ok",
"code":200,
"message":"Successfully modified order",
"id":8102710298291
},
"statusDescription":"HTTP OK"
},
{
"statusCode":200,
"body": {
"s":"ok",
"code":200,
"message":"Successfully modified order",
"id":8102710298292
},
"statusDescription":"HTTP OK"
}
]}
}
```

### Cancel Order

Cancel pending orders via DELETE /api/v3/orders/sync with a JSON body containing id. You may alternatively use DELETE /api/v3/orders/{orderId}/sync with the order id in the path instead of the body.

### Order rate limiting (HTTP 429)

When order rate limiting is hit, the API returns HTTP 429 Too Many Requests. Retry timing is provided in response headers (not in the response body): Retry-After: wait time in **seconds** (standard HTTP header) X-Retry-After-Ms: wait time in **milliseconds** (precision header) For DELETE /api/v3/orders/{orderId}/sync, pass the order id in the path (orderId); a JSON body is not required.

### Request attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| id* | string | Mandatory for DELETE /api/v3/orders/sync (JSON body). Eg: 119031547242 |

### Response attributes

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| s string | ok / error |
| code int | This is the code to identify specific responses If 201 comes in code it implies that order request has been made but no acknowledgement has been received in this case check orderbook before placing order |
| message string | Message to clarify the request status. Eg: Successfully canceled order |
| id string | The order number of the canceled order. Eg: 119031547242 |

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X DELETE -d '{
"id":"52009227353"
}' https://api-t1.fyers.in/api/v3/orders/sync
# Alternative:  order id in path
# curl -H "Authorization:app_id:access_token"-X DELETE "https://api-t1.fyers.in/api/v3/orders/52009227353/sync"
```

**Sample Success Response**

```json
{
"s":"ok",
"code":1103,
"message":"Successfully cancelled order",
"id":"808058117761"
}
```

### Cancel Multi Order

You can cancel upto 10 orders simultaneously via the API. While cancelling Multi orders you need to pass an ARRAY containing the orders request attributes **Endpoint:**DELETE /api/v3/multi-order/sync

### Order rate limiting (HTTP 429)

When order rate limiting is hit, the API returns HTTP 429 Too Many Requests. Retry timing is provided in response headers (not in the response body): Retry-After: wait time in **seconds** (standard HTTP header) X-Retry-After-Ms: wait time in **milliseconds** (precision header) Sample Request :

```json
[{
"id":orderId
},
{
"id":orderId
}]
```

**Request samples**

```bash
curl --location --request DELETE 'https://api-t1.fyers.in/api/v3/multi-order/sync' \
--header 'Authorization: app_id:access_token' \
--header 'Content-Type: application/json' \
--header 'version: 3' \
--header 'Cookie: __cf_bm=GpjVBCIqRdfvM7e7HqkhAyo0jAbOQEq5zrAk9uqV1hs-1771416585-1.0.1.1-
lwzfCE6iZPodLxw_1rZYbU8fReZrVla4Dw09R_Fht_4ESaexeaVIRXqDlHNAeS9pbNA_8GSAsbgFSlJr9DL0wxBhDvLrEL0enSachoieA74' \
--data '[
{
"id":"808058117761"
},
{
"id":"808058117762"
}
]'
```

**Sample Success Response**

```json
{
"s":ok,
"code":200,
"message":"",
"data": [{"statusCode":200,
"body":
{
"s":ok,
"code":1103,
"message":"Successfully cancelled order",
"id":"808058117761"
},"statusDescription":"HTTP OK"
},
{
"statusCode":200,
"body":
{
"s":ok,
"code":1103,
"message":"Successfully cancelled order",
"id":"808058117762"
},"statusDescription":"HTTP OK"
}
]
}
```

### Exit Position

This allows the user to either exit all open positions or any specific open position.

### Request attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| Id | string | In case id is not passed, then all the open positions will be closed |

### Response attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | This is the code to identify specific responses . If 201 comes in code it implies that counter order has been placed but not filled due to low liquidity or any other reason |
| **Attribute** | **Data Type** | **Description** |
| message | string | Message to clarify the request status. Eg:All positions are closed |

Sample Request :

```json
{
"id": [positionId1,positionId2]
}
```

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X DELETE -d '{"exit_all":1}'
https://api-t1.fyers.in/api/v3/positions
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"The position is closed."
}
```

### Exit Position - By Id

### Request attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
|  | string or | Optional Eg: NSE:SBIN-EQ-BO |

```
id
```

[string]This will only exit the open positions for a particular position id or list of position id provided like ["NSE:SBIN-EQ- INTRADAY","NSE:SBIN-EQ-CNC"]

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X DELETE -d '{"id":"NSE:SBIN-EQ-BO"}'
https://api-t1.fyers.in/api/v3/positions
```

### Exit Position - By Segment Side & productType

### Request attributes

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| segment* [ int ] | **Mandatory** In the API , to close your position for a specific segment, you need to use the "segment" parameter with one of the following possible values: 10(Capital Market),11(Equity Derivatives),12(Currency Derivatives),20(Commodity Derivatives). Eg: [10,12] |
| side* [ int] | **Mandatory** In the API , to close your position for a specific side, you need to use the "side" parameter with one of the following possible values: 1(Buy side),-1(Sell side). Eg: [1,-1] |
| [ string productType* ] | **Mandatory** In the API , to close your position for a specific orderType, you need to use the "productType" parameter with one of the following possible values: "INTRADAY","CNC","CO","BO","MARGIN","ALL". Eg: ["INTRADAY","CNC"] |

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X DELETE -d '{"segment":[10],"side":
[1,-1],"productType":["INTRADAY","CNC"]}' https://api-t1.fyers.in/api/v3/positions
```

### Pending Order Cancel

This is an added functionality for exit position API. If a user has open positions in particular stocks and also working opposite order of the particular stock, the user can close the working orders and then exit the open positions. **[Endpoint: ](https://api-t1.fyers.in/api/v3/positions)**[https://api-t1.fyers.in/api/v3/positions](https://api-t1.fyers.in/api/v3/positions) The following should be passed in the body of the DELETE method of positions to cancel the pending orders:

```json
{"pending_orders_cancel": 1}
```

If only a single symbol's order and position needs to be cancelled, the position ID should also be sent in the body:

```json
{"id": "NSE:SBIN-EQ-INTRADAY","pending_orders_cancel": 1}
```

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X DELETE -d
'{"pending_orders_cancel": 1}' https://api-t1.fyers.in/api/v3/positions
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"The position is closed."
}
```

### Convert Position

This allows the user to convert an open position from one product type to another.

### Request attributes

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| symbol* string | Mandatory. pass the position id here Eg: NSE:SBIN-EQ-INTRADAY |
| overnight* int | Mandatory. if the position to be converted is a carry forward position, then send overnight flag as 1. If the position is taken today, irrespective of its product type, then send overnight flag as 0 |
| positionSide* int | Mandatory. 1 => Open long positions -1 => Open short positions View Details |
| convertQty* int | Mandatory. Quantity to be converted. Has to be in multiples of lot size for derivatives |
| convertFrom* string | Mandatory. Existing productType (CNC positions cannot be converted) View Details |
| convertTo* string | Mandatory. The new product type View Details |

**Notes** 1. CNC, CO, BO, and MTF positions cannot be converted. 2. You cannot convert positions to CO, BO,MTF.

### Response attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | This is the code to identify specific responses |
| message | string | Message to clarify the request status. Eg: You cannot convert CNC position to INTRADAY / MARGIN. |

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X POST -d '{
"symbol":"MCX:SILVERMIC20NOVFUT-INTRADAY",
"positionSide":1,
"convertQty":1,
"convertFrom":"INTRADAY",
"convertTo":"CNC",
"overnight":1
}' https://api-t1.fyers.in/api/v3/positions
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"message":"Position Converted Successfully!!",
"positionDetails":1101
}
```

## Margin Calculator

### Span Margin Calculator

Span margin API will calculate the span margin and exposure margin required for the given stock symbols.

### Request Attributes

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| symbol string | The symbol in fyers symbology format for which margin is calculated. Example - "NSE:NIFTY2292217000CE" |
| qty integer | The quantity of the particular stock. The quantity should be in multiples of lot size for derivatives. |
| side integer | Calculate margin for buy or sell order. 1 => Buy, -1 => Sell |
| type integer | 1 => Limit Order 2 => Market Order 3 => Stop Order (SL-M) 4 => Stoplimit Order (SL-L) More details - View Details |
| productType string | The product type.The possible values are, 1) CNC 2) INTRADAY 3) MARGIN 4) CO 5) BO 6) MTF More details - View Details |
| limitPrice float | The limit price to calculate margin. (Keep default as 0.0) |
| stopLoss float | Provide valid price to calculate margin for CO and BO orders. (Keep default as 0.0) |

**Request samples**

```bash
curl --location --request POST 'https://api.fyers.in/api/v2/span_margin' \ --header 'Authorization:
UC0KMO****-102:eyJ0eX*****' \--header 'Content-Type: application/json' \ --data-raw '{
"data": [{
"symbol":"NSE:BANKNIFTY23NOV44400CE",
"qty":50,
"side":-1,
"type":2,
"productType":"INTRADAY",
"limitPrice":0.0,
"stopLoss":0.0
}, {
"symbol":"NSE:BANKNIFTY23NOVFUT",
"qty":50,
"side":-1,
"type":2,
"productType":"INTRADAY",
"limitPrice":0.0,
"stopLoss":0.0
}]
```

### Multiorder Margin Calculator

This API provides the required margin based on the list of orders passed in the request payload. The required margin may vary based on the order sequence in the payload. For example, If the BUY order is passed first and the SELL order is passed next, the margin calculation considers the hedge benefit. If the SELL order is added before the BUY order, the hedge benefit may not be considered.

### Request Attributes

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| symbol string | The symbol in fyers symbology format for which margin is calculated. Example - "NSE:NIFTY2292217000CE" |
| qty integer | The quantity of the particular stock. The quantity should be in multiples of lot size for derivatives. |
| side integer | Calculate margin for buy or sell order. 1 => Buy, -1 => Sell |
| type integer | 1 => Limit Order 2 => Market Order 3 => Stop Order (SL-M) 4 => Stoplimit Order (SL-L) More details - View Details |
| productType string | The product type.The possible values are, 1) CNC 2) INTRADAY 3) MARGIN 4) CO 5) BO 6) MTF More details - View Details |
| limitPrice float | The limit price to calculate margin. (Keep default as 0.0) |
| stopLoss float | Provide valid price to calculate margin for CO and BO orders.(Keep default as 0.0) |
| stopPrice float | The stop price to calculate margin.(Keep default as 0.0) .(Keep default as 0.0) |
| takeProfit float | Provide valid take profit price to calculate margin for CO and BO orders.(Keep default as 0.0) |

### Response attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | This is the code to identify specific responses |
| margin_total | float | Approximate margin required for the order. |
| margin_new_order | float | Approximate Total margin required including existing positions |
| margin_avail | float | Approximate available margin |

**Request samples**

```bash
curl --location 'https://api-t1.fyers.in/api/v3/multiorder/margin' \
--header 'Content-Type: application/json' \
--header 'Authorization: UC0KMO****-102:eyJ0eX*****' \
--data '{
"data": [
{
"symbol":"MCX:GOLDPETAL26JUNFUT",
"qty":2,
"side":1,
"type":1,
"productType":"INTRADAY",
"limitPrice":15800,
"stopLoss":0.0,
"stopPrice":0.0,
"takeProfit":0.0
}
]
} '
```

**Sample Success Response**

```json
{
"code":200,
"message":"",
"data": {
"margin_avail":1999.9,
"margin_total":147738.05634886527,
"margin_new_order":147738.05634886527
},
"s":"ok"
}
```

## Broker Config

### Market Status

Fetches the current market status of all the exchanges and their segments

### Response attributes - For each exchange market segment

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| exchange | int | The exchange in which the position is taken. View Details |
| segment | int | The segment in which the position is taken. View Details |
| market_type | string | NORMAL, ODD_LOT, CALL_AUCTION2, AUCTION |
| **Attribute** | **Data Type** | **Description** |
| status | string | CLOSE OPEN POSTCLOSE_START POSTCLOSE_CLOSED PREOPEN PREOPEN_CLOSED |

**Request samples**

**cURL****python****node****Web modular API****C#****Java****Go****C**

**Curl Request Method**

```bash
curl -H "Authorization:app_id:access_token" https://api-t1.fyers.in/data/marketStatus
```

**Sample Success Response**

```json
{
"code":200,
"marketStatus":[
{
"exchange":10,
"market_type": "NORMAL",
"segment":10,
"status": "POSTCLOSE_CLOSED"
},
{
"exchange":10,
"market_type": "NORMAL",
"segment":11,
"status": "CLOSED"
},
{
"exchange":10,
"market_type": "NORMAL",
"segment":12,
"status": "CLOSED"
},
{
"exchange":10,
"market_type": "CALL_AUCTION2",
"segment":10,
"status": "CLOSED"
},
{
"exchange":10,
"market_type": "AUCTION",
"segment":10,
"status": "CLOSED"
},
{
"exchange":10,
"market_type": "ODD_LOT",
"segment":10,
"status": "CLOSED"
},
{
"exchange":11,
"market_type": "NORMAL",
"segment":20,
"status": "OPEN"
},
{
"exchange":11,
"market_type": "SPECIAL",
"segment":20,
"status": "CLOSED"
},
{
"exchange":12,
"market_type": "NORMAL",
"segment":10,
"status": "POSTCLOSE_CLOSED"
},
{
"exchange":12,
"market_type": "NORMAL",
"segment":12,
"status": "POSTCLOSE_CLOSED"
},
{
```

```
"exchange":12,
"market_type": "AUCTION",
"segment":10,
"status": "CLOSED"
},
{
"exchange":12,
"market_type": "NORMAL",
"segment":11,
"status": "POSTCLOSE_CLOSED"
}
],
"message": "",
"s": "ok"
}
```

### Symbol Master

You can get all the latest symbols of all the exchanges from the symbol master files **NSE – Currency Derivatives:** [https://public.fyers.in/sym_details/NSE_CD.csv](https://public.fyers.in/sym_details/NSE_CD.csv) **NSE – Equity Derivatives:** [https://public.fyers.in/sym_details/NSE_FO.csv](https://public.fyers.in/sym_details/NSE_FO.csv) **NSE – Commodity:** [https://public.fyers.in/sym_details/NSE_COM.csv](https://public.fyers.in/sym_details/NSE_COM.csv) **NSE – Capital Market:** [https://public.fyers.in/sym_details/NSE_CM.csv](https://public.fyers.in/sym_details/NSE_CM.csv) **BSE – Capital Market:** [https://public.fyers.in/sym_details/BSE_CM.csv](https://public.fyers.in/sym_details/BSE_CM.csv) **BSE - Equity Derivatives:** [https://public.fyers.in/sym_details/BSE_FO.csv](https://public.fyers.in/sym_details/BSE_FO.csv) **MCX - Commodity:** [https://public.fyers.in/sym_details/MCX_COM.csv](https://public.fyers.in/sym_details/MCX_COM.csv)

### File Headers

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| Fytoken | string | Unique token for each symbol View Details |
| Symbol Details | string | Name of the symbol |
| Exchange Instrument type | int | Exchange instrument type View Details |
| Minimum lot size | int | Minimum qty multiplier |
| Tick size | float | Minimum price multiplier |
| ISIN | string | Unique ISIN provided by exchange for each symbol |
| Trading Session | string | Trading session provided in IST |
| Last update date | date | Date of last update |
| Expiry date | string | Date of expiry for a symbol.Applicable only for derivative contracts |
| Symbol ticker | string | Unique string to identify the symbol |
| Exchange | int | Exchange mapping View Details |
| Segment | int | Segment of the symbol View Details |
| Scrip code | int | Token of the Exchange |
| Underlying symbol | string | name of underlying symbol |
| Underlying scrip code | int | Scrip code of underlying symbol |
| **Attribute** | **Data Type** | **Description** |
| Strike price | float | Strike price |
| Option type | string | CE/PE - For options XX - For other segments |
| Underlying FyToken | string | Unique token for the underlying symbol |
| Reserved column | string | Reserved for future, kindly ignore |
| Reserved column | int | Reserved for future, kindly ignore |
| Reserved column | float | Reserved for future, kindly ignore |

### Symbol Master Json

You can get all the latest symbols of all the exchanges from the symbol master json files **NSE – Currency Derivatives:** [https://public.fyers.in/sym_details/NSE_CD_sym_master.json](https://public.fyers.in/sym_details/NSE_CD_sym_master.json) **NSE – Equity Derivatives:** [https://public.fyers.in/sym_details/NSE_FO_sym_master.json](https://public.fyers.in/sym_details/NSE_FO_sym_master.json) **NSE – Commodity:** [https://public.fyers.in/sym_details/NSE_COM_sym_master.json](https://public.fyers.in/sym_details/NSE_COM_sym_master.json) **NSE – Capital Market:** [https://public.fyers.in/sym_details/NSE_CM_sym_master.json](https://public.fyers.in/sym_details/NSE_CM_sym_master.json) **BSE – Capital Market:** [https://public.fyers.in/sym_details/BSE_CM_sym_master.json](https://public.fyers.in/sym_details/BSE_CM_sym_master.json) **BSE - Equity Derivatives:** [https://public.fyers.in/sym_details/BSE_FO_sym_master.json](https://public.fyers.in/sym_details/BSE_FO_sym_master.json) **MCX - Commodity:** [https://public.fyers.in/sym_details/MCX_COM_sym_master.json](https://public.fyers.in/sym_details/MCX_COM_sym_master.json)

### File Format

Key will be the symbol ticker and value will hold the below json object which has symbol master details for that particular symbol ticker.

| **Key** | **Data Type Of Values** | **Description** |
| --- | --- | --- |
| fyToken | string | Unique token for the security View Details |
| isin | string | ISIN code for the security |
| exSymbol | string | Exchange symbol of the security |
| symDetails | string | Full name of the security |
| symTicker | string | Unique string to identify the security |
| exchange | int | Exchange mapping View Details |
| segment | int | Segment of the security View Details |
| exSymName | string | Symbol name of the security |
| exToken | int | Exchange token |
| exSeries | string | Series of the security. This can be used only for CM segments |
| optType | string | CE/PE - For options XX - For others |
| underSym | string | name of underlying symbol |
| underFyTok | string | Unique token for the underlying symbol |
| **Key** | **Data Type Of Values** | **Description** |
| exInstType | int | Exchange instrument type View Details |
| minLotSize | int | Minimum qty multiplier |
| tickSize | float | Minimum price multiplier |
| tradingSession | string | Trading session provided in IST |
| lastUpdate | string | Date of last update in YYYY-MM-DD format |
| expiryDate | string | Date of expiry for a symbol in timestamp.Applicable only for derivative contracts |
| strikePrice | float | Strike price |
| qtyFreeze | string | Freeze qty Empty string in case value is not applicable |
| tradeStatus | int | Flag to check if security is allowed to trade. Expected values - 0/1 1 = Active. 0 = Inactive. |
| currencyCode | string | Currency code |
| upperPrice | float | Upper circut price |
| lowerPrice | float | Lower circut price |
| faceValue | float | Face value |
| qtyMultiplier | float | Quantity multipler |
| previousClose | float | Previous close price |
| previousOi | float | Previous OI value |
| asmGsmVal | string | Surveillance Indicator message |
| exchangeName | string | Exchange Name NSE/BSE/MCX |
| symbolDesc | string | Full name of the security |
| originalExpDate | string | Kindly ignore this field |
| is_mtf_tradable | int | 0: Not MTF tradable. 1: MTF tradable. |
| mtf_margin | float | Indicates the margin multiplier available for MTF transactions. For example, a value of 2.9 means you receive 2.9x margin on the stock or security. |
| stream | string | Stream Group |

## EDIS

Electronic Delivery Instruction Slip (eDIS) allows you to sell shares if your Power of Attorney (POA) is not submitted or DDPI is not activated. Please note: You can only sell the authorized stocks that you are holding in your Demat account. You can **[activate DDPI](https://support.fyers.in/portal/en/kb/articles/how-do-i-activate-ddpi-for-my-account-on-fyers)**[ to ensure a smooth and](https://support.fyers.in/portal/en/kb/articles/how-do-i-activate-ddpi-for-my-account-on-fyers) uninterrupted trading experience.

### TPIN Generation

TPIN is an authorization code generated by CDSL/NSDL respectively, using which the customer validates/authorises the transaction.

**Request samples**

```bash
curl --location --request GET 'https://api.fyers.in/api/v2/tpin'
--header 'Authorization: app_id:access_token'
```

**Sample Success Response**

```json
{"s":"ok","code":200,"message":"Successfully sent request for BO Tpin generation","data":""}
```

### Details

This API provides information about holding authorizations that have been successfully completed.

**Request samples**

```bash
curl --location --request GET 'https://api.fyers.in/api/v2/details' \
--header 'Authorization: app_id:access_token'
```

**Sample Success Response**

```json
{"s":"ok","code":200,"message":"","data": [{"clientId":"DXXXX4","isin":"INE313D01013","qty":1.0,
"qtyUtlize":0.0,"entryDate":"07/06/2021 13:58:56","startDate":"07/06/2021","endDate":"07/06/2021","noOfDays":
1,"source":"W","status":"SUCCESS","reason":"eDIS Transaction done successfully","internalTxnId":"915485",
"dpTxnId":"0706202171316317","errCode":"NA","errorCount":"0","transactionId":"915484108176"}]
```

### Index

This Api will provide you with the CDSL page to login where you can submit your Holdings information and accordingly you can provide the same to exchange to Sell your holdings.

**Request samples**

```bash
curl --location --request POST 'https://api.fyers.in/api/v2/index'--header 'Authorization: app_id:accessToken'--
header 'Content-Type: application/json'
--data-raw '{"recordLst": [{"isin_code": "INE114A01011","qty": "1","symbol": "NSE:SAIL-EQ"}]}'
```

**Sample Success Response**

```json
{"s":"ok","code":200,"message":"","data":"<table width=\"100%\"><tr><td><table align=\"center\"><tr><td>
<table  align=\"center\"><tr><th><img src=\"https://clib.fyers.in/fy_images/320x132.png\" alt=\"Fyers\" width=\"220\"
/></th></tr><tr style=\"color:#7c7e7f;\"><th class=\"sansserif\">      Free Investment Zone</th></tr>
</table></td></tr></table><table align=\"center\" bgcolor=\"#ffffff\"  style=\"Margin: 0 auto;max-width: 600px;min-
width: 320px; border-style:solid;border-left-width:10px;padding:5px; border-color:#ffffff;\"><tr
style=\"color:#3e4751;\"><th><img src=\"https://mockedis.cdslindia.com/images/CDSL-Logo.png\"></th> </tr><tr><th><hr
style=\" border:1px solid\" width=\"12%\"><br></th></tr><br><tr align=\"left\" style=\"color:#7c7e7f;\"><td
class=\"sansserif\" id=\"tpinDescp\">As per new regulations, clients are required to authorise sell transactions by
providing specific instrument details along with quantites at the CDSL portal prior to executing any sell transactions
from their demat account.<br><br> The autorisation will be valid till the end of the day irrespective of whether you
have completed the sell transaction or not. <br><br></td></tr><tr align=\"left\" style=\"color:#7c7e7f;\"><td
class=\"sansserif\"><br></td></tr><tr align=\"left\" style=\"color:#7c7e7f;\"><td class=\"sansserif\" style=\"text-
align:center\"><br><br>       <form name= \"frmDIS\" method = \"post\" action=
\"https://eDIS.cdslindia.com/eDIS/VerifyDIS\" >        <input type= \"hidden\" name= \"DPId\" value= \"89400\" />
<input type= \"hidden\" name= \"ReqId\" value= \"917177108176\" />        <input type= \"hidden\" name= \"Version\"
value= \"1.1\" />        <input type= \"hidden\" name= \"TransDtls\" value=
\"LD9WAIJCL2jgSj1hY2DABqfayzA6iInmBvh9ub+Ftqy0P+V/Qy4kRf9dsBHElVwcDdAhTx5a6+9g3y/TcVh1zEdMbslVXAcMi913u+YwHNp5IWUS6XAOC
/>        <input type= \"submit\" value=\"Submit\">         </form></td></tr><tr><td style=\"text-align: center;\"
class=\"like-anchor\"><div id=\"forgetTpinDiv\"><a href=\"#\" id=\"forgetTpin\" onclick=\"tpin()\">Forgot CDSL
TPIN</a></div></td></tr></tbody></table></td></tr></tbody></table>"}
```

### Inquiry

This Api is used to get the information/status of the provided transaction Id for the respective holdings you have on your end. **Note:** Transaction ID to be base64 encoded in payload. please refer to the [online tool](https://emn178.github.io/online-tools/base64_encode.html) for conversion.

**Request samples**

```bash
curl --location --request POST 'https://api.fyers.in/api/v2/inquiry'
--header 'Authorization: app_id:access_Token'--header 'Content-Type: application/json'--data-raw '{"transactionId":
"OTE1NDg0MTA4MTc2"}'
```

**Sample Success Response**

```json
{"s":"ok","code":200,"message":"","data": {"FAILED_CNT":0,"SUCEESS_CNT":1}}
```

## Postback (Webhooks)

The Postback API sends a POST request with a JSON payload to the registered postback_url of your app when an order's status changes. This enables you to get orders updates reliably, irrespective of when they happen (Pending, Cancel, Rejected, Traded).

### 1. Create web hooks

To Create Postback, you need to create an App by: 1. Login to **[API Dashboard](https://myapi.fyers.in/dashboard/)**. 2. Once you have logged into the Dashboard, you will see a block where you need to update your webhook URL, webhook secret, and the webhook preference (Cancel, Rejected, Pending, Traded). Here you can add multiple webhooks by clicking on the "Add webhook" button. 3. After entering the required details, click on the "Create App" button by accepting the terms and conditions.

### 2. Active App

After successful creation of the App, you need to activate the App by following the Authentication & Login mechanism. After successfully logging in via the App, you will be able to get the order data over the webhook URL.

### 3. Response

The JSON payload is posted as a raw HTTP POST body. You will have to read the raw body. **Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| id string | The unique order ID assigned for each order |
| exchOrdId string | The order ID provided by the exchange |
| symbol string | The symbol for which the order is placed |
| qty int | The original order quantity |
| **Data** **Attribute** **Type** | **Description** |
| remainingQuantity int | The remaining quantity |
| filledQty int | The filled quantity after partial trades |
| status int | 1 => Canceled, 2 => Traded / Filled, 3 => (Not used currently), 4 => Transit, 5 => Rejected, 6 => Pending, 7 => Expired. |
| message string | The error messages are shown here |
| segment int | 10 (Equity), 11 (F&O), 12 (Currency), 20 (Commodity). **View Details** |
| limitPrice float | The limit price for the order |
| stopPrice float | The stop price for the order |
| productType string | The product type |
| type int | 1 => Limit Order, 2 => Market Order, 3 => Stop Order (SL-M), 4 => Stop Limit Order (SL-L). **View Details** |
| side int | Disclosed quantity: 1 => Buy, -1 => Sell. **View Details** |
| disclosedQty int | Disclosed quantity |
| dqQtyRem int | Remaining disclosed quantity |
| orderValidity string | DAY, IOC |
| orderDateTime string | The datetime object here will be in epoch timestamp |
| tradedPrice float | The average traded price for the order |
| source string | Source from where the order was placed. **View Details** |
| fytoken string | Fytoken is a unique identifier for every symbol. **View Details** |
| offlineOrder boolean | False => When the market is open, True => When placing AMO order |
| pan string | PAN of the client |
| clientId string | The client ID of the Fyers user |
| exchange int | The exchange in which the order is placed. **View Details** |
| instrument string | Exchange instrument type. **View Details** |

Response Output :

```json
{
"orderDateTime": "18-Jul-2023 11:44:29",
"id": "23071800238607",
"exchOrdId": "2500000061319029",
"side": -1,
"segment": 11,
"instrument": 15,
"productType": "MARGIN",
"status": 2,
"qty": 5400,
"remainingQuantity": 0,
"filledQty": 5400,
"limitPrice": 2.15,
"stopPrice": 0,
"type": 2,
"discloseQty": 0,
"dqQtyRem": 0,
"orderValidity": "DAY",
"source": "M",
"fyToken": "101123072754619",
"offlineOrder": false,
"message": "Completed",
"orderNumStatus": "23071800238607:2",
"tradedPrice": 2.15,
"exchange": 10,
"pan": "",
"clientId": "xxxx",
"symbol": "NSE:ABCAPITAL23JUL190CE"
}
```

### 4. Blacklisting

The webhook/postback URL provided by the user can be blacklisted if the response status is not 200 from your web server or if the post request to your PostbackURL fails. These URLs are blacklisted for 30 minutes, and during that time, no webhooks are sent to the blacklisted URL. Additionally, the URL will be blacklisted after continuous failures, typically after three retries.

## Data Api

### History

The historical API provides archived data (up to date) for the symbols. across various exchanges within the given range. A historical record is presented in the form of a candle and the data is available in different resolutions like - minute, 10 minutes, 60 minutes...240 minutes and daily. **To Handle partial Candle** To receive completed candle data, it is important to send a timestamp that comes before the current minute. If you send a timestamp for the current minute, you will receive partial data because the minute is not yet finished. Therefore, it is recommended to always use a "range_to" timestamp of the previous minute to ensure that you receive the completed candle data. **Example:** Current Time(seconds can be 1-59): 12:10:20 PM Input for history will be: range_from: 12:08:00 PM range_to: Current Time - 1 minute = 12:09:20 PM So you will get 2 candles - 12:08 PM and 12:09 PM candles. This example is for 1-minute candles; for other resolutions, you have to subtract the resolution time from "range_to" to get completed candles only. **Limits for History** Unlimited number of stocks history data can be downloaded in a day. Up to 100 days of data per request for resolutions of 1, 2, 3, 5, 10, 15, 20, 30, 45, 60, 120, 180, and 240 minutes. Data is available from July 3, 2017. For 1D, 1W and 1M resolutions up to 366 days of data per request for 1D (1 day), 1W (1 week) and 1M (1 month) resolutions. For Seconds Charts the history will be available only for 30-Trading Days

### Request Attribute

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| symbol* string | Mandatory. Eg: NSE:SBIN-EQ |
| **Data** **Attribute** **Type** | **Description** |
| resolution* string | The candle resolution. Possible values are: Day : “D” or “1D” 5 seconds : “5S” 10 seconds : “10S” 15 seconds : “15S” 30 seconds : “30S” 45 seconds : “45S” 1 minute : “1” 2 minute : “2" 3 minute : "3" 5 minute : "5" 10 minute : "10" 15 minute : "15" 20 minute : "20" 30 minute : "30" 60 minute : "60" 120 minute : "120" 240 minute : "240" 1 week : "1W" 1 month : "1M" |
| date_format* int | date_format is a boolean flag. 0 to enter the epoch value. Eg:670073472. 1 to enter the date format as yyyy-mm- dd. |
| range_from* string | Indicating the start date of records. Accepts epoch value if date_format flag is set to 0. Eg: range_from: 670073472 Accepts yyyy-mm-dd format if date_format flag is set to 1. Eg: 2021-01-01 |
| range_to* string | Indicating the end date of records. Accepts epoch value if date_format flag is set to 0. Eg: range_to: 1622028732 Accepts yyyy-mm-dd format if date_format flag is set to 1. Eg:2021-03-01 |
| cont_flag int | set cont flag 1 for continues data and future options. |
| oi_flag int | set flag to "1" enable oi as a part of candle. |

### Response Attribute

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| Candels | array | Candles data containing array of following data for particular time stamp: 1.Current epoch time 2. Open Value 3.Highest Value 4.Lowest Value 5.Close Value 6.Total traded quantity (volume) |

**Request samples**

```bash
curl --location --request GET 'https://api-t1.fyers.in/data/history?symbol=NSE:SBIN-
EQ&resolution=30&date_format=1&range_from=2021-01-01&range_to=2021-01-02&cont_flag=' \
--header 'Authorization: app_id: access_token’
```

**Sample Success Response**

```json
{
"s":"ok",
"candles": [
[
1621814400,
417.0,
419.2,
405.3,
412.05,
142964052
],
[
1621900800,
415.1,
415.5,
408.5,
412.35,
56048127
],
[
1621987200,
413.8,
418.75,
410.8,
413.55,
52357719
],
[
1622073600,
413.7,
429.1,
412.0,
425.2,
73392997
]
]
}
```

### Quotes

The Quotes API retrieves the full market quotes for one or more symbols provided by the user.

### Request attributes

| **Attribute** | **Data Type** | *******Description** |
| --- | --- | --- |
| symbols* | string | Maximum symbol limit is 50. Eg: NSE:SBIN-EQ. |

### Response attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| ch | float | Change value |
| chp | float | Percentage of change between the current value and the previous day's market close |
| **Attribute** | **Data Type** | **Description** |
| lp | float | Last traded price |
| spread | float | Difference between lowest asking and highest bidding price |
| ask | float | Asking price for the symbol |
| bid | float | Bidding price for the symbol |
| open_price | float | Price at market opening time |
| high_price | float | Highest price for the day |
| low_price | float | Lowest price for the day |
| prev_close_price | float | Previous closing price |
| atp | float | Average traded price |
| volume | int | Volume traded |
| short_name | string | Short name for the symbol Eg: “SBIN-EQ” |
| exchange | string | Name of the exchange. Eg: “NSE” or “BSE” |
| description | string | Description of the symbol |
| original_name | string | Original name of the symbol name provided by the use |
| symbol | string | Symbol name provided by the user |
| fyToken | string | Unique token for each symbol |
| tt | int | Today’s time |
| cmd | dict | ---Deprecated--- |

**Request samples**

```bash
curl --location --request GET 'https://api-t1.fyers.in/data/quotes?symbols=NSE:SBIN-EQ' \
--header 'Authorization:  app_id: access_token’
```

**Sample Success Response**

```json
{
"s":"ok",
"code":200,
"d": [
{
"n":"NSE:SBIN-EQ",
"s":"ok",
"v": {
"ch":1.7,
"chp":0.4,
"lp":426.9,
"spread":0.05,
"ask":426.9,
"bid":426.85,
"open_price":430.5,
"high_price":433.65,
"low_price":423.6,
"prev_close_price":425.2,
"atp":428.07,
"volume":38977242,
"short_name":"SBIN-EQ",
"exchange":"NSE",
"description":"NSE:SBIN-EQ",
"original_name":"NSE:SBIN-EQ",
"symbol":"NSE:SBIN-EQ",
"fyToken":"10100000003045",
"tt":"1622160000",
}
}
]
}
```

### Market Depth

The Market Depth API returns the complete market data of the symbol provided. It will include the quantity, OHLC values, and Open Interest fields, and bid/ask prices.

### Request attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol* | string | Maximum symbol limit is 1. Eg: NSE:SBIN-EQ |
| ohlcv_flag* | int | Set the ohlcv_flag to 1 to get open, high, low, closing and volume quantity' |

### Response attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | This is the code to identify specific responses |
| totalbuyqty | int | Total buying quantity |
| totalsellqty | int | Total selling quantity |
| bids | array | Bidding price along with volume and total number of orders |
| ask | array | Offer price with volume and total number of orders |
| **Attribute** | **Data Type** | **Description** |
| o | float | Price at market opening time |
| h | float | Highest price for the day |
| i | float | Lowest price for the day |
| c | float | Price at the of market closing |
| chp | float | Percentage of change between the current value and the previous day's market close |
| tick_Size | float | Minimum price multiplier |
| ch | float | Change value |
| ltq | int | Last traded quantity |
| ltt | int | Last traded time |
| ltp | float | Last traded price |
| v | int | Volume traded |
| atp | float | Average traded price |
| lower_ckt | float | Lower circuit price` |
| upper_ckt | float | upper circuit price |
| expiry | string | Expiry date |
| oi | float | Open interest |
| oiflag | bool | Boolean flag for OI data, true or false |
| pdoi | int | previous day open interest |
| oipercent | float | Change in open Interest percentage |

**Request samples**

```bash
curl --location --request GET 'https://api-t1.fyers.in/data/depth?symbol=NSE:SBIN-EQ&ohlcv_flag=1' \
--header 'Authorization: app_id: access_token’
```

**Sample Success Response**

```json
{
"s":"ok",
"d": {
"NSE:SBIN-EQ": {
"totalbuyqty":2396063,
"totalsellqty":4990001,
"bids": [
{
"price":427.25,
"volume":4738,
"ord":5
},
{
"price":427.2,
"volume":2631,
"ord":9
},
{
"price":427.15,
"volume":6366,
"ord":19
},
{
"price":427.1,
"volume":6344,
"ord":18
},
{
"price":427.05,
"volume":8136,
"ord":16
}
],
"ask": [
{
"price":427.4,
"volume":2193,
"ord":4
},
{
"price":427.45,
"volume":5406,
"ord":19
},
{
"price":427.5,
"volume":15311,
"ord":57
},
{
"price":427.55,
"volume":11170,
"ord":17
},
{
"price":427.6,
"volume":7272,
"ord":25
}
],
"o":430.5,
"h":433.65,
"l":423.6,
"c":425.2,
```

```
"chp":0.48,
"tick_Size":0.05,
"ch":2.05,
"ltq":20,
"ltt":1622184920,
"ltp":427.25,
"v":39163870,
"atp":428.07,
"lower_ckt":382.7,
"upper_ckt":467.7,
"expiry":"",
"oi":0,
"oiflag":false,
"pdoi":0,
"oipercent":0.0
}
},
"message":""
}
```

### Option Chain

The Optionchain API provides important information about options trading, specifically focusing on strike prices, which are predetermined prices at which an option contract can be exercised. This API offers data for both Call (CE) and Put (PE) options, along with values for index, IndiaVIX (Volatility Index) and available expiry dates. When using the API, you can specify the number of strike prices you're interested in. For example, if you request a strike count of 2, the API will return data for: **At-The-Money (ATM) strike:** The closest strike price to the current market price. **Out-of-The-Money (OTM) strikes:** Strike prices higher than the current market price for Calls (CE) and lower than the current market price for Puts (PE). The API will return data for 2 CE and 2 PE OTM strikes. **In-The-Money (ITM) strikes:** Strike prices lower than the current market price for Calls (CE) and higher than the current market price for Puts (PE). The API will return data for 2 CE and 2 PE ITM strikes. .

### Request attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol* | string | Mandatory. Eg: NSE:SBIN-EQ |
| strikecount | int | Options strike count for symbol(MAX = 50) |
| timestamp | string | Options chain data at timestamp |
| greeks | string | Set greeks to 1 for greeks data which includes delta, gamma, theta, vega and iv. |

### Response attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| s | string | ok / error |
| code | int | This is the code to identify specific responses |
| callOi | int | Total open interest for call options |
| putOi | int | Total open interest for put options |
| date | string | Expiry date in DD-MM-YYYY |
| expiry | string | Expiry timestamp |
| ask | float | Ask price |
| bid | float | Bid price |
| description | string | Description of the stock |
| ex_symbol | string | Exchange Symbol |
| **Attribute** | **Data Type** | **Description** |
| exchange | int | The exchange in which order is placed. View Details |
| fytoken | string | Fytoken is a unique identifier for every symbol. View Details |
| delta | float | Sensitivity of option price to a 1-unit change in underlying price |
| gamma | float | Rate of change of delta with respect to underlying price |
| theta | float | Time decay: change in option price per day as expiry approaches |
| vega | float | Sensitivity of option price to a 1% change in implied volatility |
| iv | float | Implied volatility: expected future volatility derived from option price |
| ltp | float | LTP is the price from which the next sale of the stocks happens |
| ltpch | float | Change in last traded price |
| ltpchp | float | Percentage change in last traded price |
| option_type | string | Type of option (if applicable) |
| strike_price | int | Strike price (if applicable) |
| symbol | string | Symbol |
| fp | float | Future price |
| fpch | float | Change in future price |
| fpchp | float | Percentage change in future price |
| oi | int | Open interest |
| oich | int | Change in Open interest |
| oichp | float | Percentage change in Open interest |
| prev_oi | int | Previous Open interest |
| volume | int | Volume traded |

**Request samples**

```bash
curl --location 'https://api-t1.fyers.in/data/options-chain-v3?symbol=NSE%3ANIFTY50-EQ&strikecount=1&greeks=1' \
--header 'Authorization: access token' \
```

**Sample Success Response**

```json
{
"code":200,
"data": {
"callOi":138681800,
"expiryData": [
{
"date":"24-03-2026",
"expiry":"1774346400",
"expiry_flag":"W"
},
{
"date":"30-03-2026",
"expiry":"1774864800",
"expiry_flag":"M"
},
{
"date":"07-04-2026",
"expiry":"1775556000",
"expiry_flag":"W"
},
{
"date":"13-04-2026",
"expiry":"1776074400",
"expiry_flag":"W"
},
{
"date":"21-04-2026",
"expiry":"1776765600",
"expiry_flag":"W"
},
{
"date":"28-04-2026",
"expiry":"1777370400",
"expiry_flag":"M"
},
{
"date":"26-05-2026",
"expiry":"1779789600",
"expiry_flag":"M"
},
{
"date":"30-06-2026",
"expiry":"1782813600",
"expiry_flag":"M"
},
{
"date":"29-09-2026",
"expiry":"1790676000",
"expiry_flag":"M"
},
{
"date":"29-12-2026",
"expiry":"1798538400",
"expiry_flag":"M"
},
{
"date":"29-06-2027",
"expiry":"1814263200",
"expiry_flag":"M"
},
{
"date":"28-12-2027",
"expiry":"1829988000",
"expiry_flag":"M"
},
```

```json
{
"date":"27-06-2028",
"expiry":"1845712800",
"expiry_flag":"M"
},
{
"date":"26-12-2028",
"expiry":"1861437600",
"expiry_flag":"M"
},
{
"date":"26-06-2029",
"expiry":"1877162400",
"expiry_flag":"M"
},
{
"date":"24-12-2029",
"expiry":"1892800800",
"expiry_flag":"M"
},
{
"date":"25-06-2030",
"expiry":"1908612000",
"expiry_flag":"M"
},
{
"date":"31-12-2030",
"expiry":"1924941600",
"expiry_flag":"M"
}
],
"indiavixData": {
"ask":0,
"bid":0,
"description":"INDIAVIX-INDEX",
"ex_symbol":"INDIAVIX",
"exchange":"NSE",
"fyToken":"101000000026017",
"ltp":22.81,
"ltpch":0.01,
"ltpchp":0.04,
"option_type":"",
"strike_price":-1,
"symbol":"NSE:INDIAVIX-INDEX"
},
"optionsChain": [
{
"ask":0,
"bid":0,
"description":"NIFTY50-INDEX",
"ex_symbol":"NIFTY",
"exchange":"NSE",
"fp":23146,
"fpch":91.2,
"fpchp":0.4,
"fyToken":"101000000026000",
"ltp":23114.5,
"ltpch":112.35,
"ltpchp":0.49,
"option_type":"",
"strike_price":-1,
"symbol":"NSE:NIFTY50-INDEX"
},
{
"ask":193.65,
"bid":193,
"fyToken":"101126032462574",
"ltp":192.8,
"ltpch":-80.25,
"ltpchp":-29.39,
"oi":1453010,
"oich":495430,
```

```
"oichp":51.74,
"option_type":"PE",
"prev_oi":957580,
"strike_price":23050,
"symbol":"NSE:NIFTY2632423050PE",
"volume":82921150,
"greeks": {
"delta":-0.44,
"gamma":0.0007,
"theta":-28.48,
"vega":9.51,
"iv":23.7
}
},
{
"ask":267.2,
"bid":266.15,
"fyToken":"101126032462572",
"ltp":266,
"ltpch":17.05,
"ltpchp":6.85,
"oi":726700,
"oich":3055,
"oichp":0.42,
"option_type":"CE",
"prev_oi":723645,
"strike_price":23050,
"symbol":"NSE:NIFTY2632423050CE",
"volume":15859935,
"greeks": {
"delta":0.56,
"gamma":0.0007,
"theta":-28.52,
"vega":9.51,
"iv":23.74
}
},
{
"ask":215,
"bid":214.45,
"fyToken":"101126032462577",
"ltp":214.5,
"ltpch":-82.85,
"ltpchp":-27.86,
"oi":3207750,
"oich":1437210,
"oichp":81.17,
"option_type":"PE",
"prev_oi":1770540,
"strike_price":23100,
"symbol":"NSE:NIFTY2632423100PE",
"volume":175818760,
"greeks": {
"delta":-0.48,
"gamma":0.0007,
"theta":-28.48,
"vega":9.59,
"iv":23.51
}
},
{
"ask":238.4,
"bid":237.5,
"fyToken":"101126032462575",
"ltp":237.35,
"ltpch":14.3,
"ltpchp":6.41,
"oi":2531555,
"oich":930995,
"oichp":58.17,
"option_type":"CE",
"prev_oi":1600560,
```

```
"strike_price":23100,
"symbol":"NSE:NIFTY2632423100CE",
"volume":75646025,
"greeks": {
"delta":0.52,
"gamma":0.0007,
"theta":-28.48,
"vega":9.59,
"iv":23.51
}
},
{
"ask":237.85,
"bid":236.9,
"fyToken":"101126032462579",
"ltp":237.1,
"ltpch":-89.6,
"ltpchp":-27.43,
"oi":1256255,
"oich":552825,
"oichp":78.59,
"option_type":"PE",
"prev_oi":703430,
"strike_price":23150,
"symbol":"NSE:NIFTY2632423150PE",
"volume":124837700,
"greeks": {
"delta":-0.51,
"gamma":0.0007,
"theta":-28.16,
"vega":9.6,
"iv":23.23
}
},
{
"ask":211.8,
"bid":210.85,
"fyToken":"101126032462578",
"ltp":211.8,
"ltpch":10.5,
"ltpchp":5.22,
"oi":1378910,
"oich":709735,
"oichp":106.06,
"option_type":"CE",
"prev_oi":669175,
"strike_price":23150,
"symbol":"NSE:NIFTY2632423150CE",
"volume":63103690,
"greeks": {
"delta":0.49,
"gamma":0.0007,
"theta":-28.39,
"vega":9.6,
"iv":23.42
}
}
],
"putOi":108234555
},
"message":"",
"s":"ok"
}
```

## Price Alerts

Price Alerts are user-configured triggers that notify when a stock or instrument reaches a specific price or meets certain market conditions. Once the alert is triggered, you can get the notification in the General Websocket.

### Create Price Alert

You can create a new price alert using this API. Alerts can be configured based on the following parameters.

### Comparison Type

| **Possible Values** | **Description** |
| --- | --- |
| LTP | LTP |
| HIGH | High Price |
| LOW | Low Price |
| OPEN | Open Price |
| CLOSE | Close Price |

### Condition

| **Possible Values** | **Description** |
| --- | --- |
| GT | Greater than (>) |
| GTE | Greater than equal to (>=) |
| LT | Less than |
| LTE | Less than equal to (<=) |
| E | Equal to |

### Alert Type

| **Possible Values** | **Description** |
| --- | --- |
| 1 | v / LTP |

### Request Attributes

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| agent string | Source of alert creation. Eg: "fyers-api" |
| alert-type int | Type of alert. 1 price-based alert. |
| name string | User-provided label for alert. |
| symbol string | Full trading symbol (e.g., "NSE:SBIN-EQ") |
| comparisonType string | price metric. Allowed: "OPEN", "HIGH", "LOW", "CLOSE", "LTP" |
| condition string | comparison operator. Allowed: "GT" (greater), "GTE" (greater or equal), "LT" (lesser), "LTE" (lesser or equal), "==" (equal) |
| value float | Target price for comparison. |

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X POST -d '{
"agent":"fyers-api",
"alert-type":1,
"name":"SBIN Alert",
"symbol":"NSE:SILVERMIC25DECFUT",
"comparisonType":"CLOSE",
"condition":"LT",
"value":45
}' https://api-t1.fyers.in/api/v3/price-alert
```

**Sample Success Response**

```json
{
"code":120,
```

"message":"A price alert for NSE:SILVERMIC25DECFUT at ₹45 is created.",

```
"s":"ok"
}
```

### Get Price Alerts

You can retrieve alerts using: Alert Name Alert Id This returns both active and triggered alerts.

### Response Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| fyToken | string | Fytoken is a unique identifier for every symbol. |
| alert | object | Detailed alert configuration. |
| symbol | string | Trading symbol for the alert. |

### alert Object Fields

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| comparisonType | string | metric compared (e.g., "OPEN", "CLOSE"). |
| condition | string | Comparison operator (GT, LT, EQ). |
| name | string | user label. |
| type | string | Alert type.(e.g,"V"= LTP) |
| value | float/int | Target value. |
| triggeredAt | string | Time of trigger (if any). |
| createdAt | string | creation timestamp. |
| modifiedAt | string | Last updated timestamp. |
| notes | string | Additional notes or description. |
| status | int | Alert status: 1 = Enabled, 0 = triggered, 2 = Disabled |
| triggeredEpoch | int | Trigger time (epoch) (0 = not triggered). |
| **Attribute** | **Data Type** | **Description** |
| createdEpoch | int | Created timestamp (epoch format) . |
| modifiedEpoch | int | Last modified timestamp in epoch format (0 = never modified). |

**Request samples**

```bash
curl -H "Authorization:app_id:access_token" https://api-t1.fyers.in/api/v3/price-alert
```

**Sample Success Response**

```json
{
"code":200,
"message":"",
"data": {
"3870982": {
"fyToken":"1120251216472793",
"alert": {
"comparisonType":"LOW",
"condition":"GT",
"name":"gold",
"type":"V",
"value":90,
"triggeredAt":"04-Dec-2025 12:20:03",
"createdAt":"04-Dec-2025 12:20:02",
"modifiedAt":"",
"notes":"",
"status":0,
"triggeredEpoch":1764850803,
"createdEpoch":1764850802,
"modifiedEpoch":0
},
"symbol":"MCX:CRUDEOIL25DEC5500PE"
}
},
"s":"ok"
}
```

### Modify Price Alert

Allows you to modify alerts. Only active alerts can be modified. Expired or triggered alerts cannot be modified. The symbol associated with an alert cannot be changed; all other fields can be updated.

### Request Attributes

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| alertId* string | Mandatory. Unique alert ID |
| agent string | Identifier of client (e.g., "fyers-api") |
| alert-type int | Mandatory. 1 → Price alert (LTP) |
| **Data** **Attribute** **Type** | **Description** |
| name string | Mandatory. Max 50 characters |
| symbol string | Mandatory. Trading symbol (e.g., NSE:GOLDBEES-EQ) |
| comparisonType string | Mandatory. comparision type Allowed: "OPEN", "HIGH", "LOW", "CLOSE", "LTP" |
| condition string | comparison operator. Allowed: "GT" (greater), "GTE" (greater or equal), "LT" (lesser), "LTE" (lesser or equal), "==" (equal) |
| value float | Mandatory. Up to 6 decimal places |

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X PUT -d '{
"alertId":"3870995",
"agent":"fyers-api",
"alert-type":1,
"name":"Updated Alert",
"symbol":"NSE:SILVERMIC25DECFUT",
"comparisonType":"CLOSE",
"condition":"LT",
"value":50
}' https://api-t1.fyers.in/api/v3/price-alert
```

**Sample Success Response**

```json
{
"code":123,
```

"message":"A price alert for NSE:SILVERMIC25DECFUT at ₹50 is updated.",

```
"s":"ok"
}
```

### Delete Price Alert

Delete a price alert.

### Request Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| alertId | string | Mandatory. Alert ID from creation |
| agent | string | Client calling the API (e.g., "fyers-api") |

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X DELETE -d '{
"alertId":"3870995",
"agent":"fyers-api"
}' https://api-t1.fyers.in/api/v3/price-alert
```

**Sample Success Response**

```json
{
"code":121,
```

"message":"A price alert for NSE:GOLDBEES-EQ at ₹185 is deleted.",

```
"s":"ok"
}
```

### Enable/Disable Price Alert

This API allows you to change the alert state between enabled and disabled. Only active alerts are allowed to change state; expired or triggered alert states cannot be changed.

### Request Attributes

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| alertId | string | Mandatory. Alert ID from creation |
| agent | string | Client calling the API (e.g., "fyers-api") |

**Request samples**

```bash
curl -H "Authorization:app_id:access_token"-H "Content-Type: application/json"-X PUT -d '{
"alertId":"3870995",
"agent":"fyers-api",
}' https://api-t1.fyers.in/api/v3/toggle-alert
```

**Sample Success Response**

```json
{
"code":123,
"message":"Your alert has been successfully enabled",
"s":"ok"
}
Sample Success Response for Disabled Alert
{
"code":123,
"message":"Your alert has been successfully disabled",
"s":"ok"
}
```

## Web Socket

### Introduction

The WebSocket provides a robust method for accessing real-time data or order updates seamlessly and with low latency. It enables developers and users to establish a persistent, bidirectional connection with the server, allowing them to receive continuous updates, such as symbol updates, depth updates or orderupdate. To enhance your experience with our WebSocket, here are some helpful tips and best practices 1. **Subscription Limit:** You have the flexibility to subscribe up to **5000** data subscriptions simultaneously via WebSocket with latest SDK versions, please refer Change Log. Staying within this limit ensures smooth subscription management without errors. 2. **Single Instance:** Keep in mind that you can create only one WebSocket connection instance at a time. This approach ensures stability and prevents issues that might arise from multiple concurrent connections. 3. **Efficient Thread Management:** WebSocket operates on a dedicated thread, allowing it to run independently of your main application thread. This design guarantees that your primary tasks can continue without interruptions from WebSocket operations. 4. **Customizable Callback Functions:** Tailor your application's behavior using callback functions provided by the WebSocket. These functions empower you to define specific actions for events like data updates or error occurrences. 5. **Auto-Reconnect:** Enjoy uninterrupted connectivity by enabling automatic reconnection in case of disconnection. Simply set the reconnect parameter to true during WebSocket initialization, ensuring your application can recover without manual intervention.You can set max reconnection count upto 50. 6. **Logging to File:** If you want to log data to a file, you can set the write_to_file parameter to true. This feature allows you to efficiently save received data to a log file for analysis or archival purposes. The write_to_file function will only work without callback functions. 7. **Reconnect Retry:** If you want to define dynamic retry count(max 50), you can set the reconnect_retry parameter to int value of number of times you want it to try reconnection.(In case of node fyersdata.autoreconnect(trycount)) 8. **Disable Logging(node JS):** In case you want to disable logging use disable logging flag to disable logging sample format:

```
new FyersSocket("token","logpath",true/*flag to enable disable logging*/)
```

**Request samples**

```python
from fyers_apiv3.FyersWebsocket import data_ws
fyers = data_ws.FyersDataSocket(
access_token=access_token,        # Access token in the format "appid:accesstoken"
log_path="",# Path to save logs.Leave empty to auto-create logs in the current directory.litemode=False,# Lite mode disabled.Set to True if you want a lite response.write_to_file=False,# Save response in a log file instead of printing it.reconnect=True,# Enable auto-reconnection to WebSocket on disconnection.on_connect=onopen,                # Callback function to subscribe to data upon connection.on_close=onclose,                 # Callback function to handle WebSocket connection close events.on_error=onerror,                 # Callback function to handle WebSocket errors.on_message=onmessage,             # Callback function to handle incoming messages from the WebSocket.reconnect_retry=10# Number of times reconnection will be attepmted in case
)
```

### General Socket (orders)

The WebSocket API for receiving order, position, trade, price alerts, and EDIS updates is a real-time communication protocol designed to provide seamless access to various critical elements of a trading and EDIS system. This API allows traders and developers to establish a persistent, bidirectional connection with the server, enabling them to receive real-time updates on their orders, current positions, executed trades, price alerts, and EDIS status.

### Response attributes - For order updates

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| id | string | The unique order id assigned for each order |
| exchOrdId | string | The order id provided by the exchange |
| symbol | string | The symbol for which order is placed |
| qty | int | The original order qty |
| remainingQuantity | int | The remaining qty |
| filledQty | int | The filled qty after partial trades |
| status | int | 1 => Canceled 2 => Traded / Filled 3 => (Not used currently) 4 => Transit 5 => Rejected 6 => Pending 7 => Expired View Details |
| message | string | The error messages are shown here |
| segment | int | 10 => E (Equity) 11 => D (F&O) 12 => C (Currency) 20 => M (Commodity) View Details |
| limitPrice | float | The limit price for the order |
| stopPrice | float | The limit price for the order |
| productType | string | The product type |
| type | int | 1 => Limit Order 2 => Market Order 3 => Stop Order (SL-M) 4 => Stoplimit Order (SL-L) |
| side | int | 1 => Buy -1 => Sell View Details |
| orderValidity | string | DAY IOC |
| orderDateTime | string | The order time as per DD-MMM-YYYY hh:mm:ss in IST |
| parentId | string | The parent order id will be provided only for applicable orders.. Eg: BO Leg 2 & 3 and CO Leg 2 |
| tradedPrice | float | The average traded price for the order |
| source | string | Source from where the order was placed. View Details |
| fytoken | string | Fytoken is a unique identifier for every symbol. View Details |
| offlineOrder | boolean | False => When market is open True => When placing AMO order |
| pan | string | PAN of the client |
| clientId | string | The client id of the fyers user |
| exchange | int | The exchange in which order is placed View Details |
| instrument | int | Exchange instrument type View Details |
| **Attribute** | **Data Type** | **Description** |
| id_fyers | string | Fyers system-generated unique identifier for the order. |

**Request samples**

```python
from fyers_apiv3.FyersWebsocket import order_ws
def onOrder( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("Order Response:", message)
def onerror( message):
"""
Callback function to handle WebSocket errors.Parameters:
message (dict): The error message received from the WebSocket.
"""
print("Error:", message)
def onclose( message):
"""
Callback function to handle WebSocket connection close events.
"""
print("Connection closed:", message)
def onopen():
"""
Callback function to subscribe to data type and symbols upon WebSocket connection.
"""
# Specify the data type and symbols you want to subscribe to
data_type ="OnOrders"
# data_type = "OnTrades"
# data_type = "OnPositions"
# data_type = "OnGeneral"
# data_type = "OnOrders,OnTrades,OnPositions,OnGeneral"
fyers.subscribe( data_type=data_type)
# Keep the socket running to receive real-time data
fyers.keep_running()
# Replace the sample access token with your actual access token obtained from Fyers
access_token ="AAAAAAAA-100:eyJ..."
# Create a FyersDataSocket instance with the provided parameters
fyers = order_ws.FyersOrderSocket(
access_token=access_token,   # Your access token for authenticating with the Fyers API.write_to_file=False,# A boolean flag indicating whether to write data to a log file or not.log_path="",# The path to the log file if write_to_file is set to True (empty string means current
directory).
on_connect=onopen,           # Callback function to be executed upon successful WebSocket connection.on_close=onclose,            # Callback function to be executed when the WebSocket connection is closed.on_error=onerror,            # Callback function to handle any WebSocket errors that may occur.on_orders=onOrder,           # Callback function to handle order-related events from the WebSocket.
)
# Establish a connection to the Fyers WebSocket
fyers.connect()
```

```json
{
"s": "ok",
"orders":{
"clientId": "FY****",
"id": "23080400089344",
"exchOrdId": "1100000009596016",
"qty":1 ,
"filledQty":1 ,
"limitPrice":7.95,
"type":1 ,
"fyToken": "101000000014366",
"exchange":10,
"segment":10,
"symbol": "NSE:IDEA-EQ",
"instrument":0 ,
"offlineOrder":false,
"orderDateTime": "04-Aug-2023 10:12:58",
"orderValidity": "DAY",
"productType": "INTRADAY",
"side":-1,
"status":90,
"source": "W",
"ex_sym": "IDEA",
"description": "VODAFONE IDEA LIMITED",
"orderNumStatus": "23080400089344:2",
"id_fyers": "1b30241e-2819-4ec9-a3e4-69b6155cacab"
}
}
```

### General Socket (trades)

### Response attributes - For trade update

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol | string | Eg: NSE:SBIN-EQ |
| id | string | The unique id to sort the trades |
| orderDateTime | string | The time when the trade occurred in “DD-MM-YYYY hh:mm:ss” format in IST |
| orderNumber | string | The order id for which the trade occurred |
| tradeNumber | string | The trade number generated by the exchange |
| tradePrice | float | The traded price |
| tradeValue | float | The total traded value |
| tradedQty | int | The total traded qty |
| side | int | 1 => Buy -1 => Sell View Details |
| productType | string | The product in which the order was placed View Details |
| exchangeOrderNo | string | The order number provided by the exchange |
| segment | int | The segment in which order is placed View Details |
| exchange | int | The exchange in which order is placed View Details |
| fyToken | string | Fytoken is a unique identifier for every symbol. |
| id_fyers | string | Fyers system-generated unique identifier for the order. |

**Request samples**

```python
from fyers_apiv3.FyersWebsocket import order_ws
def onTrade( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("Trade Response:", message)
def onerror( message):
"""
Callback function to handle WebSocket errors.Parameters:
message (dict): The error message received from the WebSocket.
"""
print("Error:", message)
def onclose( message):
"""
Callback function to handle WebSocket connection close events.
"""
print("Connection closed:", message)
def onopen():
"""
Callback function to subscribe to data type and symbols upon WebSocket connection.
"""
# Specify the data type and symbols you want to subscribe to
data_type ="OnTrades"
# data_type = "OnOrders"
# data_type = "OnPositions"
# data_type = "OnGeneral"
# data_type = "OnOrders,OnTrades,OnPositions,OnGeneral"
fyers.subscribe( data_type=data_type)
# Keep the socket running to receive real-time data
fyers.keep_running()
# Replace the sample access token with your actual access token obtained from Fyers
access_token ="AAAAAAAA-100:eyJ..."
# Create a FyersDataSocket instance with the provided parameters
fyers = order_ws.FyersOrderSocket(
access_token=access_token,   # Your access token for authenticating with the Fyers API.write_to_file=False,# A boolean flag indicating whether to write data to a log file or not.log_path="",# The path to the log file if write_to_file is set to True (empty string means current
directory).
on_connect=onopen,           # Callback function to be executed upon successful WebSocket connection.on_close=onclose,            # Callback function to be executed when the WebSocket connection is closed.on_error=onerror,            # Callback function to handle any WebSocket errors that may occur.on_trades=onTrade           # Callback function to handle trade-related events from the WebSocket.
)
# Establish a connection to the Fyers WebSocket
fyers.connect()
```

**Sample Success Response**

```json
{
"s": "ok",
"trades":{
"tradeNumber": "23080400089344-21726639",
"orderNumber": "23080400089344",
"tradedQty":1 ,
"tradePrice":7.95,
"tradeValue":7.95,
"productType": "INTRADAY",
"clientId": "FY****",
"exchangeOrderNo": "1100000009596016",
"orderType":2 ,
"side":-1,
"symbol": "NSE:IDEA-EQ",
"orderDateTime": "04-08-2023 10:12:58",
"fyToken": "101000000014366",
"exchange":10,
"segment":10,
"id_fyers": "1b30241e-2819-4ec9-a3e4-69b6155cacab"
}
}
```

### General Socket (positions)

### Response attributes - For position updates

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol | string | Eg: NSE:SBIN-EQ |
| id | string | The unique value for each position |
| buyAvg | float | Average buy price |
| buyQty | int | Total buy qty |
| sellAvg | float | Average sell price |
| sellQty | int | Total sell qty |
| netAvg | float | netAvg |
| netQty | int | Net qty |
| side | int | The side shows whether the position is long / short View Details |
| qty | int | Absolute value of net qty |
| productType | string | The product type of the position View Details |
| realized_profit | float | The realized p&l of the position |
| crossCurrency | string | Y => It is cross currency position N => It is not a cross currency position |
| rbiRefRate | float | Incase of cross currency position, the rbi reference rate will be required to calculate the p&l |
| qtyMulti_com | float | Incase of commodity positions, this multiplier is required for p&l calculation |
| segment | int | The segment in which the position is taken. View Details |
| exchange | int | The exchange in which the position is taken. View Details |
| **Attribute** | **Data Type** | **Description** |
| slNo | int | This is used for sorting of positions |
| fytoken | string | Fytoken is a unique identifier for every symbol. View Details |
| cfBuyQty | int | Carry forward buy quantity |
| cfSellQty | int | Carry forward sell quantity |
| dayBuyQty | int | Day forward buy quantity |
| daySellQty | int | Day forward sell quantity |
| exchange | int | The exchange in which order is placed View Details |
| buyVal | float | Total buy value of the position. |
| sellVal | float | Total sell value of the position. |

**Request samples**

```python
from fyers_apiv3.FyersWebsocket import order_ws
def onPosition( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("Position Response:", message)
def onerror( message):
"""
Callback function to handle WebSocket errors.Parameters:
message (dict): The error message received from the WebSocket.
"""
print("Error:", message)
def onclose( message):
"""
Callback function to handle WebSocket connection close events.
"""
print("Connection closed:", message)
def onopen():
"""
Callback function to subscribe to data type and symbols upon WebSocket connection.
"""
# Specify the data type and symbols you want to subscribe to
data_type ="OnPositions"
# data_type = "OnOrders"
# data_type = "OnTrades"
# data_type = "OnGeneral"
# data_type = "OnOrders,OnTrades,OnPositions,OnGeneral"
fyers.subscribe( data_type=data_type)
# Keep the socket running to receive real-time data
fyers.keep_running()
# Replace the sample access token with your actual access token obtained from Fyers
access_token ="AAAAAAAA-100:eyJ..."
# Create a FyersDataSocket instance with the provided parameters
fyers = order_ws.FyersOrderSocket(
access_token=access_token,   # Your access token for authenticating with the Fyers API.write_to_file=False,# A boolean flag indicating whether to write data to a log file or not.log_path="",# The path to the log file if write_to_file is set to True (empty string means current
directory).
on_connect=onopen,           # Callback function to be executed upon successful WebSocket connection.on_close=onclose,            # Callback function to be executed when the WebSocket connection is closed.on_error=onerror,            # Callback function to handle any WebSocket errors that may occur.on_positions=onPosition,     # Callback function to handle position-related events from the WebSocket.
)
# Establish a connection to the Fyers WebSocket
fyers.connect()
```

**Sample Success Response**

```json
{
"s": "ok",
"positions":{
"symbol": "NSE:IDEA-EQ",
"id": "NSE:IDEA-EQ-INTRADAY",
"buyAvg":8 ,
"buyQty":1 ,
"buyVal":8 ,
"sellAvg":7.95,
"sellQty":1 ,
"sellVal":7.95,
"netAvg":0 ,
"netQty":0 ,
"side":0 ,
"qty":0 ,
"productType": "INTRADAY",
"realized_profit":-0.04999999999999982,
"rbiRefRate":1 ,
"fyToken": "101000000014366",
"exchange":10,
"segment":10,
"dayBuyQty":1 ,
"daySellQty":1 ,
"cfBuyQty":0 ,
"cfSellQty":0 ,
"qtyMulti_com":1
}
}
```

### General Socket (general)

The WebSocket API for receiving order, position, trade, price alerts, and EDIS updates is a real-time communication protocol designed to provide seamless access to various critical elements of a trading and EDIS system. This API allows traders and developers to establish a persistent, bidirectional connection with the server, enabling them to receive real-time updates on their orders, current positions, executed trades, price alerts, and EDIS status.

**Request samples**

```python
from fyers_apiv3.FyersWebsocket import order_ws
def onTrade( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("Trade Response:", message)
def onOrder( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("Order Response:", message)
def onPosition( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("Position Response:", message)
def onGeneral( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("General Response:", message)
def onerror( message):
"""
Callback function to handle WebSocket errors.Parameters:
message (dict): The error message received from the WebSocket.
"""
print("Error:", message)
def onclose( message):
"""
Callback function to handle WebSocket connection close events.
"""
print("Connection closed:", message)
def onopen():
"""
Callback function to subscribe to data type and symbols upon WebSocket connection.
"""
# Specify the data type and symbols you want to subscribe to
# data_type = "OnOrders"
# data_type = "OnTrades"
# data_type = "OnPositions"
# data_type = "OnGeneral"
data_type ="OnOrders,OnTrades,OnPositions,OnGeneral"
```

```
fyers.subscribe( data_type=data_type)
# Keep the socket running to receive real-time data
fyers.keep_running()
# Replace the sample access token with your actual access token obtained from Fyers
access_token ="AAAAAAAA-100:YYYYYYYYYYYY"
# Create a FyersDataSocket instance with the provided parameters
fyers = order_ws.FyersOrderSocket(
access_token=access_token,   # Your access token for authenticating with the Fyers API.write_to_file=False,# A boolean flag indicating whether to write data to a log file or not.log_path="",# The path to the log file if write_to_file is set to True (empty string means current
directory).
on_connect=onopen,           # Callback function to be executed upon successful WebSocket connection.on_close=onclose,            # Callback function to be executed when the WebSocket connection is closed.on_error=onerror,            # Callback function to handle any WebSocket errors that may occur.on_general=onGeneral,        # Callback function to handle general events from the WebSocket.on_orders=onOrder,           # Callback function to handle order-related events from the WebSocket.on_positions=onPosition,     # Callback function to handle position-related events from the WebSocket.on_trades=onTrade           # Callback function to handle trade-related events from the WebSocket.
)
# Establish a connection to the Fyers WebSocket
fyers.connect()
```

**Sample Success Response**

```json
{
"s": "ok",
"orders":{
"clientId": "FY****",
"id": "23080400089344",
"exchOrdId": "1100000009596016",
"qty":1 ,
"filledQty":1 ,
"limitPrice":7.95,
"type":1 ,
"fyToken": "101000000014366",
"exchange":10,
"segment":10,
"symbol": "NSE:IDEA-EQ",
"instrument":0 ,
"offlineOrder":false,
"orderDateTime": "04-Aug-2023 10:12:58",
"orderValidity": "DAY",
"productType": "INTRADAY",
"side":-1,
"status":90,
"source": "W",
"ex_sym": "IDEA",
"description": "VODAFONE IDEA LIMITED",
"orderNumStatus": "23080400089344:2",
"id_fyers":"1b30241e-2819-4ec9-a3e4-69b6155cacab"
}
}
```

### Market Data Symbol Update

The WebSocket API for receiving stock data is a real-time communication protocol designed to provide seamless and low-latency access to live stock market data. This API allows developers and traders to establish a persistent, bidirectional connection with the server, enabling them to receive continuous updates on stock prices, trading volumes, and other relevant market information. To quickly get started with the WebSocket API and start receiving real-time stock data, you can explore our sample scripts and code examples in our GitHub repository: [Data WebSocket Sample Scripts](https://github.com/FyersDev/fyers-api-sample-code/tree/sample_v2/My%20API%20Sample%20Script(GET%20STARTED)/websocket%20sample%20script)

### Response Attributes(Market Data Update)

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| symbol string | The symbol in fyers symbology format whose data is |
| ltp float | Last traded price of security or asset. |
| prev_close_price float | Previous day's close of security or asset. |
| high_price float | Current day's high of security or asset. |
| low_price float | Current day's low of security or asset. |
| open_price float | Current day's open of security or asset. |
| ch float | Change in price of security or asset today. |
| chp float | Change in price in % of security or asset today. |
| vol_traded_today int | Volume traded for security or asset today. |
| last_traded_time int | Last traded time of security or asset. |
| bid_size int | The bid size key represents the quantity or volume of the security or asset that buyers are willing to purchase at a specific bid price level. |
| ask_size int | The ask size key represents the quantity or volume of the security or asset that sellers are willing to sell at a specific ask price level. |
| ask_price float | The ask price key represents the lowest price at which sellers are willing to sell a particular security or asset. |
| bid_price float | The bid price key represents the highest price at which buyers are willing to purchase a particular security or asset. |
| last_traded_qty int | Last traded quantity of security or asset. |
| tot_buy_qty int | Total buy quantity of security or asset. |
| tot_sell_qty int | Total sell quantity of security or asset. |
| avg_trade_price float | Average trade price of security or asset. |
| type string | cn - connection message sub - subscribe message if - index data message dp - market depth data message sf - Equity and option data message |

**Request samples**

```python
from fyers_apiv3.FyersWebsocket import data_ws
def onmessage( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("Response:", message)
def onerror( message):
"""
Callback function to handle WebSocket errors.Parameters:
message (dict): The error message received from the WebSocket.
"""
print("Error:", message)
def onclose( message):
"""
Callback function to handle WebSocket connection close events.
"""
print("Connection closed:", message)
def onopen():
"""
Callback function to subscribe to data type and symbols upon WebSocket connection.
"""
# Specify the data type and symbols you want to subscribe to
data_type ="SymbolUpdate"
# Subscribe to the specified symbols and data type
symbols =['NSE:SBIN-EQ','NSE:ADANIENT-EQ']
fyers.subscribe( symbols=symbols,  data_type=data_type)
# Keep the socket running to receive real-time data
fyers.keep_running()
# Replace the sample access token with your actual access token obtained from Fyers
access_token ="XC4XXXXXXM-100:eXXXXXXXXXXXXfZNSBoLo"
# Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
access_token=access_token,        # Access token in the format "appid:accesstoken"
log_path="",# Path to save logs.Leave empty to auto-create logs in the current directory.litemode=False,# Lite mode disabled.Set to True if you want a lite response.write_to_file=False,# Save response in a log file instead of printing it.reconnect=True,# Enable auto-reconnection to WebSocket on disconnection.on_connect=onopen,                # Callback function to subscribe to data upon connection.on_close=onclose,                 # Callback function to handle WebSocket connection close events.on_error=onerror,                 # Callback function to handle WebSocket errors.on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)
# Establish a connection to the Fyers WebSocket
fyers.connect()
```

```json
{
"ltp":606.4,
"vol_traded_today":3045212,
"last_traded_time":1690953622,
"exch_feed_time":1690953622,
"bid_size":2081,
"ask_size":903,
"bid_price":606.4,
"ask_price":606.45,
"last_traded_qty":5 ,
"tot_buy_qty":749960,
"tot_sell_qty":1092063,
"avg_trade_price":608.2,
"low_price":605.85,
"high_price":610.5,
"open_price":609.85,
"prev_close_price":620.2,
"type": "sf",
"symbol": "NSE:SBIN-EQ",
"ch":-13.8,
"chp":-2.23
}
```

### Market Data Indices Update

The WebSocket API for receiving stock data is a real-time communication protocol designed to provide seamless and low-latency access to live stock market data. This API allows developers and traders to establish a persistent, bidirectional connection with the server, enabling them to receive continuous updates on stock prices, trading volumes, and other relevant market information. To quickly get started with the WebSocket API and start receiving real-time stock data, you can explore our sample scripts and code examples in our GitHub repository: [Data WebSocket Sample Scripts](https://github.com/FyersDev/fyers-api-sample-code/tree/sample_v2/My%20API%20Sample%20Script(GET%20STARTED)/websocket%20sample%20script)

### Response Attributes(Index Update)

| **Attribute** | **Data Type** | **Description** |
| --- | --- | --- |
| symbol | string | The symbol in fyers symbology format whose data is |
| ltp | float | Last traded price of security or asset. |
| prev_close_price | float | Previous day's close of security or asset. |
| high_price | float | Current day's high of security or asset. |
| low_price | float | Current day's low of security or asset. |
| open_price | float | Current day's open of security or asset. |
| ch | float | Change in price of security or asset today. |
| chp | float | Change in price in % of security or asset today. |
| type | string | cn - connection message sub - subscribe message if - index data message dp - market depth data message sf - Equity and option data message |

**Request samples**

```python
from fyers_apiv3.FyersWebsocket import data_ws
def onmessage( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("Response:", message)
def onerror( message):
"""
Callback function to handle WebSocket errors.Parameters:
message (dict): The error message received from the WebSocket.
"""
print("Error:", message)
def onclose( message):
"""
Callback function to handle WebSocket connection close events.
"""
print("Connection closed:", message)
def onopen():
"""
Callback function to subscribe to data type and symbols upon WebSocket connection.
"""
# Specify the data type and symbols you want to subscribe to
data_type ="SymbolUpdate"
# Subscribe to the specified symbols and data type
symbols =["NSE:NIFTY50-INDEX","NSE:NIFTYBANK-INDEX"]
fyers.subscribe( symbols=symbols,  data_type=data_type)
# Keep the socket running to receive real-time data
fyers.keep_running()
# Replace the sample access token with your actual access token obtained from Fyers
access_token ="XC4XXXXXXM-100:eXXXXXXXXXXXXfZNSBoLo"
# Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
access_token=access_token,        # Access token in the format "appid:accesstoken"
log_path="",# Path to save logs.Leave empty to auto-create logs in the current directory.litemode=False,# Lite mode disabled.Set to True if you want a lite response.write_to_file=False,# Save response in a log file instead of printing it.reconnect=True,# Enable auto-reconnection to WebSocket on disconnection.on_connect=onopen,                # Callback function to subscribe to data upon connection.on_close=onclose,                 # Callback function to handle WebSocket connection close events.on_error=onerror,                 # Callback function to handle WebSocket errors.on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)
# Establish a connection to the Fyers WebSocket
fyers.connect()
```

```json
{
"symbol": "NSE:NIFTY50-INDEX",
"ch": "-27.95",
"high_price": "26277.35",
"ltp": "26188.1",
"exch_feed_time": "1727428424",
"chp": "-0.11",
"low_price": "26166.95",
"open_price": "26248.25",
"type": "if",
"prev_close_price": "26216.05"
}
```

### Market Data Depth Update

The WebSocket API for receiving stock data is a real-time communication protocol designed to provide seamless and low-latency access to live stock market data. This API allows developers and traders to establish a persistent, bidirectional connection with the server, enabling them to receive continuous updates on stock prices, trading volumes, and other relevant market information. To quickly get started with the WebSocket API and start receiving real-time stock data, you can explore our sample scripts and code examples in our GitHub repository: [Data WebSocket Sample Scripts](https://github.com/FyersDev/fyers-api-sample-code/tree/sample_v2/My%20API%20Sample%20Script(GET%20STARTED)/websocket%20sample%20script)

### Response Attributes(Depth Update)

**Data**

| **Attribute** | **Description** |
| --- | --- |
| **Type** |  |
| symbol string | The symbol in fyers symbology format whose data is received on socket. |
| bid_price1-bid_price5 float | The bid price key represents the highest price at which buyers are willing to purchase a particular security or asset. |
| ask_price1-ask_price5 float | The ask price key represents the lowest price at which sellers are willing to sell a particular security or asset. |
| bid_size1-bid_size5 integer | The bid size key represents the quantity or volume of the security or asset that buyers are willing to purchase at a specific bid price level. |
| ask_size1-ask_size5 integer | The ask size key represents the quantity or volume of the security or asset that sellers are willing to sell at a specific ask price level. |
| bid_order1-bid_order5 integer | The number of bid order. |
| ask_order1-ask_order5 integer | The number of ask order. |
| type string | cn - connection message sub - subscribe message if - index data message dp - market depth data message sf - Equity and option data message |

**Request samples**

```python
from fyers_apiv3.FyersWebsocket import data_ws
def onmessage( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("Response:", message)
def onerror( message):
"""
Callback function to handle WebSocket errors.Parameters:
message (dict): The error message received from the WebSocket.
"""
print("Error:", message)
def onclose( message):
"""
Callback function to handle WebSocket connection close events.
"""
print("Connection closed:", message)
def onopen():
"""
Callback function to subscribe to data type and symbols upon WebSocket connection.
"""
# Specify the data type and symbols you want to subscribe to
data_type ="DepthUpdate"
# Subscribe to the specified symbols and data type
symbols =['NSE:SBIN-EQ','NSE:ADANIENT-EQ']
fyers.subscribe( symbols=symbols,  data_type=data_type)
# Keep the socket running to receive real-time data
fyers.keep_running()
# Replace the sample access token with your actual access token obtained from Fyers
access_token ="XXDHHIOKS-100:eajoljXXXXXXXXXX"
# Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
access_token=access_token,        # Access token in the format "appid:accesstoken"
log_path="",# Path to save logs.Leave empty to auto-create logs in the current directory.litemode=False,# Lite mode disabled.Set to True if you want a lite response.write_to_file=False,# Save response in a log file instead of printing it.reconnect=True,# Enable auto-reconnection to WebSocket on disconnection.on_connect=onopen,                # Callback function to subscribe to data upon connection.on_close=onclose,                 # Callback function to handle WebSocket connection close events.on_error=onerror,                 # Callback function to handle WebSocket errors.on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)
# Establish a connection to the Fyers WebSocket
fyers.connect()
```

```json
{
"bid_price1":606.25,
"bid_price2":606.2,
"bid_price3":606.15,
"bid_price4":606.1,
"bid_price5":606.05,
"ask_price1":606.3,
"ask_price2":606.35,
"ask_price3":606.4,
"ask_price4":606.45,
"ask_price5":606.5,
"bid_size1":20,
"bid_size2":902,
"bid_size3":111,
"bid_size4":110,
"bid_size5":979,
"ask_size1":282,
"ask_size2":568,
"ask_size3":2910,
"ask_size4":1676,
"ask_size5":2981,
"bid_order1":1 ,
"bid_order2":3 ,
"bid_order3":2 ,
"bid_order4":2 ,
"bid_order5":9 ,
"ask_order1":4 ,
"ask_order2":2 ,
"ask_order3":12,
"ask_order4":9 ,
"ask_order5":17,
"type": "dp",
"symbol": "NSE:SBIN-EQ"
}
```

### Market Data Lite-Mode

The WebSocket API provides a lightweight and efficient "Lite Mode" for receiving only the Last Traded Price (LTP) updates of specific stock symbols. This mode is designed for users who require real-time access to LTP data without the additional overhead of subscribing to other stock data fields. The Lite Mode allows for seamless integration into applications where only the latest stock prices are needed.

**Request samples**

```python
from fyers_apiv3.FyersWebsocket import data_ws
def onmessage( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("Response:", message)
def onerror( message):
"""
Callback function to handle WebSocket errors.Parameters:
message (dict): The error message received from the WebSocket.
"""
print("Error:", message)
def onclose( message):
"""
Callback function to handle WebSocket connection close events.
"""
print("Connection closed:", message)
def onopen():
"""
Callback function to subscribe to data type and symbols upon WebSocket connection.
"""
# Specify the data type and symbols you want to subscribe to
data_type ="SymbolUpdate"
# Subscribe to the specified symbols and data type
symbols =['NSE:SBIN-EQ','NSE:ADANIENT-EQ']
fyers.subscribe( symbols=symbols,  data_type=data_type)
# Keep the socket running to receive real-time data
fyers.keep_running()
# Replace the sample access token with your actual access token obtained from Fyers
access_token ="XC4XXXXXXM-100:eXXXXXXXXXXXXfZNSBoLo"
# Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
access_token=access_token,        # Access token in the format "appid:accesstoken"
log_path="",# Path to save logs.Leave empty to auto-create logs in the current directory.litemode=True,# Lite mode disabled.Set to True if you want a lite response.write_to_file=False,# Save response in a log file instead of printing it.reconnect=True,# Enable auto-reconnection to WebSocket on disconnection.on_connect=onopen,                # Callback function to subscribe to data upon connection.on_close=onclose,                 # Callback function to handle WebSocket connection close events.on_error=onerror,                 # Callback function to handle WebSocket errors.on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)
# Establish a connection to the Fyers WebSocket
fyers.connect()
```

```json
{
symbol:  'NSE:SBIN-EQ',
ltp:  500.55,
type:'sf'
}
```

### Market Data Unsubscribe

To stop receiving real-time data updates for a specific stock symbol or a group of symbols, you can utilize the "unsubscribe" action in the WebSocket API. Sending an "unsubscribe" message will remove the specified symbol(s) from your active subscriptions, and you will no longer receive updates for those symbols. You can check the sample code to know how to unsubscribe to already subscribed symbols.

**Request samples**

```python
from fyers_apiv3.FyersWebsocket import data_ws
def onmessage( message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
message (dict): The received message from the WebSocket.
"""
print("Response:", message)
# After processing or when you decide to unsubscribe for specific symbol and data_type
# you can use the fyers.unsubscribe() method
# Example of condition: Unsubscribe when a certain condition is met
if message['symbol']=='NSE:SBIN-EQ'and message['ltp']>610:
# Unsubscribe from the specified symbols and data type
data_type ="SymbolUpdate"
symbols_to_unsubscribe =['NSE:SBIN-EQ']
fyers.unsubscribe( symbols=symbols_to_unsubscribe,  data_type=data_type)
def onerror( message):
"""
Callback function to handle WebSocket errors.Parameters:
message (dict): The error message received from the WebSocket.
"""
print("Error:", message)
def onclose( message):
"""
Callback function to handle WebSocket connection close events.
"""
print("Connection closed:", message)
def onopen():
"""
Callback function to subscribe to data type and symbols upon WebSocket connection.
"""
# Specify the data type and symbols you want to subscribe to
data_type ="SymbolUpdate"
# Subscribe to the specified symbols and data type
symbols =['NSE:SBIN-EQ','NSE:ADANIENT-EQ']
fyers.subscribe( symbols=symbols,  data_type=data_type)
# Keep the socket running to receive real-time data
fyers.keep_running()
# Replace the sample access token with your actual access token obtained from Fyers
access_token ="XXDHHIOKS-100:eajoljXXXXXXXXXX"
# Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
access_token=access_token,        # Access token in the format "appid:accesstoken"
log_path="",# Path to save logs.Leave empty to auto-create logs in the current directory.litemode=False,# Lite mode disabled.Set to True if you want a lite response.write_to_file=False,# Save response in a log file instead of printing it.reconnect=True,# Enable auto-reconnection to WebSocket on disconnection.on_connect=onopen,                # Callback function to subscribe to data upon connection.on_close=onclose,                 # Callback function to handle WebSocket connection close events.on_error=onerror,                 # Callback function to handle WebSocket errors.on_message=onmessage             # Callback function to handle incoming messages from the WebSocket.
)
```

```
# Establish a connection to the Fyers WebSocket
fyers.connect()
```

**Sample Success Response**

```json
{'type':'unsub','code':200,'message':'Unsubscribed','s':'ok'}
```

### Advanced Configuration

The WebSocket queue processing interval is an **Optional** setting that allows you to customize how frequently data in the subscription queue is handled. By default, this interval is set to 1 millisecond, but it can be adjusted to better suit your application's specific needs and performance preferences. 1. **Customizable Interval:** You can set the processing interval anywhere between 1ms to 2000ms (2 seconds), giving you flexibility to optimize performance and responsiveness. 2. **Dynamic Adjustment:** The interval setting can be changed at any time during an active WebSocket session. 3. **Performance Optimization:** Shorter intervals (1-10ms) are ideal for high-frequency trading scenarios that benefit from rapid data processing, while slightly longer intervals (100-500ms) work well for general market data streaming. 4. **Resource Management:** You can tune the interval based on how your application handles incoming data, helping to maintain smooth operation across different environments.

**Request samples**

```javascript
const FyersSocket = require("fyers-api-v3").fyersDataSocket
var fyersdata=new FyersSocket("xxxxx-1xx:ey....", "logpath",true/*flag to enable disable logging*/)
fyersdata.setQueueProcessInterval(200)// 200ms - more reasonable interval for queue processing
fyersdata.connect()
```

## Order Websocket Usage Guide

### Introduction

The WebSocket API for receiving order, position, trade, price alerts, and EDIS updates is a real-time communication protocol designed to provide seamless access to various critical elements of a trading and EDIS system. This API allows traders and developers to establish a persistent, bidirectional connection with the server, enabling them to receive real-time updates on their orders, current positions, executed trades, price alerts, and EDIS status. This guide provides instructions on integrating the order WebSocket into any programming language.

### Order WebSocket Connection

To connect to order websocket, the below two input params are mandate 1. Websocket endpoint : wss://socket.fyers.in/trade/v3 2. Header: Format: **< appId:accessToken >** Sample header format : 7ABXUX38S-100:eyJ0eXAi**********qiTnzd2lGwS17s Based on the programming language chosen, respective socket connection libraries can be used. For the reference please find the sample code for socket connection written in Python. Here, we are making a connection with Fyers order websocket with parameters and callback functions on_message, on_error, on_close, on_open, which are required in the Python socket connection library used and would change as per the other programming library used. Sample callback function is shared below. Note : Handle accordingly in your Programming language **Connection Response:** **On Success:** Returns the socket object **On Failure:** Possible Error : Status code 403 1. Error: Handshake status 403 Forbidden -+-+- {'date': 'Tue, 19 Dec 2023 04:46:45 GMT', 'content-length': '0', 'connection': 'keep-alive', 'cf-cache-status': 'DYNAMIC', 'set-cookie': '__cf_bm=BOE16LGB7NHpNqW0AJOuFN1rcL3Q9TgnhmtpBfb3.Wk-1702961205-1- AfmECmK9cbVA2XGvkpx+jFuXyRsJET/ZOQYmw3LyZJ68pYLZTgtpbalvNs09ECZZ4GpPiogeYGhhFo+3PCp20nE=; path=/; expires=Tue, 19-Dec-23 05:16:45 GMT; domain=.fyers.in; HttpOnly; Secure', 'server': 'cloudflare', 'cf-ray': '837d00eec8ed17b6-MAA'} -+-+- b'' **Reason** : This error will come when your accessToken is wrong **How to solve** : Provide correct accessToken AccessToken format: **< appID:accesstoken >** 2. Error: Handshake status 404 Not Found -+-+- {'date': 'Tue, 19 Dec 2023 10:04:35 GMT', 'content-type': 'text/plain; charset=utf-8', 'content-length': '0', 'connection': 'keep-alive', 'cf-cache-status': 'DYNAMIC', 'set-cookie': '__cf_bm=I5oN6zdeKjfGsicqFiXZ57J5SX2IjsFDspaLIEGKPDE-1702980275-1- Ae+ldjrb3WfSuM7yNOzo3ykOIBQ1m+50QqcIqU26A+wqPIHhIEIGSy9kT2OG3OWNI0hwcmh7U+PnJ/aWWhz6fOA=; path=/; expires=Tue, 19-Dec-23 10:34:35 GMT; domain=.fyers.in; HttpOnly; Secure', 'server': 'cloudflare', 'cf-ray': '837ed28169c817ae-MAA'} -+-+- b'' **Reason** : Socket Connection URL would be wrong **How to solve** : Provide valid URL. **Sample callback function:** For more reference, please find our on_open callback function code for more reference

**Request samples**

```python
try:
if self.__ws_object isNone:
if self.write_to_file:
self.background_flag =True
header ={"authorization": self.__access_token}
ws = websocket.WebSocketApp(
self.__url,
header=header,
on_message=lambda ws,  ms:g  sel.f __on_message( msg),
on_error=lambda ws,  ms:g  sel.f On_error( msg),
on_close=lambda ws,  close_cod,e  close_reaso:n  sel.f __on_close(
ws,  close_code,  close_reason
),
on_open=lambda ws:  sel.f __on_open( ws),
)
self.t = Thread( target=ws.run_forever)
self. . t daemon = self.background_flag
self. . t start()
#Sample callback function:
def __on_open( self,  ws):
try:
if self.__ws_object isNone:
self.__ws_object = ws
self.ping_thread = threading.Thread( target=self.__ping)
self.ping_thread.start()
except Exception as e:
self.order_logger.error e( )
self.On_error( ) e
```

### Subscribe Method

Once the connection is established, it is required to subscribe for required actions to get the data. To subscribe for different actions, create a message data, which would be the string format for json node.

```
message = json.dumps  ( {"T":"SUB_ORD","SLIST": action_data,  "SUB_T":1} )
```

**Json node Params:** **T**: Type: String value: “SUB_ORD” (Fixed) **action_data**: Type: List/Array Value: ['orders', 'trades', 'positions', 'edis', 'pricealerts', 'login'] Note: Based on the list passed in action_data web_socket data will be received **SUB_T**: Integer Value: 1 (value 1 is for subscribing and -1 for unsubscribe) Convert the json to string and send this message to socket to subscribe for action_data mentioned **Sample Response:**

```json
{'code':1605,'message':'Successfully subscribed','s':'ok'}
```

**Response from socket on any action triggered** Once the subscribed successfully, for any action triggered, data will be received through socket, if any callback function is defined, would receive on function. Response would be string, In node we get as array buffer and in python we string, then it parsed to required format. In another programming language you might get in another format you just have to change in string. **Type:** string **Value:** {"orders":{"client_id":"XP0001","exchange":10,"fy_token":"10100000001628","id":"23121800292158","id_fyers":"df013f50-6925-4e2d-ba0f- 0becf1229298","instrument":0,"lot_size":1,"offline_flag":false,"oms_flag":"K:1","ord_source":"W","ord_status":20,"ord_type":2,"ordertag":"2:Untagged","org_ord_stat Ack","segment":10,"status_msg":"New Ack","symbol":"NSE:BECTORFOOD-EQ","symbol_desc":"MRS BECTORS FOOD SPE LTD","symbol_exch":"BECTORFOOD", "tick_size":0.05,"time_epoch_oms":1702887690,"time_exch":"NA","time_oms":"18-Dec-2023 13:51:30","tran_side":1,"update_time_epoch_oms":1702887690,"update_time_exch":"01-Jan-1970 05:30:00","validity":"DAY"},"s":"ok"} Note: 1. Above response would be in the string format (In Python ) and arraybuffer (In Node). You have to check in which format you are getting data from websocket as it is dependent on the websocket library for the particular language. 2. Once you get data, you have to change into the string.(if already in string format then no need to change). After that, you have to change this string to JSON. Here you find the following keys as a JSON Key (One of them ) : orders, trades, positions. 3. Now Based on the Key the data is identified, if key is orders it means it is order update message, if key is trades then this message is for trades updates and same for positions updates. 4. In an Fyers SDK the socket raw response is parsed to generate data with required keys and remove the unnecessary keys **Parsed Data:** {'s': 'ok', 'orders': {'clientId': 'XP03754', 'id': '23121800388066', 'qty': 1, 'remainingQuantity': 1, 'type': 2, 'fyToken': '10100000002705', 'exchange': 10, 'segment': 10, 'symbol': 'NSE:PRAJIND-EQ', 'instrument': 0, 'offlineOrder': False, 'orderDateTime': '18-Dec-2023 16:33:24', 'orderValidity': 'DAY', 'productType': 'CNC', 'side': 1, 'status': 4, 'source': 'W', 'ex_sym': 'PRAJIND', 'description': 'PRAJ INDUSTRIES LTD', 'orderNumStatus': '23121800388066:4'}} All the keys information for orders updates are available there : Link All the keys information for Trades updates are available there : Link All the keys information for positions updates are available there : Link 5. Also attaching our internal mapping for your reference, how we are changing the keys from raw data to final data.

```
"position_mapper" :
{
"symbol": "symbol",
"id": "id",
"buy_avg": "buyAvg",
"buy_qty": "buyQty",
"buy_val": "buyVal",
"sell_avg": "sellAvg",
"sell_qty": "sellQty",
"sell_val": "sellVal",
"net_avg": "netAvg",
"net_qty": "netQty",
"tran_side": "side",
"qty": "qty",
"product_type": "productType",
"pl_realized": "realized_profit",
"rbirefrate": "rbiRefRate",
"fy_token": "fyToken",
"exchange": "exchange",
"segment": "segment",
"day_buy_qty": "dayBuyQty",
"day_sell_qty": "daySellQty",
"cf_buy_qty": "cfBuyQty",
"cf_sell_qty": "cfSellQty",
"qty_multiplier": "qtyMulti_com",
"pl_total": "pl",
"cross_curr_flag": "crossCurrency",
"pl_unrealized": "unrealized_profit"
},
"order_mapper" :
{
"client_id":"clientId",
"id":"id",
"id_parent":"parentId",
"id_exchange":"exchOrdId",
"qty":"qty",
"qty_remaining":"remainingQuantity",
"qty_filled":"filledQty",
"price_limit":"limitPrice",
"price_stop":"stopPrice",
"tradedPrice":"price_traded",
"ord_type":"type",
"fy_token":"fyToken",
"exchange":"exchange",
"segment":"segment",
"symbol":"symbol",
"instrument":"instrument",
"oms_msg":"message",
"offline_flag":"offlineOrder",
"time_oms":"orderDateTime",
"validity":"orderValidity",
"product_type":"productType",
"tran_side":"side",
"org_ord_status":"status",
"ord_source":"source",
"symbol_exch":"ex_sym",
"symbol_desc":"description"
},
"trade_mapper" :
{
"id_fill": "tradeNumber",
"id": "orderNumber",
"qty_traded": "tradedQty",
"price_traded": "tradePrice",
"traded_val": "tradeValue",
"product_type": "productType",
"client_id": "clientId",
"id_exchange": "exchangeOrderNo",
"ord_type": "orderType",
"tran_side": "side",
"symbol": "symbol",
"fill_time": "orderDateTime",
"fy_token": "fyToken",
"exchange": "exchange",
"segment": "segment"
}
```

**Request samples**

```python
def subscribe( sel,f  data_type:  str)->None:
"""
Subscribes to real-time updates of a specific data type.Args:
data_type (str): The type of data to subscribe to, such as orders, position, or holdings.
"""
try:
if self.__ws_object isnotNone:
self.data_type =[]
for elem in data_type.split(","):
ifisinstance(self.socket_type[ elem],list):
self.data_type.exten(d sel.f socket_type[ elem])
else:
self.data_type.appen(d sel.f socket_type[ elem])
print("Data type is ", self.data_type)
print("Data type is ",type(self.data_type))
message = json.dumps(
{"T":"SUB_ORD","SLIST": self.data_type,  "SUB_T":1}
)
self.__ws_object.send( message)
except Exception as e:
self.order_logger.error( ) e
```

### UnSubscribe Method

To Unsubscribe for different actions, create a message data, which would be the string format for json node.

```
message = json.dumps  ( {"T":"SUB_ORD","SLIST": action_data,  "SUB_T":-1} )
```

**Json node Params:** **T**: Type: String value: “SUB_ORD” (Fixed) **action_data**: Type: List/Array Value: ['orders', 'trades', 'positions', 'edis', 'pricealerts', 'login'] Note: Based on the list passed in action_data web_socket data will be received **SUB_T**: Integer Value: -1 (value -1 is for unsubscribing and 1 for subscribe) Convert the json to string and send this message to socket to subscribe for action_data mentioned

**Request samples**

```python
def unsubscribe( self,  data_type:  str)->None:
"""
Unsubscribes from real-time updates of a specific data type.Args:
data_type (str): The type of data to unsubscribe from, such as orders, position, holdings or general.
"""
try:
if self.__ws_object isnotNone:
self.data_type =[
self.socket_type[(type)]fortypein data_type.split(",")
]
message = json.dumps(
{"T":"SUB_ORD","SLIST": self.data_type,  "SUB_T":-1}
)
self.__ws_object.send( message)
except Exception as e:
self.order_logger.error e( )
```

### Ping Method

To check whether the websocket connection is alive or not, we have to send a periodically “ping” message. If we get a pong from websocket, it means it is alive else dead. Find how we are doing in Python Code. Here there is one while loop with sleep of 10 seconds and we send a “ping” message to websocket to know that websocket is alive or not.

**Request samples**

```python
def __ping( self)  ->None:
"""
Sends periodic ping messages to the server to maintain the WebSocket connection.The method continuously sends "__ping" messages to the server at a regular interval
as long as the WebSocket connection is active.
"""
while(
self.__ws_object isnotNone
and self.__ws_object.sock
and self.__ws_objec.t soc.k connected
):
self.__ws_object.send("ping")
time.sleep(10)
```

### Mandatory fields

| **Method** | **Fields** | **Reason** |
| --- | --- | --- |
| WebSocket Connection | WebSocket Connection URL(Endpoint) | To make a connection |
| WebSocket Connection | Headers | To authorize |
| **Method** | **Fields** | **Reason** |
| Subscribe Method | action_data | To subscribe for particular actions |
| Subscribe Method | "SUB_T": 1 | While subscribing to any action |
| UnSubscribe Method | "SUB_T": -1 | While unsubscribing any action |

## Tick-by-Tick (TBT) Websocket Usage Guide

### Introduction

Tick-by-tick data is the most detailed market data, recording every trade and order book update in real-time. Each "tick" includes the price, volume, and timestamp of individual trades, as well as changes to buy and sell orders. This granular data is crucial for analyzing market microstructure, tracking order flow, and developing high-frequency trading strategies.

****Key Points:****

1. **Available for NFO and NSE Instruments Only** Tick-by-tick data is exclusively available only for **NFO (NSE Futures & Options) and NSE (Equity) instruments.** 2. **Data Formats** **Requests** are sent in **JSON** format. **Responses** are received in **protobuf** format (a compact, efficient data format). 3. **Incremental Data Updates** Instead of sending the full market data repeatedly, the server only sends **changes (differences)** between the last data packet and the current one. To get the complete picture, users must maintain previous data and **apply these changes.** The official SDKs provided by **Fyers** will handle this process automatically. 4. **Snapshot Data on New Subscriptions** When a user **subscribes to tick-by-tick data**, the first packet received is a **snapshot**, containing the full market data at that moment. After this, all subsequent packets only contain **updates (differences)** that need to be applied to the snapshot for a real-time view.

### TBT WebSocket Connection [50 Market Depth]

Currently, these are the features available on the socket

| **Feature** | **Description** | **Status** |
| --- | --- | --- |
| TBT 50 Market Depth | TBT 50 Market Depth provides users wtih 50 levels of market depth. [Learn more](https://fyers.in/community/blogs-gdppin8d/post/introducing-50-market-depth-a-game-changer-for-scalpers-and-active-traders-QBRCbSQrTGtQqFB) | Available |

To connect to tbt websocket, the below input params are mandated [1. Websocket endpoint : ](javascript:void(0))[wss://rtsocket-api.fyers.in/versova](javascript:void(0)) 2. Header: Key: Authorization Format: **< appId:accessToken >** Sample header format : 7ABXUX38S-100:eyJ0eXAi**********qiTnzd2lGwS17s

**Request samples**

```python
from fyers_apiv3.FyersWebsocket.tbt_ws import FyersTbtSocket,  SubscriptionModes
def onopen():
"""
Callback function to subscribe to data type and symbols upon WebSocket connection.
"""
print("Connection opened")
# Specify the data type and symbols you want to subscribe to
mode = SubscriptionModes.DEPTH
Channel ='1'
# Subscribe to the specified symbols and data type
symbols =['NSE:NIFTY25MARFUT','NSE:BANKNIFTY25MARFUT']
fyers.subscribe( symbol_tickers=symbols,  channelNo=Channel,  mode=mode)
fyers.switchChannel( resume_channels=[Channel], pause_channels=[])
# Keep the socket running to receive real-time data
fyers.keep_running()
def on_depth_update( ticker,  message):
"""
Callback function to handle incoming messages from the FyersDataSocket WebSocket.Parameters:
ticker (str): The ticker symbol of the received message.message (Depth): The received message from the WebSocket.
"""
print("ticker", ticker)
print("depth response:", message)
print("total buy qty:", message.tbq)
print("total sell qty:", message.tsq)
print("bids:", message.bidprice)
print("asks:", message.askprice)
print("bidqty:", message.bidqty)
print("askqty:", message.askqty)
print("bids ord numbers:", message.bidordn)
print("asks ord numbers:", message.askordn)
print("issnapshot:", message.snapshot)
print("tick timestamp:", message.timestamp)
def onerror( message):
"""
Callback function to handle WebSocket errors.Parameters:
message (dict): The error message received from the WebSocket.
"""
print("Error:", message)
def onclose( message):
"""
Callback function to handle WebSocket connection close events.
"""
print("Connection closed:", message)
def onerror_message( message):
"""
Callback function for error message events from the server
Parameters:
message (dict): The error message received from the Server.
"""
print("Error Message:", message)
# Replace the sample access token with your actual access token obtained from Fyers
access_token ="XCXXXXXXM-100:eyJ0tHfZNSBoLo"
```

```
fyers = FyersTbtSocket(
access_token=access_token,   # Your access token for authenticating with the Fyers API.write_to_file=False,# A boolean flag indicating whether to write data to a log file or not.log_path="",# The path to the log file if write_to_file is set to True (empty string means current
directory).
on_open=onopen,           # Callback function to be executed upon successful WebSocket connection.on_close=onclose,            # Callback function to be executed when the WebSocket connection is closed.on_error=onerror,            # Callback function to handle any WebSocket errors that may occur.on_depth_update=on_depth_update,  # Callback function to handle depth-related events from the WebSocket
on_error_message=onerror_message         # Callback function to handle server-related erros from the WebSocket.
)
# Establish a connection to the Fyers WebSocket
fyers.connect()
```

### Concept of channels

With the Tick-by-Tick (TBT) WebSocket, we are introducing the concept of channels. A channel acts as a logical grouping for different subscribed symbols, making it easier to manage data streams efficiently.

### **How Channels Work**

When subscribing to market data, you need to specify both the symbols and a channel number. Simply subscribing to a channel does not start the data stream—you must also resume the channel to begin receiving updates.

### **Example Usage**

Let’s say you organize your subscriptions as follows: Channel 1: All Nifty-related symbols Channel 2: All BankNifty-related symbols Now, depending on what data you need, you can control the channels dynamically: To receive only Nifty data → Pause Channel 2 and Resume Channel 1 To receive only BankNifty data → Pause Channel 1 and Resume Channel 2 To receive both Nifty and BankNifty data → Resume both channels This approach provides greater flexibility and control over market data streaming, allowing you to filter and manage real-time data efficiently.

### Request Message Types

**Encoding**

| **Type** | **Purpose** | **Data Format** |
| --- | --- | --- |
|  | **Format** |  |

```
"ping"
```

Ping message to keep connection PingString alive

```json
{
"type": 1,
"data": {
"subs": 1,
"symbols": ["NSE:IOC25FEBFUT",
"NSE:NIFTY25FEBFUT",
```

Subscribe to the symbols for which

```
"NSE:BANKNIFTY25FEBFUT",
```

SubscribeJson string data is required"NSE:FINNIFTY25FEBFUT", "NSE:TCS25FEBFUT"],

```
"mode": "depth",
"channel": "1"
}
}
```

```json
{
"type": 1,
"data": {
"subs": -1,
"symbols": ["NSE:IOC25FEBFUT",
"NSE:NIFTY25FEBFUT",
```

Unsubscribe to the symbols for which

```
"NSE:BANKNIFTY25FEBFUT",
```

UnsubscribeJson string

```
"NSE:FINNIFTY25FEBFUT", "NSE:TCS25FEBFUT"],
```

data is NOT required

```
"mode": "depth",
"channel": "1"
}
}
{
"type": 2,
"data": {
"resumeChannels": ["1"],
```

SwitchSwitch between active and paused Json string "pauseChannels": [] Channelchannels

```
}
}
```

### Response Message Types

We use Protocol Buffers (protobuf) as the response format for all market data. The .proto file, which defines the data structure, is available at: 📌 Proto URL: [https://public.fyers.in/tbtproto/1.0.0/msg.proto](https://public.fyers.in/tbtproto/1.0.0/msg.proto) Protobuf is a widely used data format, and compilers are available to generate code in different programming languages. How to Install and Use Protobuf [Protobuf Compiler Installation: ](https://protobuf.dev/getting-started/)[https://protobuf.dev/getting-started/](https://protobuf.dev/getting-started/) Using Protobuf with Python: [https://protobuf.dev/reference/python/python-generated/](https://protobuf.dev/reference/python/python-generated/) Using Protobuf with Node.js: [https://www.npmjs.com/package/protobufjs](https://www.npmjs.com/package/protobufjs) We have uploaded the compiled files also for python, nodejs, and golang. You can download the files from the below link: [https://public.fyers.in/tbtproto/1.0.0/protogencode.zip](https://public.fyers.in/tbtproto/1.0.0/protogencode.zip) Copy the required file directly in your project and use it.

****Proto Versions and Links:****

| **Proto Version** | **Proto URL** | **Compiled files URL** | **Updated on** |
| --- | --- | --- | --- |
| 1.0.0 | [https://public.fyers.in/tbtproto/1.0.0/msg.proto](https://public.fyers.in/tbtproto/1.0.0/msg.proto) | [https://public.fyers.in/tbtproto/1.0.0/protogencode.zip](https://public.fyers.in/tbtproto/1.0.0/protogencode.zip) | 20-02-2025 |
| **Type** | **Data Format** | **Field Explanation** |  |
|  | type: value will always be MessageType.depth |  |  |

```
message SocketMessage {
```

feeds: string (key) will be the symbol ticker and value will be the

```
MessageType type = 1;
```

MarketFeed datastructure. This value will have the actual 50 depth

```
map<string, MarketFeed> feeds =
2;
```

values

```
bool snapshot = 3;
```

SocketMessage snapshot: true if its a snapshot and false if its a diff packet

```
string msg = 4;
```

msg: will mostly contain error msgs when error = true bool error = 5;

```
}
```

error: true if it is an error, else false. In case of true, feeds will be nil/empty

```
message MarketFeed {
Quote quote = 1;
ExtendedQuote eq = 2;
```

depth: Depth datastructure. This field will have the actual market

```
DailyQuote dq = 3;
OHLCV ohlcv = 4;
```

depth value

```
Depth depth = 5;
```

feed_time: time of the packet in unix epoch

```
google.protobuf.UInt64Value
feed_time = 6;
```

send_time: time of the packet at the time of sending from server

```
google.protobuf.UInt64Value
```

MarketFeed token: fytoken for the symbol

```
send_time = 7;
```

snapshot: true if its a snapshot else false for a diff packet string token = 8;

```
uint64 sequence_no = 9;
```

ticker: symbol ticker

```
bool snapshot = 10;
string ticker = 11;
```

**Note: **other fields can be ignored

```
SymDetail symdetail = 12;
}
message Depth {
google.protobuf.UInt64Value tbq =
```

tbq: total bid qty

```
1;
google.protobuf.UInt64Value tsq =
```

tsq: total sell qty

```
2;
```

Depth asks: array of asks of type Marketlevel datastructure

```
repeated MarketLevel asks = 3;
repeated MarketLevel bids = 4;
```

bids: array of bids of type Marketlevel datastructure

```
}
message MarketLevel {
google.protobuf.Int64Value price =
```

price: price1;

```
google.protobuf.UInt32Value qty  =
```

qty: qty in the market depth for the price

```
2;
```

nord: number of orders in the market depth for the price google.protobuf.UInt32Value nord = MarketLevel

```
3;
```

num: depth number, for 50 depth will be between 0 and 49 [0 based

```
google.protobuf.UInt32Value num =
```

array indexing]4;

```
}
```

### Ratelimits

Following ratelimits apply for TBT Websocket:

| **Description** | **Limit** |
| --- | --- |
| Active Connections Per App Per User | 3 |
| Symbols per connection [Market Depth] | 5 |
| Channels per connection | 50 (1-50) |

## Appendix

### Fytoken

| **Indicator** | **Format** | **Description** |
| --- | --- | --- |
| Exchange | 2 Digits | Exchange of the symbol |
| Segment | 2 Digits | Segment of the symbol |
| Expiry | 6 Digits | Format: YYMMDD Eg: 200827 |
| Exchange Token` | From 2 upto 6 Digits | The token assigned for the symbol by the exchange Eg:22 |

### Exchanges

| **Possible Values** | **Description** |
| --- | --- |
| 10 | NSE (National Stock Exchange) |
| 11 | MCX (Multi Commodity Exchange) |
| 12 | BSE (Bombay Stock Exchange) |

### Segments

| **Possible Values** | **Description** |
| --- | --- |
| 10 | Capital Market |
| 11 | Equity Derivatives |
| 12 | Currency Derivatives |
| 20 | Commodity Derivatives |

### Available Exchange-Segment Combinations

| **Exchange** | **Segment** | **Exchange Code** | **Segment Code** |
| --- | --- | --- | --- |
| NSE | Capital Market | 10 | 10 |
| NSE | Equity Derivatives | 10 | 11 |
| NSE | Currency Derivatives | 10 | 12 |
| NSE | Commodity Derivatives | 10 | 20 |
| BSE | Capital Market | 12 | 10 |
| BSE | Equity Derivatives | 12 | 11 |
| BSE | Currency Derivatives | 12 | 12 |
| **Exchange** | **Segment** | **Exchange Code** | **Segment Code** |
| MCX | Commodity Derivatives | 11 | 20 |

### Instrument Types

| **Possible Values** | **Description** |
| --- | --- |
| . | **CM segment** |
| 0 | EQ (EQUITY) |
| 1 | PREFSHARES |
| 2 | DEBENTURES |
| 3 | WARRANTS |
| 4 | MISC (NSE, BSE) |
| 5 | SGB |
| 6 | G - Secs |
| 7 | T - Bills |
| 8 | MF |
| 9 | ETF |
| 10 | INDEX |
| 50 | MISC (BSE) |
| . | **FO segment** |
| 11 | FUTIDX |
| 12 | FUTIVX |
| 13 | FUTSTK |
| 14 | OPTIDX |
| 15 | OPTSTK |
| . | **CD segment** |
| 16 | FUTCUR |
| 17 | FUTIRT |
| 18 | FUTIRC |
| 19 | OPTCUR |
| 20 | UNDCUR |
| 21 | UNDIRC |
| 22 | UNDIRT |
| 23 | UNDIRD |
| 24 | INDEX_CD |
| 25 | FUTIRD |
| . | **COM segment** |
| 11 | FUTIDX |
| 30 | FUTCOM |
| 31 | OPTFUT |
| 32 | OPTCOM |
| 33 | FUTBAS |
| **Possible Values** | **Description** |
| 34 | FUTBLN |
| 35 | FUTENR |
| 36 | OPTBLN |
| 37 | OPTFUT (NCOM) |

### Symbology Format

| **Segment** | **Format** | **Examples** |
| --- | --- | --- |
| Equity | {Ex}:{Ex_Symbol}-{Series} | NSE:SBIN-EQ, NSE:ACC-EQ, NSE:MODIRUBBER-BE BSE:SBIN-A, BSE:ACC-A, BSE:MODIRUBBER-T |
| Equity Futures | {Ex}:{Ex_UnderlyingSymbol}{YY}{MMM}FUT | NSE:NIFTY20OCTFUT, NSE:BANKNIFTY20NOVFUT, BSE:SENSEX23AUGFUT |
| Equity Options (Monthly Expiry) | {Ex}:{Ex_UnderlyingSymbol}{YY}{MMM}{Strike}{Opt_Type} | NSE:NIFTY20OCT11000CE, NSE:BANKNIFTY20NOV25000PE , BSE:SENSEX23AUG60400CE |
| Equity Options (Weekly Expiry) | {Ex}:{Ex_UnderlyingSymbol}{YY}{M}{dd}{Strike}{Opt_Type} refer here for possible values of {M} | NSE:NIFTY2010811000CE, NSE:NIFTY20O0811000CE, BSE:SENSEX2381161000CE, NSE:NIFTY20D1025000CE |
| Currency Futures | {Ex}:{Ex_CurrencyPair}{YY}{MMM}FUT | NSE:USDINR20OCTFUT, NSE:GBPINR20NOVFUT |
| Currency Options (Monthly Expiry) | Ex}:{Ex_CurrencyPair}{YY}{MMM}{Strike}{Opt_Type} | NSE:USDINR20OCT75CE, NSE:GBPINR20NOV80.5PE |
| Currency Options (Weekly Expiry) | {Ex}:{Ex_CurrencyPair}{YY}{M}{dd}{Strike}{Opt_Type} | NSE:USDINR20O0875CE, NSE:GBPINR20N0580.5PE NSE:USDINR20D1075CE |
| Commodity Futures | {Ex}:{Ex_Commodity}{YY}{MMM}FUT | MCX:CRUDEOIL20OCTFUT, MCX:GOLD20DECFUT |
| Commodity Options (Monthly Expiry) | {Ex}:{Ex_Commodity}{YY}{MMM}{Strike}{Opt_Type} | MCX:CRUDEOIL20OCT4000CE, MCX:GOLD20DEC40000PE |

### Symbology Possible Values

| **Variable** | **Explanation** | **Possible Values** |
| --- | --- | --- |
| {Ex} | This is the exchange on which the symbol is trading | NSE, BSE, MCX |
| {YY} | This is the last 2 digits of the year | 2019 will be 19 2020 will be 2020 2021 will be 21 2022 will be 22 |
| **Variable** | **Explanation** | **Possible Values** |
| {MMM} | For monthly expiries such as futures and options, this value is the 3 characters of the month. The month will always be denoted in uppercase. | JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC |
| {M} | For weekly expiries, this value represents the month of expiry but with only 1 character. This is a mix of numbers as well as characters. | Jan => 1 Feb => 2 Mar => 3 Apr => 4 May => 5 Jun => 6 Jul => 7 Aug => 8 Sep => 9 Oct => O (Letter) Nov => N Dec => D |
| {dd} | This is used in weekly expiries. This represents the date of the month on which the contract is going to expire. This value will always be 2 characters. | 01 06 10 25 30 |
| {Opt_Type} | This represents whether the contract is call or put | Call Option => CE, Put Option => PE |
| {Strike} | This is the strike price of the option contract | 11000 75.5 |

### Product Types.

| **Possible Values** | **Description** |
| --- | --- |
| CNC | For equity only |
| INTRADAY | Applicable for all segments |
| MARGIN | Applicable only for derivatives |
| CO | Cover Order |
| BO | Bracket Order |
| MTF | Margin Trading Facility |

### Order Types.

| **Possible Values** | **Description** |
| --- | --- |
| 1 | Limit order |
| 2 | Market order |
| **Possible Values** | **Description** |
| 3 | Stop order (SL-M) |
| 4 | Stoplimit order (SL-L) |

### Order Status

| **Possible Values** | **Description** |
| --- | --- |
| 1 | Cancelled |
| 2 | Traded / Filled |
| 3 | For future use |
| 4 | Transit |
| 5 | Rejected |
| 6 | Pending |

### Order Sides

| **Possible Values** | **Description** |
| --- | --- |
| 1 | Buy |
| -1 | Sell |

### Position Sides

| **Possible Values** | **Description** |
| --- | --- |
| 1 | Long |
| -1 | Short |
| 0 | Closed position |

### Holding Types

| **Possible Values** | **Description** |
| --- | --- |
| T1 | The shares are purchased but not yet delivered to the demat account. |
| HLD | The shares are purchased and are available in the demat account. |

### Order Sources

| **Possible Values** | **Description** |
| --- | --- |
| M | Mobile |
| W | Web |
| R | Fyers One |
| A | Admin |
| ITS | API |

## Change Log

| **Date** | **Changes** |
| --- | --- |
|  | Added APIv3 support for Charges, Tax Profit & Loss, Ledger and Realised Profit & Loss history under Reports API. **Version**: |

```
Python : fyers-apiv3 - v3.1.13
Node : fyers-api-v3 - v1.9.0
05 JUN 2026
Web Js : fyers-web-sdk-v3 - v1.8.0
Java : fyers-api-v3 - v1.8.0
Go : fyers-api-v3 - v1.3.0
C : fyers-api-v3 - v1.3.0
```

20 APR 2026Added Support for Smart Orders in APIv3. Added Greeks param for sdk under option chain. **Version**:

```
Python : fyers-apiv3 - v3.1.12
Node : fyers-api-v3 - v1.8.0
Web Js : fyers-web-sdk-v3 - v1.7.0
13 APR 2026
Java : fyers-api-v3 - v1.7.0
Go : fyers-api-v3 - v1.2.0
C : fyers-api-v3 - v1.2.0
C# : fyers-api-v3 - v1.1.2
```

10 APR 2026Added Order Tagging support for GTT Orders 09 APR 2026Added APIv3 support for Greeks under option chain Documented **async order placement** endpoints: /api/v3/orders/async and /api/v3/multi-order/async (queued execution, 10 OPS dispatch, immediate response returns id_fyers only; outcomes via order WebSocket and GET APIs).

```
31 MAR 2026
```

/sync order APIs remain as documented. See **Async Order Placement**. Added support for Week and Month resolution in History API.

```
27 MAR 2026
```

09 MAR 2026Added regulatory changes in documentation for APIv3. Added APIv3 support for Order History and Trade History. **Version**:

```
Python : fyers-apiv3 - v3.1.11
Node : fyers-api-v3 - v1.7.0
04 MAR 2026
Web Js : fyers-web-sdk-v3 - v1.6.0
Java : fyers-api-v3 - v1.6.0
Go : fyers-api-v3 - v1.1.0
C : fyers-api-v3 - v1.1.0
```

| **Date** | **Changes** |
| --- | --- |
|  | Added APIv3 support for C. |

```
28 FEB 2026C : fyers-api-v3 - v1.0.0
```

Added Price Alerts feature. 21 JAN 2026**Version**:

```
All
```

Added the order slicing feature for single-order placements.

```
04 DEC 2025
```

Added id_fyers key in the OrderBook response.

```
17 NOV 2025
```

Masked PII (Personally Identifiable Information) in Profile API response. 09 Sep 2025Fields masked: Mobile number, Email ID, PAN number. Fixed missing symbol key in market data indices update. Updated WebSocket reconnection logic. Fixed rate limiting issue caused by internet connectivity checks.

```
22 Aug 2025
```

**Version**:

```
Java : fyers-api-v3 - v1.3.0
```

Added support for NSE equity segment on TBT (Tick by tick) Socket. **Click here for reference**

```
23 Jun 2025
```

Added optional support for customizing WebSocket queue processing interval **Version**:

```
09 Jun 2025
Node Js : fyers-web-sdk-v3 - v1.4.2
```

Added support for logout API in Web Js SDK and Java SDK **Version**:

```
16 Apr 2025Web Js : fyers-web-sdk-v3 - v1.3.1
Java : fyers-apiv3 - v1.2.0
```

Added support for TBT 50 depth in Node SDK Added support for logout API in node SDK 26 Mar 2025**Version**:

```
Node : fyers-api-v3 - v1.4.1
```

20 Mar 2025Updated Instrument Types **Version**:

```
Python : fyers-apiv3 - v3.1.7
```

Added support for TBT 50 depth in python SDK

```
04 Mar 2025
```

Added **sample code** for TBT 50 depth Added support for logout API in python SDK 20 Feb 2025**TBT 50 depth** websocket documentation 13 Feb 2025Added keys for DDPI and MTF Activation Status in Profile API [Introduced Logout API ](https://myapi.fyers.in/docsV3#tag/User/paths/~1User/patch)**[click here](https://myapi.fyers.in/docsV3#tag/User/paths/~1User/patch)** **Version**:

```
Node : fyers-api-v3 - v1.4.0
Web Js : fyers-web-sdk-v3 - v1.3.0
05 Feb 2025
CDN :fyers-web-sdk-v3 - v1.3.0
Java : fyers-apiv3 - v1.1.0
```

Added MTF and GTT Order Placement **Version**:

```
C# : fyers-apiv3 - v1.0.6
01 Feb 2025
```

Added MTF and GTT Order Placement

| **Date** | **Changes** |
| --- | --- |
|  | **Version**: |

```
Python : fyers-apiv3 - v3.1.5
30 Jan 2025
```

Added MTF and GTT Order Placement 20 Jan 2025Introduced MTF and GTT Order Placement APIs **Version**:

```
C# : fyers-api-v3 - v1.0.5
13 Jan 2025
Java : fyers-apiv3 - v1.0.2
```

Added key for DisclosedQty in modify order **Version**:

```
Node : fyers-api-v3 - v1.3.3
Web Js : fyers-web-sdk-v3 - v1.2.4
27 Dec 2024CDN :fyers-web-sdk-v3 - v1.2.1
```

Improved compatibility with symbols containing special characters **Version**:

```
C# : fyers-api-v3 - v1.0.4
26 Dec 2024
Java : fyers-apiv3 - v1.0.1
```

Fixed Data Socket Issue for Sensex Symbol **Version**:

```
Python : fyers-apiv3 - v3.1.4
10 Oct 2024
```

Minor bug fixes within websocket package **Version**:

```
C# : fyers-api-v3 - v1.0.3
09 Oct 2024
```

Added Multileg order feature **Version**:

```
Java : fyers-api-v3 - v1.0.0
03 Oct 2024
```

Introduced API V3 Java SDK **Version**:

```
C# : fyers-api-v3 - v1.0.2
17 Sep 2024
```

Added Option Chain API **Version**: All Increased API rate limit from 10,000 requests per day to 1 Lakh requests per day (10x increase from the previous daily rate [limit), ](https://myapi.fyers.in/docsV3#tag/Request-and-Response-Structure/paths/~1pet~1%7BpetId%7D/post)**[click here](https://myapi.fyers.in/docsV3#tag/Request-and-Response-Structure/paths/~1pet~1%7BpetId%7D/post)**[ to view the current rate limits.](https://myapi.fyers.in/docsV3#tag/Request-and-Response-Structure/paths/~1pet~1%7BpetId%7D/post)

```
22 Aug 2024
```

**Note:** There are no change in per-second and per-minute rate limits Updated API document with API Error Codes **[refer here](https://myapi.fyers.in/docsV3#tag/Request-and-Response-Structure/paths/~1pet~1%7BpetId%7D/patch)** **Version**:

```
Python : fyers-apiv3 - v3.1.2
03 Jul 2024Node : fyers-api-v3 - v1.3.0
```

Added Multileg order feature **Version**:

```
C# : fyers-api-v3 - v1.0.1
12 Jun 2024
```

Optimized package with bug fixes **Version**:

```
Web Js : fyers-web-sdk-v3 - v1.2.2
07 Jun 2024
```

Optimized package **Version**: `All

```
30 May 2024
```

Added description for fyers 201 code(order placement)

| **Date** | **Changes** |
| --- | --- |
|  | **Version**: |

```
Python : fyers-apiv3 - v3.1.0
29 May 2024
```

Improvised logging **Version**:

```
Web Js : fyers-web-sdk-v3 - v1.2.1
14 May 2024
```

Improvised in internal package import logic **Version**:

```
C# : fyers-api-v3 - v1.0.0
25 Apr 2024
```

Introduced API V3 C# SDK **Version**:

```
Python : fyers-apiv3 - v3.1.0
Node : fyers-api-v3 - v1.2.0
Web Js : fyers-web-sdk-v3 - v1.2.0
23 Apr 2024
CDN :fyers-web-sdk-v3 - v1.2.0
```

Added option chain API **Version**: All

```
22 Mar 2024
```

Added 2 new reserved columns in Symbol Master CSV files, will be used for future development, kindly ignore **Version**: All

```
04 Apr 2024
```

Deprecated **cmd**[ attribute in Quotes API response ](https://fyers.in/notice-board/action-required-cmd-field-in-api-to-be-deprecated.html)**[click here](https://fyers.in/notice-board/action-required-cmd-field-in-api-to-be-deprecated.html)**[ for more details](https://fyers.in/notice-board/action-required-cmd-field-in-api-to-be-deprecated.html) **Version**:

```
Python : fyers-apiv3 - v3.1.0
Node : fyers-api-v3 - v1.1.1
Web Js : fyers-web-sdk-v3 - v1.1.0
CDN :fyers-web-sdk-v3 - v1.1.0
26 Mar 2024
```

**Symbol Subscription Enhancement** Optimised symbol subscription Increased symbol subscription limit from **200** to **5000** in a single connection **Version**: All

```
22 Mar 2024
```

Added 2 new reserved columns in Symbol Master CSV files, will be used for future development, kindly ignore **Version**: fyers-web-sdk-v3 - v1.0.0

```
15 Mar 2024
```

Introduced Browser Compatible SDK. **Version**: Python SDK - v3.0.9 **Logging Enhancement** In the FyersModel class, the log_level parameter has been introduced to control the verbosity of logging. By default, the logging level is set to 'ERROR',only errors will be logged. However, users have the flexibility to set the log_level parameter 14 Mar 2024to 'DEBUG', allowing for more detailed logging. Logs are written **fyersApi.log** file. Added **fyersRequest.log** file where requested endpoints and status code are logged (can be used to analyse the API requests made). **Compatible with Python v3.12** Updated aiohttp to version 3.9.3 (latest release) to ensure compatibility with Python 3.12. **Version**: All

```
13 Mar 2024
```

Added support for seconds candles

| **Date** | **Changes** |
| --- | --- |
|  | Version: All **Order Placement** OrderTagging functionality added. **Orderbook** Orderbook returns Ordertag in response |

```
05 Dec 2023
```

Query orderbook by Ordertag **Tradebook** Orderbook returns Ordertag in response Query tradebook by Ordertag **Version**: API Version 3 **New Features and Updates** **Performance** Fast Order Placement: Achieving placement within < 75 ms Fast get APIs: Achieving response times within < 75 ms **New Data Socket:** Improved tick update speed, ensuring swift and efficient market data updates. Introducing Lite mode for targeted last traded price (LTP) change updates. SymbolUpdate: Real-time symbol-specific updates for instant parameter changes. DepthUpdate: Real-time market depth changes for selected symbols. Increased subscription capacity, accommodating tracking of 200 symbols. Strengthened error handling callbacks for seamless issue resolution. **New Order Socket** 18 Aug 2023Real-time updates for orders Real-time updates for positions Real-time updates for trades Real-time updates for eDIS Real-time updates for price alerts Improved error handling callbacks **URL update for various APIs** Enhanced History API available at: **[https://api-t1.fyers.in/data/history](https://api-t1.fyers.in/data/history)** New Market Status API introduced at: **[https://api-t1.fyers.in/data/marketStatus](https://api-t1.fyers.in/data/marketStatus)** Enhanced Quotes API available at: **[https://api-t1.fyers.in/data/quotes](https://api-t1.fyers.in/data/quotes)** [Enhanced Market Depth API available at: ](https://api-t1.fyers.in/data/depth)**[https://api-t1.fyers.in/data/depth](https://api-t1.fyers.in/data/depth)** **Documentation and Sample Code Updates** Added sample code for NodeJS and Python in the documentation Updated sample code in the GitHub repository for both Python and NodeJS **Version**: All **Quotes** URL updated to **https://api-t1.fyers.in/data/quotes?symbols=NSE:SBIN-EQ** ip updated to lp Removed fyToken & prev_close_price from response

```
04 May 2023
```

Text updation: "Symbols" changed to "symbol" **Market Depth** URL updated to **https://api-t1.fyers.in/data/depth?symbol=NSE:SBIN-EQ&ohlcv_flag=1** itt updated to ltt Removed tick_Size & oi from response

| **Date** | **Changes** |
| --- | --- |
|  | **Version**: API Version 2 |
| - | **App Related** Introduced common apps for third party app developers Different authentication methods such as OAuth2, PKCE and OIDC Permission templates at the time of app creation **Authentication** Authentication flow has been changed to improve security Authorization header value has been changed **Order placement** Multi order placement Multi order modification Multi order cancellation **Other** Market status API **Realtime Data Rest API** Quotes api to get realtime data for list of symbols via Rest API Market Depth API to get bid ask data for a particular symbol **Websocket** Get realtime price info for a list of symbols Get realtime market depth for a particular symbol Get realtime order updates Background and Foreground process enabled for websocket. User can subscribe to only Index symbols Added sample scripts to get started with websocket Object initialization method changed a bit (instead of fyers_api.websocket it is fyers_api.Websocket) No More Pong received message on the console. The data will be continuous **Postback (Webhooks)** Get realtime order updates via postbacks / webhooks **Transactions** eDIS flow |