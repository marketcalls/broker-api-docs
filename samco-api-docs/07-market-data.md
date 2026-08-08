# Market Data

Quotes, market depth, option and future chains, symbol search, and the contract analyser.

## Market Depth

`POST /marketDepth`

The Market Depth API provides real-time data on the market depth for a given trading symbol on a specific exchange. This includes details about the current bid and ask prices, their quantities, and other relevant market data. It is useful for traders and investors to understand the supply and demand dynamics of a stock and make informed trading decisions.

### Parameter

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | false | Name of the exchange. Valid values: BSE, NSE, NFO, BFO, MCX, CDS, MFO. Default is NSE if not provided. For BSE, NFO, CDS, and MCX, the exchange is mandatory. |
| `symbolName` | string | true | Symbol name of the scrip. For Equity, enter the SymbolName of the scrip. For Derivatives, enter the TradingSymbol of the scrip. |

### Sample Request Body

```json

requestBody={ 
  "exchange" : "BFO",
  "symbolName" : "BANKEX2450656000CE"
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/marketDepth' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"exchange":"BFO","symbolName":"BANKEX2450656000CE"}'
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
          "exchange": "BFO",
          "symbolName": "BANKEX2450656000CE"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/marketDepth"))
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
    exchange: "BFO",
    symbolName: "BANKEX2450656000CE"
  };

  const response = await fetch('https://tradeapi.samco.in/marketDepth', {
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
  "exchange": "BFO",
  "symbolName": "BANKEX2450656000CE"
}

r = requests.post('https://tradeapi.samco.in/marketDepth',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Response

**200**

```json
{
    "serverTime": "20/08/24 13:41:54",
    "msgId": "f494c1cb-ba67-4591-b29e-9a27f92e5204",
    "status": "Success",
    "statusMessage": "Market depth data retrieved successfully",
    "MarketDepthDetails": {
        "marketDepth": {
            "tradingSymbol": "NIFTY2482224500PE",
            "vega": "5.05",
            "theta": "-15.53",
            "gamma": "0.0010",
            "symbol": "36759_NFO",
            "tBuyQty": "774925",
            "iv": "13.80",
            "tSellQty": "985500",
            "bestFiveAsk": [
                {
                    "askNumber": "8",
                    "askSize": "1775",
                    "askPrice": "27.05"
                },
                {
                    "askNumber": "19",
                    "askSize": "4350",
                    "askPrice": "27.10"
                },
                {
                    "askNumber": "19",
                    "askSize": "3650",
                    "askPrice": "27.15"
                },
                {
                    "askNumber": "20",
                    "askSize": "5025",
                    "askPrice": "27.20"
                },
                {
                    "askNumber": "11",
                    "askSize": "1950",
                    "askPrice": "27.25"
                }
            ],
            "bestFiveBid": [
                {
                    "bidSize": "1400",
                    "bidNumber": "4",
                    "bidPrice": "27.00"
                },
                {
                    "bidSize": "3850",
                    "bidNumber": "13",
                    "bidPrice": "26.95"
                },
                {
                    "bidSize": "8975",
                    "bidNumber": "22",
                    "bidPrice": "26.90"
                },
                {
                    "bidSize": "5450",
                    "bidNumber": "18",
                    "bidPrice": "26.85"
                },
                {
                    "bidSize": "2800",
                    "bidNumber": "9",
                    "bidPrice": "26.80"
                }
            ],
            "atmIV": "11.70",
            "delta": "-0.19",
            "exc": "NFO"
        }
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
| `serverTime` | string | The timestamp of when the response was generated, indicating the server's current time. |
| `msgId` | string | A unique identifier for the request, useful for tracking and debugging. |
| `status` | string | The status of the API response. Possible values: 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message providing additional details about the status of the request. |
| `MarketDepthDetails` | Object | Contains the market depth information. |
| `tradingSymbol` | string | The identifier for the financial instrument or contract. |
| `vega` | string | Measures the sensitivity of the F&O’s price to changes in the volatility of the underlying asset. |
| `theta` | string | Measures the rate at which the F&O’s price decreases as it approaches expiration. |
| `gamma` | string | Measures the rate of change of delta with respect to changes in the underlying asset's price. |
| `symbol` | string | A unique code for the instrument on the exchange. |
| `tBuyQty` | string | The total quantity available for buying. |
| `iv` | string | Implied volatility of the F&O. |
| `tSellQty` | string | The total quantity available for selling. |
| `bestFiveAsk` | Object | An array listing the top five ask prices (prices at which sellers are willing to sell). |
| `askNumber` | string | The order number for the ask price. |
| `askSize` | string | The quantity available at the ask price. |
| `askPrice` | string | The price at which sellers are willing to sell. |
| `bestFiveBid` | Object | An array listing the top five bid prices (prices at which buyers are willing to buy). |
| `bidSize` | string | The quantity available at the bid price. |
| `bidNumber` | string | The order number for the bid price. |
| `bidPrice` | string | The price at which buyers are willing to buy. |
| `atmIV` | Object | The implied volatility of the at-the-money F&O. |
| `delta` | string | Measures the sensitivity of the F&O’s price to changes in the price of the underlying asset. |
| `exc` | string | The exchange code where the instrument is traded. |

---

## Contract Analyser

`POST /contractsAnalyser`

The Contact Analyzer API serves as an indispensable tool for traders and financial analysts seeking to evaluate and optimize intricate trading strategies involving multiple contracts, particularly in the realm of options trading. By delivering a comprehensive and detailed report that covers both performance metrics and risk assessments, the API enables users to gain profound insights into the nuances of their strategies. It provides critical data such as breakeven points, maximum profit, maximum loss, strategy Greeks, risk-reward ratio, estimated margins, and payoff points, accompanied by graphs. This empowers users to make well-informed, data-driven decisions with confidence. By offering an in-depth breakdown of every critical aspect of the strategy, including potential profits, losses, risk parameters, and various payoff scenarios, the Contact Analyzer API becomes an essential resource for those striving to enhance their decision-making processes in the complex and dynamic landscape of financial markets.

### Parameter

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | true | Specifies the exchange where the contracts are traded. Valid values: NFO, BFO. |
| `contracts` | object | true | A list of contract details being analyzed. |
| `tradingSymbol` | string | true | The symbol representing the contract. |
| `transactionType` | string | true | The type of transaction, either "Buy" or "Sell." |
| `price` | string | true | The price at which the contract is being traded. |
| `lot` | string | true | The number of lots associated with the contract. |
| `targetDate` | string | true | The date for which the analysis is being performed. |

### Sample Request Body

```json

requestBody={
    "exchange": "NFO",
    "contracts": [
        {
            "tradingSymbol": "HDFCBANK24OCT1510CE",
            "transactionType": "Buy",
            "price": "152.75",
            "lot": "2"
        },
        {
            "tradingSymbol": "HDFCBANK24SEP1510CE",
            "transactionType": "SELL",
            "price": "1342.75",
            "lot": "2"
        }
    ],
    "targetDate": "2024-10-11"
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/contractsAnalyser' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"exchange":"NFO","contracts":[{"tradingSymbol":"HDFCBANK24OCT1510CE","transactionType":"Buy","price":"152.75","lot":"2"},{"tradingSymbol":"HDFCBANK24SEP1510CE","transactionType":"SELL","price":"1342.75","lot":"2"}],"targetDate":"2024-10-11"}'
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
          "contracts": [
            {
              "tradingSymbol": "HDFCBANK24OCT1510CE",
              "transactionType": "Buy",
              "price": "152.75",
              "lot": "2"
            },
            {
              "tradingSymbol": "HDFCBANK24SEP1510CE",
              "transactionType": "SELL",
              "price": "1342.75",
              "lot": "2"
            }
          ],
          "targetDate": "2024-10-11"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/contractsAnalyser"))
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
    contracts: [
      {
        tradingSymbol: "HDFCBANK24OCT1510CE",
        transactionType: "Buy",
        price: "152.75",
        lot: "2"
      },
      {
        tradingSymbol: "HDFCBANK24SEP1510CE",
        transactionType: "SELL",
        price: "1342.75",
        lot: "2"
      }
    ],
    targetDate: "2024-10-11"
  };

  const response = await fetch('https://tradeapi.samco.in/contractsAnalyser', {
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
  "contracts": [
    {
      "tradingSymbol": "HDFCBANK24OCT1510CE",
      "transactionType": "Buy",
      "price": "152.75",
      "lot": "2"
    },
    {
      "tradingSymbol": "HDFCBANK24SEP1510CE",
      "transactionType": "SELL",
      "price": "1342.75",
      "lot": "2"
    }
  ],
  "targetDate": "2024-10-11"
}

r = requests.post('https://tradeapi.samco.in/contractsAnalyser',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Response

**200**

```json
{
    "serverTime": "09/09/24 12:16:08",
    "msgId": "cc1569f6-e666-4759-8590-4fefa538ce4e",
    "status": "Success",
    "statusMessage": "Contracts analysis report is successfully generated.",
    "analyseReport": {
        "strategyInfo": {
            "symbol": "1333_NSE",
            "symbolName": "HDFCBANK",
            "change": "2.45",
            "changePer": "0.15",
            "exchange": "NSE",
            "noOfStrategyLegs": 2,
            "strategyLegs": [
                {
                    "tradingSymbol": "HDFCBANK24OCT1510CE",
                    "symName": "HDFCBANK",
                    "symbol": "107396_NFO",
                    "optionType": "CE",
                    "instrument": "OPTSTK",
                    "expiry": "31 Oct 24",
                    "lotSize": "550",
                    "quantity": "1100",
                    "lTP": "165.55",
                    "avgPrc": "152.75",
                    "askPrice": "0.00",
                    "bidPrice": "0.00",
                    "openInterest": "0",
                    "strategyLegType": "LONG CALL",
                    "strategyExpiryType": "Next expiry",
                    "upperCktLimit": "16555.00",
                    "lowerCktLimit": "0.05",
                    "tickSize": "0.05"
                },
                {
                    "tradingSymbol": "HDFCBANK24SEP1510CE",
                    "symName": "HDFCBANK",
                    "symbol": "78225_NFO",
                    "optionType": "CE",
                    "instrument": "OPTSTK",
                    "expiry": "26 Sep 24",
                    "lotSize": "550",
                    "quantity": "1100",
                    "lTP": "148.8",
                    "avgPrc": "1342.75",
                    "askPrice": "0.00",
                    "bidPrice": "0.00",
                    "openInterest": "0",
                    "strategyLegType": "SHORT CALL",
                    "strategyExpiryType": "Current expiry",
                    "upperCktLimit": "14880.00",
                    "lowerCktLimit": "0.05",
                    "tickSize": "0.05"
                }
            ],
            "breakeven1": "NA",
            "breakeven2": "0.00",
            "maxProfit": "13,49,308",
            "sMaxProfit": "13,49,308(1265%)",
            "maxLoss": "13,10,536",
            "sMaxLoss": "13,10,536(1229%)",
            "sNetTheta": "0.000000",
            "sNetDelta": "0.000000",
            "sNetGamma": "0.000000",
            "sNetVega": "0.000000",
            "sRRRatio": "1: 1.03",
            "estimatedMargin": "1,06,632.57",
            "targetExpiryDate": "26 Sep 24",
            "lotSize": "550",
            "plDataByPricePointPayoffChart": [
                {
                    "pricePoint": 1380,
                    "pricePointProfitLoss": 1310536,
                    "pricePointProfitLossOnUserExpiry": 1309155
                },
                {
                    "pricePoint": 1381,
                    "pricePointProfitLoss": 1310582,
                    "pricePointProfitLossOnUserExpiry": 1309161
                },
                {
                    "pricePoint": 1382,
                    "pricePointProfitLoss": 1310630,
                    "pricePointProfitLossOnUserExpiry": 1309169
                },
                {
                    "pricePoint": 1382,
                    "pricePointProfitLoss": 1310678,
                    "pricePointProfitLossOnUserExpiry": 1309176
                }
            ]
        }
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
| `serverTime` | string | The timestamp of when the response was generated, indicating the server's current time. |
| `msgId` | string | A unique identifier for the request, useful for tracking and debugging. |
| `status` | string | The status of the API response. It can be either 'Success', 'Error', or 'Failure'. |
| `statusMessage` | string | A message providing additional details about the status of the request. |
| `analyseReport` | Object | The core of the response containing the detailed analysis of the strategy. |
| `strategyInfo` | Object | A summary of the strategy being analyzed. |
| `symbol` | string | An internal symbol code used by the system to represent the strategy. |
| `symbolName` | string | The name of the underlying asset in the strategy. |
| `change` | string | The change in price for the underlying asset. |
| `changePer` | string | The percentage change in price for the underlying asset. |
| `exchange` | string | The exchange where the asset is listed. |
| `noOfStrategyLegs` | string | The number of legs or positions in the strategy. A strategy can involve multiple contracts (legs). |
| `strategyLegs` | array | Details of each leg in the strategy. |
| `tradingSymbol` | string | The symbol of the contract. |
| `symName` | string | The underlying asset's name. |
| `symbol` | string | The internal symbol code used by the system. |
| `optionType` | string | The type of option (e.g., Call (CE) or Put (PE)). |
| `instrument` | string | The type of financial instrument. |
| `expiry` | string | The expiry date of the contract. |
| `lotSize` | string | The number of units in a lot. |
| `quantity` | string | Total quantity involved in the leg (lot size \* lots). |
| `lTP` | string | The last traded price of the contract. |
| `avgPrc` | string | The average price at which the contract was executed. |
| `askPrice` | string | The current ask price. |
| `bidPrice` | string | The current bid price. |
| `openInterest` | string | The current open interest of the contract. |
| `strategyLegType` | string | The type of leg (e.g., "LONG CALL" or "SHORT CALL"). |
| `strategyExpiryType` | string | Indicates whether the expiry is current or next. |
| `upperCktLimit` | string | The upper circuit limit of the contract. |
| `lowerCktLimit` | string | The lower circuit limit of the contract. |
| `tickSize` | string | The minimum price movement of the contract. |
| `breakeven1` | string | The first breakeven point for the strategy, representing the price level where neither profit nor loss is made. |
| `breakeven2` | string | The second breakeven point, set at "0.00" here. |
| `maxProfit` | string | The maximum profit that can be achieved with the strategy. |
| `sMaxProfit` | string | The maximum profit shown with the percentage of profit relative to the investment. |
| `maxLoss` | string | The maximum potential loss with the strategy. |
| `sMaxLoss` | string | The maximum loss shown with the percentage of loss relative to the investment. |
| `sNetTheta` | string | The net Theta of the strategy, representing the time decay of options. |
| `sNetDelta` | string | The net Delta of the strategy, representing the price sensitivity to the underlying asset. |
| `sNetGamma` | string | The net Gamma of the strategy, representing the rate of change of Delta. |
| `sNetVega` | string | The net Vega of the strategy, representing the sensitivity to volatility. |
| `sRRRatio` | string | The risk-reward ratio of the strategy. |
| `estimatedMargin` | string | The estimated margin required to execute the strategy. |
| `targetExpiryDate` | string | The target expiry date for the strategy. |
| `lotSize` | string | The lot size used in the strategy. |
| `plDataByPricePointPayoffChart` | array | An array of objects representing the profit/loss at different price points. |
| `pricePoint` | string | The price point of the underlying asset. |
| `pricePointProfitLoss` | string | The profit or loss at that price point. |
| `pricePointProfitLossOnUserExpiry` | string | The profit or loss at that price point on the user-defined expiry date. |

---

## Search Equity scrips

`GET /eqDervSearch/search`

This API is used to search equity, derivatives and commodity scrips based on user provided search symbol and exchange name.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | false | Name of the exchange. Valid exchange values (BSE/ NSE/ NFO/ MCX/ CDS). If the user does not provide an exchange name, it is considered as NSE by default. For trading with BSE, NFO, CDS, and MCX, the exchange is mandatory. |
| `searchSymbolName` | string | true | Trading Symbol of the scrip to be searched. |

### Sample Request Body

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/eqDervSearch/search?exchange=BFO&searchSymbolName=ZYDUSLIFE24MAYFUT' \
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
        .uri(URI.create("https://tradeapi.samco.in/eqDervSearch/search?exchange=BFO&searchSymbolName=ZYDUSLIFE24MAYFUT"))
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

  const response = await fetch('https://tradeapi.samco.in/eqDervSearch/search?exchange=BFO&searchSymbolName=ZYDUSLIFE24MAYFUT', {
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

r = requests.get('https://tradeapi.samco.in/eqDervSearch/search?exchange=BFO&searchSymbolName=ZYDUSLIFE24MAYFUT',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
    "serverTime": "05/04/24 16:44:12",
    "msgId": "c0c3fc7c-9000-4d74-8069-6f67009e7e63",
    "status": "Success",
    "statusMessage": "Request successful",
    "searchResults": [
        {
            "exchange": "BFO",
            "tradingSymbol": "ZYDUSLIFE24MAYFUT",
            "quantityInLots": "900",
            "instrument": "FUTSTK"
        }
    ]
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `msgId` | string | This is a unique identifier for every request into the system. Please quote this identifier to the support team if you face issues with the API request. |
| `status` | string | The status of the API response. It can be either 'Success' or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `searchResults` | [object] | Scrips details available for the provided search text. |
| `exchange` | string | Name of the exchange. Valid exchange values (BSE/ NSE/ NFO/ MCX/ CDS). If the user does not provide an exchange name, it is considered as NSE by default. For trading with BSE, NFO, CDS, and MCX, the exchange is mandatory. |
| `scripDescription` | string | Scrip description. |
| `tradingSymbol` | string | Trading Symbol of the scrip. |
| `isin` | string | The standard ISIN representing stocks uniquely at an international level. It is the same for every exchange. |
| `bodLotQuantity` | string | None. |
| `tickSize` | string | The value of a single price tick. Default value is 0.05. |
| `instrument` | string | Instrument Name. |
| `quantityInLots` | string | Lot size of the symbol to be traded. At the time of placing an order, the quantity should be in multiples of Broadlot Qty only. |

---

## Option Chain

`GET /option/optionChain`

This API is used to search OptionChain for equity, derivatives and commodity scrips based on user provided search symbol and exchange name.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | false | Name of the exchange. Valid exchange values (NFO/ BFO/ MCX/ CDS/ MFO). If the user does not provide an exchange name, it is considered as NFO by default. For trading with BFO, MFO, CDS, and MCX, the exchange is mandatory. |
| `searchSymbolName` | string | true | Trading Symbol of the scrip to be searched. |
| `expiryDate` | string | false | expiryDate in `yyyy-MM-dd` format. |
| `strikePrice` | string | false | The strike price is the predetermined price at which a put buyer can sell the underlying asset. |
| `optionType` | string | false | Option Type (PE/CE). |

### Sample Request Body

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/option/optionChain?exchange=NFO&searchSymbolName=NIFTY&strikePrice=25500&optionType=PE&expiryDate=2024-10-03' \
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
        .uri(URI.create("https://tradeapi.samco.in/option/optionChain?exchange=NFO&searchSymbolName=NIFTY&strikePrice=25500&optionType=PE&expiryDate=2024-10-03"))
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

  const response = await fetch('https://tradeapi.samco.in/option/optionChain?exchange=NFO&searchSymbolName=NIFTY&strikePrice=25500&optionType=PE&expiryDate=2024-10-03', {
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

r = requests.get('https://tradeapi.samco.in/option/optionChain?exchange=NFO&searchSymbolName=NIFTY&strikePrice=25500&optionType=PE&expiryDate=2024-10-03',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
    "serverTime": "25/09/24 12:23:57",
    "msgId": "e2a12d98-3c93-4773-84a8-c82c722a9a6b",
    "status": "Success",
    "statusMessage": "OptionChain details retrived successfully. ",
    "optionChainDetails": [
        {
            "tradingSymbol": "NIFTY03OCT2425500PE",
            "exchange": "NFO",
            "symbol": "58534_NFO",
            "strikePrice": "25500.0000",
            "expiryDate": "2024-10-03",
            "instrument": "OPTIDX",
            "optionType": "PE",
            "underLyingSymbol": "NIFTY",
            "spotPrice": "25884.10",
            "lastTradedPrice": 52.55,
            "openInterest": 1312350,
            "openInterestInLot": 52494,
            "openInterestChange": 94825,
            "openInterestChangeInLot": 3793,
            "oichangePer": "7.79",
            "volume": 1620250,
            "impliedVolatility": "13.1337",
            "delta": "-0.187226",
            "gamma": "0.000530033",
            "theta": "-7.04959",
            "vega": "10.3883",
            "bestBids": [
                {
                    "number": 1,
                    "quantity": "200",
                    "price": "52.40"
                },
                {
                    "number": 2,
                    "quantity": "175",
                    "price": "52.35"
                },
                {
                    "number": 3,
                    "quantity": "600",
                    "price": "52.30"
                },
                {
                    "number": 4,
                    "quantity": "675",
                    "price": "52.25"
                },
                {
                    "number": 5,
                    "quantity": "2700",
                    "price": "52.20"
                }
            ],
            "bestAsks": [
                {
                    "number": 1,
                    "quantity": "250",
                    "price": "52.55"
                },
                {
                    "number": 2,
                    "quantity": "2275",
                    "price": "52.60"
                },
                {
                    "number": 3,
                    "quantity": "1650",
                    "price": "52.65"
                },
                {
                    "number": 4,
                    "quantity": "575",
                    "price": "52.70"
                },
                {
                    "number": 5,
                    "quantity": "550",
                    "price": "52.75"
                }
            ]
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
| `status` | string | The status of the API response. It can be either 'Success' or 'Failure' |
| `statusMessage` | string | A message describing the result of the API call. |
| `optionChainDetails` | [object] | Scrips details available for the provided search text. |
| `tradingSymbol` | string | Trading Symbol of the scrip. |
| `exchange` | string | Name of the exchange. Valid exchanges values (BSE/ NSE/ NFO/ MCX/ CDS). If the user does not provide an exchange name, by default considered as NSE. For trading with BSE, NFO, CDS, and MCX, exchange is mandatory. |
| `symbol` | string | Symbol Code of the trading Symbol. |
| `strikePrice` | string | The strike price is the predetermined price at which a put buyer can sell the underlying asset. |
| `expiryDate` | string | Shows expiry date of a trading symbol. |
| `instrument` | string | Instrument Name. |
| `optionType` | string | Option Type (PE/CE). |
| `underLyingSymbol` | string | Root symbol of TradingSymbol. |
| `spotPrice` | string | Spot price. Applicable in case of Futures and Options. |
| `lastTradedPrice` | string | Price at which last transaction/trade is done. |
| `openInterest` | string | Open interest is the number of existing contracts held by buyers or sellers for any market for any given day. |
| `openInterestChange` | string | Shows the open interest change in number of contracts held for the market. |
| `oichangePer` | string | Shows the percentage change based on open interest. |
| `volume` | string | Limit amount of a security traded on the specific day. |
| `impliedVolatility` | string | The market's expectation of future volatility of the underlying asset |
| `delta` | string | Measures the sensitivity of the F&O’s price to changes in the price of the underlying asset. |
| `gamma` | string | Measures the rate of change of delta with respect to changes in the underlying asset's price. |
| `theta` | string | Measures the rate at which the F&O’s price decreases as it approaches expiration. |
| `vega` | string | Measures the sensitivity of the F&O’s price to changes in the volatility of the underlying asset. |
| `bestBids` | [object] | Most frequent trading bids for BUY. |
| `number` | string | Sequence number for Bid/Ask. |
| `quantity` | string | Quantity asked for trading. |
| `price` | string | Price asked for trading. |
| `bestAsks` | [object] | Most frequent trading asks for SELL. |
| `number` | string | Sequence number for Bid/Ask. |
| `quantity` | string | Quantity asked for trading. |
| `price` | string | Price asked for trading. |

---

## Future Chain

`GET /future/futureChain`

This API is used to search futureChain for equity, derivatives, and commodity scripts based on the user-provided search symbol and exchange name.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | false | Name of the exchange. Valid exchanges values (NFO/BFO/CDS/MCX/MFO). If the user does not provide an exchange name, by default considered as NFO. For trading with CDS, BFO, MCX, and MFO, exchange is mandatory. |
| `searchSymbolName` | string | true | Trading Symbol of the scrip to be searched. |
| `expiryDate` | string | false | expiryDate in yyyy-MM-dd. |

### Sample Request Body

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/future/futureChain?searchSymbolName=SENSEX&expiryDate=2024-09-27&exchange=BFO' \
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
        .uri(URI.create("https://tradeapi.samco.in/future/futureChain?searchSymbolName=SENSEX&expiryDate=2024-09-27&exchange=BFO"))
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

  const response = await fetch('https://tradeapi.samco.in/future/futureChain?searchSymbolName=SENSEX&expiryDate=2024-09-27&exchange=BFO', {
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

r = requests.get('https://tradeapi.samco.in/future/futureChain?searchSymbolName=SENSEX&expiryDate=2024-09-27&exchange=BFO',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
    "serverTime": "25/09/24 12:34:22",
    "msgId": "d0154c21-8bbd-43ff-a64b-2f9bcdae7b9c",
    "status": "Success",
    "statusMessage": "Future chain details retrived successfully. ",
    "futureChainDetails": [
        {
            "tradingSymbol": "SENSEX24SEPFUT",
            "exchange": "BFO",
            "symbol": "859754_BFO",
            "expiryDate": "2024-09-27",
            "instrument": "IF",
            "underLyingSymbol": "SENSEX",
            "spotPrice": 84805.89,
            "lastTradedPrice": "84819.00",
            "openInterest": 13730,
            "openInterestInLot": 1373,
            "openInterestChange": 360,
            "openInterestChangeInLot": 36,
            "oichangePer": "2.69",
            "volume": 2860,
            "impliedVolatility": "0",
            "delta": "0",
            "gamma": "0",
            "theta": "0",
            "vega": "0",
            "bestBids": [
                {
                    "number": 1,
                    "quantity": "50",
                    "price": "84815.45"
                },
                {
                    "number": 2,
                    "quantity": "50",
                    "price": "84815.00"
                },
                {
                    "number": 3,
                    "quantity": "10",
                    "price": "84814.80"
                },
                {
                    "number": 4,
                    "quantity": "50",
                    "price": "84814.50"
                },
                {
                    "number": 5,
                    "quantity": "80",
                    "price": "84814.45"
                }
            ],
            "bestAsks": [
                {
                    "number": 1,
                    "quantity": "10",
                    "price": "84825.00"
                },
                {
                    "number": 2,
                    "quantity": "50",
                    "price": "84833.30"
                },
                {
                    "number": 3,
                    "quantity": "30",
                    "price": "84833.35"
                },
                {
                    "number": 4,
                    "quantity": "100",
                    "price": "84833.40"
                },
                {
                    "number": 5,
                    "quantity": "80",
                    "price": "84833.45"
                }
            ]
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
| `status` | string | The status of the API response. It can be either 'Success' or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `futureChainDetails` | [object] | Scrips Details available for the provided search text. |
| `tradingSymbol` | string | Trading Symbol of the scrip. |
| `exchange` | string | Exchange information indicates which exchange each trading symbol comes from. |
| `symbol` | string | Symbol Code of the trading Symbol. |
| `expiryDate` | string | Shows expiry date of a trading symbol. |
| `instrument` | string | Instrument Name. |
| `underLyingSymbol` | string | Root symbol of TradingSymbol. |
| `spotPrice` | string | Spot price. Applicable in case of Futures and Options. |
| `lastTradedPrice` | string | Price at which last transaction / trade is done. |
| `openInterest` | string | Open interest is the Number of existing contracts held by buyers or sellers for any market for any given day. |
| `openInterestChange` | string | It shows Open interest change in Number of contracts held for market. |
| `oichangePer` | string | It will show the change % based on Open Interest. |
| `volume` | string | Limit amount of a security traded on the specific day. |
| `impliedVolatility` | string | The market's expectation of future volatility of the underlying asset |
| `delta` | string | Measures the sensitivity of the F&O’s price to changes in the price of the underlying asset. |
| `gamma` | string | Measures the rate of change of delta with respect to changes in the underlying asset's price. |
| `theta` | string | Measures the rate at which the F&O’s price decreases as it approaches expiration. |
| `vega` | string | Measures the sensitivity of the F&O’s price to changes in the volatility of the underlying asset. |
| `bestBids` | [object] | Most frequent trading bids for BUY. |
| `number` | string | Sequence number for Bid/Ask. |
| `quantity` | string | Quantity asked for trading. |
| `price` | string | Price asked for trading. |
| `bestAsks` | [object] | Most frequent trading asked for SELL. |
| `number` | string | Sequence number for Bid/Ask. |
| `quantity` | string | Quantity asked for trading. |
| `price` | string | Price asked for trading. |

---

## Index Quote

`GET /quote/indexQuote`

Getting Index Quote details for a specific Indicies. This helps user with market picture of an specific Index Details.

### Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `indexName` | string | true | Index name of the scrip. |

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/quote/indexQuote?indexName=Sensex' \
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
        .uri(URI.create("https://tradeapi.samco.in/quote/indexQuote?indexName=Sensex"))
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

  const response = await fetch('https://tradeapi.samco.in/quote/indexQuote?indexName=Sensex', {
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

r = requests.get('https://tradeapi.samco.in/quote/indexQuote?indexName=Sensex',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
    "serverTime": "04/04/24 14:34:13",
    "msgId": "13f6cb1e-8c31-4c5c-a15b-df7b27ac15a5",
    "status": "Success",
    "statusMessage": "Index Quote details retrieved successfully",
    "indexDetails": [
        {
            "indexName": "SENSEX",
            "listingId": "-101",
            "lastTradedTime": "2024-04-04 14:34:12.0",
            "spotPrice": 74344.02,
            "changePercentage": 0.63,
            "averagePrice": 0,
            "openValue": 74413.82,
            "highValue": 74501.73,
            "lowValue": 73485.12,
            "closeValue": 73876.82,
            "totalBuyQuantity": 0,
            "totalSellQuantity": 0,
            "totalTradedValue": 0,
            "totalTradedVolume": 0,
            "change": 467.2
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
| `status` | string | The status of the API response. It can be either 'Success' or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `indexName` | string | Index Name of the indices. |
| `listingId` | string | Identifier assigned to the scrip by exchange in the format <>_<>. |
| `lastTradedTime` | string | Time of the last transaction. |
| `spotPrice` | string | Spot price. Applicable in case of Futures and Options. |
| `changePercentage` | string | Percentage of change between the current value and the previous day's market close. |
| `averagePrice` | string | Average price of a market snapshot. |
| `openValue` | string | Opening price of a market snapshot. |
| `highValue` | string | High value of market snapshot. |
| `lowValue` | string | Low value of market snapshot. |
| `closeValue` | string | Close value of market snapshot. |
| `totalBuyQuantity` | string | Total quantity of BUY transactions. |
| `totalSellQuantity` | string | Total quantity of SELL transactions. |
| `totalTradedValue` | string | Value of total trade made for the scrip. |
| `totalTradedVolume` | string | Total volume of trading done. |
| `change` | string | Change value is the difference between the current value and the previous day's market close. |

---

## Get Quote

`GET /quote/getQuote`

Get market depth details for a specific equity scrip including but not limited to values like last trade price, previous close price, change value, change percentage, bids/asks, upper and lower circuit limits etc. This helps user with market picture of an equity scrip using which he will be able to place an order.

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `exchange` | string | false | Name of the exchange. Valid values include BSE, NSE, NFO, BFO, MCX, MFO, CDS. If not provided, default is NSE. For BSE, NFO, BFO, MFO, CDS, and MCX, exchange is mandatory. |
| `symbolName` | string | true | Symbol name of the scrip. For Equity, enter the SymbolName of the scrip. For Derivatives, enter the TradingSymbol of the scrip. |

### Sample Code

**cURL**

```bash
curl -X GET 'https://tradeapi.samco.in/quote/getQuote?symbolName=ASIANPAINT24APR2760PE&exchange=NFO' \
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
        .uri(URI.create("https://tradeapi.samco.in/quote/getQuote?symbolName=ASIANPAINT24APR2760PE&exchange=NFO"))
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

  const response = await fetch('https://tradeapi.samco.in/quote/getQuote?symbolName=ASIANPAINT24APR2760PE&exchange=NFO', {
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

r = requests.get('https://tradeapi.samco.in/quote/getQuote?symbolName=ASIANPAINT24APR2760PE&exchange=NFO',
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
    "serverTime": "04/04/24 15:47:05",
    "msgId": "4568350b-c552-4a53-8981-45241b5d20e7",
    "status": "Success",
    "statusMessage": "Quote details retrieved successfully",
    "quoteDetails": {
        "symbolName": "ASIANPAINT",
        "tradingSymbol": "ASIANPAINT24APR2760PE",
        "exchange": "NFO",
        "lastTradedTime": "04/04/2024 15:29:58",
        "lastTradedPrice": "09.95",
        "previousClose": "14.7",
        "changeValue": "-4.75",
        "changePercentage": "-32.31",
        "lastTradedQuantity": "200",
        "lowerCircuitLimit": "0.05",
        "upperCircuitLimit": "36.45",
        "averagePrice": "11.92",
        "openValue": "13.2",
        "highValue": "18.85",
        "lowValue": "7.65",
        "closeValue": "14.7",
        "totalBuyQuantity": "45200",
        "totalSellQuantity": "29000",
        "totalTradedValue": "31.4211200 (Lacs)",
        "totalTradedVolume": "263600",
        "yearlyHighPrice": "0",
        "yearlyLowPrice": "0",
        "tickSize": "0.05",
        "bestBids": [
            {
                "number": "1",
                "quantity": "200",
                "price": "9.6"
            },
            {
                "number": "2",
                "quantity": "200",
                "price": "9.55"
            },
            {
                "number": "3",
                "quantity": "200",
                "price": "9.5"
            },
            {
                "number": "4",
                "quantity": "200",
                "price": "9.45"
            },
            {
                "number": "5",
                "quantity": "6000",
                "price": "8.35"
            }
        ],
        "bestAsks": [
            {
                "number": "1",
                "quantity": "200",
                "price": "10.2"
            },
            {
                "number": "2",
                "quantity": "200",
                "price": "10.25"
            },
            {
                "number": "3",
                "quantity": "200",
                "price": "10.6"
            },
            {
                "number": "4",
                "quantity": "200",
                "price": "10.65"
            },
            {
                "number": "5",
                "quantity": "200",
                "price": "10.75"
            }
        ],
        "listingId": "73859_NFO",
        "openInterestChange": "-4200",
        "instrument": "OPTSTK",
        "expiryDate": "25 Apr 24",
        "lotQuantity": "200",
        "oIChangePer": "-9.95"
    }
}
```

### Response Schema

Status Code **200**

| **Name** | **Type** | **Description** |
| --- | --- | --- |
| `serverTime` | string | Time at Server. |
| `msgId` | string | Unique identifier for every request. Useful for tracking and troubleshooting. |
| `status` | string | Status of the API response. Can be 'Success' or 'Failure'. |
| `statusMessage` | string | Descriptive message regarding the result of the API call. |
| `symbolName` | string | Symbol name of the scrip. |
| `tradingSymbol` | string | Trading Symbol of the scrip. |
| `exchange` | string | Name of the exchange. Valid values include BSE, NSE, NFO, MCX, CDS. Defaults to NSE if not provided. Mandatory for BSE, NFO, CDS, and MCX. |
| `companyName` | string | Full name of the company. |
| `lastTradedTime` | string | Time of the last transaction. |
| `lastTradedPrice` | string | Price at which the last transaction was done. |
| `previousClose` | string | Previous close refers to the prior day's final price of the security at market close. |
| `changeValue` | string | Difference between the current value and the previous day's market close. |
| `changePercentage` | string | Percentage change between the current value and the previous day's market close. |
| `lastTradedQuantity` | string | Quantity of the last transaction. |
| `lowerCircuitLimit` | string | Limit below which a stock price cannot trade on a particular trading day. |
| `upperCircuitLimit` | string | Limit above which a stock price cannot trade on a particular trading day. |
| `averagePrice` | string | Average price of the trading session. |
| `openValue` | string | Opening price of the market snapshot. |
| `highValue` | string | High value of the market snapshot. |
| `lowValue` | string | Low value of the market snapshot. |
| `closeValue` | string | Close value of the market snapshot. |
| `totalBuyQuantity` | string | Total quantity of BUY transactions. |
| `totalSellQuantity` | string | Total quantity of SELL transactions. |
| `totalTradedValue` | string | Total value of trades made for the scrip. |
| `totalTradedVolume` | string | Total volume of trading done. |
| `yearlyHighPrice` | string | 52-week high price. |
| `yearlyLowPrice` | string | 52-week low price. |
| `tickSize` | string | Value of a single price tick. Default is 0.05. |
| `openInterest` | string | Number of existing contracts held by buyers or sellers for any market on a given day. |
| `bestBids` | object | Most frequent trading bids for BUY. |
| `number` | string | Sequence number for Bid/Ask. |
| `quantity` | string | Quantity asked for trading. |
| `price` | string | Price asked for trading. |
| `bestAsks` | object | Most frequent trading asks for SELL. |
| `number` | string | Sequence number for Bid/Ask. |
| `quantity` | string | Quantity asked for trading. |
| `price` | string | Price asked for trading. |
| `expiryDate` | string | Expiry date of the scrip. |
| `spotPrice` | string | Spot price. Applicable in case of Futures and Options. |
| `instrument` | string | Instrument Name. |
| `lotQuantity` | string | Lot quantity. Applicable for Futures & Options. |
| `listingId` | string | Identifier assigned to the scrip by the exchange in the format `<>_<>`. |
| `openInterestChange` | string | Change in open interest, reflecting the number of contracts held for the market. |
| `getoIChangePer` | string | Percentage change in open interest. |

---

## Multi Quote

`POST /quote/multiQuote`

### Parameters

| **Name** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| `BSE` | array | false | Assign the array of BSE symbol names to the BSE key. |
| `NSE` | array | false | Assign the array of NSE symbol names to the NSE key. |
| `BFO` | array | false | Assign the array of trading symbols to the BFO key. |
| `NFO` | array | false | Include the NFO trading symbol in the array and assign it to the NFO key. |
| `CDS` | array | false | Assign the array of CDS trading symbols to the CDS key. |
| `MCX` | array | false | Assign the array of MCX trading symbols to the MCX key. |
| `MFO` | array | false | Assign the array of MFO trading symbols to the MFO key. |
| `INDEX` | array | false | Assign the array of index names to the INDEX key. |

### Sample Request Body

```json

requestBody={
  "NSE":["TCS"],
  "MFO" :["SILVER24APR76250PE"] 
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/quote/multiQuote' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"NSE":["TCS"],"MFO":["SILVER24APR76250PE"]}'
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
          "NSE": [
            "TCS"
          ],
          "MFO": [
            "SILVER24APR76250PE"
          ]
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/quote/multiQuote"))
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
    NSE: [
      "TCS"
    ],
    MFO: [
      "SILVER24APR76250PE"
    ]
  };

  const response = await fetch('https://tradeapi.samco.in/quote/multiQuote', {
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
  "NSE": [
    "TCS"
  ],
  "MFO": [
    "SILVER24APR76250PE"
  ]
}

r = requests.post('https://tradeapi.samco.in/quote/multiQuote',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Responses

```json
{
    "serverTime": "05/04/24 10:46:55",
    "msgId": "6dd6d540-33a5-4516-9818-e223370f4846",
    "status": "Success",
    "statusMessage": "Multiquotes data retrieved successfully",
    "multiQuotes": [
        {
            "exchange": "NSE",
            "symbolName": "TCS",
            "tradingSymbol": "TCS-EQ",
            "companyName": "TATA CONSULTANCY SERV LT",
            "isin": "INE467B01029",
            "lotSize": "1",
            "averagePrice": "3840.50",
            "totalTradeVolume": "4311783",
            "symbol": "11536_NSE",
            "lastTradeTime": "28 Mar 2024, 07:11:43 PM",
            "lastTradeQuantity": "1",
            "lastTradePrice": "3876.30",
            "misMultiplier": "4.00",
            "change": "35.40",
            "changePercent": "0.92",
            "open": "3850.10",
            "close": "3876.30",
            "previousClose": "3840.90",
            "low": "3840.50",
            "high": "3915.00",
            "tickSize": "0.05",
            "bidSize": "782",
            "bidPrice": "3876.30",
            "totalTradedValue": "16732176051.06",
            "askSize": "0",
            "askPrice": "0.00",
            "iv": "0.00"
        },
        {
            "exchange": "MCX",
            "symbolName": "SILVER",
            "tradingSymbol": "SILVER24APR76250PE",
            "optionType": "PE",
            "instrumentType": "OPTCOM",
            "companyName": "SILVER",
            "lotSize": "30",
            "strikePrice": "76250.0000",
            "expiry": "24 Apr 24",
            "averagePrice": "0.00",
            "totalTradeVolume": "0",
            "symbol": "256981_MFO",
            "lastTradeTime": "01 Apr 2024, 04:34:41 PM",
            "lastTradeQuantity": "0",
            "lastTradePrice": "0.00",
            "misMultiplier": "100.00",
            "multiplier": "30",
            "openInterest": "0",
            "previousOpenInterest": "0",
            "change": "0.00",
            "changePercent": "0.00",
            "open": "0.00",
            "close": "1656.00",
            "previousClose": "0.00",
            "low": "0.00",
            "high": "0.00",
            "tickSize": "0.5",
            "bidSize": "0",
            "bidPrice": "0.00",
            "totalTradedValue": "0.00",
            "askSize": "0",
            "askPrice": "0.00",
            "delta": "0.00",
            "vega": "0.00",
            "theta": "0.00",
            "gamma": "0.0000",
            "iv": "0.00"
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
| `status` | string | The status of the API response. It can be either 'Success' or 'Failure'. |
| `statusMessage` | string | A message describing the result of the API call. |
| `multiQuotes` | object | Get list of multiQuote. |
| `exchange` | string | Name of the exchange. |
| `symbolName` | string | Symbol name of the scrip. |
| `tradingSymbol` | string | Trading Symbol of the scrip. |
| `optionType` | string | Option Type (PE/CE). |
| `instrumentType` | string | Instrument Name. |
| `companyName` | string | Full name of the trading company. |
| `isin` | string | The standard ISIN representing stocks uniquely at an international level. It is the same for every exchange. |
| `lotSize` | string | Lot size of the symbol to be traded. At the time of placing an order, the quantity should be in multiples of the Broadlot Qty only. |
| `strikePrice` | string | The strike price is the predetermined price at which a put buyer can sell the underlying asset. |
| `expiry` | string | Shows expiry date of a trading symbol. |
| `averagePrice` | string | Average trading price of the equity or derivative. |
| `totalTradeVolume` | string | The total amount of shares or contracts that have been traded. |
| `symbol` | string | Actual symbol name of the scrip. |
| `lastTradeTime` | string | Last transaction time in milliseconds. |
| `lastTradeQuantity` | string | Quantity of last transaction. |
| `lastTradePrice` | string | Price at which the last transaction/trade is done. |
| `misMultiplier` | string | The MIS multiplier indicates how many times a trader can exceed their available funds when purchasing shares. |
| `change` | string | Change value is the difference between the current value and the previous day's market close. |
| `changePercent` | string | Percentage of change between the current value and the previous day's market close. |
| `open` | string | Opening price of a market snapshot. |
| `close` | string | Close value of market snapshot. |
| `previousClose` | string | Previous close refers to the prior day's final price of security when the market officially closes for the day. |
| `low` | string | Low value of market snapshot. |
| `high` | string | High value of market snapshot. |
| `tickSize` | string | The value of a single price tick. Default value is 0.05. |
| `bidSize` | string | The number of shares investors are trying to buy at a given price. |
| `bidPrice` | string | The price at which investors are seeking to purchase shares. |
| `totalTradedValue` | string | The total monetary value of all trades executed for the scrip. |
| `askSize` | string | The number of shares investors are willing to sell at a given price. |
| `askPrice` | string | The price at which sellers are willing to sell the scrip. |
| `iv` | string | Implied Volatility. |
