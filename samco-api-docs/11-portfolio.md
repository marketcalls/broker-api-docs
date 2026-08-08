# Portfolio

Positions, product conversion, square-off, holdings, and the trade book.

## User Positions

`GET /position/getPositions`

Get position details of the user (The details of equity, derivative, commodity, currency borrowed or owned by the user).

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `positionType` | string | true | Position type can be DAY/NET. If Position type is “DAY”, fetch current day position details. If Position Type is “NET”, fetch carry forward position details. |

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/position/getPositions?positionType=DAY' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/position/getPositions?positionType=DAY"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .GET()
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-session-token': '<SESSION_TOKEN>',
  };

  const response = await fetch('https://tradeapi.samco.in/position/getPositions?positionType=DAY', {
    method: 'GET',
    headers,
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-session-token': '<SESSION_TOKEN>',
}

r = requests.get('https://tradeapi.samco.in/position/getPositions?positionType=DAY',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "status": "Success",
  "statusMessage": "Request successful",
  "positionSummary": {
    "gainingTodayCount": "2",
    "losingTodayCount": "2",
    "totalGainAndLossAmount": "0.00",
    "dayGainAndLossAmount": "-4910.00"
  },
  "positionDetails": [
    {
      "averagePrice": "1560.15",
      "exchange": "BSE",
      "markToMarketPrice": "-182.70",
      "lastTradedPrice": "1,550.00",
      "previousClose": "1552.55",
      "productCode": "CNC",
      "symbolDescription": "RELIANCE INDUSTRIES LTD.",
      "tradingSymbol": "RELIANCE",
      "calculatedNetQuantity": "18.0",
      "averageBuyPrice": "1560.15",
      "averageSellPrice": "0.00",
      "boardLotQuantity": "1",
      "boughtPrice": "28082.70",
      "buyQuantity": "18",
      "carryForwardQuantity": "0",
      "carryForwardValue": "0.00",
      "multiplier": "1",
      "netPositionValue": "-182.70",
      "netQuantity": "18",
      "netValue": "-182.70",
      "positionType": "DAY",
      "positionConversions": "CNC, NRML",
      "soldValue": "0.00",
      "transactionType": "BUY",
      "realizedGainAndLoss": "0.00",
      "unrealizedGainAndLoss": "-182.70",
      "companyName": "RELIANCE INDUSTRIES LTD.",
      "expiryDate": "--",
      "optionType": "--"
    }
  ]
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | Response status. Can be Success or Failure |
| `statusMessage` | string | status Message |
| `positionSummary` | object | none |
| `gainingTodayCount` | string | Count of scrips which are gaining in value in a trading day |
| `losingTodayCount` | string | Count of scrips which are losing in value in a trading day |
| `totalGainAndLossAmount` | string | Total amount of Gain / Loss for all existing positions since their creation |
| `dayGainAndLossAmount` | string | Amount of Gain / Loss for all positions on a specific trading day |
| `positionDetails` | [object] | Details of Day/Net positions as queried |
| `averagePrice` | string | Average trading price of the equity |
| `exchange` | string | Name of the exchange. Valid exchanges values (BSE/ NSE) If the user does not provide an exchange name, by default considered as NSE. |
| `markToMarketPrice` | string | Price change between previous close price and current price |
| `lastTradedPrice` | string | Price at which last transaction/trade is done |
| `previousClose` | string | Previous close refers to the prior day's final price of security when the market officially closes for the day. |
| `productCode` | string | Type of the product, allowable type is CNC |
| `symbolDescription` | string | Scrip Description |
| `tradingSymbol` | string | Symbol name of the scrip. |
| `calculatedNetQuantity` | string | Quantity left after the day |
| `averageBuyPrice` | string | Average price at which the quantities were bought |
| `averageSellPrice` | string | Average price at which the quantities were sold |
| `boardLotQuantity` | string | The standardized number of shares decided by the exchange as a trading unit |
| `boughtPrice` | string | Price at which quantities were bought during the day |
| `buyQuantity` | string | Total quantity brought and added to the position during the day |
| `carryForwardQuantity` | string | Quantity bought or sold in previous session |
| `carryForwardValue` | string | Net value of the position in previous session |
| `multiplier` | string | The lot size multiplier used to calculate Profit and Loss |
| `netPositionValue` | string | Net value of the position during the day |
| `netQuantity` | string | Limit quantity of the position |
| `netValue` | string | Net value of the bought quantities |
| `positionType` | string | Type of the position, Ex -Day/Net |
| `positionConversions` | [string] | Different Product types the user can Convert an existing position to |
| `soldValue` | string | Total value of sold quantities |
| `transactionType` | string | Type of the transaction, BUY / SELL |
| `realizedGainAndLoss` | string | The Profit and Loss returns from a closed position |
| `unrealizedGainAndLoss` | string | The Profit and Loss returns from an open position |
| `companyName` | string | Full name of the trading company |
| `expiryDate` | string | Expiry date of the scrip |
| `optionType` | string | Option Type (PE/CE). |

---

## Position Conversion

`POST /position/convertPosition`

Convert an existing position of a margin product to a different margin product type. All or a subset of an existing position quantity can be converted to a different product type.The available margin product types are MARGIN_INTRADAY_SQUAREOFF(MIS), CASHNCARRY(CNC), NORMAL(NRML).

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `body` | object | false | none |
| `symbolName` | string | true | Symbol name of the scrip |
| `exchange` | string | true | Name of the exchange. If the user does not provide an exchange name, by default considered as NSE |
| `transactionType` | string | true | Transaction type can be either BUY or SELL |
| `positionType` | string | true | DAY or NET |
| `netQuantity` | string | true | Total quantity of the position |
| `quantityToConvert` | string | true | Quantity to be converted. Can be less than or equal to netQuantity |
| `fromProductType` | string | true | The existing product type of the position. It can be CNC (Cash and Carry), NRML (Normal), MIS (Intraday) |
| `toProductType` | string | true | The target product type user wants to convert to. It can be CNC (Cash and Carry), NRML (Normal), MIS (Intraday) |

### Sample Request Body

```json
requestBody={
  "symbolName": "RELIANCE",
  "exchange": "BSE",
  "transactionType": "BUY",
  "positionType": "DAY",
  "netQuantity": "18",
  "quantityToConvert": "2",
  "fromProductType": "MIS",
  "toProductType": "CNC"
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/position/convertPosition' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"symbolName":"RELIANCE","exchange":"BSE","transactionType":"BUY","positionType":"DAY","netQuantity":"18","quantityToConvert":"2","fromProductType":"MIS","toProductType":"CNC"}'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    String requestBody = """
        {
          "symbolName": "RELIANCE",
          "exchange": "BSE",
          "transactionType": "BUY",
          "positionType": "DAY",
          "netQuantity": "18",
          "quantityToConvert": "2",
          "fromProductType": "MIS",
          "toProductType": "CNC"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/position/convertPosition"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .POST(HttpRequest.BodyPublishers.ofString(requestBody))
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-session-token': '<SESSION_TOKEN>',
  };

  const requestBody = {
    symbolName: "RELIANCE",
    exchange: "BSE",
    transactionType: "BUY",
    positionType: "DAY",
    netQuantity: "18",
    quantityToConvert: "2",
    fromProductType: "MIS",
    toProductType: "CNC"
  };

  const response = await fetch('https://tradeapi.samco.in/position/convertPosition', {
    method: 'POST',
    headers,
    body: JSON.stringify(requestBody),
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-session-token': '<SESSION_TOKEN>',
}

requestBody = {
  "symbolName": "RELIANCE",
  "exchange": "BSE",
  "transactionType": "BUY",
  "positionType": "DAY",
  "netQuantity": "18",
  "quantityToConvert": "2",
  "fromProductType": "MIS",
  "toProductType": "CNC"
}

r = requests.post('https://tradeapi.samco.in/position/convertPosition',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "status": "Success",
  "statusMsg": "Position Conversion from MIS to CNC successful"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | Status of the position conversion request. Success / Failure |
| `statusMsg` | string | Status message of position conversion request |

---

## Position Square Off

`POST /position/squareOff`

SqareOff existing position. Mostly used in day trading, in which user buy or sell a particular quantity of a stock and later in the day reverse the transaction to earn a profit.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `positionSquareOffRequestList` | Array | true | List of position square-off requests |
| `exchange` | String | true | Exchange code (e.g., NSE, BSE) |
| `symbolName` | String | true | Symbol name (e.g., TCS, INFY) |
| `productType` | String | true | Product type (e.g., MIS) |
| `netQuantity` | String | true | Net quantity of the position |
| `transactionType` | String | true | Transaction type (e.g., BUY, SELL) |

### Sample Request Body

```json
requestBody={

  "positionSquareOffRequestList": [
    {
      "exchange": "NSE",
      "symbolName": "TCS",
      "productType": "MIS",
      "netQuantity": "250",
      "transactionType": "BUY"
    },
    {
      "exchange": "BSE",
      "symbolName": "INFY",
      "productType": "MIS",
      "netQuantity": "25",
      "transactionType": "SELL"
    }
  ]
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/position/squareOff' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"positionSquareOffRequestList":[{"exchange":"NSE","symbolName":"TCS","productType":"MIS","netQuantity":"250","transactionType":"BUY"},{"exchange":"BSE","symbolName":"INFY","productType":"MIS","netQuantity":"25","transactionType":"SELL"}]}'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    String requestBody = """
        {
          "positionSquareOffRequestList": [
            {
              "exchange": "NSE",
              "symbolName": "TCS",
              "productType": "MIS",
              "netQuantity": "250",
              "transactionType": "BUY"
            },
            {
              "exchange": "BSE",
              "symbolName": "INFY",
              "productType": "MIS",
              "netQuantity": "25",
              "transactionType": "SELL"
            }
          ]
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/position/squareOff"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .POST(HttpRequest.BodyPublishers.ofString(requestBody))
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-session-token': '<SESSION_TOKEN>',
  };

  const requestBody = {
    positionSquareOffRequestList: [
      {
        exchange: "NSE",
        symbolName: "TCS",
        productType: "MIS",
        netQuantity: "250",
        transactionType: "BUY"
      },
      {
        exchange: "BSE",
        symbolName: "INFY",
        productType: "MIS",
        netQuantity: "25",
        transactionType: "SELL"
      }
    ]
  };

  const response = await fetch('https://tradeapi.samco.in/position/squareOff', {
    method: 'POST',
    headers,
    body: JSON.stringify(requestBody),
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-session-token': '<SESSION_TOKEN>',
}

requestBody = {
  "positionSquareOffRequestList": [
    {
      "exchange": "NSE",
      "symbolName": "TCS",
      "productType": "MIS",
      "netQuantity": "250",
      "transactionType": "BUY"
    },
    {
      "exchange": "BSE",
      "symbolName": "INFY",
      "productType": "MIS",
      "netQuantity": "25",
      "transactionType": "SELL"
    }
  ]
}

r = requests.post('https://tradeapi.samco.in/position/squareOff',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "positionSquareOffResponseList": [
    {
      "serverTime": "12/12/19 16:20:11",
      "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
      "status": "Success",
      "statusMessage": "Request successful"
    }
  ]
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | String | Time at Server. |
| `msgId` | String | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `positionSquareOffResponseList` | Array | List of the PositionSquareOff end of the day. |
| `status` | String | Response status. Can be Success or Failure. |
| `statusMessage` | String | Status Message. |

---

## User Holdings

`GET /holding/getHoldings`

Get the details of the Stocks which client is holding. Here, you will be able to get the Client holdings which are bought under ‘CNC’ product type and are not sold yet.

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/holding/getHoldings' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/holding/getHoldings"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .GET()
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-session-token': '<SESSION_TOKEN>',
  };

  const response = await fetch('https://tradeapi.samco.in/holding/getHoldings', {
    method: 'GET',
    headers,
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-session-token': '<SESSION_TOKEN>',
}

r = requests.get('https://tradeapi.samco.in/holding/getHoldings',
  headers=headers)

print(r.json())
```

### Sample Response

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "status": "Success",
  "statusMessage": "Request successful",
  "holdingSummary": {
    "gainingTodayCount": "2",
    "losingTodayCount": "2",
    "totalGainAndLossAmount": "0.00",
    "dayGainAndLossAmount": "-4910.00",
    "portfolioValue": "343.80"
  },
  "holdingDetails": [
    {
      "averagePrice": "1560.15",
      "exchange": "BSE",
      "markToMarketPrice": "-182.70",
      "lastTradedPrice": "1,550.00",
      "previousClose": "1552.55",
      "productCode": "CNC",
      "symbolDescription": "RELIANCE INDUSTRIES LTD.",
      "tradingSymbol": "RELIANCE",
      "totalGainAndLoss": "0.00",
      "calculatedNetQuantity": "18.0",
      "holdingsQuantity": "3",
      "collateralQuantity": "2",
      "holdingsValue": "436.46",
      "isin": "INE917I01010",
      "sellableQuantity": "1",
      "totalMarketToMarketPrice": "0"
    }
  ]
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | String | Time at Server. |
| `msgId` | String | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | String | Response status. Can be Success or Failure. |
| `statusMessage` | String | Status Message. |
| `holdingSummary` | Object | None. |
| `gainingTodayCount` | String | Count of scrips which are gaining in value in a trading day. |
| `losingTodayCount` | String | Count of scrips which are losing in value in a trading day. |
| `totalGainAndLossAmount` | String | Total amount of Gain / Loss for all existing positions since their creation. |
| `dayGainAndLossAmount` | String | Amount of Gain / Loss for all positions on a specific trading day. |
| `portfolioValue` | String | Value of the portfolio. |
| `holdingDetails` | Array | Details of the user holdings. |
| `averagePrice` | String | Average trading price of the equity. |
| `exchange` | String | Name of the exchange. Valid exchange values (BSE/ NSE). If the user does not provide an exchange name, by default considered as NSE. |
| `markToMarketPrice` | String | Price change between previous close price and current price. |
| `lastTradedPrice` | String | Price at which last transaction/trade is done. |
| `previousClose` | String | Previous close refers to the prior day's final price of security when the market officially closes for the day. |
| `productCode` | String | Type of the product, allowable type is CNC. |
| `symbolDescription` | String | Scrip Description. |
| `tradingSymbol` | String | Trading Symbol of the scrip. |
| `totalGainAndLoss` | String | Total Gain/Loss for all existing positions since their creation. |
| `calculatedNetQuantity` | String | Quantity left after the day. |
| `holdingsQuantity` | String | Currently holding (CNC) quantity. |
| `collateralQuantity` | String | Quantity of loan against shares offered by SAMCO to their clients for trading in stock and shares. |
| `holdingsValue` | String | Limit value of the available holdings. |
| `isin` | String | The standard ISIN representing stocks uniquely at international level. It is same for every exchange. |
| `sellableQuantity` | String | Quantity which is open for sale. |
| `totalMarketToMarketPrice` | String | Total price change between previous close price and current price. |

---

## Trade Book

`GET /trade/tradeBook`

Details of all successfully executed orders placed by the user.

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/trade/tradeBook' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>'
```

**Java**

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Sample {
  public static void main(String[] args) throws Exception {
    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/trade/tradeBook"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .GET()
        .build();

    HttpResponse<String> response =
        client.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

**NodeJs**

```js
(async () => {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-session-token': '<SESSION_TOKEN>',
  };

  const response = await fetch('https://tradeapi.samco.in/trade/tradeBook', {
    method: 'GET',
    headers,
  });

  const data = await response.json();
  console.log(data);
})();
```

**Python**

```py
import requests
import json

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'x-session-token': '<SESSION_TOKEN>',
}

r = requests.get('https://tradeapi.samco.in/trade/tradeBook',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "status": "Success",
  "statusMessage": "Request successful",
  "tradeBookDetails": [
    {
      "orderNumber": "191206000000079",
      "exchange": "BSE",
      "tradingSymbol": "RELIANCE",
      "symbolDescription": "RELIANCE INDUSTRIES LTD.",
      "transactionType": "BUY",
      "productCode": "MIS",
      "orderType": "L",
      "orderPrice": "1560.15",
      "quantity": "13",
      "disclosedQuantity": "1",
      "triggerPrice": "0.00",
      "marketProtection": "3",
      "orderValidity": "DAY",
      "orderStatus": "Complete",
      "orderValue": "20281.95",
      "instrumentName": "NA",
      "orderTime": "06-Dec-2019 13:47:04",
      "userId": "DV99999",
      "filledQuantity": "13",
      "unfilledQuantity": "0",
      "exchangeConfirmationTime": "05:06:12",
      "coverOrderPercentage": "%",
      "exchangeOrderNumber": "1571202357797000054",
      "tradeNumber": "195300",
      "tradePrice": "1560.15",
      "tradeDate": "06DEC2019",
      "tradeTime": "02:14:47 PM",
      "strikePrice": "800.00",
      "optionType": "XX",
      "lastTradePrice": "2,077.00",
      "expiry": "NA"
    }
  ]
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | Response status. Can be Success or Failure. |
| `statusMessage` | string | Status Message. |
| `tradeBookDetails` | [object] | Get list of TradeBookEntries. |
| `orderNumber` | string | Unique Order identifier generated after placing an order. |
| `exchange` | string | Name of the exchange. Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS). If the user does not provide an exchange name, by default considered as NSE. For trading with BSE, NFO, CDS, and MCX, exchange is mandatory. |
| `tradingSymbol` | string | Trading Symbol of the scrip. |
| `symbolDescription` | string | Scrip description. |
| `transactionType` | string | Type of the transaction, BUY / SELL. |
| `productCode` | string | Product Type of order as placed by the user. It can be CNC (Cash and Carry), BO (Bracket Order), CO (Cover Order), NRML (Normal), MIS (Intraday). |
| `orderType` | string | Type of order user has placed. It can be one of the following: MKT - Market Order, L - Limit Order, SL - Stop Loss Limit, SL-M - Stop Loss Market. |
| `orderPrice` | string | Limit price of a particular order. |
| `quantity` | string | It is the order quantity. |
| `disclosedQuantity` | string | Quantity to disclose to the public in the market. |
| `triggerPrice` | string | The price at which an order should be triggered in case of SL, SL-M. |
| `marketProtection` | string | Percentage of MarketProtection required for ordertype MKT/SL-M to limit loss due to market price changes against the price with which order is placed. Default value is 3%. |
| `orderValidity` | string | Order validity can be DAY / IOC. |
| `orderStatus` | string | Status of the order at Exchange side, either executed successfully or pending or rejected. |
| `orderValue` | string | Value of the order. |
| `instrumentName` | string | Name of the instrument. |
| `orderTime` | string | Order placement time. |
| `userId` | string | The client code provided to you by SAMCO after opening an account. |
| `filledQuantity` | string | Quantity which is filled in a specific trade. Can be less than or equal to the total quantity. |
| `unfilledQuantity` | string | Quantity which is not filled in a partially filled order. Can be less than or equal to the total quantity. |
| `exchangeConfirmationTime` | string | Order confirmation time at exchange. |
| `coverOrderPercentage` | string | Percentage of cover order. |
| `exchangeOrderNumber` | string | Unique Order identifier generated after placing an order. |
| `tradeNumber` | string | Unique trade identifier generated for every trade. |
| `tradePrice` | string | Price of a trade. |
| `tradeDate` | string | Date of a trade. |
| `tradeTime` | string | Time of a trade. |
| `strikePrice` | string | The strike price is the predetermined price at which a put buyer can sell the underlying asset. |
| `optionType` | string | Option Type (PE/CE). |
| `lastTradePrice` | string | Price at which last transaction/trade is done. |
| `expiry` | string | Shows expiry date of a trading symbol. |
