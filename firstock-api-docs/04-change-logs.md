# Change Logs

> Source: https://firstock.in/api/docs/change-logs/

### **Developer API Version 1.9 : Monday 20th July 2026**

#### Combined Holdings API

- **New API Endpoint:** Introduced the /V1/combinedHoldings endpoint to fetch unified portfolio records in a single request.
- **Consolidated Asset Tracking:** Combines Mutual Funds and Equity Stocks datasets to deliver aggregated totals for overall investments, current valuations, and net portfolio returns.

## **Developer API Version 1.8 : Monday 27th April 2026**

Basket Order API

- Introduced new **Basket Order API** for placing multiple order legs in a single request.
- Support for multi-leg strategy execution such as spreads, hedging, and basket trading.
- Enabled batch order placement through the legs array structure
- Reduced multiple API call dependency by enabling grouped order execution in one request.

## **Developer API Version 1.7 : Tuesday 31st March 2026**

#### APIs

Enhanced order placement and security across Place Order, Modify Order, Place After Market Order, and Modify After Market Order APIs:

- **Order Slicing** – Orders exceeding the exchange-defined freeze quantity are now automatically sliced into multiple sub-orders (up to 10 slices) and placed in parallel. Applies to Place Order and Place After Market Order APIs.
- **Market Protection Enhancement** – Extended market protection logic to support SL-MKT to SL-LMT conversion alongside existing MKT to LMT conversion. Market protection is now also applied on Modify Order and Modify After Market Order APIs.
- **IP Whitelisting** – Added IP whitelist validation to restrict API access to pre-approved IP addresses for enhanced security.
- **Rate Limiting Changed** – All order placement endpoints with 10 req/sec.

## Developer API Version 1.6 : Friday 20th March 2026

#### APIs

Introduced new APIs to support After Market Orders (AMO) and enhanced options analytics:

- **Place After Market Order API** – Enables users to place orders outside regular market hours.
- **Modify After Market Order API** – Allows modification of existing AMO orders before execution.
- **Option Chain Greeks API** – Provides option chain data along with Greeks (Delta, Gamma, Theta, Vega, etc.) for better trading insights.

## Developer API Version 1.5 : Friday 30th January

#### Websockets

