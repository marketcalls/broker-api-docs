# Basket Orders

Group multiple orders into a basket, manage its legs, calculate margin, and execute the basket in one call.

## Introducing the New Basket Order API Feature!

We are thrilled to announce the launch of our new Basket Order feature within our API! This feature has been one of the most requested by our intraday traders, and we are excited to deliver it to you.

### What are Basket Orders?

Basket Orders enable you to place multiple trade orders at once, covering a range of instruments, including options, futures, and equities. This is particularly beneficial for traders looking to execute strategies that involve multiple positions, allowing for better coordination and efficiency.

### Key Features of the Basket Order API

1. **Simultaneous Order Placement:**With a single API call, you can execute multiple orders across different assets. This saves you time and reduces the hassle of placing individual orders one at a time.
2. **Margin Insights:**The Basket Order API provides crucial margin calculations:

   - **Max Margin:**This shows the maximum margin requirement for the entire basket, helping you understand your total capital commitment.
   - **Final Margin:**This value reflects the margin after considering hedge margin benefits, allowing you to see the actual amount that will be blocked in your account when executing the basket.
3. **Real-time Updates:**The API offers real-time information on order statuses and margin requirements, ensuring you are always informed about your positions.
4. **Improved Risk Management:** By consolidating orders, you can implement better risk management strategies, monitoring your exposure across multiple instruments simultaneously.
5. **User-Friendly Documentation:**Comprehensive documentation is available to guide you through the implementation process, making it easier to integrate the Basket Order feature into your trading applications.

### Benefits

Increased Efficiency: Trade multiple contracts with a single request, streamlining your trading process. Better Capital Utilization: Understand and manage your margin requirements more effectively. Enhanced Trading Strategies: Execute complex trading strategies with ease and confidence.

- **Increased Efficiency:**Trade multiple contracts with a single request, streamlining your trading process.
- **Better Capital Utilization:**Understand and manage your margin requirements more effectively.
- **Enhanced Trading Strategies:**Execute complex trading strategies with ease and confidence.

### Get Started

To utilize the new Basket Order feature, refer to our updated API documentation, which provides detailed instructions on how to place basket orders, check margin requirements, and monitor order statuses.

