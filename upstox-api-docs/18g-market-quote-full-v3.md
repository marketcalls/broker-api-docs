# Full Market Quotes V3

## Overview

API to retrieve the full market quotes for one or more instruments. Provides the complete market data snapshot of up to 500 instruments in one go. These snapshots are obtained directly from the exchanges at the time of request.

## Endpoint

**GET** `https://api.upstox.com/v3/market-quote/quotes`

## Closing Auction Session (CAS)

The headline addition in V3 is live Closing Auction Session (CAS) data:

| Field | Description |
| --- | --- |
| indicative_equilibrium_price (IEP) | The specific price at which the maximum possible number of shares can be matched based on the current order book. |
| indicative_equilibrium_quantity (IEQ) | The exact total number of shares that will successfully execute at the calculated IEP. |
| indicative_imbalance_quantity_total | The net excess buy or sell quantity that remains unmatched at the IEP. |
| indicative_imbalance_quantity_market | The portion of that unmatched total quantity that originates exclusively from unpriced market orders. |
| reference_price | The base price used to calculate the symbol's applicable price bands and circuit filters for the session. |
| cas_eligible | Whether the symbol is permitted to participate in any Call Auction Session. |

See [Order Flow for CAS-Eligible Securities](https://upstox.com/developer/api-documentation/announcements/closing-auction-session#order-flow-for-cas-eligible-securities) for the CAS session timings.

V3 also adds four fields available throughout the session, plus two inside `ohlc` :

| Field | Description |
| --- | --- |
| prev_close_price | The close price from the previous session of trading. |
| year_high and year_low | The price range over the trailing year. |
| previous_oi | The open interest from the previous session, for F&O instruments. |
| volume and ts (inside ohlc) | The candle volume and the candle's start time. |

## New Instruments

- **Global Index** — Major global stock market indices such as GIFT NIFTY, Dow Jones, S&P, FTSE 100, and more. See [Global Instruments](https://upstox.com/developer/api-documentation/instruments#global-instruments) for details and download the [Global Instruments file](https://assets.upstox.com/market-quote/instruments/exchange/global.json.gz) for instrument keys.
- **India VIX** — The NSE Volatility Index, available using instrument key `NSE_INDEX|India VIX` .

## Query Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| instrument_key | Required | string | Comma separated list of instrument keys, up to a maximum of 500. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern) . |

## Response

```json
{
  "status": "success",
  "data": {
    "NSE_EQ:NHPC": {
      "ohlc": {
        "open": 76.1,
        "high": 77.25,
        "low": 75.95,
        "close": 76.59,
        "volume": 24123697,
        "ts": 1757000100000
      },
      "depth": {
        "buy": [
          {
            "quantity": 6917,
            "price": 76.55,
            "orders": 20
          },
          {
            "quantity": 0,
            "price": 0,
            "orders": 0
          }
        ],
        "sell": [
          {
            "quantity": 0,
            "price": 0,
            "orders": 0
          },
          {
            "quantity": 0,
            "price": 0,
            "orders": 0
          }
        ]
      },
      "timestamp": "2026-09-04T15:22:31.099+05:30",
      "instrument_token": "NSE_EQ|INE848E01016",
      "symbol": "NHPC",
      "last_price": 76.58999633789062,
      "volume": 24123697,
      "average_price": 76.42,
      "oi": 0,
      "net_change": 0.79,
      "total_buy_quantity": 6917,
      "total_sell_quantity": 0,
      "lower_circuit_limit": 60.64,
      "upper_circuit_limit": 90.96,
      "last_trade_time": "1757000551130",
      "oi_day_high": 0,
      "oi_day_low": 0,
      "prev_close_price": 75.8,
      "year_high": 118.35,
      "year_low": 46.6,
      "previous_oi": 0,
      "indicative_equilibrium_price": 76.65,
      "reference_price": 75.8,
      "indicative_equilibrium_quantity": 9800,
      "indicative_imbalance_quantity_total": 2500,
      "indicative_imbalance_quantity_market": 500,
      "cas_eligible": true
    }
  }
}
```

The `data` object is keyed by `<EXCHANGE>:<TRADING_SYMBOL>` , for example `NSE_EQ:NHPC` . For index instruments the key is the instrument key with the pipe replaced by a colon, for example `NSE_INDEX:Nifty 50` .

| Name | Type | Description |
| --- | --- | --- |
| status | string | A string indicating the outcome of the request. Typically `success` for successful operations. |
| data | object | Data object holding full market quote information |
| data.ohlc | object | Data object with OHLC information |
| data.ohlc.open | number | The open price of the trading session |
| data.ohlc.high | number | The high price of the trading session |
| data.ohlc.low | number | The low price of the trading session |
| data.ohlc.close | number | The close price of the trading session |
| data.ohlc.volume | integer | The volume traded during the candle |
| data.ohlc.ts | integer | Starting timestamp of candle, in milliseconds |
| data.depth | object | Data object with top 5 buy and sell depth information |
| data.depth.buy | object[] | Bids |
| data.depth.buy[].quantity | integer | quantity |
| data.depth.buy[].price | number | price |
| data.depth.buy[].orders | integer | orders |
| data.depth.sell | object[] | Asks |
| data.depth.sell[].quantity | integer | quantity |
| data.depth.sell[].price | number | price |
| data.depth.sell[].orders | integer | orders |
| data.timestamp | string | The time at which the response was generated, as an ISO 8601 timestamp with offset |
| data.instrument_token | string | Key of the instrument. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern) . |
| data.symbol | string | Shows the trading symbol of the instrument |
| data.last_price | number | The last traded price of symbol |
| data.volume | integer | The volume traded today on symbol |
| data.average_price | number | Average price |
| data.oi | number | Total number of outstanding contracts held by market participants exchange-wide (only F&O) |
| data.net_change | number | The absolute change from yesterday's close to last traded price |
| data.total_buy_quantity | number | The total number of bid quantity available for trading |
| data.total_sell_quantity | number | The total number of ask quantity available for trading |
| data.lower_circuit_limit | number | The lower circuit of symbol |
| data.upper_circuit_limit | number | The upper circuit of symbol |
| data.last_trade_time | string | Time in milliseconds at which last trade happened |
| data.oi_day_high | number | The highest open interest recorded on symbol during the day |
| data.oi_day_low | number | The lowest open interest recorded on symbol during the day |
| data.prev_close_price | number | The close price of the symbol from the previous session of trading |
| data.year_high | number | The highest price of the symbol over the trailing year |
| data.year_low | number | The lowest price of the symbol over the trailing year |
| data.previous_oi | number | The open interest of the symbol from the previous session (only F&O) |
| data.indicative_equilibrium_price | number | The specific price at which the maximum possible number of shares can be matched based on the current order book |
| data.reference_price | number | The base price used to calculate the applicable price bands and circuit filters for the session |
| data.indicative_equilibrium_quantity | integer | The exact total number of shares that will successfully execute at the calculated indicative equilibrium price |
| data.indicative_imbalance_quantity_total | integer | The net excess buy or sell quantity that remains unmatched at the indicative equilibrium price |
| data.indicative_imbalance_quantity_market | integer | The portion of that unmatched total quantity that originates exclusively from unpriced market orders |
| data.cas_eligible | boolean | Whether the symbol is permitted to participate in any Call Auction Session |

## Error Codes

| Error code | Description |
| --- | --- |
| UDAPI1009 | **symbol is required** - The `instrument_key` parameter is missing. |
| UDAPI1011 | **symbol is of invalid format** - The provided `instrument_key` does not conform to the accepted format. |
| UDAPI100011 | **Invalid Instrument key** - The provided `instrument_key` is invalid. |
| UDAPI100095 | **Invalid Instrument key** - The provided `instrument_key` is not accepted on this endpoint. |
| UDAPI100042 | **Data of only 500 instrument keys can be requested in single API call** - Limit your request to 500 instrument keys at a time. |
