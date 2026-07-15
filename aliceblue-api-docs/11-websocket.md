<!-- Source: https://ant.aliceblueonline.com/productdocumentation/Websocket/ -->

# Web Socket Connection for Vendors

## Introduction

The WebSocket API is an advanced technology that makes it possible to open a two-way interactive communication session between the user's browser and a server. With this API, you can send messages to a server and receive event-driven responses without having to poll the server for a reply.

With a WebSocket API, you can receive quotes for all scrips across all Indian Exchanges during the market hours. The feeds are usually classified into two categories, Market Feed and Depth Feed. For every new connection, you will receive an acknowledgment (usually represented as "tk") followed by the exchange feed (usually represented as "tf").

## Invalidate Session

This endpoint allows clients to invalidate an existing WebSocket session. Upon successful invalidation, the session is terminated, and further communication using the session ID becomes invalid. This operation requires authentication credentials and the session ID of the WebSocket session to be invalidated.

| Method | APIS |
| --- | --- |
| Post | /open-api/od/v1/profile/invalidateWsSess |

**Request**

Parameters are as below (Payload). Use JSON content type

```
{
    "source": "API",
    "userId": "1614986"
}          
```

**Response from Rest API**

```
{
    "status": "Ok",
    "message": "Success",
    "infoMessage": null,
    "result": [
        {
            "Status": "OK"
        }
    ]
}
```

## Create Session

Create a new session using REST API.

| Method | APIS |
| --- | --- |
| Post | /open-api/od/v1/profile/createWsSess |

**Request**

Parameters are as below (Payload). Use JSON content type

```
 {
    "source": "API",
    "userId": "1614986"
}          
```

**Response from Rest API**

```
{
    "status": "Ok",
    "message": "Success",
    "infoMessage": null,
    "result": [
        {
            "Status": "OK"
        }
    ]
}
```

## Create Connection

**Create Connection to Web Socket using the following URL**

User has to generate SHA-256 encrypted key of User's Session Id 2 times for susertoken.

