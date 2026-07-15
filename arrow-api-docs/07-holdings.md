> Source: https://docs.arrow.trade/rest-api/holdings/

# Holdings API

Retrieve comprehensive portfolio holdings data for authenticated users, including position details, profit/loss calculations, and collateral information.

## Overview

The Holdings API provides complete visibility into a user's equity positions across multiple exchanges, enabling portfolio management and risk assessment capabilities. Holdings are consolidated by instrument, with support for multi-exchange trading symbols.

## Endpoint Reference

### Get User Holdings

Retrieve all current holdings for the authenticated user account.

Endpoint Details

**Method:** `GET`
**URL:** `/user/holdings`
**Header:** Required (`appID` \+ `token`)

#### Request Example

```bash
curl --location 'https://edge.arrow.trade/user/holdings' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

## Response Schema

### Success Response

The API returns a structured response containing an array of holding objects. Each holding represents a consolidated position across multiple exchanges where the instrument is traded.

```json
{
    "data": [
        {
            "symbols": [
                {
                    "symbol": "GROWW",
                    "tradingSymbol": "GROWW-EQ",
                    "exchange": "NSE",
                    "token": "759806",
                    "isin": "INE0HOQ01053"
                },
                {
                    "symbol": "GROWW",
                    "tradingSymbol": "GROWW",
                    "exchange": "BSE",
                    "token": "1543603",
                    "isin": "INE0HOQ01053"
                }
            ],
            "avgPrice": "152.00",
            "qty": "2",
            "usedQty": "0",
            "t1Qty": "0",
            "depositoryQty": "0",
            "collateralQty": "0",
            "brokerCollateralQty": "2.00",
            "authorizedQty": "0",
            "unPledgedQty": "0",
            "nonPOAQty": "0",
            "haircut": "0.00",
            "effectiveQty": "2",
            "sellableQty": "2",
            "ltp": "",
            "pnl": "",
            "close": ""
        },
        {
            "symbols": [
                {
                    "symbol": "CDSL",
                    "tradingSymbol": "CDSL-EQ",
                    "exchange": "NSE",
                    "token": "21174",
                    "isin": "INE736A01011"
                },
                {
                    "symbol": "CDSL",
                    "tradingSymbol": "CDSL",
                    "exchange": "BSE",
                    "token": "1200232",
                    "isin": "INE736A01011"
                }
            ],
            "avgPrice": "1346.00",
            "qty": "1",
            "usedQty": "0",
            "t1Qty": "1",
            "depositoryQty": "0",
            "collateralQty": "0",
            "brokerCollateralQty": "0.00",
            "authorizedQty": "0",
            "unPledgedQty": "0",
            "nonPOAQty": "0",
            "haircut": "0.00",
            "effectiveQty": "1",
            "sellableQty": "0",
            "ltp": "",
            "pnl": "",
            "close": ""
        },
        {
            "symbols": [
                {
                    "symbol": "GOLDETF",
                    "tradingSymbol": "GOLDETF-EQ",
                    "exchange": "NSE",
                    "token": "14286",
                    "isin": "INF769K01JP9"
                },
                {
                    "symbol": "GOLDETF",
                    "tradingSymbol": "GOLDETF",
                    "exchange": "BSE",
                    "token": "1542781",
                    "isin": "INF769K01JP9"
                }
            ],
            "avgPrice": "107.00",
            "qty": "1",
            "usedQty": "0",
            "t1Qty": "0",
            "depositoryQty": "0",
            "collateralQty": "0",
            "brokerCollateralQty": "1.00",
            "authorizedQty": "0",
            "unPledgedQty": "0",
            "nonPOAQty": "0",
            "haircut": "0.00",
            "effectiveQty": "1",
            "sellableQty": "1",
            "ltp": "",
            "pnl": "",
            "close": ""
        },
        {
            "symbols": [
                {
                    "symbol": "SBIN",
                    "tradingSymbol": "SBIN-EQ",
                    "exchange": "NSE",
                    "token": "3045",
                    "isin": "INE062A01020"
                },
                {
                    "symbol": "SBIN",
                    "tradingSymbol": "SBIN",
                    "exchange": "BSE",
                    "token": "1499112",
                    "isin": "INE062A01020"
                }
            ],
            "avgPrice": "882.00",
            "qty": "3",
            "usedQty": "0",
            "t1Qty": "0",
            "depositoryQty": "3",
            "collateralQty": "0",
            "brokerCollateralQty": "0.00",
            "authorizedQty": "0",
            "unPledgedQty": "0",
            "nonPOAQty": "0",
            "haircut": "0.00",
            "effectiveQty": "3",
            "sellableQty": "3",
            "ltp": "",
            "pnl": "",
            "close": ""
        },
        {
            "symbols": [
                {
                    "symbol": "GOLDBEES",
                    "tradingSymbol": "GOLDBEES-EQ",
                    "exchange": "NSE",
                    "token": "14428",
                    "isin": "INF204KB17I5"
                },
                {
                    "symbol": "GOLDBEES",
                    "tradingSymbol": "GOLDBEES",
                    "exchange": "BSE",
                    "token": "1589095",
                    "isin": "INF204KB17I5"
                }
            ],
            "avgPrice": "91.00",
            "qty": "1",
            "usedQty": "0",
            "t1Qty": "0",
            "depositoryQty": "1",
            "collateralQty": "0",
            "brokerCollateralQty": "0.00",
            "authorizedQty": "0",
            "unPledgedQty": "0",
            "nonPOAQty": "0",
            "haircut": "0.00",
            "effectiveQty": "1",
            "sellableQty": "1",
            "ltp": "",
            "pnl": "",
            "close": ""
        },
        {
            "symbols": [
                {
                    "symbol": "IDEA",
                    "tradingSymbol": "IDEA-EQ",
                    "exchange": "NSE",
                    "token": "14366",
                    "isin": "INE669E01016"
                },
                {
                    "symbol": "IDEA",
                    "tradingSymbol": "IDEA",
                    "exchange": "BSE",
                    "token": "1531822",
                    "isin": "INE669E01016"
                }
            ],
            "avgPrice": "7.00",
            "qty": "1190",
            "usedQty": "0",
            "t1Qty": "0",
            "depositoryQty": "412",
            "collateralQty": "0",
            "brokerCollateralQty": "778.00",
            "authorizedQty": "0",
            "unPledgedQty": "0",
            "nonPOAQty": "0",
            "haircut": "0.00",
            "effectiveQty": "1190",
            "sellableQty": "1190",
            "ltp": "",
            "pnl": "",
            "close": ""
        },
        {
            "symbols": [
                {
                    "symbol": "NSDL",
                    "tradingSymbol": "NSDL",
                    "exchange": "BSE",
                    "token": "1543467",
                    "isin": "INE301O01023"
                }
            ],
            "avgPrice": "1284.00",
            "qty": "6",
            "usedQty": "0",
            "t1Qty": "0",
            "depositoryQty": "0",
            "collateralQty": "0",
            "brokerCollateralQty": "6.00",
            "authorizedQty": "0",
            "unPledgedQty": "0",
            "nonPOAQty": "0",
            "haircut": "0.00",
            "effectiveQty": "6",
            "sellableQty": "6",
            "ltp": "",
            "pnl": "",
            "close": ""
        },
        {
            "symbols": [
                {
                    "symbol": "BSE",
                    "tradingSymbol": "BSE-EQ",
                    "exchange": "NSE",
                    "token": "19585",
                    "isin": "INE118H01025"
                }
            ],
            "avgPrice": "2367.00",
            "qty": "2",
            "usedQty": "0",
            "t1Qty": "0",
            "depositoryQty": "2",
            "collateralQty": "0",
            "brokerCollateralQty": "0.00",
            "authorizedQty": "0",
            "unPledgedQty": "0",
            "nonPOAQty": "0",
            "haircut": "0.00",
            "effectiveQty": "2",
            "sellableQty": "2",
            "ltp": "",
            "pnl": "",
            "close": ""
        },
        {
            "symbols": [
                {
                    "symbol": "YESBANK",
                    "tradingSymbol": "YESBANK-EQ",
                    "exchange": "NSE",
                    "token": "11915",
                    "isin": "INE528G01035"
                },
                {
                    "symbol": "YESBANK",
                    "tradingSymbol": "YESBANK",
                    "exchange": "BSE",
                    "token": "1531648",
                    "isin": "INE528G01035"
                }
            ],
            "avgPrice": "19.00",
            "qty": "2",
            "usedQty": "0",
            "t1Qty": "0",
            "depositoryQty": "2",
            "collateralQty": "0",
            "brokerCollateralQty": "0.00",
            "authorizedQty": "0",
            "unPledgedQty": "0",
            "nonPOAQty": "0",
            "haircut": "0.00",
            "effectiveQty": "2",
            "sellableQty": "2",
            "ltp": "",
            "pnl": "",
            "close": ""
        }
    ],
    "status": "success"
}
```

## Integration Notes

Best Practices

  * Holdings are consolidated across exchanges - use the `symbols` array to identify specific exchange tokens
  * Handle empty market data fields (`ltp`, `pnl`, `close`) gracefully
  * Cache holdings data appropriately to minimize API calls
  * Implement proper error handling and retry logic
  * Use the `haircut` field for risk assessment calculations

Data Freshness

Holdings data is updated in real-time during market hours. Market data fields may be empty outside trading hours or during system maintenance. Position quantities and average prices are always available.
