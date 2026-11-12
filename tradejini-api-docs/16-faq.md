# Frequently Asked Questions

## What are the requests for websockets ?

One can send 10 requests per second.

## How many instruments can you subscribe to on a single WebSocket connection ?

You can subscribe for up to 3000 instruments on a single WebSocket connection and receive live
quotes for them.You can have a maximum of 5 webSockets

## What events can be subscribed to in the stream ?

Available events include 'orders', 'positions', and 'trades'.
The event fields include type, trdSym, qty, product, price, side,
status, orderId, evntType, exch, msg, and reason.

## How do I get started with the Tradejini Rest API ?

To get started, follow these steps:

1. Login to the [Apps ](https://developer.tradejini.com/developer-portal)and create an app.
2. Obtain your API keys by creating a new application within the Apps section.
3. Set up authorization by following the instructions in the
   "Auth" section
4. Download the SDK by navigating to the "Download SDK" option
   in the top-right corner of the Apps section, select your preferred
   programming language, and refer to the README file
   for detailed instructions on accessing the APIs and WebSocket.

## What is a Bearer token ?

A Bearer token is a unique cryptic string that identifies the user making a
transaction on the CubePlus platform. All Tradejini Rest APIs,
except for the authorization section, require the Bearer token for authorization.

## How do I authenticate API requests ?

Authentication is done using an HTTP Bearer token. The format is: **{APIkey}:{accessToken}.**

Example:  **e4deb3c426836c33000a2f6ebe47d7e2:d0e2659e69e199b0d716b52ee0fe00c1**

## How do I obtain an API key?

To obtain an API key, register at the [Apps ](https://developer.tradejini.com/developer-portal)and create an application. This will generate the API key needed for your requests.

## What is an access token, and how do I get one ?

An access token can be received in the response of the access-token service or
individual token service.This token is used to authenticate your API requests.

## What is the host for the CubePlus Streaming ?

The host CubePlus Streaming URL for the production environment is: **api.tradejini.com.**

## What happens if the authToken expires or is invalid ?

If the authToken is expired or invalid,
you will receive a close message with code "401" and the message "Unauthorized Access".

## How do I form the authToken and subscribe for prices ?

If you have the API key and access token handy, form the authToken and
subscribe to prices. If not, generate it from the [developer portal API documentation.](https://developer.tradejini.com/developer-portal)

## What is the streaming symbol logic in Cubeplus ?

The Cubeplus stream requires a streaming symbol for price subscription.
The stream symbol is a combination of exchangeToken and exchangeName in the format
<exchangeToken>_<exchangeName>. For example, for ACC NSE symbol, the stream symbol would be '22_NSE'.

## How do I retrieve exchangeToken and exchangeName ?

Exchange token 'excToken' is received from the ScripMaster Data API response, and exchangeName
should be retrieved from the field 'ID' from the same response. The ID should be split
using the underscore ('_'), and the last string will be the exchange name.

## What are the different subscription methods in socket implementation ?

Various methods like subscribeL1, subscribeL1SnapShot, subscribeL2, subscribeL2SnapShot,
subscribeGreeks, subscribeGreeksSnapShot, subscribeEvents, and subscribeOHLC are available for
different types of data subscriptions. Additionally, unsubscribe methods are available for each
type of subscription.

## What happens to previous subscriptions when making a new request ?

If you make a new subscription request, the old symbols subscribed will be unsubscribed, and
only the new subscription list will be considered. For example, if on the first subscription Symbols
[A, B, C, D] are sent and on the subsequent request, Symbols [E, F] are sent, only [E, F] will be
streamed, and [A, B, C, D] will be unsubscribed.

## What are the fields in the stream response data ?

Various fields like exchSeg, token, precision, ltp, open, high, low, close, chng, chngPer, atp,
yHigh, yLow, ltq, vol, ttv, ucl, lcl, OI, OIChngPer, ltt, bidPrice, qty, no, askPrice, symbol,
totBuyQty, totSellQty, prevOI, dayHighOI, dayLowOI, marketStatus, spotPrice, dayClose, vwap, itm, iv,
delta, gamma, theta, rho, vega, highiv, lowiv, time, type, minuteOi are included in
the streaming response data.

## What do the streaming error messages mean ?

The 'Error' message indicates {"s": "error", "reason": <error Message>}, 'Close' message
indicates {"s": "closed", "code": <close code>, "reason": <close Message>}, and 'Open' message
indicates {"s": "connected"}.
