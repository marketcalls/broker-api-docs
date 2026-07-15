# Market Quotes and Instruments

## Endpoints

| Method | Endpoint | Purpose | Limit |
|--------|----------|---------|-------|
| GET | `/instruments` | CSV dump of all instruments | - |
| GET | `/instruments/:exchange` | CSV dump per exchange | - |
| GET | `/quote` | Full market quotes | 500 instruments |
| GET | `/quote/ohlc` | OHLC quotes | 1000 instruments |
| GET | `/quote/ltp` | LTP quotes | 1000 instruments |

## Instruments API

Returns a gzipped CSV dump of all tradable instruments. Generated once daily (last_price not real-time).

### CSV Columns

| Column | Description |
|--------|-------------|
| instrument_token | Numerical ID for WebSocket subscriptions |
| exchange_token | Exchange-issued identifier |
| tradingsymbol | Exchange trading symbol |
| name | Company name (equities) |
| last_price | Last traded price |
| expiry | Expiry date (derivatives) |
| strike | Strike price (options) |
| tick_size | Single price tick value |
| lot_size | Quantity per lot |
| instrument_type | EQ, FUT, CE, PE |
| segment | Instrument segment |
| exchange | Exchange name |

**Key:** Use combination of `exchange` and `tradingsymbol` as unique key, not `instrument_token`.

## Full Market Quotes

```
GET https://api.kite.trade/quote?i=NSE:INFY&i=BSE:SENSEX
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| instrument_token | int | Exchange identifier |
| timestamp | string | Exchange timestamp |
| last_trade_time | string | Last trade timestamp |
| last_price | float | Last traded price |
| volume | int | Volume traded today |
| average_price | float | VWAP |
| buy_quantity | int | Pending buy quantity |
| sell_quantity | int | Pending sell quantity |
| open_interest | int | Outstanding contracts (F&O) |
| last_quantity | int | Last traded quantity |
| ohlc | object | open, high, low, close |
| net_change | float | Change from previous close |
| lower_circuit_limit | float | Lower circuit |
| upper_circuit_limit | float | Upper circuit |
| depth | object | Buy/sell market depth (5 levels) |

## OHLC Quotes

Returns `instrument_token`, `last_price`, and `ohlc` object.

## LTP Quotes

Returns `instrument_token` and `last_price`.

**Note:** Always check for key existence in response (e.g., `NSE:INFY`).
