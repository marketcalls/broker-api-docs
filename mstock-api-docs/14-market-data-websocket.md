# Market Data WebSocket API

> Source: https://tradingapi.mstock.com/docs/v1/typeB/market-data/
>
> Section: Type B

## Overview

The Market Data WebSocket API provides real-time market feed data through a persistent WebSocket connection. This API supports subscription-based data streaming with multiple data modes and exchange types.

## Connection Endpoint

Connect to the Mirae WebSocket using the following endpoint:

```
wss://ws.mstock.trade?API_KEY=your_api_key_here&ACCESS_TOKEN=your_jwt_token_here
```

## Authentication

### Initial Authentication

1. Authentication requires both API Key and JWT Token
2. API Key is obtained from your account dashboard
3. JWT Token is generated during login process
4. Pass both parameters as query parameters in the WebSocket URL
5. Connection will be rejected if either parameter is invalid or expired

### Connection Maintenance

After successful connection, send a login message to maintain the session:

```
LOGIN:your_jwt_token_here
```

> **Session Timeout**
>
> If the LOGIN message is not sent promptly after connection, the WebSocket will automatically disconnect.

## Request Format

All requests are JSON messages with the following structure:

| Parameter | Description | Type |
| --- | --- | --- |
| `correlationID` | Optional identifier for request tracking | string |
| `action` | Action to perform | integer |
| `params` | Request parameters | object |

### Available Actions

| Value | Action | Description |
| --- | --- | --- |
| `1` | Subscribe | Subscribe to market data |
| `0` | Unsubscribe | Unsubscribe from market data |

### Available Modes

| Value | Mode | Description |
| --- | --- | --- |
| `1` | LTP | Last Traded Price only |
| `2` | Quote | Basic quote data |
| `3` | Snap Quote | Complete market data with depth |

### Supported Exchange Types

| Value | Exchange | Description |
| --- | --- | --- |
| `1` | NSECM | NSE Cash Market |
| `2` | NSEFO | NSE Futures & Options |
| `3` | BSECM | BSE Cash Market |
| `4` | BSEFO | BSE Futures & Options |
| `13` | NSECD | NSE Currency Derivatives |

## API Operations

### Subscribe to Market Data

Subscribe to real-time data for specific instruments:

```json
{
    "correlationID": "optional_tracking_id",
    "action": 1,
    "params": {
        "mode": 3,
        "tokenList": [
            {
                "exchangeType": 1,
                "tokens": ["22", "1333"]
            }
        ]
    }
}
```

### Unsubscribe from Market Data

Stop receiving data for specific instruments:

```json
{
    "correlationID": "optional_tracking_id",
    "action": 0,
    "params": {
        "tokenList": [
            {
                "exchangeType": 1,
                "tokens": ["22", "1333"]
            }
        ]
    }
}
```

## Response Format

### Binary Message Structure

All market data responses are delivered as binary messages that must be parsed as byte arrays and type-cast into appropriate data structures.

#### Message Header

Each binary message contains a header followed by the quote packet:

| Component | Type | Description |
| --- | --- | --- |
| Packet Count | `[byte[2]]` | Number of packets in the message |
| Packet Size | `[byte[2]]` | Total bytes in the quote packet |
| Quote Data | `[byte[]]` | Actual quote packet data |

> **Data Types**
>
> - [short] : 2 Bytes
> - [int] : 4 Bytes
> - [long] : 8 Bytes
> - [double] : 8 Bytes
> - [byte[n]] : n Bytes

### Quote Packet Structure: (379 bytes)

| Field | Type | Bytes |
| --- | --- | --- |
| Subscription Mode | [byte[1]] | 0 - 1 |
| Exchange Type | [byte[1]] | 1 - 2 |
| Token | [byte[25]] | 2 - 27 |
| Sequence Number | [long] | 27 - 35 |
| Exchange Timestamp | [long] | 35 - 43 |
| LTP | [long] | 43 - 51 |
| Last Traded Qty | [long] | 51 - 59 |
| Average Traded Price | [long] | 59 - 67 |
| Volume Traded Today | [long] | 67 - 75 |
| Total Buy Qty | [double] | 75 - 83 |
| Total Sell Qty | [double] | 83 - 91 |
| Open | [long] | 91 - 99 |
| High | [long] | 99 - 107 |
| Low | [long] | 107 - 115 |
| Close | [long] | 115 - 123 |
| Last Traded Timestamp | [long] | 123 - 131 |
| Open Interest | [long] | 131 - 139 |
| Open Interest Percent | [long] | 139 - 147 |
| Market Depth | [byte[200]] | 147 - 347 |
| Upper Circuit Limit | [long] | 347 - 355 |
| Lower Circuit Limit | [long] | 355 - 363 |
| 52 Week High | [long] | 363 - 371 |
| 52 Week Low | [long] | 371 - 379 |

### Market Depth Structure: (200 Bytes)

| Field | Type | Bytes |
| --- | --- | --- |
| Buy/Sell Flag 1 | short | 147 - 149 |
| Bid Qty 1 | long | 149 - 157 |
| Bid Price 1 | long | 157 - 165 |
| Bid Number Of Orders 1 | short | 165 - 167 |
| Buy/Sell Flag 2 | short | 167 - 169 |
| Bid Qty 2 | long | 169 - 177 |
| Bid Price 2 | long | 177 - 185 |
| Bid Number Of Orders 2 | short | 185 - 187 |
| Buy/Sell Flag 3 | short | 187 - 189 |
| Bid Qty 3 | long | 189 - 197 |
| Bid Price 3 | long | 197 - 205 |
| Bid Number Of Orders 3 | short | 205 - 207 |
| Buy/Sell Flag 4 | short | 207 - 209 |
| Bid Qty 4 | long | 209 - 217 |
| Bid Price 4 | long | 217 - 225 |
| Bid Number Of Orders 4 | short | 225 - 227 |
| Buy/Sell Flag 5 | short | 227 - 229 |
| Bid Qty 5 | long | 229 - 237 |
| Bid Price 5 | long | 237 - 245 |
| Bid Number Of Orders 5 | short | 245 - 247 |
| Buy/Sell Flag 1 | short | 247 - 249 |
| Ask Qty 1 | long | 249 - 257 |
| Ask Price 1 | long | 257 - 265 |
| Ask Number Of Orders 1 | short | 265 - 267 |
| Buy/Sell Flag 2 | short | 267 - 269 |
| Ask Qty 2 | long | 269 - 277 |
| Ask Price 2 | long | 277 - 285 |
| Ask Number Of Orders 2 | short | 285 - 287 |
| Buy/Sell Flag 3 | short | 287 - 289 |
| Ask Qty 3 | long | 289 - 297 |
| Ask Price 3 | long | 297 - 305 |
| Ask Number Of Orders 3 | short | 305 - 307 |
| Buy/Sell Flag 4 | short | 307 - 309 |
| Ask Qty 4 | long | 309 - 317 |
| Ask Price 4 | long | 317 - 325 |
| Ask Number Of Orders 4 | short | 325 - 327 |
| Buy/Sell Flag 5 | short | 327 - 329 |
| Ask Qty 5 | long | 329 - 337 |
| Ask Price 5 | long | 337 - 345 |
| Ask Number Of Orders 5 | short | 345 - 347 |
