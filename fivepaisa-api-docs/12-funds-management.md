# Funds Management System

Fund balance / margin and multi-order margin.

## Contents

- [Margin](#margin)
- [Multi Order Margin](#multi-order-margin)

---

## Margin

> Source: https://xstream.5paisa.com/dev-docs/funds-management-system/margin

**Type:** Rest API · **Method:** POST

The API provides details of the fund balance in the IIFL Securities trading account.

This API provides comprehensive details regarding the available funds in a user's 5paisa Securities trading account. It is essential for understanding the real-time financial standing of an account, including the available trading margin, utilized funds, and fund composition.

It requires client code, API credentials and a valid session token for a successful request and provides details and bifurcation of the funds into various categories like EquityMargin , MFMargin , NetAvailableMargin, MarginUtilized, Cash, Collateral etc.

### REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V4/Margin
```

### Request headers

| KEY | VALUE |
|---|---|
| Content-Type | application/json |
| Authorization | bearer {Your Access Token} |

### Request body

| FIELD NAME |  | MANDATORY | DESCRIPTION |
|---|---|---|---|
| head | key<br>STRING | Yes | AppKey of User or Partner |
| body | ClientCode<br>STRING | Yes | 5paisa demat account client code of the user in plain text. |

### SAMPLE REQUEST BODY

**JSON**

```json
{
    "head": {
        "key": "{Your App Key}"
    },
    "body": {
        "ClientCode": "{User Client code}"
    }
}
```

**cURL**

```bash
curl --location 'https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V4/Margin' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {access_token}' \
--data '{
    "head": {
        "key": "{key}"
    },
    "body": {
        "ClientCode": "{client_code}"
    }
}

'
```

**Python**

```python
from py5paisa import FivePaisaClient
cred={
    "APP_NAME":"YOUR APP_NAME",
    "APP_SOURCE":"YOUR APP_SOURCE",
    "USER_ID":"YOUR USER_ID",
    "PASSWORD":"YOUR PASSWORD",
    "USER_KEY":"YOUR USERKEY",
    "ENCRYPTION_KEY":"YOUR ENCRYPTION_KEY"
    }

#This function will automatically take care of generating and sending access token for all your API's

client = FivePaisaClient(cred=cred)

# New TOTP based authentication
client.get_totp_session('Your ClientCode','TOTP from authenticator app','Your Pin')

client.margin()
```

**JAVA**

```java
Unirest.setTimeouts(0, 0);
HttpResponse<String> response = Unirest.post("https://dataservice.iifl.in/openapi/prod/Margin")
  .header("Ocp-Apim-Subscription-Key", "fc714d8e5b82438a93a95baa493ff45b")
  .header("Cookie", "IIFLMarcookie=as5to0ztyemldw4sjbdxxb5y")
  .header("Content-Type", "application/json")
  .body("{\r\n    \"head\": {\r\n        \"appName\": \"OPEN_API_APP_NAME\",\r\n        \"appVer\": \"VERSION_NUMBER\",\r\n        \"key\": \"OPEN_API_USER_KEY\",\r\n        \"osName\": \"OS_NAME\",\r\n        \"requestCode\": \"IIFLMarRQMarginV3\",\r\n        \"userId\": \"OPEN_API_USER_ID\",\r\n        \"password\": \"OPEN_API_USER_PASSWORD\"\r\n    },\r\n    \"body\": {\r\n        \"ClientCode\": \"DEMAT_ACCOUNT_CLIENT_CODE\"\r\n    }\r\n}")
  .asString();
```

**C#**

```csharp
var client = new RestClient("https://dataservice.iifl.in/openapi/prod/Margin");
client.Timeout = -1;
var request = new RestRequest(Method.POST);
request.AddHeader("Ocp-Apim-Subscription-Key", "fc714d8e5b82438a93a95baa493ff45b");
request.AddHeader("Cookie", "IIFLMarcookie=as5to0ztyemldw4sjbdxxb5y");
request.AddHeader("Content-Type", "application/json");
var body = @"{
" + "\n" +
@"    ""head"": {
" + "\n" +
@"        ""appName"": ""OPEN_API_APP_NAME"",
" + "\n" +
@"        ""appVer"": ""VERSION_NUMBER"",
" + "\n" +
@"        ""key"": ""OPEN_API_USER_KEY"",
" + "\n" +
@"        ""osName"": ""OS_NAME"",
" + "\n" +
@"        ""requestCode"": ""IIFLMarRQMarginV3"",
" + "\n" +
@"        ""userId"": ""OPEN_API_USER_ID"",
" + "\n" +
@"        ""password"": ""OPEN_API_USER_PASSWORD""
" + "\n" +
@"    },
" + "\n" +
@"    ""body"": {
" + "\n" +
@"        ""ClientCode"": ""DEMAT_ACCOUNT_CLIENT_CODE""
" + "\n" +
@"    }
" + "\n" +
@"}";
request.AddParameter("application/json", body,  ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
```

### Response body

| FIELD NAME |  | VALUES | DESCRIPTION |
|---|---|---|---|
| head | responseCode<br>STRING | 5PMarginV4 | This is the unique response code for the API. |
| head | status<br>STRING | 0: Success<br>2: Invalid head parameters. | This is the status code which depicts the status of API request to the server. |
| head | statusDescription<br>STRING | Success<br>Invalid head parameters. | This is the description of the status received from the server for the API request. |
| body | ClientCode<br>STRING |  | It is 5paisa demat account client code of the user. |
| body | EquityMargin<br>ARRAY |  | It provides the details of the fund balance of the user at the time of API request. |
| body | MFMargin<br>ARRAY |  | It provides the details of the MF fund balance of the user at the time of API request. |
| body | Status<br>INTEGER | 0: Success<br>1: No record found<br>9: Invalid Session | This is the numeric code<br>for the status of API <br>request |
|  | Message<br>STRING | Success<br>No record found<br>Invalid Session | This is the description of the status of API request. |
|  | TimeStamp<br>DATETIME | - | This is the date and time of the funds information in the epoch format. |

### Equity Margin

Equity Margin refers to the amount of funds a trader must maintain in their account as collateral to initiate and hold positions in the equity market. It acts as a financial guarantee to cover potential losses and ensures compliance with regulatory margin requirements.

| FIELD NAME | VALUES | DESCRIPTION |
|---|---|---|
| Adhoc<br>DOUBLE | - | This is the additional margin provided by 5paisa Capital. |
| CollateralValueAfterHairCut<br>DOUBLE | - | Collateral Margin available after haricut. |
| DPFreeStockValue<br>DOUBLE | - | DPFree stock value which can be pledged to create Collateral Margin. |
| DerivativeMargin<br>DOUBLE | - | Derivative Margin available |
| FundsPayln<br>DOUBLE | - | This is the amount added on the day in the user's account. |
| FundsWithdrawal<br>DOUBLE | - | This is the amount withdrawn on the day from the user's account. |
| GrossHoldingValue<br>DOUBLE | - | This is the gross holding value of the user. |
| GrossHoldingValueCoverPercentage<br>DOUBLE | - | This is the percentage change of gross holding value in the user's trading account. |
| HairCut<br>DOUBLE | - | This is the margin deducted for the pledged stocks to avail collateral margin. |
| Ledgerbalance<br>DOUBLE | - | This is ledger balance of the user. |
| MarginBlockedForPendingOrders<br>DOUBLE | - | This is the margin blocked for pending orders in the user's account. |
| MarginBlockedforOpenPostion_Cash<br>DOUBLE | - | This is the cash margin blocked for open Position in the user's account. |
| MarginBlockedforOpenPostion_Collateral<br>DOUBLE | - | This is the Collateral margin blocked for open Position in the user's account. |
| MarginBlockedforPendingOrder_Cash<br>DOUBLE | - | This is the cash margin blocked for pending orders in the user's account. |
| MarginBlockedforPendingOrder_Collateral<br>DOUBLE | - | This is the collateral margin blocked for pending orders in the user's account. |
| MarginBlockedForOpenPositionAndPendingOrders<br>DOUBLE | - | Returns the total margin blocked against the user's open positions and pending orders |
| MarginUtilized<br>DOUBLE | - | This is total margin utilized for Open Orders in the user's account. |
| NetAvailableMargin<br>DOUBLE | - | This is the total margin which can be used for buying or selling instruments or contracts. |
| OptionsPremium<br>DOUBLE |  | This is total options premium Payable/Receivable. |
| TodaysLoss<br>DOUBLE |  | This is total loss in user's account for a day. |
| TotalCollateralValue<br>DOUBLE |  | This is the total collateral value without haircut. |
| Unsettled_Credits<br>DOUBLE |  | This is unsettled credit amount in users account. |

### SAMPLE SUCCESS RESPONSE

```json
{
   "body": {
       "ClientCode": "50011110",
       "EquityMargin": [
           {
               "AdhocMargin": 0,
               "CollateralValueAfterHairCut": 1135322,
               "DPFreeStockValue": 345402.1,
               "DerivativeMargin": 0,
               "FundsPayln": 0,
               "FundsWithdrawal": 0,
               "GrossHoldingValue": 2106932,
               "GrossHoldingValueCoverPercentage": 100,
               "HairCut": -512627.25,
               "Ledgerbalance": 27787.39,
               "MFCollateralValueAfterHaircut": 363629,
               "MarginBlockedForPendingOrders": 0,
               "MarginBlockedforOpenPostion_Cash": 0,
               "MarginBlockedforOpenPostion_Collateral": 0,
               "MarginBlockedforPendingOrder_Cash": 0,
               "MarginBlockedforPendingOrder_Collateral": 0,
               "MarginUtilized": 0,
               "NetAvailableMargin": 1526738.39,
               "OptionsPremium": 0,
               "TodaysLoss": 0,
               "TotalCollateralValue": 1349952.75,
               "Unsettled_Credits": 0
           }
       ],
       "MFMargin": [
           {
               "MFCollateralValue": 397268.1727,
               "MFFreeStockValue": 2825.5488,
               "MFHaircutValue": 33639.1727
           }
       ],
       "Message": "",
       "Status": 0,
       "TimeStamp": "/Date(1707026698837+0530)/"
   },
   "head": {
       "responseCode": "5PMarginV4",
       "status": "0",
       "statusDescription": "Success"
   }
}
```

### SAMPLE FAILURE RESPONSE

Failure due to incorrect client code or IIFLMarcookie

```json
{
   "body": {
       "ClientCode": null,
       "EquityMargin": [],
       "MFMargin": [],
       "Message": "Invalid ClientCode",
       "Status": 2,
       "TimeStamp": "/Date(1707035098478+0530)/"
   },
   "head": {
       "responseCode": "5PMarginV4",
       "status": "0",
       "statusDescription": "Success"
   }
}
```

### SAMPLE FAILURE RESPONSE

Failure when head parameters are wrong

```json
{
   "body": null,
   "head": {
       "responseCode": "5PMarginV4",
       "status": "2",
       "statusDescription": "Invalid head parameters."
   }
}
```

---

## Multi Order Margin

> Source: https://xstream.5paisa.com/dev-docs/funds-management-system/Multi%20order%20margin

**Type:** Rest API · **Method:** POST

### Multi order margin

**Multi order margin**

This API calculates the margin required for given set of orders. If input is single scrip then margin required for single order is provided if input is multiple scripts then combined margin with hedge benefit is provided. API also accepts parameter CoverPositions if yes the margin is calculated considering existing positions.

### REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/MultiOrderMargin
```

### Request headers

| Key | Value |
|---|---|
| Content-Type | application/json |
| Authorization | bearer{your access token} |

### SAMPLE REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/MultiOrderMargin
```

### Request body

|  |  |  |  |  |
|---|---|---|---|---|
| Field Name |  |  | Mandatory | Description |
| Head |  | key | Yes | AppKey of User or Partner |
| body |  | Client Code | Yes | Client code of user |
| body |  | Cover Positions | Yes |  |
| body | Orders | Exchange |  | Exchange of the insrument |
| body | Orders | Exchange Type |  | Type of exchange |
| body | Orders | Scrip Code |  | Scrip code of the instrument traded |
| body | Orders | PlaceModifyCancel |  | User has to put what function they need:<br>P: Place ,M:Modify,C:Cancel |
| body | Orders | Order Type |  | Type of order |
| body | Orders | Price |  | The price at which order took place at market |
| body | Orders | Quantity |  | The quantity of the orders placed |
| body | Orders | IsIntraday |  | Either the order was intraday or not . <br>Pass boolean value: True/False |

### SAMPLE REQUEST BODY

**JSON**

```json
{
    "head": {
        "key": "6zWyCzzGupJnB7bllZEzlgKbzVCJ7viT"
    },
    "body": {
        "ClientCode": "52839446",
        "CoverPositions":"N",
        "Orders": [
            {
                "Exch": "N",
                "ExchType": "D",
                "ScripCode": "53480",
                "ScripData": "",
                "PlaceModifyCancel": "P",
                "OrderType": "B",
                "Price": 274,
                "Qty": 3000,
                "IsIntraday":false
            }
        ]
    }
}
```

### Response Body

| Field Name |  | Values | Description |
|---|---|---|---|
| head | responseCode | 5PMultiOrderMargin | This is the unique response code for the API. |
| head | status | -1: Server unable to process your request<br>0: Success<br>1: Invalid input parameters.<br>2: Invalid head parameters. | This is the status code which depicts the status of API request to the server. |
| head | statusDescription | Server unable to process your request<br>Success<br>Invalid input parameters.<br>Invalid head parameters. | This is the description of the status received from the server for the API request. |
| body | AvailableMargin | Numeric value | This shows the margin available for user's account |
| body | Message | Success<br>Invalid client code | The message depicts if margin has been fetched succesfully by putting in correct parameters |
| body | Status | -1: Server unable to process your request<br>0: Success<br>1: Invalid input parameters.<br>2: Invalid head parameters. | This is the status code which depicts the status of API request to the server. |
| body | TotalMarginRequired | Numerical value | This calculates the total margin required for you to correctly place the order |

### Response body

**JSON**

```json
{
    "body": {
        "AvailableMargin": 0,
        "Message": "Success",
        "Status": 0,
        "TotalMarginRequired": 145122
    },
    "head": {
        "responseCode": "5PMultiOrderMargin",
        "status": "0",
        "statusDescription": "Success"
    }
}
```
