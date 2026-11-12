# WebSocket Broadcast

> Source: https://invest.motilaloswal.com/moAPI/APIDocumentation/Introduction

The WebSocket API used to receive different type of quotes for instrument/Exchanges during market hours , only for those scrips which are registered. The API uses WebSocket protocols to establish a TCP connection after an HTTP handshake .To connect with the OpenAPI WebSocket, you will need a WebSocket client library in your choice of programming language

AuthValidation is necessary before using OpenAPI WebSocket Broadcast.

## Connecting To WebSocket End Point

CAfter Login Authentication for Connecting with OpenAPI WebSocket call

**Mofsl.connect()**

## Index Register

To register an Index, pass a single parameter Exchange (BSE or NSE) with function call

**Mofsl.IndexRegister("NSE")**

## Index Unregister

To Unregister an Index, pass a single parameter Exchange (BSE or NSE) with function call

**Mofsl.IndexUnregister("NSE")**

## Scrip Register

To Register a script, pass three parameters Exchange (BSE or NSE), Exchange Type (CASH or DERIVATIVES), Scrip Code (eg 532540, 532543)

**Mofsl.Register("BSE", "CASH", 532540)**

## Scrip Unregister

To unregister, pass the same information with UnRegister() function call

**Mofsl.UnRegister("BSE", "CASH", 532540)**

## Quote packet structures

**DayOHLC**

{'Exchange': 'BSE', 'Scrip Code': 532540, 'Time': '2022-03-09 12:45:35', 'Open': 3610.0, 'High': 3644.0, 'Low': 3599.0, 'PrevDayClose': 3599.95}

**LTP**

{'Exchange': 'BSE', 'Scrip Code': 532540, 'Time': '2022-03-09 12:45:35', 'LTP_Rate': 3636.8,'LTP_Qty': 4, 'LTP_Cumulative Qty': 75937, 'LTP_AvgTradePrice': 3627.39, 'LTP_Open Interest': 0}

**DPR**

{'Exchange': 'BSE', 'Scrip Code': 532540, 'Time': '2022-03-09 12:45:35', 'UpperCktLimit': 3959.9, 'LowerCktLimit': 3240.0}

**MarketDepth**

{'Exchange': 'BSE', 'Scrip Code': 532540, 'Time': '2022-03-09 12:45:35', 'BidRate': 3636.8, 'BidQty': 10, 'BidOrder': 1, 'OfferRate': 3638.95, 'OfferQty': 51, 'OfferOrder': 1, 'Level': 1}

**OpenInterest**

{'Exchange': 'NSE', 'Scrip Code': 532540, 'Time': '2022-03-09 12:45:35', 'Open Interest': 0, 'Open Interest High': 0,'Open Interest Low': 0}

**Index**

{'Exchange': 'N', 'Scrip Code': 26000, 'Time': '2022-03-09 12:57:15', 'Rate': 16284.25}
