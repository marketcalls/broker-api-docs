<!-- Source: https://smartapi.angelone.in/docs -->
<!-- Section: Live Market Data API -->

# Live Market Data API

The Live Market Data API provides real-time market data for specific symbols, allowing clients to make informed trading and investment decisions. The API offers three distinct modes: LTP, OHLC, and FULL, each delivering varying levels of comprehensive market information.

```
https://apiconnect.angelone.in/rest/secure/angelbroking/market/v1/quote/
```

## Modes

| Modes | Description |
| --- | --- |
| LTP Mode | Retrieve the latest Last Traded Price (LTP) for a specified exchange and symbol. |
| OHLC Mode | Retrieve the Open, High, Low, and Close prices for a given exchange and symbol. |
| Full Mode | Access an extensive set of data for a specified exchange and symbol. This mode provides a comprehensive range of data points, including LTP, open, high, low, close prices, last trade quantity, exchange feed time, exchange trade time, net change, percent change, average price, trade volume, open interest, circuit limits, total buying and selling quantity, 52-week low, 52-week high, and depth information for the best five buy and sell orders. |

## Supported Exchanges

All exchanges are supported.

## Number of tokens supported in one request:

The market data API allows you to fetch data for 50 symbols in just one request with a rate limit of 1 request per second

## Request Format

| Mode | Sample Request |
| --- | --- |
| Full Mode | { "mode": "FULL", "exchangeTokens": { "NSE": ["3045","881"], "NFO": ["58662"]} } |
| OHLC Mode | { "mode": "OHLC", "exchangeTokens": { "NSE": ["3045","881"], "NFO": ["58662"]} } |
| LTP Mode | { "mode": "LTP", "exchangeTokens": { "NSE": ["3045","881"], "NFO": ["58662"]} } |

## Response Format

The response is a JSON object containing the requested stock market data:

1. status: A boolean indicating whether the request was successful.
2. message: A string describing the status of the request.
3. errorcode: A string providing specific error codes, if any.
4. data: An object containing the fetched market data and any unfetched data with errors.

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data": {
"fetched": [
{
"exchange": "NSE",
"tradingSymbol": "SBIN-EQ",
"symbolToken": "3045",
"ltp": 568.2,
"open": 567.4,
"high": 569.35,
"low": 566.1,
"close": 567.4,
"lastTradeQty": 1,
"exchFeedTime": "21-Jun-2023 10:46:10",
"exchTradeTime": "21-Jun-2023 10:46:09",
"netChange": 0.8,
"percentChange": 0.14,
"avgPrice": 567.83,
"tradeVolume": 3556150,
"opnInterest": 0,
"lowerCircuit": 510.7,
"upperCircuit": 624.1,
"totBuyQuan": 839549,
"totSellQuan": 1284767,
"52WeekLow": 430.7,
"52WeekHigh": 629.55,
"depth": {
"buy": [
{
"price": 568.2,
"quantity": 511,
"orders": 2
},
{
"price": 568.15,
"quantity": 411,
"orders": 2
}
],
"sell": [
{
"price": 568.25,
"quantity": 3348,
"orders": 5
}
]
}
}
],
"unfetched": []
}
}
```

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data":{
"fetched":[
{
"exchange": "NSE",
"tradingSymbol": "SBIN-EQ",
"symbolToken": "3045",
"ltp": 571.8,
"open": 568.75,
"high": 568.75,
"low": 567.05,
"close": 566.5
}
],
"unfetched": []
}
}
```

```json
{
"status": true,
"message": "SUCCESS",
"errorcode": "",
"data":{
"fetched":[
{
"exchange": "NSE",
"tradingSymbol": "SBIN-EQ",
"symbolToken": "3045",
"ltp": 571.75,
}
],
"unfetched": []
}
}
```

```json
{
"success": true,
"message": "SUCCESS",
"errorCode": "",
"data":{
"fetched": [],
"unfetched":[
{
"exchange": "MCX",
"symbolToken": "",
"message": "Symbol token cannot be empty",
"errorCode": "AB4018"
}
]
}
}
```

