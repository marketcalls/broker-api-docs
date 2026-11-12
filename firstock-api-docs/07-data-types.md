# Data Types

> Source: https://firstock.in/api/docs/data-types/

## Data Types Reference

This document provides a consolidated overview of common fields (keys) and their data types used across various Firstock APIs. Understanding these data types helps ensure seamless integration and accurate data handling.

---

## Common Data Variables

**Exchanges**

| Exchange | Segment / Description |
|---|---|
| **BSE** | BSE Equity |
| **NSE** | NSE Equity |
| **NFO** | NSE Futures & Options |
| **BFO** | BSE Futures & Options |

**Products (C, I, M)**

| Code | Full Name | Description / Usage |
|---|---|---|
| **C** | Cash & Carry | Positions are taken for delivery (not squared off intraday). |
| **I** | Intraday | Positions must be squared off within the same trading day. |
| **M** | Market (sometimes used) | Depending on context, can refer to “Market” product type in certain integrations. |

**Price Types**

| Code | Meaning | Description |
|---|---|---|
| **MKT** | Market Order | Executes immediately at the best available market price. |
| **LMT** | Limit Order | Executes at or better than a specific limit price set by the user. |
| **SL-LMT** | Stop Loss Limit Order | Triggers a limit order once a specified stop price is reached. |
| **SL-MKT** | Stop Loss Market Order | Triggers a market order once a specified stop price is reached. |

## 1.Common Response Fields

| Field | Data Type | Description | Example |
|---|---|---|---|
| *userId* | string | Indicates whether the request succeeded or failed. Possible values: *"success"* or *"failed"*. | *"success"* |
| *message* | string | Describes the outcome of the request. | *"Login successful"* |
| *code* | string or integer | Error or status code, often provided on failure. | *"400"*, *"401"* |
| *name* | string | Error name or identifier. | *"MISSING_FIELD"*, *"BAD_REQUEST"* |
| *error* | object | Contains error details when *status* is *"failed".* | *"{"field": "...", "message": "..."}"* |
| *data* | object or array | Primary response payload, can be an object or array of objects. | Varies by endpoint |

## 2.Authentication & Session Fields

| Field | Data Type | Description | Example |
|---|---|---|---|
| *userId* | string | Unique identifier for the user. | *"AB1234"* |
| *password* | string | Hashed password for authentication. | *"be5628d7f2d0..."* |
| *TOTP* | string | Time-based One-Time Password (MFA code). | *"1997"* |
| *vendorCode* | string | Vendor or partner code used for authorizing API usage. | *"AB1234_API"* |
| *apiKey* | string | API key used to authenticate requests. | *"2b9d6c37476be0..."* |
| *jKey* | string | Session token or key required for subsequent requests. | *"1478b9b71707..."* |
| *userToken* | string | Alternate session token returned on login. | *"abc123"* |

## 3.User & Profile Fields

| Field | Data Type | Description | Example |
|---|---|---|---|
| *actid* | string | Account ID, often same as *userId* in some responses. | *"AB1234"* |
| *userName* | string | Full name of the user. | *"PERESANDRA SUBRAMANYAM KUMAR"* |
| *email* | string | Email address associated with the user account. | *"nitishkumarpsXXX @gmail.com"* |
| *exchange* | array | List of enabled exchanges for the user. | *["NFO", "NSE", "BSE"]* |
| *orarr* | array | List of supported order types. | *"["MKT", "LMT", "SL-LMT", "SL-MKT"]"* |
| *uprev* | string | User privilege level. | *"INVESTOR"* |
| *requestTime* | string | Timestamp of server processing the request. | *"10:40:21 23-04-2025"* |

## 4. Market Data & Quotes

