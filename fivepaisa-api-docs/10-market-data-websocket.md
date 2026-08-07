# Market Data System - WebSocket

Streaming market data: the main market feed socket, option Greeks and the 20-level depth feed.

## Contents

- [Web Socket](#web-socket)
- [Options Greeks](#options-greeks)
- [20-Market Depth](#20-market-depth)

---

## Web Socket

> Source: https://xstream.5paisa.com/dev-docs/market-data-system/web-socket

**Type:** Rest API · **Method:** POST

The web socket provides the live streaming of open, high, low and close rates, volume being traded and market depth along with order confirmation.

Whether it is fetching market data or trade confirmations, live streaming support can make the life of traders and investors easy. Web socket helps the clients to integrate live streaming functionality of the market data as well as order and trade confirmations. It can be easily integrated on any kind of application and works in an authenticated environment .

The consumption of web socket requires client to first connect it to the server and then subscribe to the type of data he or she wants to fetch. The connection request requires access token and client code as a query parameters, which is received in the response of the get access token API. After successful connection, users can subscribe or unsubscribe to different types of live streaming by sending respective requests.

### CONNECTION URL

```
wss://openfeed.5paisa.com/feeds/api/chat?Value1={{access_token}}|{{clientcode}}
```

### URL Query Parametrs

| PARAMETER NAME | MANDATORY | DESCRIPTION |
|---|---|---|
| access_token<br>STRING | Yes | Access token received in the response of login API |
| clientcode<br>STRING | Yes | Demat account client code of the client in plain text |

### SAMPLE CONNECTION URL

```
https://openfeed.5paisa.com/feeds/api/chat?Value1=eyJhbGciOiJIUzI1NiIsInR5cCI6IkXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjwMDUyNzcwIiwicm9sSI6IjEwMzQ1IiwiU3RhdGiOiIiLCJSZWRpcmVjdFNlcnZlciI6IkEiLCJuYmYiOjE3MDY5Og2NTUsImV4cCI6MTcwNzA3MTM5OSwiaWF0IjoxNz2OTk4NjU1fQ.TNCMKL4Vd09D3Z0X77zc6PTe7RRBWDD367v_ZHco0|50011110
```

### Subscription Requests

| PARAMETER NAME | MANDATORY | DESCRIPTION |
|---|---|---|
| Method<br>STRING | Yes | It represents code for the type of data client wants to fetch.<br>MarketFeedV3<br>MarketDepthService GetScripInfoForFuture OrderTradeConfirmations |
| Operation<br>STRING | Yes | It specifies if the request is for subscribing or unsubscribing the data feed.<br>Subscribe<br>Unsubscribe |
| ClientCode<br>STRING | Yes | Demat account client code of the client in plain text |
| MarketFeedData<br>ARRAY | Only for methods: MarketFeedV3 MarketDepthService GetScripInfoForFuture(OI) Indices | It contains an array of details of instruments for which live data streaming needs to be subscribed or unsubscribed |

### MarketFeedData

| FIELD NAME | MANDATORY | DESCRIPTION |
|---|---|---|
| Exch<br>STRING | Yes | This is the exchange of the instrument<br>N :- NSE<br>B :- BSE<br>M :- MCX |
| ExchType<br>STRING | Yes | This is the exchange segment of the instrument<br>C :- Cash<br>D :- Derivatives<br>U :- Currency |
| ScripCode<br>INTEGER | Yes | This is the unique code for the instrument |

> **Note — NOTE**
> The details of exchange, exchange type and scrip code for any instrument can be found from the [Scrip master.](https://xstream.5paisa.com/dev-docs/docFundamentals/scrip-master)

### Method

#### MarketFeedV3

##### SAMPLE REQUEST : Subscribe

**JSON**

```json
{"Method":"MarketFeedV3","Operation":"Subscribe", "ClientCode":"{clientcode}","MarketFeedData":[ {"Exch":"N","ExchType":"C","ScripCode":1660} ]}
```

##### SAMPLE REQUEST : UnSubscribe

**JSON**

```json
{"Method":"MarketFeedV3","Operation":"Unsubscribe", "ClientCode":"50052770","MarketFeedData":[ {"Exch":"N","ExchType":"C","ScripCode":1660} ]}
```

##### Response body

| PARAMETER NAME | LIST OF VALUES | DESCRIPTION |
|---|---|---|
| Exch<br>STRING | N<br>B<br>M | This is the exchange of the instrument |
| ExchType<br>STRING | C<br>D<br>U | This is the exchange segment of the instrument |
| Token<br>INTEGER | - | This is the unique scrip code for the instrument |
| LastRate<br>DOUBLE | - | This is the last traded rate for the instrument |
| LastQty<br>INTEGER | - | This is the last traded quantity for the instrument |
| TotalQty<br>INTEGER | - | This is the total traded quantity for the instrument |
| High<br>DOUBLE | - | This is the highest price of the day for the <br>instrument |
| Low<br>DOUBLE | - | This is the lowest price of the day for the <br>instrument |
| OpenRate<br>DOUBLE | - | This is the open price rate of the instrument |
| PClose<br>DOUBLE | - | This is the close price rate of the instrument |
| AvgRate<br>DOUBLE | - | This is the average traded price of the day <br>for the instrument |
| Time<br>INTEGER | - | - |
| BidQty<br>INTEGER | - | This is the last bid quantity for the instrument |
| BidRate<br>DOUBLE | - | This is the last bid rate for the instrument |
| OffQty<br>INTEGER | - | This is the last ask quantity for the instrument |
| OffRate<br>DOUBLE | - | This is the last bid rate for the instrument |
| TBidQ<br>INTEGER | - | This is the total bid quantity of the day for the <br>instrument |
| TOffQ<br>INTEGER | - | This is the total ask quantity of the day for the<br>instrument |
| TickDt<br>DATETIME | - | This is the timestamp in epoch format at which <br>feed is fetched |

##### SAMPLE RESPONSE

```json
[
   {
       "Exch": "N",
       "ExchType": "C",
       "Token": 1660,
       "LastRate": 440.1,
       "LastQty": 0,
       "TotalQty": 0,
       "High": 447.2,
       "Low": 439.5,
       "OpenRate": 445,
       "PClose": 442.9,
       "AvgRate": 0,
       "Time": 35950,
       "BidQty": 0,
       "BidRate": 0,
       "OffQty": 0,
       "OffRate": 0,
       "TBidQ": 0,
       "TOffQ": 0,
       "TickDt": "\/Date(-62135596800000)\/",
       "ChgPcnt": -0.6321969
   }
]
```

#### MarketDepthService

##### SAMPLE REQUEST : Subscribe

**JSON**

```json
{"Method":"MarketDepthService","Operation":"Subscribe","ClientCode":
"{clientcode}","MarketFeedData":[
{ "Exch":"N","ExchType":"C","ScripCode":2885}]}
```

##### SAMPLE REQUEST : UnSubscribe

**JSON**

```json
{"Method":"MarketDepthService","Operation":"Unsubscribe","ClientCode":
"{clientcode}","MarketFeedData":[
{ "Exch":"N","ExchType":"C","ScripCode":2885}]}
```

##### Response body

| PARAMETER NAME | LIST OF VALUES | DESCRIPTION |
|---|---|---|
| Exch<br>STRING | N<br>B<br>M | This is the exchange of the instrument |
| ExchType<br>STRING | C<br>D<br>U | This is the exchange segment of the instrument |
| Token<br>INTEGER | - | This is the unique scrip code for the instrument |
| TBidQ<br>INTEGER | - | This is the total bid quantity of the day for the <br>instrument |
| TOffQ<br>INTEGER | - | This is the total ask quantity of the day for the<br>instrument |
| Details<br>ARRAY | - | This is the array containing details of the market depth of the instrument |
| Time<br>DATETIME | - | This is the timestamp in epoch format at which feed is fetched |

##### Details

| PARAMETER NAME | LIST OF VALUES | DESCRIPTION |
|---|---|---|
| Quantity<br>INTEGER | - | This is the quantity traded |
| Price<br>DOUBLE | - | This is the price at which orders are placed |
| NumberOfOrders<br>INTEGER | - | This is the number of orders placed |
| BbBuySellFlag<br>INTEGER | - | - |

> **Note — NOTE**
> In the market depth data array “Details”, top 5 elements of the array are for the best bids and last 5 are for the best asks.

##### SAMPLE RESPONSE

```json
{"Exch":"N","ExchType":"D","Token":71319,"TBidQ":86225,"TOffQ":135100,
"Details":[
{"Quantity":50,"Price":34925.65,"NumberOfOrders":2,"BbBuySellFlag":66},
{"Quantity":75,"Price":34925.6,"NumberOfOrders":2,"BbBuySellFlag":66},
{"Quantity":25,"Price":34925.55,"NumberOfOrders":1,"BbBuySellFlag":66},
{"Quantity":50,"Price":34925.5,"NumberOfOrders":2,"BbBuySellFlag":66},
{"Quantity":25,"Price":34925.4,"NumberOfOrders":1,"BbBuySellFlag":66},
{"Quantity":25,"Price":34932.1,"NumberOfOrders":1,"BbBuySellFlag":83},
{"Quantity":25,"Price":34932.15,"NumberOfOrders":1,"BbBuySellFlag":83},
{"Quantity":75,"Price":34932.95,"NumberOfOrders":1,"BbBuySellFlag":83},
{"Quantity":50,"Price":34933,"NumberOfOrders":1,"BbBuySellFlag":83},
{"Quantity":25,"Price":34933.15,"NumberOfOrders":1,"BbBuySellFlag":83}],
"TimeStamp":0,"Time":"\/Date(1640148238196)\/"}
```

#### GetScripInfoForFuture(Open Interest)

##### SAMPLE REQUEST : Subscribe

**JSON**

```json
{"Method":"GetScripInfoForFuture","Operation":"Subscribe","ClientCode": " {clientcode} ","MarketFeedData":[
{ "Exch":"N","ExchType":"D","ScripCode":48508}]}
```

##### SAMPLE REQUEST : UnSubscribe

**JSON**

```json
{"Method":"GetScripInfoForFuture","Operation":"Unsubscribe","ClientCode": " clientcode ","MarketFeedData":[
{ "Exch":"N","ExchType":"D","ScripCode":48508}]}
```

##### Response body

| PARAMETER NAME | LIST OF VALUES | DESCRIPTION |
|---|---|---|
| Exch<br>STRING | N<br>B<br>M | This is the exchange of the instrument |
| ExchType<br>STRING | C<br>D<br>U | This is the exchange segment of the instrument |
| Token<br>INTEGER | - | This is the unique scrip code for the instrument |
| OpenInterest<br>INTEGER | - | This is the open interest for the instrument. |
| DayHiOI<br>INTEGER | - | This is the highest open interest of the day for the instrument |
| DayLoOI<br>INTEGER | - | This is the lowest open interest of the day for the instrument |

##### SAMPLE RESPONSE

```json
{"Exch":"N","ExchType":"D","Token":71319,"OpenInterest":2388700,"DayHiOI":2388700,"DayLoOI":2345100}
```

#### OrderTradeConfirmations

##### SAMPLE REQUEST : Subscribe

**JSON**

```json
{"Method":"OrderTradeConfirmations","Operation":"Subscribe","ClientCode":"CLIENT_CODE"}
```

##### SAMPLE REQUEST: Unsubscribe

**JSON**

```json
{"Method":"OrderTradeConfirmations","Operation":"Unsubscribe","ClientCode":" CLIENT_CODE "}
```

##### Response body

| PARAMETER NAME | LIST OF VALUES | DESCRIPTION |
|---|---|---|
| ClientCode<br>STRING | - | 5Paisa demat account client code of the client in plain text |
| Exch<br>STRING | N:NSE<br>B:NSE | This is the exchange of the instrument |
| ExchType<br>STRING | C:Cash<br>D:Derivatives | This is the exchange segment of the instrument |
| BrokerOrderID<br>INTEGER | - | This is the order ID generated by 5paisa. |
| ExchangeOrderID<br>STRING | - | This is the order ID generated by the exchange |
| ScripCode<br>INTEGER | - | This is the unique scrip code for the instrument |
| Price<br>DOUBLE | - | This is the price at which order is placed |
| Qty<br>INTEGER | - | This is the quantity for which order is placed |
| BuySell<br>STRING | B: Buy<br>S: Sell | This specifies if the order is of buy or sell type. |
| ReqType<br>STRING | P: Place<br>M: Modify<br>C: Cancel<br>T: Trade<br>S: Stop Loss Trigeer | This specifies if the request is for placing, cancelling or modifying the order |
| ReqStatus<br>INTEGER | 0: Success<br>1: Failure | This is the status code for the order |

##### SAMPLE RESPONSE

Place

```json
{"ReqType":"P","ClientCode":"CLIENT_CODE","Exch":"N","ExchType":"C","ScripCode":1660,"Symbol":"ITC","Series":"EQ","BrokerOrderID":132038757,"ExchOrderID":"1200010221327930","ExchOrderTime":"2024-05-09 11:28:22","BuySell":"B","Qty":1,"Price":425,"ReqStatus":0,"Status":"Placed","OrderRequestorCode":"CLIENT_CODE","AtMarket":"N","Product":"D","WithSL":"N","SLTriggerRate":0,"DisclosedQty":0,"PendingQty":1,"TradedQty":0,"RemoteOrderId":"202405091128221","Remark":""}
```

##### SAMPLE RESPONSE

Modify

```json
{"ReqType":"M","ClientCode":"CLIENT_CODE","Exch":"N","ExchType":"C","ScripCode":1660,"Symbol":"ITC","Series":"EQ","BrokerOrderID":132029886,"ExchOrderID":"1100030061127930","ExchOrderTime":"2024-05-09 11:32:34","BuySell":"B","Qty":1,"Price":0,"ReqStatus":0,"Status":"Modified","OrderRequestorCode":"CLIENT_CODE","AtMarket":"Y","Product":"D","WithSL":"N","SLTriggerRate":0,"DisclosedQty":0,"PendingQty":1,"TradedQty":0,"RemoteOrderId":"2324057911323","Remark":""}
```

##### SAMPLE RESPONSE

Cancel

```json
{"ReqType":"C","ClientCode":"CLIENT_CODE","Exch":"N","ExchType":"C","ScripCode":1660,"Symbol":"ITC","Series":"EQ","BrokerOrderID":222072376,"ExchOrderID":"11000028100","ExchOrderTime":"2024-05-09 11:45:18","BuySell":"B","Qty":1,"Price":430,"ReqStatus":0,"Status":"Cancelled","OrderRequestorCode":"CLIENT_CODE","AtMarket":"N","Product":"D","WithSL":"N","SLTriggerRate":0,"DisclosedQty":0,"PendingQty":1,"TradedQty":0,"RemoteOrderId":"1235319136","Remark":""}
```

##### SAMPLE RESPONSE

Trade

```json
{"ReqType":"T","ClientCode":"CLIENT_CODE","Exch":"N","ExchType":"C","ScripCode":1660,"Symbol":"ITC","Series":"EQ","ExchOrderID":"120210200213230","ExchTradeId":"234495","ExchTradeTime":"2024-05-09 11:32:34","BuySell":"B","Qty":1,"Price":434.2,"PendingQty":0,"TotalTradedQty":1,"OrderQty":1,"OrderPrice":434.15,"RemoteOrderId":"204059112343","Product":"D","ReqStatus":0,"Status":"Fully Executed","Remark":""}
```

##### SAMPLE RESPONSE

StopLoss

```json
{"ReqType":"S","ClientCode":"CLIENT_CODE","Exch":"N","ExchType":"C","ScripCode":1660,"Symbol":"ITC","Series":"EQ","ExchOrderID":"1100000043224370","BuySell":"B","Qty":1,"OrderPrice":433.9,"AtMarket":"N","Product":"D","RemoteOrderId":"17152356907","ReqStatus":0,"SLTriggerRate":433.85,"SLTriggerTime":"2024-05-09 11:50:46","Status":"SL Triggered","Remark":""}
```

---

## Options Greeks

> Source: https://xstream.5paisa.com/dev-docs/market-data-system/option-greeks

**Type:** Rest API · **Method:** POST

Options Greeks WebSocket API :

The Options Greeks WebSocket API provides real-time option Greeks data for derivative instruments only.

This stream delivers advanced risk metrics such as Delta, Gamma, Theta, Vega, IV, and higher-order Greeks with low latency, suitable for algo trading, risk engines, and analytics platforms.

This API is read-only, subscription-based, and available via a secure WebSocket connection.

**Options Greeks** are quantitative risk measures that describe how the price of an option responds to changes in key market factors such as the underlying price, volatility, and time.  
They are widely used by traders, risk managers, and algorithmic systems to **monitor exposure, manage risk, and make informed trading decisions**.

In the derivatives market, Greeks provide real-time insight into an option’s **price sensitivity and behavior under changing market conditions** & This WebSocket only works for **exchange NSE.**

### CONNECTION URL

```
wss://gateway.5paisa.com/openapi/greeks?access_token={access_token}
```

### URL Query Parametrs

| PARAMETER NAME | MANDATORY | DESCRIPTION |
|---|---|---|
| access_token<br>STRING | Yes | Access token received in the response of login API |

### SAMPLE CONNECTION URL

```
wss://gateway.5paisa.com/openapi/greeks?access_token={{access_token}}
```

### Subscription Requests

| PARAMETER NAME | MANDATORY | DESCRIPTION |
|---|---|---|
| Method<br>STRING | Yes | It specifies if the request is for subscribing or unsubscribing the data feed.<br>Subscribe<br>Unsubscribe |
| Operation<br>STRING | Yes | optiongreek |
| instruments<br>ARRAY | Yes | List of Option Greek tokens<br>OG prefix is mandatory.<br>["og47599"] |

### Sample response body

| Field | Data Type |
|---|---|
| `PacketIdentifier` | **String** |
| `MessageLength` | **Integer** |
| `Token` | **Integer** |
| `IV` | **Number (float)** |
| `DELTA` | **Number (float)** |
| `THETA` | **Number (float)** |
| `VEGA` | **Number (float)** |
| `GAMMA` | **Number (float)** |
| `IV_VWAP` | **Number (float)** |
| `VANNA` | **Number (float)** |
| `CHARM` | **Number (float)** |
| `SPEED` | **Number (float)** |
| `ZOMMA` | **Number (float)** |
| `COLOR` | **Number (float)** |
| `VOLGA` | **Number (float)** |
| `VETA` | **Number (float)** |
| `TGR` | **Number (float)** |
| `TV` | **Number (float)** |
| `DTR` | **Number (float)** |

> **Note — NOTE**
> - The details scrip code for any instrument can be found from the [Scrip master.](https://xstream.5paisa.com/dev-docs/docFundamentals/scrip-master)
> - Example for multiple subscribe : instruments:["og47599","og47625"]
> - This only works for NSE Scrip codes.

---

## 20-Market Depth

> Source: https://xstream.5paisa.com/dev-docs/market-data-system/20MarketDepth

**Type:** Rest API · **Method:** POST

The Market 20-Depth WebSocket API provides real-time order book depth for supported instruments, delivering up to 20 bid and 20 ask price levels with corresponding quantity and order count. This feed enables clients to monitor market liquidity and order book activity across multiple price levels.

Currently, the 20-Depth feed supports NSE Cash (NC) and NSE Derivatives (ND) instruments only.

This API is read-only and subscription-based, delivering low-latency depth updates via a secure WebSocket connection for the subscribed instruments.

The **Market 20-Depth** feature provides a detailed view of the **order book for a particular instrument**, displaying up to **20 levels of bid (buy) and ask (sell) orders**. This depth information reflects the current market liquidity by showing the quantity, price, and number of orders available at different price levels.

Market depth is commonly used by traders, algorithmic systems, and institutional participants to analyze **supply and demand dynamics**, assess **market liquidity**, and understand potential **price movements** based on order concentration.

### CONNECTION URL

```
wss://gateway.5paisa.com/openapi/20depth?access_token={{access_token}}
```

### URL Query Parametrs

| PARAMETER NAME | MANDATORY | DESCRIPTION |
|---|---|---|
| access_token<br>STRING | Yes | Access token received in the response of login API |

### SAMPLE CONNECTION URL

```
wss://gateway.5paisa.com/openapi/20depth?access_token={{access_token}}
```

### Subscription Requests

| PARAMETER NAME | MANDATORY | DESCRIPTION |
|---|---|---|
| Method<br>STRING | Yes | It specifies if the request is for subscribing or unsubscribing the data feed.<br>Subscribe<br>Unsubscribe |
| Operation<br>STRING | Yes | 20Depth |
| instruments<br>ARRAY | Yes | List of instrument identifiers to subscribe<br>["nc1660","nd45456"] |

### Response body

| Field | Data Type |
|---|---|
| Exch | String |
| ExchType | String |
| Token | Integer |
| TBidQ | Integer |
| TOffQ | Integer |
| Details | Array |
| Quantity | Integer |
| Price | Float |
| NumberOfOrders | Integer |
| BbBuySellFlag | Integer |
| TimeStamp | Integer (Epoch Milliseconds) |

### Sample Response

```json
{
 "Exch": "N",
 "ExchType": "C",
 "Token": 1660,
 "TBidQ": 0,
 "TOffQ": 0,
 "Details": [
   {
     "Quantity": 13,
     "Price": 305.15,
     "NumberOfOrders": 3,
     "BbBuySellFlag": 66
   },
   {
     "Quantity": 25,
     "Price": 305.1,
     "NumberOfOrders": 4,
     "BbBuySellFlag": 66
   },
   {
     "Quantity": 1440,
     "Price": 305.05,
     "NumberOfOrders": 8,
     "BbBuySellFlag": 66
   },
   {
     "Quantity": 3064,
     "Price": 305.0,
     "NumberOfOrders": 68,
     "BbBuySellFlag": 66
   },
   {
     "Quantity": 3379,
     "Price": 304.95,
     "NumberOfOrders": 20,
     "BbBuySellFlag": 66
   }.
As follows till 20Depth.
 ],
 "TimeStamp": 1773052927557
}
```

> **Note — NOTE**
> - The details scrip code for any instrument can be found from the [Scrip master.](https://xstream.5paisa.com/dev-docs/docFundamentals/scrip-master)
> - Example for multiple subscribe : instruments:["nc1660","nd47625"]
> - This only works for NSE Scrip codes.
