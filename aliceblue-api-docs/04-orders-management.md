# Orders

> Source: https://v2api.aliceblueonline.com/orders%20Management/

> **Note**
>
> The BASE URL, Endpoint, and Payload JSON key values are case-sensitive. Please use the format which we have given in the documentation.

| Type | APIs | Details |
| --- | --- | --- |
| POST | {{BASE_URL}}/open-api/od/v1/orders/placeorder | Place Order submits a buy or sell request for a specific asset. |
| GET | {{BASE_URL}}/open-api/od/v1/orders/book | An Order Book is a real-time record of all buy and sell orders. |
| POST | {{BASE_URL}}/open-api/od/v1/orders/history | Order History is a record of all past buy and sell orders made by a user. |
| POST | {{BASE_URL}}/open-api/od/v1/orders/modify | Modify orders means changing an existing order’s price, quantity, or type. |
| POST | {{BASE_URL}}/open-api/od/v1/orders/cancel | Cancel orders means to revoke or delete a placed order before execution. |
| GET | {{BASE_URL}}/open-api/od/v1/orders/trades | TradeBook records all executed trades with details like price, quantity, and time. |
| POST | {{BASE_URL}}/open-api/od/v1/orders/checkMargin | Single Order Margin provides margin details required for placing a specific order. |
| POST | {{BASE_URL}}/open-api/od/v1/orders/basket/margin | Basket Margin provides margin details for multiple scrips. |
| POST | {{BASE_URL}}/open-api/od/v1/orders/exit/sno | Exit bracket order. |

## Place Order

**Request Structure**

```json
[
    {
        "exchange": "NSE",
        "instrumentId": "22",
        "transactionType": "BUY",
        "quantity": 30,
        "product": "LONGTERM",
        "orderComplexity": "REGULAR",
        "orderType": "LIMIT",
        "validity": "DAY",
        "price": "1120.15",
        "slLegPrice": "1110.00",
        "targetLegPrice": "3333",
        "slTriggerPrice": "11",
        "disclosedQuantity": "",
        "marketProtectionPercent": "",
        "deviceId": "123",
        "trailingSlAmount": "",
        "apiOrderSource": "",
        "algoId": "",
        "orderTag": ""
    }
]
```

**Input parameters**