[wss://ws1.aliceblueonline.com/NorenWS]

**Request**

```
    {
        "susertoken": sha256_encryption( sha256_encryption(session_id)),
        "t": "c",
        "actid": client_id+ "_API",
        "uid": client_id + "_API",
        "source": "API"
    }
```

Subscribe

- {"k":"NSE|26000#NSE|26009#CDS|5596#NSE|13#NSE|11536#NSE|26037","t":"t"}

**Response from WS**

```
    {"t":"cf","k":"OK"}

    If validation fails, response will show as its failed

    {"t":"cf","k":"failed"}
```

## Sending heartbeat

The Sending heartbeat through web socket is a way to inform server the client is still active and accepting feeds. This way, server will be able to eliminate inactive or closed client connections from server side which results in better performance. Below are the request parameters to send heartbeat to server.

**Request**

```
    {
        "k": "",
        "t": "h"
    }

    k = Send this as empty for heartbeat request 
    t = Type of request, 'h' stands for Heartbeat 
```

**Send heartbeat once in every 50 seconds.**

This will NOT provide any response. Just accepting the message is the indication that your heartbeat request is received and feeds will keep coming. At present, sending heartbeat is not mandatory. However, it is advised to send heartbeat, otherwise the server will close connection after a defined timeframe if no data is being send or received. For example, if user has subscribed for some illiquid stocks which are not traded frequently, the client will not receive any feed for longer periods. This may lead to connection closure from server side. To avoid this, sending the heartbeat will inform the server that the client is still active and receiving feed.

## Subscription to Market Data (LTP, Change, OHLC and Volume)

**Request**

```
    {"k":"NFO|54957#MCX|239484","t":"t"}

    t = Type of request, t for tick data
    k = Params for subscription with pipe ‘|’ delimited tokens and exchange. Token and
    exchange should be separated with #
```

Acknowledgement Response

```
    {"t":"tk","pp":"2","ml":"1","e":"NFO","tk":"54957","ts":"NIFTY28JUL22C16600","ls":"50","ti":"0.05","c":
    42.20","lp":"84.00","pc":"99.05","ft":"1658911102","oi":"7606750","o":"37.65","h":"98.00","l":"22.0
    0","ap":"61.35","v":"129781850","bp1":"84.00","sp1":"84.20","bq1":"1000","sq1":"300"}

    {"t":"tk","pp":"2","ml":"1","e":"MCX","tk":"239484","ts":"CRUDEOIL19SEP22","ls":"100","ti":"1.00","c"
    "7522.00","ft":"1658911100","v":"469","oi":"429","bp1":"7564.00","sp1":"7567.00","bq1":"1","sq1":"
    "7522.00","ft":"1658911100","v":"469","oi":"429","bp1":"7564.00","sp1":"7567.00","bq1":"1","sq1":"}
```

**Feed Response**

```
    {"t":"tf","e":"NFO","tk":"54957","lp":"84.20","pc":"99.53","ft":"1658911102"}

    {"t":"tf","e":"NFO","tk":"54957","lp":"84.35","pc":"99.88","ft":"1658911103","v":"129787100","bp1":"
    84.30","sp1":"84.50","bq1":"1500","sq1":"350"}
```

This table provides the descriptions for various abbreviations used in the documentation.

| Abbreviation | Description |
| --- | --- |
| t | type |
| tf | tick feed |
| tk | tick acknowledgement |
| e | exchange |
| tk | token |
| lp | LTP (Last traded price) |
| pc | Percentage change |
| cv | change value (Absolute change in price) |
| v | volume |
| o | open |
| h | high |
| l | low |
| c | close |
| ap | Average Price |
| symbol | Symbol Name |

## Un-Subscription to Market Data (LTP, Change, OHLC and Volume)

**Request**

```
    {"k":"NFO|54957#MCX|239484","t":"u"}

    t = Type of request, u for Un-subscription
    k = Params for subscription with pipe ‘|’ delimited tokens and exchange. Token and
    exchange should be separated with #
```

Response

```
No response will be coming for this. Unsubscribed tokens will no longer receive feed
```

## Subscription to Depth data (LTP, Change, OHLC, OI and Volume)

**Request**

```
    {"k":"NFO|54957#MCX|239484","t":"d"}

    t = Type of request, t for tick data
    k = Params for subscription with pipe ‘|’ delimited tokens and exchange. Token and
    exchange should be separated with #
```

Acknowledgement Response

```
    {"t":"dk","pp":"2","ml":"1","e":"NFO","tk":"54957","ts":"NIFTY28JUL22C16600","ls":"50","ti":"0.05","c":"42.20","lp":"76.40",
    "pc":"81.04","uc":"469.90","lc":"0.05","ft":"1658910517","oi
    ":"7361100","ltq":"50","o":"37.65","h":"98.00","l":"22.00","ap":"60.72","v":"125888500","ltt":"13:58:37","tbq":"965400","ts
    q":"980950","bp1":"76.30","sp1":"76.45","bp2":"76.25","sp2":"
    76.50","bp3":"76.20","sp3":"76.55","bp4":"76.15","sp4":"76.60","bp5":"76.10","sp5":"76.65","bq1":"50","sq1":"650","bq2":
    "2000","sq2":"1400","bq3":"3800","sq3":"2250","bq4":"2000","sq4":"3400","bq5":"7350","sq5":"2250","bo1":"1","so1":"2",
    bo2":"9","so2":"8","bo3":"22","so3":"12","bo4":"12","so4":"16","bo5":"17","so5":"7"}

    {"t":"dk","pp":"2","ml":"1","e":"MCX","tk":"239484","ts":"CRUDEOIL19SEP22","ls":"100","ti":"1.00","c":"7522.00","ft":"1658
    910516","v":"454","oi":"437","ltq":"1","tbq":"144","tsq":"119",
    "bp1":"7564.00","sp1":"7567.00","bp2":"7563.00","sp2":"7568.00","bp3":"7562.00","sp3":"7570.00","bp4":"7561.00","sp4":
    "7571.00","bp5":"7560.00","sp5":"7572.00","bq1":"1","sq1":"5","bq
    2":"1","sq2":"4","bq3":"5","sq3":"3","bq4":"4","sq4":"5","bq5":"3","sq5":"1","bo1":"1","so1":"3","bo2":"1","so2":"2","bo3":
    "5","so3":"1","bo4":"4","so4":"4","bo5":"3","so5":"1","52h":"8382.00","52l":"6966.00","lp":"7568.00","pc":"0.61","o":"7479.00",
    "h":"7588.00","l":"7479.00","ap":"7536.33","ltt":"13:58:12"}
```

**Feed Response**

```
    {"t":"df","e":"NFO","tk":"54957","lp":"76.55","pc":"81.40","ft":"1658910520","ltq":"200"}

    {"t":"df","e":"MCX","tk":"239484","ft":"1658910519","tsq":"117","sq1":"3","so1":"1"}
```

| Symbol | Description |
| --- | --- |
| t | type |
| dk | depth acknowledgement |
| df | depth feed |
| e | exchange |
| tk | token |
| lp | LTP (Last traded price) |
| pc | Percentage change |
| cv | change value (Absolute change in price) |
| v | volume |
| o | open |
| h | high |
| l | low |
| c | close |
| ap | Average Price |
| ts | Symbol Name |
| oi | open interest |
| ltq | last traded qty |
| ltt | last traded time |
| tbq | total buy qty |
| tsq | total sell qty |
| uc | upper circuit |
| lc | lower circuit |
| bp1,bp2,bp3,bp4,bp5 | Depth buy price |
| sp1,sp2,sp3,sp4,sp5 | Depth sell price |
| bq1,bq2,bq3,bq4,bq5 | Depth buy quantity |
| sq1,sq2,sq3,sq4,sq5 | Depth sell quantity |
| bo1,bo2,bo3,bo4,bo5 | Depth buy order |
| so1,so2,so3,so4,so5 | Depth sell order |

## Un-Subscription to Depth data (LTP, Change, OHLC and Volume)

**Request**

```
    {"k":"NFO|54957#MCX|239484","t":"ud"}

    t = Type of request, ud for Un-subscription
    k = Params for subscription with pipe ‘|’ delimited tokens and exchange. Token and
    exchange should be separated with #
```

Response

```
No response will be coming for this. Unsubscribed tokens will no longer receive feed
```
