> Source: https://docs.arrow.trade/rest-api/positions/

# Positions API

The Positions API delivers portfolio monitoring capabilities with real-time position tracking, detailed P&L breakdowns, and comprehensive risk analytics. Essential for portfolio management platforms, algorithmic trading systems, and advanced trading applications requiring precise position data.

## Endpoint Reference

### Get Portfolio Positions

Retrieve your complete position book with detailed analytics and market data.

Endpoint Details

**Method:** `GET`
**URL:** `/user/positions`
**Header:** Required (`appID` \+ `token`)

#### Request Example

```bash
curl --location 'https://edge.arrow.trade/user/positions' \
--header 'appID: <YOUR_APP_ID>' \
--header 'token: <YOUR_TOKEN>'
```

## Response Schema

### Success Response

```json
{
    "data": [
        {
            "userID": "AJ0001",
            "accountID": "",
            "token": "1531822",
            "exchange": "BSE",
            "symbol": "IDEA",
            "segment": "CM",
            "product": "I",
            "qty": "0",
            "avgPrice": "0",
            "dayBuyQty": "1",
            "daySellQty": "1",
            "dayBuyAmount": "9.9",
            "dayBuyAvgPrice": "9.9",
            "daySellAmount": "10.59",
            "daySellAvgPrice": "10.59",
            "carryForwardBuyQty": "",
            "carryForwardSellQty": "",
            "carryForwardBuyAmount": "",
            "carryForwardBuyAvgPrice": "",
            "carryForwardSellAmount": "",
            "carryForwardSellAvgPrice": "",
            "carryForwardAvgPrice": "",
            "ltp": "11.17",
            "realisedPnL": "",
            "unrealisedMarkToMarket": "",
            "breakEvenPrice": "",
            "multiplier": "0",
            "pricePrecision": "0",
            "priceFactor": "",
            "tickSize": "0.01",
            "lotSize": "1",
            "uploadPrice": "",
            "netUploadPrice": ""
        },
        {
            "userID": "AJ0001",
            "accountID": "",
            "token": "49795",
            "exchange": "NFO",
            "symbol": "NIFTY03FEB26C25300",
            "segment": "FO",
            "product": "M",
            "qty": "0",
            "avgPrice": "0",
            "dayBuyQty": "1040",
            "daySellQty": "1040",
            "dayBuyAmount": "188353.75",
            "dayBuyAvgPrice": "181.109375",
            "daySellAmount": "195737.75",
            "daySellAvgPrice": "188.209375",
            "carryForwardBuyQty": "0",
            "carryForwardSellQty": "0",
            "carryForwardBuyAmount": "0",
            "carryForwardBuyAvgPrice": "0",
            "carryForwardSellAmount": "0",
            "carryForwardSellAvgPrice": "0",
            "carryForwardAvgPrice": "",
            "ltp": "214",
            "realisedPnL": "",
            "unrealisedMarkToMarket": "",
            "breakEvenPrice": "",
            "multiplier": "0",
            "pricePrecision": "2",
            "priceFactor": "",
            "tickSize": "0.05",
            "lotSize": "65",
            "uploadPrice": "",
            "netUploadPrice": ""
        },
        {
            "userID": "AJ0001",
            "accountID": "",
            "token": "49801",
            "exchange": "NFO",
            "symbol": "NIFTY03FEB26C25400",
            "segment": "FO",
            "product": "M",
            "qty": "0",
            "avgPrice": "0",
            "dayBuyQty": "1040",
            "daySellQty": "1040",
            "dayBuyAmount": "146864.25",
            "dayBuyAvgPrice": "141.215625",
            "daySellAmount": "145141.75",
            "daySellAvgPrice": "139.559375",
            "carryForwardBuyQty": "0",
            "carryForwardSellQty": "0",
            "carryForwardBuyAmount": "0",
            "carryForwardBuyAvgPrice": "0",
            "carryForwardSellAmount": "0",
            "carryForwardSellAvgPrice": "0",
            "carryForwardAvgPrice": "",
            "ltp": "161.8",
            "realisedPnL": "",
            "unrealisedMarkToMarket": "",
            "breakEvenPrice": "",
            "multiplier": "0",
            "pricePrecision": "2",
            "priceFactor": "",
            "tickSize": "0.05",
            "lotSize": "65",
            "uploadPrice": "",
            "netUploadPrice": ""
        }
    ],
    "status": "success"
}
```

## Integration Guidelines

Best Practices

  * **Efficient Polling** : Request positions data at appropriate intervals (every 1-5 seconds during market hours)
  * **Data Caching** : Cache position data to minimize API calls while maintaining freshness
  * **P &L Monitoring**: Implement real-time P&L tracking for risk management
  * **Position Reconciliation** : Cross-verify with order and trade data for accuracy
  * **Error Recovery** : Build robust error handling for market data interruptions

Performance Optimization

  * Filter positions client-side to reduce processing overhead
  * Implement incremental updates where possible
  * Use WebSocket feeds for real-time price updates when available
  * Monitor API response times and implement fallback mechanisms

Risk Management

  * Monitor unrealized P&L for position sizing decisions
  * Set up alerts for significant position movements
  * Implement automated stop-loss mechanisms based on position data
  * Regular reconciliation with broker statements for accuracy