| Field | Type | Criticality | Description |
| --- | --- | --- | --- |
| instrumentId | String | Required | Unique identifier assigned to the specific instrument being traded. |
| exchange | String | Required | [Code representing the exchange where the trade is executed.](16-appendix.md#exchange) |
| transactionType | String | Required | [Type of transaction, indicating whether the trade is a "BUY" or "SELL".](16-appendix.md#transaction-type) |
| quantity | Int | Required | Quantity of the instrument to be traded. |
| orderComplexity | String | Required | [Complexity level of the order (e.g., REGULAR, AMO).](16-appendix.md#order-complexity) |
| product | String | Required | [Product category of the trade (e.g., INTRADAY, LONGTERM, MTF).](16-appendix.md#product-type) |
| orderType | String | Required | [Price type: Limit, Market, SL, SLM.](16-appendix.md#order-type) |
| validity | String | Required | [Validity period of the order (e.g., DAY, IOC).](16-appendix.md#validity) |
| price | String | Conditionally Required | Price specified for the trade; may be ignored for market orders. |
| slTriggerPrice | String | Conditionally Required | Trigger price for stop-loss orders. |
| trailingSlAmount | String | Optional | Amount by which the stop-loss will trail the market price. |
| disclosedQuantity | Int | Optional | Portion of the total quantity disclosed to the market. |
| marketProtectionPercent | String | Optional | Allowed percentage deviation from the market price to protect from slippage. |
| apiOrderSource | String | Optional | Source identifier for API-based orders. |
| algoId | String | Optional | Identifier for the algorithm placing the order. |
| orderTag | String | Optional | Custom tag to identify or group orders (user-defined). |
| slLegPrice | String | Optional | Stop-loss price for the leg in a multi-leg order. |
| targetLegPrice | String | Optional | Target price for the leg in a multi-leg order. |
| deviceId | String | Optional | Identifier of the device placing the order (used for tracking or analytics). |

**Response Structure**

```json
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "requestTime": "26-May-2025 11:42:10",
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

## Order Book

**Response Structure**

```json
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "clientId": "912444",
            "placedBy": "912444",
            "brokerOrderId": "25071400112229",
            "exchange": "NSE",
            "exchangeOrderId": "",
            "formattedInstrumentName": "ACC-EQ",
            "tradingSymbol": "ACC",
            "instrumentId": "22",
            "transactionType": "BUY",
            "quantity": 30,
            "product": "LONGTERM",
            "orderComplexity": "REGULAR",
            "orderType": "LIMIT",
            "price": 1120.15,
            "averageTradedPrice": 0,
            "slTriggerPrice": 0,
            "validity": "DAY",
            "disclosedQuantity": 0,
            "orderTime": "",
            "exchangeUpdateTime": "",
            "rejectionReason": "ORA:Price 1120.15 is not a multiple of tick size 0.10 ",
            "mainLegOrderId": "",
            "cancelledQuantity": 0,
            "pendingQuantity": 0,
            "filledQuantity": 0,
            "appKey": "",
            "algoId": "",
            "source": "API",
            "orderTag": "",
            "trailingSlAmount": 0,
            "brokerUpdateTime": "",
            "marketProtectionPercent": "",
            "exchangeTimestamp": "",
            "orderStatus": "REJECTED"
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| clientId | String | UCC client ID. |
| placedBy | String | Dealer/Client code who placed the order. |
| brokerOrderId | String | Unique ID assigned to the order by the broker. |
| exchange | String | [Exchange and segment (e.g., NSE,BSE).](16-appendix.md#exchange) |
| exchangeOrderId | String | Unique ID assigned to the order by the exchange. |
| formattedInstrumentName | String | Full name of the instrument. |
| tradingSymbol | String | Trading symbol of the instrument. |
| instrumentId | String | Unique identifier or scrip code of the instrument. |
| transactionType | String | [Type of transaction:Buy or Sell.](16-appendix.md#transaction-type) |
| quantity | Int | Total quantity for the order. |
| product | String | [Product type (e.g., INTRADAY, LONGTERM).](16-appendix.md#product-type) |
| orderComplexity | String | [Type of order: REGULAR, AMO, etc.](16-appendix.md#order-complexity) |
| orderType | String | [Order pricing type: LIMIT, MARKET, SL, SLM.](16-appendix.md#order-type) |
| price | Float | Limit price entered by the client. |
| averageTradedPrice | Float | Weighted average price of matched trades. |
| slTriggerPrice | Float | Stop Loss trigger price. |
| validity | String | [Order validity duration (e.g., DAY, IOC).](16-appendix.md#validity) |
| disclosedQuantity | Int | Quantity to be disclosed in market feed. |
| orderTime | DateTime | Date and time when the order was initially placed on the exchange or by the client. |
| exchangeUpdateTime | DateTime | Time when the latest update for this order came from exchange. |
| rejectionReason | String | Reason for order rejection. |
| mainLegOrderId | String | Identifier for the main/parent order in a bracket order. |
| cancelledQuantity | Int | Quantity of the order that was cancelled. |
| pendingQuantity | Int | Quantity of the order still pending. |
| filledQuantity | Int | Quantity of the order that has been filled. |
| appKey | String | App key of the client/vendor/franchise that placed the order. |
| algoId | String | Identifier for the algorithm placing the order. |
| source | String | Origin of the order (Web, App, API, etc.). |
| orderTag | String | User-defined tag for internal tracking. |
| trailingSLAmount | Int | Amount by which SL price trails the market. |
| brokerUpdateTime | DateTime | Timestamp when the broker last updated the order. |
| marketProtectionPercent | String | Price deviation limit for market protection. |
| exchangeTimestamp | DateTime | Timestamp when the order was placed. |
| orderStatus | String | Current status of the order (e.g., rejected, open, complete). |

## Order History

**Request Structure**

```json
{
    "brokerOrderId": "250526000002881"
}
```

**Input Parameters**

| Field | Type | Description |
| --- | --- | --- |
| brokerOrderId | String | Unique ID assigned to the order by the broker. |

**Response Structure**

```json
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "clientId": "912444",
            "placedBy": "912444",
            "brokerOrderId": "25071400112229",
            "exchange": "NSE",
            "exchangeOrderId": "",
            "formattedInstrumentName": "ACC-EQ",
            "tradingSymbol": "ACC-EQ",
            "instrumentId": "22",
            "transactionType": "BUY",
            "quantity": 30,
            "product": "LONGTERM",
            "orderComplexity": "REGULAR",
            "orderType": "LIMIT",
            "price": 1120.15,
            "averageTradedPrice": 0,
            "slTriggerPrice": 0,
            "validity": "DAY",
            "disclosedQuantity": 0,
            "orderTime": "",
            "exchangeUpdateTime": "",
            "rejectionReason": "ORA:Price 1120.15 is not a multiple of tick size 0.10 ",
            "mainLegOrderId": "",
            "cancelledQuantity": 0,
            "pendingQuantity": 0,
            "filledQuantity": 0,
            "appKey": "",
            "algoId": "",
            "source": "API",
            "orderTag": "",
            "trailingSlAmount": 0,
            "brokerUpdateTime": "",
            "marketProtectionPercent": "",
            "exchangeTimestamp": "",
            "orderStatus": "REJECTED"
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| clientId | String | UCC client ID. |
| placedBy | String | Dealer/Client code who placed the order. |
| brokerOrderId | String | Unique ID assigned to the order by the broker. |
| exchange | String | [Exchange and segment (e.g., NSE,BSE).](16-appendix.md#exchange) |
| exchangeOrderId | String | Unique ID assigned to the order by the exchange. |
| formattedInstrumentName | String | Full name of the instrument. |
| tradingSymbol | String | Trading symbol of the instrument. |
| instrumentId | String | Unique identifier or scrip code of the instrument. |
| transactionType | String | [Type of transaction:Buy or Sell.](16-appendix.md#transaction-type) |
| quantity | Int | Total quantity for the order. |
| product | String | [Product type (e.g., INTRADAY, LONGTERM).](16-appendix.md#product-type) |
| orderComplexity | String | [Type of order: REGULAR, AMO, etc.](16-appendix.md#order-complexity) |
| orderType | String | [Order pricing type: LIMIT, MARKET, SL, SLM.](16-appendix.md#order-type) |
| price | Float | Limit price entered by the client. |
| averageTradedPrice | Float | Weighted average price of matched trades. |
| slTriggerPrice | Float | Stop Loss trigger price. |
| validity | String | [Order validity duration (e.g., DAY, IOC).](16-appendix.md#validity) |
| disclosedQuantity | Int | Quantity to be disclosed in market feed. |
| orderTime | DateTime | Date and time when the order was initially placed on the exchange or by the client. |
| exchangeUpdateTime | DateTime | Time when the latest update for this order came from exchange. |
| rejectionReason | String | Reason for order rejection. |
| mainLegOrderId | String | Identifier for the main/parent order in a bracket order. |
| cancelledQuantity | Int | Quantity of the order that was cancelled. |
| pendingQuantity | Int | Quantity of the order still pending. |
| filledQuantity | Int | Quantity of the order that has been filled. |
| appKey | String | App key of the client/vendor/franchise that placed the order. |
| algoId | String | Identifier for the algorithm placing the order. |
| source | String | Origin of the order (Web, App, API, etc.). |
| orderTag | String | User-defined tag for internal tracking. |
| trailingSLAmount | Int | Amount by which SL price trails the market. |
| brokerUpdateTime | DateTime | Timestamp when the broker last updated the order. |
| marketProtectionPercent | String | Price deviation limit for market protection. |
| exchangeTimestamp | DateTime | Timestamp when the order was placed. |
| orderStatus | String | Current status of the order (e.g., rejected, open, complete). |

## Modify Order

**Request Structure**

```json
{
    "brokerOrderId": "25061300124513",
    "quantity": 3,
    "orderType": "SL",
    "slTriggerPrice": 5400,
    "price": "8",
    "slLegPrice": 5369, //stoploss
    "trailingSLAmount": "",
    "targetLegPrice": 5500, //targetPrice
    "validity": "DAY",
    "disclosedQuantity": "0",
    "marketProtection": "",
    "deviceId": "123"
}
```

**Input parameters**

| Field | Type | Criticality | Description |
| --- | --- | --- | --- |
| brokerOrderId | String | Required | Unique ID assigned to the order by the broker. |
| quantity | Int | Optional | Quantity of the instrument specified in the order. |
| orderType | String | Optional | [Order pricing type: LIMIT, MARKET, SL, SLM.](16-appendix.md#order-type) |
| price | String | Conditionally Required | Price at which the order is intended to execute, if applicable. |
| slTriggerPrice | String | Conditionally Required | Price at which a conditional order triggers, used for stop orders. |
| validity | String | Optional | [Order validity duration (e.g., DAY, IOC).](16-appendix.md#validity) |
| disclosedQuantity | String | Optional | Quantity disclosed to the market for transparency, if different from the full quantity. |
| marketProtectionPercent | String | Optional | Market protection setting to reduce impact on price movement; may be blank if unused. |
| trailingSLAmount | String | Optional | Amount by which SL price trails the market. |
| slLegPrice | String | Stop-loss price for the leg in a multi-leg order. |  |
| targetLegPrice | String | Target price for the leg in a multi-leg order. |  |
| deviceId | String | Identifier of the device placing the order (used for tracking or analytics). |  |

**Response Structure**

```json
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

## Cancel Order

**Request Structure**

```json
{
    "brokerOrderId":"250526000002881"
}
```

**Input Parameters**

| Field | Type | Description |
| --- | --- | --- |
| brokerOrderId | String | Unique ID assigned to the order by the broker. |

**Response Structure**

```json
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "brokerOrderId": "250526000002881",
            "requestTime": "26-May-2025 14:24:36"
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| requestTime | String | when the API request was initiated by the client, used for logging, tracking, or validating request timing. |
| brokerOrderId | String | Order Number is defined as Unique number it can be generated while placing the order. |

## Trade Book

**Response Structure**

```json
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "clientId": "DK2200295",
            "placedBy": "DK2200295",
            "brokerOrderId": "250526000005634",
            "exchangeOrderId": "1100000067912030",
            "exchangeTradeId": "207745115",
            "formattedInstrumentName": "IDEA",
            "tradingSymbol": "IDEA-EQ",
            "instrumentId": "14366",
            "exchange": "NSE",
            "transactionType": "BUY",
            "product": "LONGTERM",
            "orderComplexity": "REGULAR",
            "orderType": "MARKET",
            "validity": "DAY",
            "tradedPrice": 6.95,
            "filledQuantity": 1,
            "orderTime": "2025-05-26 14:27:43",
            "fillTimestamp": "2025-05-26 14:27:43",
            "orderTag": "--",
            "algoId": ""
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| clientId | String | UCC client ID. |
| placedBy | String | Dealer/Client code who placed the order. |
| brokerOrderId | String | Unique ID assigned to the order by the broker. |
| exchangeOrderId | String | Unique ID assigned to the order by the exchange. |
| exchangeTradeId | String | A unique identifier assigned by the exchange to each executed trade |
| formattedInstrumentName | String | Full name of the instrument. |
| tradingSymbol | String | Trading symbol of the instrument. |
| instrumentId | String | Unique identifier or scrip code of the instrument. |
| exchange | String | [Exchange and segment (e.g., NSE,BSE).](16-appendix.md#exchange) |
| transactionType | String | [Type of transaction:Buy or Sell.](16-appendix.md#transaction-type) |
| product | String | [Product type (e.g., INTRADAY, LONGTERM).](16-appendix.md#product-type) |
| orderComplexity | String | [Type of order: REGULAR, AMO, etc.](16-appendix.md#order-complexity) |
| orderType | String | [Order pricing type: LIMIT, MARKET, SL, SLM.](16-appendix.md#order-type) |
| validity | String | [Order validity duration (e.g., DAY, IOC).](16-appendix.md#validity) |
| tradedPrice | Number | Weighted average price of matched trades. |
| filledQuantity | Number | Quantity of the order that has been filled. |
| orderTime | DateTime | Date and time when the order was initially placed on the exchange or by the client. |
| fillTimestamp | DateTime | The exact date and time when the order was executed (filled) on the exchange. |
| algoId | String | Identifier for the algorithm placing the order. |
| orderTag | String | User-defined tag for internal tracking. |

## Order Margin

**Request Structure**

```json
{
"exchange": "NSEEQ",
"instrumentId": "22",
"transactionType": "BUY",
"quantity": 1,
"product": "intraday",
"orderComplexity": "regular",
"orderType": "market",
"price": "",
"validity": " day",
"slTriggerPrice": ""
}
```

**Input parameters**

| Field | Type | Description |
| --- | --- | --- |
| exchange | String | [Exchange and segment (e.g., NSE,BSE).](16-appendix.md#exchange) |
| instrumentId | String | Unique identifier or scrip code of the instrument. |
| transactionType | String | [Type of transaction:Buy or Sell.](16-appendix.md#transaction-type) |
| quantity | Number | Total quantity for the order. |
| product | String | [Product type (e.g., INTRADAY, LONGTERM).](16-appendix.md#product-type) |
| orderComplexity | String | [Type of order: REGULAR, AMO, etc.](16-appendix.md#order-complexity) |
| orderType | String | [Order pricing type: LIMIT, MARKET, SL, SLM.](16-appendix.md#order-type) |
| price | Number | Limit price entered by the client. |
| validity | String | [Order validity duration (e.g., DAY, IOC).](16-appendix.md#validity) |
| slTriggerPrice | String | Trigger price for stop-loss orders. |

**Response Structure**

```json
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "status": "Ok",
            "message": "Success",
            "totalCashAvailable": "52926",
            "preOrderMargin": "",
            "postOrderMargin": "183.65",
            "currentOrderMargin": "113.70",
            "rmsValidationCheck": "",
            "fundShort": ""
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| totalCashAvailable | String | The total cash amount available in the trading account. |
| preOrderMargin | String | Margin utilized before placing the current order. |
| postOrderMargin | String | Margin amount required or reserved after placing the current order. |
| currentOrderMargin | String | Margin needed specifically for the current order. |
| rmsValidationCheck | String | Result or status of the Risk Management System validation (empty if no issues). |
| fundShort | String | Indicates any shortfall in funds required for the order. |

## Basket Margin

**Request Structure**

```json
[{
    "exchange": "NSE",
    "tradingSymbol": "TCS-EQ",
    "price": "3056.8",
    "qty": "1",
    "product": "CNC",
    "priceType": "L",
    "triggerPrice": "",
    "transType": "B"
}
]
```

**Input parameters**

| Field | Type | Description |
| --- | --- | --- |
| exchange | String | [Exchange and segment (e.g., NSE,BSE).](16-appendix.md#exchange) |
| tradingSymbol | String | Unique identifier or scrip code of the instrument. |
| transType | String | [Type of transaction:B or S.](16-appendix.md#transaction-type) |
| qty | Number | Total quantity for the order. |
| product | String | [Product code (MIS or CO or CNC or BO or NRML).](16-appendix.md#product-type) |
| priceType | String | [(L or MKT or SL or SL-M).](16-appendix.md#order-type) |
| price | Number | Limit price entered by the client. |
| triggerPrice | String | Trigger price for stop-loss orders. |

**Response Structure**

```json
{
    "status": "Ok",
    "message": "Success",
    "result": [
        {
            "status": "Ok",
            "message": "Success",
            "totalCashAvailable": "52926",
            "preOrderMargin": "",
            "postOrderMargin": "183.65",
            "currentOrderMargin": "113.70",
            "rmsValidationCheck": "",
            "fundShort": ""
        }
    ]
}
```

**Response Parameters**

| Field | Type | Description |
| --- | --- | --- |
| totalCashAvailable | String | The total cash amount available in the trading account. |
| preOrderMargin | String | Margin utilized before placing the current order. |
| postOrderMargin | String | Margin amount required or reserved after placing the current order. |
| currentOrderMargin | String | Margin needed specifically for the current order. |
| rmsValidationCheck | String | Result or status of the Risk Management System validation (empty if no issues). |
| fundShort | String | Indicates any shortfall in funds required for the order. |

## Exit Bracket Order

**Request Structure**

```json
[
    {
        "orderNo": "25051400177494",
        "orderComplexity": "BO"
    }
]
```

**Input parameters**

| Field | Type | Description |
| --- | --- | --- |
| brokerOrderId | String | Broker orderId is defined as Unique number it can be generated while placing the order. |
| orderComplexity | String | [Type of order: REGULAR, AMO, etc.](16-appendix.md#order-complexity) |

**Response Structure**

```json
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
