# Funds & Margin

All APIs require the request header:

```
Authorization: <api_session_key>
```

| Method | Relative URL | Description |
| --- | --- | --- |
| GET | `/limits` | Get limits across segments |
| POST | `/margin` | Get order margin for a basket |
| POST | `/spancalculator` | Get span margin information |

---

## Limits

| Particular | Details |
| --- | --- |
| API Name | Get Limits |
| Relative URL | `/limits` |
| Method | GET |
| Content-Type | NA |
| Produces | application/json |

### Description

This API provides limits across the segments.

### Request message format

NA

### Limit Response (key fields)

| Field | Description |
| --- | --- |
| `status` | Shows the status for the request |
| `cash` | Available cash |
| `payin` | Pay-in amount |
| `payout` | Pay-out amount |
| `brokerCollateralAmount` | Broker collateral amount |
| `unClearedCash` | Uncleared cash |
| `dayCash` | Day cash |
| `turnOverLimit` | Turnover limit |
| `pendordvallmt` | Pending order value limit |
| `marginUsed` | Total margin used |
| `collateral` | Collateral value |
| `premium` | Premium |
| `span` | Span margin |
| `exposureMargin` | Exposure margin |

> The full response can contain a large set of additional fields, including (non-exhaustive):
> `CACBuyUsed`, `CACSellCredits`, `additionalScripBasketMargin` (and its Commodity/Derivative/FX Intraday/Margin variants),
> `brokerage` (and its Commodity/Derivative/Equity/FX × BracketOrder/HighLeverage/Intraday/Margin/CAC variants),
> `currentRealizedPNL` and `currentUnrealizedMTOM` (and their per-segment variants), `currentUnrealizedMtom`,
> `exposureMargin` (per-segment variants), `grcoll`, `grossExposure`, `grossExposureDerivative`,
> `marginProduct` (per-segment BracketOrder/HighLeverage variants), `message`, `mtomCurrentPercentage`,
> `optionPremium` (per-segment variants), `peakMarginUsedByClient`, `pendordval`, `product`, `requestTime`,
> `scripBasketMargin` (per-segment variants), `segment`, `spanMargin` (per-segment variants),
> `turnover`, `varElm` (per-segment variants), and `exchange`.

### Response Message Format

```json
{
  "status": "SUCCESS",
  "cash": "2500000.00",
  "payin": "0.00",
  "payout": "0.0",
  "brokerCollateralAmount": "0.00",
  "unClearedCash": "0.00",
  "dayCash": "0.00",
  "turnOverLimit": "750000000.00",
  "pendordvallmt": "450000000.00"
}
```

---

## Get Margin

| Particular | Details |
| --- | --- |
| API Name | Get Order Margin |
| Relative URL | `/margin` |
| Method | POST |
| Content-Type | application/json |
| Produces | application/json |

### Description

This API provides the margin required for multiple orders. If multiple orders are required to be placed, use this API and pass information about trading symbols for which orders are to be placed.

### Basket Margin Request

| Field | Possible values | Description |
| --- | --- | --- |
| `basketlists` | | Refer to the **Basket Margin Item Request** table below |
| `exchange` | | Exchange to which order will be placed |
| `order_type` | BUY / SELL | Order type BUY/SELL |
| `price` | | Price to place the order (0 in case of `price_type = MARKET`) |
| `price_type` | LIMIT / MARKET / SL-LIMIT / SL-MARKET | Price type for order |
| `product_type` | CNC / INTRADAY / NORMAL | Product type |
| `quantity` | | Order quantity (in multiples of lots for derivatives) |
| `tradingsymbol` | | Trading symbol as per master file |
| `trigger_price` | | Price at which the order should be triggered (only for `price_type = SL-LIMIT` or `SL-MARKET`) |

### Basket Margin Item Request

