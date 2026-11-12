# Live Market Data

- [Live Market Data WebSocket Streaming](#live-market-data-websocket-streaming)
- [Live Market Data API](#live-market-data-api)
- [test](#test)

## Live Market Data WebSocket Streaming

Source: https://developer.paytmmoney.com/docs/api/live-market-data-webSocket-streaming/

### Description

> The Market Data WebSocket Streaming is the most efficient way to receive live market quotes for instruments during live market hours. WebSocket Streaming helps with high speed, low latency, low resource consumption, and low bandwidth. You will get market data with fields like open, high, low, close, last traded price, 5 levels of bid/offer market depth data etc.  
> The Live Market Data WebSocket Streaming service supports 500 preferences on a single web socket connection. A client can create multiple web socket connections using the same jwt token. A preference comprises five fields- actionType, scripType, scripId, modeType, exchangeType. Currently, we support NSE & BSE for scripTypes namely INDEX, ETF, EQUITY, FUTURE, and OPTION with each scripType having four modes- LTP, QUOTE, FULL, and CAS. Once a user has subscribed to a particular scrip, they will start receiving live market data for it via a WebSocket connection.

### Notes

### How to use it ?

1. Create a Public Access Token (JWT Token) using the get access token API. **You can access Live Market Data WebSocket Streaming API using public access token only.**   
   Request  

   ```
   		curl --location --request POST 'https://developer.paytmmoney.com/accounts/v2/gettoken' \
   			--header 'Content-Type: application/json' \
   			--data-raw '{
   				"api_secret_key" : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   				"request_token" : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   				"api_key" : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   			}'
   		
   ```

     
   Response

   ```
   		
   {
   	"merchant_id": "MER_241Qua",
   	"channel_id": "MER_241Qua",
   	"api_key": "7fc3d98dc31744e0ac670d74bd11b6af",
   	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJtZXJjaGFudCIsImlzcyI6InBheXRtbW9uZXkiLCJpZCI6MzEwLCJleHAiOjE2NzI4NTY5OTl9.x-rPswqH0wX-MTrWFdP9yj7WqgLLrNb7PQKG-Ut7Ul4",
   	"public_access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJtZXJjaGFudCIsImlzcyI6InBheXRtbW9uZXkiLCJpZCI6MzEwLCJleHAiOjE2NzI4NTY5OTl9.Swz02RvHCt-f9y25sPtSj55eYgSK3m1O58-U7sMNlbA",
   	"read_access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJtZXJjaGFudCIsImlzcyI6InBheXRtbW9uZXkiLCJpZCI6MzEwLCJleHAiOjE2NzI4NTY5OTl9.noxtdrQens5RNPBqlyxWkGRg4LAoe5u4OVUNyn8GiaU"
   } 
   		
   ```
2. To create a web socket connection with the Live Market Data WebSocket Streaming service, send a web socket connection request to
   > wss://developer-ws.paytmmoney.com/broadcast/user/v1/data?x\_jwt\_token={{PUBLIC\_ACCESS\_TOKEN}}

   ```
           // Sample JavaScript code for connecting to the WebSocketServer 
   			// Javascript example 
   			var socket = new WebSocket("wss://developer-ws.paytmmoney.com/broadcast/user/v1/data?x_jwt_token={{PUBLIC_ACCESS_TOKEN}}");
   ```
3. Once successfully connected, you may send a preference to receive live market data.

   ```
               // Subscribe to Multiple scrips 
               var preferences = 
               [
                 {
                   "actionType": "ADD",
                   "modeType": "FULL",
                   "scripType": "INDEX",
                   "exchangeType": "NSE",
                   "scripId": "13"
                 },
                 {
                   "actionType": "ADD",
                   "modeType": "LTP",
                   "scripType": "EQUITY",
                   "exchangeType": "BSE",
                   "scripId": "523144"
                 }
               ]; 
               
               socket.send(JSON.stringify(preferences));
   ```

> For fetching the latest security ids please use [Security Master API](https://developer.paytmmoney.com/docs/api/security-master/)

### Preference structure

#### A single preference must contain the following fields:

##### **ActionType**

actionType key may have one of the following values

| ActionType | Description |
| --- | --- |
| ADD | To subscribe to a particular scrip |
| REMOVE | To unsubscribe to a particular scrip |

##### **ModeType**

ModeType key may have one of the following values

| ModeType | Description |
| --- | --- |
| LTP | The packet contains several fields including the last traded price |
| QUOTE | The packet contains several fields excluding the market depth |
| FULL | The packet contains several fields including the market depth |
| CAS | The packet contains several fields including the auction depth |

##### **ScripType**

ScripType key may have one of the following values

| ScripType | Description |
| --- | --- |
| INDEX | for scrip ids belonging to the index scrip type |
| EQUITY | for scrip ids belonging to equity scrip type |
| ETF | for scrip ids belonging to ETF scrip type |
| FUTURE | for scrip ids belonging to future scrip type |
| OPTION | for scrip ids belonging to option scrip type |

##### **ExchangeType**

ExchangeType key may have one of the following values

| ExchangeType | Description |
| --- | --- |
| BSE | for scrip ids belonging to BSE Limited |
| NSE | for scrip ids belonging to the National Stock Exchange of India Limited |

##### **ScripId**

| ScripId | Description |
| --- | --- |
| xxx15 | The exchange scrip id of the stock you want to receive live market data for. |

```
    // Preference structure for subscribing a scrip 
    {
      "actionType": "ADD",
      "modeType": "FULL",
      "scripType": "INDEX",
      "exchangeType": "NSE",
      "scripId": "13"
    }
    // Preference structure for unsubscribing a scrip 
    {
      "actionType": "REMOVE",
      "modeType": "QUOTE",
      "scripType": "ETF",
      "exchangeType": "NSE",
      "scripId": "2328"
    }
```

### Api Info

> GET - wss://developer-ws.paytmmoney.com/broadcast/user/v1/data?x\_jwt\_token={{PUBLIC\_ACCESS\_TOKEN}}

##### **Description**

GET Request to establish a web socket connection

| Key/Parameter | Type | Required? | Value | Description |
| --- | --- | --- | --- | --- |
| x\_jwt\_token | string | Yes | jwtToken | Valid Public Access Token |

##### **Response Fields**

| Attribute | Description |
| --- | --- |
| tradableByte | 0 for false, 1 for true. True if stock is tradable else false |
| modeByte | Type of Packet LTP/QUOTE/FULL/CAS LTP=61; QUOTE=62; FULL=63; INDEX LTP=64; INDEX QUOTE=65; INDEX FULL=66; CAS=67 |
| security\_idInteger | Security Id for which broadcast is received |
| last\_priceFloat | Last traded market price |
| last\_traded\_quantityInteger | Last traded quantity |
| average\_traded\_priceFloat | Average traded market price |
| volume\_tradedInteger | Volume traded today |
| total\_buy\_quantityInteger | Total quantity of buy orders pending at the exchange |
| total\_sell\_quantityInteger | Total quantity of sell orders pending at the exchange |
| openFloat | Price when the market opened |
| highFloat | Highest price today |
| lowFloat | Lowest price today |
| closeFloat | Closing price of the instrument from the last trading day |
| change\_percentFloat | The absolute percentage price change of the security's price since the previous day's close |
| change\_absoluteFloat | The absolute change in security's price since the previous day's close |
| 52\_week\_highFloat | The highest price at which a security has traded during the time period that equates to one year |
| 52\_week\_lowFloat | The lowest price at which a security has traded during the time period that equates to one year |
| last\_traded\_timeString | Last trade timestamp |
| last\_update\_timeString | Last update timestamp |
| oiInteger | Number of future and option contracts traded but not yet liquidated |
| change\_oiInteger | The change in the number of future and option contracts traded but not yet liquidated |
| indicative\_equilibrium\_priceFloat | The real-time, volume-maximizing price calculated dynamically during call auction sessions before the final market price is locked |
| reference\_priceFloat | The base price used to calculate the ±3% operating band and fallback closing price for the Closing Auction Session (CAS) |
| imbalance\_quantityLong | The un-matchable surplus buy or sell volume remaining at the Indicative Equilibrium Price (IEP) during a call auction session |

##### **MBP ROW PACKET**

| Attribute | Description |
| --- | --- |
| Buy QuantityInteger | Net quantity from the pending orders |
| Buy PriceFloat | Price at which the buy order depth stands |
| Buy OrdersFloat | Price at which the buy order depth stands |
| Sell QuantityFloat | Net quantity from the pending orders |
| Sell PriceFloat | Price at which the sell order depth stands |
| Sell OrdersInteger | Number of open sell orders at the price |

##### **Error Codes and Messages**

HTTP Error Codes

| Response Code | Response message | Description |
| --- | --- | --- |
| 400 | Bad Request | Bad Request |
| 401 | Unauthorized | Unauthorized jwt token or sso token |
| 500 | Internal Server Error | Internal Server Error |
| 509 | Bandwidth limit exceeded | The server has reached its maximum connection limit |

##### **Web socket Error Message**

| Error Message | Description |
| --- | --- |
| "You have sent preference packet in an invalid format" | preference structure is invalid |
| "You have reached the maximum subscription limit: 500" | connection's preference subscription limit of 500 reached |

##### **IMPORTANT NOTE:**

1. The Preferences must be sent in the form of a JSON array.
2. The Response received from Live Market Data WebSocket Streaming service will be a byte buffer and may contain Live market data for one or more preferences.
3. All connections will receive a ping frame from Live Market Data WebSocket Streaming service every 30 seconds.
4. Our servers will restart every day at 12:30:00 AM (hh:mm:ss), which may lead to disconnection if you have an active connection with our server.

### EPOC Converter

```
    import java.util.Calendar;
    import java.util.Locale;
    import java.util.TimeZone;
     
    class EpocConverter {
        public static void main(String[] args) {
            try {
                long input_epoch_value = 1339062026;
                final TimeZone utc = TimeZone.getTimeZone("UTC");
                Calendar ninetyEighty = Calendar.getInstance();
                ninetyEighty.clear();
                ninetyEighty.setTimeZone(utc);
                ninetyEighty.set(1980, 0, 1, 0, 0, 0);
                long timenew = ninetyEighty.getTimeInMillis() / 1000;
                long output_epoch_value = input_epoch_value + timenew;
                System.out.println(output_epoch_value);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
```

### Response Table according to ModeType

##### **PACKET CODE**

| TYPE | PACKET CODE |
| --- | --- |
| LTP | 61 |
| QUOTE | 62 |
| FULL | 63 |
| INDEX LTP | 64 |
| INDEX QUOTE | 65 |
| INDEX FULL | 66 |
| CAS | 67 |

##### **TRADABLE**

| TYPE | VALUE |
| --- | --- |
| true | 1 |
| false | 0 |

##### **MODE**

| MODE TYPE | VALUE |
| --- | --- |
| LTP | 61 |
| QUOTE | 62 |
| FULL | 63 |
| INDEX LTP | 64 |
| INDEX QUOTE | 65 |
| INDEX FULL | 66 |
| CAS | 67 |

##### **MBP ROW PACKET**

| Attribute | Offset |
| --- | --- |
| Buy Quantityint | 0-3 |
| Sell Quantityint | 4-7 |
| Number Of Buy Ordersshort | 8-9 |
| Number Of Sell Ordersshort | 10-11 |
| Buy Pricefloat | 12-15 |
| Sell Pricefloat | 16-19 |

##### **LTP**

PACKET SIZE = 23

| Attribute | Offset |
| --- | --- |
| Packet Codebyte | 0 |
| last\_priceFloat | 1-4 |
| last\_traded\_timeInteger | 5-8 |
| security\_idInteger | 9-12 |
| tradablebyte | 13 |
| modebyte | 14 |
| change\_absoluteFloat | 15-18 |
| change\_percentFloat | 19-22 |

##### **LTP INDEX**

PACKET SIZE = 23

| Attribute | Offset |
| --- | --- |
| Packet Codebyte | 0 |
| last\_priceFloat | 1-4 |
| last\_update\_timeInteger | 5-8 |
| security\_idInteger | 9-12 |
| tradablebyte | 13 |
| modebyte | 14 |
| change\_absoluteFloat | 15-18 |
| change\_percentFloat | 19-22 |

##### **QUOTE**

PACKET SIZE = 67

| Attribute | Offset |
| --- | --- |
| Packet Codebyte | 0 |
| last\_priceFloat | 1-4 |
| last\_traded\_timeInteger | 5-8 |
| security\_idInteger | 9-12 |
| tradablebyte | 13 |
| modebyte | 14 |
| last\_traded\_quantityInteger | 15-18 |
| average\_traded\_priceFloat | 19-22 |
| volume\_tradedInteger | 23-26 |
| total\_buy\_quantityInteger | 27-30 |
| total\_sell\_quantityInteger | 31-34 |
| openFloat | 35-38 |
| closeFloat | 39-42 |
| highFloat | 43-46 |
| lowFloat | 47-50 |
| change\_absoluteFloat | 55-58 |
| change\_percentFloat | 51-54 |
| 52\_week\_highFloat | 59-62 |
| 52\_week\_lowFloat | 63-66 |

##### **INDEX QUOTE**

PACKET SIZE = 43

| Attribute | Offset |
| --- | --- |
| Packet Codebyte | 0 |
| last\_priceFloat | 1-4 |
| security\_idInteger | 5-8 |
| tradablebyte | 9 |
| modebyte | 10 |
| openFloat | 11-14 |
| closeFloat | 15-18 |
| highFloat | 19-22 |
| lowFloat | 23-26 |
| change\_absoluteFloat | 27-30 |
| change\_percentFloat | 31-34 |
| 52\_week\_highFloat | 35-38 |
| 52\_week\_lowFloat | 39-42 |

##### **FULL**

PACKET SIZE = 175

| Attribute | Offset |
| --- | --- |
| Packet Codebyte | 0 |
| MBP\_ROW\_PACKET []Array Containing 5 MBP\_ROW\_PACKET | 1-100 |
| last\_priceFloat | 101-104 |
| last\_traded\_timeInteger | 105-108 |
| security\_idInteger | 109-112 |
| tradablebyte | 113 |
| modebyte | 114 |
| last\_traded\_quantityInteger | 115-118 |
| average\_traded\_priceFloat | 119-122 |
| volume\_tradedInteger | 123-126 |
| total\_buy\_quantityInteger | 127-130 |
| total\_sell\_quantityInteger | 131-134 |
| openFloat | 135-138 |
| closeFloat | 139-142 |
| highFloat | 143-146 |
| lowFloat | 147-150 |
| change\_absoluteFloat | 155-158 |
| change\_percentFloat | 151-154 |
| 52\_week\_highFloat | 159-162 |
| 52\_week\_lowFloat | 163-166 |
| OIInteger | 167-170 |
| OI\_changeInteger | 171-174 |

##### **FULL INDEX**

PACKET SIZE = 39

| Attribute | Offset |
| --- | --- |
| Packet Codebyte | 0 |
| last\_priceFloat | 1-4 |
| security\_idInteger | 5-8 |
| tradablebyte | 9 |
| modebyte | 10 |
| openFloat | 11-14 |
| closeFloat | 15-18 |
| highFloat | 19-22 |
| lowFloat | 23-26 |
| change\_percentFloat | 27-30 |
| change\_absoluteFloat | 31-34 |
| last\_trade\_timeInteger | 35-38 |

##### **CAS**

PACKET SIZE = 23

| Attribute | Offset |
| --- | --- |
| Packet Codebyte | 0 |
| indicative\_equilibrium\_priceFloat | 1-4 |
| security\_idInteger | 5-8 |
| tradablebyte | 9 |
| modebyte | 10 |
| reference\_priceFloat | 11-14 |
| imbalance\_quantityLong | 15-22 |

### Sample Client-Side Implementation

#### The following code shows an example of client-side implementation in javascript:

```
		var publicAccessToken = "YOUR_PUBLIC_ACCESS_TOKEN";
		url = 'wss://developer-ws.paytmmoney.com/broadcast/user/v1/data?' + `x_jwt_token=${publicAccessToken}`;
		
		var socket = new WebSocket(url);
		
		// Event triggered when user connection has successfully opened
		socket.addEventListener('open', function () {
			if (socket.readyState === socket.OPEN) {
				socket.send(JSON.stringify(
					[{
						"actionType": "ADD",
						"modeType": "FULL",
						"scripType": "INDEX",
						"exchangeType": "NSE",
						"scripId": "13"
					},
					{
						"actionType": "ADD",
						"modeType": "LTP",
						"scripType": "INDEX",
						"exchangeType": "BSE",
						"scripId": "51"
					}
					]
				));
			}
		})
		
		// Event triggered when user connection has closed
		socket.addEventListener('close', function (event) {
			console.log("user disconnected");
		})
		
		// Event triggered when user connection gets an error
		socket.addEventListener('error', function (event) {
			console.log("error");
		}) // Event triggered when user connection gets a message from the server
		socket.addEventListener("message", function (message) {
			try {
				if (message.data instanceof Blob) {
					processByteMessage(message);
				} else {
					console.log("Message: " + message.data);
				}
			} catch (e) {
				console.log("Error: " + e);
			}
		});
		
		function processByteMessage(message) {
			const arrayBufferPromise = message.data.arrayBuffer();
			arrayBufferPromise.then((data) => {
				var l = data.byteLength;
				var dvu = new DataView(data);
				let position = 0;
				while (position != l) {
					var type = dvu.getInt8(position);
					position = position + 1;
					console.log("Mode Type: " + type);
					switch (type) {
						case 64:
							console.log("IndexLtpPacket");
							processIndexLtpPacket(dvu);
							break;
						case 65:
							console.log("IndexQuotePacket");
							processIndexQuotePacket(dvu);
							break;
						case 66:
							console.log("IndexFullPacket");
							processIndexFullPacket(dvu);
							break;
						case 61:
							console.log("LtpPacket");
							processLtpPacket(dvu);
							break;
						case 62:
							console.log("QuotePacket");
							processQuotePacket(dvu);
							break;
						case 63:
							console.log("FullPacket");
							processFullPacket(dvu);
							break;
						default:
							console.log("Default");
							break;
					}
				}
		
				function processLtpPacket(dvu) {
					console.log("last_trade_price: " + dvu.getFloat32(position, true));
					console.log("last_trade_time: " + dvu.getInt32(position + 4, true));
					console.log("security id: " + dvu.getInt32(position + 8, true));
					console.log("traded: " + dvu.getInt8(position + 12, true));
					console.log("Mode: " + dvu.getInt8(position + 13, true));
					console.log("changeAbsolute: " + dvu.getFloat32(position + 14, true));
					console.log("changePercent: " + dvu.getFloat32(position + 18, true));
					position += 22;
				}
		
				function processIndexLtpPacket(dvu) {
					console.log("last_trade_price: " + dvu.getFloat32(position, true));
					console.log("last_update_time: " + dvu.getInt32(position + 4, true));
					console.log("security id: " + dvu.getInt32(position + 8, true));
					console.log("traded: " + dvu.getInt8(position + 12, true));
					console.log("Mode: " + dvu.getInt8(position + 13, true));
					console.log("changeAbsolute: " + dvu.getFloat32(position + 14, true));
					console.log("changePercent: " + dvu.getFloat32(position + 18, true));
					position += 22;
				}
		
				function processQuotePacket(dvu) {
					console.log("last_traded_price: " + dvu.getFloat32(position, true));
					console.log("Last_trade_time: " + dvu.getInt32(position + 4, true));
					console.log("security id: " + dvu.getInt32(position + 8, true));
					console.log("traded: " + dvu.getInt8(position + 12, true));
					console.log("Mode: " + dvu.getInt8(position + 13, true));
					console.log("last_traded_quantity " + dvu.getInt32(position + 14, true));
					console.log("average_traded_price: " + dvu.getFloat32(position + 18, true));
					console.log("volume: " + dvu.getInt32(position + 22, true));
					console.log("total_buy_quantity: " + dvu.getInt32(position + 26, true));
					console.log("total_sell_quantity: " + dvu.getInt32(position + 30, true));
					console.log("open: " + dvu.getFloat32(position + 34, true));
					console.log("close: " + dvu.getFloat32(position + 38, true));
					console.log("high: " + dvu.getFloat32(position + 42, true));
					console.log("low: " + dvu.getFloat32(position + 46, true));
					console.log("change_percent: " + dvu.getFloat32(position + 50, true));
					console.log("change_absolute: " + dvu.getFloat32(position + 54, true));
					console.log("52_week_high: " + dvu.getFloat32(position + 58, true));
					console.log("52_week_low: " + dvu.getFloat32(position + 62, true));
					position += 66;
				}
		
				function processIndexQuotePacket(dvu) {
					console.log("last_trade_price: " + dvu.getFloat32(position, true));
					console.log("security id: " + dvu.getInt32(position + 4, true));
					console.log("traded: " + dvu.getInt8(position + 8, true));
					console.log("Mode: " + dvu.getInt8(position + 9, true));
					console.log("open " + dvu.getFloat32(position + 10, true));
					console.log("close: " + dvu.getFloat32(position + 14, true));
					console.log("high: " + dvu.getFloat32(position + 18, true));
					console.log("low: " + dvu.getFloat32(position + 22, true));
					console.log("change_percent: " + dvu.getFloat32(position + 26, true));
					console.log("change_absolute: " + dvu.getFloat32(position + 30, true));
					console.log("52_week_high: " + dvu.getFloat32(position + 34, true));
					console.log("52_week_low: " + dvu.getFloat32(position + 38, true));
					position += 42;
				}
		
				function processFullPacket(dvu) {
					depthPosition = position;
					for (let i = 0; i < 5; i++) {
						console.log("DEPTH PACKET  #" + (i + 1));
						console.log("buy_quantity: " + dvu.getInt32(depthPosition, true));
						console.log("sell_quantity: " + dvu.getInt32(depthPosition + 4, true));
		
						console.log("buy_order: " + dvu.getInt16(depthPosition + 8, true));
						console.log("sell_order: " + dvu.getInt16(depthPosition + 10, true));
		
						console.log("buy_price: " + dvu.getFloat32(depthPosition + 12, true));
						console.log("sell_price: " + dvu.getFloat32(depthPosition + 16, true));
						console.log("\n");
						depthPosition += 20;
					}
		
					position += 100;
		
					console.log("last_traded_price: " + dvu.getFloat32(position, true));
					console.log("last_trade_time: " + dvu.getInt32(position + 4, true));
					console.log("security id: " + dvu.getInt32(position + 8, true));
					console.log("traded: " + dvu.getInt8(position + 12, true));
					console.log("Mode: " + dvu.getInt8(position + 13, true));
					console.log("last_traded_quantity " + dvu.getInt32(position + 14, true));
					console.log("average_traded_price: " + dvu.getFloat32(position + 18, true));
					console.log("volume: " + dvu.getInt32(position + 22, true));
					console.log("total_buy_quantity: " + dvu.getInt32(position + 26, true));
					console.log("total_sell_quantity: " + dvu.getInt32(position + 30, true));
					console.log("open: " + dvu.getFloat32(position + 34, true));
					console.log("close: " + dvu.getFloat32(position + 38, true));
					console.log("high: " + dvu.getFloat32(position + 42, true));
					console.log("low: " + dvu.getFloat32(position + 46, true));
					console.log("change_percent: " + dvu.getFloat32(position + 50, true));
					console.log("change_absolute: " + dvu.getFloat32(position + 54, true));
					console.log("52_week_high: " + dvu.getFloat32(position + 58, true));
					console.log("52_week_low: " + dvu.getFloat32(position + 62, true));
					console.log("oi: " + dvu.getInt32(position + 66, true));
					console.log("change_oi: " + dvu.getInt32(position + 70, true));
					position += 74;
				}
		
				function processIndexFullPacket(dvu) {
					console.log("last_trade_price: " + dvu.getFloat32(position, true));
					console.log("security id: " + dvu.getInt32(position + 4, true));
					console.log("traded: " + dvu.getInt8(position + 8, true));
					console.log("Mode: " + dvu.getInt8(position + 9, true));
					console.log("open " + dvu.getFloat32(position + 10, true));
					console.log("close: " + dvu.getFloat32(position + 14, true));
					console.log("high: " + dvu.getFloat32(position + 18, true));
					console.log("low: " + dvu.getFloat32(position + 22, true));
					console.log("change_percent: " + dvu.getFloat32(position + 26, true));
					console.log("change_absolute: " + dvu.getFloat32(position + 30, true));
					console.log("last_update_time: " + dvu.getInt32(position + 34, true));
					position += 38;
				}
			});
		}
```

---

## Live Market Data API

Source: https://developer.paytmmoney.com/docs/api/live-market-data-api/

**Method:** `GET`  
**Endpoint:** `https://developer.paytmmoney.com/data/v1/price/live/`  

### Description

> The Live data API enables users to fetch live market feed data via pull mode. The user may fetch data for one or more preferences in a single GET request.  
>   
>   
> The user may fetch packet with below Modes:  
>   
> **LTP Mode** : In this mode user get Last Trade Price, Last Traded Quantity, Change percentage & absolute rupees and Last Traded Time etc  
>   
> **QUOTE Mode**: In this mode user get LTP Mode features and total buy/sell Quantity, OHCL, 52 week high/Low, Average price, volume etc  
>   
> **FULL Mode**: In this mode use get all the features of LTP & Quote mode along with Best 5 buy/bid Price and Best 5 Sell/Ask price and Quantity etc  
>   
> **CAS Mode** : In this mode user get Indicative Equilibrium Price (IEP), Reference Price and Imbalance Quantity during auction windows

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `x-jwt-token` | string | mandatory | xxxxxx ( The one retrieved from Generate Access Token Steps ) . Can be accessed using: {access\_token} or {read\_access\_token} . |

### Response Attributes

Content Type: JSON

#### Body

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `LTP Response Model` | string | optional | This packet contains several fields including the last traded price |
| `LTP INDEX Response Model` | string | optional | LTP packet for INDEX scrip type containing several fields including the last traded price |
| `QUOTE Response Model` | string | optional | This packet contains several fields excluding the market depth |
| `QUOTE INDEX Response Model` | string | optional | QUOTE packet for INDEX scrip type containing several fields excluding the market depth |
| `FULL Response Model` | string | optional | This packet contains several fields including the market depth |
| `FULL INDEX Response Model` | string | optional | FULL packet for INDEX scrip type containing several fields excluding 52 Week high and low |
| `No Packet Found` | string | optional | If No Packet was Found for the given Preference |

### Code Samples

#### CURL

```bash
curl --location --request GET 'https://developer.paytmmoney.com/data/v1/price/live?mode={MODE_TYPE}&pref={PREFERENCES}' \
--header 'x-jwt-token: {YOUR_JWT_TOKEN}'
```

### Sample Responses

#### SUCCESS

```json

// LTP Response Model
{
    "data": [
        {
            "tradable": true,
            "mode": "LTP",
            "security_id": 3456,
            "last_price": 423.75,
            "change_percent": 1.8,
            "change_absolute": 7.5,
            "last_trade_time": 1352018334,
            "found": true
        }
    ]
}
// LTP INDEX Response Model
{
    "data": [
        {
            "tradable": false,
            "mode": "LTP",
            "security_id": 13,
            "last_price": 18054.15,
            "change_percent": 0.01,
            "change_absolute": 1.4511719,
            "last_update_time": 1352017943,
            "found": true
        }
    ]
}
// QUOTE Response Model
{
    "data": [
        {
            "tradable": true,
            "mode": "QUOTE",
            "security_id": 3456,
            "last_price": 424.0,
            "last_traded_quantity": 10,
            "average_traded_price": 421.84,
            "volume_traded": 8782174,
            "total_buy_quantity": 1118828,
            "total_sell_quantity": 1788524,
            "ohlc": {
                "open": 418.2,
                "high": 425.0,
                "low": 416.9,
                "close": 416.25
            },
            "change_percent": 1.86,
            "change_absolute": 7.75,
            "52_week_high": 536.7,
            "52_week_low": 366.2,
            "last_trade_time": 1352018028,
            "found": true
        }
    ]
}
// QUOTE INDEX Response Model
{
    "data": [
        {
            "tradable": false,
            "mode": "QUOTE",
            "security_id": 13,
            "last_price": 18053.6,
            "ohlc": {
                "open": 18053.4,
                "high": 18108.0,
                "low": 18017.15,
                "close": 18052.7
            },
            "change_percent": 0.0,
            "change_absolute": 0.9003906,
            "52_week_high": 18350.95,
            "52_week_low": 15183.4,
            "found": true
        }
    ]
}
// FULL Response Model
{
    "data": [
        {
            "tradable": true,
            "mode": "FULL",
            "security_id": 3456,
            "last_price": 423.85,
            "last_traded_quantity": 1,
            "average_traded_price": 421.84,
            "volume_traded": 8780591,
            "total_buy_quantity": 1115999,
            "total_sell_quantity": 1787096,
            "ohlc": {
                "open": 418.2,
                "high": 425.0,
                "low": 416.9,
                "close": 416.25
            },
            "change_percent": 1.83,
            "change_absolute": 7.6,
            "52_week_high": 536.7,
            "52_week_low": 366.2,
            "last_trade_time": 1352018011,
            "oi": 0,
            "change_oi": 0,
            "depth": {
                "buy": [
                    {
                        "quantity": 1628,
                        "price": 423.85,
                        "orders": 13
                    },
                    {
                        "quantity": 5880,
                        "price": 423.8,
                        "orders": 27
                    },
                    {
                        "quantity": 5099,
                        "price": 423.75,
                        "orders": 18
                    },
                    {
                        "quantity": 8196,
                        "price": 423.7,
                        "orders": 28
                    },
                    {
                        "quantity": 6140,
                        "price": 423.65,
                        "orders": 21
                    }
                ],
                "sell": [
                    {
                        "quantity": 33,
                        "price": 424.0,
                        "orders": 1
                    },
                    {
                        "quantity": 3335,
                        "price": 424.05,
                        "orders": 6
                    },
                    {
                        "quantity": 1055,
                        "price": 424.1,
                        "orders": 9
                    },
                    {
                        "quantity": 2641,
                        "price": 424.15,
                        "orders": 14
                    },
                    {
                        "quantity": 7722,
                        "price": 424.2,
                        "orders": 20
                    }
                ]
            },
            "found": true
        }
    ]
}
// FULL INDEX Response Model
{
    "data": [
        {
            "tradable": false,
            "mode": "FULL",
            "security_id": 13,
            "last_price": 18054.1,
            "ohlc": {
                "open": 18053.4,
                "high": 18108.0,
                "low": 18017.15,
                "close": 18052.7
            },
            "change_percent": 0.01,
            "change_absolute": 1.4003906,
            "last_update_time": 1352017988,
            "found": true
        }
    ]
}
// No Packet Response Model
{
    "data": [
        {
            "mode": "LTP",
            "security_id": 123,
            "found": false
        }
    ]
}
```

#### FAIL

```json
// 400
{
    "status": 400,
    "message": "Bad Request",
    "error_code": "PM_OPEN_API_400"
}

// 401
{
    "status": 401,
    "message": "Invalid Access Token",
    "error_code": "PM_OPEN_API_0001"
}

// 403
{
    "status": 403,
    "message": "Forbidden",
    "error_code": "PM_OPEN_API_403"
}

// 500 
{
    "status": 500,
    "message": "Unexpected Error",
    "error_code": "PM_OPEN_API_500"
}
```

### Possible Response Status

| Code | Status | Message |
| --- | --- | --- |
| 400 | FAILURE | Bad Request |
| 401 | FAILURE | Authentication required |
| 403 | FAILURE | Forbidden |
| 500 | FAILURE | Refer Error Model |

### Notes

##### **Query Param**

| Key/Parameter | Value | Description |
| --- | --- | --- |
| modestring  mandatory | Available values: LTP, QUOTE, FULL | mode of preference |
| prefarray of string  mandatory | Preference Structure:  {Exchange}:{ScripId}:{ScripType} | Field | Value | | --- | --- | | Exchange | NSE or BSE | | ScripId | Security id | | ScripType | INDEX, EQUITY, ETF, FUTURE, OPTION | | list of preferences, containing one or more preferences, for which the client requires data |

##### **LTP**

| Attribute | Description |
| --- | --- |
| tradableBoolean | T/F. True if stock is tradable else false |
| modeString | Type of Packet LTP/QUOTE/FULL/CAS |
| security\_idInteger | Security Id for which broadcast is received |
| last\_priceFloat | Last traded market price |
| change\_percentFloat | The absolute percentage price change of the security's price since the previous day's close |
| change\_absoluteFloat | The absolute change in security's price since the previous day's close |
| last\_trade\_timeInteger | Last trade timestamp |
| foundBoolean | true if data for a given preference was found, else false |

##### **INDEX LTP**

| Attribute | Description |
| --- | --- |
| tradableBoolean | T/F. True if stock is tradable else false |
| modeString | Type of Packet LTP/QUOTE/FULL/CAS |
| security\_idInteger | Security Id for which broadcast is received |
| last\_priceFloat | Last traded market price |
| change\_percentFloat | The absolute percentage price change of the security's price since the previous day's close |
| change\_absoluteFloat | The absolute change in security's price since the previous day's close |
| last\_update\_timeInteger | Last update timestamp |
| foundBoolean | true if data for a given preference was found, else false |

##### **QUOTE**

| Attribute | Description |
| --- | --- |
| tradableBoolean | T/F. True if stock is tradable else false |
| modeString | Type of Packet LTP/QUOTE/FULL/CAS |
| security\_idInteger | Security Id for which broadcast is received |
| last\_priceFloat | Last traded market price |
| last\_traded\_quantityInteger | Last traded quantity |
| average\_traded\_priceFloat | Average traded market price |
| volume\_tradedInteger | Volume traded today |
| total\_buy\_quantityInteger | Total quantity of buy orders pending at the exchange |
| total\_sell\_quantityInteger | Total quantity of sell orders pending at the exchange |
| ohlcObject | ohlc data for the scrip  | Attribute | Description | | --- | --- | | open | Price when the market opened | | high | Highest price today | | low | Lowest price today | | close | Closing price of the instrument from the last trading day | |
| change\_percentFloat | The absolute percentage price change of the security's price since the previous day's close |
| change\_absoluteFloat | The absolute change in security's price since the previous day's close |
| 52\_week\_highFloat | The highest price at which a security has traded during the time period that equates to one year |
| 52\_week\_lowInteger | The lowest price at which a security has traded during the time period that equates to one year |
| last\_trade\_timeInteger | Last trade timestamp |
| foundBoolean | true if data for a given preference was found, else false |

##### **INDEX QUOTE**

| Attribute | Description |
| --- | --- |
| tradableBoolean | T/F. True if stock is tradable else false |
| modeString | Type of Packet LTP/QUOTE/FULL/CAS |
| security\_idInteger | Security Id for which broadcast is received |
| last\_priceFloat | Last traded market price |
| ohlcObject | ohlc data for the scrip  | Attribute | Description | | --- | --- | | open | Price when the market opened | | high | Highest price today | | low | Lowest price today | | close | Closing price of the instrument from the last trading day | |
| change\_percentFloat | The absolute percentage price change of the security's price since the previous day's close |
| change\_absoluteFloat | The absolute change in security's price since the previous day's close |
| 52\_week\_highFloat | The highest price at which a security has traded during the time period that equates to one year |
| 52\_week\_lowInteger | The lowest price at which a security has traded during the time period that equates to one year |
| foundBoolean | true if data for a given preference was found, else false |

##### **FULL**

| Attribute | Description |
| --- | --- |
| tradableBoolean | T/F. True if stock is tradable else false |
| modeString | Type of Packet LTP/QUOTE/FULL/CAS |
| security\_idInteger | Security Id for which broadcast is received |
| last\_priceFloat | Last traded market price |
| last\_traded\_quantityInteger | Last traded quantity |
| average\_traded\_priceFloat | Average traded market price |
| volume\_tradedInteger | Volume traded today |
| total\_buy\_quantityInteger | Total quantity of buy orders pending at the exchange |
| total\_sell\_quantityInteger | Total quantity of sell orders pending at the exchange |
| ohlcObject | ohlc data for the scrip  | Attribute | Description | | --- | --- | | open | Price when the market opened | | high | Highest price today | | low | Lowest price today | | close | Closing price of the instrument from the last trading day | |
| change\_percentFloat | The absolute percentage price change of the security's price since the previous day's close |
| change\_absoluteFloat | The absolute change in security's price since the previous day's close |
| 52\_week\_highFloat | The highest price at which a security has traded during the time period that equates to one year |
| 52\_week\_lowInteger | The lowest price at which a security has traded during the time period that equates to one year |
| last\_trade\_timeInteger | Last trade timestamp |
| oiInteger | Number of future and option contracts traded but not yet liquidated |
| change\_oiInteger | The change in the number of option contracts traded but not yet liquidated |
| depthObject | best buy & sell data  | Attribute | Description | | --- | --- | | buy | 5 best buy prices, quantity & open orders at the price  | Attribute | Description | | --- | --- | | quantity | Net quantity from the pending orders | | price | Price at which the buy order depth stands | | orders | Number of open buy orders at the price | | | sell | 5 best sell prices, quantity & open orders at the price  | Attribute | Description | | --- | --- | | quantity | Net quantity from the pending orders | | price | Price at which the sell order depth stands | | orders | Number of open sell orders at the price | | |

##### **INDEX FULL**

| Attribute | Description |
| --- | --- |
| tradableBoolean | T/F. True if stock is tradable else false |
| modeString | Type of Packet LTP/QUOTE/FULL/CAS |
| security\_idInteger | Security Id for which broadcast is received |
| last\_priceFloat | Last traded market price |
| ohlcObject | ohlc data for the scrip  | Attribute | Description | | --- | --- | | open | Price when the market opened | | high | Highest price today | | low | Lowest price today | | close | Closing price of the instrument from the last trading day | |
| change\_percentFloat | The absolute percentage price change of the security's price since the previous day's close |
| change\_absoluteFloat | The absolute change in security's price since the previous day's close |
| last\_update\_timeInteger | Last update timestamp |
| foundBoolean | true if data for a given preference was found, else false |

##### **CAS**

| Attribute | Description |
| --- | --- |
| tradableBoolean | T/F. True if stock is tradable else false |
| modeString | Type of Packet LTP/QUOTE/FULL/CAS |
| security\_idInteger | Security Id for which broadcast is received |
| iepFloat | The real-time, volume-maximizing price calculated dynamically during call auction sessions before the final market price is locked |
| reference\_priceFloat | The base price used to calculate the ±3% operating band and fallback closing price for the Closing Auction Session (CAS) |
| imbalance\_qtyLong | The un-matchable surplus buy or sell volume remaining at the Indicative Equilibrium Price (IEP) during a call auction session |
| foundBoolean | true if data for a given preference was found, else false |

##### **No Packet was Found for the given Preference**

| Attribute | Description |
| --- | --- |
| modeString | Type of Packet LTP/QUOTE/FULL |
| security\_idInteger | Security Id for which broadcast is received |
| foundBoolean | true if data for a given preference was found, else false |

---

## test

Source: https://developer.paytmmoney.com/docs/api/create-test/

**Method:** `POST`  

### Description

> test orders

### Request Attributes

Content Type: JSON

#### Head

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `test-header` | string | optional | xxxxxx pass header for test |