**Note**: WebSocket endpoint upgraded to [wss://socket.firstock.in/V2/ws](https://firstock.in/api/docs/getting-started-v2/) with new unified response format that consolidates NSE and BSE market data into standardized JSON objects per instrument.

[Click here](https://firstock.in/api/docs/getting-started-v2/) to check the latest update.

## Developer API Version 1.4 : Thursday 18th September

#### Product Conversion

**Note:** A new field**`msgFlag`** has been added to the request payload.

## Developer API Version 1.3 : Friday 8th August

#### Get Security info

**Note:** Added`companyName` and`freezeQuantity` for clearer issuer details and trade limit compliance.

#### Holding Details

New API is Added

## Developer API Version 1.2 : Friday 1st August

#### Option Chain

**Note:** Maximum value allowed for **count**is **30**.

## Developer API Version 1.1 : Friday 17th July

#### Position Book

- "**lastTradedPrice**", "**totalPNL**", "**totalMTM**", "**cfBuyAmt"**, "**cfSellAmt"**, "**cfBuyQty"**, "**cfSellQty"**key is newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
{
    "status": "success",
    "message": "Positions retrieved successfully",
    "data": [
        {
            "RealizedPNL": "0.03",
            "cfBuyAmt": "",
            "cfBuyQty": "",
            "cfSellAmt": "",
            "cfSellQty": "",
            "dayBuyAmount": "7.68",
            "dayBuyAveragePrice": "7.68",
            "dayBuyQuantity": "01",
            "daySellAmount": "7.71",
            "daySellAveragePrice": "7.71",
            "daySellQuantity": "01",
            "exchange": "NSE",
            "lastTradedPrice": "7.72",
            "lotSize": "1",
            "netAveragePrice": "0.00",
            "netQuantity": "0",
            "netUploadPrice": "0.00",
            "product": "C",
            "tickSize": "5.00",
            "token": "14366",
            "totalMTM": "0.03",
            "totalPNL": "0.03",
            "tradingSymbol": "IDEA-EQ",
            "uploadPrice": "00",
            "userId": "NP2997"
        }
    ]
}

```

**Old Success Response (V4)**

```json
      {
  "status": "success",
  "data": {
    "userId": "AA0011",
    "exchange": "NSE",
    "tradingSymbol": "ITC-EQ",
    "product": "I",
    "token": "1660",
    "pricePrecision": "2",
    "lotSize": "1",
    "tickSize": "0.05",
    "mult": "1",
    "priceFactor": "1.000000",
    "dayBuyQuantity": "4",
    "daySellQuantity": "4",
    "dayBuyAmount": "1305.90",
    "dayBuyAveragePrice": "326.48",
    "datSellAveragePrice": "328.44",
    "netQuantity": "0",
    "netAveragePrice": "0.00",
    "uploadPrice": "0.00",
    "netUploadPrice": "0.00",
    "unrealizedMTOM": "0.00",
    "RealizedPNL": "7.85"
  }
}

```

## Developer API Version 1 : Friday 9th May

#### Key Generation

- The generated key validity has been extended to 365 Days.

**Success Response**

- Success response structure has been changed from previous **Connect V4** and current **Developer API V1.**
- A new key has been added to the success response called "message" to all the API in the **Developer API V1.**

**New Success Response (Developer V1)**

```json
{
  "status": "success",
  "message": "API execution information",
  "data": {
        ...
    }
}
```

**Old Success Response (Connect V4)**

```json
{
  "status": "success",
  "data": {
  	...
    }
}
```

#### Order Margin

- There are new key variable added to the success response of order margin - "**marginOnNewOrder**", "**availableMargin**".

**New Success Response (Developer API V1)**

```json
{
  "status": "success",
  "message": "Fetched order margin successfully",
  "data": {
      "availableMargin": "459.71299999999974",
      "cash": "7709",
      "marginOnNewOrder": "780468",
      "remarks": "Insufficient Balance",
      "requestTime": "16:21:04 30-04-2025"
    }
}
```

**Old Success Response (Connect V4)**

```json
{
  "status": "success",
  "data": {
    "requestTime": "14:31:41 15-02-2023",
    "cash": "-141.37",
    "marginused": "523.05",
    "remarks": "Insufficient Balance"
  }
}
```

#### Cancel Order

- There is a new key variable added to the success response of cancel order - "**rejreason**".

**New Success Response (Developer API V1)**

```json
{
   "status": "success",
   "message": "Order cancellation details",
   "data": {
      "orderNumber": "25042100011119",
      "rejreason": "SAF:order is not open to cancel",
      "requestTime": "17:59:57 21-04-2025"
   }
}
```

**Old Success Response (Connect V4)**

```json
{
  "status": "success",
  "data": {
    "requestTime": "14:45:38 15-02-2023",
    "orderNumber": "1234567890111"
	}
}
```

#### Modify Order

- There are new key variables added to the request of the modify order - **"retention", "mkt_protection".**

**New Request (Developer API V1)**

```json
{
  "userId": "{{userId}}",
  "jKey": "{{jKey}}",
  "orderNumber": "25042100011120",
  "priceType": "LMT",
  "tradingSymbol": "IDEA-EQ",
  "price": "418",
  "triggerPrice": "0",
  "quantity": "1",
  "product": "C",
  "retention": "DAY",
  "mkt_protection": "0.5"
}
```

**Old Request (Connect V4)**

```json
{
    "userId": "{{userID}}",
    "exchange": "NSE",
    "quantity": "250",
    "price": "413",
    "triggerPrice": "0",
    "orderNumber": "",
    "tradingSymbol": "",
    "priceType": "LMT",
    "jKey": "{{jKey}}"
}
```

- There is a new key variable added to the success response of modify order - "rejreason".

**New Success Response (V1)**

```json
{
  "status": "success",
  "message": "Order modification details",
  "data": {
    "orderNumber": "25042100011120",
    "rejreason": "SAF:order is not open to modify",
    "requestTime": "18:07:09 21-04-2025"
  }
}
```

**Old Success Response (V4)**

```json
{
  "status": "success",
  "data": {
    "requestTime": "14:45:38 15-02-2023",
    "orderNumber": "1234567890111"
  }
}
```

#### Single Order History

- There is a new key variable added to the success response of Single order History - "**reportType**", "**exchangeTime**", "**exchangeOrderNum**"

**New Success Response (V1)**

```json
{
    "status": "success",
    "message": "Order history data received",
    "data": [
        {
            "averagePrice": "0.00",
            "exchange": "NFO",
            "exchangeOrderNum": "1400000007552574",
            "exchangeTime": "07-May-2025 09:30:33",
            "fillShares": "0",
            "orderNumber": "25050700001776",
            "orderTime": "09:30:33 07-05-2025",
            "price": "190.00",
            "priceType": "LMT",
            "product": "M",
            "quantity": "750",
            "rejectReason": " ",
            "remarks": "Mobile App Order",
            "reportType": "Cancelled",
            "retention": "DAY",
            "status": "CANCELED",
            "tickSize": "0.05",
            "token": "38605",
            "tradingSymbol": "NIFTY08MAY25P24350",
            "transactionType": "S",
            "userId": "TV0001"
        }
        {
            "averagePrice": "0.00",
            "exchange": "NFO",
            "exchangeOrderNum": "",
            "exchangeTime": "01-Jan-1970 05:30:00",
            "fillShares": "0",
            "orderNumber": "25050700001776",
            "orderTime": "09:22:08 07-05-2025",
            "price": "190.00",
            "priceType": "LMT",
            "product": "M",
            "quantity": "750",
            "rejectReason": " ",
            "remarks": "Mobile App Order",
            "reportType": "Pending New",
            "retention": "DAY",
            "status": "PENDING",
            "tickSize": "0.05",
            "token": "38605",
            "tradingSymbol": "NIFTY08MAY25P24350",
            "transactionType": "S",
            "userId": "TV0001"
        },
        {
            "averagePrice": "0.00",
            "exchange": "NFO",
            "exchangeOrderNum": "",
            "exchangeTime": "01-Jan-1970 05:30:00",
            "fillShares": "0",
            "orderNumber": "25050700001776",
            "orderTime": "09:22:08 07-05-2025",
            "price": "190.00",
            "priceType": "LMT",
            "product": "M",
            "quantity": "750",
            "rejectReason": " ",
            "remarks": "Mobile App Order",
            "reportType": "New Ack",
            "retention": "DAY",
            "status": "OPEN",
            "tickSize": "0.05",
            "token": "38605",
            "tradingSymbol": "NIFTY08MAY25P24350",
            "transactionType": "S",
            "userId": "TV0001"
        }
      ]
  }
```

**Old Success Response (V4)**

```json
{
  "status": "success",
    "data": [
    {
      "userId": "AA0011",
      "orderNumber": "1234567890111",
      "exchange": "NSE",
      "tradingSymbol": "ITC-EQ",
      "quantity": "1",
      "transactionType": "B",
      "priceType": "LMT",
      "retention": "DAY",
      "token": "1660",
      "lotSize": "1",
      "tickSize": "0.05",
      "price": "0.00",
      "product": "M",
      "status": "REJECTED",
      "orderTime": "14:45:11 15-02-2023",
      "fillShares": "",
      "averagePrice": "",
      "remarks": "singleOrderHistory",
      "rejectReason": "ORA:Product Regular not enabled on exchange NSE"
    }
  ]
}
```

#### Product Conversion

- "Message" key is newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
        {
          "status": "success",
          "message": "Partial position conversion info fetched",
          "data": {
            "Status": "RED:Product Conversions are disallowed after system square off",
            "requestTime": "18:27:50 21-04-2025"
          }
    }

```

**Old Success Response (V4)**

```json
      {
  "status": "success",
  "data": {
    "requestTime": " "17:38:34 17-02-2023"",
    "status": "ok"
  }
}

```

#### Holdings

- In newer version, each item in data contains only two keys: "**exchange**" and "**tradingSymbol**", in older version we used exchangeTradingSymbol, sellAmount, tradeQuantity, usedQuantity, BTSTQuantity, uploadPrice, holdQuantity

**New Success Response (V1)**

```json
       {
          "status": "success",
          "message": "Fetched holdings",
          "data": [
          {
            "exchange": "BSE",
            "tradingSymbol": "INDINFO"
          },
          {
            "exchange": "NSE",
            "tradingSymbol": "VIKASECO-EQ"
          },
          {
            "exchange": "BSE",
            "tradingSymbol": "VIKASECO"
          }
        ]
    }

```

**Old Success Response (V4)**

```json
      {
  "status": "success",
  "data": [
      {
          "exchangeTradingSymbol": [
              {
                  "exchange": "NSE",
                  "token": "11184",
                  "tradingSymbol": "IDFCFIRSTB-EQ",
                  "pricePrecision": "2",
                  "tickSize": "0.05",
                  "lotSize": "1"
              },
              {
                  "exchange": "BSE",
                  "token": "539437",
                  "tradingSymbol": "IDFCFIRSTB",
                  "pricePrecision": "2",
                  "tickSize": "0.05",
                  "lotSize": "1"
              }
          ],
          "sellAmount": "0.000000",
          "holdQuantity": "0",
          "uploadPrice": "58.50",
          "BTSTQuantity": "0",
          "usedQuantity": "0",
          "tradeQuantity": "0"
      },
      {
          "exchangeTradingSymbol": [
              {
                  "exchange": "NSE",
                  "token": "1660",
                  "tradingSymbol": "ITC-EQ",
                  "pricePrecision": "2",
                  "tickSize": "0.05",
                  "lotSize": "1"
              },
              {
                  "exchange": "BSE",
                  "token": "500875",
                  "tradingSymbol": "ITC",
                  "pricePrecision": "2",
                  "tickSize": "0.05",
                  "lotSize": "1"
              }
          ],
          "sellAmount": "0.000000",
          "holdQuantity": "0",
          "uploadPrice": "349.25",
          "BTSTQuantity": "0",
          "usedQuantity": "0",
          "tradeQuantity": "0"
      },
      {
          "exchangeTradingSymbol": [
              {
                  "exchange": "NSE",
                  "token": "827",
                  "tradingSymbol": "DEEPAKFERT-EQ",
                  "pricePrecision": "2",
                  "tickSize": "0.05",
                  "lotSize": "1"
              },
              {
                  "exchange": "BSE",
                  "token": "500645",
                  "tradingSymbol": "DEEPAKFERT",
                  "pricePrecision": "2",
                  "tickSize": "0.05",
                  "lotSize": "1"
              }
          ],
          "sellAmount": "0.000000",
          "holdQuantity": "0",
          "uploadPrice": "1027.55",
          "BTSTQuantity": "0",
          "usedQuantity": "0",
          "tradeQuantity": "0"
      }
  ]
}

```

#### Limit

- "Message", "**availableMargin**"" key is newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
       {
          "status": "success",
          "message": "Successfully fetched RMS limits",
          "data": {
            "availableMargin": "2.49",
            "brkcollamt": "0.00",
            "cash": "5.60",
            "collateral": "0.00",
            "expo": "0.00",
            "marginused": "71.49",
            "payin": "0.00",
            "peak_mar": "0.00",
            "premium": "0.00",
            "requestTime": "17:14:15 30-04-2025",
            "span": "0.00"
        }
  }

```

**Old Success Response (V4)**

```json
      {
  "status": "success",
  "data": {
      "requestTime": "15:50:24 15-02-2023",
      "cash": "-142.37",
      "payin": "0.00",
      "marginused": "0.00",
      "brkcollamt": "0.00",
      "peak_mar": "0.00",
      "span": "0.00",
      "expo": "0.00",
      "premium": "0.00",
      "collateral": "0.00"
  }
}

```

#### Basket Margin

- "Message" "**BasketMargin**", "**MarginOnNewOrder**", "**PreviousMargin**" key is newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
       {
          "status": "success",
          "message": "Fetched basket margin successfully",
          "data": {
            "BasketMargin": [
              126075.6,
              126783.0242,
              2
            ],
            "MarginOnNewOrder": 126783.0242,
            "PreviousMargin": 0,
            "Remarks": "",
            "TradedMargin": 126783.0242
          }
    }

```

**Old Success Response (V4)**

```json
      {
  "status": "success",
  "data": {
      "request_time": "18:00:27 16-02-2023",
      "stat": "Ok",
      "marginused": "19150.45",
      "marginusedtrade": "22.95",
      "remarks": "basketMargin"
  }
}

```

#### Get Security info

- "**Message**", "**priceFactor**", " **companyName**", "**freezeQuantity**" key is newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
       {
    "status": "success",
    "message": "Fetched security info successfully",
    "data": {
        "companyName": "VODAFONE IDEA LIMITED",
        "exchange": "NSE",
        "freezeQuantity": "15059681",
        "instrumentName": "EQ",
        "lotSize": "1",
        "mult": "1",
        "priceFactor": "(1 / 1 ) * (1 / 1)",
        "pricePrecision": "2",
        "segment": "EQT",
        "symbolName": "IDEA",
        "tickSize": "1.00",
        "token": "14366",
        "tradingSymbol": "IDEA-EQ"
    }
}

```

**Old Success Response (V4)**

```json
       {
  "status": "success",
  "data": {
      "exchange": "NSE",
      "tradingSymbol": "ACC-EQ",
      "symbolName": "ACC",
      "companyName": "ACC LIMITED",
      "instrumentName": "EQ",
      "segment": "EQT",
      "pricePrecision": "2",
      "lotSize": "1",
      "tickSize": "0.05",
      "mult": "1",
      "prcftr_d": "(1 / 1 ) * (1 / 1)",
      "token": "22"
  }
}

```

#### Get Quote

- "**Message**", "**data**" is in array, "**instrumentName**", "**segment**", "**symbolName**" keys are newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
       {
          "status": "success",
          "message": "Quote data retrieved successfully",
          "data": [
          {
            "VWAP": "0.00",
            "bestBuyOrder1": "0",
            "bestBuyOrder2": "0",
            "bestBuyOrder3": "0",
            "bestBuyOrder4": "0",
            "bestBuyOrder5": "0",
            "bestBuyPrice1": "0.00",
            "bestBuyPrice2": "0.00",
            "bestBuyPrice3": "0.00",
            "bestBuyPrice4": "0.00",
            "bestBuyPrice5": "0.00",
            "bestBuyQuantity1": "0",
            "bestBuyQuantity2": "0",
            "bestBuyQuantity3": "0",
            "bestBuyQuantity4": "0",
            "bestBuyQuantity5": "0",
            "bestSellOrder1": "0",
            "bestSellOrder2": "0",
            "bestSellOrder3": "0",
            "bestSellOrder4": "0",
            "bestSellOrder5": "0",
            "bestSellPrice1": "0.00",
            "bestSellPrice2": "0.00",
            "bestSellPrice3": "0.00",
            "bestSellPrice4": "0.00",
            "bestSellPrice5": "0.00",
            "bestSellQuantity1": "0",
            "bestSellQuantity2": "0",
            "bestSellQuantity3": "0",
            "bestSellQuantity4": "0",
            "bestSellQuantity5": "0",
            "companyName": "Nifty 50",
            "dayClosePrice": "2412555",
            "dayHighPrice": "2420165",
            "dayLowPrice": "2407200",
            "dayOpenPrice": "2418540",
            "exchange": "NSE",
            "lastTradedPrice": "2417780",
            "lotSize": "1",
            "multipler": "1",
            "openInterest": "0.00",
            "priceFactor": "(1 / 1 ) * (1 / 1)",
            "pricePrecision": "2",
            "requestTime": "04:08:13 22-04-2025",
            "segment": "Indices",
            "symbolName": "NIFTY",
            "tickSize": "0.05",
            "token": "26000",
            "totalBuyQuantity": "0",
            "totalSellQuantity": "0",
            "tradingSymbol": "NIFTY"
          }
        ]
    }

```

**Old Success Response (V4)**

```json
      {
    "status": "success",
    "data": {
        "requestTime": "01:05:45 05-02-2024",
        "companyName": "ITC LTD",
        "exchange": "NSE",
        "tradingSymbol": "ITC-EQ",
        "symbolName": "ITC",
        "segment": "EQT",
        "instrumentName": "EQ",
        "pricePrecision": "2",
        "lotSize": "1",
        "tickSize": "0.05",
        "multipler": "1",
        "priceFactor": "(1 / 1 ) * (1 / 1)",
        "token": "1660",
        "lastTradedPrice": "472.30",
        "dayClosePrice": "440.10",
        "dayOpenPrice": "444.00",
        "isin": "INE154A01025",
        "upperCircuit": "506.10",
        "lowerCircuit": "396.10",
        "dayHighPrice": "506.10",
        "dayLowPrice": "396.10",
        "volume": "6836353",
        "lastTradedQuantity": "3",
        "lastTradeTime": "15:42:13",
        "bestBuyPrice1": "0.00",
        "bestBuyPrice2": "0.00",
        "bestBuyPrice3": "0.00",
        "bestBuyPrice4": "0.00",
        "bestBuyPrice5": "0.00",
        "bestSellPrice1": "472.30",
        "bestSellPrice2": "0.00",
        "bestSellPrice3": "0.00",
        "bestSellPrice4": "0.00",
        "bestSellPrice5": "0.00",
        "bestBuyQuantity1": "0",
        "bestBuyQuantity2": "0",
        "bestBuyQuantity3": "0",
        "bestBuyQuantity4": "0",
        "bestBuyQuantity5": "0",
        "bestSellQuantity1": "146",
        "bestSellQuantity2": "0",
        "bestSellQuantity3": "0",
        "bestSellQuantity4": "0",
        "bestSellQuantity5": "0",
        "bestSellOrder1": "2",
        "bestSellOrder2": "0",
        "bestSellOrder3": "0",
        "bestSellOrder4": "0",
        "bestSellOrder5": "0",
        "bestBuyOrder1": "0",
        "bestBuyOrder2": "0",
        "bestBuyOrder3": "0",
        "bestBuyOrder4": "0",
        "bestBuyOrder5": "0",
        "VWAP": "455.00",
        "totalSellQuantity": "146",
        "openInterest": "0.00",
        "totalBuyQuantity": "0"
    }
}

```

#### Get Multi Quote

- "**openInterest**", "**VWAP**", "**dayClosePrice**", "**dayOpenPrice**" keys are newly added and visible in the newer version of the response, and no "result" nesting here.

**New Success Response (V1)**

```json
       {
          "status": "success",
          "message": "Multiple quotes data retrieved successfully",
          "data": [
          {
              "VWAP": "0.00",
              "bestBuyOrder1": "0",
              "bestBuyOrder2": "0",
              "bestBuyOrder3": "0",
              "bestBuyOrder4": "0",
              "bestBuyOrder5": "0",
              "bestBuyPrice1": "0.00",
              "bestBuyPrice2": "0.00",
              "bestBuyPrice3": "0.00",
              "bestBuyPrice4": "0.00",
              "bestBuyPrice5": "0.00",
              "bestBuyQuantity1": "0",
              "bestBuyQuantity2": "0",
              "bestBuyQuantity3": "0",
              "bestBuyQuantity4": "0",
              "bestBuyQuantity5": "0",
              "bestSellOrder1": "0",
              "bestSellOrder2": "0",
              "bestSellOrder3": "0",
              "bestSellOrder4": "0",
              "bestSellOrder5": "0",
              "bestSellPrice1": "0.00",
              "bestSellPrice2": "0.00",
              "bestSellPrice3": "0.00",
              "bestSellPrice4": "0.00",
              "bestSellPrice5": "0.00",
              "bestSellQuantity1": "0",
              "bestSellQuantity2": "0",
              "bestSellQuantity3": "0",
              "bestSellQuantity4": "0",
              "bestSellQuantity5": "0",
              "companyName": "Nifty 50",
              "dayClosePrice": "24335.95",
              "dayHighPrice": "24396.15",
              "dayLowPrice": "24198.75",
              "dayOpenPrice": "24342.05",
              "exchange": "NSE",
              "identifier": "NSE:NIFTY",
              "instrumentName": "",
              "lastTradedPrice": "24334.20",
              "lotSize": "1",
              "multipler": "1",
              "openInterest": "0.00",
              "priceFactor": "(1 / 1 ) * (1 / 1)",
              "pricePrecision": "2",
              "requestTime": "17:44:35 30-04-2025",
              "segment": "Indices",
              "symbolName": "NIFTY",
              "tickSize": "0.05",
              "token": "26000",
              "totalBuyQuantity": "0",
              "totalSellQuantity": "0",
              "tradingSymbol": "NIFTY"
          },
          {
              "VWAP": "0.00",
              "bestBuyOrder1": "0",
              "bestBuyOrder2": "0",
              "bestBuyOrder3": "0",
              "bestBuyOrder4": "0",
              "bestBuyOrder5": "0",
              "bestBuyPrice1": "0.00",
              "bestBuyPrice2": "0.00",
              "bestBuyPrice3": "0.00",
              "bestBuyPrice4": "0.00",
              "bestBuyPrice5": "0.00",
              "bestBuyQuantity1": "0",
              "bestBuyQuantity2": "0",
              "bestBuyQuantity3": "0",
              "bestBuyQuantity4": "0",
              "bestBuyQuantity5": "0",
              "bestSellOrder1": "0",
              "bestSellOrder2": "0",
              "bestSellOrder3": "0",
              "bestSellOrder4": "0",
              "bestSellOrder5": "0",
              "bestSellPrice1": "0.00",
              "bestSellPrice2": "0.00",
              "bestSellPrice3": "0.00",
              "bestSellPrice4": "0.00",
              "bestSellPrice5": "0.00",
              "bestSellQuantity1": "0",
              "bestSellQuantity2": "0",
              "bestSellQuantity3": "0",
              "bestSellQuantity4": "0",
              "bestSellQuantity5": "0",
              "companyName": "NIFTY 28 29JUN 39000 P",
              "dayClosePrice": "0.05",
              "exchange": "NFO",
              "identifier": "NFO:NIFTY28JUN29P39000",
              "instrumentName": "OPTIDX",
              "lastTradedPrice": "0.05",
              "lotSize": "1",
              "multipler": "1",
              "openInterest": "0.00",
              "priceFactor": "(1 / 1 ) * (1 / 1)",
              "pricePrecision": "2",
              "requestTime": "17:44:35 30-04-2025",
              "segment": "Options",
              "symbolName": "NIFTY28JUN29P39000",
              "tickSize": "0.05",
              "token": "89665",
              "totalBuyQuantity": "0",
              "totalSellQuantity": "0",
              "tradingSymbol": "NIFTY28JUN29P39000"
          }
        ]
    }

```

**Old Success Response (V4)**

```json
      {
    "status": "success",
    "data": [
        {
            "token": "26000",
            "result": {
                "requestTime": "12:26:55 18-03-2023",
                "companyName": "NIFTY INDEX",
                "exchange": "NSE",
                "tradingSymbol": "Nifty 50",
                "symbolName": "NIFTY",
                "segment": "EQT",
                "instrumentName": "UNDIND",
                "pricePrecision": "2",
                "lotSize": "1",
                "tickSize": "0.05",
                "multipler": "1",
                "priceFactor": "(1 / 1 ) * (1 / 1)",
                "token": "26000",
                "lastTradedPrice": "17314.75",
                "company": "17100.05",
                "upperCircuit": "0.00",
                "lowerCircuit": "0.00",
                "dayHighPrice": "17745.60",
                "dayLowPrice": "16921.35",
                "volume": "0.00",
                "lastTradedQuantity": "0.00",
                "lastTradeTime": "0.00",
                "bestBuyPrice1": "0.00",
                "bestBuyPrice2": "0.00",
                "bestBuyPrice3": "0.00",
                "bestBuyPrice4": "0.00",
                "bestBuyPrice5": "0.00",
                "bestSellPrice1": "0.00",
                "bestSellPrice2": "0.00",
                "bestSellPrice3": "0.00",
                "bestSellPrice4": "0.00",
                "bestSellPrice5": "0.00",
                "bestBuyQuantity1": "0.00",
                "bestBuyQuantity2": "0.00",
                "bestBuyQuantity3": "0.00",
                "bestBuyQuantity4": "0.00",
                "bestBuyQuantity5": "0.00",
                "bestSellQuantity1": "0.00",
                "bestSellQuantity2": "0.00",
                "bestSellQuantity3": "0.00",
                "bestSellQuantity4": "0.00",
                "bestSellQuantity5": "0.00",
                "bestSellOrder1": "0.00",
                "bestSellOrder2": "0.00",
                "bestSellOrder3": "0.00",
                "bestSellOrder4": "0.00",
                "bestSellOrder5": "0.00",
                "bestBuyOrder1": "0.00",
                "bestBuyOrder2": "0.00",
                "bestBuyOrder3": "0.00",
                "bestBuyOrder4": "0.00",
                "bestBuyOrder5": "0.00"
            }
        }
    ]
}

```

#### Get Multi Quote Ltp

- "**Message**", "**identifier**", "**tradingSymbol**" keys are newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
       {
          "status": "success",
          "message": "Multiple quotes LTP data retrieved successfully",
          "data": [
          {
            "companyName": "RELIANCE INDUSTRIES LTD",
            "exchange": "NSE",
            "identifier": "NSE:RELIANCE-EQ",
            "lastTradedPrice": "1300.00",
            "requestTime": "09:13:20 22-04-2025",
            "token": 2885,
            "tradingSymbol": "RELIANCE-EQ"
          },
          {
            "companyName": "VODAFONE IDEA LIMITED",
            "exchange": "NSE",
            "identifier": "NSE:IDEA-EQ",
            "lastTradedPrice": "8.08",
            "requestTime": "09:13:20 22-04-2025",
            "token": 14366,
            "tradingSymbol": "IDEA-EQ"
          }
        ]
    }

```

**Old Success Response (V4)**

```json
      {
    "status": "success",
    "data": [
        {
            "token": "26000",
            "result": {
                "requestTime": "12:29:12 18-03-2023",
                "companyName": "NIFTY INDEX",
                "exchange": "NSE",
                "token": "26000",
                "lastTradedPrice": "17438.65"
            }
        }
    ]
}

```

#### Index List

- "**symbol**", "**tradingSymbol**","**exchange**" keys are newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
       {
          "status": "success",
          "message": "All indexes",
          "data": [
          {
            "exchange": "NSE",
            "token": "26000",
            "tradingSymbol": "NIFTY",
            "symbol": "NIFTY",
            "idxname": "NIFTY 50"
          },
          {
            "exchange": "NSE",
            "token": "26009",
            "tradingSymbol": "BANKNIFTY",
            "symbol": "BANKNIFTY",
            "idxname": "NIFTY BANK"
          },
          {
            "exchange": "BSE",
            "token": "1",
            "tradingSymbol": "SENSEX",
            "symbol": "SENSEX",
            "idxname": "SENSEX"
          }
        ]
    }

```

**Old Success Response (V4)**

```json
     {
  "status": "success",
  "data": {
      "requestTime": "12:04:58 16-02-2023",
      "values": [
          {
              "idxname": "HangSeng BeES-NAV",
              "token": "26016"
          },
          {
              "idxname": "India VIX",
              "token": "26017"
          },
          {
              "idxname": "Nifty 50",
              "token": "26000"
          },
          {
              "idxname": "Nifty IT",
              "token": "26008"
          },
          {
              "idxname": "Nifty Next 50",
              "token": "26013"
          },
          {
              "idxname": "Nifty Bank",
              "token": "26009"
          },
          {
              "idxname": "Nifty 500",
              "token": "26004"
          },
          {
              "idxname": "Nifty 100",
              "token": "26012"
          },
          {
              "idxname": "Nifty Midcap 50",
              "token": "26014"
          },
          {
              "idxname": "Nifty Realty",
              "token": "26018"
          },
          {
              "idxname": "Nifty Infra",
              "token": "26019"
          },
          {
              "idxname": "Nifty Energy",
              "token": "26020"
          },
          {
              "idxname": "Nifty FMCG",
              "token": "26021"
          },
          {
              "idxname": "Nifty MNC",
              "token": "26022"
          },
          {
              "idxname": "Nifty Pharma",
              "token": "26023"
          },
          {
              "idxname": "Nifty PSE",
              "token": "26024"
          },
          {
              "idxname": "Nifty PSU Bank",
              "token": "26025"
          },
          {
              "idxname": "Nifty Serv Sector",
              "token": "26026"
          },
          {
              "idxname": "Nifty Auto",
              "token": "26029"
          },
          {
              "idxname": "Nifty Metal",
              "token": "26030"
          },
          {
              "idxname": "Nifty Media",
              "token": "26031"
          },
          {
              "idxname": "Nifty 200",
              "token": "26033"
          },
          {
              "idxname": "Nifty Div Opps 50",
              "token": "26034"
          },
          {
              "idxname": "Nifty Commodities",
              "token": "26035"
          },
          {
              "idxname": "Nifty Consumption",
              "token": "26036"
          },
          {
              "idxname": "Nifty Fin Service",
              "token": "26037"
          },
          {
              "idxname": "Nifty50 Div Point",
              "token": "26038"
          },
          {
              "idxname": "Nifty100 Liq 15",
              "token": "26040"
          },
          {
              "idxname": "Nifty CPSE",
              "token": "26041"
          },
          {
              "idxname": "Nifty GrowSect 15",
              "token": "26001"
          },
          {
              "idxname": "Nifty50 PR 2x Lev",
              "token": "26002"
          },
          {
              "idxname": "Nifty50 PR 1x Inv",
              "token": "26042"
          },
          {
              "idxname": "Nifty50 TR 2x Lev",
              "token": "26043"
          },
          {
              "idxname": "Nifty50 TR 1x Inv",
              "token": "26044"
          },
          {
              "idxname": "Nifty50 Value 20",
              "token": "26045"
          },
          {
              "idxname": "Nifty Mid Liq 15",
              "token": "26046"
          },
          {
              "idxname": "Nifty Pvt Bank",
              "token": "26047"
          },
          {
              "idxname": "NIFTY100 Qualty30",
              "token": "26048"
          },
          {
              "idxname": "NIFTY MIDCAP 100",
              "token": "26011"
          },
          {
              "idxname": "NIFTY SMLCAP 100",
              "token": "26032"
          },
          {
              "idxname": "Nifty GS 8 13Yr",
              "token": "26049"
          },
          {
              "idxname": "Nifty GS 10Yr",
              "token": "26050"
          },
          {
              "idxname": "Nifty GS 10Yr Cln",
              "token": "26051"
          },
          {
              "idxname": "Nifty GS 4 8Yr",
              "token": "26052"
          },
          {
              "idxname": "Nifty GS 11 15Yr",
              "token": "26053"
          },
          {
              "idxname": "Nifty GS 15YrPlus",
              "token": "26054"
          },
          {
              "idxname": "Nifty GS Compsite",
              "token": "26055"
          },
          {
              "idxname": "NIFTY50 EQL Wgt",
              "token": "26056"
          },
          {
              "idxname": "NIFTY100 EQL Wgt",
              "token": "26057"
          },
          {
              "idxname": "NIFTY100 LowVol30",
              "token": "26058"
          },
          {
              "idxname": "NIFTY Alpha 50",
              "token": "26059"
          },
          {
              "idxname": "NIFTY MIDCAP 150",
              "token": "26060"
          },
          {
              "idxname": "NIFTY SMLCAP 50",
              "token": "26061"
          },
          {
              "idxname": "NIFTY SMLCAP 250",
              "token": "26062"
          },
          {
              "idxname": "NIFTY MIDSML 400",
              "token": "26063"
          },
          {
              "idxname": "NIFTY200 QUALTY30",
              "token": "26064"
          },
          {
              "idxname": "Nifty FinSrv25 50",
              "token": "26065"
          },
          {
              "idxname": "NIFTY AlphaLowVol",
              "token": "26066"
          },
          {
              "idxname": "Nifty200Momentm30",
              "token": "26067"
          },
          {
              "idxname": "Nifty100ESGSecLdr",
              "token": "26068"
          },
          {
              "idxname": "NIFTY HEALTHCARE",
              "token": "26069"
          },
          {
              "idxname": "NIFTY CONSR DURBL",
              "token": "26070"
          },
          {
              "idxname": "NIFTY OIL AND GAS",
              "token": "26071"
          },
          {
              "idxname": "NIFTY500 MULTICAP",
              "token": "26072"
          },
          {
              "idxname": "NIFTY LARGEMID250",
              "token": "26073"
          },
          {
              "idxname": "NIFTY MID SELECT",
              "token": "26074"
          },
          {
              "idxname": "NIFTY TOTAL MKT",
              "token": "26075"
          },
          {
              "idxname": "NIFTY MICROCAP250",
              "token": "26076"
          },
          {
              "idxname": "NIFTY IND DIGITAL",
              "token": "26077"
          },
          {
              "idxname": "NIFTY100 ESG",
              "token": "26078"
          },
          {
              "idxname": "NIFTY M150 QLTY50",
              "token": "26079"
          },
          {
              "idxname": "NIFTY INDIA MFG",
              "token": "26080"
          }
      ]
  }
}

```

#### Option Chain

- "**Message**","**parentToken**",**"lastTradedPrice"** keys are newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
      {
          "status": "success",
          "message": "Option chain data retrieved successfully",
          "data": [
          {
            "exchange": "NFO",
            "lotSize": "75",
            "optionType": "CE",
            "parentToken": "26000",
            "pricePrecision": "2",
            "strikePrice": "22950.00",
            "tickSize": "0.05",
            "token": "79424",
            "tradingSymbol": "NIFTY24APR25C22950",
            "lastTradedPrice": "130.00"
          },
          {
            "exchange": "NFO",
            "lotSize": "75",
            "optionType": "PE",
            "parentToken": "26000",
            "pricePrecision": "2",
            "strikePrice": "23400.00",
            "tickSize": "0.05",
            "token": "79489",
            "tradingSymbol": "NIFTY24APR25P23400",
            "lastTradedPrice": "130.00"
          }
        ]
    }

```

**Old Success Response (V4)**

```json
      {
  "status": "success",
  "data": {
    "requestTime": "13:25:51 24-08-2022""values": [
      {
        "exchange": "NFO",
        "token": "48831",
        "tradingSymbol": "NIFTY19JAN23C20050",
        "optionType": "CE",
        "pricePrecision": "2",
        "lotSize": "25",
        "tickSize": "0.05",
        "strikePrice": "35500.00"
      },
      {
        "exchange": "NFO",
        "token": "48834",
        "tradingSymbol": "NIFTY19JAN23C20050",
        "optionType": "CE",
        "pricePrecision": "2",
        "lotSize": "25",
        "tickSize": "0.05",
        "strikePrice": "35600.00"
      }
    ]
  }
}

```

#### Search Scrips

- "**Message**","**representationName**" keys are newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
     {
          "status": "success",
          "message": "Search symbols",
          "data": [
          {
            "token": "1660",
            "exchange": "NSE",
            "companyName": "ITC LTD",
            "representationName": "ITC",
            "instrumentName": "Equity",
            "tradingSymbol": "ITC-EQ"
          },
          {
            "token": "29251",
            "exchange": "NSE",
            "companyName": "ITC HOTELS LIMITED",
            "representationName": "ITCHOTELS",
            "instrumentName": "Equity",
            "tradingSymbol": "ITCHOTELS-EQ"
          },
          {
            "token": "500875",
            "exchange": "BSE",
            "companyName": "ITC LTD.",
            "representationName": "ITC",
            "instrumentName": "Equity",
            "tradingSymbol": "ITC"
          },
          {
            "token": "96871",
            "exchange": "NFO",
            "companyName": "Monthly",
            "representationName": "ITC APR 425 CE",
            "instrumentName": "Options",
            "tradingSymbol": "ITC APR 425 CE"
          }
        ]
    }

```

**Old Success Response (V4)**

```json
      {
  "status": "success",
  "values": [
      {
          "exchange": "NSE",
          "tradingSymbol": "MUTHOOTFIN-EQ",
          "token": "23650",
          "companyName": "MUTHOOT FINANCE LIMITED",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MUTHOOTCAP-EQ",
          "token": "10415",
          "companyName": "MUTHOOT CAP SERV LTD",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MURUDCERA-EQ",
          "token": "2313",
          "companyName": "MURUDESHWAR CERAMICS LTD",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MUNJALSHOW-EQ",
          "token": "2307",
          "companyName": "MUNJAL SHOWA LTD",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MUNJALAU-EQ",
          "token": "13511",
          "companyName": "MUNJAL AUTO IND. LTD.",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MUKTAARTS-EQ",
          "token": "8687",
          "companyName": "MUKTA ARTS LIMITED",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MUKANDLTD-EQ",
          "token": "11325",
          "companyName": "MUKAND LTD.",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MTNL-EQ",
          "token": "2294",
          "companyName": "MAHANAGAR TELEPHONE NIGAM",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MTEDUCARE-BE",
          "token": "31413",
          "companyName": "MT EDUCARE LTD",
          "instrumentName": "BE",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MTARTECH-EQ",
          "token": "2709",
          "companyName": "MTAR TECHNOLOGIES LIMITED",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MSUMI-EQ",
          "token": "8596",
          "companyName": "MOTHERSON SUMI WRNG IND L",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MSTCLTD-EQ",
          "token": "9356",
          "companyName": "MSTC LIMITED",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MSPL-EQ",
          "token": "11919",
          "companyName": "MSP STEEL & POWER LTD.",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MRPL-EQ",
          "token": "2283",
          "companyName": "MRPL",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MRO-TEK-EQ",
          "token": "8998",
          "companyName": "MRO-TEK REALTY LIMITED",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MRF-EQ",
          "token": "2277",
          "companyName": "MRF LTD",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MPSLTD-EQ",
          "token": "10578",
          "companyName": "MPS LIMITED",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MPHASIS-EQ",
          "token": "4503",
          "companyName": "MPHASIS LIMITED",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MOVALUE-EQ",
          "token": "10825",
          "companyName": "MOTILALAMC - MOVALUE",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.01"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MOTOGENFIN-EQ",
          "token": "2268",
          "companyName": "MOTOR & GENERAL FINANCE L",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MOTILALOFS-EQ",
          "token": "14947",
          "companyName": "MOTILAL OSWAL FIN LTD",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MOTHERSON-EQ",
          "token": "4204",
          "companyName": "SAMVRDHNA MTHRSN INTL LTD",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MOREPENLAB-EQ",
          "token": "2259",
          "companyName": "MOREPEN LAB. LTD",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MORARJEE-EQ",
          "token": "28877",
          "companyName": "MORARJEE TEXTILES LIMITED",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.05"
      },
      {
          "exchange": "NSE",
          "tradingSymbol": "MOQUALITY-EQ",
          "token": "10822",
          "companyName": "MOTILALAMC - MOQUALITY",
          "instrumentName": "EQ",
          "pricePrecision": "2",
          "lotSize": "1",
          "tickSize": "0.01"
      }
  ]
}

```

#### Time Price Regular Interval

- "**Message**","**volume**", "**close**", "**low**", "**high**", "**open**", "**epochTime**" keys are newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
     {
          "status": "success",
          "message": "Successfully fetched charts data",
          "data": [
          {
              "time": "00:00:00 23-04-2025",
              "epochTime": 1745346600,
              "open": 24277.9,
              "high": 24347.85,
              "low": 24216.15,
              "close": 24246.7,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 24-04-2025",
              "epochTime": 1745433000,
              "open": 24289,
              "high": 24365.45,
              "low": 23847.85,
              "close": 24039.35,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 25-04-2025",
              "epochTime": 1745519400,
              "open": 24289,
              "high": 24365.45,
              "low": 23847.85,
              "close": 24039.35,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 26-04-2025",
              "epochTime": 1745605800,
              "open": 24289,
              "high": 24365.45,
              "low": 23847.85,
              "close": 24039.35,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 27-04-2025",
              "epochTime": 1745692200,
              "open": 24070.25,
              "high": 24355.1,
              "low": 24054.05,
              "close": 24328.5,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 28-04-2025",
              "epochTime": 1745778600,
              "open": 24370.7,
              "high": 24457.65,
              "low": 24290.75,
              "close": 24335.95,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 29-04-2025",
              "epochTime": 1745865000,
              "open": 24370.7,
              "high": 24457.65,
              "low": 24290.75,
              "close": 24335.95,
              "volume": 0,
              "oi": 0
          }
      ]
    }

```

**Old Success Response (V4)**

```json
     {
  "status": "success",
  "data": [
    {
      "stat": "Ok",
      "time": "25-08-2022 10:59:00",
      "ssboe": "1661405340",
      "into": "2298.05",
      "inth": "2299.20",
      "intl": "2298.00",
      "intc": "2299.20",
      "intvwap": "2299.02",
      "intv": "478",
      "intoi": "0",
      "v": "92740",
      "oi": "0"
    },
    {
      "stat": "Ok",
      "time": "25-08-2022 10:58:00",
      "ssboe": "1661405280",
      "into": "2298.60",
      "inth": "2299.00",
      "intl": "2298.30",
      "intc": "2298.70",
      "intvwap": "2299.02",
      "intv": "326",
      "intoi": "0",
      "v": "92262",
      "oi": "0"
    },
  ]
}

```

#### Time Price Day Interval

- "**Message**","**volume**", "**close**", "**low**", "**high**", "**open**", "**epochTime**" keys are newly added and visible in the newer version of the response

**New Success Response (V1)**

```json
    {
          "status": "success",
          "message": "Successfully fetched charts data",
          "data": [
          {
              "time": "00:00:00 23-04-2025",
              "epochTime": 1745346600,
              "open": 24277.9,
              "high": 24347.85,
              "low": 24216.15,
              "close": 24246.7,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 24-04-2025",
              "epochTime": 1745433000,
              "open": 24289,
              "high": 24365.45,
              "low": 23847.85,
              "close": 24039.35,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 25-04-2025",
              "epochTime": 1745519400,
              "open": 24289,
              "high": 24365.45,
              "low": 23847.85,
              "close": 24039.35,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 26-04-2025",
              "epochTime": 1745605800,
              "open": 24289,
              "high": 24365.45,
              "low": 23847.85,
              "close": 24039.35,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 27-04-2025",
              "epochTime": 1745692200,
              "open": 24070.25,
              "high": 24355.1,
              "low": 24054.05,
              "close": 24328.5,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 28-04-2025",
              "epochTime": 1745778600,
              "open": 24370.7,
              "high": 24457.65,
              "low": 24290.75,
              "close": 24335.95,
              "volume": 0,
              "oi": 0
          },
          {
              "time": "00:00:00 29-04-2025",
              "epochTime": 1745865000,
              "open": 24370.7,
              "high": 24457.65,
              "low": 24290.75,
              "close": 24335.95,
              "volume": 0,
              "oi": 0
          }
      ]
    }

```

**Old Success Response (V4)**

```json
     {
  "status": "success",
  "data": [
    {
      "stat": "Ok",
      "time": "25-08-2022 10:59:00",
      "ssboe": "1661405340",
      "into": "2298.05",
      "inth": "2299.20",
      "intl": "2298.00",
      "intc": "2299.20",
      "intvwap": "2299.02",
      "intv": "478",
      "intoi": "0",
      "v": "92740",
      "oi": "0"
    },
    {
      "stat": "Ok",
      "time": "25-08-2022 10:58:00",
      "ssboe": "1661405280",
      "into": "2298.60",
      "inth": "2299.00",
      "intl": "2298.30",
      "intc": "2298.70",
      "intvwap": "2299.02",
      "intv": "326",
      "intoi": "0",
      "v": "92262",
      "oi": "0"
    },
  ]
}

```

#### Brokerage Calculator

- Additional API in this new version

**New Success Response (V1)**

```json
      {
          "status": "success",
          "message": "Brokerage Data",
          "data": {
            "exchange": "NSE",
            "instrumentName": "UNDIND",
            "lotSize": "1",
            "mult": "1",
            "priceFactor": "(1 / 1 ) * (1 / 1)",
            "pricePrecision": "2",
            "segment": "EQT",
            "symbolName": "NIFTY",
            "tickSize": "0.00",
            "token": "26000",
            "tradingSymbol": "Nifty 50"
          }
    }

```

#### Get Expiry

- Additional API in this new version

**New Success Response (V1)**

```json
      {
          "status": "success",
          "message": "Expiry dates retrieved successfully",
          "data": {
            "expiryDates": [
                "08MAY2025",
                "15MAY2025",
                "22MAY2025",
                "29MAY2025",
                "05JUN2025",
                "26JUN2025",
                "31JUL2025",
                "25SEP2025",
                "24DEC2025",
                "25MAR2026",
                "24JUN2026",
                "30DEC2026",
                "23JUN2027",
                "29DEC2027",
                "29JUN2028",
                "28DEC2028",
                "28JUN2029",
                "27DEC2029"
            ]
        }
    }

```
