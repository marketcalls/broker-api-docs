# Account and Limits

Available margin, cash balance, and user-defined index baskets.

## User Limits

`GET /limit/getLimits`

Gets the user cash balances, available margin for trading in equity and commodity segments.

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/limit/getLimits' \
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
        .uri(URI.create("https://tradeapi.samco.in/limit/getLimits"))
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

  const response = await fetch('https://tradeapi.samco.in/limit/getLimits', {
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

r = requests.get('https://tradeapi.samco.in/limit/getLimits',
  headers=headers)

print(r.json())
```

### Sample responses

```json
{
    "serverTime": "10/04/24 13:29:07",
    "msgId": "77bb4c9b-17fc-4465-8e30-02e80eaff78c",
    "status": "Success",
    "statusMessage": "User Limit details retrieved successfully",
    "equityLimit": {
        "grossAvailableMargin": "0.00",
        "payInToday": "0",
        "notionalCash": "0",
        "marginUsed": "0",
        "netAvailableMargin": "0.00"
    },
    "commodityLimit": {
        "grossAvailableMargin": "0.00",
        "payInToday": "0",
        "notionalCash": "0",
        "marginUsed": "0",
        "netAvailableMargin": "0.00"
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
| `grossAvailableMargin` | string | Total amount of margins or balances available for trading. Opening balance for the current day. |
| `payInToday` | string | Current day deposited amount. |
| `notionalCash` | string | Additional limit that may or may not be given by RMS for trading. |
| `collateralMarginAgainstShares` | string | Margin against shares offered by SAMCO to their clients for trading in stocks and shares. |
| `marginUsed` | string | The amount deducted from the opening balance for trading on the current day, and the amount blocked for creating a position when the user places an order. |
| `netAvailableMargin` | string | Actual margin available with the user for trading after making all necessary adjustments. |

---

## Personal Index

`GET /indexData`

The Personal Index API provides detailed insights into a user's trading performance by aggregating the overall profit and loss of all executed trades. This API delivers comprehensive data on an individual's personal index, allowing users to monitor and analyze their trading activities efficiently. It is an essential tool for evaluating performance metrics and managing investment strategies based on historical trade outcomes.

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/indexData' \
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
        .uri(URI.create("https://tradeapi.samco.in/indexData"))
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

  const response = await fetch('https://tradeapi.samco.in/indexData', {
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

r = requests.get('https://tradeapi.samco.in/indexData',
  headers=headers)

print(r.json())
```

### Sample Response

```json
{
  "serverTime": "04/04/24 11:22:12",
  "msgId": "2164268d-d38b-490e-bbb2-d3cedda3a907",
  "status": "Success",
  "statusMessage": "Index Data retrieved successfully",
  "indexData": {
    "indexName": "MXXXXXXD IXXXx",
    "networth": "209.52",
    "indexData": {
      "index": "4.04",
      "indexChange": "0.04",
      "indexChangePercentage": "1.04",
      "latestTime": "2024-04-04 11:21:00",
      "networthChange": "2.15",
      "networthChangePercentage": "1.04",
      "fundReceipt": "0.00"
    }
  }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | The date and time when the server generated the response. |
| `msgId` | string | A unique identifier for the API response message. Useful for tracking or debugging. |
| `status` | string | The status of the API response. Possible values: 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `indexDataDetails` | Object | Detailed information about the user's personal index. |
| `indexName` | string | The name of the personal index. |
| `networth` | string | The current net worth associated with the personal index. |
| `indexData` | Object | Specific details about the index's performance. |
| `Index` | string | The current value of the index. |
| `IndexChange` | string | The absolute change in the index value compared to the previous update. |
| `IndexChangePercentage` | string | The percentage change in the index value compared to the previous update. |
| `latestTime` | string | The timestamp indicating the most recent update to the index data. |
| `networthChange` | string | The variance between yesterday's and today's net worth values. |
| `networthChangePercentage` | string | The percentage change in net worth value from yesterday to today. |
| `fundReceipt` | string | Today's payment amount: the sum received or transferred to fund. |
