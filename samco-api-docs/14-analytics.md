# Trade View Analytics

Realised/unrealised P&L summaries, trade-level detail, and gain-loss reporting.

## Analytics Summary API

`POST tradeview/analyticsSummary`

The `analyticsSummary` API retrieves a summarized analysis of a user's trading performance over a specified time period. This summary includes insights into the user's trade scores, best and worst performing strategies, sector performance, and suggestions for improvement based on their trading behavior.

### Request Parameters

The request requires a `duration` parameter, which specifies the time period for which the analytics summary will be generated. If `duration` is not provided, it defaults to `ALL`, which means all available data. Possible values are summarized below:

| Key | Type | Allowed Values | Description |
| --- | --- | --- | --- |
| `duration` | String | `ALL`, `1Y`, `6M`, `1M` | Specifies the time period for analysis. Defaults to `ALL` if not provided. |

### Sample Request Body

```json
{
    "duration": "ALL"
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/tradeview/analyticsSummary' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"duration":"ALL"}'
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
          "duration": "ALL"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/tradeview/analyticsSummary"))
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
    duration: "ALL"
  };

  const response = await fetch('https://tradeapi.samco.in/tradeview/analyticsSummary', {
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
  "duration": "ALL"
}

r = requests.post('https://tradeapi.samco.in/tradeview/analyticsSummary',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Response

The response includes a `status`, `statusMessage`, `serverTime`, `msgId`, and a detailed `analyticsSummary` with trade insights.

```json
{
    "serverTime": "29/10/24 12:10:26",
    "msgId": "cdce1c29-5c14-4990-9748-24273b770a4c",
    "status": "Success",
    "statusMessage": "Analytics summary retrieved successfully.",
    "analyticsSummary": {
        "insightMessage": [
            {
                "AndekhaSach": "Your Samco Trade Score of <b>0.13</b> is very poor. If this ratio is not improved,your chances of success in the stock market are very low. Great traders have a score of at least more than 3",
                "ActionSuggested": "To improve this ratio you should either improve your win rate by working on your strategy or reduce your average losses by adding stop loss and cutting your losers early."
            },
            {
                "AndekhaSach": "<b>Shorting Equity and squaring off Intraday strategy</b> strategy, having a Samco Trade Score of <b>0.97</b>, has been working really well for you. Your trade performance is best in this strategy.",
                "ActionSuggested": "You should focus on allocating more to this strategy because it is working wonderfully for you"
            },
            {
                "AndekhaSach": "You have the most poor performance in <b>Buying Index Call Options</b> strategy",
                "ActionSuggested": "You should either completely avoid this strategy or work on improving it"
            },
            {
                "AndekhaSach": "Your best performance is in <b>Banking</b> sector in <b>EQ-Intraday</b> segment and your worst performance is in <b>Others</b> sector in <b>EQ-Delivery</b> segment.",
                "ActionSuggested": "You should focus on allocating more to <b>Banking</b> sector since it is working great for you. Also, you should either completely avoid picking <b>Others</b> sector or work on improving your strategy therein."
            },
            {
                "AndekhaSach": "Your best performance is in stocks belonging to <b>Intraday-Long Micro Cap</b> category in <b>EQ</b> Strategy and your worst performance is in stocks of <b>Intraday-Long Mid Cap</b> category in <b>EQ</b> strategy.",
                "ActionSuggested": "You should focus on allocating more to <b>Intraday-Long Micro Cap</b> category stocks since it is working great for you. Also, you should either completely avoid picking <b>Intraday-Long Mid Cap</b> stocks or work on improving your strategy therein."
            },
            {
                "AndekhaSach": "On your losing trades in options segment, you could have reduced your loss by approx. <b>79.86</b>% per trade by simply adding a reasonable stop loss of 20%",
                "ActionSuggested": "Basis your risk appetite, define what stop loss suits you and start placing stop losses in your option trades. Remember that options are extremely volatile & hence risk management becomes essential."
            },
            {
                "AndekhaSach": "Overall, the average amount of loss on your losing trades is sizeably higher than the average gain amount on your winning trades. This is also dragging your Samco Trade Score lower.",
                "ActionSuggested": "Your focus should be on:\n\t- Reducing the average loss size significantly by adding stop losses on your naked positions,cutting your losing trades early \n\t- Improving your win size by letting your winners run"
            },
            {
                "AndekhaSach": "Your Samco Trade Score has decreased from <b>0.20</b> in <b>AUGUST</b> to <b>0.18</b> in <b>SEPTEMBER</b>.This indicates a decline in your overall performance.There is ample room for improvement!",
                "ActionSuggested": "To improve your Samco Trade Score, you should focus on: \nImproving your strike rate by allocating more to strategies that are working for you \nReducing the average loss size further by adding stop losses"
            },
            {
                "AndekhaSach": "Your winning rate % has increased from <b>38.98</b> in <b>AUGUST</b> to <b>40.62</b> in <b>SEPTEMBER</b>.This positive trend reflects your growing proficiency.Keep up the good work!",
                "ActionSuggested": "To improve your Samco Trade Score, you should focus on: \nImproving your strike rate by allocating more to strategies that are working for you \nReducing the average loss size further by adding stop lossesYou have done a good job in the last month.But,to further improve your Strike rate,you should focus on: \nAllocating more to the strategies that are working for you \nHaving proper stop-loss management to minimize losing positions"
            }
        ],
        "samcoSucessProbabilityRatio": "0.13",
        "strikeRateWinningTrade": "37.31",
        "strikeRateLosingTrade": "62.69",
        "averageWinSize": "2.13",
        "averageLossSize": "23.76",
        "averageHoldingWinningTrade": "14",
        "averageHoldingLosingTrade": "15",
        "averageGainPercentage": "3.35",
        "averageLossPercentage": "15.74",
        "startDate": "2022-12-30",
        "endDate": "2024-10-29"
    }
}
```

#### Response Key Descriptions

| Key | Type | Description |
| --- | --- | --- |
| `serverTime` | String | Server's response timestamp in `dd/MM/yy HH:mm:ss` format. |
| `msgId` | String | Unique identifier for the response message. |
| `status` | String | Status of the request, e.g., `"Success"` or `"Failure"`. |
| `statusMessage` | String | Provides additional information about the response, e.g., `"Analytics summary retrieved successfully."`. |
| `analyticsSummary` | Object | Contains the detailed summary of trading analytics and recommendations. |
| `insightMessage` | Array | Array of objects, each containing insights and suggestions for the user. |
| `AndekhaSach` | String | Key insight about the user's trading behavior. |
| `ActionSuggested` | String | Suggested action based on the insight provided. |
| `samcoSucessProbabilityRatio` | String | The calculated Samco Trade Score, indicating the user's success probability ratio. |
| `strikeRateWinningTrade` | String | Percentage of winning trades. |
| `strikeRateLosingTrade` | String | Percentage of losing trades. |
| `averageWinSize` | String | Average size of winning trades. |
| `averageLossSize` | String | Average size of losing trades. |
| `averageHoldingWinningTrade` | String | Average holding period of winning trades (in days). |
| `averageHoldingLosingTrade` | String | Average holding period of losing trades (in days). |
| `averageGainPercentage` | String | Average percentage gain on winning trades. |
| `averageLossPercentage` | String | Average percentage loss on losing trades. |
| `startDate` | String | Start date for the analytics period in `YYYY-MM-DD` format. |
| `endDate` | String | End date for the analytics period in `YYYY-MM-DD` format. |

##### Summary of `analyticsSummary` Fields

The `analyticsSummary` object provides comprehensive feedback on the user's trading performance:

- **Insight Messages**: Offers specific insights into the user’s trading strategies, such as strengths, weaknesses, and recommended actions.
- **Samco Success Probability Ratio**: Indicates the user's success probability; higher values imply a better chance of consistent trading success.
- **Strike Rate**: Breakdown of winning and losing trade percentages.
- **Average Trade Metrics**: Highlights the average win and loss sizes, holding periods, and the gains/losses as a percentage.
- **Time Range**: Represents the period over which the analytics were calculated.

---

This API is useful for traders looking to enhance their performance by understanding areas for improvement, successful strategies, and areas that need re-evaluation.

---

## Analytics Details

`POST tradeview/analyticsDetails`

The TradeView Analytics Details API retrieves detailed analytics for a given duration and filter type, providing insights on trading strategies or market characteristics. It returns metrics such as average win/loss size, success probability, holding periods, and transaction summaries categorized by strategy or other parameters.

---

### Request Parameters

| Parameter | Type | Possible Values | Description |
| --- | --- | --- | --- |
| `duration` | String | ALL / 1Y / 6M / 1M | Specifies the time duration for which analytics details are retrieved. If not provided, it defaults to `ALL`. |
| `filter` | String | strategy / market cap / sector | Specifies the category by which analytics are filtered. If not provided, it defaults to `strategy`. |

### Sample Request Body

```json
{
    "duration":"1M",
    "filter":"strategy"
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/tradeview/analyticsDetails' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"duration":"1M","filter":"strategy"}'
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
          "duration": "1M",
          "filter": "strategy"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/tradeview/analyticsDetails"))
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
    duration: "1M",
    filter: "strategy"
  };

  const response = await fetch('https://tradeapi.samco.in/tradeview/analyticsDetails', {
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
  "duration": "1M",
  "filter": "strategy"
}

r = requests.post('https://tradeapi.samco.in/tradeview/analyticsDetails',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Response

```json
{
    "serverTime": "29/10/24 13:05:39",
    "msgId": "1d3cacfa-cce8-4a6c-941e-0a8baaa53455",
    "status": "Success",
    "statusMessage": "Analytics Details retrieved successfully.",
    "analyticsDetails": {
        "averageWinSize": "0.00",
        "averageLossSize": "0.15",
        "samcoSuccessProbabilityRatio": "0.00",
        "strikeRateWinningTrades": "0.00",
        "strikeRateLosingTrades": "100.00",
        "averageHoldingPeriodWin": "0",
        "averageHoldingPeriodLoss": "0",
        "startDate": "2024-09-29",
        "endDate": "2024-10-29",
        "averageGainPercentage": "0.00",
        "averageLossPercentage": "0.99",
        "strategyList": [
            {
                "groupName": "Equity-Cash Market",
                "strategywiseList": [
                    {
                        "strategy": "Long Intraday",
                        "averagePL": "-0.15",
                        "plContribution": "0.00",
                        "winningTradesPercentage": "0.00",
                        "losingTradesPercentage": "100.00",
                        "sspRatio": "0.00",
                        "strikeRateWinningTrades": "0.00",
                        "strikeRateLosingTrades": "100.00",
                        "averageGainPercentage": "0.00",
                        "averageLossPercentage": "0.99",
                        "strikeRatePercentage": "0.00",
                        "averageWinSize": "0.00",
                        "averageLossSize": "0.15",
                        "holdingPeriodWinners": "0",
                        "holdingPeriodLossers": "0",
                        "avgHoldingPeriodWin": "0",
                        "avgHoldingPeriodLoss": "0",
                        "totalTransaction": 2
                    }
                ]
            }
        ]
    }
}
```

#### Response Key Descriptions

| Parameter | Type | Description |
| --- | --- | --- |
| `serverTime` | String | Timestamp of the response in the format `DD/MM/YY HH:MM:SS`. |
| `msgId` | String | Unique identifier for the message. |
| `status` | String | Status of the API call (e.g., "Success"). |
| `statusMessage` | String | Message providing additional information about the status. |
| `analyticsDetails` | Object | Main container for analytics details. |
| `analyticsDetails.averageWinSize` | String | Average size of winning trades. |
| `analyticsDetails.averageLossSize` | String | Average size of losing trades. |
| `analyticsDetails.samcoSuccessProbabilityRatio` | String | Success probability ratio for trades. |
| `analyticsDetails.strikeRateWinningTrades` | String | Percentage of trades that were successful. |
| `analyticsDetails.strikeRateLosingTrades` | String | Percentage of trades that were unsuccessful. |
| `analyticsDetails.averageHoldingPeriodWin` | String | Average holding period for winning trades. |
| `analyticsDetails.averageHoldingPeriodLoss` | String | Average holding period for losing trades. |
| `analyticsDetails.startDate` | String | Start date of the specified duration (format `YYYY-MM-DD`). |
| `analyticsDetails.endDate` | String | End date of the specified duration (format `YYYY-MM-DD`). |
| `analyticsDetails.averageGainPercentage` | String | Average percentage gain on trades. |
| `analyticsDetails.averageLossPercentage` | String | Average percentage loss on trades. |
| `analyticsDetails.strategyList` | Array | List of strategy group details within the analytics data. |
| `strategyList[].groupName` | String | Name of the strategy group, such as "Equity-Cash Market." |
| `strategyList[].strategywiseList` | Array | Detailed list of analytics for each strategy. |
| `strategywiseList[].strategy` | String | Name of the trading strategy (e.g., "Long Intraday"). |
| `strategywiseList[].averagePL` | String | Average profit/loss for the strategy. |
| `strategywiseList[].plContribution` | String | Contribution of this strategy to overall P/L. |
| `strategywiseList[].winningTradesPercentage` | String | Percentage of winning trades in this strategy. |
| `strategywiseList[].losingTradesPercentage` | String | Percentage of losing trades in this strategy. |
| `strategywiseList[].sspRatio` | String | Success probability ratio within the strategy. |
| `strategywiseList[].strikeRateWinningTrades` | String | Strike rate for winning trades in this strategy. |
| `strategywiseList[].strikeRateLosingTrades` | String | Strike rate for losing trades in this strategy. |
| `strategywiseList[].averageGainPercentage` | String | Average gain percentage for trades in this strategy. |
| `strategywiseList[].averageLossPercentage` | String | Average loss percentage for trades in this strategy. |
| `strategywiseList[].strikeRatePercentage` | String | Overall strike rate percentage for this strategy. |
| `strategywiseList[].averageWinSize` | String | Average size of winning trades in this strategy. |
| `strategywiseList[].averageLossSize` | String | Average size of losing trades in this strategy. |
| `strategywiseList[].holdingPeriodWinners` | String | Holding period for winning trades. |
| `strategywiseList[].holdingPeriodLossers` | String | Holding period for losing trades. |
| `strategywiseList[].avgHoldingPeriodWin` | String | Average holding period for winning trades. |
| `strategywiseList[].avgHoldingPeriodLoss` | String | Average holding period for losing trades. |
| `strategywiseList[].totalTransaction` | Integer | Total transactions made under this strategy. |

---

---

## Gain Loss

`POST tradeview/gainLoss`

The Gain and Loss API provides insights into the gains and losses of trades within a specified date range. It allows users to filter results based on the status of the trades, whether they are open or closed.

### Request Parameters

The request body should be in JSON format and include the following fields:

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| status | string | false | The status of the trades. Possible values: `open` (default) / `close`. |
| fromDate | string | true | The start date for the gain/loss calculation in `YYYY-MM-DD` format. |
| toDate | string | true | The end date for the gain/loss calculation in `YYYY-MM-DD` format. |

### Sample Request Body

```json
{
    "status": "close",
    "fromDate": "2022-10-24",
    "toDate": "2024-10-24"
}
```

### Sample Code

**cURL**

```bash
curl -X POST 'https://tradeapi.samco.in/tradeview/gainLoss' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'x-session-token: <SESSION_TOKEN>' \
  -d '{"status":"close","fromDate":"2022-10-24","toDate":"2024-10-24"}'
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
          "status": "close",
          "fromDate": "2022-10-24",
          "toDate": "2024-10-24"
        }
        """;

    HttpClient client = HttpClient.newHttpClient();

    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://tradeapi.samco.in/tradeview/gainLoss"))
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
    status: "close",
    fromDate: "2022-10-24",
    toDate: "2024-10-24"
  };

  const response = await fetch('https://tradeapi.samco.in/tradeview/gainLoss', {
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
  "status": "close",
  "fromDate": "2022-10-24",
  "toDate": "2024-10-24"
}

r = requests.post('https://tradeapi.samco.in/tradeview/gainLoss',
  data=json.dumps(requestBody),
  headers=headers)

print(r.json())
```

### Sample Response

```json
{
    "serverTime": "29/10/24 13:23:18",
    "msgId": "1cc16113-e30d-4d4b-b1ca-8b738ef7150c",
    "status": "Success",
    "statusMessage": "Analytics Details retrieved successfully.",
    "gainLossValue": {
        "realizedGL": "-905.38",
        "unrealizedGL": "0.00"
    }
}
```

#### Response Key Descriptions

| Field | Type | Description |
| --- | --- | --- |
| serverTime | string | Server timestamp in `DD/MM/YY HH:mm:ss` format. |
| msgId | string | Unique message identifier. |
| status | string | Response status (e.g., `Success`). |
| statusMessage | string | Brief status message. |
| gainLossValue | object | Contains realized and unrealized gains/losses. |
| gainLossValue.realizedGL | string | Total realized gain/loss. |
| gainLossValue.unrealizedGL | string | Total unrealized gain/loss. |
