# Market Data System - REST APIs

Snapshot and historical market data over REST.

## Contents

- [Market Feed](#market-feed)
- [Market Snapshot (Quotes)](#market-snapshot-quotes)
- [Market Depth](#market-depth)
- [Historical Candles](#historical-candles)

---

## Market Feed

> Source: https://xstream.5paisa.com/dev-docs/market-data-system/market-feed

**Type:** Rest API · **Method:** POST

The API provides live OHLC and volume data of any set of instruments.

This API is used to fetch the market feed of a particular scrip or a set of scrips.

The response of the API consists of an details like LTP, High, Low, Previous Close of the requested scrips. The response also consists of status and messages to be delivered as per status of execution of the API.

> **Note**
> Either ScripCode or ScripData can be used to fetch market data, with priority given to ScripCode. If the ScripCode value is present, the API response will be for the specified ScripCode

### REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V1/MarketFeed
```

### Headers

| KEY | VALUE |
|---|---|
| Content-Type | application/json |
| Authorization | bearer {Your Access Token} |

### Request body

| FIELD NAME |  | MANDATORY | DESCRIPTION |
|---|---|---|---|
| head | key<br>STRING | Yes | AppKey of User or Partner |
| body | ClientCode<br>STRING | Yes | 5paisa demat account client code of the user. |
| body | MarketFeedData<br>ARRAY | Yes | An array consisting of details (exchange, exchange segment , scrip code or scrip Data) of all the instruments for which live feed is required. |

### MarketFeedData

| FIELD NAME | MANDATORY | DESCRIPTION |
|---|---|---|
| Exch<br>STRING | Yes | This is the exchange of the instrument.<br>N: NSE<br>B: BSE<br>M: MCX |
| ExchType<br>STRING | Yes | It specifies the exchange segment of the instrument.<br>C: Cash<br>D: Derivatives (FnO for NSE, BSE & MCX)<br>U: Currency Derivatives |
| ScripCode<br>STRING | Optional | This is the unique code for the instrument. Can be skipped or passed as 0 if ScripData is to be used. |
| ScripData<br>STRING | Optional | This is the unique Scrip Data for the instrument. Can be skipped or passed as Blank("") if ScripCode is to be used. |

### SAMPLE REQUEST BODY

**JSON**

```json
{
    "head": {
        "key": "{{Your App Key}}"
    },
    "body": {
        "MarketFeedData": [
            {
                "Exch": "N",
                "ExchType": "C",
                "ScripCode": "2885",
                "ScripData": ""
            },
            {
                "Exch": "N",
                "ExchType": "C",
                "ScripData": "ITC_EQ"
            }
        ],
        "LastRequestTime": "/Date(0)/",
        "RefreshRate": "H"
    }
}
```

**cURL**

```bash
curl --location 'https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V1/MarketFeed' \
--header 'Content-Type: application/json' \
--data '{
    "head": {
        "key": "{Your App Key}"
    },
    "body": {
        "MarketFeedData": [
            {
                "Exch": "N",
                "ExchType": "C",
                "ScripCode": "2885",
                "ScripData": ""
            },
            {
                "Exch": "N",
                "ExchType": "C",
                "ScripData": "ITC_EQ"
            }
        ],
        "LastRequestTime": "/Date(0)/",
        "RefreshRate": "H"
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

req_list_ = [{"Exch": "N", "ExchType": "C", "ScripData": "ITC_EQ"}]
              {"Exch": "N", "ExchType": "C", "ScripCode": "2885"}]

print(client.fetch_market_feed_scrip(req_list_))
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
| head | responseCode<br>STRING | 5PMFV1 | This is the unique response code for the API. |
| head | status<br>STRING | 0: Success<br>2: Invalid head parameters. | This is the status code which depicts the status of API request to the server. |
| head | statusDescription<br>STRING | Success<br>Invalid head parameters. | This is the description of the status received from the server for the API request. |
| body | CacheTime<br>INTEGER | - | It provides total cache time for the tick data. |
| body | Data<br>ARRAY | - | It provides the OHLC and volume data for the requested scrips. |
| body | Message<br>STRING | - | This is the description of <br>the status of API request |
| body | Status<br>INTEGER | - | This is the numeric code<br>for the status of API <br>request |
| body | TimeStamp<br>DATETIME | - | This is the time stamp of the tick data. |

### Data

| FIELD NAME | VALUES | DESCRIPTION |
|---|---|---|
| Chg<br>DOUBLE | - | This is Points change between Previous Close and LTP. |
| ChgPcnt<br>DOUBLE | - | This is Percentage change between Previous Close and LTP. |
| Exch<br>STRING | N: NSE<br>B: BSE<br>M:MCX | This is the exchange of the instrument. |
| ExchType<br>STRING | C: Cash<br>D: Derivatives (FnO for NSE, BSE & MCX)<br>U: Currency | This specifies the exchange segment of the instrument. |
| High<br>DOUBLE | - | This is the high rate for the day of the instrument. |
| LastRate<br>DOUBLE | - | This is the last rate for the instrument. |
| Low<br>DOUBLE | - | It provides the low rate for the day for the instrument. |
| Message<br>STRING | - | This is the description of <br>the status of data request |
| PClose<br>DOUBLE | - | This is the previous close rate for the instrument. |
| Status<br>INTEGER | 0<br>2 | This is the status of the data request through the API. |
| TickDt<br>DATETIME | - | This is the time stamp of the tick data. |
| Time<br>INTEGER | - | - |
| Token<br>INTEGER | - | This is the unique scrip code for the instrument. |
| TotalQty<br>INTEGER | - | This is the total quantity or volume trading on the day. |

### SAMPLE SUCCESS RESPONSE

SAMPLE SUCCESS RESPONSE

```json
{
   "body": {
       "CacheTime": 5,
       "Data": [
           {
               "Chg": 62.1,
               "ChgPcnt": 2.18,
               "Exch": "N",
               "ExchType": "C",
               "High": 2949.8,
               "LastRate": 2915.4,
               "Low": 2866.35,
               "PClose": 2853.3,
               "Symbol": "RELIANCE",
               "TickDt": "/Date(1706956047000+0530)/",
               "Time": 35847,
               "Token": 2885,
               "TotalQty": 0
           },
           {
               "Chg": -2.8,
               "ChgPcnt": -0.63,
               "Exch": "N",
               "ExchType": "C",
               "High": 447.2,
               "LastRate": 440.1,
               "Low": 439.5,
               "PClose": 442.9,
               "Symbol": "ITC",
               "TickDt": "/Date(1706956150000+0530)/",
               "Time": 35950,
               "Token": 1660,
               "TotalQty": 0
           }
       ],
       "Message": "Success",
       "Status": 0,
       "TimeStamp": "/Date(1707038151652+0530)/"
   },
   "head": {
       "responseCode": "5PMFV1",
       "status": "0",
       "statusDescription": "Success"
   }
}
```

### SAMPLE FAILURE RESPONSE:

Failure when scripCode is passed as blank

```json
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
   <title>Request Error</title>
   <style>BODY { color: #000000; background-color: white; font-family: Verdana; margin-left: 0px; margin-top: 0px;
} #content { margin-left: 30px; font-size: .70em; padding-bottom: 2em;
} A:link { color: #336699; font-weight: bold; text-decoration: underline;
} A:visited { color: #6699cc; font-weight: bold; text-decoration: underline;
} A:active { color: #336699; font-weight: bold; text-decoration: underline;
} .heading1 { background-color: #003366; border-bottom: #336699 6px solid; color: #ffffff; font-family: Tahoma; font-size: 26px; font-weight: normal;margin: 0em 0em 10px -20px; padding-bottom: 8px; padding-left: 30px;padding-top: 16px;
} pre { font-size:small; background-color: #e5e5cc; padding: 5px; font-family: Courier New; margin-top: 0px; border: 1px #f0f0e0 solid; white-space: pre-wrap; white-space: -pre-wrap; word-wrap: break-word;
} table { border-collapse: collapse; border-spacing: 0px; font-family: Verdana;
} table th { border-right: 2px white solid; border-bottom: 2px white solid; font-weight: bold; background-color: #cecf9c;
} table td { border-right: 2px white solid; border-bottom: 2px white solid; background-color: #e5e5cc;
}</style>
 </head>
 <body>
   <div id="content">
     <p class="heading1">Request Error</p>
     <p>The server encountered an error processing the request. See server logs for more details.</p>
   </div>
 </body>
</html>
```

---

## Market Snapshot (Quotes)

> Source: https://xstream.5paisa.com/dev-docs/market-data-system/market-snapshot

**Type:** Rest API · **Method:** POST

The API provides live OHLC, Open Interest, 52 week high/low and volume data of any set of instruments.

This API is used to fetch the Full market snapshot of a particular scrip or a set of scrips. The response has all the details like LTP, High, Low, Previous Close , Open Interest, 52w High/Low and Volume of the requested scrips.

The input parameters include Client code and Scrip Request data consisting of Exchange, exchange type and scrip code or Scrip Data.

The response includes key metrics such as OHLC data , Total quantity , points and percentage change between ltp and previous close .

This feature is ideal for building dashboards, watchlists, and real-time trading tools, offering a complete view of market behavior for selected instruments.

> **Note**
> Either ScripCode or ScripData can be used to fetch market snapshot, with priority given to ScripCode. If the ScripCode value is present, the API response will be for the specified ScripCode.

### REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/MarketSnapshot
```

### Headers

| KEY | VALUE |
|---|---|
| Content-Type | application/json |
| Authorization | bearer {Your Access Token} |

### Request body

| FIELD NAME |  | MANDATORY | DESCRIPTION |
|---|---|---|---|
| head | key<br>STRING | Yes | AppKey of User or Partner |
| body | ClientCode<br>STRING | Yes | 5paisa demat account client code of the user. |
| body | Data<br>ARRAY | Yes | An array consisting of details (exchange, exchange segment , scrip code or scrip Data) of all the instruments for which live feed is required. |

### Data

| FIELD NAME | MANDATORY | DESCRIPTION |
|---|---|---|
| Exch<br>STRING | Yes | This is the exchange of the instrument.<br>N: NSE<br>B: BSE<br>M: MCX |
| ExchType<br>STRING | Yes | It specifies the exchange segment of the instrument.<br>C: Cash<br>D: Derivatives (FnO for NSE, BSE & MCX)<br>U: Currency Derivatives |
| ScripCode<br>STRING | Optional | This is the unique code for the instrument. Can be skipped or passed as 0 if ScripData is to be used. |
| ScripData<br>STRING | Optional | This is the unique Scrip Data for the instrument. Can be skipped or passed as Blank("") if ScripCode is to be used. |

### SAMPLE REQUEST BODY

**JSON**

```json
{
    "head": {
        "key": "{{Your App Key}}"
    },
    "body": {
        "ClientCode": "{{clientcode}}",
        "Data": [
            {
                "Exchange": "N",
                "ExchangeType": "D",
                "ScripCode": "51409",
                "ScripData": ""
            },
            {
                "Exchange": "N",
                "ExchangeType": "C",
                "ScripCode": "0",
                "ScripData": "ITC_EQ"
            }
        ]
    }
}
```

**cURL**

```bash
curl --location --request POST 'https://Openapi.5paisa.com/VendorsAPI/Service1.svc/MarketSnapshot' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "head": {
        "key": "{{Your App Key}}"
    },
    "body": {
        "ClientCode": "{client_code}",
        "Data": [
            {
                "Exchange": "N",
                "ExchangeType": "D",
                "ScripCode": "51409",
                "ScripData": ""
            },
            {
                "Exchange": "N",
                "ExchangeType": "C",
                "ScripCode": "0",
                "ScripData": "ITC_EQ"
            }
        ]
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

a=[{"Exchange":"N","ExchangeType":"C","ScripCode":"2885"},
   {"Exchange":"N","ExchangeType":"C","ScripData":"ITC_EQ"},
   ]
print(client.fetch_market_snapshot(a))
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
| head | responseCode<br>STRING | 5PMFV1 | This is the unique response code for the API. |
| head | status<br>STRING | 0: Success<br>2: Invalid head parameters. | This is the status code which depicts the status of API request to the server. |
| head | statusDescription<br>STRING | Success<br>Invalid head parameters. | This is the description of the status received from the server for the API request. |
| body | CacheTime<br>INTEGER | - | It provides total cache time for the tick data. |
| body | Data<br>ARRAY | - | It provides the OHLC and volume data for the requested scrips. |
| body | Message<br>STRING | - | This is the description of <br>the status of API request |
| body | Status<br>INTEGER | - | This is the numeric code<br>for the status of API <br>request |
| body | TimeStamp<br>DATETIME | - | This is the time stamp of the tick data. |

### Data

| FIELD NAME | VALUES | DESCRIPTION |
|---|---|---|
| Chg<br>DOUBLE | - | This is Points change between Previous Close and LTP. |
| ChgPcnt<br>DOUBLE | - | This is Percentage change between Previous Close and LTP. |
| Exch<br>STRING | N: NSE<br>B: BSE<br>M:MCX | This is the exchange of the instrument. |
| ExchType<br>STRING | C: Cash<br>D: Derivatives (FnO for NSE, BSE & MCX)<br>U: Currency | This specifies the exchange segment of the instrument. |
| High<br>DOUBLE | - | This is the high rate for the day of the instrument. |
| LastRate<br>DOUBLE | - | This is the last rate for the instrument. |
| Low<br>DOUBLE | - | It provides the low rate for the day for the instrument. |
| Message<br>STRING | - | This is the description of <br>the status of data request |
| PClose<br>DOUBLE | - | This is the previous close rate for the instrument. |
| Status<br>INTEGER | 0<br>2 | This is the status of the data request through the API. |
| TickDt<br>DATETIME | - | This is the time stamp of the tick data. |
| Time<br>INTEGER | - | - |
| Token<br>INTEGER | - | This is the unique scrip code for the instrument. |
| TotalQty<br>INTEGER | - | This is the total quantity or volume trading on the day. |

### SAMPLE SUCCESS RESPONSE

SAMPLE SUCCESS RESPONSE

```json
{
   "body": {
       "CacheTime": 5,
       "Data": [
           {
               "Chg": 62.1,
               "ChgPcnt": 2.18,
               "Exch": "N",
               "ExchType": "C",
               "High": 2949.8,
               "LastRate": 2915.4,
               "Low": 2866.35,
               "PClose": 2853.3,
               "Symbol": "RELIANCE",
               "TickDt": "/Date(1706956047000+0530)/",
               "Time": 35847,
               "Token": 2885,
               "TotalQty": 0
           },
           {
               "Chg": -2.8,
               "ChgPcnt": -0.63,
               "Exch": "N",
               "ExchType": "C",
               "High": 447.2,
               "LastRate": 440.1,
               "Low": 439.5,
               "PClose": 442.9,
               "Symbol": "ITC",
               "TickDt": "/Date(1706956150000+0530)/",
               "Time": 35950,
               "Token": 1660,
               "TotalQty": 0
           }
       ],
       "Message": "Success",
       "Status": 0,
       "TimeStamp": "/Date(1707038151652+0530)/"
   },
   "head": {
       "responseCode": "5PMFV1",
       "status": "0",
       "statusDescription": "Success"
   }
}
```

### SAMPLE FAILURE RESPONSE

Failure when scripCode is passed as blank

```json
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
   <title>Request Error</title>
   <style>BODY { color: #000000; background-color: white; font-family: Verdana; margin-left: 0px; margin-top: 0px;
} #content { margin-left: 30px; font-size: .70em; padding-bottom: 2em;
} A:link { color: #336699; font-weight: bold; text-decoration: underline;
} A:visited { color: #6699cc; font-weight: bold; text-decoration: underline;
} A:active { color: #336699; font-weight: bold; text-decoration: underline;
} .heading1 { background-color: #003366; border-bottom: #336699 6px solid; color: #ffffff; font-family: Tahoma; font-size: 26px; font-weight: normal;margin: 0em 0em 10px -20px; padding-bottom: 8px; padding-left: 30px;padding-top: 16px;
} pre { font-size:small; background-color: #e5e5cc; padding: 5px; font-family: Courier New; margin-top: 0px; border: 1px #f0f0e0 solid; white-space: pre-wrap; white-space: -pre-wrap; word-wrap: break-word;
} table { border-collapse: collapse; border-spacing: 0px; font-family: Verdana;
} table th { border-right: 2px white solid; border-bottom: 2px white solid; font-weight: bold; background-color: #cecf9c;
} table td { border-right: 2px white solid; border-bottom: 2px white solid; background-color: #e5e5cc;
}</style>
 </head>
 <body>
   <div id="content">
     <p class="heading1">Request Error</p>
     <p>The server encountered an error processing the request. See server logs for more details.</p>
   </div>
 </body>
</html>
```

---

## Market Depth

> Source: https://xstream.5paisa.com/dev-docs/market-data-system/market-depth

**Type:** Rest API · **Method:** POST

The API provides live OHLC and volume data of any set of instruments.

The Market Depth API provides detailed insight into the order book of a particular trading instrument (scrip). It displays the best bid(here level 5) and ask prices along with their corresponding quantities and number of orders at each level.

This data helps traders assess liquidity, understand supply/demand zones, detect large orders, and make more informed decisions for entries, exits, and risk management.

This API is used to fetch the level 5 market Depth of a particular scrip.

Please note that the response of the API consists of details like Price , Quantity, No of Orders of the requested scrip.

The BbBuySellFlag is an interesting feature which indicates values for buy and sell : 66-Buy , 83 - Sell

### REQUEST URL

```
https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V2/MarketDepth
```

> **Note — Note**
> Either ScripCode or ScripData can be used to fetch market depth, with priority given to ScripCode. If the ScripCode value is present, the API response will be for the specified ScripCode

### Headers

| KEY | VALUE |
|---|---|
| Content-Type | application/json |
| Authorization | bearer {Your Access Token} |

### Request body

| FIELD NAME |  | MANDATORY | DESCRIPTION |
|---|---|---|---|
| head | key<br>STRING | Yes | AppKey of User or Partner |
| body | ClientCode<br>STRING | Yes | 5paisa demat account client code of the user. |
| body | Exch<br>STRING | Yes | This is the exchange of the instrument.<br>N: NSE<br>B: BSE<br>M: MCX |
|  | ExchType<br>STRING | Yes | It specifies the exchange segment of the instrument.<br>C: Cash<br>D: Derivatives (FnO for NSE, BSE & MCX)<br>U: Currency Derivatives |
|  | ScripCode<br>STRING | Optional | This is the unique code for the instrument. Can be skipped or passed as 0 if ScripData is to be used. |
|  | ScripData<br>STRING | Optional | This is the unique Scrip Data for the instrument. Can be skipped or passed as Blank("") if ScripCode is to be used. |

### SAMPLE REQUEST BODY

**JSON**

```json
{
    "head": {
        "key": "{{vendor_key}}"
    },
    "body": {
        "ClientCode": "{{clientcode}}",
         "Exchange":"N",
         "ExchangeType":"C",
         "ScripCode":2885,
         "ScripData":""
    }
}
```

**cURL**

```bash
curl --location 'https://Openapi.5paisa.com/VendorsAPI/Service1.svc/V2/MarketDepth' \
--header 'Content-Type: application/json' \
--data '{
    "head": {
        "key": "{Your App Key}"
    },
    "body": {
        "ClientCode": "{{clientcode}}",
         "Exchange":"N",
         "ExchangeType":"C",
         "ScripCode":2885,
         "ScripData":""
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

print(client.fetch_market_depth_by_scrip(Exchange="N",ExchangeType="C",ScripCode="1660"))
print(client.fetch_market_depth_by_scrip(Exchange="N",ExchangeType="C",ScripData="RELIANCE_EQ"))
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
| head | responseCode<br>STRING | 5PMDV2 | This is the unique response code for the API. |
| head | status<br>STRING | 0: Success<br>2: Invalid head parameters. | This is the status code which depicts the status of API request to the server. |
| head | statusDescription<br>STRING | Success<br>Invalid head parameters. | This is the description of the status received from the server for the API request. |
| body | CacheTime<br>INTEGER | - | It provides total cache time for the tick data. |
| body | Exch<br>STRING | N: NSE<br>B: BSE<br>M:MCX | This is the exchange of the instrument. |
| body | ExchType<br>STRING | C: Cash<br>D: Derivatives (FnO for NSE, BSE & MCX)<br>U: Currency | This specifies the exchange segment of the instrument. |
| body | MarketDepthData<br>ARRAY | - | It provides level 5 bid/ask market depth. |
| body | ScripCode<br>STRING | - | ScripCode code of the request scrip. |
| body | Message<br>STRING | - | This is the description of <br>the status of API request |
| body | Status<br>INTEGER | - | This is the numeric code<br>for the status of API <br>request |
| body | TimeStamp<br>DATETIME | - | This is the time stamp of the tick data. |

### Data

| FIELD NAME | VALUES | DESCRIPTION |
|---|---|---|
| BbBuySellFlag<br>DOUBLE | 66/83 | This is buy or sell Flag. 66 stands for Buy and 83 for sell. |
| NumberOfOrders<br>DOUBLE | - | Total orders available for buy/sell at above price level. |
| Price<br>DOUBLE | - | The price at each depth level. |
| Quantity<br>DOUBLE | - | Total quantity available for buy/sell at above price level. |

### SAMPLE SUCCESS RESPONSE

SAMPLE SUCCESS RESPONSE

```json
{
   "body": {
       "CacheTime": 5,
       "Exch": "N",
       "ExchType": "C",
       "MarketDepthData": [
           {
               "BbBuySellFlag": 66,
               "NumberOfOrders": 1,
               "Price": 2802.05,
               "Quantity": 212
           },
           {
               "BbBuySellFlag": 66,
               "NumberOfOrders": 1,
               "Price": 2802,
               "Quantity": 4
           },
           {
               "BbBuySellFlag": 66,
               "NumberOfOrders": 1,
               "Price": 2801.95,
               "Quantity": 1
           },
           {
               "BbBuySellFlag": 66,
               "NumberOfOrders": 1,
               "Price": 2801.85,
               "Quantity": 1
           },
           {
               "BbBuySellFlag": 66,
               "NumberOfOrders": 3,
               "Price": 2801.75,
               "Quantity": 9
           },
           {
               "BbBuySellFlag": 83,
               "NumberOfOrders": 2,
               "Price": 2803.65,
               "Quantity": 55
           },
           {
               "BbBuySellFlag": 83,
               "NumberOfOrders": 2,
               "Price": 2803.85,
               "Quantity": 54
           },
           {
               "BbBuySellFlag": 83,
               "NumberOfOrders": 2,
               "Price": 2803.9,
               "Quantity": 55
           },
           {
               "BbBuySellFlag": 83,
               "NumberOfOrders": 3,
               "Price": 2804,
               "Quantity": 147
           },
           {
               "BbBuySellFlag": 83,
               "NumberOfOrders": 1,
               "Price": 2804.6,
               "Quantity": 35
           }
       ],
       "Message": "Success",
       "ScripCode": 2885,
       "Status": 0,
       "TimeStamp": "/Date(1715594363000+0530)/"
   },
   "head": {
       "responseCode": "5PMDV2",
       "status": "0",
       "statusDescription": "Success"
   }
}
```

### SAMPLE FAILURE RESPONSE:

Failure when scripCode is passed as blank

```json
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
   <title>Request Error</title>
   <style>BODY { color: #000000; background-color: white; font-family: Verdana; margin-left: 0px; margin-top: 0px;
} #content { margin-left: 30px; font-size: .70em; padding-bottom: 2em;
} A:link { color: #336699; font-weight: bold; text-decoration: underline;
} A:visited { color: #6699cc; font-weight: bold; text-decoration: underline;
} A:active { color: #336699; font-weight: bold; text-decoration: underline;
} .heading1 { background-color: #003366; border-bottom: #336699 6px solid; color: #ffffff; font-family: Tahoma; font-size: 26px; font-weight: normal;margin: 0em 0em 10px -20px; padding-bottom: 8px; padding-left: 30px;padding-top: 16px;
} pre { font-size:small; background-color: #e5e5cc; padding: 5px; font-family: Courier New; margin-top: 0px; border: 1px #f0f0e0 solid; white-space: pre-wrap; white-space: -pre-wrap; word-wrap: break-word;
} table { border-collapse: collapse; border-spacing: 0px; font-family: Verdana;
} table th { border-right: 2px white solid; border-bottom: 2px white solid; font-weight: bold; background-color: #cecf9c;
} table td { border-right: 2px white solid; border-bottom: 2px white solid; background-color: #e5e5cc;
}</style>
 </head>
 <body>
   <div id="content">
     <p class="heading1">Request Error</p>
     <p>The server encountered an error processing the request. See server logs for more details.</p>
   </div>
 </body>
</html>
```

---

## Historical Candles

> Source: https://xstream.5paisa.com/dev-docs/market-data-system/historical-candles

**Type:** Rest API · **Method:** POST

The API provides historical OHLC and volume data of any instrument of NSE, BSE, MCX and NCDEX.

**Purpose of the API:** To provide historical candle data for various scrip codes for the purpose of strategy deployment.

**Authentication:** Requires clients to log in, and upon successful login, a token is generated in the response. This token needs to be validated using a JWT validation API.

**Data Provided:**

- **OHLC Data:** Open, high, low, and close rates.
- **Volume Data:** Information about the trading volume.
- **Timestamps:** Time information associated with the provided data.

**Interval Size:**

- **Maximum Permissible Interval Size:** 6 months.
- **Day Wise Data:** No restrictions on the size of the interval; maximum data can be fetched when the interval is a day.

**Supported Intervals:**

- 1 minute
- 5 minutes
- 10 minutes
- 15 minutes
- 30 minutes
- 60 minutes
- Day-based interval

**Note:** The API allows fetching data for any time duration within the specified interval limits.

### REQUEST URL

```
https://openapi.5paisa.com/V2/historical/N/C/1630/1d?from={FromDate}&end={EndDate}
```

### Headers

| KEY | VALUE |
|---|---|
| Content-Type | application/json |
| Authorization | bearer {Your Access Token} |

### URL Parameters

| FIELD NAME | MANDATORY | DESCRIPTION |
|---|---|---|
| Exch<br>STRING | Yes | This indicates the exchange name of the instrument.<br>N: NSE<br>B: BSE<br>M: MCX<br>n: NCDEX (If exchange type is ‘X’) |
| ExchType<br>STRING | Yes | It specifies the exchange segment of the instrument.<br>c: Cash<br>d: Derivatives (FnO for NSE, BSE & MCX)<br>u: Currency Derivatives<br>x: NCDEX Commodity<br>y: NSE & BSE Commodity |
| ScripCode<br>STRING | Yes | This is the unique numerical code defined for the instrument.<br>It can be fetched from the scripmaster. |
| Interval<br>STRING | Yes | Interval range for the candles.<br>1m: 1 minute<br>5m: 5 minute<br>10m: 10 minute<br>15m: 15 minute<br>30m: 30 minute<br>60m: 60 minute<br>1d: 1 day |
| FromDate<br>DATETIME | Yes | Date from which candle data needs to be fetched (Format: YYYY-MM-DD) |
| EndDate<br>DATETIME | Yes | Date to which candle data needs to be fetched (Format: YYYY-MM-DD) |

### SAMPLE REQUEST URL

```
https://openapi.5paisa.com/V2/historical/N/C/1630/1d?from=2023-02-23&end=2023-04-23
```

### SAMPLE REQUEST BODY

**cURL**

```bash
curl --location 'https://openapi.5paisa.com/V2/historical/N/C/1630/1d?from=2023-02-23&end=2023-04-23' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjUwMDUyNzcwIiwicm9sZSI6IjEwMzQ1IiwiU3RhdGUiOiIiLCJSZWRpcmVjdFNlcnZlciI6IkEiLCJuYmYiOjE3MDU1MDE1NjUsImV4cCI6MTcwNTUxNjE5OSwiaWF0IjoxNzA1NTAxNTY1fQ.4Tr9txu_Wowf-AXmTD2yAm98d3TZl5KgKFOFEE6EMco' \
--header 'Cookie: 5paisacookie=ysri4csgzdpr0vqhr45qq4gk' \
--data ''
```

**Python**

```python
req_list=[
            { "Exch":"N","ExchType":"C","ScripCode":1660},
            ]

req_data=client.Request_Feed('mf','s',req_list)
def on_message(ws, message):
    print(message)

client.connect(req_data)

client.receive_data(on_message)
```

**JAVA**

```java
Unirest.setTimeouts(0, 0);
HttpResponse<String> response = Unirest.get("https://dataservice.iifl.in/openapi/prod/historical/n/c/1660/1d?from=2022-02-01&end=2022-02-21")
  .header("x-clientcode", "CLIENT_CODE")
  .header("x-auth-token", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik1BWUFOQ0hJIiwicm9sZSI6IjYwIiwibmJmIjoxNjQ1NDQ1MDY3LCJleHAiOjE2NDU0NDY4NjcsImlhdCI6MTY0NTQ0NTA2N30.K7vrOlJCzBy_wuXVLl1EXN7QCFQ9NldrfAFMIogAjf8")
  .header("Ocp-Apim-Subscription-Key", " fc714d8e5b82438a93a95baa493ff45b")
  .asString();
```

**C#**

```csharp
var client = new RestClient("https://dataservice.iifl.in/openapi/prod/historical/n/c/1660/1d?from=2022-02-01&end=2022-02-21");
client.Timeout = -1;
var request = new RestRequest(Method.GET);
request.AddHeader("x-clientcode", "CLIENT_CODE");
request.AddHeader("x-auth-token", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6Ik1BWUFOQ0hJIiwicm9sZSI6IjYwIiwibmJmIjoxNjQ1NDQ1MDY3LCJleHAiOjE2NDU0NDY4NjcsImlhdCI6MTY0NTQ0NTA2N30.K7vrOlJCzBy_wuXVLl1EXN7QCFQ9NldrfAFMIogAjf8");
request.AddHeader("Ocp-Apim-Subscription-Key", " fc714d8e5b82438a93a95baa493ff45b");
IRestResponse response = client.Execute(request);
Console.WriteLine(response.Content);
```

### Response Body

| FIELD NAME |  | VALUES | DESCRIPTION |
|---|---|---|---|
| status<br>STRING |  | success | This is the status description of the API call. |
| data | candles<br>ARRAY |  | It provides open, high, close and low rates along with the timestamp for each candle in an array. |

### Response Body - candles

| FIELD NAME | VALUES | DESCRIPTION |
|---|---|---|
| Timestamp<br>DATETIME | - | This is the timestamp of the candle in the format of YYYY-MM-DDTHH:MM:SS |
| Open<br>DOUBLE | - | This is the open rate at given time stamp of the candle |
| High<br>DOUBLE | - | This is the high rate at given time stamp of the candle |
| Low<br>DOUBLE | - | This is the low rate at given time stamp of the candle |
| Close<br>DOUBLE | - | This is the close rate at given time stamp of the candle |
| Volume<br>INTEGER | - | This is the volume at given time stamp of the candle |

### SAMPLE SUCCESS RESPONSE

```json
{
    "status": "success",
    "data": {
        "candles": [
            [
                "2022-07-15T00:00:00",
                292.0,
                294.0,
                289.5,
                293.55,
                11025420
            ],
            [
                "2022-07-18T00:00:00",
                295.0,
                296.3,
                293.75,
                295.3,
                11315876
            ],
            [
                "2022-07-19T09:15:00",
                295.2,
                295.6,
                292.7,
                294.45,
                9149737
            ]
        ]
    }
}
```

### SAMPLE FAILURE RESPONSE:

Failure due to wrong client code or JWT passed in the headers

```json
{
    "head": {
        "ResponseCode": "RPOpenAPI",
        "Status": 1,
        "Status_description": "Error While Processing"
    },
    "body": null
}
```
