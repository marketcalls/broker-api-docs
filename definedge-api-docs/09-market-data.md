# Market Data

All APIs require the request header:

```
Authorization: <api_session_key>
```

| Method | Relative URL | Description |
| --- | --- | --- |
| GET | `/quotes/{exchange}/{token}` | Get quotes for a symbol |
| GET | `/securityinfo/{exchange}/{token}` | Get security information for a symbol |

---

## Get Quotes

| Particular | Details |
| --- | --- |
| API Name | Get Quotes |
| Relative URL | `/quotes/{exchange}/{token}` |
| Method | GET |
| Content-Type | NA |
| Produces | application/json |

### Description

This API provides quotes information for supplied trading symbols.

### Request message format

Create a GET request and put exchange and token in the request URL.

```
e.g. /quotes/NSE/22
```

### Get Quotes Response

| Field | Description |
| --- | --- |
| `average_traded_price` | Average price of the traded quantity |
| `best_ask_orders1` … `best_ask_orders5` | Orders for Best Ask 1–5 |
| `best_ask_price1` … `best_ask_price5` | Best Ask Price 1–5 |
| `best_ask_qty1` … `best_ask_qty5` | Quantity for Best Ask 1–5 |
| `best_bid_orders1` … `best_bid_orders5` | Orders for Best Bid 1–5 |
| `best_bid_price1` … `best_bid_price5` | Best Bid Price 1–5 |
| `best_bid_qty1` … `best_bid_qty5` | Quantity for Best Bid 1–5 |
| `company_name` | Specifies Company name in case of NSE Equity Symbol |
| `day_high` | Day High Price |
| `day_low` | Day Low Price |
| `day_open` | Day Open Price |
| `exchange` | Exchange to which order will be placed |
| `instrument_name` | Instrument name |
| `isin` | ISIN code for the given scrip, in case of Equity Scrips |
| `last_trade_time` | Time for the last executed trade |
| `last_traded_qty` | Quantity for the last executed trade |
| `lotsize` | For Derivatives symbols, specifies its lot size |
| `lower_circuit` | Current Lower Circuit limit for the symbol |
| `ltp` | Specifies the Last Traded Price for that scrip |
| `message` | Shows the status message |
| `multiplier` | Contract price multiplier (used for order value calculation) |
| `price_factor` | Price factor `((GN / GD) * (PN / PD))` |
| `price_precision` | Price Precision |
| `segment` | Specifies Segment, whether equity or derivatives |
| `status` | Shows the status for the request |
| `symbol_name` | Symbol name |
| `ticksize` | Tick size for the mentioned symbol |
| `token` | Unique token ID for each symbol |
| `tradingsymbol` | Trading symbol as per master file |
| `upper_circuit` | Current Upper Circuit limit for the symbol |
| `volume` | Total Volume for the day |

### Response Message Format

```json
{
  "status": "SUCCESS",
  "lotsize": "1",
  "exchange": "NSE",
  "tradingsymbol": "ACC-EQ",
  "company_name": "ACC LIMITED",
  "symbol_name": "ACC",
  "segment": "EQT",
  "instrument_name": "EQ",
  "isin": "INE012A01025",
  "ticksize": "0.05",
  "price_precision": "2",
  "multiplier": "1",
  "upper_circuit": "2165.10",
  "lower_circuit": "1673.05",
  "price_factor": "(1 / 1 ) * (1 / 1)",
  "ltp": "1858.00",
  "day_high": "2008.50",
  "day_low": "1750.00",
  "volume": "4839643",
  "last_traded_qty": "2",
  "last_trade_time": "15:29:59",
  "best_bid_price1": "1858.00",
  "best_ask_price1": "1859.00",
  "best_bid_price2": "1855.00",
  "best_ask_price2": "1859.90",
  "best_bid_price3": "1854.00",
  "best_ask_price3": "1860.00",
  "best_bid_price4": "1853.00",
  "best_ask_price4": "1860.85",
  "best_bid_price5": "1852.60",
  "best_ask_price5": "1862.00",
  "best_bid_qty1": "8",
  "best_ask_qty1": "94",
  "best_bid_qty2": "1",
  "best_ask_qty2": "242",
  "best_bid_qty3": "10",
  "best_ask_qty3": "292",
  "best_bid_qty4": "20",
  "best_ask_qty4": "34",
  "best_bid_qty5": "100",
  "best_ask_qty5": "10",
  "best_bid_orders1": "1",
  "best_ask_orders1": "4",
  "best_bid_orders2": "1",
  "best_ask_orders2": "7",
  "best_bid_orders3": "1",
  "best_ask_orders3": "14",
  "best_bid_orders4": "1",
  "best_ask_orders4": "1",
  "best_bid_orders5": "1",
  "best_ask_orders5": "1",
  "day_open": "1999.50",
  "average_traded_price": "1858.91"
}
```