We believe the new Basket Order API feature will significantly enhance your trading experience and help you achieve your trading goals more efficiently. [**Read More..**](https://www.samco.in/knowledge-center/articles/introducing-basket-orders/)

---

## Create Basket

`POST /basket/createBasket`

### What is a Basket?

In trading, a basket is a collection of different financial assets such as stocks, future, or options that are grouped together. This allows traders and investors to buy or sell multiple assets in one single transaction, rather than dealing with each one individually.

> **DANGER** — Basket name can only contain alphabets, numbers, hyphen, and space

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `basketName` | string | true | The basket name is a label or identifier you give to a collection of financial assets grouped together as a basket. |

### Sample Request Body

```json
requestBody={
  "basketName": "Basket Name"
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/basket/createBasket' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"basketName":"Basket Name"}'
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
          "basketName": "Basket Name"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/basket/createBasket"))
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
    basketName: "Basket Name"
  };

  const response = await fetch('https://tradeapi.samco.in/basket/createBasket', {
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
  "basketName": "Basket Name"
}

r = requests.post('https://tradeapi.samco.in/basket/createBasket',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

**200**

```json
{
    "serverTime": "08/08/24 19:06:22",
    "msgId": "b8d2d66b-2729-46eb-b799-7f2055008a57",
    "status": "Success",
    "statusMessage": "Basket created successfully",
    "basketDetails": {
        "basketId": 64,
        "basketName": "NIFTY FO"
    }
}
```

**400**

```json
{
    "serverTime": "08/08/24 19:07:00",
    "msgId": "dccaa746-f30c-48cf-96cf-2eca0f50949a",
    "status": "Failure",
    "statusMessage": "You have reached the maximum order limit of 50 orders. Please remove existing orders and try again."
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | Status of the order cancellation request. Can be 'success' or 'failure'. |
| `statusMessage` | string | Status message for the order cancellation request. |
| `basketDetails` | string | An object that contains information about a specific trading basket. |
| `basketId` | string | A unique identifier for the basket. It is typically a numeric value that allows for easy reference and management of the basket within the trading system. |
| `basketName` | string | The name of the basket. This string provides a human-readable identifier for the basket, helping users understand its purpose or the assets it contains. |

---

## Modify Basket

`PUT basket/modifyBasket`

The modifyBasket API allows users to update the name of an existing trading basket identified by its unique basket ID.

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `basketName` | string | true | The new name for the basket. This is the only modifiable parameter. |
| `basketId` | string | true | The unique identifier of the basket that you want to modify. |

### Sample Request Body

```json
requestBody={
    "basketName" : "Testing basket for 37283",
    "basketId": "55"
}
```

### Sample Code

**cURL**

```bash
curl -X PUT 'https://tradeapi.samco.in/basket/modifyBasket' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"basketName":"Testing basket for 37283","basketId":"55"}'
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
          "basketName": "Testing basket for 37283",
          "basketId": "55"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/basket/modifyBasket"))
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
    basketName: "Testing basket for 37283",
    basketId: "55"
  };

  const response = await fetch('https://tradeapi.samco.in/basket/modifyBasket', {
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
  "basketName": "Testing basket for 37283",
  "basketId": "55"
}

r = requests.put('https://tradeapi.samco.in/basket/modifyBasket',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

**200**

```json
{
    "serverTime": "08/08/24 19:19:34",
    "msgId": "80c30a7b-77e1-4231-a0c7-102e1c6ad9f4",
    "status": "Success",
    "statusMessage": "Basket name updated successfully",
    "basketDetails": {
        "basketId": 55,
        "basketName": "Testing basket for 37283"
    }
}
```

**400**

```json
{
    "serverTime": "08/08/24 19:19:54",
    "msgId": "dfa4cb48-a042-4c75-90fd-2f2cd4b7a912",
    "status": "Failure",
    "statusMessage": "Basket name already exists"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | Status of the order cancellation request. Can be 'success' or 'failure'. |
| `statusMessage` | string | Status message for the order cancellation request. |
| `basketDetails` | string | An object that contains information about a specific trading basket. |
| `basketId` | string | A unique identifier for the basket. It is typically a numeric value that allows for easy reference and management of the basket within the trading system. |
| `basketName` | string | The name of the basket. This string provides a human-readable identifier for the basket, helping users understand its purpose or the assets it contains. |

---

## Delete Basket

`DELETE basket/deleteBasket`

This API endpoint allows users to delete a specified trading basket from their account. By removing the trading basket identified by the given basket ID, all associated trades and configurations will be permanently deleted from the system.

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `basketId` | string | true | The unique identifier of the trading basket to be deleted. |

### Sample Request Body

```json
requestBody={
    "basketId" : "65"
}
```

### Sample Code

**cURL**

```bash
curl -X DELETE 'https://tradeapi.samco.in/basket/deleteBasket' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"basketId":"65"}'
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
          "basketId": "65"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/basket/deleteBasket"))
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
    basketId: "65"
  };

  const response = await fetch('https://tradeapi.samco.in/basket/deleteBasket', {
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
  "basketId": "65"
}

r = requests.delete('https://tradeapi.samco.in/basket/deleteBasket',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

**200**

```json
{
    "serverTime": "08/08/24 19:08:35",
    "msgId": "b591eeb5-3214-4b0e-b892-81d1ef0e0f01",
    "status": "Success",
    "statusMessage": "Baskets Deleted Successfully"
}
```

**400**

```json
{
    "serverTime": "08/08/24 19:24:29",
    "msgId": "d38debfc-22bd-4faa-8e1c-e5e156aa4a94",
    "status": "Failure",
    "statusMessage": "The provided BasketIds are invalid: [basketId]"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | Status of the order cancellation request. Can be 'success' or 'failure'. |
| `statusMessage` | string | Status message for the order cancellation request. |

---

## List Basket

`GET basket/listBasket`

This API lets you see all the trading baskets you have. Each basket shows the trades inside it, its status (like executed, not executed, or all), and when it was created.

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listType` | string | true | The listType parameter defaults to 'ALL' if not specified. Valid values include 'ALL,' 'EXECUTED,' and 'NOT EXECUTED.' |

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/basket/listBasket?listType=NOT EXECUTED' \
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
        .uri(URI.create("https://tradeapi.samco.in/basket/listBasket?listType=NOT EXECUTED"))
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

  const response = await fetch('https://tradeapi.samco.in/basket/listBasket?listType=NOT EXECUTED', {
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

r = requests.get('https://tradeapi.samco.in/basket/listBasket?listType=NOT EXECUTED',
  headers=headers)

print(r.json())
```

### Sample Responses

**200**

```json
{
    "serverTime": "09/08/24 11:42:06",
    "msgId": "d27758a6-48b2-43d1-bbd0-6be6c1c75948",
    "status": "Success",
    "statusMessage": "List of Baskets fetched successfully",
    "basketList": [
        {
            "basketId": 64,
            "basketName": "NIFTY FO",
            "totalOrders": 0,
            "maxOrders": 100,
            "executedOrders": 0,
            "displayOrder": 63,
            "requiredMargin": "0.00",
            "finalMargin": "0.00",
            "isreArranged": false,
            "deletedContracts": 0,
            "createdAt": "2024-08-08 19:06:22",
            "updatedAt": "",
            "basketStatus": "NOT EXECUTED",
            "chronologicalView": true
        },
    ]
}
```

**400**

```json
{
    "serverTime": "09/08/24 11:48:59",
    "status": "Failure",
    "validationErrors": [
        " Please enter a valid listType - ALL / EXECUTED / NOT EXECUTED "
    ]
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | Unique identifier for every request. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | Status of the order cancellation request. Can be 'success' or 'failure'. |
| `statusMessage` | string | Status message for the order cancellation request. |
| `basketList` | Array of Objects | List of baskets with details about each basket. |
| `basketId` | string | Unique identifier for the basket. |
| `basketName` | string | The name given to the basket, representing its purpose or content. |
| `totalOrders` | string | The total number of orders currently placed within this basket. |
| `maxOrders` | string | The maximum number of orders allowed in this basket. |
| `executedOrders` | string | The number of orders within the basket that have been executed. |
| `displayOrder` | string | The order in which this basket should be displayed in the list. A lower number usually means higher priority. |
| `requiredMargin` | string | The margin required for the orders in this basket, in the account's currency. |
| `finalMargin` | string | The final margin calculated after considering the orders in the basket, also in the account's currency. |
| `isreArranged` | string | Flag indicating whether the orders in the basket have been rearranged (`true`) or not (`false`). |
| `deletedContracts` | string | The number of contracts that have been deleted from the basket. |
| `createdAt` | string | The date and time when the basket was created. |
| `updatedAt` | string | The date and time when the basket was last updated. This field is empty if the basket has not been updated since creation. |
| `basketStatus` | string | The current status of the basket, indicating whether it has been executed ("EXECUTED") or not ("NOT EXECUTED"). |
| `chronologicalView` | string | Indicates whether the orders in the basket are displayed in chronological order (`true`) or not (`false`). |

---

## Create Basket Order

`POST basket/createOrder`

The create order API is used to add a new order to a specified basket. This operation allows users to specify the details of the order, including the product, quantity, and any special instructions.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `basketID` | string | true | The ID of the basket to which the order needs to be added. |
| `symbolName` | string | true | The stock symbol to be traded. |
| `exchange` | string | true | The exchange where the stock is listed. |
| `transactionType` | string | true | Indicates whether the transaction is BUY or SELL. |
| `orderType` | string | true | Specifies the order type (e.g., L - Limit, SL - Stop Limit). |
| `orderValidity` | string | true | Specifies the order's validity duration. |
| `productType` | string | true | Specifies the product type (e.g., CNC - Cash and Carry, CO - Cover Order, BO - Bracket Order, NRML, MIS). |
| `quantity` | string | true | The number of shares or units to be traded. |
| `disclosedQuantity` | string | true | The quantity to be disclosed in the market, which can be equal to or less than the order quantity. |
| `price` | string | false | The execution price for the order. Mandatory for L or SL orders. |
| `priceType` | string | false | Applicable only for BO orders. Valid options: LTP (Last Traded Price) or ATP (Average Traded Price). Default is LTP. |
| `squareOffValue` | string | false | The value used to square off the position automatically. Applicable only for BO orders. |
| `stopLossValue` | string | false | The stop-loss value. Applicable only for BO orders. |
| `valueType` | string | false | The type of value for Stop Loss and Square Off. Valid options: Absolute or Ticks. Default is Absolute. Applicable only for BO orders. |
| `trailingStopLoss` | string | false | Incremental value as a percentage of the price change. The trailing stop loss moves with price increases but stays fixed if the price drops. Applicable only for BO orders. |
| `triggerPrice` | string | false | The price at which the order will be triggered. Applicable for SL orders. |

### Sample Request Body

**MIS ORDER**

```json
requestBody={
  "basketID": "88",
  "symbolName": "INFY",
  "exchange": "NSE",
  "transactionType": "BUY",
  "orderType": "L",
  "orderValidity": "DAY",
  "productType": "MIS",
  "quantity": "150",
  "disclosedQuantity": "",
  "price":"1800",
  "triggerPrice": "1925.30"
}
```

**CNC ORDER**

```json
requestBody={
  "basketID": "88",
  "symbolName": "HDFCBANK",
  "exchange": "NSE",
  "transactionType": "BUY",
  "orderType": "L",
  "orderValidity": "DAY",
  "productType": "CNC",
  "quantity": "50",
  "disclosedQuantity": "50",
  "price": "1600"
}
```

**BO ORDER**

```json
requestBody={
  "basketID": "88",
  "symbolName": "RELIANCE",
  "exchange": "NSE",
  "transactionType": "BUY",
  "orderType": "L",
  "orderValidity": "DAY",
  "productType": "BO",
  "quantity": "100",
  "disclosedQuantity": "50",
  "price": "2700",
  "squareOffValue": "3000",
  "stopLossValue": "2690",
  "valueType": "Absolute",
  "trailingStopLoss": "10",
  "priceType": "LTP"
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/basket/createOrder' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"basketID":"88","symbolName":"INFY","exchange":"NSE","transactionType":"BUY","orderType":"L","orderValidity":"DAY","productType":"MIS","quantity":"150","disclosedQuantity":"","price":"1800","triggerPrice":"1925.30"}'
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
          "basketID": "88",
          "symbolName": "INFY",
          "exchange": "NSE",
          "transactionType": "BUY",
          "orderType": "L",
          "orderValidity": "DAY",
          "productType": "MIS",
          "quantity": "150",
          "disclosedQuantity": "",
          "price": "1800",
          "triggerPrice": "1925.30"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/basket/createOrder"))
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
    basketID: "88",
    symbolName: "INFY",
    exchange: "NSE",
    transactionType: "BUY",
    orderType: "L",
    orderValidity: "DAY",
    productType: "MIS",
    quantity: "150",
    disclosedQuantity: "",
    price: "1800",
    triggerPrice: "1925.30"
  };

  const response = await fetch('https://tradeapi.samco.in/basket/createOrder', {
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
  "basketID": "88",
  "symbolName": "INFY",
  "exchange": "NSE",
  "transactionType": "BUY",
  "orderType": "L",
  "orderValidity": "DAY",
  "productType": "MIS",
  "quantity": "150",
  "disclosedQuantity": "",
  "price": "1800",
  "triggerPrice": "1925.30"
}

r = requests.post('https://tradeapi.samco.in/basket/createOrder',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

**MIS Order**

```json
{
    "serverTime": "26/12/24 16:21:36",
    "msgId": "c5268be4-f1c5-488b-bc86-69b06317aeb0",
    "status": "Success",
    "statusMessage": "Order Added Successfully",
    "basketDetails": {
        "clientId": "RM37283",
        "basketId": 88,
        "basketOrderId": 39,
        "displayOrder": 39,
        "exchange": "NSE",
        "tradingSymbol": "INFY-EQ",
        "transactionType": "BUY",
        "productCode": "MIS",
        "orderType": "L",
        "quantity": 150,
        "orderPrice": 1800,
        "createdAt": "2024-12-26 16:21:38"
    }
}
```

**CNC Order**

```json
{
    "serverTime": "26/12/24 16:28:24",
    "msgId": "d1b5be1c-2dff-4e7d-a566-fd642c594015",
    "status": "Success",
    "statusMessage": "Order Added Successfully",
    "basketDetails": {
        "clientId": "RM37283",
        "basketId": 88,
        "basketOrderId": 41,
        "displayOrder": 41,
        "exchange": "NSE",
        "tradingSymbol": "HDFCBANK-EQ",
        "transactionType": "BUY",
        "productCode": "CNC",
        "orderType": "L",
        "quantity": 50,
        "orderPrice": 1680,
        "createdAt": "2024-12-26 16:28:25"
    }
}
```

**BO Order**

```json
{
    "serverTime": "26/12/24 16:29:21",
    "msgId": "c1f4dadb-06b0-417e-9b73-dc3020851d6d",
    "status": "Success",
    "statusMessage": "Order Added Successfully",
    "basketDetails": {
        "clientId": "RM37283",
        "basketId": 88,
        "basketOrderId": 43,
        "displayOrder": 43,
        "exchange": "NSE",
        "tradingSymbol": "RELIANCE-EQ",
        "transactionType": "BUY",
        "productCode": "BO",
        "orderType": "L",
        "quantity": 100,
        "orderPrice": 1200,
        "stoplossValue": "1190",
        "squareOffValue": "1300",
        "trailingStopLoss": "10",
        "createdAt": "2024-12-26 16:29:21"
    }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | The timestamp when the order response was generated by the server. |
| `msgId` | string | A unique identifier for the order response message. |
| `status` | string | The outcome of the order request (e.g., Success, Failure). |
| `clientId` | string | A unique identifier for the client who placed the order. |
| `basketId` | string | The identity of the user or customer associated with the order. |
| `basketOrderId` | string | The identifier for the specific order in the user's basket. |
| `displayOrder` | string | Dispaly order at this number. |
| `triggerPrice` | string | The price at which a conditional order, such as a Stop Loss, is triggered. |
| `exchange` | string | The stock exchange where the order is being executed (e.g., NSE). |
| `tradingSymbol` | string | The symbol representing the stock or asset being traded (e.g., AAPL). |
| `transactionType` | string | The type of trade (e.g., BUY, SELL). |
| `productCode` | string | The type of trading product (e.g., BO, CO, MIS, CNC, NRML). |
| `orderType` | string | The nature of the order (e.g., L for Limit, SL for Stop Loss). |
| `quantity` | string | The number of units being bought or sold. |
| `orderPrice` | string | The price at which the order was executed or filled. |
| `stoplossValue` | string | The price at which the Stop Loss order will trigger. |
| `squareOffValue` | string | The price at which the order is expected to be squared off (completed). |
| `trailingStopLoss` | string | The price level for a trailing stop loss, adjusting as the price moves. |
| `createdAt` | string | The timestamp when the order was initially placed. |

---

## Modify Basket Order

`PUT basket/modifyBasketOrder`

The modifyBasketOrder API allows you to modify an existing order within a specific basket by targeting the order's unique ID. This API enables you to adjust various parameters of the order, such as quantity, price, or other details, ensuring that the order aligns with updated trading strategies or market conditions. It's designed to provide flexibility and precision in managing your basket orders.

> **DANGER** — In a `modify order`, we can replace the old order with the same order ID with a new order.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `basketOrderId` | string | true | Unique identifier of the specific order within the basket that you want to modify. |
| `basketId` | string | true | Unique identifier of the basket containing the order. |
| `symbolName` | string | false | The stock symbol to be traded. |
| `exchange` | string | false | The exchange where the stock is listed. |
| `transactionType` | string | false | Indicates whether the transaction is BUY or SELL. |
| `orderType` | string | false | Specifies the order type (e.g., L - Limit, SL - Stop Limit). |
| `orderValidity` | string | false | Specifies the order's validity duration. |
| `productType` | string | false | Specifies the product type (e.g., CNC - Cash and Carry, CO - Cover Order, BO - Bracket Order, NRML, MIS). |
| `quantity` | string | false | The number of shares or units to be traded. |
| `disclosedQuantity` | string | false | The quantity to be disclosed in the market, which can be equal to or less than the order quantity. |
| `price` | string | false | The execution price for the order. Mandatory for L or SL orders. |
| `priceType` | string | false | Applicable only for BO orders. Valid options: LTP (Last Traded Price) or ATP (Average Traded Price). Default is LTP. |
| `squareOffValue` | string | false | The value used to square off the position automatically. Applicable only for BO orders. |
| `stopLossValue` | string | false | The stop-loss value. Applicable only for BO orders. |
| `valueType` | string | false | The type of value for Stop Loss and Square Off. Valid options: Absolute or Ticks. Default is Absolute. Applicable only for BO orders. |
| `trailingStopLoss` | string | false | Incremental value as a percentage of the price change. The trailing stop loss moves with price increases but stays fixed if the price drops. Applicable only for BO orders. |
| `triggerPrice` | string | false | The price at which the order will be triggered. Applicable for SL orders. |

### Sample Code

**cURL**

```bash
curl -X PUT 'https://tradeapi.samco.in/basket/modifyBasketOrder' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"basketId":"6","basketOrderId":"12","orderType":"L","quantity":"100","price":"1500.00","orderValidity":"DAY","productType":"CNC"}'
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
          "basketId": "6",
          "basketOrderId": "12",
          "orderType": "L",
          "quantity": "100",
          "price": "1500.00",
          "orderValidity": "DAY",
          "productType": "CNC"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/basket/modifyBasketOrder"))
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
    basketId: "6",
    basketOrderId: "12",
    orderType: "L",
    quantity: "100",
    price: "1500.00",
    orderValidity: "DAY",
    productType: "CNC"
  };

  const response = await fetch('https://tradeapi.samco.in/basket/modifyBasketOrder', {
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
  "basketId": "6",
  "basketOrderId": "12",
  "orderType": "L",
  "quantity": "100",
  "price": "1500.00",
  "orderValidity": "DAY",
  "productType": "CNC"
}

r = requests.put('https://tradeapi.samco.in/basket/modifyBasketOrder',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

**200**

```json
{
    "serverTime": "21/08/24 15:08:43",
    "msgId": "e70296a1-f06e-4976-a00e-e5fca43532b9",
    "status": "Success",
    "statusMessage": "Basket Order Data Updated Successfully"
}
```

**400**

```json
{
    "serverTime": "21/08/24 15:30:31",
    "msgId": "7f8bc4f0-8641-40e9-ae7d-abe0b9520a99",
    "status": "Failure",
    "statusMessage": "Invalid basket order id or BasketId "
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | The status of the API request, typically 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message providing more details about the status. |

---

## Delete Basket Order

`DELETE basket/deleteBasketOrder`

The Delete Basket Order API endpoint allows you to remove a specific order from a basket. To use this API, you need to provide the basketId and basketOrderId in the request body. Upon successful deletion of the order, the server responds with a confirmation message indicating the operation was successful, including a timestamp and a unique message ID for tracking purposes.

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `basketId` | Integer | true | The unique identifier for the basket from which an order needs to be deleted. |
| `basketOrderId` | Integer | true | The unique identifier for the order within the basket that needs to be deleted. |

### Sample Code

**cURL**

```bash
curl -X DELETE 'https://tradeapi.samco.in/basket/deleteBasketOrder' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"basketId":6,"basketOrderId":12}'
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
          "basketId": 6,
          "basketOrderId": 12
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/basket/deleteBasketOrder"))
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
    basketId: 6,
    basketOrderId: 12
  };

  const response = await fetch('https://tradeapi.samco.in/basket/deleteBasketOrder', {
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
  "basketId": 6,
  "basketOrderId": 12
}

r = requests.delete('https://tradeapi.samco.in/basket/deleteBasketOrder',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

**200**

```json
{
    "serverTime": "21/08/24 15:43:38",
    "msgId": "8e9f3c6f-ee6a-440b-a1a6-9ef9e46edc58",
    "status": "Success",
    "statusMessage": "Basket Order Deleted Successfully"
}
```

**400**

```json
{
    "serverTime": "21/08/24 15:56:10",
    "msgId": "f4411c2d-20f7-4fa1-90e7-94aeedc527bf",
    "status": "Failure",
    "statusMessage": "The provided BasketIds are invalid: [2]"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | The timestamp indicating when the server processed the request. |
| `msgId` | string | A unique identifier for the message or transaction. Useful for tracking or debugging. |
| `status` | string | Status of the order cancellation request. Can be success, error, or failure. |
| `statusMessage` | string | A descriptive message about the status of the operation. |

---

## Execute Basket Order

`POST basket/executeBasketOrder`

The Execute Basket Order API allows you to execute a basket of orders using the provided basketId. You can specify the execution type as either "allatonce" to execute all orders simultaneously or "chronologically" to execute them in sequence.

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `basketId` | string | true | The unique identifier of the basket that you want to execute. |
| `executionType` | string | true | Specifies how the orders in the basket should be executed. The value can be **allatonce** or **chronologically**. |

### Sample Request Body

```json
requestBody={
  "basketId":"63",
  "executionType":"allatonce"
}
```

> **WARNING** — Live trading endpoint
>
> This sample sends a real request against your trading account. Replace `<SESSION_TOKEN>` and review every field before running — Samco does not provide a sandbox, and any successful call affects live positions and balances.

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/basket/executeBasketOrder' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"basketId":"63","executionType":"allatonce"}'
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
          "basketId": "63",
          "executionType": "allatonce"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/basket/executeBasketOrder"))
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
    basketId: "63",
    executionType: "allatonce"
  };

  const response = await fetch('https://tradeapi.samco.in/basket/executeBasketOrder', {
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
  "basketId": "63",
  "executionType": "allatonce"
}

r = requests.post('https://tradeapi.samco.in/basket/executeBasketOrder',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
    "serverTime": "21/08/24 12:26:46",
    "msgId": "53aab933-0003-48ee-999c-0e68fe1f89b7",
    "status": "Success",
    "statusMessage": "Basket Order Initiated Successfully"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | This indicates the timestamp of when the response was generated by the server. |
| `msgId` | string | A unique identifier for the message or response. It helps in tracking and referencing the specific response. |
| `status` | string | Status of the order cancellation request. Can be success, error, or failure. |
| `statusMessage` | string | A human-readable message confirming that the basket order has been initiated successfully. |

---

## List Basket Order

`GET basket/listBasketOrder`

The "List Basket Order" API retrieves and lists all orders associated with a specific basket based on the basket ID provided by the user.

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `basketId` | string | true | The main order identifier provided as an input which needs to be exited. |

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/basket/listBasketOrder?basketId=6' \
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
        .uri(URI.create("https://tradeapi.samco.in/basket/listBasketOrder?basketId=6"))
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

  const response = await fetch('https://tradeapi.samco.in/basket/listBasketOrder?basketId=6', {
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

r = requests.get('https://tradeapi.samco.in/basket/listBasketOrder?basketId=6',
  headers=headers)

print(r.json())
```

### Sample Responses

**200**

```json
{
    "serverTime": "21/08/24 17:27:48",
    "msgId": "87cb63fb-2a49-48bb-af77-b63bedec477d",
    "status": "Success",
    "statusMessage": "Basket order listed successfully",
    "basketDetails": {
        "deletedContracts": 0,
        "finalMargin": "0.00",
        "maxMargin": "0.00",
        "estimatedCharges": "0.00",
        "notSentToExchange": [],
        "executed": [],
        "pending": [],
        "rejected": []
    }
}
```

**400**

```json
{
    "serverTime": "21/08/24 17:28:08",
    "msgId": "d91f23c6-be83-4cd1-b2ac-82fefed650c8",
    "status": "Failure",
    "statusMessage": "No such Basket found"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | The server's timestamp when the response was generated. |
| `msgId` | string | Unique message ID associated with the response. |
| `status` | string | Indicates the success or failure of the API call. |
| `statusMessage` | string | Provides additional information about the status of the API call. |
| `basketDetails` | string | Contains detailed information about the basket order, including executed, pending, and rejected orders. |
| `deletedContracts` | string | Number of contracts that were deleted from the basket. |
| `finalMargin` | string | Final margin amount after all adjustments. |
| `maxMargin` | string | Maximum margin required for the basket order. |
| `estimatedCharges` | string | Estimated charges for executing the basket order. |
| `notSentToExchange` | string | List of contracts not sent to the exchange for execution. |
| `executed` | string | List of executed orders in the basket. |
| `pending` | string | List of pending orders in the basket. |
| `rejected` | string | List of rejected orders in the basket. |
| `client_id` | string | Client ID associated with the basket order. |
| `basketId` | string | Unique ID of the basket. |
| `basketOrderId` | string | Unique ID of the specific order within the basket. |
| `symName` | string | Symbol name of the security. |
| `symbol` | string | Complete symbol code, including the exchange identifier. |
| `instrumentType` | string | Type of financial instrument (e.g., EQ for equity). |
| `transactionSide` | string | Type of transaction (e.g., BUY or SELL). |
| `orderPrice` | string | Price at which the order is placed. |
| `validity` | string | Validity of the order (e.g., DAY). |
| `orderType` | string | Type of order placed. |
| `quantity` | string | Number of shares or contracts in the order. |
| `productCode` | string | Code representing the type of product (e.g., CNC). |
| `disclosedQuantity` | string | Disclosed quantity of the order. |
| `marginBlocked` | string | Margin amount blocked for the order. |
| `marginRequired` | string | Total margin required for the order. |
| `incrementalMargin` | string | Incremental margin required for the order. |
| `filledQuantity` | string | Quantity of the order that has been filled or executed. |
| `tradingSymbol` | string | Trading symbol of the security. |
| `dispCompanyName` | string | Display name of the company associated with the security. |
| `companyName` | string | Full name of the company associated with the security. |
| `dispExpiryDate` | string | Display expiry date for derivatives, if applicable. |
| `expiry` | string | Expiry date of the contract, if applicable. |
| `instrument` | string | Type of instrument (e.g., FUT, OPT, etc.), if applicable. |
| `dispExc` | string | Display exchange code (e.g., BSE). |
| `dispInstType` | string | Display instrument type (e.g., EQ, FUT, OPT, etc.). |
| `orderStatus` | string | Status of the order (e.g., PENDING, EXECUTED, REJECTED). |
| `stopPrice` | string | Stop price for stop-loss orders, if applicable. |
| `sSLVal` | string | Stop-loss value for the order, if applicable. |
| `sLtpOrAtp` | string | Last traded price or average traded price related to stop-loss, if applicable. |
| `sSLAbsOrTicks` | string | Stop-loss in absolute value or ticks, if applicable. |
| `sSqrOffVal` | string | Square-off value for the order, if applicable. |
| `sSqroffLtpOrAtp` | string | Last traded price or average traded price for square-off, if applicable. |
| `sSqrOffAbsOrTicks` | string | Square-off value in absolute or ticks, if applicable. |
| `sTrailingSL` | string | Trailing stop-loss value for the order, if applicable. |
| `sTrailingSLTicks` | string | Trailing stop-loss value in ticks, if applicable. |
| `rmsOrder` | string | RMS (Risk Management System) order ID for tracking the order. |

---

## Rearrange Basket Order

`POST basket/rearrangeBasketOrder`

The "Rearrange Basket Order" API lets you reorder one or more existing orders inside a basket without modifying their parameters. Pass the `basketId` and either a single `basketOrderId` or an array of `basketOrderId` values listed in the new sequence you want them executed in. The server returns the updated order list reflecting the new arrangement.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `basketId` | string \| number | true | Unique identifier of the basket whose orders are being rearranged. |
| `basketOrderId` | string \| number \| array | true | Either a single `basketOrderId` to reposition, or an array of `basketOrderId` values listed in the desired execution order. |

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/basket/rearrangeBasketOrder' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{
    "basketId": "6",
    "basketOrderId": ["4", "3", "2", "1"]
  }'
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

    String requestBody = "{\n" +
        "  \"basketId\": \"6\",\n" +
        "  \"basketOrderId\": [\"4\", \"3\", \"2\", \"1\"]\n" +
        "}";

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/basket/rearrangeBasketOrder"))
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
    basketId: "6",
    basketOrderId: ["4", "3", "2", "1"],
  };

  const response = await fetch('https://tradeapi.samco.in/basket/rearrangeBasketOrder', {
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

payload = {
  "basketId": "6",
  "basketOrderId": ["4", "3", "2", "1"],
}

r = requests.post('https://tradeapi.samco.in/basket/rearrangeBasketOrder',
  headers=headers, json=payload)

print(r.json())
```

### Sample Responses

**200**

```json
{
    "serverTime": "21/08/24 17:30:14",
    "msgId": "a4b7d930-1c1e-4ad1-9a85-dc09a2c2f8e3",
    "status": "Success",
    "statusMessage": "Basket orders rearranged successfully",
    "rearrangeOrderList": {
        "basketId": 6,
        "orders": [
            { "basketOrderId": 4, "sequence": 1 },
            { "basketOrderId": 3, "sequence": 2 },
            { "basketOrderId": 2, "sequence": 3 },
            { "basketOrderId": 1, "sequence": 4 }
        ]
    }
}
```

**400**

```json
{
    "serverTime": "21/08/24 17:30:32",
    "msgId": "f01e1c44-9c34-4b35-89ac-fa9c54b7ab21",
    "status": "Failure",
    "statusMessage": "No such Basket found"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | The server's timestamp when the response was generated. |
| `msgId` | string | Unique message ID associated with the response. |
| `status` | string | Indicates the success or failure of the API call. |
| `statusMessage` | string | Provides additional information about the status of the API call. |
| `rearrangeOrderList` | object | Updated ordering of the basket's orders, reflecting the new sequence. |
| `basketId` | number | Identifier of the basket whose orders were rearranged. |
| `orders` | array | Array of orders in the basket, each with its `basketOrderId` and new `sequence` position. |

---

## Basket Margin Calculator

`POST basket/spanCalculator`

This API calculates the margin requirements for a basket of financial instruments, including futures and options, by evaluating potential risks across various market scenarios. It determines the minimum margin needed to cover potential losses, ensuring sufficient margin is maintained to protect against significant market fluctuations.

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `basketId` | string | true | This is the unique identifier for the basket. The span calculator will use this ID to retrieve details about the basket and perform the necessary calculations. |

### Sample Request Body

```json
requestBody={
    "basketId" :"63"
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/basket/spanCalculator' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"basketId":"63"}'
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
          "basketId": "63"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/basket/spanCalculator"))
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
    basketId: "63"
  };

  const response = await fetch('https://tradeapi.samco.in/basket/spanCalculator', {
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
  "basketId": "63"
}

r = requests.post('https://tradeapi.samco.in/basket/spanCalculator',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

**200**

```json
{
    "serverTime": "20/08/24 19:17:32",
    "msgId": "493edbec-ee44-4022-a7d2-b2431eae8c28",
    "status": "Success",
    "statusMessage": "Peak Margin and Final Margin Calculated Successfully",
    "spanDetails": {
        "maxMargin": 11.56,
        "finalMargin": 23.1
    }
}
```

**400**

```json
{
    "serverTime": "20/08/24 19:27:51",
    "status": "Failure",
    "statusMessage": "No such Basket found"
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | This indicates the timestamp of when the response was generated by the server. |
| `msgId` | string | A unique identifier for the message or response. It helps in tracking and referencing the specific response. |
| `status` | string | Status of the order cancellation request. Can be success, error or failure. |
| `statusMessage` | string | Provides a human-readable description of the status. |
| `spanDetails` | object | This is an object containing detailed information about the margins. |
| `maxMargin` | string | The maximum margin required for the basket order. |
| `finalMargin` | string | The final margin amount required after considering all adjustments. |
