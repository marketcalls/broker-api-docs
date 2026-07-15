<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Websocket Order Status -->

# Websocket Order Status

Websocket Order Status API will function in providing order status updates through websocket server connection and provide Order responses similar to the one received in Postback/Webhook. The connection can be made to the Websocket Server API using below url and input parameters.

To connect to the WebSocket, clients need to use the following URL:-

```
wss://tns.angelone.in/smart-order-update
```

In the WebSocket connection request, include the following Header key:-

```
Authorization: Bearer AUTHORIZATION_TOKEN
```

#### Please note that there is a connection limit for each user. Each client code is limited to 3 connections.

Initial Response: Upon successfully connecting to the WebSocket, you will receive an initial response in the following format:

```json
{
"user-id": "Your_client_code",
"status-code": "200",
"order-status": "AB00",
"error-message": "",
"orderData": {
"variety": "",
"ordertype": "",
"ordertag": "",
"producttype": "",
"price": 0,
"triggerprice": 0,
"quantity": "0",
"disclosedquantity": "0",
"duration": "",
"squareoff": 0,
"stoploss": 0,
"trailingstoploss": 0,
"tradingsymbol": "",
"transactiontype": "",
"exchange": "",
"symboltoken": "",
"instrumenttype": "",
"strikeprice": 0,
"optiontype": "",
"expirydate": "",
"lotsize": "0",
"cancelsize": "0",
"averageprice": 0,
"filledshares": "",
"unfilledshares": "",
"orderid": "",
"text": "",
"status": "",
"orderstatus": "",
"updatetime": "",
"exchtime": "",
"exchorderupdatetime": "",
"fillid": "",
"filltime": "",
"parentorderid": ""
}
}
```

#### The order-status field can have values like:

| Sr. No | Status Code | Description |
| --- | --- | --- |
| 1 | AB00 | after-successful connection |
| 2 | AB01 | open |
| 3 | AB02 | cancelled |
| 4 | AB03 | rejected |
| 5 | AB04 | modified |
| 6 | AB05 | complete |
| 7 | AB06 | after market order req received |
| 8 | AB07 | cancelled after market order |
| 9 | AB08 | modify after market order req received |
| 10 | AB09 | open pending |
| 11 | AB10 | trigger pending |
| 12 | AB11 | modify pending |

#### Client Interaction:

The client application should periodically send a ping message to the server and expect a pong message from the server every 10 seconds. This helps check the liveliness of the WebSocket connection.

#### Sample Response:

Here's an example of a response you might receive from the WebSocket:

```json
{
"user-id": "Your_client_code",
"status-code": "200",
"order-status": "AB00",
"error-message": "",
"orderData": {
"variety": "NORMAL",
"ordertype": "LIMIT",
"ordertag": "10007712",
"producttype": "DELIVERY",
"price": 551,
"triggerprice": 0,
"quantity": "1",
"disclosedquantity": "0",
"duration": "DAY",
"squareoff": 0,
"stoploss": 0,
"trailingstoploss": 0,
"tradingsymbol": "SBIN-EQ",
"transactiontype": "BUY",
"exchange": "NSE",
"symboltoken": "3045",
"instrumenttype": "",
"strikeprice": -1,
"optiontype": "",
"expirydate": "",
"lotsize": "1",
"cancelsize": "0",
"averageprice": 0,
"filledshares": "0",
"unfilledshares": "1",
"orderid": "1111111",
"text": "Adapter is Logged Off",
"status": "rejected",
"orderstatus": "rejected",
"updatetime": "25-Oct-2023 23:53:21",
"exchtime": "",
"exchorderupdatetime": "",
"fillid": "",
"filltime": "",
"parentorderid": ""
}
}
```

## Error Codes:

| Sr. No | Error Code | Description |
| --- | --- | --- |
| 1 | 401 | If the AUTHORIZATION_TOKEN is invalid, you will receive a 401 Response Code. |
| 2 | 403 | If the AUTHORIZATION_TOKEN is expired, you will receive a 403 Response Code. |
| 3 | 429 | If you breach the connection limit, you will receive a 429 Response Code. |