**4.1 Common Fields for Quotes**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *exchange* | string | Exchange code (e.g.,*"NSE"* , *"BSE"*, *"NFO"*). | *"NFO"* |
| *tradingSymbol* | string | Symbol or instrument identifier. | *"NIFTY06MAR25C22500"* |
| *companyName* | string | Display name or descriptive label for the symbol. | *"Nifty 50"* |
| *lastTradedPrice* | string or number | Most recent traded price. | *"2417780"* |
| *dayOpenPrice* | string | Opening price for the trading day. | *"2418540"* |
| *dayHighPrice* | string | Highest price of the day. | *"2420165"* |
| *dayLowPrice* | string | Lowest price of the day. | *"2407200"* |
| *dayClosePrice* | string | Previous day's closing price. | *"2412555"* |
| *segment* | string | Instrument segment: e.g., *"EQT"*, *"Options"* ,*"Indices"* . | *"Indices"* |
| *token* | string or number | Numeric identifier for the instrument. | *26000* |
| *lotSize* | string or number | Size of one lot (for derivatives). | *"1"* |
| *tickSize* | string | Minimum price increment for the instrument. | *"0.05"* |
| *openInterest* | string | Open interest for F&O instruments. | *"0.00"* |
| *bestBuyPriceX*, *bestBuyQuantityX* | string | Top buy price/quantity at level X. For example, *bestBuyPrice1* or *bestBuyQuantity1*. | *"0.00"*,*"0"* |
| *bestSellPriceX*, *bestSellQuantityX* | string | Top sell price/quantity at level X. | *"0.00"*,*"0"* |

**4.2 Search Scripts**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *stext* | string | Search term or partial symbol for the instrument lookup. | *"ITC"* |
| *representationName* | string | Display-friendly name for the scrip. | *"ITC APR 425 CE"* |
| *instrumentName* | string | Category or type of instrument (e.g., Equity, Options). | *"Equity"* |

**4.3 Multi Quotes**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *data* | array of objects | Contains multiple quote objects, each with standard quote fields. | *[ ...... ]* |

## 5. Chart / Historical Data

| Field | Data Type | Description | Example |
|---|---|---|---|
| *startTime* | string | Start timestamp (e.g., *DD-MM-YYYY HH:MM:SS*) for historical data. | *"09:15:00 23-04-2025"* |
| *endTime* | string | End timestamp for historical data. | *"15:29:00 23-04-2025"* |
| *interval* | string | Candle interval (*"1d"*, *"2mi"*, *"1mi"*, etc.). | *"1d"* |
| *time* | string | Candle start time in ISO-like format. | *"2025-02-11 T00:00:00"* |
| *epochTime* | number | Unix epoch timestamp (seconds since 1970-01-01). | *1739212200* |
| *open*, *high*, *low*, *close*, | number | Candle prices during the specified interval. | *23071.8* |
| *volume*, *oi* | number | Trading volume and open interest (for F&O) over the interval. | *0* |

## 6. Order Management (OMS)

 **6.1 Place / Modify / Cancel Order Fields**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *orderNumber* | string or number | Unique identifier for the order. | *"25042100011119"* |
| *exchange* | string | Exchange code (*"NSE"*, *"BSE"*, *"NFO"*, etc.). | *"NSE"* |
| *transactionType* | string | *"B"* for Buy, *"S"* for Sell. | *"B"* |
| *retention* | string | Order duration (e.g., *"DAY"*, *"IOC"*). | *"DAY"* |
| *customer_firm* | number | Customer type (e.g., *"C"*). | *"C"* |
| *product* | number | Product type (e.g., *"C"*, *"M"*,*"I"*). | *MKT* |
| *priceType* | string | Pricing model (*"MKT"*, *"LMT"*, etc.). | *0* |
| *price* | number | Limit price, or 0 if market order. | *780*,*0* |
| *triggerPrice* | number | Stop-Loss trigger price. | *0* |
| *quantity* | number | Number of shares or lots. | *1* |
| *remarks* | number | Optional note or reference for the order. | *"Test"* |
| *mkt_protection* | number (optional) | Market protection buffer for certain order types. | *0.5* |

**6.2 Order Margin**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *marginOnNewOrder* | string or number | Margin required for the new order. | *"798.2978* |
| *availableMarginFor TheOrder* | string or number | Remaining margin after placing the order. | *5068.297799985* |
| *remarks* | string | Additional info (e.g., "Insufficient Balance"). | *"Insufficient Balance"* |
| *totalCash* | string or number | Total cash in the trading account. | *7906.99999* |
| *requestTime* | string | Timestamp of margin calculation. | *"17:54:23 21-04-2025"* |

 **6.3 Order Book / Single Order History**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *fillShares* | string or number | Total shares (or lots) filled. | *"0"*,*"1"* |
| *averagePrice* | string or number | Average fill price. | *"0.00"*, *"2837"* |
| *rejectReason* | string | Reason for order rejection. | *"ORA: order generation source info missing"* |
| *orderTime* | string | Time the order was placed. | *"09:30:02 21-04-2025"* |
| *status* | string | Order status (e.g., *"REJECTED"*, *"Open"*, *Filled"*"). | *"REJECTED"* |

 **6.4 Trade Book**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *fillId* | string | Unique identifier for a fill (trade execution). | *"401070025"* |
