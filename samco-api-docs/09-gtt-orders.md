# GTT and OCO Orders

Good-Till-Triggered and One-Cancels-Other orders that stay active until filled or cancelled.

## GTT

A GTT order is a type of limit order that remains active until it is either filled or canceled by the user. This is useful for traders who want to buy or sell a security at a specific price but are not able to monitor the market continuously.

The Trade API mentioned here likely allows traders to interact with a trading platform programmatically, enabling them to place GTT orders without needing to use a graphical user interface (GUI). The API would typically involve sending HTTP requests with specific parameters to a server, which would then execute the order on behalf of the trader.

---

## Add GTT

`POST /gttoco/addGtt`

GTT (Good Till Triggered) is a feature that allows users to place buy or sell orders of any stock at market or limit price. These orders are executed (triggered) once the market price of the stock reaches your desired price i.e the price you mentioned in the GTT Order. [Read More....](https://www.samco.in/gtt-order)

> **INFO** — In the BFO exchange, only SENSEX and BANKEX trades are allowed.

### Parameter

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | true | The stock exchange where the order will be placed. Valid values: BSE, NSE, NFO, BFO, MCX, CDS, MFO. Default is NSE if not provided. For trading with BSE, NFO, BFO, CDS, MFO, and MCX, the exchange is mandatory. |
| `symbolName` | string | true | Symbol name of the scrip. For Equity, enter the SymbolName of the scrip. For Derivatives, enter the TradingSymbol of the scrip. |
| `transactionType` | string | true | Determines whether the order is a buy or sell transaction. |
| `quantity` | string | true | Defines the number of units or shares of the asset to be bought or sold. |
| `productType` | string | true | Product type of the order. Can be CNC, NRML. The valid product type for F&O (Futures and Options) is NRML. |
| `orderType` | string | true | Type of order placed. Can be MKT (Market Order) or L (Limit Order). |
| `triggerPrice` | string | true | Represents the market-entry price level for the placed order. |
| `limitPrice` | string | true | Required for L (Limit) orders. This is the price at which the order is executed in the market. |
| `marketProtection` | string | true | Required for market orders. Default is set to 3% to protect the order from potential market losses. |

### Sample Request Body

**LIMIT ORDER**

```json
requestBody={
  "exchange": "NFO",
  "symbolName": "WIPRO24JUN585PE",
  "transactionType": "BUY",
  "quantity": "1500",
  "productType": "NRML",
  "orderType": "L",
  "triggerPrice": "1180",
  "limitPrice": "1160"
}
```

**MARKET ORDER**

```json
requestBody={
  "exchange": "BFO",
  "symbolName": "SENSEX502441823950PE",
  "transactionType": "BUY",
  "quantity": "1",
  "productType": "NRML",
  "orderType": "MKT",
  "triggerPrice": "12",
  "marketProtection" : ""
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/gttoco/addGtt' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"exchange":"NFO","symbolName":"WIPRO24JUN585PE","transactionType":"BUY","quantity":"1500","productType":"NRML","orderType":"L","triggerPrice":"1180","limitPrice":"1160"}'
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
          "exchange": "NFO",
          "symbolName": "WIPRO24JUN585PE",
          "transactionType": "BUY",
          "quantity": "1500",
          "productType": "NRML",
          "orderType": "L",
          "triggerPrice": "1180",
          "limitPrice": "1160"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/gttoco/addGtt"))
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
    exchange: "NFO",
    symbolName: "WIPRO24JUN585PE",
    transactionType: "BUY",
    quantity: "1500",
    productType: "NRML",
    orderType: "L",
    triggerPrice: "1180",
    limitPrice: "1160"
  };

  const response = await fetch('https://tradeapi.samco.in/gttoco/addGtt', {
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
  "exchange": "NFO",
  "symbolName": "WIPRO24JUN585PE",
  "transactionType": "BUY",
  "quantity": "1500",
  "productType": "NRML",
  "orderType": "L",
  "triggerPrice": "1180",
  "limitPrice": "1160"
}

r = requests.post('https://tradeapi.samco.in/gttoco/addGtt',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

**LIMIT ORDER**

```json
{
  "serverTime": "30/05/24 11:42:25",
  "msgId": "b74e09a8-4925-42cd-bca3-2a96872684e0",
  "status": "Success",
  "statusMessage": "GTT CREATED",
  "gttSummaryId": "140954",
  "orderDetails": {
    "productType": "NRML",
    "orderType": "L",
    "triggerPrice": "1180",
    "marketProtection": "",
    "transactionType": "BUY",
    "triggerId": "177902",
    "symbol": "146465_NFO",
        "symbolName": "WIPRO24JUN585PE",
        "createdAt": "2024-05-30 11:42:25"
    }
}
```

**MARKET ORDER**

```json
{
    "serverTime": "29/05/24 18:47:38",
    "msgId": "5e1d73de-347a-4174-8dde-70d5f9c1c56b",
    "status": "Success",
    "statusMessage": "GTT CREATED",
    "gttSummaryId": "931720",
    "orderDetails": {
        "productType": "NRML",
        "orderType": "MKT",
        "triggerPrice": "11.7",
        "marketProtection": "3",
        "transactionType": "BUY",
        "triggerId": "1325140",
        "symbol": "14366_NSE",
        "symbolName": "IDEA",
        "createdAt": "2024-05-29 18:47:38"
    }
}
```

**400**

```json
{
  "serverTime": "14/05/24 13:49:07",
  "status": "Failure",
  "statusMessage": "No Symbol found for the provided symbol name and exchange."
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | The timestamp when the server generated the response. |
| `msgId` | string | A unique identifier for the message, used to track the response. |
| `status` | string | The status of the API response. Possible values: 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message providing additional details about the status. |
| `gttSummaryId` | string | Uniquely identifies the GTT order, essential for modifying, retrieving status, and deleting. |
| `productType` | string | The product type used in the order. |
| `orderType` | string | The type of order placed. |
| `triggerPrice` | string | The price at which the GTT order is triggered. |
| `marketProtection` | string | An optional field for market protection, used to limit market exposure. |
| `transactionType` | string | Indicates whether the order is a buy or sell transaction. |
| `triggerId` | string | A unique identifier for the GTT trigger. |
| `symbol` | string | The actual name of the symbol for the scrip. |
| `symbolName` | string | The name of the financial instrument. |
| `createdAt` | string | The timestamp when the GTT order was created. |

---

## Modify GTT

`PUT /gttoco/modifyGtt`

Modifying a GTT (Good Till Triggered) order allows investors to adjust the parameters of their existing GTT orders. This can include changing the trigger price, altering the quantity of the order, productType, limitPrice, marketProtection or modifying the order type.

> **INFO** — **Steps to modify a GTT (Good Till Trigger) order :**
>
> 1. Retrieve all active GTT orders using the [List GTT OCO](#list-gtt-oco) API. In the 'List GTT OCO ' API response, we will get both active GTT and GTT OCO orders. To identify an GTT order, check if the 'triggers' key in the API response contains 'gtt' key. If it does, then it is an GTT order.
> 2. Note down the GTT summary ID of the order you wish to modify.Then, based on the parameters provided below, you can modify your order.

> **DANGER** — After the order is modified, a new gttSummaryId is generated. For any further operation, this new gttSummaryId will be valid for this order and the old gttSummaryId becomes invalid.

### Parameter

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | true | The valid exchange will remain the same as it was at the time of creating the GTT. It cannot be modified. |
| `symbolName` | string | true | The symbol name will also remain the same as it was at the time of creating the GTT. It cannot be modified. |
| `transactionType` | string | true | Determines whether the order is a buy or sell transaction. |
| `quantity` | number | true | Defines the number of units or shares of the asset to be bought or sold. |
| `productType` | string | true | Product type of the order. Can be CNC (Cash and Carry) or NRML (Normal). |
| `orderType` | string | true | Type of order placed. Can be MKT (Market Order) or L (Limit Order). |
| `triggerPrice` | number | true | Represents the market-entry price level for the placed order. |
| `limitPrice` | number | true | Price at which the order is executed in the market. |
| `marketProtection` | string | true | Required for market orders. Default is set to 3% to protect the order from potential market losses. |
| `gttSummaryId` | number | true | Enter the gttSummaryId of the GTT order you want to modify. |

### Sample Request Body

```json
requestBody={
  "symbolName": "WIPRO24JUN585PE", 
  "exchange": "NFO",
  "transactionType": "BUY", 
  "orderType": "MKT",
  "quantity": "500",
  "productType": "NRML",
  "triggerPrice": "124.7",
  "limitPrice": "126.7",
  "marketProtection": "12",
  "gttSummaryId":"945505"
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X PUT 'https://tradeapi.samco.in/gttoco/modifyGtt' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"symbolName":"WIPRO24JUN585PE","exchange":"NFO","transactionType":"BUY","orderType":"MKT","quantity":"500","productType":"NRML","triggerPrice":"124.7","limitPrice":"126.7","marketProtection":"12","gttSummaryId":"945505"}'
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
          "symbolName": "WIPRO24JUN585PE",
          "exchange": "NFO",
          "transactionType": "BUY",
          "orderType": "MKT",
          "quantity": "500",
          "productType": "NRML",
          "triggerPrice": "124.7",
          "limitPrice": "126.7",
          "marketProtection": "12",
          "gttSummaryId": "945505"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/gttoco/modifyGtt"))
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
    symbolName: "WIPRO24JUN585PE",
    exchange: "NFO",
    transactionType: "BUY",
    orderType: "MKT",
    quantity: "500",
    productType: "NRML",
    triggerPrice: "124.7",
    limitPrice: "126.7",
    marketProtection: "12",
    gttSummaryId: "945505"
  };

  const response = await fetch('https://tradeapi.samco.in/gttoco/modifyGtt', {
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
  "symbolName": "WIPRO24JUN585PE",
  "exchange": "NFO",
  "transactionType": "BUY",
  "orderType": "MKT",
  "quantity": "500",
  "productType": "NRML",
  "triggerPrice": "124.7",
  "limitPrice": "126.7",
  "marketProtection": "12",
  "gttSummaryId": "945505"
}

r = requests.put('https://tradeapi.samco.in/gttoco/modifyGtt',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

**200**

```json
{
    "serverTime": "02/06/24 12:00:52",
    "msgId": "82452735-e3b8-4fc4-8346-0ef314b5a404",
    "status": "Success",
    "statusMessage": "GTT MODIFIED",
    "gttSummaryId": "945510",
    "orderDetails": {
        "productType": "NRML",
        "orderType": "MKT",
        "triggerPrice": "124.7",
        "marketProtection": "12",
        "transactionType": "BUY",
        "limitPrice": "",
        "symbol": "146465_NFO",
        "symbolName": "WIPRO24JUN585PE",
        "quantity": "500"
    }
}
```

**400**

```json

{
  "serverTime": "15/05/24 18:49:18",
  "msgId": "e4d832c0-c7ac-405c-bf0a-6eebc9214150",
  "status": "Failure",
  "statusMessage": "TRIGGER DOES NOT EXIST",
  "orderDetails": {
    "productType": "NRML",
    "orderType": "MKT",
    "triggerPrice": "124.7",
    "marketProtection": "12",
    "transactionType": "SELL",
    "limitPrice": "",
    "symbol": "532540_BSE",
    "symbolName": "TCS",
    "quantity": "500"
  }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | The time when the server processed the request. |
| `msgId` | string | A unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | The status of the API response. Possible values: 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `gttSummaryId` | string | After the order is modified, a new gttSummaryId is generated. Use this new gttSummaryId for further operations; the old one becomes invalid. |
| `orderDetails` | Object | Details of the modified order. |
| `productType` | string | The product type of the order. |
| `orderType` | string | The type of order. |
| `triggerPrice` | string | The trigger price for the order. |
| `marketProtection` | string | The market protection percentage for the order. |
| `transactionType` | string | The transaction type for the order. |
| `limitPrice` | string | The price at which the order is executed in the market. |
| `symbol` | string | The actual name of the symbol for the scrip. |
| `symbolName` | string | The name of the symbol representing the scrip. |
| `quantity` | string | Defines the number of units or shares of the asset to be bought or sold. |

---

## Delete GTT

Deleting a GTT order cancels it before execution, removing it from the exchange's order book and preventing future execution. Once GTT is triggered, deletion is not possible.

`DELETE /gttoco/deleteGtt`

> **INFO** — **Steps to Delete a GTT (Good Till Trigger) order :**
>
> 1. Retrieve all active GTT orders using the [List GTT OCO](#list-gtt-oco) API. In the 'List GTT OCO ' API response, we will get both active GTT and GTT OCO orders. To identify an GTT order, check if the 'triggers' key in the API response contains 'gtt' key. If it does, then it is an GTT order.
> 2. Note down the GTT summary ID of the order you wish to delete.

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `gttSummaryId` | number | true | Enter the gttSummaryId of the GTT order you want to delete here. |

### Sample Request Body

```json
requestBody={
  "gttSummaryId" : 136045
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X DELETE 'https://tradeapi.samco.in/gttoco/deleteGtt' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"gttSummaryId":136045}'
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
          "gttSummaryId": 136045
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/gttoco/deleteGtt"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .method("DELETE", HttpRequest.BodyPublishers.ofString(requestBody))
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
    gttSummaryId: 136045
  };

  const response = await fetch('https://tradeapi.samco.in/gttoco/deleteGtt', {
    method: 'DELETE',
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
  "gttSummaryId": 136045
}

r = requests.delete('https://tradeapi.samco.in/gttoco/deleteGtt',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
  "serverTime": "28/02/24 12:49:19",
  "status": "Success",
  "msgId": "a62afb04-84a5-4d3d-ba5b-3299cce4fd77",
  "gttSummaryId": "136045",
  "statusMessage": "GTT order Deleted",
  "orderDetails": {
    "userId": "RM1001"
  }
}
```

### Response Schema

Status Code **200**

| Name | Type | Description |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | A unique identifier for the API response message. This can be useful for tracking or debugging purposes. |
| `status` | string | The status of the API response. It can be either 'Success', 'Error' or 'Failure' |
| `statusMessage` | string | A message describing the result of the API call. |
| `gttSummaryId` | string | gttSummaryId of the order which is deleted. |
| `userId` | string | User ID of the user who deleted the order. |

---

## Add OCO

`POST /gttoco/addOco`

Add OCO refers to the functionality of adding an OCO (One-Cancels-the-Other) condition to a GTT (Good Till Triggered) order. With this feature, investors can set up two separate exit conditions for a single position. If one condition is triggered and the corresponding order is executed, the other order is automatically canceled, hence the "one-cancels-the-other" concept.

#### Here’s how it works?

- Let’s say you are holding a stock in your portfolio and you have kept a target and stoploss in mind for exiting this stock.
- You can place a GTT OCO order and Enter your target trigger and stoploss trigger along with respective order prices. Once you’ve entered your target and stoploss prices, our system will start monitoring the market.
- If the price of your stock reaches your target price, our system will automatically place a sell order with target price for you. In this scenario, your stoploss trigger will get canceled automatically.
- If the price of your stock reaches your stoploss price, our system will automatically place a sell order with stoploss price for you. In this scenario, your target trigger will get canceled automatically. [Read More....](https://www.samco.in/help-support/article/all-about-gtt-oco-good-till-triggered-one-cancels-other/)

> **INFO** — In the BFO exchange, only SENSEX and BANKEX trades are allowed.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | true | Name of the exchange. Valid values: BSE, NSE, NFO, BFO, MFO, MCX, CDS. Default is NSE if not provided. Mandatory for BSE, NFO, BFO, MFO, CDS, and MCX. |
| `symbolName` | string | true | Symbol name of the scrip. For Equity, enter SymbolName of the scrip. For Derivatives, enter TradingSymbol of the scrip. |
| `transactionType` | string | true | Determines whether the order is a buy or sell transaction. EQ delivery buy orders are not allowed in GTT. |
| `quantity` | string | true | Defines the number of units or shares of the asset to be bought or sold. |
| `productType` | string | true | Product type of the order. Can be CNC (Cash and Carry) or NRML (Normal). |
| `orderType` | string | true | Type of order placed. Can be MKT (Market Order) or L (Limit Order). |
| `targetTriggerPrice` | string | true | The price at which the order will enter the market. |
| `targetLimitPrice` | string | true | Required for limit orders. The price at which the order will be executed on the exchange. |
| `stoplossTriggerPrice` | string | false | The price at which the stop-loss order will enter the market. |
| `stoplossLimitPrice` | string | true | Required for limit orders. The price at which the stop-loss order will be executed on the exchange. |
| `marketProtection` | string | true | Required for market orders. Default is set to 3% to protect the order from potential market losses. |

### Sample Request Body

**LIMIT ORDER**

```json
requestBody={
  "exchange": "NSE", 
  "symbolName": "IDEA", 
  "transactionType": "SELL", 
  "quantity": "1", 
  "productType": "NRML",
  "orderType": "L", 
  "targetTriggerPrice": "14.5",
  "targetLimitPrice": "15",
  "stoplossTriggerPrice": "13.95",
  "stoplossLimitPrice": "12.90"
}
```

**MARKET ORDER**

```json
requestBody={
  "exchange": "NSE", 
  "symbolName": "IDEA", 
  "transactionType": "SELL", 
  "quantity": "1", 
  "productType": "NRML",
  "orderType": "MKT", 
  "targetTriggerPrice": "14.5",
  "stoplossTriggerPrice": "13.95",
  "marketProtection": ""
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/gttoco/addOco' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"exchange":"NSE","symbolName":"IDEA","transactionType":"SELL","quantity":"1","productType":"NRML","orderType":"L","targetTriggerPrice":"14.5","targetLimitPrice":"15","stoplossTriggerPrice":"13.95","stoplossLimitPrice":"12.90"}'
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
          "exchange": "NSE",
          "symbolName": "IDEA",
          "transactionType": "SELL",
          "quantity": "1",
          "productType": "NRML",
          "orderType": "L",
          "targetTriggerPrice": "14.5",
          "targetLimitPrice": "15",
          "stoplossTriggerPrice": "13.95",
          "stoplossLimitPrice": "12.90"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/gttoco/addOco"))
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
    exchange: "NSE",
    symbolName: "IDEA",
    transactionType: "SELL",
    quantity: "1",
    productType: "NRML",
    orderType: "L",
    targetTriggerPrice: "14.5",
    targetLimitPrice: "15",
    stoplossTriggerPrice: "13.95",
    stoplossLimitPrice: "12.90"
  };

  const response = await fetch('https://tradeapi.samco.in/gttoco/addOco', {
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
  "exchange": "NSE",
  "symbolName": "IDEA",
  "transactionType": "SELL",
  "quantity": "1",
  "productType": "NRML",
  "orderType": "L",
  "targetTriggerPrice": "14.5",
  "targetLimitPrice": "15",
  "stoplossTriggerPrice": "13.95",
  "stoplossLimitPrice": "12.90"
}

r = requests.post('https://tradeapi.samco.in/gttoco/addOco',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample response

**LIMIT ORDER**

```json
{
    "serverTime": "29/05/24 18:54:01",
    "msgId": "505b7b1b-f3d9-4597-86ac-cb0accc21898",
    "status": "Failure",
    "statusMessage": "Failure",
    "orderDetails": {
        "transactionType": "SELL",
        "symbol": "14366_NSE",
        "symbolName": "IDEA-EQ",
        "productType": "NRML",
        "orderType": "L",
        "target": {
            "quantity": "1",
            "triggerPrice": "14.5",
            "limitPrice": "15",
            "marketProtection": "",
            "type": "TARGET",
            "triggerId": "0"
        },
        "stopLoss": {
            "quantity": "1",
            "triggerPrice": "13.95",
            "limitPrice": "12.90",
            "marketProtection": "",
            "type": "STOPLOSS",
            "triggerId": "0"
        }
    }
}
```

**MARKET ORDER**

```json
{
    "serverTime": "29/05/24 18:51:12",
    "msgId": "8f7d196b-c432-43fb-a2b3-34e134d00035",
    "status": "Failure",
    "statusMessage": "Failure",
    "orderDetails": {
        "transactionType": "SELL",
        "symbol": "14366_NSE",
        "symbolName": "IDEA-EQ",
        "productType": "NRML",
        "orderType": "MKT",
        "target": {
            "quantity": "1",
            "triggerPrice": "14.5",
            "limitPrice": "",
            "marketProtection": "3",
            "type": "TARGET",
            "triggerId": "0"
        },
        "stopLoss": {
            "quantity": "1",
            "triggerPrice": "13.95",
            "limitPrice": "",
            "marketProtection": "3",
            "type": "STOPLOSS",
            "triggerId": "0"
        }
    }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | The time when the server processed the request. |
| `msgId` | string | A unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | The status of the API response. Possible values: 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `gttSummaryId` | string | Uniquely identifies the GTT order, essential for modifying, retrieving status, and deleting. |
| `transactionType` | string | Determines whether the order is a buy or sell transaction. |
| `symbol` | string | The actual name of the symbol for the scrip. |
| `symbolName` | string | The name of the symbol representing the scrip. |
| `productType` | string | The product type of the order. |
| `orderType` | string | The type of order. |
| `target` | object | An object containing details about the target order. |
| `stopLoss` | object | An object containing details about the stop-loss order. |
| `quantity` | string | The number of units to be traded. |
| `triggerPrice` | string | The price at which the target order will be triggered. |
| `limitPrice` | string | The maximum price at which the order will be executed. |
| `marketProtection` | string | An object containing details about the market protection. |
| `type` | string | The "TARGET" type indicates a target order, while "STOPLOSS" signifies a stop-loss order. |
| `triggerId` | string | An identifier for the trigger. |

---

## Modify OCO

`PUT /gttoco/modifyOco`

Modifying a GTT OCO (Good Till Triggered, One-Cancels-the-Other) order involves adjusting the parameters of an existing GTT OCO order. This can include changing the trigger prices, adjusting the quantity of the order, or modifying the order types.

When modifying a GTT OCO order, investors can make changes to both legs of the OCO order, ensuring that the exit strategies remain aligned with their trading objectives and market conditions. For example, if market conditions change and the investor wants to adjust their profit target or stop-loss levels, they can modify the trigger prices accordingly.

> **INFO** — **Steps to modify a GTT OCO order :**
>
> 1. Retrieve all active GTT orders using the [List GTT OCO](#list-gtt-oco) API. In the 'List GTT OCO ' API response, we will get both active GTT and GTT OCO orders. To identify an OCO order, check if the 'triggers' key in the API response contains both 'stopLoss' and 'target' keys. If it does, then it is an OCO order.
> 2. Note down the GTT summary ID of the order you wish to modify.Then, based on the parameters provided below, you can modify your order.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | true | The exchange remains the same as when creating the GTT OCO. It cannot be modified. |
| `symbolName` | string | true | The symbol name remains the same as when creating the GTT OCO. It cannot be modified. |
| `transactionType` | string | true | Determines whether the order is a buy or sell transaction. |
| `quantity` | string | true | Defines the number of units or shares of the asset to be bought or sold. |
| `productType` | string | true | Product type of the order. Can be CNC (Cash and Carry) or NRML (Normal). |
| `orderType` | string | true | Type of order placed. Can be MKT (Market Order) or L (Limit Order). |
| `targetTriggerPrice` | string | true | The price at which the target order will enter the market. |
| `targetLimitPrice` | string | true | Required for limit orders. The price at which the target order will be executed on the exchange. |
| `stoplossTriggerPrice` | string | true | The price at which the stop-loss order will enter the market. |
| `stoplossLimitPrice` | string | true | Required for limit orders. The price at which the stop-loss order will be executed on the exchange. |
| `marketProtection` | string | true | Required for market orders. Default is set to 3% to protect the order from potential market losses. |
| `gttSummaryId` | number | true | Enter the gttSummaryId of the GTT OCO order you want to modify here. |

### Sample Request Body

```json
requestBody={
  "exchange": "NSE",
  "symbolName": "IDEA",
  "transactionType": "SELL",
  "quantity": "25",
  "productType": "CNC",
  "orderType": "L",
  "targetTriggerPrice": "13.5",
  "targetLimitPrice": "13.5",
  "stoplossTriggerPrice": "10.5",
  "stoplossLimitPrice": "10.5",
  "marketProtection": "",
  "gttSummaryId" : 670745
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X PUT 'https://tradeapi.samco.in/gttoco/modifyOco' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"exchange":"NSE","symbolName":"IDEA","transactionType":"SELL","quantity":"25","productType":"CNC","orderType":"L","targetTriggerPrice":"13.5","targetLimitPrice":"13.5","stoplossTriggerPrice":"10.5","stoplossLimitPrice":"10.5","marketProtection":"","gttSummaryId":670745}'
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
          "exchange": "NSE",
          "symbolName": "IDEA",
          "transactionType": "SELL",
          "quantity": "25",
          "productType": "CNC",
          "orderType": "L",
          "targetTriggerPrice": "13.5",
          "targetLimitPrice": "13.5",
          "stoplossTriggerPrice": "10.5",
          "stoplossLimitPrice": "10.5",
          "marketProtection": "",
          "gttSummaryId": 670745
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/gttoco/modifyOco"))
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
    exchange: "NSE",
    symbolName: "IDEA",
    transactionType: "SELL",
    quantity: "25",
    productType: "CNC",
    orderType: "L",
    targetTriggerPrice: "13.5",
    targetLimitPrice: "13.5",
    stoplossTriggerPrice: "10.5",
    stoplossLimitPrice: "10.5",
    marketProtection: "",
    gttSummaryId: 670745
  };

  const response = await fetch('https://tradeapi.samco.in/gttoco/modifyOco', {
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
  "exchange": "NSE",
  "symbolName": "IDEA",
  "transactionType": "SELL",
  "quantity": "25",
  "productType": "CNC",
  "orderType": "L",
  "targetTriggerPrice": "13.5",
  "targetLimitPrice": "13.5",
  "stoplossTriggerPrice": "10.5",
  "stoplossLimitPrice": "10.5",
  "marketProtection": "",
  "gttSummaryId": 670745
}

r = requests.put('https://tradeapi.samco.in/gttoco/modifyOco',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Response

```json
{
  "serverTime": "04/04/24 13:53:23",
  "msgId": "432b12e6-6acc-4b38-98b3-3940e09d0c26",
  "status": "Success",
  "statusMessage": "GTT MODIFIED",
  "gttSummaryId": "671170",
  "orderDetails": {
    "transactionType": "SELL",
    "orderType": "L",
    "symbol": "14366_NSE",
    "symbolName": "IDEA",
    "productType": "CNC",
    "target": {
      "limitPrice": "13.5",
      "triggerId": "932815",
      "triggerPrice": "13.5",
      "type": "TARGET",
      "quantity": "25",
      "marketProtection": ""
    },
    "stopLoss": {
      "limitPrice": "10.5",
      "triggerId": "932820",
      "triggerPrice": "10.5",
      "type": "STOPLOSS",
      "quantity": "25",
      "marketProtection": ""
    }
  }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | A unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | The status of the API response. It can be either 'Success' or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `gttSummaryId` | string | After the order is modified, a new gttSummaryId is generated. For any further operation, this gttSummaryId will be valid for this order and the old gttSummaryId becomes invalid. |
| `transactionType` | string | Describes whether the transaction involves buying or selling. |
| `orderType` | string | The type of order. |
| `symbol` | string | The actual name of the symbol for the scrip. |
| `symbolName` | string | The name of the symbol representing the scrip. |
| `productType` | string | The product type of the order. |
| `target` | object | An object containing details about the target order. |
| `stopLoss` | object | An object containing details about the stop loss order. |

---

## Delete OCO

`DELETE /gttoco/deleteOco`

Deleting an OCO (One-Cancels-the-Other) order involves canceling both legs of the order simultaneously. In an OCO order, when one part of the order is executed, the other part is automatically canceled. However, if the investor decides to delete the entire OCO order before either part is executed, they can do so using the delete OCO API.

> **INFO** — **Steps to Delete a GTT OCO order :**
>
> 1. Retrieve all active GTT orders using the [List GTT OCO](#list-gtt-oco) API. In the 'List GTT OCO ' API response, we will get both active GTT and GTT OCO orders. To identify an OCO order, check if the 'triggers' key in the API response contains both 'stopLoss' and 'target' keys. If it does, then it is an OCO order.
> 2. Note down the GTT summary ID of the order you wish to delete.

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `gttSummaryId` | number | true | Enter the gttSummaryId of the GTT order you want to delete here. |

### Sample Request Body

```json
requestBody={
    "gttSummaryId" : 136045
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X DELETE 'https://tradeapi.samco.in/gttoco/deleteOco' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"gttSummaryId":136045}'
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
          "gttSummaryId": 136045
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/gttoco/deleteOco"))
        .header("Content-Type", "application/json")
        .header("Accept", "application/json")
        .header("x-session-token", "<SESSION_TOKEN>")
        .method("DELETE", HttpRequest.BodyPublishers.ofString(requestBody))
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
    gttSummaryId: 136045
  };

  const response = await fetch('https://tradeapi.samco.in/gttoco/deleteOco', {
    method: 'DELETE',
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
  "gttSummaryId": 136045
}

r = requests.delete('https://tradeapi.samco.in/gttoco/deleteOco',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Response

```json
{
  "serverTime": "28/02/24 12:49:19",
  "status": "Success",
  "msgId": "a62afb04-84a5-4d3d-ba5b-3299cce4fd77",
  "gttSummaryId": "136045",
  "statusMessage": "GTT OCO order Deleted",
  "orderDetails": {
    "userId": "RM1001"
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
| `gttSummaryId` | string | gttSummaryId of the order which is deleted. |
| `userId` | string | User ID of the user who deleted the order. |

---

## List GTT OCO

`GET /gttoco/listGttOco`

Using the list OCO, we can retrieve the list of active GTT OCO, triggered GTT OCO, and expired GTT OCO.

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listType` | string | true | Type of list. valid type is (active / triggered / expired). If the user does not provide a listType, by default considered as active. |

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/gttoco/listGttOco?listType=active' \
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
        .uri(URI.create("https://tradeapi.samco.in/gttoco/listGttOco?listType=active"))
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

  const response = await fetch('https://tradeapi.samco.in/gttoco/listGttOco?listType=active', {
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

r = requests.get('https://tradeapi.samco.in/gttoco/listGttOco?listType=active',
  headers=headers)

print(r.json())
```

### Sample Responses

**200**

```json
{
  "serverTime": "04/04/24 14:18:54",
  "msgId": "ec67dc5b-d626-4e16-a3eb-461ac37bb93b",
  "status": "Success",
  "statusMessage": "List of GTT / OCO orders received.",
  "orderDetails": [
    {
      "summary": {
        "id": 136027,
        "userId": "RM1001",
        "symbol": "14366_NSE",
        "symbolName": "IDEA",
        "orderType": "L",
        "productType": "CNC",
        "gttType": "SINGLE",
        "validTill": "FOREVER",
        "createdAt": "2024-02-28 17:52:27",
        "deletedAt": "",
        "gttSummaryId": "136027",
        "isExpired": false,
      },
      "triggers": {
        "gtt": {
          "status": "",
          "triggeredAt": "",
          "triggerId": "172714",
          "gttId": "172714",
          "quantity": "1",
          "limitPrice": "13.25",
          "marketProtection": "",
          "ltpAtCreation": "16.30",
          "triggerPrice": "13.50",
          "transactionType": "BUY",
          "rejectReason": "",
          "orderNumber": ""
        }
      }
    }
  ]
}
```

**400**

```json
{
  "serverTime": "16/05/24 18:51:28",
  "status": "Failure",
  "validationErrors": [
    " Enter a valid listType ( active / triggered / expired)."
  ]
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
| `summary` | object | Summary data for GTT orders. |
| `gtt` | object | GTT order details available for GTT orders. |
| `target` | object | Target details available for OCO orders. |
| `stopLoss` | object | Stoploss details available for OCO orders. |