## Field Description

| Field | Data Type | Description |
| --- | --- | --- |
| success | Boolean | Indicates whether the API request was successful. |
| message | String | Provides success or error message. |
| errorCode | String | Displays the error code if there was an issue with the request. Otherwise, it is blank. |
| data | Object | Contains the fetched and unfetched data. |
| data.fetched | Array | Array of fetched data objects. |
| exchange | Enum ( Values - NSE, NFO,BSE, MCX, CDS, NCDEX ) | The exchange for the fetched data. |
| tradingSymbol | String | The trading symbol for the fetched data. |
| symbolToken | String | The token for the fetched symbol. |
| ltp | Float | The last trading price for the fetched symbol. |
| open | Float | The opening price for the fetched symbol. |
| high | Float | The highest price for the fetched symbol. |
| low | Float | The lowest price for the fetched symbol. |
| close | Float | The previous closing price for the fetched symbol. |
| lastTradeQty | Integer | The quantity of the last trade executed for the fetched symbol. |
| exchFeedTime | String | The exchange feed time for the fetched symbol. |
| exchTradeTime | String | The exchange trade time for the fetched symbol. |
| netChange | Float | The net change for the fetched symbol. |
| percentChange | Float | The percent change for the fetched symbol. |
| avgPrice | Float | The average price for the fetched symbol. |
| tradeVolume | Integer | The trade volume for the fetched symbol. |
| opnInterest | Integer | The open interest for the fetched symbol. |
| upperCircuit | Float | Maximum price increase allowed before trading pauses temporarily. |
| lowerCircuit | Float | Maximum price decrease allowed before trading pauses temporarily. |
| totBuyQuan | Integer | The total buy quantity for the fetched symbol. |
| totSellQuan | Integer | The total sell quantity for the fetched symbol. |
| 52WeekHigh | Float | The yearly highest price for the fetched symbol. |
| 52WeekLow | Float | The yearly lowest price for the fetched symbol. |
| depth.buy | Array | Array of buy depth objects. |
| depth.buy[n].price | Float | The price at the nth level of buy depth. |
| depth.buy[n].quantity | Integer | The quantity at the nth level of buy depth. |
| depth.buy[n].orders | Integer | The number of buy orders at the nth level of market depth. |
| depth.sell | Array | Array of sell depth objects. |
| depth.sell[n].price | Float | The price at the nth level of sell depth. |
| depth.sell[n].quantity | Integer | The quantity at the nth level of sell depth. |
| depth.sell[n].orders | Integer | The number of sell orders at the nth level of market depth. |

**Python**

```python
import http.client

conn = http.client.HTTPSConnection("apiconnect.angelone.in")
payload = {
    "mode": "FULL",
    "exchangeTokens": {
        "NSE": ["3045"]
    }
}
headers = {
  'X-PrivateKey': 'API_KEY',
  'Accept': 'application/json',
  'X-SourceID': 'WEB',
  'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
  'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
  'X-MACAddress': 'MAC_ADDRESS',
  'X-UserType': 'USER',
  'Authorization': 'Bearer AUTHORIZATION_TOKEN',
  'Accept': 'application/json',
  'X-SourceID': 'WEB',
  'Content-Type': 'application/json'
}
conn.request("POST", "rest/secure/angelbroking/market/v1/quote/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**NodeJs**

```javascript
var axios = require('axios');
var data = JSON.stringify({
    "mode": "FULL",
    "exchangeTokens": {
        "NSE": ["3045"]
    }
});