| *fillPrice* | number | Price at which the trade was executed. | *2837* |
| *fillQuantity* | string or number | Quantity filled at this execution. | *"1"* |
| *exchangeUpdateTime* | string | Timestamp of the trade update from the exchange. | *"21-04-2025 09:30:02"* |
| *exchordid* | string | Exchange’s order ID reference. | *"1200000006968574"* |

## 7. Account & Portfolio

 **7.1 RMS Limit**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *brkcollamt* | string | Broker collateral amount. | *"0.00"* |
| *cash* | string | Current cash balance in the account. | *"51.68"* |
| *collateral* | string | Value of pledged collateral. | *"0.00"* |
| *expo* | string | Exposure margin used. | *"0.00"* |
| *marginused* | string | Margin currently utilized by open positions. | *"28.39"* |
| *payin* | string | Funds paid into the account but not yet cleared. | *"0.00"* |
| *peak_mar* | string | Peak margin utilized during the day. | *"0.00"* |
| *premium* | string | Premium credit/debit for options trades. | *"0.00"* |
| *span* | string | SPAN margin (for F&O). | *"0.00"* |

 **7.2 Position Book**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *RealizedPNL* | string | Realized profit or loss. | *"0.00"* |
| *dayBuyAveragePrice* | string | Average price for intraday buy. | *"2837.00"* |
| *dayBuyQuantity* | string | Quantity bought during the day. | *"1.00"* |
| *daySellAveragePrice* | string | Average price for intraday sell. | *"0.00"* |
| *daySellQuantity* | string | Quantity sold during the day. | *"0.00"* |
| *netQuantity* | string | et position (buy - sell). | *"1.00"* |
| *netAveragePrice* | string | Weighted average price for the net position. | *"2837.00"* |
| *unrealizedMTOM* | string | Mark-to-market P/L for open positions. | *"0.00"* |

 **7.3 Holdings**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *exchange* | string | Exchange where the holding is listed (*"NSE"*, *"BSE"*). | *"NSE"* |
| *tradingSymbol* | string | Symbol representing the holding. | *"VIKASECO-EQ"* |

## 8. Additional Utilities

 **8.1 Brokerage Calculator**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *brokerage* | number | Total brokerage for the transaction. | *2000* |
| *exchange_charge* | number | Exchange transaction charges. | *0* |
| *gst* | number | Goods and Services Tax. | *0* |
| *sebi_charge* | number | SEBI turnover fee, if applicable. | *0* |
| *stamp_duty* | number | Stamp duty, if applicable. | *0* |
| *remarks* | number | Additional comments or warnings. | *"\r"* |

 **8.2 Basket Margin**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *BasketMargin* | array of numbers | Margin details for multiple orders in the basket. | *[126075.6, 126783.0242, 2]* |
| *MarginOnNewOrder* | number | Additional margin required for the new basket items. | *126783.0242* |
| *PreviousMargin* | number | Margin before the new basket was added. | *0* |
| *TradedMargin* | number | Updated total margin in use after adding the basket. | *126783.0242* |
| *Remarks* | string | Any relevant comments or warnings. | *""* |

**8.3 Get Security Info**

| Field | Data Type | Description | Example |
|---|---|---|---|
| *instrumentName* | string | Instrument type/category. | *"UNDIND"* |
| *segment* | string | Market segment (*"EQT"*, *"FNO"*, etc.). | *"EQT"* |
| *symbolName* | string | System-recognized symbol name. | *"NIFTY"* |
| *tradingSymbol* | string | Display-oriented symbol name. | *"Nifty 50"* |

## Notes on Data Types

- **String vs. Number**: Certain fields (e.g., *price*, *quantity*, *token*) may appear as strings in JSON responses, even though they represent numeric values. Adjust your parsing accordingly.
- **Timestamps**: Most time-related fields (e.g., *orderTime*, *requestTime*) are strings in the format *"DD-MM-YYYY HH:MM:SS"* or sometimes *"YYYY-MM-DDTHH:MM:SS*". Handle parsing and timezones as required.
- **Optional Fields**: Many endpoints only require or return certain fields in specific scenarios. When a field is missing or irrelevant, it may be omitted or default to *null*, *0*, or an empty string.

## Conclusion

This Data Types Reference consolidates the key fields encountered across Firstock’s APIs and their typical formats. Use this guide to correctly parse and handle data, ensuring robust integrations for both trading and market data scenarios.