| Field | Possible values | Description |
| --- | --- | --- |
| `book_loss_price` | | Stoploss price. Applicable only for Bracket orders |
| `exchange` | | Exchange to which order will be placed |
| `filled_qty` | | Total Traded / filled quantity |
| `order_id` | | Shows Order ID |
| `order_type` | BUY / SELL | Order type BUY/SELL |
| `price` | | Price to place the order (0 in case of `price_type = MARKET`) |
| `price_type` | LIMIT / MARKET / SL-LIMIT / SL-MARKET | Price type for order |
| `product_type` | CNC / INTRADAY / NORMAL | Product type |
| `quantity` | | Order quantity (in multiples of lots for derivatives) |
| `tradingsymbol` | | Trading symbol as per master file |
| `trigger_price` | | Price at which the order should be triggered (only for `price_type = SL-LIMIT` or `SL-MARKET`) |

### Basket Margin Response

| Field | Description |
| --- | --- |
| `status` | Place order success or failure indication |
| `requestTime` | Response received time |
| `remarks` | This field will contain rejection reason |
| `newTotalMarginUsed` | Total margin used |
| `newMarginUsedAfterTrade` | Margin used after trade |
| `errorMessage` | Present only if order placement fails |
| `marginUsed` | Margin used for this basket |

### Request Message Format

```json
{
  "basketlists": [
    {
      "exchange": "NFO",
      "tradingsymbol": "NIFTY23FEB23F",
      "quantity": "50",
      "price": "18000",
      "product_type": "INTRADAY",
      "order_type": "BUY",
      "price_type": "LIMIT"
    }
  ]
}
```

### Response Message Format

```json
{
  "status": "SUCCESS",
  "remarks": "",
  "newTotalMarginUsed": "109263.47",
  "newMarginUsedAfterTrade": "113898.47",
  "marginUsed": "9056.27"
}
```

---

## Span Calculator

| Particular | Details |
| --- | --- |
| API Name | Span calculator |
| Relative URL | `/spancalculator` |
| Method | POST |
| Content-Type | application/json |
| Produces | application/json |

### Description

This API provides span information for supplied trading symbols.

### Span Calculator Request Item

| Field | Possible values | Description |
| --- | --- | --- |
| `exchange` | | Specifies the Exchange for your tradingsymbol |
| `expiry` | | For derivatives, specifies expiry of the contract |
| `net_qty` | | Net Traded quantity |
| `open_buy_qty` | | Open buy quantity |
| `open_sell_qty` | | Open sell quantity |
| `option_strike` | | Option Strike price |
| `option_type` | CE / PE | Option type, whether CE or PE |
| `product_type` | CNC / INTRADAY / NORMAL | Product type |
| `symbol_name` | | Symbol name |
| `tradingsymbol` | | Specifies the trading symbol |

### Span Calculator Response

| Field | Description |
| --- | --- |
| `exposure` | Exposure Margin |
| `exposureTrade` | |
| `message` | Shows the status message |
| `request_time` | |
| `span` | Span Margin |
| `spanTrade` | |
| `status` | Shows the status for the request |

### Request Message Format

```json
{
  "positions": [
    {
      "product_type": "NORMAL",
      "exchange": "NFO",
      "symbol_name": "NIFTY",
      "tradingsymbol": "NIFTY23FEB2317700C",
      "expiry": "23-FEB-2023",
      "open_sell_qty": 100,
      "open_buy_qty": 0,
      "option_strike": "17700",
      "option_type": "CE"
    },
    {
      "product_type": "NORMAL",
      "exchange": "NFO",
      "symbol_name": "NIFTY",
      "tradingsymbol": "NIFTY23FEB2317700P",
      "expiry": "23-FEB-2023",
      "open_sell_qty": 100,
      "open_buy_qty": 0,
      "option_strike": "17700",
      "option_type": "PE"
    }
  ]
}
```

### Response Message Format

```json
{
  "status": "SUCCESS",
  "span": "328482.00",
  "exposure": "70660.00",
  "spanTrade": "328482.00",
  "exposureTrade": "70660.00",
  "request_time": "19:08:56 01-02-2023"
}
```
