<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: WebSocket Streaming 2.0 -->

# WebSocket Streaming 2.0

- Web Socket URL
- Features
- Request Headers for Authentication
- Response Headers for Authentication Errors
- Heartbeat message

## WebSocket URL

```
wss://smartapisocket.angelone.in/smart-stream
```

## Features

For example: If the client subscribes to Infosys NSE with LTP, Quote, and SnapQuote mode then this will be counted as 3 subscriptions.

Duplicate subscriptions to the same token and mode will be gracefully ignored and will not be counted towards the quota

For example: If the client subscribes to Infosys NSE with LTP, Quote, and SnapQuote mode then 1 tick will be published for each mode, containing respective fields.

The recommendation is to subscribe to one mode at a time for a token.

## Request Headers for Authentication

| Field | Mandatory | Description |
| --- | --- | --- |
| Authorization | Yes | jwt auth token received from Login API |
| x-api-key | Yes | API key |
| x-client-code | Yes | client code (Angel Onetrading account id) |
| x-feed-token | Yes | feed token received fromLogin API |

## Response Headers for Authentication Errors

| Field | Mandatory | Description | Valid Values |
| --- | --- | --- | --- |
| x-error-message | No | Along with HTTP status code 401, the responseheader will contain textual description of why auth failed. | Invalid Header - Invalid Auth token<br>Invalid Header - Invalid Client Code<br>Invalid Header - Invalid API Key Invalid<br>Header - Invalid Feed Token |

## For Users using Browser Based clients for websocket

For users using browser based clients for websocket streaming, please append the query params in the url in the given format to make connection

```
wss://smartapisocket.angelone.in/smart-stream?clientCode=&feedToken=&apiKey=
```

| Query Param | Mandatory | Description |
| --- | --- | --- |
| clientCode | Yes | Angel One Client Code |
| feedToken | Yes | feedToken received in login response |
| apiKey | Yes | Your API Key |

Note : Please note that all error handling and status codes will remain the same.

## Heartbeat message

```
ping
```

```
pong
```

## Request Contract

JSON Request

#### Sample

```json
{
"correlationID": "abcde12345",
"action": 1,
"params": {
"mode": 1,
"tokenList": [
{
"exchangeType": 1,
"tokens": [
"10626",
"5290"
]
},
{
"exchangeType": 5,
"tokens": [
"234230",
"234235",
"234219"
]
}
]
}
}
```

## Field Description

| Field | Type | Mandatory (M) / Optional(O) | Description | Valid Values |
| --- | --- | --- | --- | --- |
| correlationID | String | O | A 10 character alphanumeric ID client may provide which will be returned by the server in error response to indicate which request generated error response.<br>Clients can use this optional ID for tracking purposes between request and corresponding error response. |  |
| action | Integer | M | action | 1 (Subscribe)<br>0 (Unsubscribe) |
| params | JSON Object | M |  |  |
| mode | Integer | M | Subscription Type as per this. | 1 (LTP)<br>2 (Quote)<br>3 (Snap Quote) |
| tokenList[] | array of JSONObjects | M | list of tokens per exchange |  |
| tokenList[].exchangeType | Integer | M | exchange type | 1 (nse_cm)<br>2 (nse_fo)<br>3 (bse_cm)<br>4 (bse_fo)<br>5 (mcx_fo) |
| tokenList[].tokens | List of Strings | M | tokens to subscribe.Refer Master Scrip for token by stock |  |

## Response Contract for LTP, Quote and Snap Quote mode

Response is in binary format with Little Endian byte order.

#### Section-1) Payload

|  | Field | DataType | Size (in bytes) | Field Start Position(Index in Byte Array) | Description | Valid Values |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Subscription Mode | byte/int8 | 1 | 0 | Subscription Type such as LTP, Quote, Snap Quote | 1 (LTP)<br>2 (Quote)<br>3 (Snap Quote) |
| 2 | Exchange Type | byte/int8 | 1 | 1 |  | 1 (nse_cm)<br>2 (nse_fo)<br>3 (bse_cm)<br>4 (bse_fo)<br>5 (mcx_fo) |
| 3 | Token | byte array | 25 | 2 | Token Id in characters encoded as byte array. One byte represents one utf-8 encoded character.<br>Null char signifies the end of characters i.e. \0000u in Java |  |
| 4 | Sequence Number | int64/long | 8 | 27 |  |  |
| 5 | Exchange Timestamp | int64/long | 8 | 35 | Exchange feed timestamp in epoch milliseconds |  |
| 6 | Last Traded Price (LTP)(If mode is ltp, the packet ends here.packet size = 51 bytes) | int32 | 8 | 43 | All prices are in paise. For currencies, the int 32 price values should be divided by 10000000.0 to obtain four decimal places. For everything else, the price values should be divided by 100. |  |
| 7 | Last traded quantity | int64/long | 8 | 51 |  |  |
| 8 | Average traded price | int64/long | 8 | 59 |  |  |
| 9 | Volume traded for the day | int64/long | 8 | 67 |  |  |
| 10 | Total buy quantity | double | 8 | 75 |  |  |
| 11 | Total sell quantity | double | 8 | 83 |  |  |
| 12 | Open price of the day | int64/long | 8 | 91 |  |  |
| 13 | High price of the day | int64/long | 8 | 99 |  |  |
| 14 | Low price of the day | int64/long | 8 | 107 |  |  |
| 15 | Close price(If mode is quote,the packet ends here.packet size = 123 bytes) | int64/long | 8 | 115 |  |  |
| 16 | Last traded timestamp | int64/long | 8 | 123 |  |  |
| 17 | Open Interest | int64/long | 8 | 131 |  |  |
| 18 | Open Interest change % (this is a dummy field. contains garbage value) | double | 8 | 139 |  |  |
| 19 | Best Five Data | Array containing 10 packets. Each packet having 20 bytes. | 200 | 147 | sequence of best five buys data,followed by best five sells.(refer Section-2) Best Five Data) |  |
| 20 | Upper circuit limit |  | 8 | 347 |  |  |
| 21 | Lower circuit limit |  | 8 | 355 |  |  |
| 22 | 52 week high price |  | 8 | 363 |  |  |
| 23 | 52 week low price(If mode is snapquote, the packet ends here. packet size = 379 bytes) |  | 8 | 371 |  |  |

**NOTE -**Sequence number for index feed is not available. please ignore the sequence number for index feed in the websocket response.

#### Section-2) Best Five Data

| Field | DataType | Size (in bytes) | Field Start Position(Index in Byte Array) | Description | Valid Values |
| --- | --- | --- | --- | --- | --- |
| Buy/Sell Flag | int16 | 2 | 0 | Flag to indicate whether this packet is for buy or sell data | 1 (buy)<br>0 (sell) |
| Quantity | int64 | 8 | 2 | Buy/Sell Quantity |  |
| Price | int64 | 8 | 10 | Buy/Sell Price |  |
| Number of Orders | int16 | 2 | 18 | Buy/Sell Orders |  |

### Error Response

#### Sample

```json
{
"correlationID": "abcde12345",
"errorCode": "E1002"
"errorMessage": "Invalid Request. Subscription Limit Exceeded"
}
```

### Error Codes

| Error Code | Error Message |
| --- | --- |
| E1001 | Invalid Request Payload. |
| E1002 | Invalid Request. Subscription Limit Exceeded. |

**NOTE:** Packet Received Time is a dummy value and will be deprecated soon.
