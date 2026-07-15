<!-- Source: https://ant.aliceblueonline.com/productdocumentation/portfolio/ -->

# Portfolio

Note

The BASE URL, Endpoint, and Payload JSON key values are case-sensitive. Please use the format which we have given in the documentation.

| Method | API | Detail |
| --- | --- | --- |
| GET | {{BASE_URL}}/open-api/od/v1/holdings/[productType](../Appendix/#holdings-product-type) | Retrieve the list of long-term equity holdings. Possible Values CNC or MTF |
| GET | {{BASE_URL}}/open-api/od/v1/positions | Retrieve the list of short-term positions. |
| POST | {{BASE_URL}}/open-api/od/v1/orders/positions/sqroff | Close an open position by offsetting it with an opposite trade. |
| POST | {{BASE_URL}}/open-api/od/v1/conversion | Conversion of positions. |

## Holdings

Holdings contain the long term equity Holdings of the customer. All the financial instruments in the holdings reside in the customer’s DEMAT account indefinitely until its sold or is delisted or changed by the exchanges. Changes to DEMAT account is settled in T+1 days.

**Response Structure**

```
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "isin": "INE669E01016",
            "nseInstrumentId": "14366",
            "bseInstrumentId": "532822",
            "nseTradingSymbol": "IDEA-EQ",
            "bseTradingSymbol": "IDEA",
            "previousDayClose": 7.17,
            "product": "DELIVERY",
            "formattedInstrumentName": "IDEA",
            "averageTradedPrice": 7.17,
            "collateralQuantity": 0,
            "authorizedQuantity": 0,
            "dpQuantity": 36,
            "totalQuantity": 0,
            "t1Quantity": 0,
            "ltp": 8.12,
            "sellableQty": 2,
            "investedPrice": 8.11
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| isin | String | International Securities Identification Number (ISIN) for the stock. |
| nseInstrumentId | String | Numeric identifier for the instrument on NSE (National Stock Exchange). |
| bseInstrumentId | String | Numeric identifier for the instrument on BSE (Bombay Stock Exchange). |
| nseTradingSymbol | String | Trading symbol/code used on NSE. |
| bseTradingSymbol | String | Trading symbol/code used on BSE. |
| previousDayClose | Float | Closing price of the instrument on the previous trading day. |
| product | String | Category/type of product (e.g., LONGTERM for long-term holdings). |
| formattedInstrumentName | String | Official full name of the instrument. |
| averageTradedPrice | Float | Average price at which the instrument was traded. |
| collateralQuantity | Int | Quantity of the instrument held as collateral. |
| authorizedQuantity | Int | Quantity authorized for trading or holding. |
| dpQuantity | Int | Quantity held in the Depository Participant account. |
| totalQuantity | Int | Total quantity of the instrument held. |
| t1Quantity | Int | Quantity still in the T+1 settlement period. |
| ltp | Float | Last traded price. |
| sellableQty | Int | Quantity avialble to sell. |
| investedPrice | Float | Invested price. |

## Positions

Users can retrieve a list of all open positions for the day. This includes all F&O carryforward positions as well.

**Response Structure**

```
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "instrumentId": "14366",
            "tradingSymbol": "IDEA-EQ",
            "formattedInstrumentName": "IDEA-EQ",
            "exchange": "NSE",
            "product": "CNC",
            "netQuantity": 1,
            "netAveragePrice": 7.69,
            "overnightQuantity": 0,
            "overnightPrice": 0.0,
            "buyQuantity": 1,
            "sellQuantity": 0,
            "daySellQuantity": 0,
            "dayBuyQuantity": 1,
            "dayBuyPrice": 7.69,
            "daySellPrice": 0.0,
            "multiplier": 1,
            "lotsize": 1,
            "ticksize": 0.01,
            "previousDayClose": null,
            "realizedPnl": 0,
            "buyPrice": 0,
            "sellPrice": 0.0,
            "dayBuyValue": 7.69,
            "daySellValue": 0,
            "validity": ""
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| instrumentId | String | Unique identifier of the traded instrument. |
| tradingSymbol | String | Ticker symbol used for trading the instrument. |
| formattedInstrumentName | String | Readable name of the instrument. |
| exchange | String | [Code representing the exchange where the trade is executed.](../Appendix/#exchange) |
| product | String | [Product category of the trade (e.g., INTRADAY, LONGTERM, MTF).](../Appendix/#product-type) |
| netQuantity | Int | Total quantity currently held after netting buy and sell transactions. |
| netAveragePrice | Float | Weighted average price of the net position. |
| overnightQuantity | Int | Quantity carried forward from the previous trading day. |
| overnightPrice | Int | Average price of the overnight quantity. |
| buyQuantity | Int | Total quantity bought. |
| sellQuantity | Int | Total quantity sold. |
| daySellQuantity | Int | Quantity sold during the current trading day. |
| dayBuyQuantity | Int | Quantity bought during the current trading day. |
| dayBuyPrice | Float | Average price of the quantity bought during the day. |
| daySellPrice | Float | Average price of the quantity sold during the day. |
| multiplier | Int | Used to calculate the contract value (generally 1 for equities). |
| lotsize | Int | Minimum quantity allowed per order in the instrument. |
| ticksize | Float | Minimum allowed price movement (e.g., 0.01 means prices change by ₹0.01). |
| previousDayClose | Float | Last closing price of the instrument from the previous trading day. |
| realizedPnl | Float | Profit or loss made from closed (executed and exited) positions. |
| buyPrice | Float | Last traded buy price. |
| sellPrice | Float | Last traded sell price. |
| dayBuyValue | Float | Total value of buy trades executed during the day. |
| daySellValue | Float | Total value of sell trades executed during the day. |
| validity | String | Validity period of the order (e.g., DAY, IOC). |

## Position Square Off

Closing an open position by placing an opposite trade to realize profit or cut loss.

**Request Structure**

```
[
  {
    "exchange": "NSE",
    "symbol": "TCS-EQ",
    "quantity": "75",
    "price": "898",
    "product": "LONGTERM",
    "transactionType": "SELL",
    "orderType": "MKT",
    "triggerPrice": "",
    "ret": "DAY",
    "disclosedQuantity": "",
    "mktProtection": "",
    "target": "",
    "stopLoss": "",
    "trailingStopLoss": "",
    "orderComplexity": "REGULAR",
    "source": "WEB",
    "instrumentId": "22",
    "deviceNumber": "f23fb229a91c43d3"
  }
]
```

**Input parameters**

| Field | Type | Description |
| --- | --- | --- |
| instrumentId | String | Unique identifier assigned to the specific instrument being traded. |
| exchange | String | [Code representing the exchange where the trade is executed.](../Appendix/#exchange) |
| transactionType | String | [Type of transaction, indicating whether the trade is a "BUY" or "SELL".](../Appendix/#transaction-type) |
| quantity | Int | Quantity of the instrument to be traded. |
| orderComplexity | String | [Complexity level of the order (e.g., REGULAR, AMO).](../Appendix/#order-complexity) |
| product | String | [Product category of the trade (e.g., INTRADAY, LONGTERM, MTF).](../Appendix/#product-type) |
| orderType | String | [Price type: Limit, Market, SL, SLM.](../Appendix/#order-type) |
| validity | String | [Validity period of the order (e.g., DAY, IOC).](../Appendix/#validity) |
| price | String | Price specified for the trade; may be ignored for market orders. |
| slTriggerPrice | String | Trigger price for stop-loss orders. |
| trailingSlAmount | String | Amount by which the stop-loss will trail the market price. |
| disclosedQuantity | Int | Portion of the total quantity disclosed to the market. |
| marketProtectionPercent | String | Allowed percentage deviation from the market price to protect from slippage. |
| apiOrderSource | String | Source identifier for API-based orders. |
| algoId | String | Identifier for the algorithm placing the order. |
| orderTag | String | Custom tag to identify or group orders (user-defined). |

**Response Structure**

```
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "requestTime": "17:21:21 26-05-2025",
            "brokerOrderId": "250526000002697"
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| requestTime | String | when the API request was initiated by the client, used for logging, tracking, or validating request timing. |
| brokerOrderId | String | Broker orderId is defined as Unique number it can be generated while placing the order. |

## Position conversion

Convert a position from intraday to delivery or vice versa.

**Request Structure**

```
{
    "exchange": "MCX",
    "validity": "DAY",
    "prevProduct": "MIS",
    "product": "CNC",
    "quantity": "1",
    "tradingSymbol": "SILVER25SEP25C100000",
    "transactionType": "BUY",
    "orderSource": "MOB"
}
```

**Input parameters**

| Field | Type | Description |
| --- | --- | --- |
| exchange | String | [Code representing the exchange where the trade is executed.](../Appendix/#exchange) |
| validity | String | [Validity period of the order (e.g., DAY, IOC).](../Appendix/#validity) |
| prevProduct | String | [Product category of the trade (e.g., MIS, CNC).](../Appendix/#product-type) |
| product | String | [Product category of the trade (e.g., MIS, CNC).](../Appendix/#product-type) |
| quantity | Int | Quantity of the instrument to be traded. |
| tradingSymbol | String | Ticker symbol used for trading the instrument. |
| transactionType | String | [Type of transaction, indicating whether the trade is a "BUY" or "SELL".](../Appendix/#transaction-type) |
| orderSource | String | Source identifier for API-based orders. |

**Response Structure**

```
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "brokerOrderId": "250526000002881",
            "requestTime": "26-May-2025 13:11:34"
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| requestTime | String | when the API request was initiated by the client, used for logging, tracking, or validating request timing. |
| brokerOrderId | String | Order Number is defined as Unique number it can be generated while placing the order. |
