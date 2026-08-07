# Portfolio Management System

Holdings, net-wise positions and eDIS authorisation.

## Contents

- [Holdings](#holdings)
- [Net-wise Position](#net-wise-position)
- [EDIS](#edis)

---

## Holdings

> Source: https://xstream.5paisa.com/dev-docs/portfolio-management-system/holdings

**Type:** Rest API · **Method:** POST

The API provides details of all the stocks in holdings of the user.

The API is helpful in building holdings section in any application as well as providing various analytics options through holdings data of the user. This API requires successful authentication of the user for which data is being fetched.

A successful API response provides instrument details, quantity in holdings, current value of holdings, current profit and loss through the holdings as well as flag for E-Dis authorization of the holdings through the depository.

### REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V3/Holding
```

### Request headers

| KEY | VALUE |
|---|---|
| Content-Type | application/json |
| Authorization | bearer {Your Access Token} |

### Request body

| FIELD NAME |  | MANDATORY | DESCRIPTION |
|---|---|---|---|
| head | key<br>STRING | Yes | AppKey Of User or Partner |
| body | ClientCode<br>STRING | Yes | 5paisa demat account client code of the user. |

### SAMPLE REQUEST BODY

**JSON**

```json
{
    "head": {
        "key": "{Your App Key}"
    },
    "body": {
        "ClientCode": "{Your Client Code}"
    }
}
```

**cURL**

```bash
curl --location --request POST 'https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V3/Holding' \
--header 'Authorization: bearer {Your Access Token}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "head": {
        "key": "{Your Vendor/User Key}"
    },
    "body": {
        "ClientCode": "{Your Client Code}"
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

client.holdings()
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
| head | responseCode<br>STRING | 5PHoldingV3 | This is the unique response code for the API. |
| head | status<br>STRING | 0: Success<br>2: Invalid head parameters. | This is the status code which depicts the status of API request to the server. |
| head | statusDescription<br>STRING | Success<br>Invalid head parameters. | This is the description of the status received from the server for the API request. |
| body | Data<br>ARRAY |  | It provides the list of all stocks available in user's 5paisa account holdings. |
| body | CacheTime<br>INTEGER |  | It is the cache time for the update in holdings data. |
| body | Status<br>INTEGER | 0: Success<br>1: No data found for this Client.<br>9: Invalid Session | This is the numeric code<br>for the status of API <br>request |
|  | Message<br>STRING | Success<br>No data found for this Client.<br>Invalid Session | This is the description of the status of API request. |

### Data

| FIELD NAME | VALUES | DESCRIPTION |
|---|---|---|
| AvgRate<br>DOUBLE | - | Avg Price for which the stock holding is brought. |
| BseCode<br>INTEGER | - | This is the unique scrip code of the instrument for BSE. |
| CurrentPrice<br>DOUBLE | - | It is the market price of the instrument. |
| DPQty<br>INTEGER | - | It is the market price of the instrument. |
| Exch<br>STRING | N: NSE<br>B: BSE<br>M: MCX | This is the exchange in which holdings is available. |
| ExchType<br>STRING | C: Cash<br>D: Derivatives (NSE, BSE & MCX F&O)<br>U: Currency | This is exchange type in which the holdings is available. |
| FullName<br>STRING | - | This is the full name for the instrument in the holdings. |
| MTFPledge<br>INTEGER | - | MTFPledge – Quantity pledged under MTF. |
| MTFQty<br>INTEGER | - | MTFQty – Quantity currently held under MTF. |
| NseCode<br>INTEGER | - | This is the unique scrip code of the instrument for NSE. |
| POASigned<br>STRING | Y: E-Dis authorized<br>N: Unauthorized quantity | This is the flag for E-Dis authorization of the holdings. |
| PoolQty<br>STRING | - | DP Pool Quantity of the instrument. |
| Quantity<br>INTEGER | - | Total Holding Quantity of the Instrument. |
| ScripMultiplier<br>INTEGER | - | ScripMultiplier of the instrument. |
| Symbol<br>STRING | - | This is symbol name for the instrument in holdings |

### SAMPLE SUCCESS RESPONSE

```json
{
    "body": {
        "CacheTime": 300,
        "Data": [
            {
                "AvgRate": 455.7229,
                "BseCode": 500875,
                "CurrentPrice": 440.1,
                "DPQty": 7,
                "Exch": "N",
                "ExchType": "C",
                "FullName": "ITC LTD",
                "NseCode": 1660,
                "POASigned": "N",
                "PoolQty": 0,
                "Quantity": 7,
                "ScripMultiplier": 1,
                "Symbol": "ITC"
            },
            {
                "AvgRate": 242.45,
                "BseCode": 543940,
                "CurrentPrice": 253.8,
                "DPQty": 40,
                "Exch": "N",
                "ExchType": "C",
                "FullName": "JIO FIN SERVICES LTD",
                "NseCode": 18143,
                "POASigned": "N",
                "PoolQty": 0,
                "Quantity": 40,
                "ScripMultiplier": 1,
                "Symbol": "JIOFIN"
            }
        ],
        "Message": "Success",
        "Status": 0
    },
    "head": {
        "responseCode": "5PHoldingV3",
        "status": "0",
        "statusDescription": "Success"
    }
}
```

### SAMPLE FAILURE RESPONSE

Failure due to incorrect client code

```json
{
    "body": {
        "CacheTime": 0,
        "Data": [],
        "Message": "Invalid ClientCode",
        "Status": 2
    },
    "head": {
        "responseCode": "5PHoldingV3",
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
        "responseCode": "5PHoldingV3",
        "status": "2",
        "statusDescription": "Invalid head parameters."
    }
}
```

---

## Net-wise Position

> Source: https://xstream.5paisa.com/dev-docs/portfolio-management-system/netwise-positions

**Type:** Rest API · **Method:** POST

The API provides details of all the stocks in positions of the user.

NetPosition API provides Open Positions in Derivates contracts and Intraday Stock positions.

Overnight Derivative positions can be identified with BodQty flag. While overnigh stock positions will not appear as it will be converted to holding.

### REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V2/NetPositionNetWise
```

### Request headers

| KEY | VALUE |
|---|---|
| Content-Type | application/json |
| Authorization | bearer{Your Access Token} |

### Request body

| FIELD NAME |  | MANDATORY | DESCRIPTION |
|---|---|---|---|
| head | key<br>STRING | Yes | AppKey of user or partner. |
| body | Clientcode<br>STRING | Yes | 5paisa demat account client code of the user in plain text. |

### SAMPLE REQUEST BODY

**JSON**

```json
{
    "head": {
        "key": "{{vendor_key}}"
    },
    "body": {
        "ClientCode": "{{clientcode}}"
    }
}
```

**cURL**

```bash
curl --location 'https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V2/NetPositionNetWise' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {access_token}' \
--data '{
    "head": {
        "key": "{App Key}"
    },
    "body": {
        "ClientCode": "{client_code}"
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

# Fetches positions
client.positions()
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
| head | responseCode<br>STRING | 5PNPNWV2 | This is the unique response code for the API. |
| head | status<br>STRING | 0: Success<br>2: Invalid head parameters. | This is the status code which depicts the status of API request to the server. |
| head | statusDescription<br>STRING | Success<br>Invalid head parameters. | This is the description of the status received from the server for the API request. |
| body | NetPositionDetail<br>ARRAY |  | It provides the list of all stocks available in user's IIFL Securities account positions for the day along with holdings as beginning of the day. |
| body | Status<br>INTEGER | 0: Success<br>1: No record found<br>9: Invalid Session | This is the numeric code<br>for the status of API <br>request |
|  | Message<br>STRING | Success<br>No record found<br>Invalid Session | This is the description of the status of API request. |

### NetPositionDetail

| FIELD NAME | VALUES | DESCRIPTION |
|---|---|---|
| BODPositionPrice<br>DOUBLE | - | This is the price of the instrument in positions as beginning of the day. |
| BodQty<br>INTEGER | - | This is total quantity of the instrument in positions as beginning of the day. |
| BookedPL<br>DOUBLE | - | Total profit or loss booked for the day by the user through the instrument. |
| BuyAvgRate<br>DOUBLE | - | This is the average rate at which instrument is bought on the day. |
| BuyQty<br>INTEGER | - | This is total quantity of the instrument bought on the day. |
| BuyValue<br>DOUBLE | - | It is total value of the instrument bought on the day. |
| Exch<br>STRING | N: NSE<br>B: BSE<br>M: MCX<br>N: NCDEX (for exchange type = ‘X’) | This is the exchange in which position is available. |
| ExchType<br>STRING | C: Cash<br>D: Derivatives (NSE, BSE & MCX F&O)<br>U: Currency<br>Y: NSE & BSE Commodities<br>X: NCDEX Commodities | This is exchange type in which the position is available. |
| LTP<br>DOUBLE | - | This is last traded price for the instrument for the time request is sent. |
| MTOM<br>DOUBLE | - | This is the market-to-market profit or loss from the position. |
| Multiplier<br>INTEGER | - | This is multiplier of quantity used while calculating profit or loss. |
| NetQty<br>INTEGER | - | This is the net quantity of the position. |
| OrderFor<br>STRING | D: Delivery<br>I: Intraday<br>S: Bracket Order<br>C: Cover Order | This is the type of the position. |
| PreviousClose<br>DOUBLE | - | This is closing price of the previous trading day for the instrument. |
| ScripCode<br>INTEGER | - | This is unique code for the instrument. |
| ScripName<br>STRING | - | This is the name of the instrument in the position. |
| SellAvgRate<br>DOUBLE | - | This is average rate for selling the instrument on the day. |
| SellQty<br>INTEGER | - | This is the total quantity of the instrument sold on the day. |
| SellValue<br>DOUBLE | - | This is total value of the instrument sold. |

### SAMPLE SUCCESS RESPONSE

```json
{
    "body": {
        "Message": "",
        "NetPositionDetail": [
            {
                "BODPositionPrice": 809.2514,
                "BodQty": 5,
                "BookedPL": 0,
                "BuyAvgRate": 0,
                "BuyQty": 0,
                "BuyValue": 0,
                "Exch": "N",
                "ExchType": "C",
                "LTP": 818.6,
                "MTOM": 46.743,
                "Multiplier": 1,
                "NetQty": 5,
                "OrderFor": "D",
                "PreviousClose": 814.6,
                "ScripCode": 4963,
                "ScripName": "ICICIBANK",
                "SellAvgRate": 0,
                "SellQty": 0,
                "SellValue": 0
            },
            {
                "BODPositionPrice": 91.1505,
                "BodQty": 0,
                "BookedPL": 0,
                "BuyAvgRate": 0,
                "BuyQty": 0,
                "BuyValue": 0,
                "Exch": "N",
                "ExchType": "C",
                "LTP": 107.6,
                "MTOM": 0,
                "Multiplier": 1,
                "NetQty": 0,
                "OrderFor": "D",
                "PreviousClose": 100.35,
                "ScripCode": 3499,
                "ScripName": "TATASTEEL",
                "SellAvgRate": 0,
                "SellQty": 0,
                "SellValue": 0
            }
        ],
        "Status": 0
    },
    "head": {
        "responseCode": "IIFLMarRQNPNWV2",
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
        "Message": "Invalid Session",
        "NetPositionDetail": [],
        "Status": 9
    },
    "head": {
        "responseCode": "IIFLMarRQNPNWV2",
        "status": "0",
        "statusDescription": "Invalid Session"
    }
}
```

### SAMPLE FAILURE RESPONSE

Failure when head parameters are wrong

```json
{
    "body": null,
    "head": {
        "responseCode": "IIFLMarRQNPNWV2",
        "status": "2",
        "statusDescription": "Invalid head parameters."
    }
}
```

---

## EDIS

> Source: https://xstream.5paisa.com/dev-docs/portfolio-management-system/edis

**Type:** Rest API · **Method:** POST

To sell a stock in your DMAT account you need to complete EDIS process. We are offering this through API.

To sell a stock in your DMAT account you need to complete EDIS process. We are offering this through API.

Process for EDIS-

1. Create .html file with form data with the required fields. Sample file format is mentioned below.

2. Open the HTML file in browser and complete Sell authorization process.

### REQUEST URL

```
https://dev-openapi.5paisa.com/WebVendorLogin/EDISAuthorization/Authorization
```

### Request body

| FIELD NAME | MANDATORY | DESCRIPTION |
|---|---|---|
| Access Token<br>STRING | Yes | Access Token of Client. |
| Clientcode<br>STRING | Yes | 5paisa demat account client code of the user in plain text. |
| VednorKey<br>STRING | Yes | AppKey of user or partner. |
| ResponseURL<br>STRING | Yes | The Callback URL where customer will be redirected after successful sell authorization. |

### SAMPLE REQUEST BODY

**JSON**

```json
<form name= "VEdisForm" method = "post"
action="https://dev-openapi.5paisa.com/WebVendorLogin/EDISAuthorization/Authorization" >
<input type= "hidden" name= "AccessToken" value= "{Access Token}"/>
<input type= "hidden" name= "ClientCode" value="{client_code}" />
<input type= "hidden" name= "VendorKey" value="{Your Vendor/User Key}" />
<input type= "hidden" name= "ResponseURL" value="{Your Redirect URL e.g.https://google.com}" />
<div>
<button>Authorize</button>
</div>
</form>
```
