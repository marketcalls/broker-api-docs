# Portfolio

Two endpoints for fetching holdings and open positions.

| Method | Endpoint | Processing Mode | Action |
| --- | --- | --- | --- |
| GET | `/holdings` | Single | Long-term equity holdings sitting in the client's DEMAT account. Settles T+1. |
| GET | `/positions` | Single | All open positions for the day, including F&O carryforward positions |

## Holdings

`GET /holdings`

**Headers:** `Authorization: Bearer <userSession>`

No request body.

### Response

```json
{
  "isin": "INE002A01018",
  "nseInstrumentId": "2885",
  "bseInstrumentId": "500325",
  "nseTradingSymbol": "RELIANCE-EQ",
  "bseTradingSymbol": "RELIANCE",
  "formattedInstrumentName": "RELIANCE INDUSTRIES LTD.",
  "product": "DELIVERY",
  "totalQuantity": 300,
  "dpQuantity": 300,
  "collateralQuantity": 0,
  "t1Quantity": 0,
  "authorizedQuantity": "0",
  "averageTradedPrice": "280000.00",
  "previousDayClose": null
}
```

| Field | Description |
| --- | --- |
| `isin` | ISIN of the instrument |
| `nseInstrumentId` / `bseInstrumentId` | Instrument identifier on NSE / BSE |
| `nseTradingSymbol` / `bseTradingSymbol` | Trading symbol on NSE / BSE |
| `formattedInstrumentName` | Display name |
| `product` | `DELIVERY` or `BNPL` |
| `totalQuantity` | Total shares held (`dpQuantity + t1Quantity`) |
| `dpQuantity` | Shares held in the Demat account |
| `collateralQuantity` | Shares pledged as collateral |
| `t1Quantity` | Quantity pending settlement from yesterday's trades |
| `authorizedQuantity` | Shares authorized for trading/transfer |
| `averageTradedPrice` | Average acquisition price |
| `previousDayClose` | Previous trading day's closing price |

---

## Positions

`GET /positions`

**Headers:** `Authorization: Bearer <userSession>`

No request body.

### Response

```json
{
  "instrumentId": "35382",
  "tradingSymbol": "NIFTY24OCTFUT",
  "formattedInstrumentName": "NIFTY 31 Oct 2024",
  "exchange": "NSEFO",
  "product": "NORMAL",
  "netQuantity": 26,
  "netAveragePrice": "0",
  "overnightQuantity": 1,
  "overnightPrice": "0",
  "buyQuantity": 25,
  "buyPrice": 652000,
  "sellQuantity": 0,
  "sellPrice": 0,
  "dayBuyQuantity": "25",
  "dayBuyPrice": 652000,
  "dayBuyValue": "627961.54",
  "daySellQuantity": "0",
  "daySellPrice": "0.00",
  "daySellValue": "0.00",
  "multiplier": "1",
  "lotSize": "25",
  "tickSize": "0.05",
  "previousDayClose": "26308.85"
}
```

| Field | Description / Formula |
| --- | --- |
| `realizedPnl` | Profit/loss booked from closed positions |
| `netQuantity` | `overnightQuantity + dayBuyQuantity − daySellQuantity` |
| `netAveragePrice` | `(overnightQuantity*overnightPrice + dayBuyValue − daySellValue) / netQuantity` |
| `overnightQuantity` / `overnightPrice` | Net quantity/price carried forward from the previous day |
| `buyQuantity` | `max(overnightQuantity,0) + dayBuyQuantity` |
| `buyPrice` | `(overnightPrice*max(overnightQuantity,0) + dayBuyPrice*dayBuyQuantity) / buyQuantity` |
| `sellQuantity` | `max(-overnightQuantity,0) + daySellQuantity` |
| `sellPrice` | `(overnightPrice*max(-overnightQuantity,0) + daySellPrice*daySellQuantity) / sellQuantity` |
| `dayBuyQuantity` / `dayBuyPrice` | Quantity/weighted-avg price bought today |
| `dayBuyValue` | `dayBuyQuantity * dayBuyPrice` |
| `daySellQuantity` / `daySellPrice` | Quantity/weighted-avg price sold today |
| `daySellValue` | `daySellQuantity * daySellPrice` |
| `multiplier` | Lot-size multiplier used for P&L calculation |
| `lotSize` | Minimum tradable unit |
| `tickSize` | Minimum price movement |
| `previousDayClose` | Previous trading day's close |