---

## Security Information

| Particular | Details |
| --- | --- |
| API Name | Security information |
| Relative URL | `/securityinfo/{exchange}/{token}` |
| Method | GET |
| Content-Type | NA |
| Produces | application/json |

### Description

This API provides details about the mentioned security for that token.

### Request message format

Create a GET request and put exchange and token in the request URL.

```
e.g. /securityinfo/NSE/22
```

### Get Security Info Response

| Field | Possible values | Description |
| --- | --- | --- |
| `additional_buy_margin` | | Additional margin for Buy order |
| `additional_sell_margin` | | Additional margin for Sell order |
| `company_name` | | Specifies Company name in case of NSE Equity Symbol |
| `deliveryMargin` | | |
| `deliveryUnits` | | |
| `elmMargin` | | |
| `elm_buy_margin` | | Extreme Loss margin for Buy order |
| `elm_sell_margin` | | Extreme Loss margin for Sell order |
| `exchange` | | Exchange to which order will be placed |
| `exerciseEndDate` | | |
| `exerciseStartDate` | | |
| `expiry` | | For derivatives, specifies expiry of the contract |
| `exposureMargin` | | |
| `freeze_qty` | | Freeze Quantity |
| `instrument_name` | | |
| `isin` | | Specifies ISIN code for the given scrip, in case of Equity Scrips |
| `issueDate` | | |
| `last_trade_date` | | Date for the last executed trade |
| `listingDate` | | |
| `lotsize` | | For Derivatives symbols, specifies its lot size |
| `marketType` | | |
| `message` | | |
| `multiplier` | | Contract price multiplier (used for order value calculation) |
| `nonTradableInstruments` | | |
| `option_strike` | | Option Strike price |
| `option_type` | CE / PE | Option type, whether CE or PE |
| `prcftr_d` | | |
| `priceQuoteQuantity` | | |
| `priceUnit` | | |
| `price_precision` | | Price Precision |
| `requestTime` | | |
| `segment` | | Specifies Segment, whether equity or derivatives |
| `special_buy_margin` | | Special margin for Buy order |
| `special_sell_margin` | | Special margin for Sell order |
| `status` | | Shows the status for the request |
| `symbol_name` | | Specifies Symbol name |
| `tenderEndDate` | | |
| `tenderMargin` | | |
| `tenderStartDate` | | |
| `ticksize` | | Tick size for the mentioned symbol |
| `token` | | Unique token ID for each symbol |
| `tradeUnits` | | |
| `tradingsymbol` | | Trading symbol as per master file |
| `varMargin` | | |
| `weeklyOption` | | |

### Response Message Format

```json
{
  "requestTime": "16:33:33 03-02-2023",
  "status": "SUCCESS",
  "exchange": "NSE",
  "tradingsymbol": "ACC-EQ",
  "company_name": "ACC LIMITED",
  "segment": "EQT",
  "instrument_name": "EQ",
  "ticksize": "0.05",
  "lotsize": "1",
  "price_precision": "2",
  "multiplier": "1",
  "isin": "INE012A01025",
  "freeze_qty": "54270",
  "deliveryMargin": "0.00",
  "varMargin": "20.00",
  "token": "22",
  "prcftr_d": "(1/1)*(1/1)",
  "issueDate": "24-10-1994",
  "listingDate": "01-01-1980"
}
```
