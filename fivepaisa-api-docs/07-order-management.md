# Order Management System

Place, modify and cancel orders.

## Contents

- [Place Order](#place-order)
- [Modify Order](#modify-order)
- [Cancel Order](#cancel-order)

---

## Place Order

> Source: https://xstream.5paisa.com/dev-docs/order-management-system/place-order

**Type:** Rest API · **Method:** POST

The API allows clients and partners to place an order for the user by taking order details in the input.

The Order API is the backbone of the trading system as it allows the application to place an order through the client’s demat account.

The API requires authentication for successful execution. The authentication can be provided by passing the Access token(Bearer token).

The API is flexible with a variety of orders and allows the users to place the following type of orders:

- Limit Order
- Market Order
- Stop Loss Order
- Stop Loss – Market Order
- After Market Order
- IOC Order

The above-mentioned types of orders can be placed as intraday or delivery.

The API works either with ScripCode or ScripData, ScripData format is mentioned here.

> **Note — Order Tracking**
> Once an order is placed, its status can be tracked through the following methods:
>
> Order Status API
>
> Order Book
>
> Order Confirmation via WebSocket (recommended)
>
> Upon placing an order, the API returns a BrokerOrderId. This BrokerOrderId can then be used to fetch the ExchangeOrderId. All three of the aforementioned order APIs can help you map the BrokerOrderId to the ExchangeOrderId.

> **Note — RemoteOrderId Usage**
> Overview
>
> We have introduced the RemoteOrderId field as a user-defined identifier. Partners or clients can create their own RemoteOrderId and include it when placing an order.
>
> This identifier serves several purposes:
>
> Track Order Status: Use the RemoteOrderId to track the order status via the Order Stand API.
>
> Obtain ExchangeOrderId: Retrieve the ExchangeOrderId using the RemoteOrderId, which can then be used to modify the order.
>
> Usage and Benefits:
>
> In certain scenarios, specifically with Stop-Loss (SL) orders, we have observed issues where the BrokerOrderId changes, causing clients to be unable to map the ExchangeOrderId from the broker ID. To mitigate this issue, we recommend using the RemoteOrderId.

### REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V1/PlaceOrderRequest
```

### Headers

| KEY | VALUE |
|---|---|
| Content-Type | application/json |
| Authorization | bearer {Your Access Token} |

### Request body

| FIELD NAME |  |  | MANDATORY | DESCRIPTION |
|---|---|---|---|---|
| p_Data | head | Key<br>STRING | Yes | AppKey of User or Partner |
| p_Data | body | OrderType<br>STRING | Yes | Represents if it is buy or sell order.<br>B: Buy<br>S: Sell |
| p_Data | body | Exchange<br>STRING | Yes | This is the exchange of the instrument<br>N: NSE<br>B: BSE<br>M: MCX |
| p_Data | body | ExchangeType<br>STRING | Yes | This is the exchange segment of the instrument<br>C: Cash<br>D: Derivatives (FnO of NSE, BSE & MCX)<br>U: Currency |
| p_Data | body | ScriCode<br>STRING | Yes | ScripCode of the instrument |
| p_Data | body | ScriData<br>STRING | Yes | It is the unique symbol of the instrument for which order needs to be placed, format is mentioned below. |
| p_Data | body | Price<br>DOUBLE | No | It is the price at which order needs to be placed. (0 for market orders). |
| p_Data | body | Qty<br>INTEGER | Yes | Total quantity in the modified order |
| p_Data | body | StopLossPrice<br>DOUBLE | No | It is the stop loss price for the order |
| p_Data | body | DisQty<br>INTEGER | No | It is the quantity to be disclosed publicly |
| p_Data | body | IsIntraday<br>BOOLEAN | No | It specifies if the order is intraday or delivery order<br>Intraday: true<br>Delivery: false |
| p_Data | body | AHPlaced<br>STRING | No | It specifies if the order is after market order or not<br>After Market: Y<br>Limt/At-market: N |
| p_Data | body | isMTF<br>BOOLEAN | No | When isMTF is set to true, the order will be treated as an MTF order. |
| p_Data | body | RemoteOrderID<br>STRING | Yes | This is a unique ID which user can generate for his/her reference |

> **Note — Note**
> 1. If the price is not passed in the request body, its value will be considered as 0. The 0 value of price indicates order to be of at-market type. It takes market price by default.
> 2. Disclosed quantity passed in the field “DisQty” should always be less than or equal to the value of the field “Qty”.
> 3. The values of exchange, exchange type, ScripCode , symbol name, expiry, option type and strike can be fetched from the scrip master.
> 4. The field “ScripData” follows a particular structure for the stocks which is mentioned below:

> **Note — Algo ID**
> To perform algorithmic trading via 5paisa, users must comply with SEBI regulations. This includes obtaining a valid Algo ID for identification and authorization.
>
> Who Needs an Algo ID?
>
> To perform algorithmic trading via 5paisa, users must comply with SEBI regulations. This includes obtaining a valid Algo ID for identification and authorization.
>
> Algo Users:  
> Traders who wish to execute orders through algorithmic strategies must be registered as algo users.  
> To obtain an Algo ID, users must send a request to support@5paisa.com. Once approved, a unique Algo ID will be generated and provided by the 5paisa team. This ID must be used in all relevant API requests.
>
> Non-Algo Users:  
> Users who are not registered for algorithmic trading should pass the `AlgoID` as `0` or `null` in their API requests.

### Symbol Format - scripData

| INSTRUMENT TYPE | SYMBOL FORMAT | SAMPLE VALUE |
|---|---|---|
| Cash | Symbol Name_EQ | RELIANCE_EQ |
| Derivatives | Futures-<br>SYMBOL Name_yyyymmdd<br>Derivatives -SYMBOL_YYYYMMDD_CE/PE_STRIKE | Futures - NIFTY 30 Sep 2021_20210930<br>Options - BANKNIFTY 29 Mar 2023 CE 41600.00_20230329_CE_41600 |
| Currency | Symbol Name_Expiry_Option Type_Strike Rate | GBPINR 29 Dec 2021 CE 107.2500_1325255400_CE_107.25 |
| Commodity | Symbol Name_Expiry_Option Type_Strike Rate | SILVER 27 Aug 2021 CE 63750.00_1314489600_CE_63750 |

### SAMPLE REQUEST BODY

**JSON**

```json
{
    "head": {
        "key": "{{Your App Key}}"
    },
    "body": {
        "Exchange":"N",
        "ExchangeType":"C",
        "ScripCode":"1660",
        "Price": "445",
        "StopLossPrice": "0",
        "OrderType": "Buy",
        "Qty": 1,
        "DisQty": "0",
        "IsIntraday": true,
        "iOrderValidity": "0",
        "AHPlaced":"N"
    }
}
```

**cURL**

```bash
curl --location 'https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V1/PlaceOrderRequest' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {access_token}' \
--data '{
    "head": {
        "key": "{Your App Key}"
    },
    "body": {
        "Exchange":"N",
        "ExchangeType":"C",
        "ScripCode":"1660",
        "Price": "445",
        "StopLossPrice": "0",
        "OrderType": "Buy",
        "Qty": 1,
        "DisQty": "0",
        "IsIntraday": false,
        "iOrderValidity": "0",
        "AHPlaced":"N"
    }
}'
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

#Using Scrip Data :-

client.place_order(OrderType='B',Exchange='N',ExchangeType='C', ScripData = 'ITC_EQ', Qty=1, Price=450)

#Using Scrip Code :-

#Sample For SL order (for order to be treated as SL order just pass StopLossPrice)
client.place_order(OrderType='B',Exchange='N',ExchangeType='C', ScripCode = 1660, Qty=1, Price=350, IsIntraday=False, StopLossPrice=345)

#Derivative Order
client.place_order(OrderType='B',Exchange='N',ExchangeType='D', ScripCode = 57633, Qty=50, Price=1.5)
```

**JAVA**

```java

```

**C#**

```csharp

```

### Response body

| FIELD NAME |  | VALUES | DESCRIPTION |
|---|---|---|---|
| head | responseCode<br>STRING | 5PPlaceOrdReqV1 | This is the unique response code for the API. |
| head | status<br>STRING | -1: Server unable to process your request<br>0: Success<br>1: Invalid input parameters.<br>2: Invalid head parameters. | This is the status code which depicts the status of API request to the server. |
| head | statusDescription<br>STRING | Server unable to process your request<br>Success<br>Invalid input parameters.<br>Invalid head parameters. | This is the description of the status received from the server for the API request. |
| body | BrokerOrderID<br>INTEGER | - | This is the order ID generated from the Broker's end |
| body | ClientCode<br>STRING | - | This is the 5paisa demat account client code of the user |
| body | Exch<br>STRING | N: NSE<br>B: BSE<br>M: MCX | This is the exchange of the instrument |
| body | ExchOrderID<br>INTEGER | - | This is the order ID generated by the exchange. |
| body | ExchType<br>STRING | C: Cash<br>D: Derivatives (FnO of NSE, BSE & MCX)<br>U: Currency | This is the exchange segment for the order |
| body | LocalOrderID<br>INTEGER | - | This is the numeric local order ID generated by the user |
| body | Message<br>STRING | 0: Success<br>1: 5paisa System (RMS) Response<br>2: Invalid Input Parameters.<br>9: Authentication Fails | This is the status description of the order API request based on input parameters.<br>**Note :** The current RMS rejections will be decommissioned once we migrate to the new order placement APIs. Kindly design your product accordingly, as the Order Book API is expected to be helpful for this purpose. |
| body | RMSResponseCode<br>INTEGER | - | This is the status code of the order received from 5paisa Securities system |
| body | RemoteOrderID<br>STRING | - | This is the unique order ID passed for the order while sending the request |
| body | ScripCode<br>INTEGER | - | This is the numeric code for the instrument in which order has been placed |
| body | Status<br>INTEGER | 0: Success<br>1: 5paisa System (RMS) Response<br>2: Invalid Input Parameters.<br>9: Authentication Fails | This is the status code of the API response |
| body | Time<br>DATETIME | - | This is the time at which order has been placed |

### SAMPLE SUCCESS RESPONSE

```json
{
    "body": {
        "BrokerOrderID": 672112769,
        "ClientCode": "CLIENT_CODE",
        "Exch": "N",
        "ExchOrderID": "0",
        "ExchType": "C",
        "LocalOrderID": 0,
        "Message": "Success",
        "RMSResponseCode": 1,
        "RemoteOrderID": "YESBANKTESTING15",
        "ScripCode": 11915,
        "Status": 0,
        "Time": "/Date(1658255400000+0530)/"
    },
    "head": {
        "responseCode": "5PPlaceOrdReqV1",
        "status": "0",
        "statusDescription": "Success"
    }
}
```

### SAMPLE FAILURE RESPONSE

Failure due to invalid user key being passed in the request

```json
{
    "body": null,
    "head": {
        "responseCode": "5PPlaceOrdReqV1",
        "status": "2",
        "statusDescription": "Invalid Head Parameters"
    }
}
```

### SAMPLE FAILURE RESPONSE

Failure due to invalid JWT token passed in the request

```json
{
    "body": {
        "BrokerOrderID": 0,
        "ClientCode": "",
        "Exch":"?”, 
        "ExchOrderID": "",
        "ExchType":"?”, 
        "LocalOrderID": 0,
        "Message": "Authentication Fails",
        "RMSResponseCode": 0,
        "ScripCode": 0,
        "Status": 9,
        "Time": "/Date(1637494442204+0530)/"
    },
    "head": {
        "responseCode": "5PPlaceOrdReqV1",
        "status": "0",
        "statusDescription": "Fail"
    }
}
```

### SAMPLE FAILURE RESPONSE

Failure when client code is not passed respective to the user's JWT token

```json
{
    "body": {
        "BrokerOrderID": 0,
        "ClientCode": "",
        "Exch":"?”, 
        "ExchOrderID": "",
        "ExchType":"?”, 
        "LocalOrderID": 0,
        "Message": "Invalid Session",
        "RMSResponseCode": 0,
        "ScripCode": 0,
        "Status": 9,
        "Time": "/Date(1637494569494+0530)/"
    },
    "head": {
        "responseCode": "5PPlaceOrdReqV1",
        "status": "0",
        "statusDescription": "Fail"
    }
}
```

### Sample Failure Response

Failure due to missing mandatory parameters in the request

```json
{
    "body": {
        "BrokerOrderID": 0,
        "ClientCode": "5paisa_Client",
        "Exch":"?”, 
        "ExchOrderID": "0",
        "ExchType":"?”, 
        "LocalOrderID": 0,
        "Message": "Invalid Input Parameters.",
        "RMSResponseCode": 0,
        "ScripCode": 0,
        "Status": 2,
        "Time": "/Date(1637494757568+0530)/"
    },
    "head": {
        "responseCode": "5PPlaceOrdReqV1",
        "status": "0",
        "statusDescription": "Success"
    }
}
```

---

## Modify Order

> Source: https://xstream.5paisa.com/dev-docs/order-management-system/modify-order

**Type:** Rest API · **Method:** POST

The API allows clients and partners to modify an order for the user by taking order details in the input.

This API provides a modification functionality to the users where they can modify any order which is not executed successfully yet. The users can change the price, quantity and stop loss price as well as the type of order from limit to market order and market to limit order.

Please note you just need to pass the filed to be modified along with exchangeOrderId, passing all other fields is not mandatory.

The API requires “ExchangeOrderID” for order identification which can be fetched from order book. This API requires authentication for successful execution, and it can be provided by passing the access token received through OAuth .

> **Note — ExchangeOrderId**
> Please note modify API required ExchangeOrderId to modify an Order. There are 2 ways to fetch exchOrderId for an order, either through OrderBook with help of mapping brokerOrderId to exchOrderId or through Order Status API with help of remoteOrderID.
>
> The `remoteOrderID` is a unique identifier assigned by our system to track and manage orders efficiently. We strongly recommend using this identifier for all order modification requests to ensure precise and reliable updates, minimizing discrepancies and enhancing order management consistency.

### REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V1/ModifyOrderRequest
```

### Headers

| KEY | VALUE |
|---|---|
| Content-Type | application/json |
| Authorization | bearer {Your Access Token} |

### Request body

| FIELD NAME |  |  | MANDATORY | DESCRIPTION |
|---|---|---|---|---|
| p_Data | head | UserKey<br>STRING | Yes | User Key of the client received along with API <br>credentials |
| p_Data | body | ExchangeOrderID<br>STRING | Yes | It is the order ID generated by the exchange |
| p_Data | body | Price<br>DOUBLE | No | It is the price at which order needs to be placed |
| p_Data | body | Qty<br>INTEGER | No | Total quantity in the modified order |
| p_Data | body | StopLossPrice<br>DOUBLE | No | It is the stop loss price for the order |
| p_Data | body | DisQty<br>INTEGER | No | It is the quantity disclosed to the market |

> **Note — Note**
> 1. The 0 value of price indicates order to be of at-market type. It takes market price by default.
> 2. Disclosed quantity passed in the field “DisQty” should always be less than or equal to the value of the field “Qty”.

### SAMPLE REQUEST BODY

**JSON**

```json
{
    "head": {
        "key": "{{Your App Key}}"
    },
    "body": {
        "Price":"0",
        "StopLossPrice":"449",
        "ExchOrderID": "1100000018012644"
    }
}
```

**cURL**

```bash
curl --location --request POST 'https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V1/ModifyOrderRequest' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "head": {
        "key": "{{app_key}}"
    },
    "body": {
        "Price":"0",
        "StopLossPrice":"449",
        "ExchOrderID": "1100000018012644"
    }
}'
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

#Modify Quantity
client.modify_order(ExchOrderID="1100000017861430", Qty=2)

#Modify Price
client.modify_order(ExchOrderID="1100000017861430", Price=261)
```

**JAVA**

```java
Unirest.setTimeouts(0, 0);
HttpResponse<String> response = Unirest.post("https://dataservice.iifl.in/openapi/prod/V2/ModifyOrder")
  .header("Ocp-Apim-Subscription-Key", "fc714d8e5b82438a93a95baa493ff45b")
  .header("Content-Type", "application/json")
  .header("Cookie", "IIFLMarcookie=zhsq1apyptvtborjcaec4o3d")
  .body("{\r\n    \"p_Data\": {\r\n        \"head\": {\r\n            \"UserKey\": \"OPEN_API_USER_KEY\",\r\n            \"JWTToken\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik1BWUFOQ0hJIiwicm9sZSI6IjYwIiwibmJmIjoxNjM3NTA0Mzc0LCJleHAiOjE2Mzc1MDQ0MDQsImlhdCI6MTYzNzUwNDM3NH0.KVbF6CXRab7ZoT00N3noU0mN6pR1c6n6YaD2p4Dr0dw\"\r\n        },\r\n        \"body\": {\r\n            \"ClientCode\": \"CLIENT_CODE\",\r\n            \"ExchOrderID\": \"1100000000082718\",\r\n            \"Price\": 1902,\r\n            \"UniqueOrderID\": 2,\r\n            \"OrderType\": \"BUY\",\r\n            \"Qty\": 1,\r\n            \"Exchange\": \"N\",\r\n            \"ExchangeType\": \"C\",\r\n            \"NmSymbol\": \"RELIANCE_EQ\",\r\n            \"AtMarket\": false,\r\n            \"DisQty\": 0,\r\n            \"IsStopLossOrder\": false,\r\n            \"StopLossPrice\": 1170,\r\n            \"IOCOrder\": false,\r\n            \"IsIntraday\": false,\r\n            \"AHPlaced\": \"N\",\r\n            \"ValidTillDate\": \"/Date(1563857357611)/\"\r\n        }\r\n    },\r\n    \"AppSource\": 0\r\n}")
  .asString();
```

**C#**

```csharp
var client = new RestClient("https://dataservice.iifl.in/openapi/prod/V2/ModifyOrder");
client.Timeout = -1;
var request = new RestRequest(Method.POST);
request.AddHeader("Ocp-Apim-Subscription-Key", "fc714d8e5b82438a93a95baa493ff45b");
request.AddHeader("Content-Type", "application/json");
request.AddHeader("Cookie", "IIFLMarcookie=zhsq1apyptvtborjcaec4o3d");
var body = @"{
" + "\n" +
@"    ""p_Data"": {
" + "\n" +
@"        ""head"": {
" + "\n" +
@"            ""UserKey"": ""OPEN_API_USER_KEY"",
" + "\n" +
@"            ""JWTToken"": ""eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik1BWUFOQ0hJIiwicm9sZSI6IjYwIiwibmJmIjoxNjM3NTA0Mzc0LCJleHAiOjE2Mzc1MDQ0MDQsImlhdCI6MTYzNzUwNDM3NH0.KVbF6CXRab7ZoT00N3noU0mN6pR1c6n6YaD2p4Dr0dw""
" + "\n" +
@"        },
" + "\n" +
@"        ""body"": {
" + "\n" +
@"            ""ClientCode"": ""CLIENT_CODE"",
" + "\n" +
@"            ""ExchOrderID"": ""1100000000082718"",
" + "\n" +
@"            ""Price"": 1902,
" + "\n" +
@"            ""UniqueOrderID"": 2,
" + "\n" +
@"            ""OrderType"": ""BUY"",
" + "\n" +
@"            ""Qty"": 1,
" + "\n" +
@"            ""Exchange"": ""N"",
" + "\n" +
@"            ""ExchangeType"": ""C"",
" + "\n" +
@"            ""NmSymbol"": ""RELIANCE_EQ"",
" + "\n" +
@"            ""AtMarket"": false,
" + "\n" +
@"            ""DisQty"": 0,
" + "\n" +
@"            ""IsStopLossOrder"": false,
" + "\n" +
@"            ""StopLossPrice"": 1170,
" + "\n" +
@"            ""IOCOrder"": false,
" + "\n" +
@"            ""IsIntraday"": false,
" + "\n" +
@"            ""AHPlaced"": ""N"",
" + "\n" +
@"            ""ValidTillDate"": ""/Date(1563857357611)/""
" + "\n" +
@"        }
" + "\n" +
@"    },
" + "\n" +
@"    ""AppSource"": 0
" + "\n" +
@"}";
request.AddParameter("application/json", body,  ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
```

### Response body

| FIELD NAME |  | VALUES | DESCRIPTION |
|---|---|---|---|
| head | responseCode<br>STRING | 5PModifyOrdReqV1 | This is the unique response code for the API. |
| head | status<br>STRING | -1: Server unable to process your request<br>0: Success<br>1: Invalid input parameters.<br>2: Invalid head parameters. | This is the status code which depicts the status of API request to the server. |
| head | statusDescription<br>STRING | Server unable to process your request<br>Success<br>Invalid input parameters.<br>Invalid head parameters. | This is the description of the status received from the server for the API request. |
| body | BrokerOrderID<br>INTEGER | - | This is the order ID generated from the 5paisa end |
| body | ClientCode<br>STRING | - | This is the 5paisa demat account client code of the user |
| body | Exch<br>STRING | N: NSE<br>B: BSE<br>M: MCX | This is the exchange of the instrument |
| body | ExchOrderID<br>STRING | - | This is the order ID generated by the exchange |
| body | ExchType<br>STRING | C: Cash<br>D: Derivatives (FnO of NSE, BSE & MCX)<br>U: Currency | This is the exchange segment for the order |
| body | Message<br>STRING | 0: Success<br>1: System (RMS) Response<br>2: Invalid Input Parameters.<br>9: Authentication Fails | This is the status description of the order API request based on input parameters.<br>**Note :** The current RMS rejections will be decommissioned once we migrate to the new order placement APIs. Kindly design your product accordingly, as the Order Book API is expected to be helpful for this purpose. |
| body | RMSResponseCode<br>INTEGER | - | This is the status code of the order received from 5paisa Securities system |
| body | RemoteOrderID<br>STRING | - | This is the unique order ID passed for the order while sending the request |
| body | ScripCode<br>INTEGER | - | This is the numeric code for the instrument in which order has been placed |
| body | Status<br>INTEGER | 0: Success<br>1: System (RMS) Response<br>2: Invalid Input Parameters.<br>9: Authentication Fails | This is the status code of the API response |
| body | Time<br>DATETIME | - | This is the time at which order has been placed |

### SAMPLE SUCCESS RESPONSE

```json
{
    "body": {
        "BrokerOrderID": 292699,
        "ClientCode": "{clientcode}",
        "Exch": "B",
        "ExchOrderID": "116718512092173",
        "ExchType": "D",
        "LocalOrderID": 4,
        "Message": "Exchange is closed. Cannot Modify your order.",
        "RMSResponseCode": -15,
        "RemoteOrderID": "1716729926",
        "ScripCode": 86752,
        "Status": 1,
        "Time": "/Date(171674800000+0530)/"
    },
    "head": {
        "responseCode": "5PModifyOrdReqV1",
        "status": "0",
        "statusDescription": "Success"
    }
}
```

### SAMPLE FAILURE RESPONSE

Failure due to invalid user key being passed in the request

```json
{
    "body": null,
    "head": {
        "responseCode": "5PModifyOrdReqV1",
        "status": "2",
        "statusDescription": "Invalid head parameters."
    }
}
```

### SAMPLE FAILURE RESPONSE

Not passing access token

```json
Invalid Token
```

### SAMPLE FAILURE RESPONSE

Failure when ExchangeOrderID is not passed

```json
{
    "body": {
        "BrokerOrderID": 0,
        "ClientCode": "client_code",
        "Exch":"N",
		"ExchOrderID": "0",
        "ExchType":"C",
		"LocalOrderID": 0,
        "Message": "Order does not exist",
        "RMSResponseCode": 0,
        "RemoteOrderID": "",
        "ScripCode": 0,
        "Status": 1,
        "Time": "/Date(1716811251790+0530)/"
    },
    "head": {
        "responseCode": "5PModifyOrdReqV1",
        "status": "0",
        "statusDescription": "Success"
    }
}
```

---

## Cancel Order

> Source: https://xstream.5paisa.com/dev-docs/order-management-system/cancel-order

**Type:** Rest API · **Method:** POST

The API allows clients and partners to cancel an order for the user by taking order details in the input.

The API allows the user to cancel the order which has not been executed successfully yet.

The API can cancel the order by passing just exchange order ID. These details for any order can be fetched from the Order Status, Order book or Order Webscoket.

### REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V1/CancelOrderRequest
```

### Headers

| KEY | VALUE |
|---|---|
| Content-Type | application/json |
| Authorization | bearer {Your Access Token} |

### Request body

| FIELD NAME |  | MANDATORY | DESCRIPTION |
|---|---|---|---|
| head | Key<br>STRING | Yes | AppKey of User or Partner |
| body | ExchangeOrderID<br>STRING | Yes | It is the order ID generated by the exchange |

### SAMPLE REQUEST BODY

**JSON**

```json
{
    "head": {
        "key": "{Your App Key}"
    },
    "body": {
        "ExchOrderID":"1000000000000970"
    }
}
```

**cURL**

```bash
curl --location 'https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V1/CancelOrderRequest' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {access_token}' \
--data '{
    "head": {
        "key": "{Your App Key}"
    },
    "body": {
        "ExchOrderID":"1000000000000970"
    }
}'
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

client.cancel_order(exch_order_id="1100000017795041")

cancel_bulk=[
            {
                "ExchOrderID": "<Exchange Order ID 1>"
            },
            {
                "ExchOrderID": "<Exchange Order ID 2>"
            },
client.cancel_bulk_order(cancel_bulk)
```

**JAVA**

```java

```

**C#**

```csharp

```

### Response body

| FIELD NAME |  | VALUES | DESCRIPTION |
|---|---|---|---|
| head | responseCode<br>STRING | 5PCancelOrdReqV1 | This is the unique response code for the API. |
| head | status<br>STRING | -1: Server unable to process your request<br>0: Success<br>1: Invalid input parameters.<br>2: Invalid head parameters. | This is the status code which depicts the status of API request to the server. |
| head | statusDescription<br>STRING | Server unable to process your request<br>Success<br>Invalid input parameters.<br>Invalid head parameters. | This is the description of the status received from the server for the API request. |
| body | BrokerOrderID<br>INTEGER | - | This is the order ID generated from the 5paisa's end |
| body | ClientCode<br>STRING | - | This is the 5paisa demat account client code of the user |
| body | Exch<br>STRING | N: NSE<br>B: BSE<br>M: MCX | This is the exchange of the instrument |
| body | ExchOrderID<br>STRING | - | This is the order ID generated by the exchange |
| body | ExchType<br>STRING | C: Cash<br>D: Derivatives (FnO of NSE, BSE & MCX)<br>U: Currency | This is the exchange segment for the order |
| body | LocalOrderID<br>INTEGER | - | This is the numeric local order ID generated by the user |
| body | Message<br>STRING | 0: Success<br>1: 5paisa System (RMS) Response<br>2: Invalid Input Parameters.<br>9: Authentication Fails | This is the status description of the order API request based on input parameters.<br>**Note :** The current RMS rejections will be decommissioned once we migrate to the new order placement APIs. Kindly design your product accordingly, as the Order Book API is expected to be helpful for this purpose. |
| body | RMSResponseCode<br>INTEGER | - | This is the status code of the order received from 5paisa system |
| body | RemoteOrderID<br>STRING | - | This is the unique order ID passed for the order while sending the request |
| body | ScripCode<br>INTEGER | - | This is the numeric code for the instrument in which order has been placed |
| body | Status<br>INTEGER | 0: Success<br>1: 5paisa System (RMS) Response<br>2: Invalid Input Parameters.<br>9: Authentication Fails | This is the status code of the API response |
| body | Time<br>DATETIME | - | This is the time at which order has been cancelled |

### SAMPLE SUCCESS RESPONSE

```json
{
    "body": {
        "BrokerOrderID": 555919893,
        "ClientCode": "5paisa_CLIENT",
        "Exch": "N",
        "ExchOrderID": "0",
        "ExchType": "C",
        "LocalOrderID": 0,
        "Message": "Success",
        "RMSResponseCode": 0,
        "ScripCode": 2885,
        "Status": 0,
        "Time": "/Date(1637433000000+0530)/"
    },
    "head": {
        "responseCode": "5PCancelOrdReqV1",
        "status": "0",
        "statusDescription": "Success"
    }
}
```

### SAMPLE FAILURE RESPONSE

Failure due to invalid user key being passed in the request

```json
{
    "body": null,
    "head": {
        "responseCode": "5PCancelOrdReqV1",
        "status": "2",
        "statusDescription": "Invalid Head Parameters"
    }
}
```

### Sample Failure Response

Failure due to missing mandatory parameters in the request

```json
{
    "body": {
        "BrokerOrderID": 0,
        "ClientCode": "5paisa_Client",
        "Exch":"?”, 
        "ExchOrderID": "0",
        "ExchType":"?”, 
        "LocalOrderID": 0,
        "Message": "Invalid Input Parameters.",
        "RMSResponseCode": 0,
        "ScripCode": 0,
        "Status": 2,
        "Time": "/Date(1637494757568+0530)/"
    },
    "head": {
        "responseCode": "5PCancelOrdReqV1",
        "status": "0",
        "statusDescription": "Success"
    }
}
```
