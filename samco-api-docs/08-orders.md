# Orders

Place, modify, and cancel regular, bracket, and cover orders; read the order book, order status, and trigger orders; and calculate span margin.

## Span Margin

`POST /spanMargin`

The Span Margin API calculates the margin requirements for derivative contracts like futures and options on an exchange. By taking a list of requests that specify the contracts, it processes the data and returns the total margin required for those contracts. This ensures that traders maintain sufficient capital to cover potential losses. The API helps in efficient risk management by determining how much margin needs to be set aside based on the positions held. This functionality is essential for traders and brokers to comply with exchange regulations and manage risk exposure effectively.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | true | Name of the exchange. |
| `tradingSymbol` | string | true | Trading Symbol of the scrip. |
| `qty` | string | true | Quantity asked for margin. |
| `transactionType` | string | false | Price is mandatory for single scrip. If not provided, default is considered as SELL. |
| `price` | string | false | Price is mandatory for single scrip. |
| `productType` | string | true | The product type of the order. It can be CNC (Cash and Carry), NRML (Normal), or MIS (Intraday). |
| `orderType` | string | true | The type of order. It can be one of the following: L (Limit Order), SL (Stop Loss Limit). |

### Sample Request Body

```json
requestBody={
    "request":[
        {
            "exchange":"NFO",
            "tradingSymbol":"NIFTY24MAR2627550CE",
            "qty":"65",
            "transactionType":"BUY",
            "price" :"6.15",
            "productType" :"BO",
            "orderType" :"L"
        }
    ]
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/spanMargin' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"request":[{"exchange":"NFO","tradingSymbol":"NIFTY24MAR2627550CE","qty":"65","transactionType":"BUY","price":"6.15","productType":"BO","orderType":"L"}]}'
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
          "request": [
            {
              "exchange": "NFO",
              "tradingSymbol": "NIFTY24MAR2627550CE",
              "qty": "65",
              "transactionType": "BUY",
              "price": "6.15",
              "productType": "BO",
              "orderType": "L"
            }
          ]
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/spanMargin"))
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
    request: [
      {
        exchange: "NFO",
        tradingSymbol: "NIFTY24MAR2627550CE",
        qty: "65",
        transactionType: "BUY",
        price: "6.15",
        productType: "BO",
        orderType: "L"
      }
    ]
  };

  const response = await fetch('https://tradeapi.samco.in/spanMargin', {
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
  "request": [
    {
      "exchange": "NFO",
      "tradingSymbol": "NIFTY24MAR2627550CE",
      "qty": "65",
      "transactionType": "BUY",
      "price": "6.15",
      "productType": "BO",
      "orderType": "L"
    }
  ]
}

r = requests.post('https://tradeapi.samco.in/spanMargin',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
    "serverTime": "17/03/26 19:02:46",
    "msgId": "726494be-a5ce-45d0-8e93-fbe6aa1a5b9d",
    "status": "Success",
    "statusMessage": "Span margin calculated",
    "spanDetails": {
        "estimatedBrokerage": "20.00",
        "estimatedExpenses": "3.88",
        "estimatedOrderValue": "423.63",
        "marginRequired": "423.63",
        "exposureMargin": "0.00",
        "totalMargin": "423.63"
    }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | The status of the API response. It can be either 'Success' or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `totalRequirement` | string | This is the total amount of margin required for a particular portfolio of futures and options positions. It includes the SPAN requirement, exposure margin, and any additional margin that may be required by the exchange. |
| `spanRequirement` | string | This is the margin requirement calculated using the SPAN algorithm, which is a risk-based margining system. The SPAN requirement takes into account factors such as price volatility, correlation between different positions, and the overall risk of the portfolio. |
| `exposureMargin` | string | Exposure margin is an additional margin that may be required by the exchange to cover potential losses beyond those accounted for by the SPAN requirement. It provides a buffer against adverse market movements and helps ensure that traders maintain sufficient margin to cover their positions. |
| `spreadBenefit` | string | Spread benefit refers to a reduction in margin requirements that may be applied when certain offsetting positions are held in the same account. This reduction reflects the reduced risk associated with offsetting positions and encourages traders to engage in spread trading strategies. |
| `estimatedBrokerage` | string | Projected fee charged by brokers for making a stock trade. |
| `estimatedExpenses` | string | Projected costs for completing a stock trade, excluding brokerage fees. |
| `estimatedOrderValue` | string | Total projected value of a stock trade before any fees. |
| `marginRequired` | string | Funds needed to cover potential losses in a stock trade. |
| `totalMargin` | string | The total funds needed for a leveraged stock trade equals the sum of the margin required and the exposure margin. |

---

## Place Order

`POST /order/placeOrder`

This API allows you to place an equity/derivative order to the exchange i.e the place order request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. To be precise, under normal scenarios, the whole flow of order execution starting with order placement, routing to OMS and transfer to the exchange, order execution, and confirmation from exchange happen real time. But due to various reasons like market hours, exchange related checks etc. This may not happen instantly. So when an order is successfully placed the placeOrder API returns an orderNumber in response, and in scenarios as above the actual order status can be checked separately using the orderStatus API call.This is for Placing CNC, MIS and NRML Orders.

> **INFO** — In the BFO exchange, only SENSEX and BANKEX trades are allowed.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `symbolName` | string | true | Pass the "name" in the `symbolName` parameter for Equity Cash symbols, and the "Trading Symbol" for all F&O contracts (both 'name' and 'tradingSymbol' are available in the ScripMaster.csv). |
| `exchange` | string | true | Name of the exchange. Valid exchange values are BSE, NSE, NFO, BFO, MCX, and CDS. If the user does not provide an exchange name, the default is NSE. For trading on BSE, NFO, BFO, CDS, and MCX, the exchange is mandatory. |
| `transactionType` | string | true | The transaction type should be either BUY or SELL. |
| `orderType` | string | true | The type of order. It can be one of the following: L (Limit Order), SL (Stop Loss Limit). |
| `quantity` | string | true | The quantity with which the order is being placed. |
| `disclosedQuantity` | string | false | If provided, it should be a minimum of 10% of the actual quantity. |
| `price` | string | false | Price is mandatory when the order type is L (Limit Order) or SL (Stop Loss Limit). |
| `orderValidity` | string | true | Order validity can be DAY or IOC. DAY is valid for the entire trading day and stays pending until executed, while IOC (Immediate or Cancel) means the order hits the exchange and is cancelled if not executed immediately. |
| `afterMarketOrderFlag` | string | false | After Market Order Flag. Acceptable values are YES or NO. |
| `productType` | string | true | The product type of the order. It can be CNC (Cash and Carry), NRML (Normal), or MIS (Intraday). |
| `triggerPrice` | string | false | The price at which an order should be triggered in the case of SL (Stop Loss). |

### Sample Request Body

**LIMIT ORDER**

```json
requestBody={ 
"symbolName":"IDEA",
"exchange":"NSE",
"transactionType":"BUY",
"orderType":"L",
"quantity": "1",
"disclosedQuantity":"1",
"orderValidity":"DAY",
"productType":"CNC",
"afterMarketOrderFlag":"NO",
"price":"13.40"
}
```

**STOP LIMIT ORDER**

```json
requestBody={ 
"symbolName":"IDEA",
"exchange":"NSE",
"transactionType":"BUY",
"orderType":"SL",
"quantity": "1",
"orderValidity":"DAY",
"productType":"CNC",
"price":"13.40",
"triggerPrice":"14.9"
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Code Sample

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/order/placeOrder' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"symbolName":"IDEA","exchange":"NSE","transactionType":"BUY","orderType":"L","quantity":"1","disclosedQuantity":"1","orderValidity":"DAY","productType":"CNC","afterMarketOrderFlag":"NO","price":"13.40"}'
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
          "symbolName": "IDEA",
          "exchange": "NSE",
          "transactionType": "BUY",
          "orderType": "L",
          "quantity": "1",
          "disclosedQuantity": "1",
          "orderValidity": "DAY",
          "productType": "CNC",
          "afterMarketOrderFlag": "NO",
          "price": "13.40"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/order/placeOrder"))
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
    symbolName: "IDEA",
    exchange: "NSE",
    transactionType: "BUY",
    orderType: "L",
    quantity: "1",
    disclosedQuantity: "1",
    orderValidity: "DAY",
    productType: "CNC",
    afterMarketOrderFlag: "NO",
    price: "13.40"
  };

  const response = await fetch('https://tradeapi.samco.in/order/placeOrder', {
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
  "symbolName": "IDEA",
  "exchange": "NSE",
  "transactionType": "BUY",
  "orderType": "L",
  "quantity": "1",
  "disclosedQuantity": "1",
  "orderValidity": "DAY",
  "productType": "CNC",
  "afterMarketOrderFlag": "NO",
  "price": "13.40"
}

r = requests.post('https://tradeapi.samco.in/order/placeOrder',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample responses

**LIMIT ORDER**

```json
{
    "serverTime": "22/05/24 17:17:15",
    "msgId": "dc1a9957-8bee-4895-9b7e-8e5e5f627a1a",
    "status": "Success",
    "orderNumber": "240522000162545",
    "statusMessage": "CNC Order request placed successfully",
    "exchangeOrderStatus": "PENDING",
    "rejectionReason": "",
    "orderDetails": {
        "pendingQuantity": 1,
        "avgExecutionPrice": "0.00",
        "orderPlacedBy": "--",
        "tradingSymbol": "IDEA-EQ",
        "triggerPrice": "0.00",
        "exchange": "NSE",
        "totalQuantity": 1,
        "transactionType": "B",
        "productType": "CNC",
        "orderType": "L",
        "quantity": 1,
        "filledQuantity": 0,
        "orderPrice": "13.40",
        "filledPrice": "0.00",
        "orderValidity": "DAY",
        "orderTime": "22/05/2024 17:17:15"
    }
}
```

**STOP LIMIT ORDER**

```json
{
    "serverTime": "22/05/24 17:25:06",
    "msgId": "810d707d-b23e-4dd4-bf72-f4f9dfb2d688",
    "status": "Success",
    "orderNumber": "240522000162594",
    "statusMessage": "CNC Order request placed successfully",
    "exchangeOrderStatus": "PENDING",
    "rejectionReason": "",
    "orderDetails": {
        "pendingQuantity": 1,
        "avgExecutionPrice": "0.00",
        "orderPlacedBy": "--",
        "tradingSymbol": "IDEA-EQ",
        "triggerPrice": "14.90",
        "exchange": "NSE",
        "totalQuantity": 1,
        "transactionType": "B",
        "productType": "CNC",
        "orderType": "SL",
        "quantity": 1,
        "filledQuantity": 0,
        "orderPrice": "13.40",
        "filledPrice": "0.00",
        "orderValidity": "DAY",
        "orderTime": "22/05/2024 17:25:06"
    }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `orderNumber` | string | Unique Order identifier generated after placing an order which could be used for tracking order status. |
| `status` | string | Status of the order. It would be success or failure. |
| `statusMessage` | string | Order placement status Message. |
| `exchangeOrderStatus` | string | Status of the order execution at the Exchange side. Most common values are PENDING, COMPLETE, REJECTED, CANCELLED, and OPEN. |
| `rejectionReason` | string | If an order is rejected, the cause of order rejection, which comes as a user-friendly textual description. |
| `orderDetails` | object | none |
| `pendingQuantity` | string | Quantity which is in a waiting state to be filled in a specific trade. |
| `avgExecutionPrice` | string | Average price at which the quantities were bought/sold during the day. |
| `orderPlacedBy` | string | Client code of the user who placed the order. |
| `tradingSymbol` | string | Trading Symbol of the scrip. |
| `triggerPrice` | string | The price at which an order should be triggered in the case of SL. |
| `exchange` | string | Name of the exchange. Valid exchange values are BSE, NSE, NFO, MCX, and CDS. If not provided, the default is NSE. For BSE, NFO, CDS, and MCX, it is mandatory. |
| `totalQuantity` | string | Total Quantity. |
| `expiry` | string | Expiry date of the trading symbol. |
| `transactionType` | string | Type of the transaction, BUY / SELL. |
| `productType` | string | Product Type of order as placed by the user. It can be CNC (Cash and Carry), BO (Bracket Order), CO (Cover Order), NRML (Normal), MIS (Intraday). |
| `orderType` | string | Type of order the user has placed. It can be L (Limit Order), SL (Stop Limit). |
| `quantity` | string | Order Quantity as placed by the user. |
| `filledQuantity` | string | Quantity filled in a specific trade. Can be less than or equal to the total quantity. |
| `orderPrice` | string | Limit price entered at the time of placing the order. |
| `filledPrice` | string | Price at which the exchange has filled the order. |
| `exchangeOrderNo` | string | Order identifier at the exchange. |
| `orderValidity` | string | Validity of the order. |
| `orderTime` | string | Order placement time. |

---

## Place BO Order

`POST /order/placeOrderBO`

This API allows you to place an equity/derivative order to the exchange i.e the place order request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. To be precise, under normal scenarios, the whole flow of order execution starting with order placement, routing to OMS and transfer to the exchange, order execution, and confirmation from exchange happen real time. But due to various reasons like market hours, exchange related checks etc. This may not happen instantly. So when an order is successfully placed the placeOrder API returns an orderNumber in response, and in scenarios as above the actual order status can be checked separately using the orderStatus API call. This is for Placing BO Orders.

> **INFO** — In the BFO exchange, only SENSEX and BANKEX trades are allowed.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `symbolName` | string | true | Pass the "name" in the `symbolName` parameter for Equity Cash symbols and the "Trading Symbol" for all F&O contracts ('name' and 'tradingSymbol' are available in ScripMaster.csv). |
| `exchange` | string | true | Name of the exchange. Valid exchange values are NSE, BSE, NFO, BFO, MCX, CDS, MFO. If the user does not provide an exchange name, the default is NSE. For NFO, CDS, and MCX, the exchange is mandatory. BO orders are not applicable for BSE. |
| `transactionType` | string | true | Transaction type should be either BUY or SELL. |
| `quantity` | string | true | Quantity with which the order is being placed. |
| `disclosedQuantity` | string | true | If provided, it should be a minimum of 10% of the actual quantity. |
| `price` | string | true | Price at which the order will be placed. |
| `priceType` | string | true | Price type required to place an order. Valid price types are LTP/ATP, with the default being LTP. Applicable for BO orders only. |
| `squareOffValue` | string | true | Price difference from entry price at which the order should be squared off to limit losses (e.g., if the order price is 300 and the profit target is 305, the target is 5). Applicable for BO orders only. |
| `stopLossValue` | string | true | Stop loss price difference from the entry price at which the order should be squared off (e.g., if the order price is 300 and the stop loss target is 295, the stop loss is 5). Applicable for both BO & CO orders. |
| `valueType` | string | true | Value type required to place an order. Applicable for both stop loss value and square off value. Valid value types are Absolute/Ticks, with the default being Absolute. Applicable for BO orders only. |
| `trailingStopLoss` | string | true | Incremental value set as a percentage change from the market price. The trailing stop moves as the price moves up, but if the price falls, the stop loss does not move. Applicable for BO orders only. |

### Sample Request Body

```json
requestBody={
  "symbolName": "RELIANCE",
  "exchange": "NSE",
  "transactionType": "BUY",
  "quantity": "1",
  "disclosedQuantity": "1",
  "price": "1240.0",
  "priceType": "LTP",
  "squareOffValue": "5",
  "stopLossValue": "5",
  "valueType": "Ticks",
  "trailingStopLoss": "5"
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/order/placeOrderBO' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"symbolName":"RELIANCE","exchange":"NSE","transactionType":"BUY","quantity":"1","disclosedQuantity":"1","price":"1240.0","priceType":"LTP","squareOffValue":"5","stopLossValue":"5","valueType":"Ticks","trailingStopLoss":"5"}'
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
          "exchange": "NSE",
          "transactionType": "BUY",
          "quantity": "1",
          "disclosedQuantity": "1",
          "price": "1240.0",
          "priceType": "LTP",
          "squareOffValue": "5",
          "stopLossValue": "5",
          "valueType": "Ticks",
          "trailingStopLoss": "5"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/order/placeOrderBO"))
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
    exchange: "NSE",
    transactionType: "BUY",
    quantity: "1",
    disclosedQuantity: "1",
    price: "1240.0",
    priceType: "LTP",
    squareOffValue: "5",
    stopLossValue: "5",
    valueType: "Ticks",
    trailingStopLoss: "5"
  };

  const response = await fetch('https://tradeapi.samco.in/order/placeOrderBO', {
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
  "exchange": "NSE",
  "transactionType": "BUY",
  "quantity": "1",
  "disclosedQuantity": "1",
  "price": "1240.0",
  "priceType": "LTP",
  "squareOffValue": "5",
  "stopLossValue": "5",
  "valueType": "Ticks",
  "trailingStopLoss": "5"
}

r = requests.post('https://tradeapi.samco.in/order/placeOrderBO',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample responses

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "orderNumber": "190726000001077",
  "status": "Success",
  "exchangeOrderStatus": "Executed",
  "rejectionReason": "--",
  "statusMessage": "BO Order request placed successfully",
  "orderDetails": {
    "pendingQuantity": "0",
    "avgExecutionPrice": "1193.00",
    "orderPlacedBy": "DV9999",
    "tradingSymbol": "RELIANCE",
    "triggerPrice": "0.00",
    "exchange": "NSE",
    "totalQuantity": "1",
    "expiry": "--",
    "transactionType": "BUY",
    "productType": "BO",
    "orderType": "L",
    "quantity": "1",
    "filledQuantity": "1",
    "orderPrice": "1240.00",
    "filledPrice": "1240.0",
    "exchangeOrderNo": "1565067682526005486",
    "orderValidity": "DAY",
    "orderTime": "12/12/2019 16:20:09"
  }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `orderNumber` | string | Unique Order identifier generated after placing an order which could be used for tracking order status. |
| `status` | string | Status of the order. It would be success or failure. |
| `exchangeOrderStatus` | string | Status of the order execution at the Exchange side. Most common values are PENDING, COMPLETE, REJECTED, CANCELLED, and OPEN. |
| `rejectionReason` | string | If an order is rejected, the cause of order rejection, which comes as a user-friendly textual description. |
| `statusMessage` | string | Order placement status message. |
| `orderDetails` | object | none. |
| `pendingQuantity` | string | Quantity which is in a waiting state to be filled in a specific trade. |
| `avgExecutionPrice` | string | Average price at which the quantities were bought/sold during the day. |
| `orderPlacedBy` | string | Client code of the user who placed the order. |
| `tradingSymbol` | string | Trading Symbol of the scrip. |
| `triggerPrice` | string | The price at which an order should be triggered in the case of SL, SL-M. |
| `exchange` | string | Name of the exchange. Valid exchange values are NSE, NFO, MCX, and CDS. If not provided, the default is NSE. For NFO, CDS, and MCX, the exchange is mandatory. BO orders are not applicable for BSE exchange. |
| `totalQuantity` | string | Total quantity. |
| `expiry` | string | Expiry date of the trading symbol. |
| `transactionType` | string | Type of the transaction, BUY / SELL. |
| `productType` | string | Product type of the order as placed by the user is BO (Bracket Order). |
| `orderType` | string | Type of order the user has placed. It can be L (Limit Order), SL (Stop Loss Limit). |
| `quantity` | string | Order quantity as placed by the user. |
| `filledQuantity` | string | Quantity filled in a specific trade. Can be less than or equal to the total quantity. |
| `orderPrice` | string | Limit price entered at the time of placing the order. |
| `filledPrice` | string | Price at which the exchange has filled the order. |
| `exchangeOrderNo` | string | Order identifier at the exchange. |
| `orderValidity` | string | Validity of the order. |
| `orderTime` | string | Order placement time. |

---

## Place CO Order

`POST /order/placeOrderCO`

This API allows you to place an equity/derivative order to the exchange i.e the place order request typically registers the order with OMS and when it happens successfully, a success response is returned. Successful placement of an order via the API does not imply its successful execution. To be precise, under normal scenarios, the whole flow of order execution starting with order placement, routing to OMS and transfer to the exchange, order execution, and confirmation from exchange happen real time. But due to various reasons like market hours, exchange related checks etc. This may not happen instantly. So when an order is successfully placed the placeOrder API returns an orderNumber in response, and in scenarios as above the actual order status can be checked separately using the orderStatus API call. This is for Placing CO Orders.

> **INFO** — In the BFO exchange, only SENSEX and BANKEX trades are allowed.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `body` | object | false | none |
| `symbolName` | string | true | Pass "name" in the `symbolName` parameter for Equity Cash symbols and "Trading Symbol" for all the F&O contracts ('name' and 'tradingSymbol' are available in ScripMaster.csv). |
| `exchange` | string | true | Name of the exchange. Valid exchange values are BSE, NSE, NFO, MCX, and CDS. If the user does not provide an exchange name, the default is NSE. For trading with BSE, NFO, CDS, and MCX, the exchange is mandatory. |
| `transactionType` | string | true | Transaction type should be either BUY or SELL. |
| `orderType` | string | true | Type of order. It can be one of the following: L (Limit Order). |
| `quantity` | string | true | Quantity with which the order is being placed. |
| `disclosedQuantity` | string | true | If provided, it should be a minimum of 10% of the actual quantity. |
| `price` | string | true | Price at which the order will be placed. |
| `orderValidity` | string | true | Order validity should be DAY. DAY is an order type which is valid for the whole trading day and stays pending until it is executed within the respective trading day. |
| `productType` | string | true | Product type of the order. It can be CO (Cover Order). |
| `triggerPrice` | string | false | The price at which an order should be triggered. |

### Sample Request Body

```json
requestBody={
  "symbolName": "RELIANCE",
  "exchange": "BSE",
  "transactionType": "BUY",
  "orderType": "L",
  "quantity": "1",
  "disclosedQuantity": "1",
  "price": "1240.0",
  "orderValidity": "DAY",
  "productType": "CO",
  "triggerPrice": "1070.00"
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/order/placeOrderCO' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"symbolName":"RELIANCE","exchange":"BSE","transactionType":"BUY","orderType":"L","quantity":"1","disclosedQuantity":"1","price":"1240.0","orderValidity":"DAY","productType":"CO","triggerPrice":"1070.00"}'
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
          "orderType": "L",
          "quantity": "1",
          "disclosedQuantity": "1",
          "price": "1240.0",
          "orderValidity": "DAY",
          "productType": "CO",
          "triggerPrice": "1070.00"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/order/placeOrderCO"))
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
    orderType: "L",
    quantity: "1",
    disclosedQuantity: "1",
    price: "1240.0",
    orderValidity: "DAY",
    productType: "CO",
    triggerPrice: "1070.00"
  };

  const response = await fetch('https://tradeapi.samco.in/order/placeOrderCO', {
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
  "orderType": "L",
  "quantity": "1",
  "disclosedQuantity": "1",
  "price": "1240.0",
  "orderValidity": "DAY",
  "productType": "CO",
  "triggerPrice": "1070.00"
}

r = requests.post('https://tradeapi.samco.in/order/placeOrderCO',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "orderNumber": "190726000001077",
  "status": "Success",
  "exchangeOrderStatus": "Executed",
  "rejectionReason": "--",
  "statusMessage": "CO Order request placed successfully",
  "orderDetails": {
    "pendingQuantity": "0",
    "avgExecutionPrice": "1193.00",
    "orderPlacedBy": "DV9999",
    "tradingSymbol": "RELIANCE",
    "triggerPrice": "0.00",
    "exchange": "BSE",
    "totalQuantity": "1",
    "expiry": "--",
    "transactionType": "BUY",
    "productType": "CO",
    "orderType": "L",
    "quantity": "1",
    "filledQuantity": "1",
    "orderPrice": "1240.00",
    "filledPrice": "1240.0",
    "exchangeOrderNo": "1565067682526005486",
    "orderValidity": "DAY",
    "orderTime": "12/12/2019 16:20:09"
  }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `orderNumber` | string | Unique Order identifier generated after placing an order which could be used for tracking order status. |
| `status` | string | Status of the order. It would be success or failure. |
| `exchangeOrderStatus` | string | Status of the order execution at the Exchange side. Most common values are PENDING, COMPLETE, REJECTED, CANCELLED, and OPEN. |
| `rejectionReason` | string | If an order is rejected, the cause of order rejection, which comes as a user-friendly textual description. |
| `statusMessage` | string | Order placement status message. |
| `orderDetails` | object | none. |
| `pendingQuantity` | string | Quantity which is in a waiting state to be filled in a specific trade. |
| `avgExecutionPrice` | string | Average price at which the quantities were bought/sold during the day. |
| `orderPlacedBy` | string | Client code of the user who placed the order. |
| `tradingSymbol` | string | Trading Symbol of the scrip. |
| `triggerPrice` | string | The price at which an order should be triggered in the case of SL. |
| `exchange` | string | Name of the exchange. Valid exchange values are BSE, NSE, NFO, MCX, and CDS. If not provided, the default is NSE. For trading with BSE, NFO, CDS, and MCX, the exchange is mandatory. |
| `totalQuantity` | string | Total quantity. |
| `expiry` | string | Expiry date of the trading symbol. |
| `transactionType` | string | Type of the transaction, BUY / SELL. |
| `productType` | string | Product type of the order as placed by the user is CO (Cover Order). |
| `orderType` | string | Type of order the user has placed. It can be one of the following: L (Limit Order), SL (Stop Loss Limit). |
| `quantity` | string | Order quantity as placed by the user. |
| `filledQuantity` | string | Quantity filled in a specific trade. Can be less than or equal to the total quantity. |
| `orderPrice` | string | Limit price entered at the time of placing the order. |
| `filledPrice` | string | Price at which the exchange has filled the order. |
| `exchangeOrderNo` | string | Order identifier at the exchange. |
| `orderValidity` | string | Validity of the order. |
| `orderTime` | string | Order placement time. |

---

## Get Order Status

`GET /order/getOrderStatus`

Get status of an order placed previously. This API returns all states of the orders,but not limited to open, pending, and partially filled ones.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `orderNumber` | string | true | Order Number for which the user wants to check the order status |

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/order/getOrderStatus?orderNumber=190707000000004' \
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
        .uri(URI.create("https://tradeapi.samco.in/order/getOrderStatus?orderNumber=190707000000004"))
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

  const response = await fetch('https://tradeapi.samco.in/order/getOrderStatus?orderNumber=190707000000004', {
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

r = requests.get('https://tradeapi.samco.in/order/getOrderStatus?orderNumber=190707000000004',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "orderNumber": "190722000000243",
  "orderStatus": "Success",
  "statusMessage": "Requested MIS Order placed successfully",
  "orderDetails": {
    "pendingQuantity": "0",
    "avgExecutionPrice": "1193.00",
    "orderPlacedBy": "DV9999",
    "tradingSymbol": "RELIANCE",
    "triggerPrice": "0.00",
    "exchange": "BSE",
    "totalQuantity": "1",
    "expiry": "--",
    "transactionType": "BUY",
    "productType": "MIS",
    "orderType": "L",
    "quantity": "1",
    "filledQuantity": "1",
    "orderPrice": "1240.00",
    "filledPrice": "1240.0",
    "exchangeOrderNo": "1565067682526005486",
    "orderValidity": "DAY",
    "orderTime": "12/12/2019 16:20:09"
  }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `orderNumber` | string | Unique number generated at the exchange while placing an order. |
| `orderStatus` | string | Status of the order at the Exchange side. Most common values are PENDING, COMPLETE, REJECTED, CANCELLED, and OPEN. |
| `statusMessage` | string | Status message of the order. |
| `orderDetails` | object | none. |
| `pendingQuantity` | string | Quantity which is in a waiting state to be filled in a specific trade. |
| `avgExecutionPrice` | string | Average price at which the quantities were bought/sold during the day. |
| `orderPlacedBy` | string | Client code of the user who placed the order. |
| `tradingSymbol` | string | Trading symbol of the scrip. |
| `triggerPrice` | string | The price at which an order should be triggered in the case of SL. |
| `exchange` | string | Name of the exchange. Valid exchange values are BSE, NSE, NFO, MCX, and CDS. If not provided, the default is NSE. For trading with BSE, NFO, CDS, and MCX, the exchange is mandatory. |
| `totalQuantity` | string | Total quantity. |
| `expiry` | string | Expiry date of the trading symbol. |
| `transactionType` | string | Type of the transaction, BUY / SELL. |
| `productType` | string | Product type of the order as placed by the user. It can be CNC (Cash and Carry), BO (Bracket Order), CO (Cover Order), NRML (Normal), or MIS (Intraday). |
| `orderType` | string | Type of order the user has placed. It can be one of the following: L (Limit Order), SL (Stop Loss Limit). |
| `quantity` | string | Order quantity as placed by the user. |
| `filledQuantity` | string | Quantity filled in a specific trade. Can be less than or equal to the total quantity. |
| `orderPrice` | string | Limit price entered at the time of placing the order. |
| `filledPrice` | string | Price at which the exchange has filled the order. |
| `exchangeOrderNo` | string | Order identifier at the exchange. |
| `orderValidity` | string | Validity of the order. |
| `orderTime` | string | Order placement time. |

---

## Order Book

`GET /order/orderBook`

Orderbook retrieves and displays details of all orders placed by the user on a specific day. This API returns all states of the orders, namely, open, pending, rejected and executed ones.

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/order/orderBook' \
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
        .uri(URI.create("https://tradeapi.samco.in/order/orderBook"))
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

  const response = await fetch('https://tradeapi.samco.in/order/orderBook', {
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

r = requests.get('https://tradeapi.samco.in/order/orderBook',
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
  "orderBookDetails": [
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
      "triggerPrice": "1090.00",
      "marketProtection": "3",
      "orderValidity": "DAY",
      "orderStatus": "Complete",
      "orderValue": "20281.95",
      "instrumentName": "NA",
      "orderTime": "06-Dec-2019 13:47:04",
      "userId": "DV99999",
      "filledQuantity": "13",
      "fillPrice": "1560.15",
      "averagePrice": "1560.15",
      "unfilledQuantity": "0",
      "exchangeOrderId": "1575608622401000995",
      "rejectionReason": "NA",
      "exchangeConfirmationTime": "06-Dec-2019 14:14:47",
      "cancelledQuantity": "0",
      "referenceLimitPrice": "0.00",
      "coverOrderPercentage": "0.00",
      "orderRemarks": "--",
      "exchangeOrderNumber": "1575608622401000995",
      "symbol": "52310_NFO",
      "displayStrikePrice": "0.00",
      "displayNetQuantity": "10",
      "status": "complete",
      "exchangeStatus": "complete",
      "expiry": "--",
      "pendingQuantity": "0",
      "instrument": "--",
      "scripName": "--",
      "totalQuanity": "13",
      "optionType": "--",
      "orderPlaceBy": "DV99999",
      "lotQuantity": "1",
      "parentOrderId": "200824000050316"
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
| `statusMessage` | string | Status message. |
| `orderBookDetails` | [object] | List of all orders with details during the day. |
| `orderNumber` | string | Unique Order identifier generated after placing an order. |
| `exchange` | string | Name of the exchange. Valid exchange values are BSE, NSE, NFO, MCX, and CDS. If not provided, the default is NSE. For trading with BSE, NFO, CDS, and MCX, the exchange is mandatory. |
| `tradingSymbol` | string | Trading Symbol of the scrip. |
| `symbolDescription` | string | Scrip description. |
| `transactionType` | string | Type of the transaction, BUY / SELL. |
| `productCode` | string | Product Type of order as placed by the user. It can be CNC (Cash and Carry), BO (Bracket Order), CO (Cover Order), NRML (Normal), or MIS (Intraday). |
| `orderType` | string | Type of order the user has placed. It can be one of the following: MKT (Market Order), L (Limit Order), SL (Stop Loss Limit), SL-M (Stop Loss Market). |
| `orderPrice` | string | Total price of a particular order. |
| `quantity` | string | Total quantity as placed by the user. |
| `disclosedQuantity` | string | If provided, should be a minimum of 10% of the actual quantity. |
| `triggerPrice` | string | The price at which an order should be triggered in the case of SL, SL-M. |
| `marketProtection` | string | Percentage of market protection required for order type MKT/SL-M to limit loss due to market price changes against the price with which the order is placed. Default value is 3%. |
| `orderValidity` | string | Order validity can be DAY / IOC. |
| `orderStatus` | string | Status of the order at the Exchange side, either executed successfully, pending, or rejected. |
| `orderValue` | string | Value of the order. |
| `instrumentName` | string | Name of the instrument. |
| `orderTime` | string | Order placement time. |
| `userId` | string | The client code provided to you by SAMCO after opening an account. |
| `filledQuantity` | string | Quantity filled in a specific trade. Can be less than or equal to the total quantity. |
| `fillPrice` | string | Price at which the exchange has filled the order. |
| `averagePrice` | string | Average trading price of the equity. |
| `unfilledQuantity` | string | Quantity which is not filled in a partially filled order. Can be less than or equal to the total quantity. |
| `exchangeOrderId` | string | Unique Order identifier generated from the exchange. |
| `rejectionReason` | string | If the order is rejected, cause of order rejection. |
| `exchangeConfirmationTime` | string | Order confirmation time at the exchange. |
| `cancelledQuantity` | string | Cancelled quantity for partially cancelled orders. |
| `referenceLimitPrice` | string | Limit price reference. |
| `coverOrderPercentage` | string | Percentage of cover order. |
| `orderRemarks` | string | Remarks about the order. |
| `exchangeOrderNumber` | string | Unique Order identifier generated after placing an order. |
| `symbol` | string | Symbol about the stock. |
| `displayStrikePrice` | string | Shows the strike price. |
| `displayNetQuantity` | string | Displays the limit quantity of the order. |
| `status` | string | Status will display Executed/Pending/Rejected. |
| `exchangeStatus` | string | Exchange status will display Executed/Pending/Rejected. |
| `expiry` | string | Shows expiry date of the stock. |
| `pendingQuantity` | string | Pending quantity will show the pending quantity of stock. |
| `instrument` | string | Instrument is about the type of stock. FUT/OPT. |
| `scripName` | string | Name of the scrip. |
| `totalQuantity` | string | Total quantity. |
| `optionType` | string | Option type (PE/CE). |
| `orderPlacedBy` | string | Client code of the user who placed the order. |
| `lotQuantity` | string | Lot quantity represents the number of contracts contained in one derivative security. Applicable for F&O. |
| `parentOrderId` | string | Order ID of the parent order (applicable for only BO/CO orders). |

---

## TriggerOrders

`GET /order/getTriggerOrders`

This API allows you to get the trigger order numbers in case of BO and CO orders so that their attribute values can be modified for BO orders, it will give the order identifiers. For Stop loss leg and target leg. Similarly for CO orders, it will return order identifier of stop loss leg only. Using the order identifier, the user would be able to modify the order attributes using the modifyOrder API. Refer modifyOrder API documentation for the parameters details.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `orderNumber` | string | true | Order Number for which the user wants to check the order status |

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/order/getTriggerOrders?orderNumber=190707000000004' \
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
        .uri(URI.create("https://tradeapi.samco.in/order/getTriggerOrders?orderNumber=190707000000004"))
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

  const response = await fetch('https://tradeapi.samco.in/order/getTriggerOrders?orderNumber=190707000000004', {
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

r = requests.get('https://tradeapi.samco.in/order/getTriggerOrders?orderNumber=190707000000004',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "status": "Success",
  "statusMessage": "SubOrder details retrieved successfully.",
  "triggerOrders": [
    {
      "stopLossOrderNo": "191219000000063",
      "orderStatus": "Complete",
      "orderPrice": "351.20",
      "triggerPrice": "331.20"
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
| `triggerOrders` | [object] | Trigger order details available for the provided `OrderNumber`. |
| `stopLossOrderNo` | string | Unique Order identifier generated from the exchange. |
| `orderStatus` | string | Status of the order at the Exchange side, either executed successfully, complete, trigger pending, or cancelled. |
| `orderPrice` | string | Price of a particular order. |
| `triggerPrice` | string | The price at which an order should be triggered. |

---

## Modify Order

`PUT /order/modifyOrder/{orderNumber}`

To modify an order in the system, you can only do so while the order is in an open or pending status. orderNumber is mandatory for any modification request. Along with the orderNumber, you may send the specific attribute(s) that you wish to modify. If no optional parameters are provided, the system will retain the original order's default attributes.

> **WARNING** — Please note that this API cannot be used to modify orders that have already been executed, rejected, or canceled. Ensure that you only send the attribute(s) that need to be modified in the request, along with the required order identifier.

> **INFO** — **Steps to modify an order :**
>
> 1. Fetch all today's orders using the [Order Book](#order-book) API. From these, note down the order number of the orders that have a status of 'pending' or 'open' and that you want to modify.
> 2. Then, check the current status of that order using the [order status](#get-order-status) API. You can only modify the order if its status is still 'pending'.Then, based on the parameters provided below, you can modify your order.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `orderNumber` | string | true | Unique Order identifier of the order which needs to be modified. |
| `orderType` | string | false | Type of order user has placed. It can be one of the following: L - Limit Order, SL - Stop Loss Limit. |
| `quantity` | string | false | Quantity of the order user wants to modify. |
| `disclosedQuantity` | string | false | Quantity to disclose publicly. |
| `orderValidity` | string | true | Order validity can be DAY or IOC. |
| `price` | string | false | Price at which the order was placed. |
| `triggerPrice` | string | false | The price at which an order should be triggered in case of SL. |

### Sample Request Body

```json
requestBody={
  "orderType": "L",
  "quantity": "3",
  "disclosedQuantity": "1",
  "orderValidity": "DAY",
  "price": "1240.00",
  "triggerPrice": "1070.00"
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X PUT 'https://tradeapi.samco.in/order/modifyOrder/240820000131756' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"orderType":"L","quantity":"3","disclosedQuantity":"1","orderValidity":"DAY","price":"1240.00","triggerPrice":"1070.00"}'
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
          "orderType": "L",
          "quantity": "3",
          "disclosedQuantity": "1",
          "orderValidity": "DAY",
          "price": "1240.00",
          "triggerPrice": "1070.00"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/order/modifyOrder/240820000131756"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .PUT(HttpRequest.BodyPublishers.ofString(requestBody))
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
    orderType: "L",
    quantity: "3",
    disclosedQuantity: "1",
    orderValidity: "DAY",
    price: "1240.00",
    triggerPrice: "1070.00"
  };

  const response = await fetch('https://tradeapi.samco.in/order/modifyOrder/240820000131756', {
    method: 'PUT',
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
  "orderType": "L",
  "quantity": "3",
  "disclosedQuantity": "1",
  "orderValidity": "DAY",
  "price": "1240.00",
  "triggerPrice": "1070.00"
}

r = requests.put('https://tradeapi.samco.in/order/modifyOrder/240820000131756',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

**200**

```json
{
    "serverTime": "20/08/24 18:43:33",
    "msgId": "6178372c-d2e4-47d0-937a-e1122f30633a",
    "status": "Success",
    "statusMessage": "Order  modified successfully.",
    "ordernumber": "240820000131756"
}
```

**400**

```json

 {
    "serverTime": "20/08/24 18:22:22",
    "msgId": "471550bd-3677-471b-bc83-8b2de1535ae1",
    "status": "Failure",
    "statusMessage": "Invalid Order number.",
    "ordernumber": "240812000073930"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | This key indicates the time when the server processed the request. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | Status of the order. It would be success, error, or failure. |
| `statusMessage` | string | This provides a more detailed message regarding the status. |
| `orderNumber` | string | This is the unique identifier for the order that was modified. It can be used to reference the specific order within the system for further operations or inquiries. |

---

## Cancel BO Order

`DELETE /order/exitBO`

For Cancellation/exit of BO orders pass main leg Order number. If main leg is in Open/Pending state that order will be cancelled. If the main leg is executed and the sublegs are created and in open/Trigger pending state, the order will be exited. If the main leg is executed and if either of Stop loss or target is hit, API will return error message "SubOrder is in Executed status. Cannot exit/cancel such orders."

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `orderNumber` | string | true | The main order identifier provided as an input which needs to be exited. |

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X DELETE 'https://tradeapi.samco.in/order/exitBO?orderNumber=190707000000004' \
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
        .uri(URI.create("https://tradeapi.samco.in/order/exitBO?orderNumber=190707000000004"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .DELETE()
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

  const response = await fetch('https://tradeapi.samco.in/order/exitBO?orderNumber=190707000000004', {
    method: 'DELETE',
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

r = requests.delete('https://tradeapi.samco.in/order/exitBO?orderNumber=190707000000004',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "status": "Success",
  "orderNumber": "190722000000243",
  "statusMessage": "Order cancellation request placed successfully"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | Status of the order cancellation request. Can be success or failure. |
| `orderNumber` | string | Unique Order identifier generated after placing an order. |
| `statusMessage` | string | Status Message for the order cancellation request. |

---

## Cancel CO Order

`DELETE /order/exitCO`

For Cancellation/exit of CO orders pass main leg Order number. If main leg is in Open/Pending state that order will be cancelled. If the main leg is executed and the sublegs are created and in open/Trigger pending state, the order will be exited. If the main leg is executed and if Stop loss is hit, API will return error message "SubOrder is in Executed status. Cannot exit/cancel such orders."

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `orderNumber` | string | true | The main order identifier provided as an input which needs to be exited. |

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X DELETE 'https://tradeapi.samco.in/order/exitCO?orderNumber=190707000000004' \
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
        .uri(URI.create("https://tradeapi.samco.in/order/exitCO?orderNumber=190707000000004"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .DELETE()
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

  const response = await fetch('https://tradeapi.samco.in/order/exitCO?orderNumber=190707000000004', {
    method: 'DELETE',
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

r = requests.delete('https://tradeapi.samco.in/order/exitCO?orderNumber=190707000000004',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "status": "Success",
  "orderNumber": "190722000000243",
  "statusMessage": "Order cancellation request placed successfully"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | Status of the order cancellation request. Can be success or failure. |
| `orderNumber` | string | Unique Order identifier generated after placing an order. |
| `statusMessage` | string | Status Message for the order cancellation request. |

---

## Cancel Order

`DELETE /order/cancelOrder`

An order which is open or pending in system can be cancelled. In other words, cancellation cannot be initiated for already Executed, Rejected orders.This is for CNC, MIS and NRML Orders.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `orderNumber` | string | true | The order identifier provided as an input which needs to be cancelled. |

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X DELETE 'https://tradeapi.samco.in/order/cancelOrder?orderNumber=190707000000004' \
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
        .uri(URI.create("https://tradeapi.samco.in/order/cancelOrder?orderNumber=190707000000004"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .DELETE()
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

  const response = await fetch('https://tradeapi.samco.in/order/cancelOrder?orderNumber=190707000000004', {
    method: 'DELETE',
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

r = requests.delete('https://tradeapi.samco.in/order/cancelOrder?orderNumber=190707000000004',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "status": "Success",
  "orderNumber": "190722000000243",
  "statusMessage": "Order cancellation request placed successfully"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | Status of the order cancellation request. Can be success or failure. |
| `orderNumber` | string | Unique Order identifier generated after placing an order. |
| `statusMessage` | string | Status Message for the order cancellation request. |

---

## Bulk Order

`POST /order/bulkOrder`

The Bulk Order API is intended for placing large orders that surpass the exchange's standard freeze quantity limits. This API is particularly useful when you need to execute significant trades that would otherwise exceed the usual quantity restrictions imposed by trading platforms. It allows traders to efficiently handle substantial orders by either exceeding the freeze quantity or within it, depending on the order's size and requirements.

> **INFO** — In the BFO exchange, only SENSEX and BANKEX trades are allowed.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `symbolName` | string | true | Pass "name" in "symbolName" parameter for Equity Cash symbols and "Trading Symbol" for all the F&O contracts ('name' and 'tradingSymbol' is available in ScripMaster.csv). |
| `exchange` | string | true | Name of the exchange. Valid exchanges values (BSE/ NSE/ NFO/ BFO/ MCX/ CDS). If the user does not provide an exchange name, by default considered as NSE. For trading with BSE, NFO, BFO, CDS and MCX, exchange is mandatory. |
| `transactionType` | string | true | Transaction type should be BUY or SELL. |
| `orderType` | string | true | Type of order. It can be one of the following: L - Limit Order, SL - Stop Loss Limit. |
| `quantity` | string | true | Quantity with which the order is being placed. |
| `disclosedQuantity` | string | false | If provided, should be a minimum of 10% of the actual quantity. |
| `price` | string | false | Price mandatory when order type is L (Limit Order) or SL (Stop Loss Limit). |
| `orderValidity` | string | true | Order validity can be DAY / IOC. DAY is an order type which is valid for the whole trading day and stays pending till it is executed in the respective trading day. IOC (Immediate Or Cancel) order type is where once the user punches the order, the order hits the exchange and if not executed immediately, the order stands cancelled. |
| `afterMarketOrderFlag` | string | false | After Market Order Flag YES/NO. |
| `productType` | string | true | Product Type of the order. It can be CNC (Cash and Carry), NRML (Normal), MIS (Intraday), CO (Cover Order), BO (Bracket Order). |
| `triggerPrice` | string | false | The price at which an order should be triggered in case of SL. |

### Sample Request Body

**LIMIT ORDER**

```json
requestBody={ 
"symbolName":"IDEA",
"exchange":"NSE",
"transactionType":"BUY",
"orderType":"L",
"quantity": "1",
"disclosedQuantity":"1",
"orderValidity":"DAY",
"productType":"CNC",
"afterMarketOrderFlag":"NO",
"price":"13.40"
}
```

**STOP LIMIT ORDER**

```json
requestBody={ 
"symbolName":"IDEA",
"exchange":"NSE",
"transactionType":"BUY",
"orderType":"SL",
"quantity": "1",
"orderValidity":"DAY",
"productType":"CNC",
"price":"13.40",
"triggerPrice":"14.9"
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Code Sample

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/order/bulkOrder' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"symbolName":"IDEA","exchange":"NSE","transactionType":"BUY","orderType":"L","quantity":"1","disclosedQuantity":"1","orderValidity":"DAY","productType":"CNC","afterMarketOrderFlag":"NO","price":"13.40"}'
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
          "symbolName": "IDEA",
          "exchange": "NSE",
          "transactionType": "BUY",
          "orderType": "L",
          "quantity": "1",
          "disclosedQuantity": "1",
          "orderValidity": "DAY",
          "productType": "CNC",
          "afterMarketOrderFlag": "NO",
          "price": "13.40"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/order/bulkOrder"))
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
    symbolName: "IDEA",
    exchange: "NSE",
    transactionType: "BUY",
    orderType: "L",
    quantity: "1",
    disclosedQuantity: "1",
    orderValidity: "DAY",
    productType: "CNC",
    afterMarketOrderFlag: "NO",
    price: "13.40"
  };

  const response = await fetch('https://tradeapi.samco.in/order/bulkOrder', {
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
  "symbolName": "IDEA",
  "exchange": "NSE",
  "transactionType": "BUY",
  "orderType": "L",
  "quantity": "1",
  "disclosedQuantity": "1",
  "orderValidity": "DAY",
  "productType": "CNC",
  "afterMarketOrderFlag": "NO",
  "price": "13.40"
}

r = requests.post('https://tradeapi.samco.in/order/bulkOrder',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

> **TIP** — The response will be consistent across all order types.

```json
{
    "serverTime": "22/08/24 15:28:44",
    "msgId": "88f189f9-28da-431c-b7dc-3b5e673d4fb0",
    "status": "Success",
    "orders": [
        {
            "orderNumber": "240822000136560",
            "orderStatus": "REJECTED",
            "rejectionReason": "Your order was rejected since you can't place intraday orders in the last half hour of trade as intraday square off's are initiated by the RMS System in this period. All MIS / BO / CO orders shall be rejected during square off block period.",
            "orderDetails": {
                "pendingQuantity": 0,
                "avgExecutionPrice": "0.00",
                "orderPlacedBy": "--",
                "tradingSymbol": "NIFTY2482224500PE",
                "triggerPrice": "0.00",
                "exchange": "NFO",
                "totalQuantity": 1800,
                "transactionType": "BUY",
                "productType": "MIS",
                "orderType": "L",
                "quantity": 1800,
                "filledQuantity": 0,
                "orderPrice": "17.40",
                "filledPrice": "0.00",
                "orderValidity": "DAY",
                "orderTime": "22/08/2024 15:28:44"
            }
        },
        {
            "orderNumber": "240822000136562",
            "orderStatus": "REJECTED",
            "rejectionReason": "Your order was rejected since you can't place intraday orders in the last half hour of trade as intraday square off's are initiated by the RMS System in this period. All MIS / BO / CO orders shall be rejected during square off block period.",
            "orderDetails": {
                "pendingQuantity": 0,
                "avgExecutionPrice": "0.00",
                "orderPlacedBy": "--",
                "tradingSymbol": "NIFTY2482224500PE",
                "triggerPrice": "0.00",
                "exchange": "NFO",
                "totalQuantity": 200,
                "transactionType": "BUY",
                "productType": "MIS",
                "orderType": "L",
                "quantity": 200,
                "filledQuantity": 0,
                "orderPrice": "17.40",
                "filledPrice": "0.00",
                "orderValidity": "DAY",
                "orderTime": "22/08/2024 15:28:44"
            }
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
| `orderNumber` | string | Unique Order identifier generated after placing an order which could be used for tracking order status. |
| `status` | string | Status of the order. It would be success or failure. |
| `statusMessage` | string | Order placement status Message. |
| `exchangeOrderStatus` | string | Status of the order execution at Exchange side. Most common values are PENDING, COMPLETE, REJECTED, CANCELLED, and OPEN. |
| `rejectionReason` | string | If an order is rejected, cause of order rejection which comes as user-friendly textual description. |
| `orderDetails` | object | none |
| `pendingQuantity` | string | Quantity which is in waiting state to be filled in a specific trade. |
| `avgExecutionPrice` | string | Average price at which the quantities were bought/sold during the day. |
| `orderPlacedBy` | string | Client code of the user who placed the order. |
| `tradingSymbol` | string | Trading Symbol of the scrip. |
| `triggerPrice` | string | The price at which an order should be triggered in case of SL. |
| `exchange` | string | Name of the exchange. Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS). If the user does not provide an exchange name, by default considered as NSE. For trading with BSE, NFO, CDS and MCX, exchange is mandatory. |
| `totalQuantity` | string | Total Quantity. |
| `expiry` | string | Expiry date of trading symbol. |
| `transactionType` | string | Type of the transaction, BUY / SELL. |
| `productType` | string | Product Type of order as placed by the user. It can be CNC (Cash and Carry), BO (Bracket Order), CO (Cover Order), NRML (Normal), MIS (Intraday). |
| `orderType` | string | Type of order user has placed. It can be one of the following: L - Limit Order, SL - Stop Limit. |
| `quantity` | string | Order Quantity as placed by the user. |
| `filledQuantity` | string | Quantity which is filled in a specific trade. Can be less than or equal to the total quantity. |
| `orderPrice` | string | Limit price entered at the time of placing the order. |
| `filledPrice` | string | Price at which exchange has filled the order. |
| `exchangeOrderNo` | string | Order identifier at the exchange. |
| `orderValidity` | string | Validity of the order. |
| `orderTime` | string | Order placement time. |
