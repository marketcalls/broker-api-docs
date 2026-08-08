# Candle Data

Intraday and historical OHLC candles for scrips and indices.

## Intraday candle data

`GET /intraday/candleData`

Gets the Intraday candle data such as Open, high, low, close and volume within specific time period per min for a specific symbol.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | String | False | Name of the exchange. Valid exchange values (BSE/ NSE/ NFO/ MCX/ CDS). If the user does not provide an exchange name, by default considered as NSE. For trading with BSE, NFO, CDS and MCX, exchange is mandatory. |
| `symbolName` | String | True | Symbol name of the scrip. |
| `fromDate` | String | True | From date in yyyy-MM-dd hh:mm:ss. |
| `toDate` | String | False | To date in yyyy-MM-dd hh:mm:ss. |
| `interval` | String | False | Interval of data. By default, interval is considered as 1 min. |

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/intraday/candleData?symbolName=INFY&fromDate=2019-11-11%2010%3A00%3A00' \
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
        .uri(URI.create("https://tradeapi.samco.in/intraday/candleData?symbolName=INFY&fromDate=2019-11-11%2010%3A00%3A00"))
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

  const response = await fetch('https://tradeapi.samco.in/intraday/candleData?symbolName=INFY&fromDate=2019-11-11%2010%3A00%3A00', {
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

r = requests.get('https://tradeapi.samco.in/intraday/candleData?symbolName=INFY&fromDate=2019-11-11%2010%3A00%3A00',
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
  "intradayCandleData": [
    {
      "dateTime": "2019-11-11 10:01:00",
      "open": "689.9",
      "high": "694.0",
      "low": "682.75",
      "close": "688.0",
      "volume": "600344"
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
| `status` | String | Response status. Can be Success or Failure |
| `statusMessage` | String | Status message |
| `intradayCandleData` | Array | Get list of Intraday Candle Data. |
| `dateTime` | String | Date for which Candle Data is shown |
| `open` | String | Opening price of a market snapshot |
| `high` | String | High value of market snapshot |
| `low` | String | Low value of market snapshot |
| `close` | String | Close value of market snapshot |
| `volume` | String | Limit amount of a security traded on the specific day |

---

## Index IntraDay candle data

`GET /intraday/indexCandleData`

Gets the Index intraday candle data such as Open, high, low, close and volume within specific time period per min for a specific index.

### Supported Index names:

| **BSE CG** | **SENSEX** | **BSE CD** | **NIFTY50 PR 1x INV** |
| --- | --- | --- | --- |
| **BSE IT** | **METAL** | **OILGAS** | **NIFTY50 PR 2x LEV** |
| **BSEIPO** | **GREENX** | **POWER** | **NIFTY50 TR 1x INV** |
| **CARBON** | **BASMTR** | **CDGS** | **NIFTY50 TR 2x LEV** |
| **BSEFMC** | **BSE HC** | **ALLCAP** | **NIFTY50 TR 2x LEV** |
| **REALTY** | **SMEIPO** | **DOL30** | **NIFTY Mid LIQ 15** |
| **LRGCAP** | **MIDSEL** | **SMLSEL** | **NIFTY100 LIQ 15** |
| **SNXT50** | **SNSX50** | **NIFTY 50** | **NIFTY Quality 30** |
| **NIFTY BANK** | **NIFTY NEXT 50** | **DOL100** | **NIFTY MIDCAP 50** |
| **NIFTY 100** | **NIFTY 200** | **NIFTY 500** | **NIFTY FIN SERVICE** |
| **NIFTY AUTO** | **NIFTY FMCG** | **NIFTY IT** | **NIFTY COMMODITIES** |
| **NIFTY MEDIA** | **NIFTY METAL** | **NIFTY PHARMA** | **NIFTY CONSUMPTION** |
| **NIFTY PSU BANK** | **NIFTY PVT BANK** | **NIFTY REALTY** | **NIFTY GROWSECT 15** |
| **NIFTY CPSE** | **NIFTY ENERGY** | **NIFTY INFRA** | **NIFTY DIV OPPS 50** |
| **NIFTY MNC** | **NIFTY PSE** | **NIFTY SERV SECTOR** | **NIFTY MID100 FREE** |
| **DOL200** | **TECK** | **BSEPSU** | **NIFTY SML100 FREE** |
| **AUTO** | **BANKEX** | **INDIA VIX** | **NIFTY50 VALUE 20** |
| **NIFTY MID SELECT** |  |  |  |

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `indexName` | string | true | Index name of the scrip. |
| `fromDate` | string | true | From date in `yyyy-MM-dd hh:mm:ss` format. |
| `toDate` | string | false | To date in `yyyy-MM-dd hh:mm:ss` format. |
| `interval` | string | false | Interval of data; default is 1 minute. |

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/intraday/indexCandleData?indexName=SENSEX&fromDate=2020-03-11%2010%3A00%3A00' \
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
        .uri(URI.create("https://tradeapi.samco.in/intraday/indexCandleData?indexName=SENSEX&fromDate=2020-03-11%2010%3A00%3A00"))
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

  const response = await fetch('https://tradeapi.samco.in/intraday/indexCandleData?indexName=SENSEX&fromDate=2020-03-11%2010%3A00%3A00', {
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

r = requests.get('https://tradeapi.samco.in/intraday/indexCandleData?indexName=SENSEX&fromDate=2020-03-11%2010%3A00%3A00',
  headers=headers)

print(r.json())
```

### Sample response

> 200 Response

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "status": "Success",
  "statusMessage": "Index details retrieved successfully.",
  "indexIntraDayCandleData": [
    {
      "dateTime": "2019-11-11 10:01:00",
      "open": "689.9",
      "high": "694.0",
      "low": "682.75",
      "close": "688.0",
      "volume": "600344"
    }
  ]
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | Unique identifier for every request. |
| `status` | string | Response status; can be success or failure. |
| `statusMessage` | string | Status message of the Index request. |
| `indexIntraDayCandleData` | [object] | List of Index IntraDay Candle Data. |
| `dateTime` | string | Date for which Candle Data is shown. |
| `open` | string | Opening price of a market snapshot. |
| `high` | string | High value of market snapshot. |
| `low` | string | Low value of market snapshot. |
| `close` | string | Close value of market snapshot. |
| `volume` | string | Volume of security traded on the specific day. |

---

## Historical candle data

`GET /history/candleData`

Gets the historical candle data such as Open, high, low, close, last traded price and volume within specific dates for a specific symbol. From date is mandatory. End date is optional and defaults to yesterday.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | false | Name of the exchange. Valid values are (BSE/ NSE/ NFO/ MCX/ CDS). Default is NSE if not provided. |
| `symbolName` | string | true | Symbol name of the scrip. |
| `fromDate` | string | true | Start date in `yyyy-MM-dd` format. |
| `toDate` | string | false | End date in `yyyy-MM-dd` format. If not provided, data is fetched only for the `fromDate`. |

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/history/candleData?symbolName=INFY&fromDate=2019-10-11' \
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
        .uri(URI.create("https://tradeapi.samco.in/history/candleData?symbolName=INFY&fromDate=2019-10-11"))
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

  const response = await fetch('https://tradeapi.samco.in/history/candleData?symbolName=INFY&fromDate=2019-10-11', {
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

r = requests.get('https://tradeapi.samco.in/history/candleData?symbolName=INFY&fromDate=2019-10-11',
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
  "historicalCandleData": [
    {
      "date": "2019-11-01",
      "open": "689.9",
      "high": "694.0",
      "low": "682.75",
      "close": "688.0",
      "ltp": "688.0",
      "volume": "600344"
    }
  ]
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | Unique identifier for the request. Quote this to the support team if needed. |
| `status` | string | Response status. Can be Success or Failure. |
| `statusMessage` | string | Status message of the response. |
| `historicalCandleData` | [object] | List of historical candle data. |
| `date` | string | Date for which CandleData is shown. |
| `open` | string | Opening price of the market snapshot. |
| `high` | string | Highest value of the market snapshot. |
| `low` | string | Lowest value of the market snapshot. |
| `close` | string | Closing price of the market snapshot. |
| `ltp` | string | Last traded price. |
| `volume` | string | Amount of security traded on the specific day. |

---

## Index Historical CandleData

`GET /history/indexCandleData`

Gets the Index historical candle data such as Open, high, low, close, last traded price and volume within specific dates for a specific index. From date is mandatory. End date is optional and defaults to Today.

### Supported Index names:

| **BSE CG** | **SENSEX** | **BSE CD** | **NIFTY50 PR 1x INV** |
| --- | --- | --- | --- |
| **BSE IT** | **METAL** | **OILGAS** | **NIFTY50 PR 2x LEV** |
| **BSEIPO** | **GREENX** | **POWER** | **NIFTY50 TR 1x INV** |
| **CARBON** | **BASMTR** | **CDGS** | **NIFTY50 TR 2x LEV** |
| **BSEFMC** | **BSE HC** | **ALLCAP** | **NIFTY50 TR 2x LEV** |
| **REALTY** | **SMEIPO** | **DOL30** | **NIFTY Mid LIQ 15** |
| **LRGCAP** | **MIDSEL** | **SMLSEL** | **NIFTY100 LIQ 15** |
| **SNXT50** | **SNSX50** | **NIFTY 50** | **NIFTY Quality 30** |
| **NIFTY BANK** | **NIFTY NEXT 50** | **DOL100** | **NIFTY MIDCAP 50** |
| **NIFTY 100** | **NIFTY 200** | **NIFTY 500** | **NIFTY FIN SERVICE** |
| **NIFTY AUTO** | **NIFTY FMCG** | **NIFTY IT** | **NIFTY COMMODITIES** |
| **NIFTY MEDIA** | **NIFTY METAL** | **NIFTY PHARMA** | **NIFTY CONSUMPTION** |
| **NIFTY PSU BANK** | **NIFTY PVT BANK** | **NIFTY REALTY** | **NIFTY GROWSECT 15** |
| **NIFTY CPSE** | **NIFTY ENERGY** | **NIFTY INFRA** | **NIFTY DIV OPPS 50** |
| **NIFTY MNC** | **NIFTY PSE** | **NIFTY SERV SECTOR** | **NIFTY MID100 FREE** |
| **DOL200** | **TECK** | **BSEPSU** | **NIFTY SML100 FREE** |
| **AUTO** | **BANKEX** | **INDIA VIX** | **NIFTY50 VALUE 20** |
| **NIFTY MID SELECT** |  |  |  |

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `indexName` | string | true | Index name of the scrip. |
| `fromDate` | string | true | From date in yyyy-MM-dd. |
| `toDate` | string | false | To date in yyyy-MM-dd. |

### Code Sample

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/history/indexCandleData?indexName=SENSEX&fromDate=2020-03-09' \
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
        .uri(URI.create("https://tradeapi.samco.in/history/indexCandleData?indexName=SENSEX&fromDate=2020-03-09"))
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

  const response = await fetch('https://tradeapi.samco.in/history/indexCandleData?indexName=SENSEX&fromDate=2020-03-09', {
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

r = requests.get('https://tradeapi.samco.in/history/indexCandleData?indexName=SENSEX&fromDate=2020-03-09',
  headers=headers)

print(r.json())
```

### Sample Response

```json
{
  "serverTime": "12/12/19 16:20:11",
  "msgId": "786cdd94-2fc9-4c38-8f14-672ec64dd032",
  "status": "Success",
  "statusMessage": "Index details retrieved successfully.",
  "indexCandleData": [
    {
      "date": "2019-11-01",
      "open": "689.9",
      "high": "694.0",
      "low": "682.75",
      "close": "688.0",
      "ltp": "688.0",
      "volume": "600344"
    }
  ]
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | Unique identifier for the request. Please quote this to the support team if needed. |
| `status` | string | Response status. Can be success or failure. |
| `statusMessage` | string | Status message of the Index request. |
| `indexCandleData` | [object] | List of Index data. |
| `date` | string | Date for which CandleData is shown. |
| `open` | string | Opening price of the market snapshot. |
| `high` | string | Highest value of the market snapshot. |
| `low` | string | Lowest value of the market snapshot. |
| `close` | string | Closing price of the market snapshot. |
| `ltp` | string | Last traded price. |
| `volume` | string | Limit amount of a security traded on the specific day. |