var config = {
  method: 'post',
  url: 'https://apiconnect.angelone.in/
  rest/secure/angelbroking/market/v1/quote/',
  headers: {
    'X-PrivateKey': 'API_KEY',
    'Accept': 'application/json, application/json',
    'X-SourceID': 'WEB, WEB',
    'X-ClientLocalIP': 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP': 'CLIENT_PUBLIC_IP',
    'X-MACAddress': 'MAC_ADDRESS',
    'X-UserType': 'USER',
    'Authorization': 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type': 'application/json'
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
```

**Java**

```java
OkHttpClient client = new OkHttpClient().newBuilder()
  .build();
MediaType mediaType = MediaType.parse("application/json");
RequestBody body = RequestBody.create(mediaType, "{\r\n   \"mode\": \"FULL\",\r\n   \"exchangeTokens\": { \"NSE\": [\"3045\"] }\r\n}");
Request request = new Request.Builder()
  .url("https://apiconnect.angelone.in/rest/secure/angelbroking/market/v1/quote/")
  .method("POST", body)
  .addHeader("X-PrivateKey", "API_KEY")
  .addHeader("Accept", "application/json")
  .addHeader("X-SourceID", "WEB")
  .addHeader("X-ClientLocalIP", "CLIENT_LOCAL_IP")
  .addHeader("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
  .addHeader("X-MACAddress", "MAC_ADDRESS")
  .addHeader("X-UserType", "USER")
  .addHeader("Authorization", "Bearer AUTHORIZATION_TOKEN")
  .addHeader("Accept", "application/json")
  .addHeader("X-SourceID", "WEB")
  .addHeader("Content-Type", "application/json")
  .build();
Response response = client.newCall(request).execute();
```

**R**

```r
library(httr)

url <- "https://apiconnect.angelone.in/
rest/secure/angelbroking/market/v1/quote/"
json_body <- jsonlite::toJSON(list(
  mode = "FULL",
  exchangeTokens = list(
    NSE = list("3045")
  )
))

response <- POST(url,
    config = list(
    add_headers(
    'Authorization'= 'Bearer AUTHORIZATION_TOKEN',
    'Content-Type'= 'application/json',
    'Accept'= 'application/json',
    'X-UserType'= 'USER',
    'X-SourceID'= 'WEB',
    'X-ClientLocalIP'= 'CLIENT_LOCAL_IP',
    'X-ClientPublicIP'= 'CLIENT_PUBLIC_IP',
    'X-MACAddress'= 'MAC_ADDRESS',
    'X-PrivateKey'= 'API_KEY'
    ))
    ),
    body = json_body,
    encode = "raw"

print(response)
```

**GO**

```go
package main

 import (
   "fmt"
   "strings"
   "net/http"
   "io/ioutil"
 )

 func main() {

   url := "https://apiconnect.angelone.in/
   rest/secure/angelbroking/market/v1/quote/"
   method := "POST"

   payload := strings.NewReader({
		"mode": "FULL",
		"exchangeTokens": {
			"NSE": ["3045"]
		}
	})

   client := &http.Client {
   }
   req, err := http.NewRequest(method, url, payload)

   if err != nil {
     fmt.Println(err)
     return
   }
   req.Header.Add("X-PrivateKey", "API_KEY")
   req.Header.Add("Accept", "application/json")
   req.Header.Add("X-SourceID", "WEB")
   req.Header.Add("X-ClientLocalIP", "CLIENT_LOCAL_IP")
   req.Header.Add("X-ClientPublicIP", "CLIENT_PUBLIC_IP")
   req.Header.Add("X-MACAddress", "MAC_ADDRESS")
   req.Header.Add("X-UserType", "USER")
   req.Header.Add("Authorization", "Bearer AUTHORIZATION_TOKEN")
   req.Header.Add("X-PrivateKey", "API_KEY")
   req.Header.Add("Accept", "application/json")
   req.Header.Add("X-SourceID", "WEB")
   req.Header.Add("Content-Type", "application/json")

   res, err := client.Do(req)
   if err != nil {
     fmt.Println(err)
     return
   }
   defer res.Body.Close()

   body, err := ioutil.ReadAll(res.Body)
   if err != nil {
     fmt.Println(err)
     return
   }
   fmt.Println(string(body))
 }
```
