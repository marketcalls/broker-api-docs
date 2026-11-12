# Trade WebSocket

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction

Websocket Trade Status API will function in providing trade status updates through websocket server connection and provide Trade responses. The connection can be made to the Websocket Server API using below url and input parameters.

Websocket endpoint UAT URL is :-

```text
wss://uatopenapi.motilaloswal.com/ws
```

Websocket endpoint Live URL is :- (WIP)

```text
wss://openapi.motilaloswal.com/ws
```

The message format to send messages to the Server to make the connection as a JSON object is as below :-

Request for Authorization

```json
{
“clientid”: “AA020”,
“authtoken”: “auth_token”
“apikey”: “api_key”
}
```

The message format to send messages to the Server to make subscription request after connection is made as a JSON object is as below :-

Request for TradeSubscription

```json
{
“clientid”: “AA020”,
“action”: “TradeSubscribe”
}
```

Similarly all the possible action values are as follows :-

action = TradeSubscribe, TradeUnsubscribe, OrderSubscribe, OrderUnsubscribe, logout and heartbeat.

Request for TradeUnsubscription

```json
{
“clientid”: “AA020”,
“action”: “TradeSubscribe”
}
```

Request for OrderSubscription

```json
{
“clientid”: “AA020”,
“action”: “OrderSubscribe”
}
```

Request for OrderUnsubscription

```json
{
“clientid”: “AA020”,
“action”: “OrderUnsubscribe”
}
```

Request for Logout

```json
{
“clientid”: “AA020”,
“action”: “logout”
}
```

Request for Heartbeat

```json
{
“clientid”: “AA020”,
“action”: “heartbeat”
}
```

Sample Trade JSON response

```json
{
"clientid": "AA020",
"exchange": "NSE",
"symboltoken": 11536,
"producttype": "NORMAL",
"symbol": "TCS EQ",
"instrumenttype": "",
"series": "EQ",
"strikeprice": 0,
"optiontype": "EQ",
"expirydate": "0",
"lotsize": 1,
"precision": 2,
"multiplier": 1,
"tradeprice": 3597.05,
"tradeqty": 1,
"tradevalue": 3597.05,
"buyorsell": "BUY",
"orderid": "1100000000160907",
"tradeno": "50160094",
"tradetime": "15-Mar-2022 18:44:54",
"uniqueorderid": "1500006T024312"
}
```

Sample Order JSON response

```json
{
"ordercategory": "NORMAL",
"clientid": "T024312",
"exchange": "NSE",
"symboltoken": 22,
"symbol": "ACC EQ",
"series": "EQ",
"expirydate": "0",
"strikeprice": 0,
"optiontype": "EQ",
"orderid": "1000000000131639",
"orderinitiatorid": "T024312",
"ordertype": "Market",
"orderduration": "Day",
"producttype": "NORMAL",
"error": "",
"orderstatus": "Confirm",
"buyorsell": "BUY",
"totalqtyremaining": 50,
"orderqty": 50,
"qtytradedtoday": 0,
"disclosedqty": 0,
"price": 0,
"triggerprice": 0,
"entrydatetime": "17-Jun-2022 16:07:55",
"lastmodifiedtime": "17-Jun-2022 16:07:55",
"vendor": "MOFSL",
"uniqueorderid": "1700001T024312",
"goodtilldate": "0",
"algoid": 0,
"algocategory": 0,
"averageprice": 0,
"totalqtytraded": 0,
"lotsize": 1,
"tag": "KTEST1"
}
```

## WebSocket Server Error Codes

| Sr. No | Error Code | Description |
| --- | --- | --- |
| 1 | MO1001 | Invalid User Id Or Auth Token |
| 2 | MO8000 | Technical Error |
| 3 | MO2012 | Invalid Action Request. |
